from itertools import permutations


def run():
    BAD_LETTER_PATTERNS = {x * 3 for x in 'QWERTYUIPASDFGHJKLZXCVBNM'}
    BAD_NUM_PATTERNS = {x * 2 for x in '123456789'}

    count = 0

    for x in permutations('Q1W5ERT3YUI2P8AS4DFGH6JKLZXCV7B9NM', r=8):
        first_half = ''.join(x[:4])
        second_half = ''.join(x[4:])

        if first_half.isnumeric():
            continue
        elif second_half.isnumeric():
            continue
        elif any(pattern in first_half for pattern in BAD_LETTER_PATTERNS):
            continue
        elif any(pattern in first_half for pattern in BAD_NUM_PATTERNS):
            continue
        elif any(pattern in second_half for pattern in BAD_LETTER_PATTERNS):
            continue
        elif any(pattern in second_half for pattern in BAD_NUM_PATTERNS):
            continue
        count += 1

        if count % 100000 == 0:
            print('count: {} -  Q2AZ-{}-{}'.format(count, first_half, second_half))

    print(count)


if __name__ == '__main__':
    run()
