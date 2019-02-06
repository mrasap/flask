FROM python:alpine
MAINTAINER Michael Kemna <michael.kemna@gmail.com>

# application folder
ENV APP_DIR /src
ENV FLASK_APP /src/app.py

# Copy the current directory contents into the container at /app
COPY . ${APP_DIR}

# Set the current work directory to the app
WORKDIR ${APP_DIR}

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r ./requirements.txt
RUN python ./setup.py

EXPOSE 5000

#ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
ENTRYPOINT ["flask", "run"]