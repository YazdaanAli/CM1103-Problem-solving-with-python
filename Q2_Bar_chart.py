import random
import csv
from matplotlib import pyplot as plt
import numpy as np


def game(ra, rb):
    a, b, c, win = 0, 0, 100, 11
    for i in range(0, c):
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


def game2(ra, rb):
    s, a, b, win, c, x = 4, 0, 0, 9, 100, 0
    s = random.randint(0, 1)
    for i in range(0, c):
        pa = ra / (ra + rb)
        r = random.uniform(0, 1)
        if a == win or b == win:
            return a, b
        elif a == 8 and b == 8:
            x = random.randint(0, 1)
            if x == 0:
                win = win + 1
                if s == 0:  # means a is server
                    if r < pa:
                        a = a + 1
                    else:
                        s = 1
                elif s == 1:
                    if r < pa:
                        s = 0
                    else:
                        b = b + 1
            elif x == 1:
                win = win + 2
                if s == 0:  # means a is server
                    if r < pa:
                        a = a + 1
                    else:
                        s = 1
                elif s == 1:
                    if r < pa:
                        s = 0
                    else:
                        b = b + 1
        elif s == 0:  # means a is server
            if r < pa:
                a = a + 1
            else:
                s = 1
        elif s == 1:
            if r < pa:
                s = 0
            else:
                b = b + 1


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


def winProbability2(ra, rb, n):
    a, b, total = 0, 0, 0
    for i in range(0, n):
        x = game2(ra, rb)
        if x[0] > x[1]:
            a = a + 1
        elif x[1] > x[0]:
            b = b + 1
    total = a / (b + a)
    total = float("{:.2f}".format(total))
    return total


def winProbability3(ra, rb, n):
    a, b, total = 0, 0, 0
    for i in range(0, n):
        x = game(ra, rb)
        if x[0] > x[1]:
            a = a + 1
        elif x[1] > x[0]:
            b = b + 1
    total = b / (b + a)
    total = float("{:.2f}".format(total))
    return total


def winProbability4(ra, rb, n):
    a, b, total = 0, 0, 0
    for i in range(0, n):
        x = game2(ra, rb)
        if x[0] > x[1]:
            a = a + 1
        elif x[1] > x[0]:
            b = b + 1
    total = b / (b + a)
    total = float("{:.2f}".format(total))
    return total


def player_ability():
    ability_a, ability_b, ability = [], [], []
    with open('Abilities_to_check.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            ability_a.append(row[0])
            ability_b.append(row[1])
            ability = list(zip(ability_a, ability_b))
    return ability


def plot_a_prob():
    ability, prob, p_ability = player_ability(), ["PARS player a", "PARS player b", "English player a", "English player b"], []
    e = []
    u = []
    Barlist = []
    a = 0
    c = 0
    d = 0
    b = 0
    for x, y in ability:
        x, y = [int(x), int(y)]
        e.append(game(x, y))
        u.append(game2(x, y))
    for f, g in e:
        if f > g:
            a = a + 1
        elif g > f:
            b = b + 1
    for r, p in u:
        if r > p:
            c = c + 1
        elif p > r:
            d = d + 1
    p_ability.append(a)
    p_ability.append(b)
    p_ability.append(c)
    p_ability.append(d)
    Barlist = plt.bar(prob, p_ability, align="center", alpha=1, width=0.5)
    Barlist[2].set_color("r")
    Barlist[3].set_color("r")
    plt.ylabel("Number of wins per player")
    plt.xlabel("Pars and English scoring system")
    plt.title("Number of wins per player")
    plt.show()


print(plot_a_prob())


