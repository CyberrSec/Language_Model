# Use the official Node.js image from the Docker Hub
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY lmapp/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY lmapp /app/lmapp

# Build the React application
RUN npm run build --prefix lmapp

# Install a lightweight server to serve the static files
RUN npm install -g serve

# Expose the port the app will run on
EXPOSE 3000

# Command to serve the React application
CMD ["serve", "-s", "lmapp/build", "-l", "3000"]
