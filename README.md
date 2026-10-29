# Actividad de Spark Batch: análisis de ventas

## Descripción

Este proyecto utiliza Apache Spark y Python para procesar los datos de ventas de una miscelánea almacenados en un archivo CSV. Calcula el valor de cada venta, el total vendido por categoría, las unidades vendidas por producto y un resumen general.

## Herramientas

- Python
- Apache Spark 3.5.8
- Archivo de datos CSV

## Estructura esperada

El archivo de datos debe llamarse `ventas.csv` y estar disponible en:

`/home/vboxuser/actividad_spark_lotes/datos/ventas.csv`

El CSV debe incluir las columnas `fecha`, `venta_id`, `producto`, `categoria`, `cantidad` y `precio_unitario`.

## Cómo ejecutar

En la máquina virtual Ubuntu donde está instalado Spark, ejecutar:

```bash
spark-submit ~/actividad_spark_lotes/spark_batch.py
```

El programa muestra en la terminal los registros, el valor de cada venta, el total por categoría, las unidades vendidas por producto y el resumen general.

> Nota: la ruta del archivo CSV que utiliza el programa corresponde al entorno de Ubuntu usado para esta actividad. Si se ejecuta en otro equipo, se debe ajustar la variable `ruta` en `spark_batch.py`.
