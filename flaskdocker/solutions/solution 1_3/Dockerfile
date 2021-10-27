FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP main.py
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
