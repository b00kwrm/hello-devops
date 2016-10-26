FROM python:3.5.2
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["hello.py"]
EXPOSE 5000