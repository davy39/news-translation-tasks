---
title: Comment créer un serveur Django exécutant uWSGI, NGINX et PostgreSQL sur AWS
  EC2 avec Python 3.6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-26T18:38:32.000Z'
originalURL: https://freecodecamp.org/news/django-uwsgi-nginx-postgresql-setup-on-aws-ec2-ubuntu16-04-with-python-3-6-6c58698ae9d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RoxYjB7zefsqzjUMLLaprQ.png
tags:
- name: AWS
  slug: aws
- name: Django
  slug: django
- name: nginx
  slug: nginx
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer un serveur Django exécutant uWSGI, NGINX et PostgreSQL sur
  AWS EC2 avec Python 3.6
seo_desc: 'By Sumeet Kumar

  Getting a server up and running for a new project every time might be time-consuming
  or difficult for new developers. So I thought I’d write a step-by-step guide that
  will ease the deployment process.

  If you’re in no mood to read, you...'
---

Par Sumeet Kumar

Mettre en place un serveur pour un nouveau projet chaque fois peut être chronophage ou difficile pour les nouveaux développeurs. J'ai donc pensé écrire un guide étape par étape qui facilitera le processus de déploiement.

**Si vous n'avez pas envie de lire, vous pouvez copier-coller chaque étape comme décrit (remplacez les valeurs) et mettre votre serveur en route ?**

#### Prérequis :

1. Une instance Amazon Linux EC2 en cours d'exécution avec la paire de clés associée (_accès ssh_).
2. **Les ports 22, 80** doivent être ouverts pour cette instance.
3. Une application Django que vous souhaitez déployer.
4. Les paramètres de la base de données sont configurés pour utiliser PostgreSQL.
5. Le fichier _requirements.txt_ est présent dans votre application, contenant la liste des dépendances à installer.
6. Un dépôt Git pour votre application Django.

### SSH & mise à jour de l'instance Ubuntu

Vous devez vous connecter en SSH à votre instance EC2, assurez-vous donc que le **port 22** est ouvert pour votre instance, puis effectuez une mise à jour/upgrade.

```
ssh -i chemin-vers-votre-clé.pem ubuntu@votre-ip-publique-aws

sudo apt-get update && sudo apt-get upgrade -y
```

### Installation de Python 3.6.x sur AWS EC2 (Ubuntu 16.04)

Nous allons télécharger le fichier **tar.xz** depuis le site officiel, puis l'installer manuellement. Avant cela, nous devons installer certaines dépendances requises.

#### Construction et installation des dépendances

```
sudo apt install build-essential checkinstall

sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev
```

#### Téléchargement et installation manuelle de la version requise de Python

```
cd /opt && sudo wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz

sudo tar -xvf Python-3.6.6.tar.xz

cd Python-3.6.6/

sudo ./configure

sudo make && sudo make install
```

#### Suppression du fichier téléchargé

```
sudo rm -rf Python-3.6.6.tar.xz
```

#### Vérification de la version de Python

```
python3 -V
> Python 3.6.6
```

### Configuration de l'utilisateur Ubuntu pour notre application

Django est un framework très sécurisé, je suis d'accord. Mais les applications web sont encore vulnérables. Il est bon de faire tourner votre application en tant qu'utilisateur système avec des privilèges limités, ce qui a un accès limité aux ressources de votre serveur. Dans cette section, nous allons ajouter un nouvel utilisateur et un groupe de permissions à notre instance EC2.

#### Ajout d'un groupe système Ubuntu 'nom_du_groupe' [webapps dans mon cas] et attribution d'un utilisateur 'nom_utilisateur' [bunny dans mon cas] à ce groupe

```
sudo groupadd --system webapps
sudo useradd --system --gid webapps --shell /bin/bash --home /webapps/nom_du_projet bunny
```

Note : Je suppose que "**nom_du_projet**" est le nom que vous avez utilisé pendant "**django-admin startproject <nom>**"

#### Création d'un répertoire pour stocker votre application

Créez un répertoire pour stocker votre application dans /webapps/nom_du_projet/. Changez le propriétaire de ce répertoire pour votre utilisateur d'application bunny :

```
sudo mkdir -p /webapps/nom_du_projet/

sudo chown bunny /webapps/nom_du_projet/
```

#### Autoriser un accès limité aux autres utilisateurs du groupe au répertoire de l'application

```
sudo chown -R bunny:users /webapps/nom_du_projet

sudo chmod -R g+w /webapps/nom_du_projet
```

#### Vous pouvez maintenant basculer vers votre utilisateur

```
sudo su - bunny

// votre console passera à quelque chose comme ceci
bunny@ip-172-31-5-231:~$
```

Pour revenir à l'utilisateur **sudo**, il suffit de faire `**ctrl+d**` et cela fermera le terminal de l'utilisateur.

### Installation et configuration de PostgreSQL

#### Installation de PostgreSQL & création de la base de données

```
sudo apt install postgresql postgresql-contrib

sudo su - postgres

postgres@ip-172-31-5-231:~$ psql

postgres=# CREATE DATABASE nom_de_la_base_de_donnees;
```

#### Changement du mot de passe par défaut pour postgres dans le terminal **psql**

```
postgres=# \password
```

### Déploiement de l'application Django sur l'instance EC2 via Git dans un environnement virtuel

Déployer votre application en utilisant un environnement virtuel permet à votre application et à ses dépendances d'être gérées séparément. Il est bon de garder votre application isolée.

Utiliser le concept d'environnement est pratique lorsque vous déployez plus d'une application Django sur une seule instance pour les garder, ainsi que leurs dépendances, isolées les unes des autres.

Nous allons créer un [environnement virtuel](https://docs.python.org/3.6/library/venv.html) dans le répertoire de notre utilisateur système (_bunny_). Avant cela, nous allons installer git en tant qu'utilisateur _sudo_.

#### Installation de Git et récupération de votre code depuis le dépôt git

```
sudo apt-get install git

sudo su - bunny

// changez pour votre lien de dépôt https ou ssh
bunny@ip-172-31-5-231:~$ git remote add origin 

git@github.com:<utilisateur>/<depot-utilisateur>.git

bunny@ip-172-31-5-231:~$ git pull origin <nom_de_la_branche>
```

Notez que nous n'avons pas cloné notre dépôt complet ici. Au lieu de cela, nous avons manuellement défini notre lien git et seulement tiré la branche que nous voulons déployer sur cette instance. Vous pouvez avoir une instance différente pour votre développement, bêta, ou application web prête pour la production correspondant à chaque branche sur git.

#### Création d'un environnement virtuel utilisant Python 3.6 dans le répertoire courant

```
bunny@ip-172-31-5-231:~$ python3.6 -m venv .
bunny@ip-172-31-5-231:~$ source bin/activate
(nom_du_projet)bunny@ip-172-31-5-231:~$ pip install -r requirements.txt
```

À ce stade, nous avons réussi à configurer notre projet. Maintenant, nous devons exécuter quelques commandes **manage.py**. Cela nécessitera que nous soyons dans le répertoire où notre manage.py est présent, ou chaque fois que nous devons donner un chemin vers celui-ci :

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ python <chemin-vers->manage.py migrate

(nom_du_projet)bunny@ip-172-31-5-231:~$ python <chemin-vers->manage.py createsuperuser

(nom_du_projet)bunny@ip-172-31-5-231:~$ python <chemin-vers->manage.py collectstatic
```

Note : La commande `collectstatic` nécessite que la configuration STATIC soit correctement configurée. Nous n'en discutons pas ici, car cela n'est pas dans le cadre de ce tutoriel.

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ python <chemin-vers->manage.py runserver 0.0.0.0:8000
```

Cela démarrera le serveur de développement sur le port `8000`. **En supposant que le port 8000 est également ouvert pour votre instance, vous pouvez visiter le nom de domaine ou l'adresse IP de votre serveur suivi de `8000` dans votre navigateur.**

```
http://votre_nom_de_domaine_ou_ip_publique:8000
```

```
http://votre_nom_de_domaine_ou_ip_publique:8000/admin
```

**Note : N'oubliez pas d'ajouter votre domaine ou IP à ALLOWED_HOST dans votre settings.py**

### Configuration du serveur d'application uWSGI

Maintenant que nous avons notre projet configuré et prêt à fonctionner, nous pouvons configurer uWSGI pour servir notre application sur le web au lieu du serveur de développement léger fourni par Django.

**Si vous pensez à exécuter la commande runserver sur un écran, abandonnez. Le serveur de développement avec Django est terriblement léger, très peu sécurisé et non scalable.**

Vous pouvez installer uWSGI soit dans virtualenv soit globalement et le configurer en conséquence.

Dans ce tutoriel, nous allons installer uWSGI dans _virtualenv_. Avant de pouvoir installer uWSGI, nous avons besoin des fichiers de développement Python sur lesquels le logiciel repose.

#### Installation de uWSGI avec ses dépendances

```
sudo apt-get install python3-dev
```

```
sudo su - bunny
```

```
bunny@ip-172-31-5-231:~$ source bin/activate
```

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ pip install uwsgi
```

Lançons le serveur en utilisant uWSGI. Cette commande fait la même chose qu'un _manage.py runserver_. Vous devez remplacer les valeurs en conséquence pour tester avec succès avec cette commande.

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ uwsgi --http :8000 --home <chemin-vers-virtualenv> --chdir <chemin-vers-repertoire-manage.py> -w <nom-du-projet>.wsgi
```

#### Création du fichier de configuration uWSGI

Exécuter uWSGI depuis la ligne de commande n'est utile que pour les tests. Pour un déploiement réel, nous allons créer un fichier **_.ini_** quelque part dans le répertoire de notre utilisateur système. Ce fichier contiendra toute la configuration pour gérer une charge de requêtes importante, et peut être ajusté en conséquence.

Plus tard dans ce tutoriel, nous allons exécuter uWSGI derrière NGINX. NGINX est hautement compatible avec uWSGI et a un support intégré pour interagir avec uWSGI.

#### Créer un répertoire **conf** dans le répertoire de votre utilisateur système où vous stockerez **uwsgi.ini**

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ mkdir conf
```

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ cd conf
```

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ nano uwsgi.ini
```

Copiez le code ci-dessous depuis le gist et sauvegardez-le. Je pense que les commentaires sont suffisamment explicatifs pour chaque option.

**NOTE : `updateMe` doit être remplacé par le nom de votre projet. C'est le même nom que vous avez donné ci-dessus lors de la création du répertoire de l'utilisateur système, alors mettez-le à jour en conséquence.**

```
[uwsgi]

# indiquer à l'utilisateur d'exécuter le fichier
uid = bunny

# indiquer au groupe d'exécuter le fichier
gid = webapps

# nom du projet que vous avez utilisé pendant "django-admin startproject <nom>"
project_name = updateMe

# construction du chemin de base vers le répertoire du projet [Dans mon cas, ce répertoire est aussi où se trouve mon environnement virtuel]
base_dir = /webapps/%(project_name)

# définir PYTHONHOME/virtualenv ou définir où se trouve mon environnement virtuel
virtualenv = %(base_dir)

# changer le répertoire courant vers le répertoire du projet où se trouve manage.py
chdir = %(base_dir)/src/

# chargement du module wsgi
module =  %(project_name).wsgi:application

# activer le processus maître avec n processus enfants
master = true
processes = 4

# activer le multithreading et attribuer des threads par processus
# enable-threads  = true
# threads = 2

# Activer la mise en mémoire tampon postérieure à N octets. sauvegarder sur le disque tous les corps HTTP plus grands que la limite $
post-buffering = 204800

# Sérialiser l'utilisation de accept() (si possible).
thunder-lock = True


# Lier à la socket spécifiée en utilisant le protocole uwsgi par défaut.
uwsgi-socket = %(base_dir)/run/uwsgi.sock

# définir les permissions des sockets UNIX pour l'accès
chmod-socket = 666

# Définir le délai d'attente des sockets internes en secondes.
socket-timeout = 300

# Définir le temps maximum (en secondes) qu'un worker peut prendre pour recharger/s'éteindre.
reload-mercy = 8

# Recharger un worker si son utilisation de l'espace d'adressage est supérieure à la valeur spécifiée (en mégaoctets).
reload-on-as = 512

# redémarrer les processus prenant plus de 50 secondes
harakiri = 50

# redémarrer les processus après avoir servi 5000 requêtes
max-requests = 5000

# effacer l'environnement à la sortie
vacuum = true

# Lorsqu'il est activé (définir sur True), seuls les messages et erreurs internes de uWSGI sont enregistrés.
disable-logging = True

# chemin vers l'endroit où les logs de uwsgi seront sauvegardés
logto = %(base_dir)/log/uwsgi.log

# taille maximale du fichier log 20MB
log-maxsize = 20971520

# Définir le nom du fichier log après rotation.
log-backupname = %(base_dir)/log/old-uwsgi.log

# Recharger uWSGI si le fichier ou répertoire spécifié est modifié/touché.
touch-reload = %(base_dir)/src/

# Définir le nombre de cœurs (CPU) à allouer à chaque processus worker.
# cpu-affinity = 1

# Recharger les workers après ce nombre de secondes. Désactivé par défaut.
max-worker-lifetime = 300
```

J'essaie de rendre tout facile avec des explications claires. Vérifiez les chemins, le nom du répertoire et autres entrées que vous devez remplacer.

Nous devons créer le fichier log et le répertoire run où notre fichier socket sera créé, que nous venons de mentionner dans notre uwsgi.ini :

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ mkdir log
```

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ mkdir run
```

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ touch log/uwsgi.log
```

Assurez-vous de changer les permissions pour ces deux répertoires afin que chaque groupe ou utilisateur puisse écrire ou exécuter des fichiers dans ces répertoires :

```
$ sudo chmod 777 /webapps/updateMe/run
```

```
$ sudo chmod 777 /webapps/updateMe/log
```

Maintenant, essayons de lancer le serveur en utilisant **uwsgi.ini** que nous venons de créer.

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ uwsgi --ini /webapps/updateMe/conf/uwsgi.ini
```

Si tout jusqu'à maintenant est configuré correctement, alors cela devrait fonctionner. Sinon, vous devez revenir en arrière pour vérifier ce que vous avez manqué (comme le chemin/nom du projet, etc.).

Pour vérifier les logs de uwsgi, vous pouvez utiliser **cat** ou **tail** sur uwsgi.log :

```
(nom_du_projet)bunny@ip-172-31-5-231:~$ tail log/uwsgi.log
```

#### Création d'un fichier Unit pour systemd pour uWSGI

À ce stade, si tout est correct, vous pouvez même exécuter cette commande dans [screen](http://manpages.ubuntu.com/manpages/bionic/en/man1/screen.1.html) et la détacher — mais encore une fois, ce n'est pas une bonne pratique du tout. Au lieu de cela, nous allons créer un service système et laisser **systemd** (le gestionnaire de services d'Ubuntu) s'en occuper.

#### Retour à l'utilisateur sudo

```
$ sudo nano /etc/systemd/system/uwsgi.service
```

et copiez-collez le code depuis le gist ci-dessous. N'oubliez pas de mettre à jour et de vérifier les noms/chemins qui conviennent à votre application :

```
[Unit]
Description=Instance uWSGI pour servir le projet updateMe
After=network.target

[Service]
User=bunny
Group=webapps
WorkingDirectory=/webapps/nom_du_projet/src
Environment="PATH=/webapps/nom_du_projet/bin"
ExecStart=/webapps/nom_du_projet/bin/uwsgi --ini /webapps/nom_du_projet/conf/uwsgi.ini
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

Après avoir sauvegardé le fichier ci-dessus et l'avoir fermé, vous pouvez exécuter les commandes suivantes :

**Recharger le démon systemctl pour recharger la configuration du gestionnaire systemd et recréer l'arborescence de dépendance entière**

```
$ sudo systemctl daemon-reload
```

**Activer le service uwsgi pour qu'il démarre au redémarrage du système**

```
$ sudo systemctl enable uwsgi
```

**Démarrer le service uwsgi**

```
$ sudo service uwsgi start
```

**Redémarrer le service uwsgi**

```
$ sudo service uwsgi restart
```

**Vérifier le statut du service uwsgi**

```
$ sudo service uwsgi status
```

Prenez une grande inspiration ici si tout s'est bien passé. Nous venons de terminer la configuration de la partie la plus difficile de ce tutoriel, alors vous devriez être fier.

Ensuite, nous allons configurer NGINX, et ensuite nous aurons terminé ! Je sais que cela prend un peu de temps, mais croyez-moi — une fois terminé, vous serez aussi heureux que je le serai après avoir publié ce tutoriel.

### Configuration de NGINX sur EC2 pour uWSGI

NGINX est un serveur léger, et nous allons l'utiliser comme un proxy inverse.

**Nous pourrions laisser uWSGI fonctionner directement sur le port 80, mais NGINX a beaucoup plus d'[avantages](https://serverfault.com/questions/590819/why-do-i-need-nginx-when-i-have-uwsgi/590833#590833) qui le rendent souhaitable.** De plus, NGINX inclut nativement le [support](https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html) pour uWSGI.

#### Assez parlé, installons NGINX sur notre instance

```
$ sudo apt-get install nginx
```

Maintenant, lorsque vous allez sur **http://votre-ip-publique-ou-adresse**, vous verrez une page de bienvenue de Nginx. Cela est dû au fait que NGINX écoute le port 80 selon sa configuration par défaut.

NGINX a deux répertoires, **sites-available** et **sites-enabled**, qui nécessitent notre attention. **sites-available** stocke tous les fichiers de configuration pour tous les sites disponibles sur cette instance particulière. **sites-enabled** stocke le lien symbolique pour chaque site activé vers le répertoire sites-available.

Par défaut, il n'y a qu'un seul fichier de configuration nommé default qui a une configuration de base pour NGINX. Vous pouvez soit le modifier, soit en créer un nouveau. Dans notre cas, je vais le supprimer :

```
$ sudo rm -rf /etc/nginx/sites-available/default
```

```
$ sudo rm -rf /etc/nginx/sites-enabled/default
```

Créons notre fichier **nginx-uwsgi.conf** pour connecter la requête du navigateur au serveur uwsgi que nous exécutons dans site-available :

```
$ sudo nano /etc/nginx/sites-available/nginx-uwsgi.conf
```

et copiez le code suivant depuis le gist ci-dessous :

```
upstream updateMe_dev {
    server unix:/webapps/updateMe/run/uwsgi.sock;
}

server {
    listen 80;
    server_name votre-IP-ou-adresse-ici;
    charset utf-8;

    client_max_body_size 128M;

    location /static {
    # chemin exact vers l'endroit où vos fichiers statiques sont situés sur le serveur
    # [la plupart du temps vous n'en aurez pas besoin, car vous utiliserez un service de stockage pour cela]
        alias /webapps/updateMe/static_local;
    }

    location /media {
    # chemin exact vers l'endroit où vos fichiers media sont situés sur le serveur
    # [la plupart du temps vous n'en aurez pas besoin, car vous utiliserez un service de stockage pour cela]
        alias /webapps/updateMe/media_local;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass updateMe_dev;
        uwsgi_read_timeout 300s;
        uwsgi_send_timeout 300s;
    }

    access_log /webapps/updateMe/log/dev-nginx-access.log;
    error_log /webapps/updateMe/log/dev-nginx-error.log;
}
```

#### Créer un lien symbolique dans le répertoire sites-enabled pour le même

```
$ sudo ln -s /etc/nginx/sites-available/nginx-uwsgi.conf /etc/nginx/sites-enabled/nginx-uwsgi.conf
```

C'est tout, nous y sommes presque, sur le point de terminer...

#### Recharger le démon systemctl

```
$ sudo systemctl daemon-reload
```

#### Activer le service nginx au redémarrage du système

```
$ sudo systemctl enable nginx
```

#### Démarrer le service Nginx

```
$ sudo service nginx start
```

Tester Nginx. Il devrait retourner OK, Successful comme partie du résultat.

```
$ sudo nginx -t
```

Si NGINX échoue, vous pouvez vérifier son dernier fichier error-log ou access-log sur le chemin spécifié par nous dans sa configuration.

```
$ tail -f /webapps/updateMe/log/nginx-error.log
```

```
$ tail -f /webapps/updateMe/log/nginx-access.log
```

#### Redémarrer le service Nginx

```
$ sudo service nginx restart
```

#### Vérifier le statut du service Nginx

```
$ sudo service nginx status
```

Vous devriez maintenant pouvoir accéder à votre application à l'adresse [**http://votre-ip-publique-ou-adresse**](http://votre-ip-publique-ou-adresse)

Eh bien, c'est la fin de ce long tutoriel. J'espère que vous avez obtenu ce que vous attendiez. Merci de m'avoir suivi.

PS : uWSGI + NGINX + Django est hautement personnalisable pour répondre à toutes les exigences à grande échelle. Cela dit, l'optimisation de base réside toujours au niveau de l'application. La façon dont vous codez et utilisez l'ORM Django ou les requêtes SQL brutes, etc., vous aidera davantage.