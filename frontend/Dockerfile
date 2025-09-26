FROM node:20 AS build

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

ENV PUBLIC_URL=https://dolar.juanbogado.dev

RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 8003
CMD ["nginx", "-g", "daemon off;"]
