import pandas as pd
import random

from flask import Flask, redirect, render_template, request, session
from pytrends.request import TrendReq

# Trend list
pytrends = TrendReq(hl='en-US', tz=360)
trending = pytrends.trending_searches()
TRENDS = trending[0].tolist()

# Picks two random trends from the trends list
def create_trends():
    choice1 = random.choice(TRENDS)
    choice2 = random.choice(TRENDS)
    if choice1 == choice2:
        choice2 = random.choice(TRENDS)

    return choice1, choice2


# Check to see which trend is more popular
def find_winner(choice1, choice2):
    trend_rank1 = []
    trend_rank2 = []
    rank = 0
    trend_len = len(TRENDS)

    while rank < trend_len:
        if choice1 == TRENDS[rank]:
            trend_rank1.append(rank)
        if choice2 == TRENDS[rank]:
            trend_rank2.append(rank)
        rank += 1

    if trend_rank1[0] < trend_rank2[0]:
        return choice1
    else:
        return choice2


def get_trends():
    return TRENDS