FROM nginx:alpine


COPY ./default.conf /etc/nginx/default.conf
COPY ./../database/ /usr/share/nginx/html/

#RUN ln -sf ./../database/ ./html/

EXPOSE 80 443

#CMD ["nginx"]
