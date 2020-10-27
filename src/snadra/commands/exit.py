"""
The command to exit snadra.
"""
from typing import TYPE_CHECKING, Optional

from snadra._util import console
from snadra.commands._base import CommandDefinition, Complete, Parameter

if TYPE_CHECKING:
    import argparse


class Command(CommandDefinition):
    """
    Help message for "exit"
    """

    KEYWORDS = {"exit", "quit"}
    HELP_TEXT = "Exit the console"

    ARGS = {
        "-y,--yes": Parameter(
            complete=Complete.NONE, action="store_true", help="Confirm to exit"
        )
    }

    def run(self, args: Optional["argparse.Namespace"] = None):
        """
        Exit `snadra`.
        """
        if args is None or not args.yes:
            console.log("[red]Error[/red]: exit not confirmed (use '--yes')")
            return

        raise EOFError("Got an exit signal")
