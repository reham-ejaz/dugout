import csv

from reham_dugout.models import Player, FantasyTeam

def load_players(path):

    players = {}

    with open (path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            player = Player.from_row(row)
            players[player.player_id] = player
    return players

def team_from_row(row, players):
    team = FantasyTeam(row["team_name"], row["owner"])

    for player_id in row["players"].split(";"):
        team.add_player(players[player_id.strip()])
    
    team.set_captain(players[row["captain"]], players[row["vice_captain"]])

    return team

def load_team(path, players):

    with open (path, newline="", encoding= "utf-8") as f:
        for row in csv.DictReader(f):
            return team_from_row(row, players)

def load_teams(path, players):
    """Return a list of every team in a teams CSV file."""
    teams = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            teams.append(team_from_row(row, players))
    return teams
