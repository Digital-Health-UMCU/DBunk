FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src src
WORKDIR /src

ENV FLASK_APP main.py
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
