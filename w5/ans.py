list1 = open('no.txt' ,'r')
list2 = open('yes.txt','r')

s1 = set(list1)
s2 = set(list2)
print ('二乙')
print (list(s1.symmetric_difference(s2)))