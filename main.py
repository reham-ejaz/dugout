class Player:
    """One real cricketer in the PSL player list."""
 
    def __init__(self, player_id, name, franchise, role, credits):
        self.player_id = player_id
        self.name = name
        self.franchise = franchise
        self.role = role          # WK, BAT, AR or BOWL
        self.credits = credits    # price in the fantasy game

class FantasyTeam:
    """A fantasy XI picked by one person."""
 
    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None
 
    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
            total = 0
            for player in self.players:
                total = total + player.credits
            return total

    def count_by_role(self):
        counts = {"WK": 0, "BAT": 0, "AR": 0, "BOWL": 0}
        for player in self.players:
            counts[player.role] = counts[player.role] + 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain
 
    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner: {self.owner}, {size} players, {cost} cr)"


team = FantasyTeam("Chakwal Raiders", "Reham")
fakhar = Player("P056", "Fakhar Zaman", "Lahore Qalandars", "BAT", 8.5)
shaheen = Player("P068", "Shaheen Shah Afridi", "Lahore Qalandars", "BOWL", 10.5)
abbas = Player("P045", "Abbas Afridi", "Karachi Kings", "BOWL", 10.0)
ali = Player("P017", "Muhammad Ali", "Hyderabad Kingsmen", "BOWL", 9.5)
haris = Player("P066", "Haris Rauf", "Lahore Qalandars", "BOWL", 7.5) 
saud = Player("P110", "Saud Shakeel", "Quetta Gladiators", "BAT", 9.0)
warner = Player("P037", "DA Warner", "Karachi Kings", "BAT", 9.5)
naeem = Player("P059", "Muhammad Naeem", "Lahore Qalandars", "BAT", 9.0)
sikandar = Player("P065", "Fakhar Zaman", "Lahore Qalandars", "AR", 10)
arafat = Player("P077", "Arafat Minhas", "Multan Sultans", "AR", 7.0)
muhammad = Player("P087", "Muhammad Haris", "Peshawar Zalmi", "WK", 7.5)
team.add_player(fakhar)
team.add_player(shaheen)
team.add_player(abbas)
team.add_player(ali)
team.add_player(haris)
team.add_player(saud)
team.add_player(warner)
team.add_player(naeem)
team.add_player(sikandar)
team.add_player(arafat)
team.add_player(muhammad)
team.set_captain(fakhar, shaheen)
 
print(team)
print("Roles:", team.count_by_role())
print("Captain:", team.captain)
print("Vice Captain:", team.vice_captain)

for player in [fakhar, shaheen, abbas, ali, haris, saud, warner, naeem, sikandar, arafat, muhammad]:
    print(player)

