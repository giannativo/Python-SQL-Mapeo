import sqlalchemy as db
engine = db.create_engine('mysql://root:root@localhost:3306/test')

connection = engine.connect()
metadata = db.MetaData()
persona = db.Table('persona', metadata, autoload=True, autoload_with=engine)

query = db.select([persona])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

query = db.select([persona]).where(persona.columns.nombre == 'Nahuel')
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

query = db.insert(persona).values(nombre='Juan Román', apellido='Riquelme')
ResultProxy = connection.execute(query)

query = db.select([persona])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)