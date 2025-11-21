FROM python:3.9
RUN git clone -b botnyafio https://github.com/amerraa/botnyafio /home/Botnyafio/ \
    && chmod 777 /home/Botnyafio \
    && mkdir /home/Botnyafio/bin/

COPY ./sample_config.env ./config.env* /home/Botnyafio/

WORKDIR /home/Botnyafio/

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install av
RUN pip install av --no-binary av
RUN pip install -r requirements.txt

CMD ["bash","start"]
