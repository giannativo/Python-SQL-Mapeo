import sqlalchemy as db
engine = db.create_engine('mysql://root:root@localhost:3306/test')

connection = engine.connect()
metadata = db.MetaData()
persona = db.Table('persona', metadata, autoload=True, autoload_with=engine)

query = db.select([persona])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

query = db.select([persona]).where(persona.columns.nombre == 'gianluca')
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
