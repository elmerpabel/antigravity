# Tutorial Paso a Paso: Aprende a Hacer SSH Port Forwarding en Menos de 1 Minuto

[Ver Video Original en YouTube Shorts](https://youtube.com/shorts/fJgBO7NMbYg)

---

## 📖 1. Introducción y Objetivo

El **SSH Port Forwarding** (o Tunelización SSH) es una técnica esencial de administración de redes y ciberseguridad que permite tunelizar y redirigir el tráfico de un puerto local hacia un servidor remoto (o viceversa) a través de un canal seguro y cifrado.

El objetivo de este tutorial es enseñar la sintaxis, comandos prácticos y los tipos principales de redirección de puertos mediante SSH (*Local*, *Remote* y *Dynamic*).

---

## 🛠️ 2. Requisitos Previos

1. **Cliente SSH**: Terminal en Linux, macOS o Windows (OpenSSH o PowerShell).
2. **Acceso a un Servidor Remoto**: Credenciales de usuario e IP/dominio del servidor SSH remoto.
3. **Servicio objetivo**: Un puerto local o remoto que desees exponer (ej: servidor web en puerto `80`/`8080`, base de datos MySQL en puerto `3306`, etc.).

---

## 📋 3. Guía Paso a Paso para Realizar SSH Port Forwarding

### Paso 1: Local Port Forwarding (Redirección Local `-L`)
Permite conectar un puerto de tu computadora local (`localhost:puerto_local`) hacia un servicio que corre en el servidor remoto.

**Sintaxis General**:
```bash
ssh -L [puerto_local]:[host_destino]:[puerto_destino] usuario@servidor_remoto
```

**Ejemplo Práctico**:  
Acceder a una interfaz web interna que se ejecuta en el puerto `80` del servidor remoto `192.168.1.100`, exponiéndola localmente en el puerto `8080`:
```bash
ssh -L 8080:localhost:80 usuario@192.168.1.100
```
* **Verificación**: Abre tu navegador web e ingresa a `http://localhost:8080`.

---

### Paso 2: Remote Port Forwarding (Redirección Remota `-R`)
Permite exponer un servicio que corre en tu máquina local para que sea accesible desde el servidor remoto.

**Sintaxis General**:
```bash
ssh -R [puerto_remoto]:[host_local]:[puerto_local] usuario@servidor_remoto
```

**Ejemplo Práctico**:  
Exponer tu servidor de desarrollo local (puerto `3000`) en el puerto `9000` del servidor remoto:
```bash
ssh -R 9000:localhost:3000 usuario@192.168.1.100
```

---

### Paso 3: Dynamic Port Forwarding (Proxy SOCKS `-D`)
Convierte tu conexión SSH en un **servidor Proxy SOCKS** local. Todo el tráfico que configures a través de ese puerto viajará cifrado a través del servidor SSH.

**Sintaxis General**:
```bash
ssh -D [puerto_proxy_local] usuario@servidor_remoto
```

**Ejemplo Práctico**:  
Crear un proxy SOCKS5 en el puerto `1080`:
```bash
ssh -D 1080 usuario@192.168.1.100
```

---

### Paso 4: Opciones Recomendadas para Túneles en Segundo Plano
Para mantener el túnel abierto sin abrir un shell interactivo de comandos, utiliza los parámetros `-N` y `-f`:

```bash
ssh -N -f -L 8080:localhost:80 usuario@192.168.1.100
```
* **`-N`**: Indica a SSH que no ejecute ningún comando remoto (solo crea el túnel).
* **`-f`**: Envía el proceso SSH a segundo plano en tu terminal.

---

## 💡 4. Resumen y Puntos Clave

* **Seguridad Cifrada**: Protege servicios que no tienen cifrado nativo (HTTP, bases de datos sin SSL) envolviéndolos en SSH.
* **Acceso a Redes Privadas**: Permite saltar cortafuegos (firewalls) e ingresar a recursos de red interna autorizados.
* **Créditos**: Tutorial basado en el video explicativo de **@ElPinguinoDeMario** en YouTube Shorts.

---

*Documento preparado y sincronizado automáticamente en Google Drive:*  
`https://drive.google.com/drive/folders/1MMBaFNn-A6aQwA6GJndXVjSVV1If14rd`
