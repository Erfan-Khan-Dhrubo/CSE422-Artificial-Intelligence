import math
import random

# Strength function
def strength(x):
    return math.log2(x + 1) + x / 10

# Utility function with randomness
def utility(x, y):
    MAX = strength(x)
    MIN = strength(y)
    randomValue = ((-1) ** random.randint(0, 1)) * (random.randint(1, 10) / 10)
    return MAX - MIN + randomValue


def minimax(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 4:
        return values[node_index]
    if maximizing_player:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def mind_control_minimax(depth, node_index, maximizing_player, values):
    if depth == 4:
        return values[node_index]
    best = float('-inf')
    for i in range(2):
        val = mind_control_minimax(depth + 1, node_index * 2 + i, True, values)
        best = max(best, val)
    return best


# === MAIN ===
player_input = int(input("Enter who goes first (0 for Light, 1 for L): "))
cost = float(input("Enter the cost of using Mind Control: "))
light_power = float(input("Enter base strength for Light: "))
l_power = float(input("Enter base strength for L: "))

# Set who is max and min
if player_input == 0:
    max_name = "Light"
    min_name = "L"
    max_power = light_power
    min_power = l_power
else:
    max_name = "L"
    min_name = "Light"
    max_power = l_power
    min_power = light_power

# Generate leaf node values
values = [utility(max_power, min_power) for _ in range(32)]

# Regular minimax
normal_value = minimax(0, 0, True, values, float('-inf'), float('inf'))

# Mind control minimax
mind_value = mind_control_minimax(0, 0, True, values)
mind_value_after_cost = mind_value - cost

# Output
print(f"\nMinimax value without Mind Control: {round(normal_value, 2)}")
print(f"Minimax value with Mind Control: {round(mind_value, 2)}")
print(f"Minimax value with Mind Control after incurring the cost: {round(mind_value_after_cost, 2)}")

# Decision
if mind_value_after_cost > normal_value:
    print(f"\n{max_name} should use Mind Control.")
else:
    print(f"\n{max_name} should NOT use Mind Control.")

