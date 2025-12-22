# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

.DEFAULT_GOAL := help

CWD := $(shell realpath $(dir $(lastword $(MAKEFILE_LIST))))

CHANGELOG := $(CWD)/CHANGELOG.md

UV_INSTALL_URL := https://astral.sh/uv/install.sh

# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------

UV := uv

RM := rm

PIP := $(UV) pip

RMDIR := rm -r

MKDIR := mkdir -p

PYTHON := $(UV) run python

PUBLISHER := devpi

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

VERBOSE ?=

SVG_DIR ?= $(CWD)/docs/assets/images

SITE_DIR ?= $(CWD)/site

BUILD_DIR ?= $(CWD)/dist

SOURCE_DIR ?= $(CWD)/src

ASSETS_DIR ?= $(CWD)/assets

WORKRUN_DIR ?= $(CWD)/workrun

CACHE_DIRS ?= $(wildcard $(CWD)/.*cache)

COVERAGE_DIRS ?= $(CWD)/htmlcov $(CWD)/.coverage*

CHANGELOG_BIN ?= git-cliff

CHANGELOG_CONFIG ?= cliff.toml

CHANGELOG_FLAGS ?= \
	--workdir $(CWD) \
	--output $(CHANGELOG) \
	--config $(CHANGELOG_CONFIG)

CLEAN_ARTIFACTS ?= \
	$(SITE_DIR) \
	$(BUILD_DIR) \
	$(CACHE_DIRS) \
	$(WORKRUN_DIR) \
	$(COVERAGE_DIRS)

# -----------------------------------------------------------------------------
# Options appliance
# -----------------------------------------------------------------------------

ifeq ($(VERBOSE),)
	HIDE = @
else
	HIDE =
endif

# -----------------------------------------------------------------------------
# Goals
# -----------------------------------------------------------------------------

.PHONY: \
	uv \
	sync \
	help \
	docs \
	test \
	setup \
	build \
	clean \
	check \
	format \
	release \
	publish \
	coverage \
	changelog \
	check_api \
	check_code \
	check_docs \
	check_types \
	docs_deploy \
	export_svg

uv: ## Install 'uv' on the user, if it isn't already installed
	$(HIDE)$(UV) > /dev/null -h 2>&1 || curl -LsSf  $(UV_INSTALL_URL) | sh

help: ## Prints help for targets with comments
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

sync: uv ## Refresh, sync and upgrade project dependencies (including 'dev')
	$(HIDE)$(UV) sync --dev --refresh --upgrade --all-extras --all-groups --managed-python

docs: uv ## Serve project documentation at http://127.0.0.1:8000
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

test: uv ## Run project tests
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

check: uv ## Run all checks
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

setup: ## Set up the project
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

build: clean sync check_code format changelog ## Build wheel and sdist targets of the project for publish
	$(HIDE)$(UV) build --refresh --upgrade --sdist --wheel
	$(HIDE)/usr/bin/env -S \
		PYAPP_UV_ENABLED=1 \
		PYAPP_PROJECT_PATH=$$(realpath ./dist/*.whl) \
		$(UV) run hatch build -t binary

clean: ## Remove all auto generated artifacts (e.g. build artifacts)
	$(HIDE)$(RMDIR) $(CLEAN_ARTIFACTS) 2> /dev/null || exit 0
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

format: uv ## Run ruff formatter on project source code
	$(HIDE)$(UV) run ruff format $(CWD)/src

release: uv ## Release a new package version to github
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

publish: build ## Publish project to private devpi index
	$(HIDE)$(PUBLISHER) upload \
		--verbose --no-vcs --only-latest --wheel $(wildcard $(BUILD_DIR)/*.whl)

coverage: uv ## Report coverage as text and HTML
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

changelog: ## Update the project's CHANGELOG.md from the git commit log
	$(HIDE)$(CHANGELOG_BIN) $(CHANGELOG_FLAGS)

check_api: uv ## Check API for breaking changes.
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

check_code: uv ## Lint project code and auto apply fixes if possible
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

check_docs: uv ## Check that project documentation builds correctly
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

check_types: uv ## Check that code is properly typed
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"

docs_deploy: uv ## Deploy documentation to GitHub Pages
	$(HIDE)$(UV) run $(CWD)/scripts/make.py "$@"
	$(HIDE)$(MAKE) clean

export_svg: uv ## Export help menus of all socx commands as svg images
	$(HIDE)$(MKDIR) $(SVG_DIR)
	$(HIDE)-$(RMDIR) $(SVG_DIR)/socx-*.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx --help" $(SVG_DIR)/socx-cli.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx git --help" $(SVG_DIR)/socx-git.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx git help" $(SVG_DIR)/socx-git-help.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx git log -r .." $(SVG_DIR)/socx-git-log.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx git diff -r .." $(SVG_DIR)/socx-git-diff.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx git fetch -r .." $(SVG_DIR)/socx-git-fetch.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx git status -r .." $(SVG_DIR)/socx-git-status.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx git summary -r .." $(SVG_DIR)/socx-git-summary.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config dump plugins.git" $(SVG_DIR)/socx-git-plugin.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx rgr --help" $(SVG_DIR)/socx-rgr.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx rgr run $(CWD)/assets/rgr/inputs/tiny" $(SVG_DIR)/socx-rgr-run.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config --help" $(SVG_DIR)/socx-config.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config get plugins" $(SVG_DIR)/socx-config-get.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config dump plugins" $(SVG_DIR)/socx-config-dump.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config tree" $(SVG_DIR)/socx-config-tree.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config list" $(SVG_DIR)/socx-config-list.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config debug" $(SVG_DIR)/socx-config-debug.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config inspect" $(SVG_DIR)/socx-config-debug.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config dump plugins.config" $(SVG_DIR)/socx-config-plugin.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx plugin --help" $(SVG_DIR)/socx-plugin.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx plugin schema" $(SVG_DIR)/socx-plugin-schema.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx plugin example" $(SVG_DIR)/socx-plugin-example.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx config dump plugins.plugin" $(SVG_DIR)/socx-plugin-plugin.svg
	$(HIDE)$(UV) run termtosvg -D 3000 -m 100 -M 1000000 -t base16_default_dark -c "socx convert --help" $(SVG_DIR)/socx-convert.svg
