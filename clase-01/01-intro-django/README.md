# Empezando a trabajar con DJANGO

## Creamos el entorno

```sh
py -m venv .entorno # Esto crea la carpeta .entorno
```

```sh
.\.entorno\Scripts\activate
source .entornoS/bin/activate # Linux/macOS
```

# Instalando DJANGO

<https://pypi.org/project/Django/>

```sh
pip install Django
```

## Averiguar versión de DJANGO

```sh
py -m django --version
# 6.1.1
```

# Creando un proyecto con DJANGO
El proyecto reune configuración y aplicaciones para un mismo sitio. Es el director tecnico de nuestros módulos. 

```sh
py -m django startproject config . # . ----> indica directorio actual
```

# Creamos una aplicación
Una aplicación de DJANGO agrupa responsabilidad. categorias, usuarios, pedidos... (Un módulo)

```sh
py manage.py startapp paginas
```  

# Arrancamos nuestro entorno de desarrollo

```sh
py manage.py runserver
```

## Detener el servidor de desarrollo

Ctrl + C

# Configurando el proyecto para que encuentre paginas
Por default django no sabe que existe ningun módulo. Se lo tengo que explicar.

> config/settings.py

Agrego en el archivo settings.py dentro de la lista INSTALLED_APPS

```py
INSTALLED_APPS = [
    "paginas.apps.PaginasConfig"
]
```

## Para chequear la aplicación antes de correr el servidor

```sh
py manage.py check
``` 