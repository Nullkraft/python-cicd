""" Line 1 docstring to be something more real, but later... """
from __future__ import print_function
import random

character = (
    "Hero",
    "Archer",
    "TheRapist",
    "Recruit",
    "Invader",
    "Commander",
    "Children",
    "Spies",
    "Commanders",
    "Soldier",
    "Droids",
    "Veterans",
    "Beasts",
    "Chase",
    "Construction",
    "Honor",
    "Confinement",
    "Defenseless",
    "Alerted",
    "Light",
    "Afraid",
    "Failing",
    "Courage",
    "Demand",
    "Life"
)

final_phrase = (
    "Men's Legacy",
    "The Flight",
    "Tentacles",
    "Men's Legacy",
    "New Worlds",
    "The Future",
    "Four Eyes",
    "Everywhere",
    "Guests",
    "Robots",
    "Directors",
    "Armies",
    "Outer Space",
    "Honor",
    "The Droids",
    "The New World",
    "The Void Of Space",
    "Time Travel",
    "Orbit",
    "The Mists",
    "The New World",
    "New Earth",
    "My Journey",
    "The Machines",
    "Eats candy",
    "Love's the journey"
)

connectors = (
    "Of",
    "In",
    "With",
    "And",
    "By",
    "For",
    "Against",
    "Fired"
)


def sample(the_sample = None, sample_num = 1):
    """
    Sample the goods
    """
    result = random.sample(the_sample, sample_num)
    return result[0]


def generate_movie():
    """
    Make a great movie name
    """
    phrase = ' '.join([sample(character), sample(connectors), sample(final_phrase)])
    if sample_num != 1:
        print(f'sample num = {sample_num}')
    else:
        return phrase.title()


if __name__ == "__main__":
    print(generate_movie())
