# Test Joke

Test joke es una aplicacion de chistes
la ejecutamos de la siguiente forma:

instalamos pipenv
```pip install pipenv```
luego instalamos las dependencias
```pipenv install```
ejecutamos una shell en un entorno virtual
```pipenv shell```
Ahora luego de haber creado la base de datos y de configurarla en el archivo jokes.py en la variable engine abrimos la consola de python ejecutando:
```python```
luego creamos la tabla "Jokes" de la siguiente forma
```python
from jokes import Base, engine
Base.metadata.create_all(engine)
```
por ultimo cerramos la terminal
```python
exit()
```

e iniciamos el servior
```flask run```
## Tests

para ejecutar las pruebas unitarias ejecutamos
```python -m pytest tests/```
