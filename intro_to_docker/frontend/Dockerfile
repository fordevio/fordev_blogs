FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

RUN echo "hello world"

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
