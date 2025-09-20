# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

CWD:=$(shell realpath $(dir $(lastword $(MAKEFILE_LIST))))

CHANGELOG:=$(CWD)/CHANGELOG.md

UV_INSTALL_URL:=https://astral.sh/uv/install.sh

# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------

UV ?= uv

RM ?= rm

RMDIR ?= rm -r

PIP ?= $(UV) pip

MKDIR ?= mkdir -p

PYTHON ?= $(UV) run python

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

SVG_DIR ?= $(CWD)/images

BUILD_DIR ?= $(CWD)/dist

SOURCE_DIR ?= $(CWD)/src

ASSETS_DIR ?= $(CWD)/assets

WORKRUN_DIR ?= $(CWD)/workrun

CLEAN_ARTIFACTS ?= $(SVG_DIR) $(BUILD_DIR) $(WORKRUN_DIR)

CHANGELOG_BIN ?= git-cliff

CHANGELOG_CONFIG ?= cliff.toml

CHANGELOG_FLAGS ?= \
	--workdir $(CWD) \
	--output $(CHANGELOG) \
	--config $(CHANGELOG_CONFIG)


# -----------------------------------------------------------------------------
# Options
# -----------------------------------------------------------------------------

VERBOSE ?=

# -----------------------------------------------------------------------------
# Options appliance
# -----------------------------------------------------------------------------

ifneq ($(VERBOSE),)
	HIDE =
else
	HIDE = @
endif

# -----------------------------------------------------------------------------
# I/O Utilities
# -----------------------------------------------------------------------------

RESET:=\033[0;30m

define RED
    $(2)$(HIDE)echo -n "\033[0;31m$(1)$(RESET)"
endef

define BLUE
    $(2)$(HIDE)echo -n "\033[0;34m$(1)$(RESET)"
endef

define CYAN
    $(2)$(HIDE)echo -n "\033[0;36m$(1)$(RESET)"
endef

define GREEN
    $(2)$(HIDE)echo -n "\033[0;32m$(1)$(RESET)"
endef

define YELLOW
    $(2)$(HIDE)echo -n "\033[0;33m$(1)$(RESET)"
endef

define MAGENTA
    $(2)$(HIDE)echo -n "\033[0;35m$(strip $(1))$(RESET)"
endef

define CONFIRM
	echo -n "Do you accept? \(y/n\) [n] "; read ans; if [ $${ans:-N} != y ]; then \
		exit 0; \
	fi
endef

# -----------------------------------------------------------------------------
# Targets
# -----------------------------------------------------------------------------

.PHONY: \
	uv \
	all \
	sync \
	lint \
	help \
	test \
	build \
	clean \
	format \
	default \
	publish \
	changelog \
	export_svg


all default: help

uv: ## Install 'uv' on the user, if it isn't already installed
	$(HIDE)$(UV) > /dev/null -h 2>&1 || curl -LsSf  $(UV_INSTALL_URL) | sh

help: ## Prints help for targets with comments
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

sync: uv ## Refresh, sync and upgrade project dependencies (including 'dev')
	$(HIDE)$(UV) sync --dev --refresh --upgrade --all-extras --all-groups --managed-python

lint: uv ## Lint project python code and apply auto fixes if possible
	$(HIDE)$(UV) run ruff check --fix

test: uv ## Run project tests
	$(HIDE)$(UV) run pytest

build: clean sync lint format test changelog export_svg ## Build wheel and sdist targets of the project for publish
	$(HIDE)$(UV) build --refresh --upgrade --sdist --wheel
	$(HIDE)/usr/bin/env -S \
		PYAPP_UV_ENABLED=1 \
		PYAPP_PROJECT_PATH=$$(realpath ./dist/*.whl) \
		$(UV) run hatch build -t binary

clean: ## Remove all auto generated artifacts (e.g. build artifacts)
	$(HIDE)$(RMDIR) $(CLEAN_ARTIFACTS) 2> /dev/null || exit 0

format: uv ## Run ruff formatter on project source code
	$(HIDE)$(UV) run ruff format

publish: build ## Publish project to private devpi index
	$(HIDE)devpi upload --verbose --no-vcs --only-latest --from-dir $(BUILD_DIR)

changelog: ## Update the project's CHANGELOG.md from the git commit log
	$(HIDE)$(CHANGELOG_BIN) $(CHANGELOG_FLAGS)

export_svg: uv sync $(SVG_DIR) ## Export help menus of all 'socx [subcmd]' commands as svg images
	$(HIDE)$(UV) run rich-click -o svg socx -- socx -h > images/socx-cli.svg &
	$(HIDE)$(UV) run rich-click -o svg socx -- socx git -h > images/socx-git.svg &
	$(HIDE)$(UV) run rich-click -o svg socx -- socx rgr -h > images/socx-rgr.svg &
	$(HIDE)$(UV) run rich-click -o svg socx -- socx config -h > images/socx-config.svg &
	$(HIDE)$(UV) run rich-click -o svg socx -- socx plugin -h > images/socx-plugin.svg &
	$(HIDE)$(UV) run rich-click -o svg socx -- socx convert -h > images/socx-convert.svg &

$(SVG_DIR):
	$(HIDE)$(MKDIR) $(SVG_DIR)
