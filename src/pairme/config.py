from pathlib import Path
import configparser

PROJECT_DIR = Path(__file__).parent
CONFIG_FILE = f"{PROJECT_DIR}/.pairme.conf"
CONFIG_SECTION = "pairme"


def get_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config


def write_config(config):
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)


def set_config_value(name, value):
    config = get_config()
    if not config.has_section(CONFIG_SECTION):
        config.add_section(CONFIG_SECTION)
    config.set(CONFIG_SECTION, name, value)
    write_config(config)


def get_config_value(name, fallback=None):
    config = get_config()
    if fallback:
        return config.get(CONFIG_SECTION, name, fallback=fallback)
    return config.get(CONFIG_SECTION, name)


def set_team(members_list):
    set_config_value("team", members_list)


def set_time(seconds):
    set_config_value("time", str(seconds))


def get_team():
    try:
        team = get_config_value("team")
        return [i.strip() for i in team.split(",")]
    except (configparser.NoSectionError, configparser.NoOptionError):
        raise KeyError("No team configured, run: cli.py --mobteam Jon,Jane,Ben...")


def get_time():
    return int(get_config_value("time", fallback=15 * 60))
