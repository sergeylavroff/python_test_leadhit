FROM python:3.9

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install -r requirements.txt

EXPOSE 8088
CMD ["python", "server.py"]