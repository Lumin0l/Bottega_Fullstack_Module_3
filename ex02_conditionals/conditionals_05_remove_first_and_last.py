# How to remove first and last elements of lists using conditionals:

# My attempt
def remove_first_and_last(list_to_clean):
    index_start = 1
    index_end   = (len(list_to_clean) - 1)

    new_list = list_to_clean[index_start:index_end]

    return new_list

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(remove_first_and_last(ls))

# His solution:
# Shows something completely out of his rear:
# one, *two, three = [1, 2, 3, 4, 5]:
# This will assign 1 to 'one', 5 to 'three' and everything else to 'two'

def remove_solution(list_to_clean):
    _, *content, _ = list_to_clean
    return content

print(remove_solution(ls))
