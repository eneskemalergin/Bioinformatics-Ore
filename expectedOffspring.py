import sys

def main():
    # Takes the file name/path from command line argument
    fileName = sys.argv[1]
    # Opens the file to read
    with open(fileName, 'r') as _file:
        # Takes the input and adds to list with float conversion
        f = [float(i) for i in _file.read().split()]
        # Gets the probabilistic value
        prob = (f[0]*1 + f[1]*1 + f[2]*1 + f[3]*3/4 + f[4]*1/2 + f[5]*0)*2

    # Prints the probability with 1 decimal point 
    print('%.1f' % prob)


if __name__ == '__main__':
    main()
