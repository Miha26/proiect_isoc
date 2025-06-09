FROM nginx:alpine

# Șterge pagina implicită NGINX
RUN rm -rf /usr/share/nginx/html/*

# Copiază frontend-ul tău peste
COPY . /usr/share/nginx/html
