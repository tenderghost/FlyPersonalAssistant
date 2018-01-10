# Copyright 2017 tenderghost@gmail.com
# 
#

FROM python:3.6-alpine3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# SHOULD be in requirements.txt
RUN pip3 install Django

# In dev environment, I should use volumn mapping instead of COPY code into image.
# ADD ./mysite /code/
