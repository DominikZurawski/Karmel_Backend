FROM nginx:alpine


COPY ./default.conf /etc/nginx/default.conf
#RUN chown basic-user:basic-user /usr/share/nginx/html/*

#RUN chown -R nginx:nginx ./ && chmod -R 755 ./ && \
#        chown -R nginx:nginx /var/cache/nginx && \
#        chown -R nginx:nginx /var/log/nginx && \
#        chown -R nginx:nginx /etc/nginx/conf.d
#RUN touch /var/run/nginx.pid && \
#        chown -R nginx:nginx /var/run/nginx.pid
#USER nginx

EXPOSE 80 443

#CMD ["nginx"]
