def dirReduc(arr):
    ... your code




a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])