# 🛡️ SecureLogMonitor – Détection d’intrusions SSH & alertes Telegram

Détecteur d’intrusions simple et efficace en Python qui :
	•	Analyse les logs SSH /var/log/auth.log
	•	Détecte les tentatives d’authentification échouées répétées
	•	Banne les IPs suspects automatiquement via iptables
	•	Envoie une alerte via Telegram
	•	Offre un dashboard Flask pour visualiser et nettoyer les alertes

## 🚀 Installation

1. Cloner le dépôt

```bash
git clone https://github.com/Wolfinn974/SecureLogMonitor.git
cd SecureLogMonitor
```

2. Installer les dépendances

```bash
pip install -r requirements.txt
```

Crée un venv si besoin : python -m venv venv && source venv/bin/activate

## ⚙️ Configuration

Crée un fichier .env dans la racine du projet :
```bash
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

## 📂 Structure du projet

```bash
.
├── main.py             # Analyse de logs + alertes
├── notifier.py         # Alertes Telegram
├── dashboard.py        # Interface Flask
├── templates/
│   └── dashboard.html  # HTML du dashboard
├── alerts.json         # Liste des alertes (auto-générée)
├── .env
├── autoban.py
├── log_reader.py
├── alerter.py
├── detection.py
├── rate_limit.py
└── README.md
```

## 🧪 Lancer le projet

```bash
sudo python3 main.py     # Analyse et bannissement
python3 dashboard.py     # Dashboard Flask (http://localhost:5000)
```

## 📜 Licence

MIT – libre à l’utilisation, modification, amélioration.