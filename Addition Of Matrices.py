X = [[1, 12, 13],
     [15, 7, 16],
     [17, 12, 9]]

Y = [[10, 8, 7],
     [25, 15, 13],
     [12, 14, 1]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)