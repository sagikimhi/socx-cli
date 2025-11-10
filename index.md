SoCX is a command-line toolbox for EDA development teams.

SoCX can also be used in your own python project/library/script and provides an extensive API with many useful features targeted at EDA development.

## Installation

Requirements: Python 3.12 or newer.

### Install with uv

```
uv tool install socx-cli
```

```
uvx socx-cli
```

```
uv add socx-cli
```

```
uv add --script socx-cli
```

### Install with pip

```
pipx install socx-cli
```

```
pipx run socx-cli
```

### Verify the installation

```
socx --help
socx version
```

## License

Dual-licensed under Apache-2.0 or MIT.

See [LICENSE](home/license.html) for details.

## Development

Contributions are welcome—check `CONTRIBUTING.md` for workflow details.

Typical checks:

```
make check
```

```
make build
```

```
make sync
```

```
make docs
```

```
make docs_deploy
```

## Where to go from here

- Proceed to the [Quick Start](home/quickstart.html) guide to get up and running quickly.
- Read the [User Guide](user-guide/cli.html) for detailed usage instructions and examples.
- Explore the [API Reference](reference/api.html) for advanced integration and customization.
- Visit the [Contributing Guide](development/contributing.html) if you’d like to help improve the project.

## Documentation & Community

- Project Documentation: <https://sagikimhi.dev/socx-cli>
- Community Discussions: <https://gitter.im/socx-cli/community>
- Code of Conduct: `CODE_OF_CONDUCT.md`
- Changelog: `CHANGELOG.md`
