nested_list=[[1,2,3],[4,5],[6,7,8,9]]
l1=[x for sublist in nested_list for x in sublist]
print(l1)