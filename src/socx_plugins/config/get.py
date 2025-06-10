from functools import partial

import rich_click as click


field_argument = partial(
    click.argument, "field", required=True, type=click.STRING
)


def command():
    from socx import settings

    return partial(
        click.command,
        short_help="Get the current configuration value of FIELD.",
        help=f"""Get the current configuration value of FIELD.
        \n\b
        Possible FIELD values:
        {get_nested_keys(settings.as_dict(settings.current_env))}
        """,
    )()


def get_nested_keys(
    mapping: dict, indent: int = 0, max_indent: int = 2
) -> str:
    rv = "\n\n"

    if indent == max_indent:
        return rv

    for key in mapping:
        rv += (" " * indent) + f"- {key}"
        if isinstance(mapping[key], dict):
            rv += get_nested_keys(mapping[key], indent=indent + 2)
        rv += "\n"
    return rv
