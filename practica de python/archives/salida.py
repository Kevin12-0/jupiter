import os

def main(root):
    try:
        file = open(root, 'r')
    except:
        'file dont exits'
        return
    lines = file.readlines()
    file.close()
    column = lines[0].split('')
    values = {}
    for i in range(len(column)):
        values[column[i]] =[]
    for j in range(1, len(lines)):
        words = lines[j].split(",")
        for i in range(len(words)):
            values[column[i]].append(words[i].strip())
    return values
values = main('data.csv')
print(values)