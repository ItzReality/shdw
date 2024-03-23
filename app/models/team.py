# This file contains a model for the Team class which is used to store the team information
# and perform operations on the team such as signing, promoting, demoting, and dropping players.
# to-do add database capabilities
class Team:
    def __init__(
        self,
        name="New Team",
        div="4",
        owner="SHDW",
        coach=None,
        manager=None,
        players={"Player": {"lineup": "starters", "role": "Dps"}},
    ) -> None:
        self.name = name
        self.div = div
        self.owner = owner
        self.coach = coach
        self.manager = manager
        self.players = players

    # signs a player to the team (add a player to the team roster with any role and lineup status, default to support and tryouts respectively)
    def signPlayer(self, player, lineup="tryouts", role="support") -> bool:
        if self.existsPlayer(player):
            return False
        self.players[player] = {"lineup": lineup, "role": role}
        return True

    # promotes a player's lineup status to one level higher, promotes tryouts to subs, and subs to starters
    def promotePlayer(self, player) -> bool:
        if not self.existsPlayer(player):
            return False

        if self.players[player]["lineup"] == "starters":
            return False
        elif self.players[player]["lineup"] == "tryouts":
            self.players[player]["lineup"] = "subs"
        else:
            self.players[player]["lineup"] = "starters"
        return True

    # drops a player from the team completely (does not demote first)
    def dropPlayer(self, player) -> bool:
        return True if self.players.pop(player, None) else False

    # demotes a player's lineup status to one level lower, demotes starters to subs, and drops tryouts and subs
    def demotePlayer(self, player) -> bool:
        if not self.existsPlayer(player):
            return False

        if self.players[player]["lineup"] != "starters":
            return False
        self.players[player]["lineup"] = "subs"
        return True

    # checks if a player exists in the team roster
    def existsPlayer(self, player) -> bool:
        return player in list(self.players.keys())


# test the Team class
if __name__ == "__main__":

    players = {
        "rishi": {"lineup": "starters", "role": "Tank"},
        "rishi": {"lineup": "starters", "role": "Dps"},
        "RealityGhost": {"lineup": "starters", "role": "Dps"},
        "Gamer": {"lineup": "starters", "role": "Support"},
        "Briefen": {"lineup": "starters", "role": "Support"},
        "illushannist": {"lineup": "subs", "role": "Dps"},
        "geo": {"lineup": "subs", "role": "Dps"},
        "JStar24": {"lineup": "subs", "role": "Support"},
        "Eggy": {"lineup": "subs", "role": "Support"},
        "clover": {"lineup": "tryouts", "role": "Tank"},
    }

    team = Team("Punks", "3", "rishi", "Aimless", "Gamer", players)

    print(team.signPlayer("apple", "Tank"))
    print(team.promotePlayer("clover"))
    print(team.dropPlayer("Eggy"))
    print(team.demotePlayer("Briefen"))
    print(team.promotePlayer("JStar24"))
    print(team.dropPlayer("appl"))
    print(team.promotePlayer("rishi"))
    print(team.promotePlayer("illushannist"))
    print(team.demotePlayer("rishi"))
    print(team.demotePlayer("rishi"))

    print(team.players)
