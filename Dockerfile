FROM python:3.10.12

RUN apt-get -y update
RUN pip install poetry 
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
        ffmpeg

COPY . . 

#RUN chmod +x ./setup.sh
#RUN ./setup.sh


RUN poetry install
ENTRYPOINT ["poetry"]

CMD ["run","python","-m","catbot"] 
