# Publishing to PyPI

This guide explains how to publish the latest release of `socx-cli` to PyPI.

## Prerequisites

The repository is already configured with automated PyPI publishing via GitHub Actions. The workflow is located at `.github/workflows/publish-to-pypi.yml` and uses [trusted publishing](https://docs.pypi.org/trusted-publishers/) (OIDC).

### One-Time PyPI Setup (if not already done)

If this is the first time publishing to PyPI, you need to set up trusted publishing:

1. **Register the package on PyPI** (if not already registered):
   - Go to [PyPI](https://pypi.org/) and create an account if needed
   - Register a new project named `socx-cli`
   - Or use TestPyPI first: [TestPyPI](https://test.pypi.org/)

2. **Configure Trusted Publishing**:
   - Go to your project on PyPI: https://pypi.org/manage/project/socx-cli/settings/
   - Navigate to "Publishing" section
   - Click "Add a new publisher"
   - Fill in the details:
     - **PyPI Project Name**: `socx-cli`
     - **Owner**: `sagikimhi`
     - **Repository name**: `socx-cli`
     - **Workflow name**: `publish-to-pypi.yml`
     - **Environment name**: `pypi`
   - Save the publisher

3. **Create the PyPI environment in GitHub**:
   - Go to repository settings: https://github.com/sagikimhi/socx-cli/settings/environments
   - Create a new environment named `pypi`
   - (Optional) Add protection rules like requiring reviewers

## Publishing a Release

Once the one-time setup is complete, publishing is automated through GitHub Releases:

### Step 1: Update Version Number

1. Update the version in `pyproject.toml`:
   ```toml
   [project]
   version = "0.10.2"  # or whatever the new version is
   ```

2. Update the `CHANGELOG.md` if needed:
   ```bash
   make changelog
   ```

### Step 2: Create a Git Tag and GitHub Release

You have two options:

#### Option A: Using the Makefile (Automated)

```bash
# This will prompt for a version number, then:
# - Stage pyproject.toml and CHANGELOG.md
# - Commit the changes
# - Create a git tag
# - Push commits and tags
make release
```

When prompted, enter the version (e.g., `v0.10.2` or `0.10.2`).

#### Option B: Manual Process

```bash
# 1. Commit your version changes
git add pyproject.toml CHANGELOG.md
git commit -m "chore: prepare release v0.10.2"

# 2. Create and push a tag
git tag v0.10.2
git push origin main
git push origin v0.10.2

# 3. Create a GitHub Release from the tag
# Go to: https://github.com/sagikimhi/socx-cli/releases/new
# - Select the tag you just created
# - Set the release title (e.g., "v0.10.2")
# - Add release notes (can use CHANGELOG.md content)
# - Click "Publish release"
```

### Step 3: GitHub Actions Will Automatically Publish

Once you publish the GitHub release:

1. The workflow `.github/workflows/publish-to-pypi.yml` will trigger automatically
2. It will:
   - Build the source distribution (sdist) and wheel
   - Upload them as artifacts
   - Publish to PyPI using trusted publishing

3. Monitor the workflow progress:
   - Go to: https://github.com/sagikimhi/socx-cli/actions
   - Check the "Publish to PyPI" workflow run

### Step 4: Verify the Publication

After the workflow completes successfully:

1. Check PyPI: https://pypi.org/project/socx-cli/
2. Verify the new version is listed
3. Test installation:
   ```bash
   pip install socx-cli==0.10.2
   # or
   uv tool install socx-cli==0.10.2
   ```

## Troubleshooting

### Workflow Fails with "403 Forbidden"

This means trusted publishing is not set up correctly:
- Verify the publisher configuration on PyPI matches your repository details
- Ensure the `pypi` environment exists in GitHub repository settings
- Check that the workflow name and repository details are correct

### Workflow Fails with "400 Bad Request"

This usually means:
- The version already exists on PyPI (you can't overwrite published versions)
- The version number in `pyproject.toml` needs to be incremented

### Package Name Already Taken

If `socx-cli` is already taken by another project:
- Choose a different name in `pyproject.toml`
- Update the PyPI publisher configuration
- Update all documentation

## Additional Resources

- [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/)
- [GitHub Actions for PyPI Publishing](https://github.com/marketplace/actions/pypi-publish)
- [Python Packaging User Guide](https://packaging.python.org/)
