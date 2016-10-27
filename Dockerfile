FROM python:3.5.2
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "hello:app"]
EXPOSE 8000