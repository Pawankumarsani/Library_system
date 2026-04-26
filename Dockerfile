FROM python:3.11-slim
WORKDIR /app
COPY sys_code.py .
CMD ["python", "sys_code.py"]