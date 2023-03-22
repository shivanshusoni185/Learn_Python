def count_frequency(**kwargs):
    dict1={}
    for i,j in kwargs.items():
        for num in j:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        print(f"Frequency of number in {i}:{dict1}")
        dict1.clear()

list1=[1,2,3,2,4,3,5]
list2=[2,3,3,2,5,6,7,7,]
count_frequency(lst1=list1,lst2=list2)
