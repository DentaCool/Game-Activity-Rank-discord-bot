class Game:
    def __init__(self, name, time, exp_multiplayer=1.0):
        self.name = name
        self.total_time = time
        self.top_time = time
        self.exp_multiplayer = exp_multiplayer
        self.last_in_game_session = ''

    def update_time(self, time, session_date):
        self.total_time += time
        self.last_in_game_session = session_date
        if time > self.top_time:
            self.top_time = time

    def to_dict(self) -> dict:
        return self.__dict__


class UserData:
    """
    Main user data class
    """

    def __init__(self, discord_id, username):
        self.discord_id = discord_id
        self.username = username
        self.games = []
        self.total = 0  # total play time in seconds
        self.exp = 0
        self.lvl = 0
        self.note = ""

    def remove_game(self, name):
        for game in self.games:
            if game.name == name:
                self.games.remove(game)
                return "Deleted"
        return f"Could find game: {name}"

    def _add_game(self, name, time, exp_multiplayer=1.0):
        self.games.append(Game(name, time, exp_multiplayer))

    def _update_game_time(self, game_iter, time):
        self.games[game_iter].update_time(time)

    def update_time(self, game_name, time, exp_multiplayer=1.0):
        # TODO: add/update game info in one func
        for i, game in self.games:
            if game.name == game_name:
                self._update_game_time(i, time)
                return "game updated"
        self._add_game(game_name, time, exp_multiplayer)
        return "game added"

    def to_dict(self) -> dict:
        return self.__dict__
