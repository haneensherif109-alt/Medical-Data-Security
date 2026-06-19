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

1. Clone this repository:
```bash
   git clone [https://github.com/haneensherif109-alt/Medical-Data-Security.git](https://github.com/haneensherif109-alt/Medical-Data-Security.git)
   python main.py
1. البيانات الأصلية من جهاز المريض: 85 BPM
2. البيانات مشفرة (لو اخترقها هكر هيشوفها كده): [Ciphertext Output]
3. البيانات بعد وصولها للمستشفى وفك التشفير: 85 BPM
Future Improvements
Upgrade the system to use more robust algorithms like AES-128 optimized for IoT.
Implement network socket simulations to mimic real-time data transmission.
