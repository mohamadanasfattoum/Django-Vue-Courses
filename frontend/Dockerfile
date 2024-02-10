# Use an official Node.js runtime as the base image
FROM node:18

# Set the working directory inside the container
WORKDIR /frontend

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

COPY . .

# Expose the container port (adjust if necessary)
EXPOSE 8080

# Define the command to run your application
CMD [ "npm", "run", "dev" ]