from timeit import default_timer as timer

def calculate_pi(n):
    ''' Using Leibniz series for Pi approximation.

    Args:
        it (unsigned int): The amount of iterations to run.

    Procedure:
        A guy named Gottfried found that some series converges into PI/4.
        Just sum an alternating series...

        1 - 1/3 + 1/5 - 1/7 + 1/9 ... --> PI/4 so...
        4 - 4/3 + 4/5 - 4/7 + 4/9 ... --> PI
    '''

    denom = 3
    sign = 1
    result = 0.0

    for i in range(n):
        result += (sign / (2.0 * i + 1.0))
        sign = -sign

    return result * 4


def main():
    ''' Runs the speedtest function and times it using Python's builtin timeit.
    '''

    start = timer()
    pi = calculate_pi(pow(10, 8))
    end = timer()

    print('{} ms'.format(round((end - start), 6) * 1000))
    print('Pi is approx --> {}'.format(pi))

if __name__ == "__main__":
    main()