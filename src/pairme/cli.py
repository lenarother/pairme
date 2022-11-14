#!/usr/bin/env python

"""Console script for pairme."""

import sys
import click

from src.pairme.pair import pull_pairs
from src.pairme.session import run_mob
from src.pairme import config


@click.command()
@click.option("--mobteam", type=str, help="Team members e.g. Bob,Jane,Jon")
@click.option("--mobtime", type=int, help="Time for one mob pair.")
def main(mobteam=None, mobtime=None):
    if mobteam:
        config.set_team(mobteam)
        click.echo(f"Team set to {mobteam}.")
        return

    if mobtime:
        config.set_time(mobtime)
        click.echo(f"Mob time round set to {mobtime}.")
        return

    team = config.get_team()
    interval = config.get_time()
    break_duration = config.get_break_duration()
    break_frequency = config.get_break_frequency()

    mob_pairs = pull_pairs(team)
    for pair in mob_pairs:
        click.echo(f"Driver: {pair[0]} - Navigator: {pair[1]}.")
    click.echo(f"-" * 50)
    run_mob(
        pairs=mob_pairs,
        time_interval=interval,
        break_duration=break_duration,
        break_frequency=break_frequency,
    )
    return


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
