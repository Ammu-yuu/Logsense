# 🔍 LogSense — AI-Assisted Security Log Triage

![Python](https://img.shields.io/badge/Python-3.10-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Status](https://img.shields.io/badge/Status-In%20Progress-pink)

LogSense is a machine learning project that analyses network session data and classifies it as **benign or a potential attack**. It is designed to support security analysts by automating the first layer of log triage — reducing manual effort and helping prioritise investigations faster.

---

## 📌 What it does

In a real Security Operations Centre (SOC), analysts are flooded with thousands of log entries every day. LogSense tackles this by training a classification model on labelled network session data — learning patterns that distinguish normal traffic from attacks. Once trained, the model can predict whether a new session is suspicious, acting as a first filter before human review.

---

## 🗂️ Dataset

- **Source:** Cybersecurity Intrusion Detection Dataset
- **Rows:** 9,537 network sessions
- **Target column:** `attack_detected` (0 = Benign, 1 = Attack)

| Column | Description |
|---|---|
| `session_id` | Unique session identifier |
| `network_packet_size` | Size of network packets |
| `protocol_type` | TCP / UDP / ICMP |
| `login_attempts` | Number of login attempts in session |
| `session_duration` | Duration of the session |
| `encryption_used` | Encryption type (AES / DES / None) |
| `ip_reputation_score` | Threat score of the IP address |
| `failed_logins` | Number of failed login attempts |
| `browser_type` | Browser used in session |
| `unusual_time_access` | Whether access occurred at unusual hours |
| `attack_detected` | Target — 0 benign, 1 attack |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10 |
| ML | scikit-learn |
| Data Processing | pandas, numpy |
| Notebook | Jupyter (GitHub Codespaces) |
| Model Storage | joblib |
| Deployment | Hugging Face Spaces (coming soon) |

---

## 📁 Project Structure
logsense/
├── data/
│   └── cybersecurity_intrusion_data.csv   # Labelled network session dataset
├── notebooks/
│   └── logsense_exploration.ipynb         # Data exploration & analysis
├── requirements.txt
└── README.md

---

## 🚀 How to Run

1. Open this repo in GitHub Codespaces
2. Navigate to `notebooks/logsense_exploration.ipynb`
3. Run all cells from top to bottom

No local installation needed — everything runs in the cloud.

---

## 📊 Results

> Coming soon — model training in progress.

---

## 🌐 Live Demo

> Coming soon — will be deployed on Hugging Face Spaces.

---

## 👩‍💻 Author

Made by [Ammu-yuu](https://github.com/Ammu-yuu)
