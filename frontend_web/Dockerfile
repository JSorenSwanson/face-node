FROM node:lts-alpine

WORKDIR /frontend-app
COPY package*.json ./
COPY *.config.js ./
RUN npm install

EXPOSE 8080

COPY . .
CMD ["npm", "run", "serve"]