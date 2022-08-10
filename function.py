
""" Two dictionaries are difined..."""
tom_exp_list = [3000, 2500, 4300, 2100]
bob_exp_list = [4000, 4300, 1200, 1000]

""" Toms' expenses are calculated here through for loop """
total = 0
for i in tom_exp_list:
    total = total + i

print("Toms' total expenses is: ", total)

"""bob expenses are calculated here without using function..."""
total = 0
for i in bob_exp_list:
    total = total + i

print("Bobs' total expense is: ", total)

"""Tom and Bob expenses are calculated right here using function..."""
def calculate_total(exp):
    total = 0
    for items in exp:
        total = total + items

    return total

toms_exp = calculate_total(tom_exp_list)
bobs_exp = calculate_total(bob_exp_list)

print("Toms total expenses are calculated through function & it's: ", toms_exp)
print("Bobs total expenses are calculated through function & it's: ", bobs_exp)

def sum(a,b):
    sum = a+b
    return sum

res = sum(10, 12)
print("Sum of two integers are: ", res)

