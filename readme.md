# Server Setup

> Alle Befehle werden mit dem `root`-User ausgeführt.
> Getestet unter `Raspbian buster`.

## Dependencies

- Packete installieren
```
apt install git gunicorn nginx python3-pip
```

- Repository an den richtigen Ort clonen
```
mkdir -p /opt/scoreboard
git clone https://github.com/... /opt/scoreborad
```

- Requirements für Python installieren
```
python3 -m pip install -r /opt/scoreboard/requirements.txt
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
cp -r /opt/scoreboard/server-config/* /
```

- Berechtigungen anpassen
```
chown -R www-data:www-data /opt/scoreboard
```

- NGINX-Seite aktivieren
```
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/scoreboard /etc/nginx/sites-enabled/scoreboard
```

- NGINX und Gunicorn autostart einschalten
```
systemctl daemon-reload
systemctl enable scoreboard
systemctl enable nginx
```

- NGINX und Gunicorn starten
```
systemctl restart scoreboard
systemctl restart nginx
```

# Screen Setup

TODO

