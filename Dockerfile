
 FROM python:3.10
 WORKDIR /PythonDocker
 COPY . /PythonDocker
 EXPOSE 6368
 CMD python PythonDocker.py 
