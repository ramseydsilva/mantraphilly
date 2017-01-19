# Requirements

* Python (Preferably python3.5)
* Supervisord running as root
* Nginx running as root on port 80

# Setup

```
git clone git@github.com:ramseydsilva/mantraphilly.git mantra
virtualenv -p /usr/bin/python3.5 mantr
mkdir config
echo "ALLOWED_HOSTS=mantra.local" > config/site.conf
pip install -r requirements.txt
sudo src/server/manage.py start
```
The site should be running at http://mantra.local/
