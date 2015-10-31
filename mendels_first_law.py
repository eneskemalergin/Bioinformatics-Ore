# Get data and store it in
f = open("data/mendels_first_law.txt").readline().rstrip("\n").split(" ")
# Get the values in integer type
k = int(f[0])
m = int(f[1])
n = int(f[2])

# Get the probabilty of having dominant gene from k m n with corresponding successive probabilty
prob = ((k*k - k) + 2*(k*m) + 2*(k*n) + (.75*(m*m - m)) + 2*(.5*m*n))/((k + m + n)*(k + m + n -1))

print prob
