FROM python
MAINTAINER Ram
WORKDIR /myapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
