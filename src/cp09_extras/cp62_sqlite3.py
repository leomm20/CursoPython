import sqlite3


def crear_tabla():
    conexion.execute("""
    create table if not exists articulos (codigo integer primary key autoincrement, descripcion text, precio real)""")


def leer_datos():
    cursor = conexion.execute("select codigo, descripcion, precio from articulos")
    print(cursor.fetchall())


def insertar_datos():
    conexion.execute("insert into articulos (descripcion,precio) values ('naranjas', 23.50)")
    conexion.execute("insert into articulos (descripcion,precio) values (?,?)", ("peras", 34))
    conexion.commit()


def actualizar_datos():
    conexion.execute("update articulos set descripcion = 'manzanas', precio = 35 where codigo = 3")
    conexion.commit()


def eliminar_datos():
    conexion.execute("delete from articulos where codigo > 3")
    conexion.commit()


conexion=sqlite3.connect("cp62_sqlite.db")  # Si no existe el archivo, lo crea

crear_tabla()
insertar_datos()
leer_datos()

conexion.close()
