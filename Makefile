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
	cwd \
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


all default: build

uv:
	$(HIDE)$(UV) > /dev/null -h 2>&1 || curl -LsSf  $(UV_INSTALL_URL) | sh

sync: uv
	$(HIDE)$(UV) sync --dev --refresh --upgrade

lint: uv
	$(HIDE)$(UV) run ruff check --fix

test: uv
	$(HIDE)$(UV) run pytest

build: clean sync lint format test changelog export_svg
	$(HIDE)$(UV) build --refresh --upgrade --sdist --wheel

clean:
	$(HIDE)$(RMDIR) $(CLEAN_ARTIFACTS) 2> /dev/null || exit 0

format: uv
	$(HIDE)$(UV) run ruff format

publish: build
	$(HIDE)devpi upload --verbose --no-vcs --only-latest --from-dir $(BUILD_DIR)

changelog:
	$(HIDE)$(CHANGELOG_BIN) $(CHANGELOG_FLAGS)

export_svg: uv sync $(SVG_DIR)
	$(HIDE)$(UV) run rich-click -o svg socx.cli.cli:cli -- -h > images/socx-cli.svg &
	$(HIDE)$(UV) run rich-click -o svg socx.cli.cli:cli -- git -h > images/socx-git.svg &
	$(HIDE)$(UV) run rich-click -o svg socx.cli.cli:cli -- rgr -h > images/socx-rgr.svg &
	$(HIDE)$(UV) run rich-click -o svg socx.cli.cli:cli -- config -h > images/socx-config.svg &
	$(HIDE)$(UV) run rich-click -o svg socx.cli.cli:cli -- plugin -h > images/socx-rgr.svg &
	$(HIDE)$(UV) run rich-click -o svg socx.cli.cli:cli -- convert -h > images/socx-convert.svg &

$(SVG_DIR):
	$(HIDE)$(MKDIR) $(SVG_DIR)
