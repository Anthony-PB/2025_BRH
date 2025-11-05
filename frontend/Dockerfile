# Stage 1: Build the React application
FROM node:20-alpine AS build

# Add a build argument for the API URL and set it as an environment variable
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL

WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Serve the built application with Nginx
FROM nginx:stable-alpine

# Copy the built files from the build stage
COPY --from=build /app/out /usr/share/nginx/html

# Copy the custom Nginx configuration
COPY data/nginx/default.conf /etc/nginx/conf.d/default.conf

# Expose port 80 and start Nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]