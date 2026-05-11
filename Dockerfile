FROM python:3.9-slim
WORKDIR /app
COPY service/ ./service/
RUN pip install flask flask-talisman flask-cors
CMD ["python", "service/account.py"]
EXPOSE 8080
