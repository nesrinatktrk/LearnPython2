import os
print(os.getcwd())
os.listdir()
for i in os.listdir():
    if i.endswith(".zip"):
        print(i)


    
