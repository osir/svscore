# Server Setup

> Alle Befehle werden mit dem `root`-User ausgeführt.  
> Getestet unter `Raspbian buster` (lite image).  

## Generelles

- Shell als `root`-User starten
```
sudo -i
```

- Pakete updaten und rebooten
```
apt update -y && apt upgrade -y && reboot
```

## Dependencies

- Packete installieren
```
apt install git nginx python3-pip
```

- Repository an den richtigen Ort clonen
```
mkdir -p /opt/scoreboard
git clone https://github.com/... /opt/scoreboard
```

- Requirements für Python installieren
```
python3 -m pip install -r /opt/scoreboard/requirements.txt
```


## App Setup

- Beispielkonfiguration kopieren und anpassen
```
cp /opt/scorebroad/config.example.py /opt/scorebroad/config.py
vi /opt/scorebroad/config.py
```

- Domainname und IP-Adresse vom Ranglisten-Server eintragen
```
echo '10.11.12.13 hauptsystem.localdomain' >> /etc/hosts
```


## NGINX und Gunicorn Setup

- Gunicorn installieren
```
python3 -m pip install gunicorn
```

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

- Pakete installieren
```
apt install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox surf unclutter
```

- Config files an den richtigen Ort kopieren
```
cp /opt/scoreboard/client-config/autostart.html /home/pi/autostart.html
cp /opt/scoreboard/client-config/autostart /home/pi/.config/autostart

```

Im editor `/home/pi/.bash_profile` öffnen und auf der untersten Linie einfügen:
```
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx
```

Config-Menü öffnen
```
raspi-config
```
Folgende Option auswählen:
- **3** Boot Options
    - **B1** Desktop / CLI
        - **B2** Console Autologin

> Nach einem `reboot` sollte sich nun automatisch der Browser öffnen.
