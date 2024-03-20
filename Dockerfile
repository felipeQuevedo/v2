
 FROM python:3.10
 WORKDIR /PythonDocker
 COPY . /PythonDocker
 EXPOSE 6369
 CMD python PythonDocker.py
