# Week 2: Lists, loops, and functions
a_very_diverse_list = ['my', 1, 4.5, ['you', 'they', True], 432, -2.3, 33, [False, 1]]

# len(): number of list hold
print(len(a_very_diverse_list))

# .append(): plus element at last
a_very_diverse_list.append('a new element!')

# print(): show list holding elements
print(a_very_diverse_list) # print(): show list holding elements

# list[number]: the list element from list number (from 0 to number), number+1(from 1 to number+1)
print(a_very_diverse_list[8]) # show the 8th element (from 0 to number)

# list[-number]: the element form last number
print(a_very_diverse_list[-2]) # show the last 2nd element (from 0 to number)

# list [number][number]: the element from list's element from 0 to number)
print(a_very_diverse_list[3][2]) # list里第3个因素（第三个因素为list），第三个因素列里的第二个因素（from 0 to number)

# Index slicing
#If we want more than just one element, we can get a slice of the list.
# my_list[start:stop] gets all elements from position start to stop-1.
# my_list[start:stop:step] gets every stepth element from position start to stop-1.

my_list = ['zero', 'one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine', 'ten', 'eleven']
# list[start:stop]：list里的第start个元素，到第stop-1个元素(from 0)
print(my_list[0:12])
# list[start:stop:step] list里的第start个元素，每第step个元素(原element为第0个开始），到第stop-1个元素(from 0)
# list[start:stop:step]  list里的第start个元素，每次间隔step-1个元素，到第stop-1个元素(from 0)
print(my_list[0:12:3]) # 从第0到12-1=11个元素，每次间隔3-1=2个元素
print(my_list[0:12:4])# 从第0到12-1=11个元素，每次间隔4-1=3个元素

# for loops
my_list_cap = [] # creat a new list
# .capitalize()) 返回原字符串的副本，其首个字符大写，其余为小写
# new_list.append(list[n].capitalize()):把my_list的第n个元素(from 0)首字母大写放进新列表new list(my_list_cap)
my_list_cap.append(my_list[0].capitalize()) # 把my_list的第0个元素(from 0)首字母大写放进新列表new list(my_list_cap)
my_list_cap.append(my_list[1].capitalize()) # 把my_list的第1个元素(from 0)首字母大写放进新列表new list(my_list_cap)
my_list_cap.append(my_list[2].capitalize()) # 把my_list的第2个元素(from 0)首字母大写放进新列表new list(my_list_cap)
my_list_cap.append(my_list[3].capitalize()) # 把my_list的第3个元素(from 0)首字母大写放进新列表new list(my_list_cap)
print(my_list_cap) # show new list with new elements

# for element in list: 把list里的元素命名为element
# for...in..: 循环list里的所有element
#   new_list.append(number.capitalize()) 在new_list里加入element并首字母大写
my_list_cap1=[]
for number in my_list: # 把my_list里的元素命名为number
    my_list_cap1.append(number.capitalize())
print(my_list_cap1)












