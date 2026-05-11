with open("example.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())


# # file = open("names.txt", "a")
# file.write(f"{name}\n")
# # file.close() 