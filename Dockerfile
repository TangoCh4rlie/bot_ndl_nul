
FROM python:3.9.6

# copies des requirements.txt et installation des dépendances
COPY requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

# expose le port 8080
EXPOSE 8080
# Run the application.
CMD ["python3", "main.py"]
