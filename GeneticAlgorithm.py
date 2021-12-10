import random
import re
import matplotlib.pyplot as plt


def random_population(population_size, dna_length, nucleotide):
    population = []
    for i in range(population_size):
        dna = ""
        for j in range(dna_length):
            dna += random.choice(nucleotide)
        population.append(dna)
    return population


def fitness(dna, constraints):
    fitness = 0
    for constraint in constraints:
        fitness += len(re.findall(constraint[0], dna)) * constraint[1]
    return fitness


def crossover(dna1, dna2, dna_length):
    index = int(random.random() * dna_length)
    return dna1[0][:index] + dna2[0][index:], dna2[0][:index] + dna1[0][index:]


def mutate(dna, dna_length, nucleotide):
    random_number = random.random()
    prob = 0.01
    if random_number < prob:
        random_index = int(random.random() * dna_length)
        random_char = random.choice(nucleotide)
        return dna.replace(dna[random_index], random_char)
    return dna


if __name__ == "__main__":

    dna_length = int(input())
    population_size = int(input())
    numOfSteps = int(input())
    nucleotide = input().split()
    constraints = []
    constraint = input()

    while constraint != "Start":
        name_score = constraint.split("  ")
        constraints.append((name_score[0], int(name_score[1])))
        constraint = input()

    population = random_population(population_size, dna_length, nucleotide)
    highest_ranks = []

    for step in range(numOfSteps):
        print("Step {} ... ".format(step + 1))
        population_with_fitness_value = []

        for member in population:
            fitness_value = fitness(member, constraints)
            population_with_fitness_value.append((member, fitness_value))

        population = []
        population_with_fitness_value.sort(key=lambda x: x[1], reverse=True)

        for i in range(0, population_size, 2):
            # Selection
            dna1 = population_with_fitness_value[i]
            dna2 = population_with_fitness_value[i + 1]

            # Crossover
            dna1, dna2 = crossover(dna1, dna2, dna_length)

            # Mutate and add back into the population.
            population.append(mutate(dna1, dna_length, nucleotide))
            population.append(mutate(dna2, dna_length, nucleotide))

        highest_ranks.append(population_with_fitness_value[0][1])
        print("Done!")

    for member in population:
        fitness_val = fitness(member, constraints)
        population_with_fitness_value.append((member, fitness_val))

    best_dna = max(population_with_fitness_value, key=lambda x: x[1])

    print("Fittest DNA string is \"", best_dna[0], "\" with fitness ", best_dna[1], sep="")

    # save the DNA name in a file
    f = open("A.txt", "w")
    f.write(best_dna[0])
    f.close()

    # plot and save it
    plt.plot(highest_ranks)
    plt.savefig("Apicture.png")
    plt.show()

# 10
# 20
# 100
# a c g t
# ac  -2
# gt  1
# Start

# 500
# 100
# 5000
# a c g t
# cg  -2
# tc  -1
# cc...tt   +10
# Start