immutable_var = ([1], [2], [3], True, False)
print(immutable_var)
print(immutable_var.__sizeof__())
immutable_var [2][0] = 5
print(immutable_var)
mutable_list = [100, 200, 300, 400, 500]
print(mutable_list)
mutable_list [0] = 500
mutable_list [1] = 400
mutable_list [2] = 300
mutable_list [3] = 200
mutable_list [4] = 100
print(mutable_list)