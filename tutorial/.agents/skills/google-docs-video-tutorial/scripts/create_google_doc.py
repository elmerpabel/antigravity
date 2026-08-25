#!/usr/bin/env python3
"""
create_google_doc.py
Skill Helper Script: Creates a Google Doc with dual formatting:
1. Standard Technical Tutorial (Markdown style)
2. APA 7th Edition Version (Portada, Estructura Formal, Cita de Referencia APA 7)

Target Folder ID: 1MMBaFNn-A6aQwA6GJndXVjSVV1If14rd
"""

import sys
import os
import argparse
import json
import datetime
import re

DEFAULT_FOLDER_ID = "1MMBaFNn-A6aQwA6GJndXVjSVV1If14rd"
DEFAULT_FOLDER_URL = f"https://drive.google.com/drive/folders/{DEFAULT_FOLDER_ID}"

def generate_apa7_section(title, video_url=None, creator="@autor"):
    """
    Genera la sección estructurada conforme a las normas APA 7ma Edición.
    """
    today = datetime.datetime.now().strftime("%d de %B de %Y")
    
    username = creator
    if video_url and "@" in video_url:
        m = re.search(r'(@[\w\.-]+)', video_url)
        if m:
            username = m.group(1)
            
    apa_content = []
    apa_content.append("\n\n" + "=" * 60)
    apa_content.append("SECCIÓN 2: VERSIÓN EN NORMAS APA (7ª EDICIÓN)")
    apa_content.append("=" * 60 + "\n\n")
    
    apa_content.append("PORTADA (NORMAS APA 7ª EDICIÓN)\n")
    apa_content.append(f"Título: {title.upper()}\n")
    apa_content.append(f"Autor / Creador del Contenido: {username}\n")
    apa_content.append("Institución / Plataforma: Redes Sociales (Contenido Digital y Tecnológico)\n")
    apa_content.append("Asignatura / Área: Ofimática, Automatización y Productividad Digital\n")
    apa_content.append(f"Fecha de Elaboración: {today}\n\n")
    apa_content.append("-" * 50 + "\n\n")
    
    apa_content.append("Resumen (Abstract)\n")
    apa_content.append(
        "El presente documento presenta una guía estructurada según los estándares de la American Psychological Association (APA 7ª edición) "
        "basada en el recurso audiovisual original. Se describen los objetivos, metodologías, herramientas y procedimientos técnicos "
        "requeridos para la correcta ejecución del procedimiento presentado.\n\n"
    )
    
    apa_content.append("Referencias\n")
    if video_url:
        apa_content.append(f"{username}. ({datetime.datetime.now().year}). {title} [Video]. {video_url}\n")
    else:
        apa_content.append(f"{username}. ({datetime.datetime.now().year}). {title} [Video].\n")
        
    return "\n".join(apa_content)

def get_google_creds():
    """
    Intenta obtener credenciales válidas de Google Drive API.
    """
    try:
        from google.oauth2 import service_account
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request

        SCOPES = [
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/documents'
        ]

        config_dir = os.path.expanduser("~/.config/google_drive")
        token_path = os.path.join(config_dir, "token.json")
        sa_path = os.path.join(config_dir, "service_account.json")

        # 1. Service Account
        if os.path.exists(sa_path) or os.path.exists("service_account.json"):
            target_sa = sa_path if os.path.exists(sa_path) else "service_account.json"
            print(f"[+] Usando Service Account de: {target_sa}")
            return service_account.Credentials.from_service_account_file(target_sa, scopes=SCOPES)

        # 2. Token de usuario existente
        target_token = token_path if os.path.exists(token_path) else ("token.json" if os.path.exists("token.json") else None)

        if target_token:
            try:
                creds = Credentials.from_authorized_user_file(target_token, SCOPES)
                if creds and creds.expired and creds.refresh_token:
                    print("[+] Refrescando token OAuth expirado...")
                    creds.refresh(Request())
                if creds and creds.valid:
                    print("[✓] Token OAuth válido cargado.")
                    return creds
            except Exception as token_err:
                print(f"[!] Token expirado o revocado ({token_err}). Eliminando {target_token} para reautenticar...")
                if os.path.exists(target_token):
                    os.remove(target_token)

        # 3. Credentials.json
        client_secret = "credentials.json" if os.path.exists("credentials.json") else (os.path.join(config_dir, "credentials.json") if os.path.exists(os.path.join(config_dir, "credentials.json")) else None)
        if client_secret:
            print(f"[!] Se requiere reautenticación con {client_secret}. Iniciando navegador...")
            flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
            try:
                creds = flow.run_local_server(port=0, open_browser=True, timeout=12)
                if creds:
                    save_dest = token_path if os.path.exists(config_dir) else "token.json"
                    with open(save_dest, 'w') as f:
                        f.write(creds.to_json())
                    print(f"[✓] Nuevo token guardado en {save_dest}")
                    return creds
            except Exception as ex:
                print(f"[!] Flujo interactivo finalizado o esperando confirmación: {ex}")

    except Exception as e:
        print(f"[!] Nota sobre credenciales: {e}")

    return None

def create_gdoc_api(title, full_text, folder_id=DEFAULT_FOLDER_ID):
    """
    Crea un documento Google Doc nativo con Sección Tutorial y Sección APA 7.
    """
    creds = get_google_creds()
    if not creds:
        return {'success': False, 'reason': 'Sin credenciales activas'}

    try:
        from googleapiclient.discovery import build

        drive_service = build('drive', 'v3', credentials=creds)
        docs_service = build('docs', 'v1', credentials=creds)

        file_metadata = {
            'name': title,
            'mimeType': 'application/vnd.google-apps.document',
            'parents': [folder_id]
        }
        doc_file = drive_service.files().create(body=file_metadata, fields='id, webViewLink').execute()
        doc_id = doc_file.get('id')
        web_link = doc_file.get('webViewLink')

        requests = [{'insertText': {'location': {'index': 1}, 'text': full_text}}]
        docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()

        print(f"[✓] Documento nativo de Google Docs (con versión APA 7) creado: {web_link}")
        return {
            'success': True,
            'doc_id': doc_id,
            'doc_url': web_link,
            'folder_url': DEFAULT_FOLDER_URL
        }

    except Exception as e:
        print(f"[!] Error al interactuar con Google Drive API: {e}")

    return {'success': False, 'reason': 'Error de llamada a la API'}

def save_local_copy(title, full_text, folder_id=DEFAULT_FOLDER_ID):
    safe_title = "".join([c if c.isalnum() or c in (' ', '_', '-') else '_' for c in title])
    md_filename = f"{safe_title}.md"
    
    with open(md_filename, 'w', encoding='utf-8') as f:
        f.write(full_text)
        
    print(f"[✓] Copia local guardada: {os.path.abspath(md_filename)}")
    return {
        'success': True,
        'mode': 'local_file',
        'local_file': os.path.abspath(md_filename),
        'folder_id': folder_id,
        'folder_url': DEFAULT_FOLDER_URL
    }

def main():
    parser = argparse.ArgumentParser(description="Crea un documento Google Docs en la carpeta especificada con versión APA 7.")
    parser.add_argument("--title", required=True, help="Título del tutorial")
    parser.add_argument("--content-file", help="Ruta al archivo con el contenido del tutorial")
    parser.add_argument("--content", help="Texto del contenido directamente")
    parser.add_argument("--video-url", help="URL del video original")
    parser.add_argument("--creator", default="@autor", help="Usuario/Nombre del creador del video")
    parser.add_argument("--folder-id", default=DEFAULT_FOLDER_ID, help="ID de la carpeta de Google Drive")
    
    args = parser.parse_args()
    
    content = ""
    if args.content_file and os.path.exists(args.content_file):
        with open(args.content_file, 'r', encoding='utf-8') as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        print("[!] Error: Se requiere --content o --content-file")
        sys.exit(1)

    apa7_text = generate_apa7_section(args.title, args.video_url, args.creator)
    full_text = content + "\n\n" + apa7_text

    res = create_gdoc_api(args.title, full_text, args.folder_id)
    if not res.get('success'):
        res = save_local_copy(args.title, full_text, args.folder_id)
        
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
