# API para el RestaurantManagement

Esta API es parte del ecosistema RestaurantManagement, se podria decir que esta es la parte principal ya que en esta API se cubrira todo lo que es la gestion para acceder, obtener, modificar y eliminar todo lo relacionado a la Base de Datos

*NOTA: La Base de Datos esta desplegada en PostgreSQL*

## Despliegue

Para desplegar el API, primero crea un archivo .env en la raiz del repositorio con la siguiente estructura:

**USER='FAKEUSER'**
**PASSWORD='PASSWORDFAKE'**
**HOST='FAKEHOST'**
**DATABASE='FAKEDATABASE'**
**SECRET_KEY = 'FAKESECRET_KEY'**
**ALGORITHM = 'FAKEALGORITHM'**

Coloca los campos para conectar a la base de datos
*NOTA: ALGORITHM es el algoritmo que se va a usar para codificar los tokens, normalmente se usa HS256*

*NOTA: En caso de no tener la base de datos, crea una base de datos con cualquier nombre, luego ejecuta el archivo sql para crear las tablas de la base de datos (tables.sql) y luego el archivo insert.sql*

Crea un entorno virtual:

*Para WINDOWS*
**python -m venv venv**

Activa el venv y luego instala las dependecias con:

**pip install -r requirements.txt**

Una vez hecho eso depliega con uvicorn:

**uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload**

## Estructura de la BD

La BD contiene 11 tablas a continuacion las columnas de cada una:

### Clientes
- ID
- NACIONALIDAD
- CEDULA
- NOMBRE
- APELLIDO
- TELEFONO
- DIRECCION

### Mesas
- ID
- MESA_DESCRIPCION

### Tipos_Platos
- ID
- NOMBRE
- ICON

### Platos
- ID
- NOMBRE
- DESCRIPCION
- PRECION
- TIPO_PLATO_ID

### Ordenes
- ID
- FECHA
- CLIENTE_ID

### Mesas_Ocupadas
- ORDEN_ID
- MESA_ID

### Divisas
- ID
- NOMBRE
- RELACION

### Detalles_Ordenes_Platos
- ID
- ORDEN_ID
- PLATO_ID
- CANTIDAD

### Detalles_Ordenes_Divisas
- ID
- ORDEN_ID
- DIVISA_ID
- CANTIDAD

### Usuarios
- ID
- NOMBRE
- CONTRASEÑA
- SALT
- ROL_ID

### Roles
- ID
- NOMBRE

*Despues agrego documentacion para cada endpoint*