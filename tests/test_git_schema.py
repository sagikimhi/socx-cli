from __future__ import annotations

from socx import schema


def test_https_repository_url():
    url = schema.git.RepositoryUrl("https://github.com/sagikimhi/socx-cli")

    assert url.unicode_host() == "github.com"
    assert url.unicode_string() == "https://github.com/sagikimhi/socx-cli"

    assert url.scheme == "https"
    assert url.host == "github.com"
    assert url.port == 443
    assert url.path == "/sagikimhi/socx-cli"

    assert url.query is None
    assert url.fragment is None
    assert url.username is None
    assert url.password is None


def test_ssh_repository_url():
    url = schema.git.RepositoryUrl("ssh://git@github.com/sagikimhi/socx-cli")

    assert url.unicode_host() == "github.com"
    assert url.unicode_string() == "ssh://git@github.com/sagikimhi/socx-cli"

    assert url.scheme == "ssh"
    assert url.username == "git"
    assert url.host == "github.com"
    assert url.path == "/sagikimhi/socx-cli"

    assert url.port is None
    assert url.query is None
    assert url.fragment is None
    assert url.password is None


def test_git_ssh_repository_url():
    url = schema.git.RepositoryUrl(
        "git+ssh://git@github.com/sagikimhi/socx-cli"
    )

    assert url.unicode_host() == "github.com"
    assert (
        url.unicode_string() == "git+ssh://git@github.com/sagikimhi/socx-cli"
    )

    assert url.scheme == "git+ssh"
    assert url.username == "git"
    assert url.host == "github.com"
    assert url.path == "/sagikimhi/socx-cli"

    assert url.port is None
    assert url.query is None
    assert url.fragment is None
    assert url.password is None


if __name__ == "__main__":
    test_https_repository_url()
