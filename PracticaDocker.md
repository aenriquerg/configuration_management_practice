# Práctica Docker

**Lista comandos**
  * `docker run NOMBRE_IMAGEN`
  * `docker image pull NOMBRE_IMAGEN`
  * `docker image ls`
  * `docker ps` o `docker container ls`
  * `docker exec`

Página web para la práctica: https://labs.play-with-docker.com/ 

## 1. Ejecutando una imagen de Docker

Es momento de empezar a prácticar lo que hemos aprendio de docker!

Escribe o copia el siguiente comando para ejecutar su primer contenedor de Docker.

* `docker run hello-world`

¿Qué vemos en la consola?

## 1.1 Ejecutando una imagen de Docker

Primero vamos a descargar la imagen de `alpine`. `alpine` es una versión ligera de un sistema linux.

* `docker image pull alpine`
* `docker image ls` o `docker images`
* `docker run alpine ls`

## 1.2 Ejecutando un servidor web

Ahora vamos a descargar la imagen del conocido sevidor web [Nginx](https://www.nginx.com/).

* `docker image pull nginx`
* `docker run nginx`


## 2 Creando y ejecutando un API en Python


* `pip3 install virtualenv`
* `virtualenv .env3 -p python3`
* `source .env3/bin/activate`
* `touch app.py`
* `vim app.py`
* Copiar contenido de [myapp.py](./myapp.py)
* `python app.py`
* `pip install uvicorn`
* `pip install fastapi`
* `python myapp.py`
* `pip freeze > requirements.txt`
* `deactivate`

## 3 Creando una imagen de Docker con Dockerfile

* `touch Dockerfile`
* Copiar contenido de [Dockerfile](./Dockerfile)
* `docker build . -t myapp`
* `docker images`
* `docker run myapp`
* `docker run -p 8000:8000 myapp`

Recursos
* [Firts Alpine Linux Containers](https://training.play-with-docker.com/ops-s1-hello/)

