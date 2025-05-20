FROM node:18-alpine

WORKDIR /base/web_page

COPY . .

RUN rm -rf node_modules

RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]