#!/usr/bin/env python

import random
import csv
import time

class Ranking:
    def __init__(self, food, x, y):
        """ Create a new point at the origin """
        self.food = food
        self.min = x
        self.max = y

min_ranking = 0
max_ranking = 0
rankings = []

with open('foods.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in reader:
        food = row[0]
        ranking = row[1]

        max_ranking += 100/float(ranking)
        rankings.append(Ranking(food, min_ranking, max_ranking))
        min_ranking += 100/float(ranking)

csvfile.close()

pick = random.uniform(0.0, max_ranking)

print("Chances are:")

for ranking in rankings:
    chance = ((ranking.max-ranking.min)/max_ranking)*100
    print("\t{:2.2f}%\tfor {}".format(chance, ranking.food))

raw_input("\nPress Enter to continue...")

for ranking in rankings:
    if pick >= ranking.min and pick <= ranking.max:
        time = time.strftime("%A %d.%m.%Y")
        print("\n[{}] You have to eat {}\n".format(time, ranking.food))
        break
