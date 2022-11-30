class WrongNumberOfPlayersError(Exception):
    def __str__(self):
        return 'The number of players cannot be more than 2.'


class NoSuchStrategyError(Exception):
    def __str__(self):
        return 'The rules of the game do not allow these arguments to be accepted.'


def rps_game_winner(game_player: list) -> str:

    try:
        if len(game_player) > 2:
            raise WrongNumberOfPlayersError
        for i in game_player:
            if i[1] not in 'RPS':
                raise NoSuchStrategyError
    except ValueError as e:
        return e

    else:
        if game_player[0][1] == game_player[1][1]:
            return ' '.join(game_player[0])

        if game_player[0][1] + game_player[1][1] in ('PR', 'SP', 'RS'):
            return ' '.join(game_player[0])

        else:
            return ' '.join(game_player[1])
