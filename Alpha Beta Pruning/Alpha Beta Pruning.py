import math
import random


def strength(x):
    return math.log2(x + 1) + x / 10


def utility(x, y):
    MAX = strength(x)
    MIN = strength(y)
    RandomValue = random.randint(1, 10)
    randomValue = ((-1) ** (random.randint(1, 10))) * (RandomValue / 10)
    final = MAX - MIN + randomValue
    return final


def minimax(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 4:
        return values[node_index]

    if maximizing_player:
        best_value = float('-inf')
        for i in range(2):
            value = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float('inf')
        for i in range(2):
            value = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value


player_input = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
Carlsen_power = float(input("Enter base strength for Carlsen: "))
Caruana_power = float(input("Enter base strength for Caruana: "))
Magnus_win = 0
Fabiano_win = 0
Draw = 0

if player_input == 0:
    maximizing_player = "Magnus Carlsen"
    minimizing_player = "Fabiano Caruana"
else:
    maximizing_player = "Fabiano Caruana"
    minimizing_player = "Magnus Carlsen"

for i in range(4):
    temp_list = []
    for item in range(32):
        x = utility(Carlsen_power, Caruana_power)
        temp_list.append(x)

    if i % 2 == 0:
        if player_input == 0:   # true represent Carlsen maximizing player
            is_max = True
        else:
            is_max = False
    else:
        if player_input == 0:
            is_max = False
        else:
            is_max = True

    result = minimax(0, 0, is_max, temp_list, float('-inf'), float('inf'))

    if result > 0:
        print(f"Game {i+1} Winner: {maximizing_player} (Max)  (Utility value: {result})")
        if maximizing_player == "Magnus Carlsen":
            Magnus_win += 1
        else:
            Fabiano_win += 1

    elif result < 0:
        print(f"Game {i + 1} Winner: {minimizing_player} (Min)  (Utility value: {result})")
        if minimizing_player == "Magnus Carlsen":
            Magnus_win += 1
        else:
            Fabiano_win += 1
    else:
        print(f"Game {i+1} is Draw")
        Draw += 1

    if maximizing_player == "Magnus Carlsen":
        maximizing_player = "Fabiano Caruana"
        minimizing_player = "Magnus Carlsen"
    else:
        maximizing_player = "Magnus Carlsen"
        minimizing_player = "Fabiano Caruana"

winner = ""
if Magnus_win > Fabiano_win:
    winner = "Magnus Carlsen"
elif Fabiano_win > Magnus_win:
    winner = "Fabiano Caruana"
else:
    winner = "Draw"


print(f"Overall Results: \nMagnus Carlsen Wins: {Magnus_win} \nFabiano Caruana Wins: {Fabiano_win} \nDraws: {Draw} \nOverall Winner: {winner}")
