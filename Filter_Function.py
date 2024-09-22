def fun(t): # for printing the count >=2
    return t[1]>=2
d = {'harry': 2, 'hermonie': 2, 'ron': 3, 'snape': 1, 'dumbledore': 1, 'hagrid':1}
#print(d.items()) #outputs dict_items([('harry', 2), ('hermonie', 2), ('ron', 3), ('snape', 1), ('dumbledore', 1), ('hagrid', 1)])
print(list(filter(fun, d.items())))
