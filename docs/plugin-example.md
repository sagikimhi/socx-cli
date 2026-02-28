# Example Plugin: Hello World

This is a simple example of a socx remote plugin.

## Repository Structure

```
hello-world-plugin/
├── .socx.yaml          # Plugin configuration
├── hello.py            # Plugin implementation
└── README.md           # Documentation
```

## .socx.yaml

```yaml
plugins:
  hello:
    command: "hello:cli"
    short_help: "A simple hello world plugin"
    enabled: true
    panel: "Example Plugins"
    help: |
      Say hello to someone!

      This is a simple example plugin that demonstrates
      how to create a remote plugin for socx-cli.
```

## hello.py

```python
"""A simple hello world plugin for socx-cli."""

import rich_click as click
from rich.console import Console

console = Console()

@click.command()
@click.option(
    "--name",
    default="World",
    help="Name to greet"
)
@click.option(
    "--style",
    type=click.Choice(["simple", "fancy"]),
    default="simple",
    help="Greeting style"
)
def cli(name: str, style: str):
    """Say hello to someone."""
    if style == "fancy":
        console.print(f"[bold cyan]✨ Hello, [yellow]{name}[/yellow]! ✨[/bold cyan]")
    else:
        console.print(f"Hello, {name}!")

if __name__ == "__main__":
    cli()
```

## Usage

### Installing the Plugin

```bash
# If this plugin were published at github.com/user/hello-world-plugin
socx plugin add hello user/hello-world-plugin

# Or with a specific version
socx plugin add hello user/hello-world-plugin --ref v1.0.0
```

### Using the Plugin

```bash
# Simple greeting
socx hello

# Greet someone specific
socx hello --name Alice

# Fancy greeting
socx hello --name Bob --style fancy
```

### Updating the Plugin

```bash
socx plugin update hello
```

### Removing the Plugin

```bash
# Remove from project only
socx plugin remove hello

# Remove from project and cache
socx plugin remove hello --clear-cache
```

## Creating Your Own Plugin

1. **Create a new repository** on GitHub

2. **Add a `.socx.yaml` file** with your plugin configuration:
   ```yaml
   plugins:
     your-plugin-name:
       command: "your_module:cli"
       short_help: "Brief description"
       enabled: true
   ```

3. **Implement your plugin** in a Python file:
   ```python
   import rich_click as click

   @click.command()
   def cli():
       """Your plugin logic here."""
       click.echo("Hello from your plugin!")
   ```

4. **Test locally** by cloning and using file paths:
   ```bash
   git clone https://github.com/you/your-plugin
   cd your-project
   # Edit .socx.yaml to add plugin with file path for testing
   ```

5. **Publish** to GitHub and share with others:
   ```bash
   socx plugin add your-plugin you/your-plugin
   ```

## Plugin Best Practices

1. **Use clear, descriptive names** for your plugins
2. **Provide comprehensive help text** in `.socx.yaml`
3. **Follow Click conventions** for command implementation
4. **Include a README** with usage examples
5. **Use semantic versioning** for tags
6. **Test your plugin** before publishing
7. **Keep dependencies minimal** to avoid conflicts
8. **Document any required environment variables** or setup
