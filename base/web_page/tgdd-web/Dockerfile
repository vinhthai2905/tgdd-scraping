FROM node:20

WORKDIR /base/web_page

COPY . .

RUN rm -rf node_modules package-lock.json

RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]