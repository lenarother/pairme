import configparser

MOB_CONFIG_FILE = '.mobconfig'


def set_config_value(name, value):
    config = configparser.ConfigParser()
    config.add_section('mob')
    config.set('mob', name, value)

    with open(rf"{MOB_CONFIG_FILE}", 'w') as configfile:
        config.write(configfile)


def set_team(members_list):
    set_config_value('team', members_list)


def set_time(seconds):
    set_config_value('time', seconds)


def get_config_value(name):
    config = configparser.ConfigParser()
    config.read(f"{MOB_CONFIG_FILE}")
    return config["mob"][name]


def get_team():
    try:
        team = get_config_value("team")
        return [i.strip() for i in team.split(',')]
    except KeyError:
        raise LookupError('No team configured, run: cli.py mobteam Jon,Jane,Ben...')


def get_time():
    try:
        return get_config_value("time")
    except KeyError:
        return 15 * 60
