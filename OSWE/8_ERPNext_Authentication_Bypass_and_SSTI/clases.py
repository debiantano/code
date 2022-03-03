#!/usr/bin/python3
import pdb

class Food:
    calories = 100

class Fruit(Food):
    fructose = 2.0

class Strawberry(Fruit):
    ripeness = "Ripe"

pdb.set_trace()

s = Strawberry()
s.calories
s.fructose
s.ripeness

