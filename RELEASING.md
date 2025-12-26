# Quick Release Guide

This is a quick reference for maintainers to publish a new release to PyPI.

## Quick Steps

1. **Update the version** in `pyproject.toml`:
   ```toml
   version = "0.11.0"  # increment as appropriate
   ```

2. **Update the changelog**:
   ```bash
   make changelog
   ```

3. **Review changes**:
   ```bash
   git diff
   ```

4. **Run the release command**:
   ```bash
   make release
   ```
   - Enter the version when prompted (e.g., `v0.11.0`)
   - This will commit, tag, and push

5. **Create a GitHub Release**:
   - Go to: https://github.com/sagikimhi/socx-cli/releases/new
   - Select the tag you just pushed
   - Add a title: `v0.11.0`
   - Copy relevant changelog entries as the description
   - Click **"Publish release"**

6. **Wait for automation**:
   - The GitHub Actions workflow will automatically build and publish to PyPI
   - Monitor at: https://github.com/sagikimhi/socx-cli/actions

7. **Verify**:
   - Check https://pypi.org/project/socx-cli/
   - Test: `pip install socx-cli==0.11.0`

## First Time Setup

If this is your first release, see [docs/publish-to-pypi.md](docs/publish-to-pypi.md) for detailed setup instructions, including:
- Setting up trusted publishing on PyPI
- Creating the `pypi` environment in GitHub

## Troubleshooting

- **403 Forbidden**: Trusted publishing not configured on PyPI
- **400 Bad Request**: Version already exists or other validation error
- **Workflow doesn't start**: Make sure you created a **GitHub Release**, not just a tag

For more details, see [docs/publish-to-pypi.md](docs/publish-to-pypi.md).
