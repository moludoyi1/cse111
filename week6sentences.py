import random

def main():
    quantity = 1
    tense = "past"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    print(f'{word} {noun} {verb}')

    quantity = 1
    tense = "present"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    print(f'{word} {noun} {verb}')

    quantity = 1
    tense = "future"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    print(f'{word} {noun} {verb}')

    quantity = 2
    tense = "past"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    print(f'{word} {noun} {verb}')

    quantity = 2
    tense = "present"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    print(f'{word} {noun} {verb}')

    quantity = 2
    tense = "future"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    print(f'{word} {noun} {verb}')

    quantity = 1
    tense = "past"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase = get_prepositional_phrase(quantity)
    print(f'{word} {noun} {verb} {prep_phrase}')

    quantity = 1
    tense = "present"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase = get_prepositional_phrase(quantity)
    print(f'{word} {noun} {verb} {prep_phrase}')

    quantity = 1
    tense = "future"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase = get_prepositional_phrase(quantity)
    print(f'{word} {noun} {verb} {prep_phrase}')

    quantity = 2
    tense = "past"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase = get_prepositional_phrase(quantity)
    print(f'{word} {noun} {verb} {prep_phrase}')

    quantity = 2
    tense = "present"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase = get_prepositional_phrase(quantity)
    print(f'{word} {noun} {verb} {prep_phrase}')

    quantity = 2
    tense = "future"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prep_phrase = get_prepositional_phrase(quantity)
    print(f'{word} {noun} {verb} {prep_phrase}')



def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a noun
    noun = random.choice(noun)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    # Randomly choose and return a verb
    verbs = random.choice(verbs)
    return verbs

def get_preposition():
    preps = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    prep = random.choice(preps)

    return prep

def get_prepositional_phrase(quantity):
    prep = get_preposition()
    word = get_determiner(quantity)
    noun = get_noun(quantity)

    return f'{prep} {word} {noun}'


main()