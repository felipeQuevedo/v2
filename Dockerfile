
 FROM python:3.10
 WORKDIR /PythonDocker

 RUN pip install 
 COPY . /PythonDocker
 EXPOSE 6369
 CMD python PythonDocker.py 
