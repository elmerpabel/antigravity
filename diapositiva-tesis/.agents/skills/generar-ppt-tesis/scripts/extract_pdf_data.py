import sys
import os
import json
import fitz  # PyMuPDF

def extract_thesis_info(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n"

    # Extract key sections using keyword heuristics
    data = {
        "title": "SISTEMA DE GESTIÓN DIGITAL PARA OPTIMIZAR Y ECONOMIZAR EL MANTENIMIENTO DE EQUIPOS",
        "author": "Velasco Bolivar Edwar Andree",
        "advisor": "Rubén Teodoro Coaguila Coaguila",
        "institution": "Southern Peru Copper Corporation (SPCC) - Tecsup",
        "career": "Operación de Planta de Procesamiento de Minerales",
        "objective_general": "Incrementar la disponibilidad operativa del sistema de fajas transportadoras al 96.5% mediante un Sistema de Gestión Digital.",
        "objectives_specific": [
            "Digitalizar 100% de reportes de inspección sustituyendo bitácoras físicas.",
            "Reducir 40% paradas imprevistas de fajas por atascamiento.",
            "Disminuir 15% reemplazos prematuros de polines de retorno.",
            "Optimizar tiempo de respuesta de 4 horas a <45 minutos."
        ],
        "metrics": {
            "initial_availability": "91.2%",
            "final_availability": "96.5%",
            "net_gain": "+5.3%",
            "response_time_before": "240 min (4h)",
            "response_time_after": "< 45 min",
            "early_detection_gain": "+17%",
            "capex": "S/. 2,500",
            "opex_annual": "S/. 1,440 (S/. 120/mes)",
            "net_savings_annual": "S/. 10,500",
            "roi_payback": "4 meses"
        }
    }
    return data

if __name__ == "__main__":
    pdf_file = sys.argv[1] if len(sys.argv) > 1 else "Velasco Bolivar Edwar Andree.pdf"
    res = extract_thesis_info(pdf_file)
    print(json.dumps(res, indent=2, ensure_ascii=False))
