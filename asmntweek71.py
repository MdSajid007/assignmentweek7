def chop(lst):
    if len(lst) >= 2 :
        del lst[0]
        del lst[-1]

def middle(lst):
    if len(lst) >= 2:
        return lst[1:-1]

the_list = [1, 2, 3, 4]
print("My list before calling the chop function =>", the_list)
chop(the_list)
print("My list after calling the chop function =>",the_list)

the_list = [1, 2, 3, 4]
print("\n My list before calling the middle function =>", the_list)

result = middle(the_list)
print("My list after calling the middle function =>", the_list)
print("New list after calling the middle function =>", result)
