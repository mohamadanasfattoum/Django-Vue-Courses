# Use a specific Node.js version for consistency and security
FROM node:16-alpine

# Set the working directory inside the container
WORKDIR /frontend/app

# Copy package.json and package-lock.json first for efficient caching
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy all project files
COPY . .

# Build the Vue app for production (assuming it's a Vue app)
RUN npm run build

# Expose the correct port used by the Vue app
EXPOSE 8080

# Start the Vue app in production mode
CMD ["npm", "run", "dev","0.0.0.0:8080"]
