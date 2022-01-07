#question 5:
#(a) print a list and then remove 4th element from the list and let it print the new list
#(b) remove 'Black' and 'Pink' from the list and replace it with 'Purple'

color_list=['Red','Green','White','Black','Pink','Yellow']
# code part a
print('(a)')
print(color_list)
# remove 4th element Black
color_list.remove('Black')
print("answer part a ",color_list)

color_list=['Red','Green','White','Black','Pink','Yellow']
# code part b
print('(b)')
print(color_list)
#replace black and pink with purple
# to replace nth element we write {my_list[n-1]='new value'}
color_list[3:5]=['Purple']
print(" answer part b",color_list)