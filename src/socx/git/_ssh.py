from __future__ import annotations

import logging
from pathlib import Path

import paramiko


logger = logging.getLogger(__name__)


def get_ssh_config(
    hostname: str, path: str | Path | None = None
) -> paramiko.SSHConfigDict:
    """Retrieve the SSH configuration for a given hostname.

    Parameters:
    -----------
    hostname: str
        The hostname to look up in the SSH config.
    path: str | Path | None, optional
        Path to the SSH config file.
        Defaults to '~/.ssh/config' if not provided.

    Returns:
    --------
    paramiko.SSHConfigDict
        The SSH configuration dictionary for the hostname.
        Returns an empty dictionary if the config file is not found or cannot
        be parsed.
    """
    path = path or Path("~/.ssh/config").expanduser()
    try:
        config = paramiko.SSHConfig.from_path(path)
    except FileNotFoundError:
        err = "SSH config file not found at '%s'" % path
        logger.exception(err)
        return paramiko.SSHConfigDict()
    except paramiko.ConfigParseError:
        logger.exception("Error parsing SSH config file at '%s'", path)
        return paramiko.SSHConfigDict()
    else:
        return config.lookup(hostname)


def get_ssh_key_path(
    hostname: str, path: str | Path | None = None
) -> str | None:
    """Get the path to the SSH private key for a given hostname.

    Parameters:
    -----------
    hostname: str
        The hostname to look up in the SSH config.

    path: str | Path | None, optional
        Path to the SSH config file.
        Defaults to '~/.ssh/config' if not provided.

    Returns:
    --------
    str | None
        The path to the SSH private key if found, otherwise None.
    """
    config = get_ssh_config(hostname=hostname, path=path)
    return config.get("IdentityFile")
