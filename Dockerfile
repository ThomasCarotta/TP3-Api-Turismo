FROM python:3.11-alpine
WORKDIR /app

# Configura el PYTHONPATH para incluir /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia todo el contenido (incluyendo la carpeta api)
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]