# Practica Linux

**30 min**

## Comandos
* `ls`
* `cd`
* `file`
* `locate`
* `which`
* `history`
* `whatis`
* `apropos`
* `man`
* `mkdir`
* `touch`
* `mv`
* `rm`
* `rmdir`
* `cat`
* `more`
* `less`
* `grep`
* `head`
* `tail`
* `nano`

# Practica Git 

**20 min**

- Inicialice git en una nueva carpeta en su espacio de trabajo.
 1. `cd` hacía `~/code/scm` and `mkdir` a new folder called `git_practice_SU_NOMBRE`
 2. `cd` hacía ``` git_practice ```
 3. Ejecute ``` git init ``` para inicializar un nuevo repositorio de Git
- Cree 3 archivos nuevos
 1. Ejecute ``` touch file1.txt file2.txt file3.txt ```
- Chequeé el estado (_status_) de su repositorio de Git
 1. Ejecute ``` git status ```

> Observe que los tres archivos que recién créo están marcados como **untracked** 
> porque usted aún no los ha añadido al sistema de Git.
> Git no sabe que quiere usted hacer con esos 
> archivos, por eso los está ignorando.

- Empieze a realizar seguimiento sobre estos archivos añadiendolos a Git
 1. UsEjecutee ``` git add . ``` para mover al _stage_ todos los archivos en el directorio actual que han sido modificados. En este caso, son todos los que se encuentran en la carpeta.
 2. Chequeé el estado de su repositorio de Git ejecutando ``` git status ```

> Observe que ahora los archivos están marcados como **new file**

- Realice _commit_ sobre sus cambios
 1. Ejecute ``` git commit -m "Una breve descripción de los cambios realizados" ```
- Modifique el contenido de algunos de sus archivos
 1. Chequeé el estatus (_status_) del repositorio con ``` git status ```

> Observe que sus archivos ahora están marcados como **modified**

- Mueva sus archivos al _stage_ para integrarlos al siguiente _commit_
 1. Ejecute ``` git add . ``` para mover al _stage_ los archivos modificados
- Realice _commit_ sobre sus nuevos cambios
 1. Ejecute ``` git commit -m "Una breve descripción de los cambios realizados" ```
- Consulter la historia de los _commits_
 1. Ejecute ``` git log ``` para ver la historia de los commits realizados

### Bonus

- Intentar eliminar `file3.txt` de su repositorio ejecutando `git rm file3.txt`
- Intenrar renombrar alguno de los archivos ejecutando `git mv`

Traducido de https://gist.github.com/mdang/d87dea19e41ac808538040141223e9c8


# Practica Git 

Abra una Terminal

Pegue el siguiente texto, sustituyendo por su correo asociado a GitHub

``` $ ssh-keygen -t ed25519 -C "your_email@example.com" ```
> Nota: Si se encuentra en un sistema obsoleto que no soporta la encripción Ed25519, ejecute:

``` $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com" ```

Este comando creará una nueva llave SSH, usando el correo como etiqueta.
> Generating public/private algorithm key pair.

Cuando aparezca el texto "Enter a file in which to save the key," presione la tecla Enter. Esto aceptará crear el archivo en la ubicación por defecto.
> Enter a file in which to save the key (/home/you/.ssh/algorithm): [Press enter]

Cuando aparezca el siguiente texto, ingrese un _passphrase_ seguro. For more information, see ["Working with SSH key passphrases."](https://docs.github.com/en/articles/working-with-ssh-key-passphrases)
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]

Fuente: [generating-a-new-ssh-key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)