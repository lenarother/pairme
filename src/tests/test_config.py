import pytest
from unittest import mock
import configparser

from src.pairme.config import CONFIG_SECTION, get_team, get_time


@pytest.mark.parametrize(
    "config_dict, expected_value",
    [
        ({}, 900),
        ({CONFIG_SECTION: {'time': 1}}, 1)
    ]
)
def test_read_time_from_pairme_config(config_dict, expected_value):
    with mock.patch('src.pairme.config.get_config') as get_config_mock:
        config = configparser.ConfigParser()
        config.read_dict(config_dict)
        get_config_mock.return_value = config
        assert expected_value == get_time()


@pytest.mark.parametrize(
    "config_dict, expected_value",
    [
        ({CONFIG_SECTION: {'team': "Bob"}}, ["Bob"]),
        ({CONFIG_SECTION: {'team': "Bob,Jo"}}, ["Bob", "Jo"]),
    ]
)
def test_read_team_from_pairme_config(config_dict, expected_value):
    with mock.patch('src.pairme.config.get_config') as get_config_mock:
        config = configparser.ConfigParser()
        config.read_dict(config_dict)
        get_config_mock.return_value = config
        assert expected_value == get_team()


def test_team_not_configured():
    with mock.patch('src.pairme.config.get_config') as get_config_mock:
        config = configparser.ConfigParser()
        config.read_dict({})
        get_config_mock.return_value = config
        with pytest.raises(KeyError):
            get_team()