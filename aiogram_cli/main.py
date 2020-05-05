from typing import Any

import typer

from aiogram_cli.loader import setup_plugins


def main() -> Any:  # pragma: no cover
    app = typer.Typer()
    setup_plugins(app)
    return app()