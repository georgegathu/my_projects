#  write Python code to read the flag.txt file.
with open("flag.txt", "r") as f:
    flag = f.read()

print(flag)

# The Flag is: THM{F1LE_R3AD}