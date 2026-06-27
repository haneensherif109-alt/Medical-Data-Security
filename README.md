# Securing Smart Healthcare Devices Using Lightweight Cyber Cryptography

## 📌 Project Overview
In the modern medical field, **Internet of Medical Things (IoMT)** devices, such as pacemakers and smart health monitors, are crucial for patient monitoring. However, these devices face severe cybersecurity threats, as hackers can intercept and alter medical data during transmission. 

This project addresses this critical challenge by developing a **lightweight cryptographic system** using Python to encrypt patient data (e.g., heart rates) before transmission to hospital servers.

---

## 🎯 Key Features & Concepts
* **Lightweight Cybersecurity:** Designed specifically for resource-constrained IoMT devices to conserve battery and processing power.
* **Symmetric Encryption:** Implements a simulation of the **XOR Cipher** algorithm to demonstrate secure data obfuscation.
* **Data Integrity:** Ensures that sensitive health records remain unreadable to unauthorized interceptors (Man-in-the-Middle attacks).

---

## 💻 Code Simulation & How it Works
The project includes a Python simulation that mimics the data flow from a patient's wearable device to the hospital's secure server.

### System Workflow:
1. **Data Generation:** The device records sensitive data (e.g., `"85 BPM"`).
2. **Encryption:** Data is encrypted using a shared secret key before internet transmission.
3. **Decryption:** The hospital server receives the ciphered text and decrypts it back to readable medical data.

---
## 🚀 How to Run the Project

This repository demonstrates the evolution of the project from a basic implementation to an advanced, network-simulated system.

### Option 1: Basic Offline Simulation (Legacy Version)
This was the initial version of the project, where encryption and decryption happen sequentially within a single script.
* Run the basic single file:
```bash
python main.py
```
###Option 2: Advanced Network Simulation (Latest Upgraded Version)
To make the project realistic and closer to production, it has been upgraded to a Client-Server Architecture using Python's socket library. This simulates actual Internet of Medical Things (IoMT) data flow, where data is encrypted on the patient's device (client.py), transmitted over the network, and safely decrypted at the hospital server (server.py)
```bash
python server.py
```
```bash
python client.py
```
## Project Evolution & Cybersecurity Value
By upgrading from a single-file script (main.py) to a networked system (client.py & server.py), the project now addresses real-world Man-in-the-Middle (MitM) attack vectors. If an attacker intercepts the data traffic between the client and the server, they will only see the obfuscated cipher text, verifying the data integrity and privacy of sensitive patient health records.
