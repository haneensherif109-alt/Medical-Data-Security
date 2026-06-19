# كود محاكاة تشفير البيانات الطبية للأجهزة الذكية

def encrypt_medical_data(data, key):
    """دالة بسيطة لتشفير البيانات الطبية (نبضات القلب) باستخدام مفتاح سري"""
    encrypted_data = []
    for char in data:
        encrypted_data.append(chr(ord(char) ^ key))
    return "".join(encrypted_data)

def decrypt_medical_data(encrypted_data, key):
    """دالة فك التشفير في المستشفى لقراءة البيانات الحقيقية"""
    decrypted_data = []
    for char in encrypted_data:
        decrypted_data.append(chr(ord(char) ^ key))
    return "".join(decrypted_data)

# ---- تجربة المحاكاة ----
patient_heart_rate = "85 BPM"  # بيانات المريض الحقيقية
secret_key = 42                # المفتاح السري المشترك بين الجهاز والمستشفى

print(f"1. البيانات الأصلية من جهاز المريض: {patient_heart_rate}")

# التشفير قبل الإرسال عبر الإنترنت
encrypted = encrypt_medical_data(patient_heart_rate, secret_key)
print(f"2. البيانات مشفرة (لو اخترقها هكر هيشوفها كده): {encrypted}")

# فك التشفير لما توصل سيرفر المستشفى
decrypted = decrypt_medical_data(encrypted, secret_key)
print(f"3. البيانات بعد وصولها للمستشفى وفك التشفير: {decrypted}")
