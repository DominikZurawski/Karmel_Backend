FROM nginx:alpine


COPY ./default.conf /etc/nginx/default.conf
RUN chown nginx:nginx /usr/share/nginx/html/*

EXPOSE 80 443

#CMD ["nginx"]
