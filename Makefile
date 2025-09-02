# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------

UV ?= uv

RM ?= rm -r

PIP ?= uv pip

MKDIR ?= mkdir -p

PYTHON ?= uv run python

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

CWD:=$(realpath $(dir $(lastword $(MAKEFILE_LIST))))

CHANGELOG ?= $(CWD)/CHANGELOG.md

COMMIT_CONVENTION ?= angular

SVG_DIR ?= $(CWD)/images

BUILD_DIR ?= $(CWD)/dist

SOURCE_DIR ?= $(CWD)/src

ASSETS_DIR ?= $(CWD)/assets

WORKRUN_DIR ?= $(CWD)/workrun

CLEAN_ARTIFACTS ?= $(SVG_DIR) $(BUILD_DIR) $(WORKRUN_DIR)

UV_INSTALL_URL:=https://astral.sh/uv/install.sh


# -----------------------------------------------------------------------------
# Options
# -----------------------------------------------------------------------------

VERBOSE=true

# -----------------------------------------------------------------------------
# Options appliance
# -----------------------------------------------------------------------------

ifeq ($(VERBOSE),true)
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
	all \
	uv \
	cwd \
	sync \
	lint \
	test \
	build \
	clean \
	format \
	publish \
	changelog \
	export_svg


all: build
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
	$(HIDE)$(RM) $(CLEAN_ARTIFACTS) 2> /dev/null || exit 0

format: uv
	$(HIDE)$(UV) run ruff format

publish: build
	$(HIDE)devpi upload --verbose --no-vcs --only-latest $(BUILD_DIR)

changelog: $(CHANGELOG)
	$(HIDE)$(UV) run --with git-changelog python -m git_changelog \
		--convention $(COMMIT_CONVENTION) \
		--input $(CHANGELOG) \
		--output $(CHANGELOG) \
		--trailers

$(CHANGELOG):
	$(HIDE)$(UV) run --with git-changelog python -m git_changelog \
		--convention $(COMMIT_CONVENTION) \
		--output $(CHANGELOG) \
		--trailers

export_svg: uv sync $(SVG_DIR)
	$(HIDE)uv run rich-click -o svg socx.cli.cli:cli -- -h > images/socx-cli.svg &
	$(HIDE)uv run rich-click -o svg socx.cli.cli:cli -- git -h > images/socx-git.svg &
	$(HIDE)uv run rich-click -o svg socx.cli.cli:cli -- rgr -h > images/socx-rgr.svg &
	$(HIDE)uv run rich-click -o svg socx.cli.cli:cli -- config -h > images/socx-config.svg &
	$(HIDE)uv run rich-click -o svg socx.cli.cli:cli -- plugin -h > images/socx-rgr.svg &
	$(HIDE)uv run rich-click -o svg socx.cli.cli:cli -- convert -h > images/socx-convert.svg &

$(SVG_DIR):
	$(HIDE)$(MKDIR) $(SVG_DIR)
