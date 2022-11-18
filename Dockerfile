FROM python:3.10

WORKDIR /cfg-cyk

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]