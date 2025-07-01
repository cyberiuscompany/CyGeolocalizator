Windows
---------------------------------
python3 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python server.py

Linux
----------------------------------
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python server.py

Cloud Linux
----------------------------------
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEP
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
sudo chmod +x /usr/local/bin/cloudflared
sudo mv cloudflared-linux-amd64 /usr/local/bin/cloudflared
cloudflared --version
nohup python server.py --host=0.0.0.0 --port=5000 &