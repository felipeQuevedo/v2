
 FROM python:3.10
 WORKDIR /app
 COPY . /app
 EXPOSE 6369
 CMD python app.py 
