from random import randint


if __name__ == '__main__':

    correct_answers = 0
    for sums in range(5):

        num_1 = randint(0,12)
        num_2 = randint(0,12)

    answer = int(input(f'{num_1} x {num_2} ='))

    if answer == (num_1 * num_2):
        print('correct')
        correct_answers += 1

    else:
        print('Gah! That \'s not right!')

        print()
        print(f'You got {correct_answers} right!')
