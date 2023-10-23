FROM python:3
RUN apt-get update
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python","app.py"]