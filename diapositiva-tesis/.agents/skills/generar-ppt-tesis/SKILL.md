---
name: generar-ppt-tesis
description: >-
  Crea y genera de forma automatizada la presentación PowerPoint (.pptx) para la exposición
  de defensa de tesis final. Extrae la información académica y los datos cuantitativos reales
  del informe de tesis en PDF (objetivos, metodología, resultados, finanzas, conclusiones) y
  utiliza la plantilla institucional .pptx para redactar diapositivas bajo la Regla 6x6 y diseñar
  sugerencias de gráficos científicos. Activar ante solicitudes como "genera el powerpoint de la tesis de edwar velasco",
  "crea la presentación pptx de la tesis", o "redacta las diapositivas de sustentación".
---

# Skill: Generador de PowerPoint para Exposición de Tesis Final

Este skill automatiza el análisis del informe final de tesis (en formato PDF) y la creación de una presentación oral en PowerPoint (`.pptx`) utilizando la plantilla institucional predeterminada (ej. `PLANTILLA TITULACIÓN TTAP 2026-1.pptx`).

## ⚠️ Reglas de Oro (Obligatorias)

1. **Fidelidad Absoluta de Datos**: NUNCA inventar números, porcentajes, fechas, fórmulas o nombres de autores. Si un dato no existe en el PDF o en las instrucciones del usuario, escribir `[DATO PENDIENTE]` e indicar qué dato falta.
2. **Regla 6x6 Estricta**:
   - Máximo **6 viñetas (bullet points)** por diapositiva.
   - Máximo **6 palabras** por viñeta.
   - Si un concepto es complejo, dividirlo en dos diapositivas consecutivas.
3. **Diseño de Sugerencia de Gráficos**: Para diapositivas numéricas o metodológicas, incluir una caja de sugerencia de gráfico especificando:
   - **Tipo exacto de visualización** (ej. Gráfico de barras agrupadas, gráfico circular/donut, tabla de doble entrada, diagrama de flujo).
   - **Eje X**: Variable independiente o categorías.
   - **Eje Y**: Variable dependiente o indicador numérico/porcentual.
   - **Leyenda**: Series o comparaciones mostradas.

---

## 🛠️ Procedimiento de Ejecución

Para procesar la solicitud del usuario (ejemplo: *"genera el powerpoint de la tesis de edwar velasco"*), sigue estos pasos:

### Paso 1: Extracción e Inspección de Archivos
1. Identificar en la carpeta de trabajo el PDF del informe de tesis (ej. `Velasco Bolivar Edwar Andree.pdf`) y la plantilla `.pptx` (ej. `PLANTILLA TITULACIÓN TTAP 2026-1.pptx`).
2. Ejecutar el script auxiliar de extracción `scripts/extract_pdf_data.py` o PyMuPDF para obtener:
   - **Título exacto, Bachiller, Asesor, Carrera e Institución/Empresa**.
   - **Objetivo General y Objetivos Específicos**.
   - **Metodología resumida** (enfoque, circuito/muestra, herramientas, base de datos).
   - **Resultados cuantitativos y tablas de datos duros** (disponibilidad %, latencia en minutos, ROI, CAPEX, OPEX, ahorros netos).
   - **Citas clave del marco teórico y normativo** (ej. CEMA, Reología de finos, Tribología, Activos 4.0).
   - **Conclusiones y Recomendaciones**.

### Paso 2: Redacción del Contenido de las Diapositivas
Estructurar la presentación en una secuencia lógica de 10 a 12 diapositivas:

1. **Carátula / Título**: Título del trabajo, programa de titulación, bachiller, asesor y fecha.
2. **Planteamiento del Problema**: Diagnóstico inicial (disponibilidad 91.2% vs meta 96.0%, causa raíz por humedad 4%-8%, desfase de 4h en papel).
3. **Objetivos de la Investigación**: Objetivo general (96.5% disponibilidad) y los 4 objetivos específicos.
4. **Marco Teórico y Sustento Técnico**: Norma CEMA, reología de finos, tribología de rodamientos y gestión 4.0.
5. **Metodología y Arquitectura Digital**: Enfoque cuantitativo, circuito de fajas (FAJA01, FAJA03, FAJA04), AppSheet/Cloud y algoritmo Query.
6. **Resultados: Disponibilidad y Tiempos**: 96.5% disponibilidad, +5.3% tiempo recuperado, latencia <45 min, +17% detección temprana. Include gráfico de barras comparativo.
7. **Resultados: Cobertura de Activos**: Equidad 33.33% por faja, auditoría de 20 registros. Include gráfico circular/donut.
8. **Evaluación Económica**: CAPEX S/. 2,500, OPEX S/. 1,440/año, Ahorro S/. 10,500/año, ROI en 4 meses. Include tabla/barras de ahorro.
9. **Análisis y Discusión**: Contrastación teórica CEMA y paso de gestión reactiva a predictiva.
10. **Conclusiones**: Respuesta directa a los objetivos iniciales.
11. **Recomendaciones**: Escalabilidad a otros circuitos, sensores IoT y mantenimiento continuo.

### Paso 3: Generación del Archivo `.pptx`
Ejecutar el script automatizado `scripts/build_presentation.py` que:
1. Carga la plantilla original `.pptx` respetando los fondos, logos corporativos y layouts predefinidos.
2. Formatea los títulos, categorías y texto aplicando la Regla 6x6 y tipografías legibles.
3. Genera las cajas visuales con las sugerencias de gráficos científicos.
4. Guarda el archivo resultante en la raíz del espacio de trabajo (ej. `Exposicion_Tesis_Edwar_Velasco.pptx`).

---

## 📂 Recursos y Scripts Auxiliares

- [build_presentation.py](./scripts/build_presentation.py): Script de Python para construir el `.pptx` usando `python-pptx`.
- [extract_pdf_data.py](./scripts/extract_pdf_data.py): Script para extraer y estructurar el texto del PDF de tesis.
- [prompt_template.md](./templates/prompt_template.md): Guía de redacción y visualización de gráficos.
