#  Task - Done!

def rps_game_winner(game_player: list) -> str:

    if len(game_player) > 2:
        raise Exception('WrongNumberOfPlayersError')

    for i in game_player:
        if i[1] not in 'RPS':
            raise Exception('NoSuchStrategyError')

    if game_player[0][1] == game_player[1][1]:
        return game_player[0]

    if game_player[0][1] + game_player[1][1] in ('PR', 'SP', 'RS'):
        return game_player[0]
    else:
        return game_player[1]


#print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) # => WrongNumberOfPlayersError
#print(rps_game_winner([['player1', 'P'], ['0', '0']])) # => WrongNumberOfPlayersError
#rps_game_winner([['player1', 'P'], ['player2', 'A']]) # => NoSuchStrategyError
#print(rps_game_winner([['player1', 'P'], ['player2', 'R']])) # => 'player2 S'
#print(rps_game_winner([['player1', 'S'], ['player2', 'S']])) # => 'player1 P'