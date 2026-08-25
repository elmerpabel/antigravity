---
name: google-docs-video-tutorial
description: Genera automáticamente un tutorial paso a paso estructurado en Google Docs a partir de un video (enlaces de TikTok, YouTube Shorts/Videos, Facebook Reels descargados vía API o archivos de video local), incluyendo una Pestaña/Sección adicional en Formato APA 7 (7ª Edición) con portada, resumen y citas bibliográficas, y lo guarda en la carpeta asignada de Google Drive (https://drive.google.com/drive/folders/1MMBaFNn-A6aQwA6GJndXVjSVV1If14rd).
---

# Google Docs Video Tutorial Generator (TikTok, YouTube Shorts & Facebook Reels a Google Docs APA 7)

Esta habilidad (Skill) procesa un video (a partir de un enlace de **TikTok**, **YouTube Shorts / Videos**, **Facebook Reels**, o de un archivo de video local) para extraer la información, estructurar una guía tutorial paso a paso y generar un documento de Google Docs guardado en la carpeta de Google Drive configurada.

---

## 📌 Estructura Multisección del Documento

Cada documento generado incluye dos secciones principales estructuradas:

### 1. Sección 1: Formato Tutorial Estándar (Guía Técnica / Markdown)
- **Título del Tutorial**: Claro, descriptivo y enfocado al tema.
- **Enlace de Internet del Video**: **Ubicado justo debajo del título principal** (`[Ver Video Original en Internet](<URL>)`).
- **Introducción / Requisitos**: Herramientas necesarias y contexto.
- **Paso a Paso Detallado**: Pasos numerados secuenciales con resaltado en **negrita** para comandos, opciones de menú, fórmulas y términos clave.

### 2. Sección 2: Versión en Normas APA 7ª Edición (APA 7 Version)
- **Portada de Presentación (APA 7)**:
  - Título formal del trabajo.
  - Nombre del autor / creador del contenido audiovisual (`@usuario` / Página).
  - Institución y área (Plataforma Digital / Ofimática y Automatización / TI).
  - Fecha formal de elaboración.
- **Cuerpo Formal (APA 7)**:
  - Resumen ejecutivo estructurado en prosa formal académica.
  - Encabezados Nivel 1 y Nivel 2 acordes al manual APA 7.
- **Referencias Bibliográficas (APA 7)**:
  - Cita bibliográfica formal de la fuente audiovisual (TikTok / YouTube / Facebook) según el estándar APA 7:
    `Autor, A. [@usuario]. (Año). Título del video [Video]. Plataforma. URL`

---

## 📁 Carpeta de Destino en Google Drive

- **URL de la carpeta**: `https://drive.google.com/drive/folders/1MMBaFNn-A6aQwA6GJndXVjSVV1If14rd`
- **ID de la carpeta**: `1MMBaFNn-A6aQwA6GJndXVjSVV1If14rd`

---

## 🚀 Flujo de Trabajo (Workflow)

Cuando el usuario solicite la creación de un tutorial desde un video (ejemplo: `"genera tutorial de <URL>"`):

### Paso 1: Descarga y Obtención del Video / Metadatos
```bash
python3 .agents/skills/google-docs-video-tutorial/scripts/download_video.py "<URL>"
```

### Paso 2: Procesamiento del Contenido y Transcripción
Extraer los conceptos clave, pasos de combinación de correspondencia/diseño, menús de Word/Excel y datos del creador del video.

### Paso 3: Generación del Documento con Versión APA 7
Ejecutar el script de creación:
```bash
python3 .agents/skills/google-docs-video-tutorial/scripts/create_google_doc.py --title "<Título>" --content-file "<Ruta_del_archivo_md>" --video-url "<URL>" --creator "<@usuario>" --folder-id "1MMBaFNn-A6aQwA6GJndXVjSVV1If14rd"
```

---

## 💡 Ejemplos de Uso

```text
genera tutorial de https://www.tiktok.com/@ticomscrl/video/7663598504337542420
genera tutorial de https://youtube.com/shorts/fJgBO7NMbYg
genera tutorial de https://www.facebook.com/reel/1927522464610880
```
