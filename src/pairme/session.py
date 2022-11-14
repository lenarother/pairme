import datetime
import os
import platform
import time

import beepy as beep
import click

PAIRME_SEPARATOR = "-" * 50
MINUTE = 60


def make_sound(*args):
    system = platform.platform().lower()
    if system.startswith("macos"):
        for message in args:
            os.system(f"say {message}")
    else:
        beep.beep(7)


def should_take_break(turns_counter, break_frequency):
    return turns_counter != 0 and turns_counter % break_frequency == 0


def take_break(break_duration):
    break_end = datetime.datetime.now() + datetime.timedelta(seconds=break_duration)
    break_message = (
        f"Take a {int(break_duration / MINUTE)} minutes break until {break_end:%H:%M}."
    )
    click.echo(break_message)
    click.echo(PAIRME_SEPARATOR)
    make_sound(break_message)

    time.sleep(break_duration)


def run_mob(pairs, time_interval, break_duration, break_frequency):
    pairs.reverse()
    for counter, pair in enumerate(pairs):
        if should_take_break(counter, break_frequency):
            take_break(break_duration)

        message_change = "Times up, change pair!"
        message_pair = f"Driver is {pair[0]}, navigator is {pair[1]}."

        click.echo(message_change)
        click.echo(message_pair)
        click.echo(PAIRME_SEPARATOR)

        make_sound(message_change, message_pair)

        time.sleep(time_interval)
