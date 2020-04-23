#EL PROCEDIMIENTO CON BASES DE DATOS ES:
#1.CONECTAR  -- 2. OPERAR --- 3.DESCONECTAR

import mysql.connector
from modelo import constantes_sql, clases

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
    valores_a_insertar = (ropa.prenda, ropa.talla ,ropa.color, ropa.temporada ,ropa.precio, ropa.digital, ropa.tipo, ropa.envio)
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
    
def obtener_prenda_por_id(id):
    sql = constantes_sql.SQL_OBTENER_PRENDA_POR_ID
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    cursor.execute(sql,val)
    resultado = cursor.fetchone()
    print(resultado)
    conexion.disconnect()
    #meter el resultado en un objeto de la clase libro
    prenda = clases.Prenda()
    prenda.id = resultado[0]
    prenda.prenda = resultado[1]
    prenda.talla = resultado[2]
    prenda.color = resultado[3]
    prenda.temporada = resultado[4]
    prenda.precio = resultado[5]
    prenda.digital = resultado[6]
    prenda.tipo = resultado[7]
    prenda.envio = resultado[8]
    return prenda

def guardar_cambios_prenda(prenda_a_guardar_cambios):
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_PRENDA
    conexion = conectar()
    cursor = conexion.cursor()
    val = (prenda_a_guardar_cambios.prenda, prenda_a_guardar_cambios.talla, prenda_a_guardar_cambios.color, prenda_a_guardar_cambios.temporada, prenda_a_guardar_cambios.precio, prenda_a_guardar_cambios.digital, prenda_a_guardar_cambios.tipo, prenda_a_guardar_cambios.envio, prenda_a_guardar_cambios.id)
    try:
        cursor.execute(sql,val)
    except Exception as e:
        print(e)
        
    conexion.commit()
    conexion.disconnect()
    
    
