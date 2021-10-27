FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./data /data

ENTRYPOINT ["jupyter", "notebook", "--ip", "0.0.0.0", "--allow-root"]