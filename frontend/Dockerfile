# syntax=docker/dockerfile:1

#============================#
# ==== build environment ====#
#============================#

# use the official node 18 base image
# this is a temporary image to build the react app
FROM node:18-alpine as build

# create working directory
# it will be used as the default location by the subsequent command
WORKDIR /app


# set the PATH environment variable
ENV PATH /app/node_modules/.bin:$PATH

# Add the source code into the image
COPY . ./

# install dependencies, ci makes sure the exact versions in the lockfiles are installed
RUN npm ci
# build the app
RUN npm run build

#=============================#
# == production environment ==#
#=============================#

# use nginx image, final image
FROM nginx:stable-alpine

# copy the needed folder from the temporary image
COPY --from=build /app/build /usr/share/nginx/html

# copy custom nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# port to listen to at runtime
EXPOSE 80

# command to run when the container starts
CMD ["nginx", "-g", "daemon off;"]
