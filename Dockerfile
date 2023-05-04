FROM python

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r /app/requirements.txt

COPY . .

#RUN gunicorn /app/rtf_tube/gunicorn_conf.py

#CMD python -u /app/rtf_tube/manage.py runserver 0.0.0.0:8000