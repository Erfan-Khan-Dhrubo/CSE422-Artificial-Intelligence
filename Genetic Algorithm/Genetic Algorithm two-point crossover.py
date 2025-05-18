import random
import operator


def RandomParent():
    random_number1 = random.randint(1, 99)
    random_number2 = random.randint(1, 99)
    random_number3 = random.randint(1, 99)

    parent_str = ""
    if random_number1 > 9:
        parent_str += str(random_number1)
    else:
        parent_str += "0"
        parent_str += str(random_number1)

    if random_number2 > 9:
        parent_str += str(random_number2)
    else:
        parent_str += "0"
        parent_str += str(random_number2)

    if random_number3 > 9:
        parent_str += str(random_number3)
    else:
        parent_str += "0"
        parent_str += str(random_number3)

    return parent_str


def fitnessScore(chromosome, price_change, total_capital):
    stop_loss = int(chromosome[:2])
    take_profit = int(chromosome[2:4])
    trade_size = int(chromosome[4:])

    for i in price_change:
        if i < 0:
            if i <= -stop_loss:
                loss = (total_capital * (trade_size / 100)) * (stop_loss / 100)
                total_capital -= loss

            else:
                loss = (total_capital * (trade_size / 100)) * (i / 100)
                total_capital += loss
        else:
            if i >= take_profit:
                profit = (total_capital * (trade_size / 100)) * (take_profit / 100)
                total_capital += profit

            else:
                profit = (total_capital * (trade_size / 100)) * (i / 100)
                total_capital += profit

    return total_capital - 1000


def mutation(chromosome):
    probability = random.randint(1, 100)
    if probability <= 5:
        index = random.randint(1, 5)
        replace_number = random.randint(1, 9)
        mutated_chromosome = chromosome[:index] + str(replace_number) + chromosome[index + 1:]
        chromosome = mutated_chromosome

    return chromosome


def two_point_crossover(chromosome1, chromosome2):
    while True:
        i = random.randint(1, 4)
        j = random.randint(i + 1, 5)
        new_chromosome1 = chromosome1[:i] + chromosome2[i:j] + chromosome1[j:]
        new_chromosome2 = chromosome2[:i] + chromosome1[i:j] + chromosome2[j:]
        if new_chromosome1[:2] != "00" and new_chromosome1[2:4] != "00" and new_chromosome1[
                                                                            4:] != "00" and new_chromosome2[
                                                                                            :2] != "00" and new_chromosome2[
                                                                                                            2:4] != "00" and new_chromosome2[
                                                                                                                             4:] != "00":
            return new_chromosome1, new_chromosome2


def genetic_algorithm_two_point(generation, historical_prices, capital):
    chromosome1 = RandomParent()
    chromosome2 = RandomParent()
    chromosome3 = RandomParent()
    chromosome4 = RandomParent()
    parent_arr = [chromosome1, chromosome2, chromosome3, chromosome4]
    # print(parent_arr)

    final_result = []
    for gen in range(generation):
        offsprings = []
        for i in range(len(parent_arr)):
            for j in range(i + 1, len(parent_arr)):
                offspring1, offspring2 = two_point_crossover(parent_arr[i], parent_arr[j])
                offsprings.append(offspring1)
                offsprings.append(offspring2)

        # print(offsprings)

        fitness_dict = {}
        for i in range(len(offsprings)):
            score = fitnessScore(offsprings[i], historical_prices, capital)
            fitness_dict[offsprings[i]] = score

        # operator.itemgetter(1) is used to specify that the sorting should be based
        # on the second item (the value) of each key-value pair.

        sorted_fitness_dict = dict(sorted(fitness_dict.items(), key=operator.itemgetter(1), reverse=True))

        parent_arr = list(sorted_fitness_dict.keys())[:4]

        first_key = list(sorted_fitness_dict.keys())[0]
        first_value = list(sorted_fitness_dict.values())[0]
        final_result = [first_key, first_value]

    return final_result


two_point_result = genetic_algorithm_two_point(1, [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5], 1000)
print(f"Result Offspring {two_point_result[0]}")
