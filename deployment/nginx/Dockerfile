FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

# Start Nginx in the foreground so it can remain active for Docker
CMD ["nginx", "-g", "daemon off;"]