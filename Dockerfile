FROM python:3.11-slim

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python", "main.py"]