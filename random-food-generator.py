#!/usr/bin/env python

import random
import csv

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

for ranking in rankings:
    print "compare ranking:",ranking.food, ranking.min,"to", ranking.max, "pick:", pick
    if pick >= ranking.min and pick <= ranking.max:
        print "\nYou have to eat", ranking.food
        break
