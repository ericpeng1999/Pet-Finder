FROM node:20.10.0

EXPOSE 3000
WORKDIR /home/app
COPY . /home/app
RUN npm ci

CMD ["npm", "start"]