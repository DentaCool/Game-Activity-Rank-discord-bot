class Game:
    def __init__(self, name, time, session_date, exp_multiplayer=1.0):
        self.name = name
        self.total_time = time
        self.top_time = time
        self.exp_multiplayer = exp_multiplayer
        self.last_in_game_session = str(session_date)

    def load_data(self, data):
        for name in data:
            setattr(self, name, data[name])
        return self

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

    def load_data(self, data: dict):
        for game_data in data.pop("games"):
            self.games.append(Game(None, None, None).load_data(game_data))

        for name in data:
            setattr(self, name, data[name])
        return self

    def remove_game(self, name):
        for game in self.games:
            if game.name == name:
                self.games.remove(game)
                return "Deleted"
        return f"Could find game: {name}"

    def _add_game(self, name, time, session_date, exp_multiplayer=1.0):
        self.games.append(Game(name, time, session_date, exp_multiplayer))

    def _update_game_time(self, game_iter, time, session_date):
        self.games[game_iter].update_time(time, session_date)

    def update_time(self, game_name, time, session_date, exp_multiplayer=1.0):
        i = 0
        for game in self.games:
            if game.name == game_name:
                self._update_game_time(i, time, session_date)
                return "game updated"
            i += 1
        self._add_game(game_name, time,  session_date, exp_multiplayer)
        return "game added"

    def to_dict(self) -> dict:
        result = self.__dict__.copy()
        games = result["games"]
        result["games"] = []
        for game in games:
            result["games"].append(game.to_dict())
        return result
