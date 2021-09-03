from itertools import permutations
from random import shuffle
import time


def run():

    BAD_LETTER_PATTERNS = {x * 3 for x in 'QWERTYUIPASDFGHJKLZXCVBNM'}
    BAD_NUM_PATTERNS = {x * 2 for x in '123456789'}

    char_set = 'Q1W5ERT3YUI2P8AS4DFGH6JKLZXCV7B9NM'
    char_set_list = list(char_set)
    # Shake the it
    shuffle(char_set_list)
    first_half_char_set = ''.join(char_set_list)

    # Shake the it
    shuffle(char_set_list)
    second_half_char_set = ''.join(char_set_list)

    count = 0
    # Go
    start_time = time.time()

    # Mixed up the letters and numbers
    for fh in permutations(first_half_char_set, r=4):
        first_half = ''.join(fh)
        if first_half.isnumeric():
            continue
        elif any(pattern in first_half for pattern in BAD_LETTER_PATTERNS):
            continue
        elif any(pattern in first_half for pattern in BAD_NUM_PATTERNS):
            continue

        for sh in permutations(second_half_char_set, r=4):
            second_half = ''.join(sh)

            if second_half.isnumeric():
                continue
            elif any(pattern in second_half for pattern in BAD_LETTER_PATTERNS):
                continue
            elif any(pattern in second_half for pattern in BAD_NUM_PATTERNS):
                continue
            count += 1

            if count % 100000 == 0:
                print('count: {} -  Q2AZ-{}-{}'.format(count,
                                                       first_half, second_half))

    end_time = time.time()
    print('Total username count: {}\nStart Time: {}\nEnd Time: {}'.format(
        count, start_time, end_time))


if __name__ == '__main__':
    run()
