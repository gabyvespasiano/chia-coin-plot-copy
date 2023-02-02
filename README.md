# chia-coin-plot-copy
![Alt text](https://github.com/gabyvespasiano/chia-coin-plot-copy/blob/main/copy.py%20funcionando.jpg?raw=true)
# Aplicación de copia de plots de Chia Coin

Esta aplicación está diseñada para realizar la copia de los plots generados de Chia Coin en diferentes discos de forma eficiente. La aplicación se ejecuta y realiza la copia de un plot a la vez en cada disco para evitar la saturación del sistema de entrada y salida.

## Características
- Copia de plots de Chia Coin en diferentes discos.
- Copia de un plot a la vez en cada disco para evitar la saturación del sistema de entrada y salida.
- Desarrollada en Python para una ejecución rápida y eficiente.

## Requisitos
- Python 3.x instalado en el sistema.
- Acceso a los discos donde se desea copiar los plots.

## Instalación
1. Descargar o clonar el repositorio de la aplicación.
2. Abrir una terminal y navegar hasta la carpeta del proyecto.


## Uso
1. Abrir una terminal y navegar hasta la carpeta del proyecto.
2. Configurar las siguientes variables antes de ejecutar la aplicación:
```
aqui te dejo unos ejemplos de configuracion
(discos)introducir en orden las ubicaciones de los discos
(plots) aqui hay que introducir en orden la cantidad de plots faltantes en los discos 
```
3. Ejecutar el siguiente comando para ejecutar la aplicación:
   ```
    python3 copy.py
    ```

## Ejemplos de configuración de variables
### Ejemplo 1: Tres discos con 20, 15 y 10 plots faltantes respectivamente
```
discos = ["/media/server/disco1/plots","/media/server/disco2/plots","/media/server/disco3/plots"]
plots = [20, 15, 10]
```
### Ejemplo 2: Dos discos con 5 y 8 plots faltantes respectivamente
```
discos = ["/media/server/discoA/plots","/media/server/discoB/plots"]
plots = [5, 8]
```
### Ejemplo 3: Un solo disco con 12 plots faltantes
```
discos = ["/media/server/mi_disco/plots"]
plots = [12]
```


## Contribuciones
Si deseas contribuir a este proyecto, por favor abre una solicitud de extracción o envía un correo electrónico con tus ideas y sugerencias. También puedes reportar errores y solicitar nuevas características en la sección de problemas.
