## Enunciado
Desarrolla un diagrama de casos de uso para una aplicación de red social. Los actores pueden ser "Usuario" y "Administrador". Casos de uso incluyen "Publicar Mensaje", "Conectar con Amigos", "Eliminar Publicación", etc.

Documéntalo en Markdown, y súbelo a tu cuenta de githb, con el nombre Red 

### Caso de Uso: Publicar un mensaje
**Actor Principal:** Usuario

**Breve Descripción:** El cliente publica un mesaje en la feed.

**Flujo Básico:**
1. El Cliente inicia sesión en el sistema.
2. El Cliente selecciona la opción que quiera en la interfaz.
3. El sistema muestra un formulario de búsqueda.
4. El Cliente ingresa los datos.

**Flujos Alternativos:**
- 4a. El usuario no encuentra resultados: El sistema muestra un mensaje indicando que no se encontraron coincidencias.

---

### Caso de Uso: Elimnar publicacion
**Actor Principal:** Usuario

**Breve Descripción:** El usuario visualiza información detallada sobre las publicaciones.

**Flujo Básico:**
1. El usuario realiza una publicación.
2. El usuario selecciona una publicacio en la lista de resultados.
3. El sistema elimina la publicación seleccionada.

---

### Caso de Uso: Conectar con amigos
**Actor Principal:** Usuario

**Breve Descripción:** El  usuario agregar y conecta con amigos registrados.

**Flujo Básico:**
1. El usuario visualiza de los amigos.
2. El usuario selecciona la opción de conectar.
3. El sistema registra la solicitud y actualiza el estado del usuario.


### Caso de Uso: Dar de alta
**Actor Principal:** Administrador

**Breve Descripción:** El administrador puede dar de alta y baja a los usuarios.

**Flujo Básico:**
1. El administrador inicia sesión en el sistema.
2. El administrador selecciona la opción de dar de alta o de baja.
3. El sistema muestra una lista usuarios.

---

# Caso resuelto
[Caso](red_social.drawio.png)

