# Server Setup

> Alle Befehle werden mit dem `root`-User ausgeführt.


## Dependencies

- Packete installieren
```
apt install gunicorn nginx python3-pip
```

- Repository an den richtigen Ort clonen
```
mkdir -p /opt/scoreboard
git clone https://github.com/... /opt/scoreborad
```

- Requirements für Python installieren
```
python3 -m pip install /opt/scoreboard/requirements.txt
```


## App Setup

- Beispielkonfiguration kopieren und anpassen
```
cp /opt/scoreborad/config.example.py /opt/scoreborad/config.py
vi /opt/scoreborad/config.py
```

- Domainname und IP-Adresse vom Ranglisten-Server eintragen
```
echo '10.11.12.13 hauptsystem.localdomain' >> /etc/hosts
```


## NGINX und Gunicorn Setup

- Config an den richtigen Ort kopieren
```
cp -r /opt/scoreborad/server-config/* /
```

- Berechtigungen anpassen
```
chown -R www-data:www-data /opt/scoreborad
```

- NGINX-Seite aktivieren
```
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/scoreboard /etc/nginx/sites-enabled/scoreboard
```



