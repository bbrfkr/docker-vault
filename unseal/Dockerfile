FROM python:3.8

RUN pip install hvac pyyaml
COPY vault ./vault

CMD [ "python3", "-m", "vault" ]
