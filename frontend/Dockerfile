# Use the official Node.js image as the base image
FROM node:14

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy the Vue.js project files to the container
COPY . .

# Build the Vue.js application
RUN npm run dev

# Expose the Vue.js development server port
EXPOSE 8080

# Start the Vue.js development server
CMD ["npm", "run", "serve"]