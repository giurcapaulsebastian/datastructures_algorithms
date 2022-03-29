def binary_search(list, number):
    if list[0] == number:
        return 0
    if list[len(list)-1] == number:
        return len(list)-1
    l,h = 0, len(list)-1
    while l <= h:
        middle = (l+h)//2
        mid_number = list[middle]
        if  mid_number == number:
            return middle
        elif mid_number > number:
            h = middle - 1
        elif mid_number < number:
            l = middle + 1
    return -1


list = [1,3,4,5,12,34,56]
number = 2
poz = binary_search(list,number)
print("Position of number '{}' in the list '{}' is : {}".format(number,list,poz))
