#EL PROCEDIMIENTO CON BASES DE DATOS ES:
#1.CONECTAR  -- 2. OPERAR --- 3.DESCONECTAR

import mysql.connector
from modelo import constantes_sql

#para conectar con nuestra base de datos:

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost", #nos vamos a conectar con la bd q esta instalada en nuesstro equipo
        user = "root",
        database = "bd_ropa"
        
        )
    return conexion

def registro_ropa(ropa):
    sql = constantes_sql.SQL_INSERCION_ROPA
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_insertar = (ropa.prenda, ropa.talla ,ropa.color, ropa.temporada ,ropa.precio)
    cursor.execute(sql , valores_a_insertar )
    conexion.commit()
    conexion.disconnect()
    
def obtener_ropa():    
    sql = constantes_sql.SQL_SELECT_ROPA
    conexion= conectar()
    cursor=conexion.cursor()
    cursor.execute(sql)
    lista_resultado= cursor.fetchall()
    conexion.disconnect()
    return lista_resultado

def borrar_ropa(id_ropa):
    sql = constantes_sql.SQL_BORRAR_ROPA
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id_ropa,)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()
    
    
