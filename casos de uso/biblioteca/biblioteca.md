
### Caso de Uso: Buscar Libro
**Actor Principal:** Usuario

**Breve Descripción:** El usuario busca libros en el catálogo de la biblioteca para encontrar información sobre libros disponibles.

**Flujo Básico:**
1. El usuario inicia sesión en el sistema.
2. El usuario selecciona la opción "Buscar Libro" en la interfaz.
3. El sistema muestra un formulario de búsqueda.
4. El usuario ingresa criterios de búsqueda como título, autor o palabra clave.
5. El sistema realiza la búsqueda y muestra los resultados al usuario.

**Flujos Alternativos:**
- 4a. El usuario no encuentra resultados: El sistema muestra un mensaje indicando que no se encontraron coincidencias.

---

### Caso de Uso: Ver Información Libro
**Actor Principal:** Usuario

**Breve Descripción:** El usuario visualiza información detallada sobre un libro específico.

**Flujo Básico:**
1. El usuario realiza una búsqueda de libros.
2. El usuario selecciona un libro de la lista de resultados.
3. El sistema muestra la información detallada del libro, incluyendo título, autor, resumen, y disponibilidad.

**Flujos Alternativos:**
- 2a. El usuario intenta ver información de un libro no disponible: El sistema muestra un mensaje indicando que el libro no está disponible actualmente.

---

### Caso de Uso: Solicitar Préstamo
**Actor Principal:** Usuario

**Breve Descripción:** El usuario solicita el préstamo de un libro disponible en la biblioteca.

**Flujo Básico:**
1. El usuario visualiza la información de un libro disponible.
2. El usuario selecciona la opción "Solicitar Préstamo".
3. El sistema registra la solicitud de préstamo y actualiza el estado del libro.

**Flujos Alternativos:**
- 2a. El libro no está disponible para préstamo: El sistema muestra un mensaje indicando que el libro no se puede prestar en ese momento.

---

### Caso de Uso: Ver Historial
**Actor Principal:** Usuario

**Breve Descripción:** El usuario visualiza un historial de préstamos y devoluciones anteriores.

**Flujo Básico:**
1. El usuario inicia sesión en el sistema.
2. El usuario selecciona la opción "Ver Historial".
3. El sistema muestra una lista de préstamos y devoluciones anteriores del usuario.

**Flujos Alternativos:**
- 3a. El usuario no tiene historial de préstamos: El sistema muestra un mensaje indicando que el usuario no tiene registros de préstamos anteriores.

---

### Caso de Uso: Prestar Libro
**Actor Principal:** Bibliotecario

**Breve Descripción:** El bibliotecario presta un libro a un usuario.

**Flujo Básico:**
1. El bibliotecario inicia sesión en el sistema.
2. El bibliotecario selecciona la opción "Prestar Libro".
3. El sistema muestra una lista de libros pendientes de préstamo.
4. El bibliotecario selecciona un libro y lo presta al usuario.
5. El sistema actualiza el estado del libro y registra el préstamo.

**Flujos Alternativos:**
- 4a. El libro seleccionado no está disponible: El sistema muestra un mensaje indicando que el libro no se puede prestar en ese momento.

---

### Caso de Uso: Devolver Libro
**Actor Principal:** Bibliotecario

**Breve Descripción:** El bibliotecario registra la devolución de un libro por parte de un usuario.

**Flujo Básico:**
1. El bibliotecario inicia sesión en el sistema.
2. El bibliotecario selecciona la opción "Devolver Libro".
3. El sistema muestra una lista de libros actualmente en préstamo.
4. El bibliotecario selecciona el libro devuelto por el usuario.
5. El sistema actualiza el estado del libro y registra la devolución.

**Flujos Alternativos:**
- 4a. El libro seleccionado no está en la lista de préstamos: El sistema muestra un mensaje indicando que el libro no está actualmente en préstamo.

---

### Caso de Uso: Gestionar Inventario
**Actor Principal:** Bibliotecario

**Breve Descripción:** El bibliotecario realiza acciones para gestionar el inventario de la biblioteca, como agregar nuevos libros o eliminar libros obsoletos.

**Flujo Básico:**
1. El bibliotecario inicia sesión en el sistema.
2. El bibliotecario selecciona la opción "Gestionar Inventario".
3. El sistema muestra opciones como agregar nuevo libro, eliminar libro, actualizar información, etc.
4. El bibliotecario realiza las acciones deseadas en el inventario.

**Flujos Alternativos:**
- 4a. El bibliotecario intenta eliminar un libro que está actualmente en préstamo: El sistema muestra un mensaje indicando que el libro no se puede eliminar porque está en préstamo.

