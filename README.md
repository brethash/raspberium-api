## Raspberium API Service

### Built with Django Rest Framework!

- Supports an IR Remote based light controller!
- Supports TP-Link HS100/HS110 Smart Plugs!
- Utilizes a BME280 to measure temperature, humidity, and pressure! Wow!

### Installation Instructions
1. [Install python 3.6 from source](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f).
2. [Make python3.6 the default](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux).
3. Clone project to `/var/www/raspberium-api`.
4. Change directory to `/var/www/raspberium-api`.
5. `python -m virtualenv venv`.
6. `source venv/bin/activate`.
7. `pip install -r requirements.txt`.
8. `mkdir static sfiles && python manage.py collectstatic`
9. `pip install gunicorn`.
10. Run migrations and load fixtures: `python manage.py migrate && python manage.py loaddata raspberium.json`
11. Open the crontab `sudo crontab -e` and then add the raspberium cronjob `* * * * * source /var/www/raspberium-api/venv/bin/activate && python /var/www/raspberium-api/manage.py runcrons > /var/www/raspberium-api/logs/cronjob.log`
12. Install and Setup Nginx `apt-get install nginx`.
13. `cp /var/www/raspberium-api/webserver/api.raspberium.com.conf /etc/nginx/sites-available`.
14. `ln -s /etc/nginx/sites-available/api.raspberium.com.conf /etc/nginx/sites-enabled/`.
15. Copy and setup `/var/www/raspberium-api/webserver/raspberium-api-gunicorn.service`.
16. [Enable I2C Interface](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/).
17. Allow read access on I2C inteface `sudo chmod 666 /dev/i2c-1`.
