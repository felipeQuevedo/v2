
 FROM python:3.10
 WORKDIR /PythonDocker
 COPY requirements.txt .
 RUN pip install -r requirements.txt
 COPY . /PythonDocker
 EXPOSE 6369
 CMD python PythonDocker.py 
