## Enunciado
Diseña un diagrama de casos de uso para un sistema de gestión de tienda en línea. Los actores pueden ser "Cliente" y "Administrador". Casos de uso incluyen "Ver Catálogo", "Realizar Compra", "Gestionar Inventario", etc.

Documenta el Markdown, y súbelo a tu cuenta de github. El repositorio tendrá el nombre de Gestión de tienda en línea

### Caso de Uso: Ver catálogo
**Actor Principal:** Cliente

**Breve Descripción:** El cliente mira y busca en el catálogo que se le dispone.

**Flujo Básico:**
1. El Cliente inicia sesión en el sistema.
2. El Cliente selecciona la opción que quiera en la interfaz.
3. El sistema muestra un formulario de búsqueda.
4. El Cliente ingresa criterios de búsqueda.
5. El sistema realiza la búsqueda y muestra los resultados al Cliente.

**Flujos Alternativos:**
- 4a. El usuario no encuentra resultados: El sistema muestra un mensaje indicando que no se encontraron coincidencias.

---

### Caso de Uso: Realizar una compra
**Actor Principal:** Cliente

**Breve Descripción:** El usuario visualiza información detallada sobre el objeto que quiera comprar específico.

**Flujo Básico:**
1. El usuario realiza una búsqueda.
2. El usuario selecciona un  objeto de la lista de resultados.
3. El sistema muestra la información detallada del objeto, características, funciones, tipos, etc.

**Flujos Alternativos:**
- 2a. El usuario intenta ver información de un objeto no disponible: El sistema muestra un mensaje indicando que el objeto no está disponible actualmente.

---

### Caso de Uso: Ver su carrito
**Actor Principal:** Cliente

**Breve Descripción:** El cliente puede poner en su carrito todos los objetos que quiera comprar.

**Flujo Básico:**
1. El usuario visualiza la información del objeto disponible.
2. El usuario selecciona la opción "Añadir al carrito".
3. El sistema registra la solicitud y actualiza el estado del carrito.


### Caso de Uso: Ver Historial
**Actor Principal:** Cliente

**Breve Descripción:** El usuario visualiza un historial de compras y devoluciones anteriores.

**Flujo Básico:**
1. El usuario inicia sesión en el sistema.
2. El usuario selecciona la opción "Ver Historial".
3. El sistema muestra una lista de compras y devoluciones anteriores del usuario.

**Flujos Alternativos:**
- 3a. El usuario no tiene historial de compras: El sistema muestra un mensaje indicando que el usuario no tiene registros de compras anteriores.

---

### Caso de Uso: Ver el iventario
**Actor Principal:** Administrador

**Breve Descripción:** El administrador ve el inventario de los objetos de la tienda online.

**Flujo Básico:**
1. El Administrador inicia sesión en el sistema.
2. El Administrador selecciona la opción "Stock".
3. El sistema muestra una lista del inventario.
4. El Administrador selecciona un obejto y ve su inventario.

---


# Caso resuelto
[Caso]()

