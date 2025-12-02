---
title: Configuration Reference
description: Complete reference for all SoCX configuration options organized by category.
---

# Configuration Reference

This page documents all available configuration options in SoCX, organized by category. All settings can be overridden via user config (`~/.config/socx/socx.yaml`), repository config (`.socx.yaml`), or environment variables.

## CLI Configuration

Controls command-line interface behavior and global options.

```yaml
cli:
  # Enable debug logging (also: SOCX_CLI__DEBUG=1)
  debug: false
  
  # Load user/repository configuration files
  configure: true
  
  # Logging verbosity level
  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
  verbosity: INFO
  
  # Context settings for Click commands
  context_settings:
    help_option_names:
      - -h
      - --help
  
  # Option panel configuration for help display
  option-panels:
    - name: Options
      options:
        - --help
        - --configure/--no-configure
        - --debug
        - --verbosity
```

### Environment Variables

- `SOCX_CLI__DEBUG=1` - Enable debug mode
- `SOCX_CLI__VERBOSITY=DEBUG` - Set log level
- `SOCX_CLI__CONFIGURE=false` - Disable config loading

## Git Configuration

Settings for Git repository management and manifest generation.

```yaml
git:
  manifest:
    # Root directory to start scanning for repositories
    root: ~
    
    # Paths to include (glob patterns supported)
    includes: []
    
    # Paths to exclude (glob patterns supported)
    excludes: []
    
    # Reference mapping for specific repositories
    references: {}
  
  log:
    # Git log command flags
    flags:
      - --graph
      - --branches
      - --abbrev-commit
      - --date=relative
      - --decorate=full
      - --max-count=12
      - "--pretty=format: %C(red)%h%C(reset) %<(72,trunc)%s %C(bold blue)[%an]%C(reset) %C(yellow)%d%C(reset)%n"
  
  pull:
    # Git pull command flags
    flags:
      - --tags
      - --no-edit
      - --autostash
  
  diff:
    # Git diff command flags
    flags:
      - -M
      - -C
      - -B
      - --ignore-blank-lines
      - --default-prefix
  
  status:
    # Git status command flags
    flags:
      - --short
      - --branch
      - --renames
      - --ahead-behind
  
  summary:
    # Output format: table, json, ref
    format: table
    
    # Table styling
    style:
      headers: ~
    
    table:
      # Box style for table borders
      box: ROUNDED
      title: ~
      caption: ~
      expand: true
      highlight: true
      show_lines: true
      show_header: true
      show_footer: false
    
    # Columns to display in manifest table
    columns:
      - name: Repository
        func: socx_plugins.git.utils:get_repo_name
        style: bright_blue
      
      - name: "[green]Ahead[/] [red]Behind[/]"
        func: socx_plugins.git.utils:get_ahead_behind
        style: ~
      
      - name: Branch / Tag
        func: socx_plugins.git.utils:get_ref_name
        style: yellow
      
      - name: Commit Hash
        func: socx_plugins.git.utils:get_commit_hash
        style: red
      
      - name: Commit Message
        func: socx_plugins.git.utils:get_commit_message
        style: white
      
      - name: Author Name
        func: socx_plugins.git.utils:get_author_name
        style: cyan
      
      - name: Author Date
        func: socx_plugins.git.utils:get_author_date
        style: cyan
```

### Environment Variables

- `SOCX_GIT__MANIFEST__ROOT=~/workspace` - Set manifest root
- `SOCX_GIT__SUMMARY__FORMAT=json` - Set output format

## Regression Configuration

Settings for parallel test execution and regression automation.

```yaml
regression:
  # Working directory for regression operations
  path: ~
  
  # Custom test wrapper class (advanced)
  # Must inherit from socx.regression.test:Test
  test_cls: "socx.regression.test:Test"
  
  # Maximum number of tests to run concurrently
  # Default: 10
  max_runs_in_parallel: 10
  
  run:
    input:
      # Default input filename
      filename: small
      
      # Directory containing test command files
      # Supports @path and @format directives
      directory: "@path @format ./assets/rgr/inputs"
    
    output:
      # Directory for result logs (timestamped subdirs created automatically)
      # Supports @path directive
      directory: "@path workrun/regression"
```

### Environment Variables

- `SOCX_REGRESSION__MAX_RUNS_IN_PARALLEL=20` - Set parallelism
- `SOCX_REGRESSION__RUN__INPUT__FILENAME=failed.log` - Set input file
- `SOCX_REGRESSION__RUN__OUTPUT__DIRECTORY=/tmp/results` - Set output directory

### Parallel Execution Tuning

| Scenario | Recommended Value |
|----------|-------------------|
| CPU-bound tests | Number of CPU cores (4-8) |
| I/O-bound tests | 2-3x CPU cores (16-24) |
| Memory-intensive tests | Conservative (5-10) |
| Quick unit tests | Aggressive (30-50) |
| CI/CD environment | Moderate (10-20) |

## Plugin Configuration

Plugin metadata and registration settings.

```yaml
plugins:
  # Built-in git plugin
  - name: git
    panel: Commands
    help: Various common git command utilities to manage your environment.
    command: "socx_plugins.git:cli"
    enabled: true
    aliases: []
  
  # Built-in regression plugin
  - name: rgr
    panel: Commands
    help: Perform various regression related actions.
    command: "socx_plugins.rgr:cli"
    enabled: true
    aliases: []
  
  # Built-in plugin management
  - name: plugin
    help: Add, create, inspect, and manage extension plugins.
    panel: Commands
    command: "socx_plugins.plugin:cli"
    enabled: true
    aliases: []
  
  # Built-in config management
  - name: config
    help: Get, set, list, or modify settings configuration values.
    panel: Commands
    command: "socx_plugins.config:cli"
    enabled: true
    aliases: []
  
  # Built-in convert plugin
  - name: convert
    help: Perform a conversion based on current configurations.
    panel: Commands
    command: "socx_plugins.convert:cli"
    enabled: true
    aliases: []
  
  # Built-in version plugin
  - name: version
    help: Print version information and exit.
    panel: Commands
    command: "socx_plugins.version:version"
    enabled: true
    aliases: []
```

### Plugin Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Command name (what users type) |
| `command` | string | No* | Python import path (e.g., `module:function`) |
| `script` | string | No* | Executable script path |
| `help` | string | No | Short description for help output |
| `panel` | string | No | Group name in help display (default: "Commands") |
| `enabled` | boolean | No | Enable/disable plugin (default: true) |
| `aliases` | list | No | Alternative command names |

\* Either `command` or `script` must be provided, but not both.

### Adding Custom Plugins

#### Python Plugin Example

```yaml
plugins:
  - name: my-tool
    command: "my_package.tools:cli"
    help: "Custom development tool"
    panel: "Custom Tools"
    enabled: true
```

#### Script Plugin Example

```yaml
plugins:
  - name: build
    script: "./scripts/build.sh"
    help: "Build the project"
    enabled: true
```

## Convert Configuration

Settings for file conversion operations (e.g., LST to SystemVerilog).

```yaml
convert:
  lst:
    # Converter class (advanced)
    # Supports @symbol directive for dynamic imports
    cls: "@symbol socx_plugins.convert.converter:LstConverter"
    
    # Source directory for input files
    # Supports @path and @jinja directives
    source: "@path @jinja {{ this.paths.APP_ROOT_DIR / 'assets/lst/inputs' |abspath }}"
    
    # Target directory for output files
    # Supports @path and @jinja directives
    target: "@path @jinja {{ this.paths.APP_ROOT_DIR / 'workrun/convert/lst/outputs' |abspath }}"
    
    # Base address map JSON file
    base_addr_map: "memLd.json"
    
    # Numeric base for addresses (16=hex, 10=decimal, 8=octal)
    base_addr_base: 16
    
    # File patterns to include
    includes:
      - "*.lst"
      - SPUList.list
    
    # File patterns to exclude
    excludes: []
    
    # Input to output filename mappings
    # % is a wildcard match character
    mappings:
      - input: "%.lst"
        output: "%.svh"
      - input: "%.list"
        output: "%.sv"
      - input: hwsList.lst
        output: pixie_hws_cgs.svh
    
    # Options for path/file handling
    options:
      # How to handle existing output files
      # Options: skip, backup, overwrite
      collision: "overwrite"
```

### Environment Variables

- `SOCX_CONVERT__LST__SOURCE=/path/to/inputs` - Set source directory
- `SOCX_CONVERT__LST__TARGET=/path/to/outputs` - Set output directory

## Rich Click UI Configuration

Settings for terminal UI appearance and behavior.

```yaml
rich_click:
  # UI theme (affects colors and styling)
  THEME: cargo-modern
  
  # Enable markdown formatting in help text
  TEXT_MARKUP: markdown
  
  # Show commands before options in help
  COMMANDS_BEFORE_OPTIONS: false
  
  # Footer text displayed in help
  FOOTER_TEXT: >-
    Documentation is available at <https://sagikimhi.github.io/socx-cli>
  
  # Error suggestion text
  ERRORS_SUGGESTION: |
    Try running with '-h' or '--help' for more information.
  
  # Error epilogue with link
  ERRORS_EPILOGUE: >-
    Documentation is available at [link]https://sagikimhi.github.io/socx-cli[/link]
```

## Language Configuration

Language-specific settings for file conversion and processing.

```yaml
lang:
  systemverilog:
    name: "systemverilog"
    extensions:
      - .sv
      - .svh
    syntax:
      indent: 4
      comments:
        line: "//"
        block:
          begin: "/*"
          end: "*/"
  
  lst:
    name: "lst"
    extensions:
      - ".lst"
      - ".list"
    syntax:
      indent: 4
      comments:
        line: "//"
        block:
          begin: "/*"
          end: "*/"
    # Token processing rules (advanced)
    tokens:
      - name: "comment"
        starts_scope: false
        expr: '([#])(?!([A-Z]{2,}))(?P<content>.*)'
        subst: '{{ this.lang.systemverilog.syntax.comments.line }} \g<content>'
      
      - name: "group"
        starts_scope: true
        expr: '([#])(?P<mem>NVM|ROM)(\W+)(?P<device>[A-Z]{2,})'
        subst: |
          covergroup cg__\g<device>_\g<mem>_access;
          \tcp__\g<device>_\g<mem>_func:
          \tcoverpoint vif.\g<device>_\g<mem>_addr {
        scope_ender: |
          \t\tbins NoFunc = default;
          \t}
          endgroup : cg__\g<device>_\g<mem>_access
      
      - name: "statement"
        starts_scope: false
        expr: '0x(?P<addr>[0-9a-fA-F]+)\W+(?P<func>\w+)\W+(?P<len>\d+)(?P<other>.*)'
        subst: |
          \t\tbins \g<func> = {[
          \t\t\t(('h\g<addr> - 'h{{ base }})) : (('h\g<addr> - 'h{{ base }} + 'd\g<len>) - 1)
          \t\t]};
```

## Configuration Directives

SoCX uses special directives to process configuration values dynamically.

### Available Directives

| Directive | Purpose | Example |
|-----------|---------|---------|
| `@path` | Convert to Path object | `@path ~/workspace` |
| `@symbol` | Import Python symbol | `@symbol module.path:function` |
| `@command` | Convert to Click command | `@command module:cli` |
| `@compile` | Compile Python source | `@compile script.py` |
| `@jinja` | Process Jinja2 template | `@jinja {{ var \| filter }}` |
| `@format` | Format string substitution | `@format ./path/{var}` |

### Jinja2 Templates

Some values support Jinja2 templating:

```yaml
custom:
  path: "@jinja {{ this.paths.APP_ROOT_DIR / 'custom' | abspath }}"
  name: "@jinja {{ env.USER }}_workspace"
```

Available variables:

- `this` - Current configuration object
- `env` - Environment variables
- Built-in Jinja2 filters (e.g., `abspath`, `basename`)

## Configuration Best Practices

### 1. Use Appropriate Levels

```yaml
# Package defaults - Don't modify (edit user/repo config instead)
# Location: src/socx/static/settings/*.yaml

# User config - Personal preferences
# Location: ~/.config/socx/socx.yaml
cli:
  verbosity: DEBUG

# Repository config - Team settings
# Location: .socx.yaml (commit to version control)
regression:
  max_runs_in_parallel: 20
  run:
    input:
      directory: ${PROJECT_ROOT}/ci/logs
```

### 2. Environment Variables for CI

```bash
# In CI/CD pipeline
export SOCX_REGRESSION__MAX_RUNS_IN_PARALLEL=50
export SOCX_REGRESSION__RUN__OUTPUT__DIRECTORY=/tmp/results
socx rgr run
```

### 3. Use Variable Substitution

```yaml
regression:
  run:
    input:
      directory: ${PROJECT_ROOT}/logs
      filename: ${BUILD_TAG:-default}.log
```

### 4. Document Your Overrides

```yaml
regression:
  # Increased for powerful CI machines with 32 cores
  max_runs_in_parallel: 30
  
  run:
    output:
      # Results must go to /shared for archiving
      directory: /shared/regression-results
```

### 5. Test Configuration Changes

```bash
# Verify configuration loads correctly
socx config tree

# Test specific setting
socx config get regression.max_runs_in_parallel

# Debug loading order
socx config debug
```

## See Also

- [Configuration Guide](../user-guide/configuration.md) - How to use configuration
- [Plugin Development](../user-guide/plugins.md) - Creating custom plugins
- [Regression Guide](../user-guide/regression.md) - Running tests in parallel
