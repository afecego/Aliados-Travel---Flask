# Aliados Travel - Flask
 
Servicio usando Flask como framework, dentro del cual se requieren los dos siguientes endpoints:

1. Reciba un conjunto de números y los ordene aplicando un algoritmo de ordenamiento y los retorne en formato json

_En el siguiente endpoint se anexa numero entero, que sera ordenado de menor a mayor_

```
/numeros/<int:numeros>
```

2. Reciba el nombre de un archivo de texto y retorne el número de mayúsculas que haya en el, el código debe soportar cualquier tamaño de archivo

_En el siguiente endpoint se debe anexar el nombre del archivo sin la extension "txt"_

```
/libro/<libro>
```

Para ejecutar el servicio, se ejecuta el comando **flask run** y usara el **localhost** en el puerto **5000** por default
