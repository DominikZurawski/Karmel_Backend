FROM nginx:alpine


COPY ./default.conf /etc/nginx/default.conf
RUN chown basic-user:basic-user /usr/share/nginx/html/*

EXPOSE 80 443

#CMD ["nginx"]
