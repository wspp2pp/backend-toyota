# Backend Toyota

Este es un proyecto Django que brinda soporte al backend para las páginas descriptas en las [especificaciones.](https://www.figma.com/file/GXTK5WFOuIYtRqRFpIaepH/Test_Dev?type=design&node-id=0-1&mode=design)

## Configuración del Entorno

1. **Clonar el Repositorio**: Clona este repositorio en tu máquina local utilizando el siguiente comando:

`git clone https://github.com/wspp2pp/backend.git`


2. **Crear y Activar el Entorno Virtual**: Utiliza `virtualenv` para crear un entorno virtual para este proyecto y luego actívalo. A continuación, se muestran los comandos para hacerlo:


`virtualenv venv`

`source venv/bin/activate`


3. **Instalar Dependencias**: Una vez que el entorno virtual esté activado, instala las dependencias del proyecto ejecutando:

`pip install -r requirements.txt`


## Ejecución del Proyecto

1. **Configuración de la Base de Datos**: Si es necesario, ajusta la configuración de la base de datos en `settings.py`.

2. **Aplicar Migraciones**: Aplica las migraciones al modelo de la base de datos ejecutando:

`python manage.py migrate`


3. **Ejecutar el Servidor**: Inicia el servidor de desarrollo ejecutando:

`python manage.py runserver`


## Endpoints

Aquí se encuentran los principales endpoints de la API y una breve descripción de lo que hace cada uno:

1. **/category/all/**: Lista todas las categorías para la página **Home modelos**
2. **/product/by-category/<category_id>/**: Lista productos por categoría para la página **Home modelos** 
3. **/data-sheet/by-product/<product_id>/**: Devuelve la hoja de datos de un producto para la página **Home modelos dropdown**
4. **/info/all/**: Lista los labels con sus links para la página **Navegacion**

El diseño de los mismos fue pensado desde un punto minimalista, cumpliendo lo necesario para las páginas solicitadas y delegando ciertas tareas al frontend como lo es el ordenamiento de los Products.

## Correr los Test

Para ejecutar los todos tests del proyecto, utiliza el siguiente comando:

`pytest`

O los de una app:

`pytest ./apps/{app}`


