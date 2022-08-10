key_location = "chair"
location = ["garage", "living room", "chair", "closet"]
for i in location:
    if i == key_location:
        print("Key found in: ", i)
        break
    else:
        print("Key didn't find in ", i)