#!/usr/bin/env python3
"""
download_video.py
Skill Helper Script: Downloads/fetches metadata from TikTok videos, YouTube Shorts, Facebook Reels, or locates local workspace video files.
"""

import sys
import os
import json
import glob
import urllib.request
import urllib.parse
import re

def download_tiktok(url, output_path="video_input.mp4"):
    print(f"[+] Intentando descargar video de TikTok: {url}")
    try:
        api_url = "https://www.tikwm.com/api/"
        data = urllib.parse.urlencode({'url': url, 'count': 12, 'cursor': 0, 'web': 1}).encode('utf-8')
        req = urllib.request.Request(api_url, data=data, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            if result.get('code') == 0:
                play_path = result['data']['play']
                if not play_path.startswith('http'):
                    play_url = "https://www.tikwm.com" + play_path
                else:
                    play_url = play_path
                
                video_req = urllib.request.Request(play_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(video_req, timeout=30) as v_resp, open(output_path, 'wb') as f:
                    f.write(v_resp.read())
                
                title = result['data'].get('title', '')
                author = result['data'].get('author', {}).get('unique_id', 'autor')
                print(f"[✓] TikTok descargado exitosamente en: {output_path}")
                return {
                    'success': True,
                    'file_path': os.path.abspath(output_path),
                    'title': title,
                    'creator': f"@{author}",
                    'url': url,
                    'source': 'tiktok'
                }
    except Exception as e:
        print(f"[!] Falló obtención de TikTok: {e}")

    return {'success': False, 'error': 'No se pudo descargar el video de TikTok.'}

def fetch_youtube_info(url):
    print(f"[+] Procesando enlace de YouTube: {url}")
    try:
        video_id = None
        if "shorts/" in url:
            video_id = url.split("shorts/")[1].split("?")[0].split("/")[0]
        elif "watch?v=" in url:
            video_id = url.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1].split("?")[0]
            
        oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
        req = urllib.request.Request(oembed_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            title = data.get('title', '')
            author = data.get('author_name', 'Creador de YouTube')
            author_url = data.get('author_url', '')
            
            creator_tag = author
            if "@" in author_url:
                creator_tag = "@" + author_url.split("@")[1].split("/")[0]
                
            print(f"[✓] Información de YouTube recuperada: {title}")
            return {
                'success': True,
                'title': title,
                'creator': creator_tag,
                'url': url,
                'source': 'youtube'
            }
    except Exception as e:
        print(f"[!] Error al procesar información de YouTube: {e}")
        
    return {'success': False, 'error': 'No se pudo recuperar información de YouTube'}

def fetch_facebook_info(url):
    print(f"[+] Procesando enlace de Facebook Reel/Video: {url}")
    try:
        # Extraer ID del reel o video
        video_id = None
        m_id = re.search(r'(?:reel|watch|v)/(\d+)', url)
        if m_id:
            video_id = m_id.group(1)
            
        target_url = f"https://www.facebook.com/watch/?v={video_id}" if video_id else url
        req = urllib.request.Request(target_url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8'
        })
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode('utf-8')
            m_title = re.search(r'<title>(.*?)</title>', html)
            title = m_title.group(1) if m_title else "Tutorial de Facebook Reel"
            
            # Limpiar nombre del título
            if "|" in title:
                parts = title.split("|")
                clean_title = parts[0].strip()
                creator = "@" + parts[1].strip()
            else:
                clean_title = title.strip()
                creator = "@Word&Excel"
                
            # Extraer descripción del texto
            texts = re.findall(r'\"text\":\"(.*?)\"', html)
            if texts:
                for t in texts:
                    if len(t) > 15 and not t.startswith("http"):
                        clean_title = t.encode().decode('unicode-escape')
                        break

            print(f"[✓] Información de Facebook recuperada: {clean_title}")
            return {
                'success': True,
                'title': clean_title,
                'creator': creator,
                'url': url,
                'source': 'facebook'
            }
    except Exception as e:
        print(f"[!] Error al procesar Facebook: {e}")
        
    return {'success': False, 'error': 'No se pudo recuperar información de Facebook'}

def find_local_video(workspace_dir="."):
    video_extensions = ('*.mp4', '*.mov', '*.mkv', '*.webm', '*.avi')
    found_files = []
    for ext in video_extensions:
        found_files.extend(glob.glob(os.path.join(workspace_dir, ext)))
        found_files.extend(glob.glob(os.path.join(workspace_dir, "**", ext), recursive=True))
    
    if found_files:
        found_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        chosen = found_files[0]
        print(f"[✓] Video local encontrado: {chosen}")
        return {
            'success': True,
            'file_path': os.path.abspath(chosen),
            'title': os.path.basename(chosen),
            'creator': '@local',
            'url': None,
            'source': 'local'
        }
    else:
        print("[!] No se encontraron archivos de video en el directorio de trabajo.")
        return {'success': False, 'error': 'Sin videos locales'}

def main():
    target_url = None
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    
    if target_url:
        if "facebook.com" in target_url or "fb.watch" in target_url:
            res = fetch_facebook_info(target_url)
        elif "youtube.com" in target_url or "youtu.be" in target_url:
            res = fetch_youtube_info(target_url)
        elif "tiktok.com" in target_url or "tikvid" in target_url:
            res = download_tiktok(target_url)
        else:
            res = fetch_facebook_info(target_url)
            
        if not res.get('success'):
            res = find_local_video()
    else:
        res = find_local_video()
        
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
