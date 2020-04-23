#NO SE MODIFICA LO QUE HAY DENTRO:

SQL_INSERCION_ROPA = "INSERT INTO `tabla_ropa` (id,  prenda , talla , color , temporada , precio , digital , tipo, envio)VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);"  

SQL_SELECT_ROPA ="SELECT id,  prenda , talla , color , temporada , precio , digital , tipo, envio FROM tabla_ropa"

SQL_BORRAR_ROPA = "DELETE FROM tabla_ropa WHERE id = %s ;"
SQL_OBTENER_PRENDA_POR_ID = "SELECT * FROM tabla_ropa WHERE id = %s ;"
SQL_GUARDAR_CAMBIOS_PRENDA = "UPDATE tabla_ropa SET prenda = %s, talla = %s, color = %s, temporada = %s, precio = %s, digital = %s, tipo = %s, envio = %s WHERE id = %s ;"

