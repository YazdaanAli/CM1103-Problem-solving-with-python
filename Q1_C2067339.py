import random
import csv
from matplotlib import pyplot as plt


##################################################1A##################################################
def game(ra, rb):
    a, b, win = 0, 0, 11
    for i in range(0, 1000):
        pa = ra / (ra + rb)
        r = random.uniform(0, 1)
        if a == win or b == win:
            if b - a >= 2 or a - b >= 2:
                return a, b
            elif a - b != 2 or b - a != 2:
                if r < pa:
                    a = a + 1
                    win = win + 1
                else:
                    b = b + 1
                    win = win + 1
        else:
            if r < pa:
                a = a + 1
            else:
                b = b + 1


##################################################1B##################################################
def winProbability(ra, rb, n):
    a, b, total = 0, 0, 0
    for i in range(0, n):
        x = game(ra, rb)
        if x[0] > x[1]:
            a = a + 1
        elif x[1] > x[0]:
            b = b + 1
    total = a / (b + a)
    total = float("{:.2f}".format(total))
    return total


##################################################1C##################################################
def player_ability():
    ability_a, ability_b, ability = [], [], []
    with open('Ability.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            ability_a.append(int(row[0]))
            ability_b.append(int(row[1]))
            ability = list(zip(ability_a, ability_b))
    return ability


##################################################1D##################################################
def plotting_abilities(abilities):
    z, prob, ra_rb, total = 1000, [], [], 0
    for x, y in abilities:
        x, y = [int(x), int(y)]
        prob.append(winProbability(x, y, z))
        total = x / y
        prob = sorted(prob)
        ra_rb.append(total)
        ra_rb = sorted(ra_rb)
    plt.plot(ra_rb, prob, "-o", label="pars")
    plt.legend()
    plt.ylabel("Probability of player A winning against player B")
    plt.xlabel("Player A and B abilities")
    plt.title("Probability")
    plt.show()


##################################################1E##################################################
def extra_simulation(ra, rb):
    n, c, cp = 1, 0, 0.9
    while c == 0:
        j = winProbability(ra, rb, n)
        if j == cp:
            return n
        elif j <= cp:
            n = n - 1
            if n == 0:
                n = n + 1
        elif j >= cp:
            n = n + 1


# random.seed(57)  # This sets the random seed for Question 1A
# print(game(70, 30))  # 1A
# print(winProbability(70, 30, 5000))  # 1B
print(player_ability())  # 1C
# print(plotting_abilities([(60, 20), (100, 55), (50, 40), (20, 70), (95, 85)]))  # 1D
# print(extra_simulation(60, 40))  # 1E
