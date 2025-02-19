# -*- coding: utf-8 -*-
"""Command line interface `aiida-common-workflows`."""
from aiida.cmdline.params import options, types
import click


@click.group('aiida-common-workflows', context_settings={'help_option_names': ['-h', '--help']})
@options.PROFILE(type=types.ProfileParamType(load_profile=True))
def cmd_root(profile):  # pylint: disable=unused-argument
    """CLI for the `aiida-common-workflows` plugin."""
