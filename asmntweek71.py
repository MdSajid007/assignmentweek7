def chop(lst):
    if len(lst) >= 2 :
        del lst[0]
        del lst[-1]

def middle(lst):
    if len(lst) >= 2:
        return lst[1:-1]

the_list = [1, 2, 3, 4]
print("My list before call chop function =>", the_list)
chop(the_list)
print("My list after call chop function =>",the_list)

the_list = [1, 2, 3, 4]
print("\n My list before call middle function =>", the_list)

result = middle(the_list)
print("My list after call middle function =>", the_list)
print("New list after call middle function =>", result)
