#  lambda argument:expression
# map is used to perform a fn on each element of collection
# filter 
# reduce



# def even_no(i):
#     return i%2==0

# iseven= lambda i:i*3

# list1= (10,20,30,40,50)
# # evenno= list(filter(even_no,list1))
# # print(evenno)
# # even_no1= list(filter(iseven,list1))
# # print(even_no1)

# sqlist= list(map(lambda i:i*3,list1))
# print(sqlist)

# tuple1={80,90,97,98,89}
# marks= lambda i:i>90
# mar
from functools import reduce
list1=[1,2,3,4,5,6]
sum = reduce(lambda i,j: i+j,list1)
print(sum)

