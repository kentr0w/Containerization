import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='qweqwe',
        password='test')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'firstname varchar (150) NOT NULL,'
                                 'lastname varchar (50) NOT NULL,'
                                 'email varchar (50) NOT NULL);'
                                 )

# cur.execute('INSERT INTO users (firstname, lastname, email)'
#             'VALUES (%s, %s, %s)',
#             ('Jean',
#              'Claude',
#              'jean.claude@ok.com')
#             )

conn.commit()
cur.close()
conn.close()