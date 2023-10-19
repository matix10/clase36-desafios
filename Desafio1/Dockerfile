FROM python:3.9

COPY . .


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]