tuple_data = [[(6, 10), (3, 16)], [(2, 20), (13, 9)], [(7, 16), (4, 18)]] 
print("The original list is : " + str(tuple_data)) 
 
test_tuple = [(2, 20), (13, 9)]
print("The test row is: " + str(test_tuple))

output = [[(i[0] * 2, i[1] * 4) for i in list_tuple] if list_tuple == test_tuple else list_tuple for list_tuple in tuple_data]
print("List after modification : " + str(output)) 