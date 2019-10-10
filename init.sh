sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo gunicorn -b 0.0.0.0:8080 hello:app
#sudo gunicorn -b 0.0.0.0:8000 ask.ask.wsgi:application
cd /home/box/web/ask
gunicorn --bind=0.0.0.0:8000 ask.wsgi:application

