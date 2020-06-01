FROM python:3.7-slim

RUN pip install pipenv



COPY ./src/Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src /app/src


ENTRYPOINT ["python"]

CMD ["/app/src/MainScores.py"]