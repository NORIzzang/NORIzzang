str = "   Life is too short, you need a python   "
if "Life is too short, you need a python" == str:
    print("same")
else:
    print("different")

result = str.lstrip()
print(result)
print(str)

if "Life is too short, you need a python   " == result:
    print("same")
else:
    print("different")
