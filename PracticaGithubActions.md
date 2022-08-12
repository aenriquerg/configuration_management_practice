
# Guia Github actions.

Prerequisitos:
* [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/)


```
name: # Es el nombre de su workflow. Este nombre se muestra al momento de la ejecución del workflow.

on: #Se hace uso de esta etiqueta para ejecutar automaticamente el workflow basado en un evento. 

jobs: # Los workflows se encuentran compuestos por uno o varios jobs.
  JOB_NAME:
    runs-on: # Cada job debe especificar en qué ambiente se va a ejecutrar. Linux, Windows o Mac
    steps: # Los jobs se encuentran compuestos por steps. Los steps definen los pasos a realizar.
    - name:
      uses:
    ...
```

En el siguiente link se encuentran todos los eventos disponibles para iniciar un workflow en el apartado `on` : [_Events that trigger workflows_](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) 

Ambientes disponible para `runs-on`: [Choosing GitHub-hosted runners](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#choosing-github-hosted-runners)

## Construyendo proceso básico de integración continua. 

1. Creamos la carpeta `mkdir -p .github/worflows`
2. Creamos el archivo `touch .github/workflows/ci.yaml`
3. Copiamos el contenido que se muestra a continuación en el archivo `ci.yaml`. 
   
```
name: Continous Integration 

on: [push]

jobs:
  continous_integration:
    runs-on: ubuntu-latest
    steps:
    - name: Code checkout
      uses: actions/checkout@v3
    - name: Set up Python 3.8
      uses: actions/setup-python@v3
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
        pip install pytest
        pip install -r requirements.txt
    - name: Static code analysis with pylint
      run: |
        pylint myapp.py
    - name: Unit test with pytest
      run: |
        pytest myapp_test.py
```
4. Realizamos un _commit_ en nuestro repositorio local y luego _push_ para subir al repositorio remoto.
5. Vamos a nuestro proyecto en Github y nos dirigimos a la pestaña *Actions*

## Construyendo proceso básico de entrega continua. 

1. En la carpeta raiz de su proyecto creamos el archivo `touch Dockerfile`. Luego copiamos el siguiente código en el archivo. 
```
FROM python:3.8-alpine

WORKDIR /myproject

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY myapp.py .

EXPOSE 8000
CMD ["python","./myapp.py"]
```
2. Creamos el archivo `touch .github/workflows/cd.yaml`
3. Copiamos el contenido que se muestra a continuación en el archivo `cd.yaml`. 
```
name: Continous delivery

on:
  workflow_run:
    workflows: [ "Continous Integration" ]
    types: [ completed ]
    branches: [ master ]

jobs:
  on-success:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:
    - name: Code checkout
      uses: actions/checkout@v3
    - name: Build the Docker image
      run: docker build . --file Dockerfile --tag myapp:$(git rev-parse --short HEAD)
```
4. Realizamos un _commit_ en nuestro repositorio local y luego _push_ para subir al repositorio remoto.
5. Vamos a nuestro proyecto en Github y nos dirigimos a la pestaña *Actions*