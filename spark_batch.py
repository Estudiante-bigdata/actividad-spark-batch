from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count

# Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("Actividad Spark por Lotes") \
    .getOrCreate()

# Ruta del archivo CSV de ventas
ruta = "/home/vboxuser/actividad_spark_lotes/datos/ventas.csv"

# Leer los datos de ventas
ventas = spark.read.csv(
    ruta,
    header=True,
    inferSchema=True
)

print("=== DATOS DE VENTAS ===")
ventas.show()

# Calcular el valor total de cada venta
ventas = ventas.withColumn(
    "total_venta",
    col("cantidad") * col("precio_unitario")
)

print("=== TOTAL DE VENTAS POR REGISTRO ===")
ventas.show()

# Calcular el total vendido por categoría
print("=== TOTAL VENDIDO POR CATEGORIA ===")
ventas.groupBy("categoria").agg(
    sum("total_venta").alias("total_vendido")
).show()

# Calcular las unidades vendidas por producto
print("=== CANTIDAD DE PRODUCTOS VENDIDOS ===")
ventas.groupBy("producto").agg(
    sum("cantidad").alias("unidades_vendidas")
).orderBy(
    col("unidades_vendidas").desc()
).show()

# Generar el resumen general
print("=== RESUMEN GENERAL ===")
ventas.agg(
    sum("total_venta").alias("ventas_totales"),
    count("*").alias("numero_de_registros")
).show()

# Finalizar la sesión de Spark
spark.stop()
