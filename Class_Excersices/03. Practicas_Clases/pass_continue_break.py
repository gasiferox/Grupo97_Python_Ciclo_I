some_list = [0,1,2,3,4]

for element in some_list:
    if element == 1:
        print("Pass executed")
        pass
    print(element)

for element in some_list:
    if element == 1:
        print("Pass executed")
        continue
    print(element)

for element in some_list:
    if element == 1:
        print("Pass executed")
        break
    print(element)
