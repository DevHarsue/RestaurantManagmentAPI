# API para el RestaurantManagement

Esta API cubrira todo lo que es la gestion para acceder, obtener, modificar y eliminar todo lo relacionado a la Base de Datos

## Estructura de la BD

La BD contiene 9 tablas a continuacion las columnas de cada una:

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

*Despues agrego documentacion para cada endpoint*