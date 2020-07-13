test_dict = {'Codespeedy' : {'abc' : 5, 'bcd' : 7},  
              'the' : {'def' : None, 'efg' : None},  
              'great' : {'ghi' : 1}} 

print("The original dictionary is : " + str(test_dict)) 

res = {key: sub1 for key, sub1 in test_dict.items() if not
      all(sub2 is None for sub2 in sub1.values())} 
  
print("The dictionary after removal : " + str(res))

dict_data = {'gfg' : {'a' : 1, 'b' : 2},  
              'is' : {'d' : None, 'e' : None},  
              'best' : {'g' : 1}} 

print("The original dictionary is : " + str(test_dict)) 

res = {key: sub1 for key, sub1 in dict_data.items() if 
       any(sub2 is not None for sub2 in sub1.values())} 

print("The dictionary after removal : " + str(res))