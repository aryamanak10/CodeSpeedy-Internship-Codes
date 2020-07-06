tuple_data = [[(6, 11), (3, 16)], [(2, 20), (13, 9)], [(7, 16), (4, 18)]]
print("The original list is : " + str(tuple_data))

test_tuple = [(2, 20), (13, 9)]
print("The test row is: " + str(test_tuple))

for i, j in enumerate(tuple_data):
    if j == test_tuple:
        output = []
        for k in j:
            out = (k[0] * 3, k[1] * 4)
            output.append(out)
        tuple_data[i] = output

print("List after modification : " + str(tuple_data))
