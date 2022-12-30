FROM node:16

ENV NPM_CONFIG_LOGLEVEL warn

RUN yarn global add serve
CMD serve -s build
EXPOSE 3000

WORKDIR /app

COPY package.json ./
RUN yarn

COPY . .

CMD ["yarn", "start"]