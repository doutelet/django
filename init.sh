sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled
sudo gunicorn -b 0.0.0.0:8080 hello:app
sudo /etc/init.d/nginx restart

