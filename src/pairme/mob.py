import os
import platform
import time

import beepy as beep
import click


def make_sound(*args):
    system = platform.platform().lower()
    if system.startswith('macos'):
        for message in args:
            os.system(f"say {message}")
    else:
        beep.beep(7)


def run_mob(pairs, time_interval):
    pairs.reverse()
    while pairs:
        pair = pairs.pop()
        message_change = "Times up, change pair!"
        message_pair = f"Driver is {pair[0]}, navigator is {pair[1]}"

        click.echo(message_change)
        click.echo(message_pair)
        click.echo(f"-" * 50)

        make_sound(message_change, message_pair)

        time.sleep(time_interval)


