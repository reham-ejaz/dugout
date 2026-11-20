from reham_dugout.loader import load_players, load_team, load_teams
from reham_dugout.rules import MAX_CREDITS
from reham_dugout.models import League
 
 
def show_pool(players):
    """Print how many players there are per franchise and per role."""
    by_franchise = {}
    by_role = {}
    for player in players.values():
        # .get(key, 0) gives 0 the first time we see a key, then we add 1
        by_franchise[player.franchise] = by_franchise.get(player.franchise, 0) + 1
        by_role[player.role] = by_role.get(player.role, 0) + 1
    print("Players by franchise:")
    for franchise in sorted(by_franchise):
        print(f"  {franchise}: {by_franchise[franchise]}")
    print("Players by role:")
    for role in sorted(by_role):
        print(f"  {role}: {by_role[role]}")

def show_team(team):
    """Print a team's players, cost and captains."""
    print(f"\nTeam {team.team_name} by {team.owner}:")
    for player in team.players:
        print(f"  {player}")

    total = team.total_credits()
    remaining = MAX_CREDITS - total
    print(f"Total credits: {team.total_credits()}")
    print(f"Credits left: {remaining}")
    print(f"Captain: {team.captain.name}, Vice-captain: {team.vice_captain.name}")

def show_league_table(sample_teams, my_team):
    league = League("Dugout League")
    for team in sample_teams:
        league.add_team(team)
    league.add_team(my_team)

    ranked_teams = league.rank_teams()

    print("\nLEAGUE TABLE")
    print("-" * 50)
    print(f"{'Rank':<8}{'Team':<20}{'Owner':<12}{'Credits':<10}")
    print("-" * 50)

    for rank, team in enumerate(ranked_teams, start=1):
        print(
            f"{rank:<8}{team.team_name:<20}"
            f"{team.owner:<12}{team.total_credits():<10}"
        )

    print("-" * 50)
 
def main():
    players = load_players("data//players.csv")
    show_pool(players)
    my_team = load_team("data/my_team.csv", players)
    show_team(my_team)
    sample_teams = load_teams("data/sample_teams.csv", players)
    legal = []
    illegal = []
    for team in sample_teams:
        show_team(team)
        errors = team.check_rules()
        if errors:
            illegal.append(team)
            print("ILLEGAL:")
            for error in errors:
                print(f"  - {error}")
        else:
            legal.append(team)
            print("LEGAL")
    print(f"\nSummary: {len(legal)} legal, {len(illegal)} illegal out of {len(sample_teams)} teams")
    print("Legal teams:")
    for team in legal:
        print(f"  {team.team_name}")
    print("Illegal teams:")
    for team in illegal:
        print(f"  {team.team_name}")
    show_league_table(sample_teams, my_team)

if __name__ == "__main__":
    main()
