FROM nginx:alpine

# Șterge pagina implicită NGINX
RUN chmod -R 755 /usr/share/nginx/html

# Copiază frontend-ul tău peste
COPY . /usr/share/nginx/html
