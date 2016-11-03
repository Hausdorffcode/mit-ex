##def bad_append(new_item, a_list=[]):
##    a_list.append(new_item)
##    return a_list
##        
##print bad_append('one')
##print bad_append('two')

def good_append(new_item, a_list=None):
    if a_list is None:
        a_list = []
    a_list.append(new_item)
    return a_list

print good_append('one')
print good_append('two')

