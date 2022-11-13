from random import shuffle


def validate_team(team):
    if len(team) <= 1:
        raise ValueError("Invalid input: team must have more than one member.")
    if len(team) != len(set(team)):
        raise ValueError("Invalid input: names of team members should not be repeated.")


def pull_pairs(team):
    validate_team(team)
    shuffle(team)
    pairs = [(sm, sm_bkp) for sm, sm_bkp in zip(team, team[1:] + team[:1])]
    shuffle(pairs)
    return pairs
