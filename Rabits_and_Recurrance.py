def fib_rabbits(n,k):
    '''Returns the number of rabbits present after n generations with litters of k pairs.'''
    rabbits = [0,1]
    for i in xrange(n-1):
        rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]

    return rabbits[n % 2]


def main():
    '''Main call. Parses, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_fib.txt') as input_data:
        n, k = map(int, input_data.read().strip().split())

    # Get the number of rabbits.
    rabbits = str(fib_rabbits(n,k))

    # Print and save the answer.
    print rabbits
    with open('output/004_FIB.txt', 'w') as output_data:
        output_data.write(rabbits)


if __name__ == '__main__':
    main()
