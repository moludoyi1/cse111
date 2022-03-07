import random

def main():
    num = [16.2, 75.1, 52.3]
    print(f"numbers {num}")

    append_random_numbers(num)
    print(f"numbers {num}")

    append_random_numbers(num, 3)
    print(f"numbers {num}")

    words = []

    append_random_words(words)
    print(f"words {words}")

    append_random_words (words, 4)
    print(f"words {words}")

def append_random_numbers(num_list, quantity = 1):
    for _ in range(quantity):
        ran_num = random.uniform(0, 100)
        rounded =  round(ran_num, 1)
        num_list.append(rounded)

def append_random_words(words_list, quantity = 1):
    candidates = ["arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"]
    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)

if __name__ == "__main__":
    main()