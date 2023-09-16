FROM node:16-alpine

ARG PROJ_DIR=/front_green

RUN mkdir -p ${PROJ_DIR}
COPY ./frontend ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN npm install -g npm

COPY ./frontend/package.json ${PROJ_DIR}
COPY ./frontend/package-lock.json ${PROJ_DIR}

RUN npm install

CMD ["npm", "run", "serve"]