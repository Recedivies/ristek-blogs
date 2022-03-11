# build-stage
FROM node:16-alpine as build

WORKDIR /app/frontend
COPY ./frontend/package.json ./ && \
  ./frontend/package-lock.json ./
  
RUN npm ci --silent
COPY ./frontend/ ./
RUN npm run build

# The second stage
# Copy React static files and start nginx
FROM nginx:stable-alpine
COPY --from=build /app/frontend/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]