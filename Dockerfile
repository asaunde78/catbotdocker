FROM python:3.10.12

RUN apt-get -y update
RUN pip install poetry 
COPY . . 

RUN chmod +x ./setup.sh
RUN ./setup.sh


RUN poetry install
ENTRYPOINT ["poetry"]

CMD ["run","python","-m","catbot"] 