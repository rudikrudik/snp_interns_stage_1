def rps_game_winner(game_player: list) -> list:

    try:
        if len(game_player) > 2:
            raise ValueError('WrongNumberOfPlayersError')
        for i in game_player:
            if i[1] not in 'RPS':
                raise ValueError('NoSuchStrategyError')
    except ValueError as e:
        return e

    else:
        if game_player[0][1] == game_player[1][1]:
            return game_player[0]

        if game_player[0][1] + game_player[1][1] in ('PR', 'SP', 'RS'):
            return game_player[0]
        else:
            return game_player[1]
