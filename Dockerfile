FROM python:3.9
RUN git clone -b Rosepaw-Userbot https://github.com/rosepaw7/Rosepaw-Userbot /home/Rosepawuserbot/ \
    && chmod 777 /home/Rosepawuserbot \
    && mkdir /home/Rosepawuserbot/bin/

COPY ./sample_config.env ./config.env* /home/Rosepawuserbot/

WORKDIR /home/Rosepawuserbot/

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install av
RUN pip install av --no-binary av
RUN pip install -r requirements.txt

CMD ["bash","start"]
