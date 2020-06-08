# Expresion_Lambda_Recursiva
## Funciones lambda
Las funciones lamda son también conocidas como funciones anónimas porque se definen sin un nombre.
Algunas de sus características son:
- Pueden definir cualquier número de parámetros, pero una única expresión. Esta expresión es evaluada y devuelta.
- Pueden ser usadas en cualquier lugar que la función sea requerida.

### Sintaxis
La sintaxis para definir una función lambda es la siguiente:
~~~
  lambda parámetros: expresión
~~~

### Ejemplo
A continuación, se presenta una función sencilla y cómo se podría expresar mediante una función lambda:
~~~
  #Función sencilla
  def cuadrado(x)
    return x**2
    
  #Función lambda
  cuad = lambda x: x**2
~~~

### Función lambda recursiva
Al igual que con las funciones tradicionales, las funciones lambda pueden ser usadas de manera recursiva, es decir que la función se llame a ella misma. A continuación, un ejemplo:
~~~
  #Función lambda recursiva para hallar el factorial de un número
  lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
  print(lambda_factorial(5))
~~~
Para usar una función lambda de forma recursiva es necesario que guardemos la expresión lambda en una variable, esto nos permitirá luego hacer su llamado de forma recursiva como se ve en el ejemplo. 

|Nombre|Código|
|-----------|-----------|
|Juan Esteban Olaya García|20171020135|
