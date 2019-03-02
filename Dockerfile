FROM python:alpine as builder

# uWSGI needs a c-compiler, which results in a container of ~340 mb
RUN apk add --no-cache linux-headers build-base

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt


# This is the actual container without compilers (~100 mb)
FROM python:alpine


# Copy the compiled modules from the builder to the actual container
COPY --from=builder /install /usr/local

# Copy my flask code
COPY ./app /app

# Create a non-root user
RUN adduser -D dummyuser
# It needs ownership of the workdir to update the sqlite database
RUN chown dummyuser /app
USER dummyuser

WORKDIR /app

# Setup the database
RUN touch database.db
RUN python ./setup.py

EXPOSE 8080

CMD ["uwsgi", "--ini", "conf.ini"]