def split_in_two(lijst):
    middle = len(lijst) // 2
    return (lijst[:len(lijst)//2], lijst[len(lijst)//2:])



def merge_sorted(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


left, right = split_in_two([1, 2, 4, 3, 5, 6])
#print((left,right))
#print(merge_sorted(left,right))

print(merge_sorted([5],[6]))


def merge_sort(ns):
    if len(ns) <= 1:
        return ns
    else:
        left , right = split_in_two(ns)


        sorted_left = merge_sort(left)
        


        sorted_right = merge_sort(right)
        

        return merge_sorted(sorted_left, sorted_right)    


print(merge_sort([2,5,6,1,3,4]))