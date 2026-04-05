# Dockerfile


# Imaginea de baza - python:3.11-slim (~50MB)
FROM python:3.11-slim

# Directorul de lucru in container
WORKDIR .

# Copiem requirements PRIMUL (cache Docker)
# Daca requirments.txt nu s-a schimbat,
# Docker nu reinstaleaza pip la fiecare build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem codul aplicatiei
COPY ./src/simple_flask.py .

# EXPOSE = documentatie, NU deschide portul!
EXPOSE 8001

# Comanda la pornirea containerului
CMD ["python3", "simple_flask.py"]
