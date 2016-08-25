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
new_rows = []
selected_food = ''
csv_file_name = 'foods.csv'

with open(csv_file_name, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

    # create rankings
    for row in reader:
        new_rows.append(row)
        food = row[0]
        ranking = row[1]

        max_ranking += 100/float(ranking)
        rankings.append(Ranking(food, min_ranking, max_ranking))
        min_ranking += 100/float(ranking)

    pick = random.uniform(0.0, max_ranking)

    # show chances
    print("Chances are:")

    for ranking in rankings:
        chance = ((ranking.max-ranking.min)/max_ranking)*100
        print("\t{:2.2f}%\tfor {}".format(chance, ranking.food))

    input("\nPress Enter to continue...")

    # roll random food
    for ranking in rankings:
        if pick >= ranking.min and pick <= ranking.max:
            selected_food = ranking.food
            time = time.strftime("%A %d.%m.%Y")
            print("\n[{}] You have to eat {}\n".format(time, selected_food))
            break

    # change the odds
    for new_row in new_rows:
        if new_row[0] == selected_food:
            new_ranking = int(new_row[1])+1
            new_row[1] = new_ranking

    # write
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter =';', lineterminator='\n', quotechar='"')
        writer.writerows(new_rows)
        print("The odds for {} are decreased".format(selected_food))

    input("\nPress Enter to exit...")
