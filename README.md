Actividad de Spark Batch

Descripción

En esta actividad se utiliza Apache Spark para analizar los datos de ventas de una miscelánea almacenados en el archivo ventas.csv. El programa permite calcular el valor de las ventas, conocer los productos más vendidos y consultar los resultados por categoría.

Herramientas utilizadas

Python.

Apache Spark 3.5.8.

Archivo de datos ventas.csv.

Cómo ejecutar el programa

Tener instalado Apache Spark y Python.

Guardar el archivo ventas.csv en la carpeta de datos indicada en el programa.

Abrir una terminal y ejecutar el siguiente comando:

spark-submit ~/actividad_spark_lotes/spark_batch.py

Resultados

Al ejecutar el programa se muestran los registros de ventas, el valor de cada venta, los totales por categoría, las unidades vendidas por producto y el resumen general.
```

El programa muestra en la terminal los registros, el valor de cada venta, el total por categoría, las unidades vendidas por producto y el resumen general.

> Nota: la ruta del archivo CSV que utiliza el programa corresponde al entorno de Ubuntu usado para esta actividad. Si se ejecuta en otro equipo, se debe ajustar la variable `ruta` en `spark_batch.py`.
