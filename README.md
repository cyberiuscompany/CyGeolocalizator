# CyUSBGuard

![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Sistema](https://img.shields.io/badge/windows-x64-green)
![Sistema](https://img.shields.io/badge/linux-x64-green)
![Licencia](https://img.shields.io/badge/licencia-Privada-red)
![Uso](https://img.shields.io/badge/uso-solo%20legal-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)

##########################

---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p

---

## Descripción

**CyUSBGuard** #################################. 

Diseñada con un enfoque de ciberseguridad para entornos educativos, empresariales o domésticos.

---

## 📄 Documentación adicional

- [🔐 Seguridad](.github/SECURITY.md)
- [📜 Licencia](LICENSE)
- [🤝 Código de Conducta](.github/CODE_OF_CONDUCT.md)
- [📬 Cómo contribuir](.github/CONTRIBUTING.md)
- [📢 Soporte](.github/SUPPORT.md)
- [⚠️ Aviso legal](DISCLAIMER.md)

---

## ⚙️ 1.1 Instalación básica con clonado 🪟 Windows

```bash
git clone ############
python3 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python server.py
```

## ⚙️ 1.2 Instalación básica con clonado 🐧 Linux / macOS

```bash
git clone #############
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python server.py
```

## ⚙️ 2 Instalación como si fuese paquete profesional

```bash
git clone ######
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEP
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
sudo chmod +x /usr/local/bin/cloudflared
sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared
cloudflared --version
nohup python server.py --host=0.0.0.0 --port=5000 &
```


