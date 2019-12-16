#lst = list()
#lst = []
lst = [1,200,3, 1]

print(5 in [2, 3, 5])   #True -потому что есть 
print(5 not in [2, 3, 5])
print([2, 4] + [5, 3])
print([2, 3] * 3)
print(lst[0] / lst[1])
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
print(lst.index(200))
print(lst.count(1))
print(lst.append(99))

del lst[0]
print(lst)

lst.clear()
print(lst)

newlist = lst.copy()
print("новый список", newlist)
print("старый список", lst)