FROM python:3.9
LABEL maintainer="Girish"

COPY . /app
WORKDIR /app
RUN pwd && ls
RUN pip install -r exercises/python-helloworld/requirements.txt

# command to run on container start
CMD [ "python", "exercises/python-helloworld/app.py" ]
