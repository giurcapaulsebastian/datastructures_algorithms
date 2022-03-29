def check_location(list,number,middle):
    #1 5 5 5 12 34 56
    middle_number = list[middle]
    if list[middle] == number:
        if middle-1 >=0 and list[middle-1] == number:
            return "left"
        else:
            return "found"
    if list[middle] > number:
        return "left"
    else:
        return "right"


def binary_search(list, number):
    if list[0] == number:
        return 0
    if list[len(list)-1] == number:
        return len(list)-1
    l,h = 0, len(list)-1
    while l <= h:
        middle = (l+h)//2
        found = check_location(list,number,middle)
        if  found == "found":
            return middle
        elif found == "left":
            h = middle - 1
        elif found == "right":
            l = middle + 1
    return -1


list = [1,5,5,5,12,34,56]
number = 5
poz = binary_search(list,number)
print("Position of number '{}' in the list '{}' is : {}".format(number,list,poz))
