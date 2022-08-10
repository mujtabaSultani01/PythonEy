dic = {
    "Tom": 938745943,
    "Jeo": 938474857,
    "Bob": 983475498

}
print(dic)
print("Tom phone number is: ", dic["Tom"])

for key in dic:
    print("Keys: ", key, "\nvalue: ", dic[key])

""" to delete a specific record."""
del dic["Jeo"]
print("Jeo record is deleted.")
print(dic)
""" to delete entire dictionary."""
dic.clear()
print("all records are deleted.")



print(dic)