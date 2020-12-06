def optimalChange(coin, coins):
  matrix = []
  res = []
  for i in range(len(coins)):
    temp = [0]*(coin+1) # Set arbitrary value 0 in the row eg. [0,0,0,0]
    for j in range(1, coin+1):
      if i == 0:
        # If value of j is divisible by coin in index i 
        # then set value j divided by coin in index i or set infinity
        if j % coins[i] == 0:
          temp[j] = int(j/coins[i])
        else:
          temp[j] = float('inf')
      else:
        # If coin in index i is greater then j 
        # then copy the value from matrix[i-1][j] or set minimum value between 
        # matrix[i-1][j] and 1 + temp[j - coins[i]
        if (j - coins[i]) >= 0:
          temp[j] = min(temp[j - coins[i]] + 1, matrix[i-1][j])
        else:
          temp[j] = matrix[i-1][j]

    matrix.append(temp) # Add row in the matrix
  
  # The value in last row and last column is the minimum number of coins for change
  # If the value is infinity then the solution does not exists.
  x = len(coins) - 1 # Last row
  y = coin # Last Column
  if matrix[x][y] == float('inf'):
    print("Impossible")
  else:
    # If value exist trackback from bottom to top until the y value not 0
    while y != 0: 
      # If the value in matrix[x][y] is equal to matrix[i-1][y] then
      # Only change the x value to x-1 i.e decrease row by one in the same column
      if matrix[x][y] == matrix[x-1][y] and x > 0:
        x = x-1

      # If the value in matrix[x][y] is not equal to matrix[x-1][y] then
      # Add the coin in index x to result array and decrease y value by y - coin in index x
      # i.e decrease column value in the same row
      else:
        res.append(coins[x])
        y = y - coins[x]

    result = {}
    for c in range(len(coins)):
      result[coins[c]] = res.count(coins[c])
    return result

print(optimalChange(20, [2,5,10]))