""" remplasa basado en una lista de datos
def format_SQL(sql: str) ->str:
    words = ['select','from']
    for i in words:
        sql = sql.replace(i,i.upper())
    return sql

consult = 'select * from users;'
print(format_SQL(consult)) """

""" consultas por listas
consult = ['select * from users;','insert into users values(?)']
def format_SQL(sql: str) ->str:
    words = ['select','from','insert','update','values']
    for i in words:
        sql = sql.replace(i,i.upper())
    return sql
for i in consult:
    print(format_SQL(i)) """

""" se pasa todo a una lista
consult = ['select * from users;','insert into users values(?)']
def format_SQL(sql: str) ->str:
    words = ['select','from','insert','update','values','into']
    for i in words:
        sql = sql.replace(i,i.upper())
    return sql
consults_f = []
for i in consult:
    consults_f.append(format_SQL(i))
print(consults_f) """

def format_SQL(sql: str) ->str:
    words = ['select','from','insert','update','values','into']
    for i in words:
        sql = sql.replace(i,i.upper())
    return sql
consults_f = ['select * from xdxd','insert into xd values']
consults = list(map(format_SQL,consults_f))
print(consults_f)