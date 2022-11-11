#!/usr/bin/env python

"""Console script for pairme."""

import sys
import click

from src.pairme.pairs import pull_pairs
from src.pairme.mob import run_mob
from src.pairme.config import get_team, set_team, set_time, get_time


@click.command()
@click.option("--mobteam", type=str, help="Team members e.g. Bob,Jane,Jon")
@click.option("--mobtime", type=int, help="Time for one mob pair.")
def main(mobteam=None, mobtime=None):
    if mobteam:
        set_team(mobteam)
        click.echo(f"Team set to {mobteam}")
        return

    if mobtime:
        set_time(mobtime)
        click.echo(f"Mob time round set to {mobtime}")
        return

    team = get_team()
    interval = get_time()

    mob_pairs = pull_pairs(team)
    for pair in mob_pairs:
        click.echo(f"Driver: {pair[0]} - Navigator: {pair[1]}")
    click.echo(f"-" * 50)
    run_mob(mob_pairs, interval)
    return


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
