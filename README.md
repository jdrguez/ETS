<!-- Encabezados -->

# title en h1
## title en h2
### title en h3
#### title en h4
##### title en h5
###### title en h6
---
<!-- listas desordenadas -->
## Listas desordenadas:
* Manzanas
    * Golden
    * Reinetas
* Peras
* Albaricoques
---
<!-- Listas ordenadas -->
## Listas ordenadas:
1. Primero
    1. Primero1
    1. Primero2
2. Segundo
3. Tercero
---
<!-- tablas -->
## Tablas:
|Nombre|Apellidos|
|------|---------|
|Juan  |Perez    |

---
<!-- tipos de letra -->
## Tipos de letra:
tipos de *letra* 

tipos de **letra**

tipos de ~~letra tachada~~

---
<!-- generar una línea de codigo -->
## Generar una línea de código:
'
console.log("hola mundo")
'
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
  <html>
<body>
<h2>impresora</h2>
<table>
<tr><th>Marca</th><th>Modelo</th></tr>
<xsl:for-each select=" //impresora ">
<tr>
<td><xsl:value-of select="Marca"/></td>
<td><xsl:value-of select="Modelo"/></td>
</tr>
</xsl:for-each>
</table>
</body>
  </html>
  </xsl:template>
</xsl:stylesheet>

```

---
<!-- Acceso a paginas web -->
## Acceso a paginas web:
[periodico el pais](https://www.elpais.es)