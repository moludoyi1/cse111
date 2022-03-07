'''
Team activity
Rosenberg Self Esteem Scale
Michael
'''
print()

GOOD = 1
BAD = -1

def main():
    print('''This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.

    Please rate how much you agree with each of the
    statements by responding with one of these four letters:

    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.''')
    print()

    score = 0 
    score += question("1. I feel like I am a person of worth, at least on an equal plane with others.", GOOD)

    score += question("I feel that I have a number of good qualities.", GOOD)

    score += question("3. All in all, I am inclined to feel that I am a failure.", BAD)

    score += question("4. I am able to do things as well as most other people.", GOOD)

    score += question("5. I feel I do not have much to be proud of.", BAD)

    score += question("6. I take a positive attitude toward myself.", GOOD)

    score += question("7. On the whole, I am satisfied with myself.", GOOD)

    score += question("8. I wish I could have more respect for myself.", BAD)

    score += question("9. I certainly feel useless at times.", BAD)

    score += question("10. At times I think I am no good at all.", BAD)

    print()
    print(f'Your score is {score}.')
    print("A score below 15 may indicate problematic low self-esteem.")
    

def question(statements, good_bad):
    print(statements) # staments is the question being passed into the code
    result = input('Enter D, d, a, or A: ')
    score = 0

    if result == 'D':
        score = 0
    elif result == 'd':
        score = 1
    elif result == 'a':
        score = 2
    elif result == 'A':
        score = 3
    
    if good_bad == BAD:
        score = 3 - score
        # whatever the score is for a BAD statement, 3 - what the score is because
        # it doesnt count on putting urself on a good self esteem scale
    return score
    


if __name__ == "__main__":
    main()