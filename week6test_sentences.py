from week6sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range(4):
        noun = get_noun(1)
        assert noun in single_noun
    
    plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        quantity = random.randint(2,11)
        noun = get_noun(quantity)
        assert noun in plural_noun


def test_get_verbs():
    past_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        verb = get_verb(1, 'past')
        assert verb in past_verb
    present_singular_verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb = get_verb(1, 'present')
        assert verb in present_singular_verb
    present_plural_verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        quantity = random.randint(2,11)
        verb = get_verb(quantity, 'present')
        assert verb in present_plural_verb
    future_verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(4):
        verb = get_verb(1, 'future')
        assert verb in future_verb


def test_get_preposition():
    preps = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    prep = get_preposition()
    assert prep in preps


def test_get_prepositional_phrase():
    prepostions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_prepositional_phrase(1)
        words = word.split(' ')
        assert words[0] in prepostions
    
    singularnouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        noun = get_prepositional_phrase(1)
        nouns = noun.split(' ')
        assert nouns[2] in singularnouns
    
    pluralnouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        noun = get_prepositional_phrase(2)
        nouns = noun.split(' ')
        assert nouns[2] in pluralnouns
    
    singledeterminer = ["a", "one", "the"]
    for _ in range(4):
        determiner = get_prepositional_phrase(1)
        determiners = determiner.split(' ')
        assert determiners[1] in singledeterminer
    
    pluraldeterminer = ["two", "some", "many", "the"]
    for _ in range(4):
        determiner = get_prepositional_phrase(2)
        determiners = determiner.split(' ')
        assert determiners[1] in pluraldeterminer


pytest.main(["-v", "--tb=line", "-rN", __file__])