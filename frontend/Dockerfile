FROM node:22-alpine
WORKDIR /app
COPY package.json tsconfig.json next-env.d.ts next.config.ts ./
COPY app ./app
COPY components ./components
RUN npm install
CMD ["npm", "run", "dev", "--", "--hostname", "0.0.0.0"]
