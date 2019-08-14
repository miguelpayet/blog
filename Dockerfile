FROM python:3.7.4-slim-buster

RUN apt update -y
RUN apt upgrade -y
RUN apt install locales pkg-config libcairo2 libcairo2-dev gcc \
	 python-cairo mariadb-client libmariadb3 libmariadb-dev libmariadb-dev-compat python-mysqldb \
	 apache2 apache2-dev --no-install-recommends -y
RUN rm -r /var/lib/apt/lists/*
RUN umask 002

RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
RUN echo 'es_PE.UTF-8 UTF-8' >> /etc/locale.gen
RUN locale-gen
RUN locale
RUN LANG=en_US.UTF-8
RUN export LANG
RUN adduser --disabled-password --gecos 'Whiskey' --uid 1001 --gid 0 --home /home/whiskey whiskey

COPY requirements.txt /

#RUN pip install --upgrade pip
RUN pip install --requirement requirements.txt --upgrade

EXPOSE 8000

COPY . /app/
RUN rm /app/debug.log
RUN touch /app/debug.log
RUN chown whiskey:www-data /app/debug.log
WORKDIR /app/

RUN python manage.py collectstatic --noinput
CMD ["mod_wsgi-express", "start-server", "/app/blog/wsgi.py", "--user", "whiskey", "--group", "www-data", "--url-alias", "/static/", "/app/static/"]
#CMD ["mod_wsgi-express", "start-server", "--entry-point", "/app/hello.py", "--log-level", "DEBUG", "--user", "whiskey", "--group", "www-data", "--url-alias", "/static/", "--document-root", "/app/"]

