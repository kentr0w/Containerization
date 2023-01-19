# syntax=docker/dockerfile:1
# docker inherit from other image, use the official python image that have all the tools we need 
FROM python:3.8-alpine

# create a working directory: docker will use this path as default location for the subsequent command
WORKDIR /app

# copy requirements.txt that contains all the pip packages to install to our working directory inside the image
COPY requirements.txt requirements.txt
# install required pip packages into the image
RUN pip install -r requirements.txt

# add the source code of our app into the image
COPY . .

# indicates the container to listen on the specified port at run time
EXPOSE 5000

# command to run when the container start (by default flask run will search for a wsgi.py file)
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
