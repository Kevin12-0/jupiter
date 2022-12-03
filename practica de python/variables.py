words = ['select','from']
consult = 'select * from users;'

for i in words:
    consult = consult.replace(i,i.upper())
print(consult)