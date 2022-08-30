# Modelo de riesgo de crédito
Julian Esteban Carvajal Ramírez 1001774262
Wilfer Mauricio Chavarría Jaramillo 1035833003
Alejandro Bedoya Taborda 1152226157

Link del aplicativo: http://tae-entrega2.herokuapp.com/index/inicio/-/

# **REPORTE TÉCNICO**

**INTRODUCCIÓN**

La industria de los servicios financieros es un mercado que cada día está creciendo y evolucionando constantemente, esto lleva a que diversas empresas inviertan más dinero en estadísticos predictivos para aumentar sus ganancias y reducir los riesgos de inversión.

Este documento se centra en los préstamos de dinero y la probabilidad de que una persona pague responsablemente su deuda, para calcular esta probabilidad, normalmente las entidades bancarias tienen en cuenta el “puntaje crediticio” Gracias a esa clasificación, analizan su historial de pago, reporte a centrales de riesgo y crean un perfil sobre su capacidad económica para aprobar o no créditos. El puntaje crediticio, también llamado score, se mide de 0 a 1.000 puntos. Este depende de varios factores, por ejemplo: cumplimiento del pago de cuotas de otros créditos, nivel de endeudamiento de las personas y pagos de telefonía móvil, entre otros.

**OBJETIVO**

- Crear y validar un modelo de probabilidad de incumplimiento para la base de datos loan_data_2007_2014.csv suministrada por el profesor en el curso.
- Representar con datos estadísticos en un modelo scorecard los resultados obtenidos.
- Analizar qué posibles variables hacen que una persona presente una mayor probabilidad de no pagar el préstamo.
- Presentar todos los resultados obtenidos en una aplicación web y dar explicación de los mismos. 

**BASE DE DATOS**

La base de datos utilizada es este proyecto es loan_data_2007_2014.csv (https://classroom.google.com/c/NDc0MTYzNDgwNzI3/a/NDg2NTU0MjYwMjcw/details) suministrada por el profesor.

Para el análisis de esta base de datos, se hace un trabajo de pre-procesamiento de datos, el cual consiste en: 
Eliminar todas las variables o campos que contengan el 80% o más de datos nulos o casillas vacías.
Realizar un data cleaning para las variables que son candidatas de llevar a la simulación como lo son 'emp_length' y 'term' que requieren ser llevadas a tipo numérico y llevaremos las columnas con fechas al formato de fecha de python.
Se realiza la prueba del Chi-cuadrado para las variables características categóricas y el estadístico F de ANOVA para las características numéricas.
Se seleccionan las variables a incluir en el modelo
Después de explorar y limpiar los datos de la base de datos, procedemos a aplicar las técnicas de WoE y VI Con base en la proporción de buenos y malos solicitantes en cada nivel de grupo, este método mide la "fuerza" de la agrupación para diferenciar el riesgo bueno y el malo e intenta encontrar una relación monótona entre las variables independientes y la variable objetivo.

Por último se calcula la probabilidad de cumplimiento de pago de cada individuo, a partir de estos datos se pueden obtener resultados y conclusiones.

**RESULTADOS**

1. Se usa el método de precisión Accuracy el cual mide el porcentaje de casos que el modelo ha acertado, obteniendo un resultado aproximado del 80% (0,7920%) de aciertos, lo cual es un buen porcentaje de aciertos.


2. Para reforzar los resultados anteriores se usa el valor F1 el cual es la media armónica del accuracy (precisión) y el recall que mide que tan bueno es el modelo prediciendo clases positivas, entre más cercano a 1, significa que el modelo tiene alto accuracy y recall, arrojando un resultado de 0,8262. indicando que el modelo está entre los parámetros de aceptación.


3. Se evalúa la matriz de confusión la cual es una herramienta que permite visualizar el desempeño de un algoritmo  de aprendizaje supervisado. La matriz de confusión se lee diagonalmente, por lo que 8.200 se predijeron correctamente como 'mala paga' y 66.000 se predijeron correctamente como 'buena paga' aproximadamente (Ver en el apartado "Matriz de Confusion").

4. Se calcula la probabilidad de cada sujeto de pagar debidamente su deuda en un plazo de 12 meses y se separan en grados de la A a la G y se puede observar que los que se encuentran en Grado A tienen la ayor probabilidad de pagar su deuda en los siguientes 12 meses después de adquirir su crédito.

5. Se realiza un ScoreCard para la asignación de puntaje de todos los individuos, puntaje que está entre el rango de 0 a 1.000, este puntaje se separa en las siguientes categorías: Puntaje mayor a 746: Riesgo muy bajo, Puntaje entre 646 y 745: Riesgo bajo, Puntaje entre 476 y 645: Riesgo moderado, Puntaje entre 421 y 475: Riesgo medio, Puntaje entre 386 y 420: Riesgo medio, Puntaje entre 341 y 385: Riesgo medio, Puntaje entre 301 y 340: Riesgo medio, Puntaje entre 261 y 300: Riesgo alto, Puntaje entre 150 y 260: Riesgo muy alto.
En lo que se puede observar que la gran mayoría de la población se encuentra en las categorías menores a 600 puntos, donde los grupos predominantes son C, D, E, F y G, los cuales corresponden a los grupos con menos probabilidad de cumplir con sus compromisos financieros en los primeros 12 meses de su crédito y por el contrario los grupos A y B que cuentan con la mayor probabilidad de pagar su crédito son los que presentan un mayor puntaje en este ScoreCard validando este modelo.

**CONCLUSIONES**

- Se puede concluir que el modelo usado para asignar el puntaje ScoreCard es confiable y que las variables tomadas dan una estimación acertada.
- Cuando se analiza cuántos créditos fueron pagados en su totalidad correctamente, nos muestra que alrededor del 89% de los individuos pagaron correctamente su deuda, sin embargo, al analizar el pago oportuno de los créditos en un plazo de 12 meses a partir de la adquisición del crédito, nos arroja que menos del 20% de los individuos han pagado correctamente sus cuotas. - Esto quiere decir que en los primeros 12 meses es normal que se presenten incumplimientos con el pago de las cuotas, porque al final del plazo pactado es mucho mayor el porcentaje de personas que si pagan correctamente su deuda.
- Al analizar el cumplimiento del pago de las cuotas de cada préstamo en los primeros 12 meses, arroja un ScoreCard más bajo que analizándolo en el tiempo total del préstamo.
- El no pagar todas las cuotas de un préstamo puntualmente puede bajar el puntaje de ScoreCard drásticamente.
Para este análisis se concluye que si se va a realizar un préstamo con duración de 12 meses, solo las personas del grupo A son aceptadas para el préstamo, o en otras palabras, aquellas personas que tengan un ScoreCard superior a 600 puntos.

**RECOMENDACIONES**

- Si se desea realizar préstamos con duración de más de 12 meses, se recomienda analizar nuevamente cada sujeto en el tiempo en que desee sacar el crédito, para tener una puntuación de ScoreCard más precisa y una probabilidad de pago total de la deuda igual de precisa.
- Se recomienda que al momento de la recolección de datos, se aseguren de no tener valores nulos, pues al depurar la base de datos esto generó mucha pérdida de información valiosa.
- Se recomienda Realizar un análisis más profundo de la probabilidad de pago de cada individuo mes a mes, pues esto cambiaría significativamente los resultados de la puntuación de ScoreCard.
