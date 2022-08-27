FROM nginx:alpine


COPY ./default.conf /etc/nginx/default.conf

RUN ln -sf ./../database/ ./html/

EXPOSE 80 443

#CMD ["nginx"]
