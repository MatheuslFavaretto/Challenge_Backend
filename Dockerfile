FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY start.sh /

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x start.sh

# iniciando o servidor
CMD ["./start.sh"]