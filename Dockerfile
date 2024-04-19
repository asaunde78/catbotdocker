FROM python:3.10.12

RUN apt-get -y update
RUN pip install poetry 
COPY . . 
RUN cd scraperrework/scraper
RUN ./setup.sh
RUN cd ../..

RUN poetry install
ENTRYPOINT ["poetry"]

CMD ["run","python","-m","catbot"] 