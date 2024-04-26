FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY . /app
CMD ["./start.sh"]