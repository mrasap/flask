FROM python:alpine
MAINTAINER Michael Kemna <michael.kemna@gmail.com>

ENV FLASK_APP /app.py

RUN apk add --no-cache linux-headers build-base

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r ./requirements.txt
RUN python ./setup.py

EXPOSE 8080

CMD ["uwsgi", "--ini", "conf.ini"]
#ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=5000"]
#ENTRYPOINT ["flask", "run"]