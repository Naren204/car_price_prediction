FROM python:3.9

# COPY requirements.txt /opt/app/requirements.txt
# WORKDIR /opt/app
# RUN pip install -r requirements.txt
# COPY . /opt/app
COPY . ./app
WORKDIR /app

RUN pip install -r requirements.txt


CMD ["uwsgi","--ini","app.ini"]

EXPOSE 5000