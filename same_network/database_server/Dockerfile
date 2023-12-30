FROM python:3.12.1-bookworm

EXPOSE 8000
WORKDIR /home/app
COPY . /home/app/

RUN pip install --no-cache-dir -r requirements.txt

ENV POSTGRES_DB="petfinder" \
    POSTGRES_USER="user" \
    POSTGRES_PASSWORD="1234" \
    CLIENT_ID="Umcqw6TWPCwhteNyMqJNLJEeasrecM3RcTHZRJQWQjwBfzgzl9" \
    CLIENT_SECRET="lw1oCR5FgETXi6y2YEzmj2WZ1TVE6sGkIdy6E0o8"

CMD ["python", "-m", "uvicorn", "--host", "backend", "--port", "8000", "server:app", "--reload"]