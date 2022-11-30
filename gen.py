import os

temp = '' 
with open('template.py', 'r') as f:
    temp = f.read()

for i in range(25):
    dirname = f'day_{i + 1}'
    if (os.path.isdir(dirname)): continue;
    os.mkdir(dirname) 
    with open(f'{dirname}/main.py', 'w') as f:
        f.write(temp)
