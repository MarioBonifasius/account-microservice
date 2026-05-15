# Menggunakan base image Python 3.9 yang ringan
FROM python:3.9-slim

# Menentukan working directory di dalam container
WORKDIR /app

# Menyalin file requirements.txt (jika ada) ke working directory
# COPY requirements.txt .

# Menyalin seluruh folder service ke dalam container
COPY service/ ./service/

# Menginstall dependencies yang diperlukan
RUN pip install --no-cache-dir flask flask-talisman flask-cors

# Menentukan perintah yang akan dijalankan saat container start
CMD ["python", "service/account.py"]

# Mengekspos port 8080 agar bisa diakses dari luar container
EXPOSE 8080
