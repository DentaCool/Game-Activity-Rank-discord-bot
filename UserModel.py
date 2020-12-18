class Game:
    def __init__(self, name, time, exp_multiplayer=1.0):
        self.name = name
        self.time = time
        self.top_time = time
        self.exp_multiplayer = exp_multiplayer

    def update_time(self, time):
        pass

    def to_dict(self):
        # TODO: if dict key==Game.name, how to easily convert Game obj to dict/json?
        #  Maybe return {self.name: {"time": self.time, "Top session time": self.top_time}}
        #  or           {"name": self.name, "time": self.time, "Top session time": self.top_time}
        return {"Name": self.name, "time": self.time, "Top session time": self.top_time}


class UserData:

    def __init__(self, discord_id, username):
        self.discord_id = discord_id
        self.username = username
        self.games = {}
        self.total = 0  # total play time in seconds
        self.exp = 0
        self.lvl = 0

    def remove_game(self):
        pass

    def _add_game(self):
        pass

    def _update_game(self):
        pass

    def update_time(self, game_name, time):
        # TODO: add/update game info in one func
        pass

    def to_json(self):
        pass

    def to_dict(self) -> dict:
        return self.__dict__
