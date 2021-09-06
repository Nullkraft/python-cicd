""" Test module for Movie title generator """
#import unittest
from generator import generator

def test_sample_single_word():
    """ Test single sample word """
    word_list = ('test', 'a', 'word')
    word = generator.sample(word_list)
    assert word in word_list

def test_sample_multiple_words():
    """ Test multiple sample words """
    word_list = ('test', 'multiple', 'words')
    my_words = generator.sample(word_list, 2)
    assert len(list(my_words)) == 2


def test_generate_a_movie_with_tree_words():
    """ Test the generation of a great movie name """
    movie = generator.generate_movie()
    assert len(movie.split(' ')) >= 3
