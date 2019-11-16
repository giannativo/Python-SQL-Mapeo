# Python-SQL-Mapeo
Breve ejemplo de como conectar una base de datos MySQL a un proyecto Python.

Setup:

En la consola:
Instalar libreria de virtualenv con el siguiente comando:
py -m pip install --user virtualenv

En directorio del proyecto, crear un virtualenv con el siguiente comando:
py -m venv env

Activar entorno con el siguiente comando:
.\env\Scripts\activate

Chequear que el entorno este activado viendo si aparece "(env)" a la izquierda del directorio en la consola

Instalar librerias con el siguiente comando:
pip install -r requirements.txt

Si agregas una liberia nueva actualizar archivo requirements:
pip freeze > requirements.txt

Ir a mysql, conectarse al server local, y correr el script para crear la base de datos, luego cargarla con datos.

Para ejecutar proyecto en pycharm:
Ir a file - settings - project interpreter y seleccionar existing environment, en la opcion de interpreter buscar el ejecutable python del entorno virtual creado en el directorio del proyecto.

