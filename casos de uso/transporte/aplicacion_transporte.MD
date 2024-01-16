<div align='justify'>

# Casos de Uso

Es un artefacto que define una secuencia de acciones que da lugar a un resultado de valor observable. Los casos de uso proporcionan una estructura para expresar requisitos funcionales en el contexto de procesos empresariales y de sistema. Los casos de uso pueden representarse como un elemento gráfico en un diagrama y como una especificación de caso de uso en un documento textual.

Las especificaciones de caso de uso comparten el mismo comportamiento de texto enriquecido que está presente en todos los artefactos basados en el formato de artefacto de texto. Con frecuencia, las especificaciones incluyen contenido que se basa en una plantilla o una guía de proceso similar a este esquema:

   1. Nombre de caso de uso
   2. Breve descripción
   3. Flujo de eventos
   4. Flujo básico
   5. Flujos alternativos
   6. Requisitos especiales
   7. Condiciones previas
   8. Condiciones posteriores
   9. Puntos de ampliación

## Actor

Los actores comparten el mismo comportamiento de texto enriquecido inherente a todos los artefactos que se crean mediante el formato de artefacto de texto. Puede insertar actores en diagramas de caso de uso existentes o puede crearlos sobre la marcha al crear un diagrama de caso de uso.

## Especificacion de casos de uso

Proporcionan detalles textuales de un caso de uso. Se proporciona una descripción de ejemplo de un especificación de caso de uso. Puede reutilizar y modificar la descripción según se requiera en una especificación de caso de uso.

## Caso a resolver :

### Administrador:
Este define el medio de transporte 

   Permite al administrador agregar nuevos medios de transporte al sistema, especificando detalles como tipo de transporte, capacidad, etc.

##### Flujo Básico:

   El sistema presenta un formulario para ingresar los detalles del nuevo medio de transporte.
   El administrador completa el formulario y confirma la adición.
   El sistema registra el nuevo medio de transporte.

#### Definir precio de transporte:

Permite al administrador establecer tarifas y precios asociados a los diferentes medios de transporte disponibles.

##### Flujo Básico:
Se muestra una interfaz para ingresar tarifas por tipo de transporte y otros detalles.Este establece los precios y confirma la configuración, para su posterior actualización.
   
#### Alta y baja de usuarios:

El administrador gestionar la alta y baja de usuarios en el sistema.

##### Flujo Básico:
Para el alta de usuarios, el sistema presenta un formulario para registrar nuevos usuarios. Por otro lado, para la baja de usuarios, el administrador elige el usuario a dar de baja y confirma la acción.
El sistema registra los cambios en la base de datos de usuarios.

### Usuario
#### Login:
Permite a los usuarios autenticarse en el sistema para acceder a funciones personalizadas.
##### Flujo Básico:
El usuario proporciona sus credenciales (nombre de usuario y contraseña).
El sistema verifica las credenciales y permite el acceso si son válidas y si son válidas, el usuario accede al sistema.


#### Geoposicionamiento:

Proporciona la capacidad de determinar la ubicación actual del usuario.

##### Flujo Básico:
El sistema utiliza servicios de geoposicionamiento para obtener la ubicación del usuario.La ubicación se muestra al usuario o se utiliza en otras funciones del sistema.

#### Definir destinos

Permite al usuario agregar o modificar destinos preferidos en su perfil.
##### Flujo Básico:
El usuario elige la opción de "Definir destinos".
El sistema presenta una interfaz para agregar o modificarlos.
El usuario completa la información y confirma los cambios.
El sistema actualiza los destinos en el perfil del usuario.

#### Modificar ruta:
El usuario puede ajustar la ruta planificada según sus preferencias.
##### Flujo Básico:
El usuario selecciona la opción de "Modificar ruta".
El sistema muestra la ruta actual y permite realizar ajustes.
El usuario confirma los cambios, y el sistema actualiza la ruta planificada.


### UseCase1:
Sugerir destinos interesantes. El sistema puede sugiere destinos atractivos basados en las preferencias y ubicación del usuario.
##### Flujo Básico:
El sistema analiza las preferencias del usuario y su ubicación actual.
Selecciona destinos interesantes cercanos y los presenta al usuario.
#### Mostrar puntos de interés en ruta:
Muestra puntos de interés en la ruta planificada del usuario.
##### Flujo Básico:
El sistema obtiene la ruta actual del usuario.
Identifica puntos de interés a lo largo de la ruta.
Muestra estos puntos de interés al usuario durante la planificación de la ruta.


</div>