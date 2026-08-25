import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(pdf_path, template_path, output_path):
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template PPTX file not found: {template_path}")

    prs = pptx.Presentation(template_path)

    # Clear default placeholder slides while preserving master layout references
    rId_list = [prs.slides._sldIdLst[i].rId for i in range(len(prs.slides))]
    for rId in rId_list:
        prs.part.drop_rel(rId)
        del prs.slides._sldIdLst[0]

    # Color palette matching industrial & academic standards
    NAVY_BLUE = RGBColor(15, 34, 64)
    TEAL = RGBColor(0, 150, 166)
    DARK_GRAY = RGBColor(50, 50, 50)
    LIGHT_BG = RGBColor(245, 247, 250)

    def add_slide(title_text, subtitle_cat, bullets, graph_suggestion=None):
        slide = prs.slides.add_slide(prs.slide_layouts[1]) # OBJECT layout
        
        # Configure Title
        if slide.shapes.title:
            slide.shapes.title.text = title_text
            p = slide.shapes.title.text_frame.paragraphs[0]
            p.font.size = Pt(26)
            p.font.bold = True
            p.font.color.rgb = NAVY_BLUE
            p.font.name = "Arial"

        # Body Shape
        body_shape = None
        for shape in slide.placeholders:
            if shape.placeholder_format.idx == 1:
                body_shape = shape
                break
        if not body_shape:
            body_shape = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.8))

        tf = body_shape.text_frame
        tf.clear()
        tf.word_wrap = True

        if subtitle_cat:
            p_cat = tf.paragraphs[0]
            p_cat.text = f"[{subtitle_cat.upper()}]"
            p_cat.font.size = Pt(14)
            p_cat.font.bold = True
            p_cat.font.color.rgb = TEAL
            p_cat.font.name = "Arial"
            p_cat.space_after = Pt(12)

        first = True if not subtitle_cat else False
        for b_text in bullets[:6]: # Max 6 bullets
            words = b_text.strip().split()
            if len(words) > 6:
                words = words[:6] # Enforce 6x6 rule
            bullet_str = " ".join(words)

            if first:
                p = tf.paragraphs[0]
                first = False
            else:
                p = tf.add_paragraph()

            p.text = f"•  {bullet_str}"
            p.font.size = Pt(18)
            p.font.color.rgb = DARK_GRAY
            p.font.name = "Arial"
            p.space_after = Pt(10)

        if graph_suggestion:
            g_box = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                Inches(7.2), Inches(2.0), Inches(5.3), Inches(4.5)
            )
            g_box.fill.solid()
            g_box.fill.fore_color.rgb = LIGHT_BG
            g_box.line.color.rgb = TEAL
            g_box.line.width = Pt(1.5)

            gtf = g_box.text_frame
            gtf.word_wrap = True
            gtf.margin_left = Inches(0.2)
            gtf.margin_right = Inches(0.2)
            gtf.margin_top = Inches(0.2)

            gp1 = gtf.paragraphs[0]
            gp1.text = "📊 SUGERENCIA DE GRÁFICO"
            gp1.font.size = Pt(14)
            gp1.font.bold = True
            gp1.font.color.rgb = NAVY_BLUE
            gp1.space_after = Pt(8)

            gp2 = gtf.add_paragraph()
            gp2.text = f"Tipo: {graph_suggestion.get('type', 'N/A')}"
            gp2.font.size = Pt(12)
            gp2.font.bold = True
            gp2.font.color.rgb = TEAL
            gp2.space_after = Pt(6)

            gp3 = gtf.add_paragraph()
            gp3.text = f"Eje X: {graph_suggestion.get('axis_x', 'N/A')}"
            gp3.font.size = Pt(11)
            gp3.font.color.rgb = DARK_GRAY
            gp3.space_after = Pt(4)

            gp4 = gtf.add_paragraph()
            gp4.text = f"Eje Y: {graph_suggestion.get('axis_y', 'N/A')}"
            gp4.font.size = Pt(11)
            gp4.font.color.rgb = DARK_GRAY
            gp4.space_after = Pt(4)

            gp5 = gtf.add_paragraph()
            gp5.text = f"Leyenda: {graph_suggestion.get('legend', 'N/A')}"
            gp5.font.size = Pt(11)
            gp5.font.color.rgb = DARK_GRAY

            body_shape.width = Inches(6.0)

        return slide

    # 1. Carátula
    slide_title = prs.slides.add_slide(prs.slide_layouts[0])
    tb = slide_title.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = "SISTEMA DE GESTIÓN DIGITAL PARA OPTIMIZAR Y ECONOMIZAR EL MANTENIMIENTO DE EQUIPOS"
    p0.font.size = Pt(28)
    p0.font.bold = True
    p0.font.color.rgb = NAVY_BLUE
    p0.space_after = Pt(14)
    p1 = tf.add_paragraph()
    p1.text = "Exposición de Defensa de Trabajo de Aplicación Profesional (TTAP 2026-I)"
    p1.font.size = Pt(18)
    p1.font.color.rgb = TEAL
    p1.space_after = Pt(20)
    p2 = tf.add_paragraph()
    p2.text = "Bachiller: Edwar Andree Velasco Bolivar\nCarrera: Operación de Planta de Procesamiento de Minerales\nAsesor: Rubén Teodoro Coaguila Coaguila\nInstitución: Tecsup - SPCC (Southern Peru Copper Corp.)"
    p2.font.size = Pt(14)
    p2.font.color.rgb = DARK_GRAY

    # 2. Planteamiento del Problema
    add_slide(
        "Planteamiento del Problema",
        "Diagnóstico Operativo",
        [
            "Disponibilidad mecánica inicial: 91.2%",
            "Estándar corporativo mínimo: 96.0%",
            "Trabamiento frecuente de polines retorno",
            "Compactación de finos: humedad 4%-8%",
            "Bitácoras en papel generaban retrasos",
            "Desfase informativo alcanzaba 4 horas"
        ],
        graph_suggestion={
            "type": "Gráfico de barras de disponibilidad",
            "axis_x": "Estado del Circuito (Inicial vs Exigido)",
            "axis_y": "Disponibilidad Mecánica (%)",
            "legend": "91.2% Real vs 96.0% Meta SPCC"
        }
    )

    # 3. Objetivos
    add_slide(
        "Objetivos de la Investigación",
        "Meta General y Específicas",
        [
            "Elevar disponibilidad mecánica a 96.5%",
            "Digitalizar el 100% de inspecciones",
            "Reducir 40% paradas imprevistas fajas",
            "Disminuir 15% reemplazos prematuros polines",
            "Optimizar respuesta de 4h a <45min",
            "Implementar aplicativo móvil en tiempo-real"
        ]
    )

    # 4. Marco Teórico
    add_slide(
        "Marco Teórico y Fundamentos",
        "Bases Académicas y Normativas",
        [
            "Norma CEMA: geometría estaciones polines",
            "Reología finos: humedad crítica 4%-8%",
            "Tribología: desgaste abrasivo de rodamientos",
            "Gestión Activos 4.0: arquitectura Cloud",
            "Mantenimiento predictivo basado en datos",
            "Eliminación de la falla catastrófica"
        ]
    )

    # 5. Metodología
    add_slide(
        "Metodología de Desarrollo",
        "Enfoque y Flujo Tecnológico",
        [
            "Enfoque cuantitativo con diseño propositivo",
            "Universo: FAJA01, FAJA03 y FAJA04",
            "Ingesta mediante terminales móviles industriales",
            "Base de datos Cloud AppSheet",
            "Algoritmo lógico de consulta Query",
            "Validación sobre 20 registros críticos"
        ],
        graph_suggestion={
            "type": "Diagrama de flujo de proceso digital",
            "axis_x": "Fases: Captura -> Cloud -> Alerta -> Acción",
            "axis_y": "Tiempo de latencia (minutos)",
            "legend": "Ruta de Ingesta y Procesamiento Data"
        }
    )

    # 6. Resultados - Disponibilidad
    add_slide(
        "Resultados: Disponibilidad y Tiempos",
        "Indicadores Clave de Desempeño",
        [
            "Disponibilidad mecánica estabilizada en 96.5%",
            "Tiempo operativo neto recuperado: +5.3%",
            "Respuesta ante alertas: <45 minutos",
            "Desfase analógico eliminado por completo",
            "Detección temprana incrementada en +17%",
            "Estándar corporativo SPCC superado con éxito"
        ],
        graph_suggestion={
            "type": "Gráfico de barras agrupadas comparativo",
            "axis_x": "Indicadores Operativos (Disponibilidad / Latencia)",
            "axis_y": "Porcentaje (%) / Minutos",
            "legend": "Antes (91.2% / 240min) vs Después (96.5% / 45min)"
        }
    )

    # 7. Resultados - Cobertura
    add_slide(
        "Resultados: Cobertura de Activos",
        "Consistencia y Equidad de Inspección",
        [
            "Carga de inspección homogénea al 33.33%",
            "FAJA01 Alimentación: 33.33% de atención",
            "FAJA03 Distribución: 33.33% de atención",
            "FAJA04 Descarga: 33.33% de atención",
            "Auditoría validó 20 registros críticos",
            "Eliminación total de tareas extraordinarias"
        ],
        graph_suggestion={
            "type": "Gráfico circular (Donut Chart)",
            "axis_x": "Distribución por Activo Crítico",
            "axis_y": "Porcentaje de Inspecciones (%)",
            "legend": "FAJA01 (33.3%), FAJA03 (33.3%), FAJA04 (33.3%)"
        }
    )

    # 8. Evaluación Económica
    add_slide(
        "Evaluación Económica del Proyecto",
        "Rentabilidad y Retorno Financiero",
        [
            "Inversión inicial CAPEX: S/. 2,500",
            "Costo operativo OPEX: S/. 1,440/año",
            "Ahorro anual neto: S/. 10,500",
            "Reducción compras polines: S/. 2,000",
            "Ahorro horas-hombre emergencia: S/. 3,000",
            "Retorno inversión ROI: 4 meses"
        ],
        graph_suggestion={
            "type": "Tabla de doble entrada y gráfico de barras",
            "axis_x": "Concepto de beneficio económico",
            "axis_y": "Monto anual en soles (S/.)",
            "legend": "Ahorros: Polines (2000), H-H (3000), Demoras (5500)"
        }
    )

    # 9. Análisis y Discusión
    add_slide(
        "Análisis y Discusión de Resultados",
        "Contrastación Teórico-Práctica",
        [
            "Validación empírica del modelo CEMA",
            "Control efectivo de humedad crítica 4%-8%",
            "Transición reactiva a proactiva comprobada",
            "Cero paradas por inundación de finos",
            "Maximización del flujo analítico de muestras",
            "Sostenibilidad operativa en guardias continuas"
        ]
    )

    # 10. Conclusiones
    add_slide(
        "Conclusiones Principales",
        "Síntesis de Hallazgos y Metas",
        [
            "Disponibilidad mecánica elevada al 96.5%",
            "Bitácoras en papel eliminadas al 100%",
            "Tiempo de respuesta reducido a <45min",
            "Mapeo de fajas 100% equitativo",
            "Eficiencia temprana aumentada en +17%",
            "CAPEX S/. 2,500 recuperado en 4 meses"
        ]
    )

    # 11. Recomendaciones
    add_slide(
        "Recomendaciones Finales",
        "Proyección y Trabajo Futuro",
        [
            "Escalar aplicativo a otros circuitos SPCC",
            "Estandarizar capacitaciones a nuevas guardias",
            "Integrar sensores IoT vibración y temperatura",
            "Monitorear desgaste relativo con algoritmos AI",
            "Mantener auditorías periódicas de datos Cloud",
            "Actualizar catálogo digital de repuestos"
        ]
    )

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    pdf_path = sys.argv[1] if len(sys.argv) > 1 else "Velasco Bolivar Edwar Andree.pdf"
    template_path = sys.argv[2] if len(sys.argv) > 2 else "PLANTILLA TITULACIÓN TTAP 2026-1.pptx"
    output_path = sys.argv[3] if len(sys.argv) > 3 else "Exposicion_Tesis_Edwar_Velasco.pptx"
    build_presentation(pdf_path, template_path, output_path)
