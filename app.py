#Exercise-1: print code horizonatally
#annotations: Print function has end parameter, it has escape character(end="\n"), 
#remove the escape character and replace it with empty string (end="")

list1 = [1, 2, 3, 4]
for number in list1:
    print(number, end="")

# print function has another parameter sep, used to separate output
print('02', '02', '1988', sep='/')

#Exercise-2: Merging Dictionaries
#note: use merge(I) operator or the (**) operator
name1={"polo:": 39, 
       "wadia":4}
name2={"tania":35}
#mehtod1
names=name1|name2
print(names)

#mehtod2
names={**name1, **name2}
print(names)