# Tutorial Paso a Paso: Cómo Descargar e Instalar el Plugin YQArch para AutoCAD Gratis

[Ver Video Original en Facebook Reels](https://www.facebook.com/reel/27316855607992597/)

---

## 📖 1. Introducción y Objetivo

**YQArch** es uno de los complementos (*plugins*) más populares y potentes para **AutoCAD**, diseñado especialmente para arquitectos, ingenieros civiles y proyectistas. Permite automatizar el dibujo de planos arquitectónicos (muros, puertas, ventanas, ejes, escaleras y cotas) reduciendo el tiempo de dibujo en más de un 70% gracias a sus comandos abreviados de dos letras.

El objetivo de este tutorial es guiarte paso a paso en la descarga, extracción, instalación y configuración de idioma (inglés/español) del plugin YQArch en AutoCAD de forma completamente gratuita.

---

## 🛠️ 2. Requisitos Previos

1. **AutoCAD Instalado**: Cualquier versión de AutoCAD (2010 a 2026) instalada en sistema operativo Windows.
2. **Descompresor de Archivos**: WinRAR, 7-Zip o el descompresor nativo de Windows.
3. **Paquete YQArch**: Archivo comprimido `.zip` del plugin YQArch.

---

## 📋 3. Guía Paso a Paso para la Instalación

### Paso 1: Descargar y Extraer el Plugin en C:\
1. Descarga el archivo del plugin YQArch en formato `.zip`.
2. Haz clic derecho sobre el archivo descargado y selecciona **Extraer aquí** o **Extraer en YQArch**.
3. **Recomendación de Ruta**: Mueve la carpeta extraída `YQArch` a la raíz de tu disco local `C:\` (quedando la ruta: `C:\YQArch`).  
   *Nota*: Evita colocar la carpeta en rutas con nombres muy largos o con caracteres especiales/acentos para prevenir errores de carga en AutoLISP.

---

### Paso 2: Cargar el Plugin en la Interfaz de AutoCAD
Existen dos métodos sencillos para instalar y vincular YQArch con tu AutoCAD:

#### Método A: Arrastrar y Soltar (Recomendado)
1. Abre tu programa AutoCAD.
2. Abre la carpeta del plugin (`C:\YQArch\sys\`).
3. Busca el archivo ejecutable de instalación llamado `setup.lsp` (o `sysload.lsp`).
4. Haz clic sobre el archivo `setup.lsp` y **arrástralo suéltalo** directamente sobre la pantalla o área de dibujo de AutoCAD.
5. Verás que en la barra de herramientas superior aparecerá de inmediato el nuevo menú desplegable de **YQArch**.

#### Método B: Comando APPLOAD
1. Dentro de AutoCAD, escribe en la barra de comandos: `APPLOAD` y presiona `Enter`.
2. En la ventana emergente, navega hasta la carpeta `C:\YQArch\sys\`.
3. Selecciona el archivo `sysload.lsp` y haz clic en **Load** (Cargar).
4. Para que se cargue automáticamente cada vez que inicies AutoCAD, haz clic en **Contents...** dentro de *Startup Suite* y añade el archivo `sysload.lsp`.

---

### Paso 3: Configurar el Idioma del Plugin (Cambiar de Chino a Inglés)
Por defecto, algunas versiones de YQArch se instalan en idioma chino. Para cambiar el idioma al inglés:

1. En la línea de comandos de AutoCAD, escribe: `YY` y presiona `Enter` (o abre el menú `YQArch > System Setup > Set Language`).
2. Aparecerá un cuadro de texto o ventana de configuración.
3. Busca la variable de idioma:
   * `0` = Idioma Chino.
   * `1` = Idioma Inglés.
4. Cambia el valor a `1` y presiona `Enter` para guardar.
5. Cierra y vuelve a abrir AutoCAD. Todo el menú y los comandos del plugin se mostrarán en inglés/español.

---

### Paso 4: Comandos Rápidos Principales de YQArch
Una vez instalado, puedes probar los siguientes comandos en la línea de comandos de AutoCAD:

| Comando | Función Principal |
| :--- | :--- |
| **`WW`** | Dibuja muros dobles automáticamente especificando el grosor (ej. 0.15m). |
| **`WD`** | Inserta puertas automáticas en cualquier muro cortando el espacio de forma limpia. |
| **`WJ`** | Inserta ventanas arquitectónicas detalladas en muros existentes. |
| **`ZH`** | Genera una red de ejes arquitectónicos (*grids*) numerados automáticamente. |
| **`TW`** | Dibuja escaleras en planta de forma automatizada. |
| **`YQ`** | Abre el menú de configuración principal del plugin. |

---

## 💡 4. Consejos Prácticos y Solución de Problemas

* **Si el menú desaparece**: Si al reiniciar AutoCAD no ves la barra de YQArch, vuelve a ejecutar el comando `APPLOAD` e incluye el archivo `sysload.lsp` en la sección *Startup Suite*.
* **Compatibilidad**: Funciona tanto en versiones en inglés como en español de AutoCAD.
* **Créditos**: Tutorial basado en el video instructivo de **@Edgar Cayatopa** en Facebook Reels.

---

*Documento preparado y almacenado automáticamente en Google Drive:*  
`https://drive.google.com/drive/folders/1MMBaFNn-A6aQwA6GJndXVjSVV1If14rd`
