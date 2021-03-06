# TODO

- Fix issue with CAPTCHA v3 (as of Novemeber 3rd).
- Fix issue with user registration saying username or email already exists (when it doesn't?).

# Developing Locally

Restore development environment for Python 2.7 on Ubuntu:

```bash
pip2 install -r requirements.txt
```

This will install all the same packages we used to develop the website and
backend.

# How We Run

Gunicorn runs on the server at `localhost:8080` with <a href='https://www.nginx.com/'>Nginx</a> on top as a reverse-proxy, handling everything from port 80 (HTTP traffic).

The config for the Nginx server can be found in `/etc/nginx/nginx.conf` and the service config for Gunicorn can be found under `/etc/systemd/system/gunicorn.service`.

Our SSL certificates are obtained using <a href='https://letsencrypt.org/'>Let's Encrypt</a> are are auto-renewed every 90 days using a CRON job. This checks twice daily, and it's suggested to pick a random minute within the scheduled hour to renew on:

```bash
0 0,12 * * * python -c 'import random; import time; time.sleep(random.random() * 3600)' && ./path/to/certbot-auto renew 
```

# Getting Started

## Step 1: SSH into the thing!

```bash
sudo ssh admin@airpacfire.eecs.wsu.edu # Password: airpact@fire#16
```

## Step 2: Run server

```bash
cd /home/admin/Website
```

*No Logs*
```bash
sudo gunicorn --bind 0.0.0.0:80 AIRPACT_Fire.wsgi:application # In the same directory as `manage.py`
```

*Log to master_log file*
```bash
sudo gunicorn --bind 0.0.0.0:80 --log-level debug --log-file master_log AIRPACT_Fire.wsgi:application
```

# Updating Server Code

After you've committed your changes locally and pushed them to this repository
under the `master` branch, do the following.

## Step 1: Stop server

Kill the server with

```bash
ps -A # Find the process with the Gunicorn pid
sudo kill [pid] # Kill that process
```

## Step 3: Pull down changes

Now move to the website directory with

```bash
cd /home/admin/Website
```

and then pull your changes down from GitHub via

```bash
git pull
```

## Step 3: Restart server

At last you can start the server again

```bash
sudo gunicorn --bind 0.0.0.0:80 AIRPACT_Fire.wsgi:application
```

# Restarting Server

Run through the Updating Server Code section, but skip step 3.

# Log Script

Usage:

```bash
sudo ./log_script [log_file] [url_to_post]
```

or with nohup (so script doesn't die when server is off):

```bash
sudo nohup ./log_script [file] [url] &
```

Example:

```bash
sudo nohup ./log_script master_log https://hooks.slack.com/services/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 &
```

# Git
```bash
git clone https://github.com/AIRPACT-Fire/Website.git
```
