---
title: 'Django en production : conseils pour survivre au déploiement'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-24T22:21:00.000Z'
originalURL: https://freecodecamp.org/news/django-in-the-wild-tips-for-deployment-survival-9b491081c2e4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5w9DNocznYRp8ndO
tags:
- name: Django
  slug: django
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Django en production : conseils pour survivre au déploiement'
seo_desc: 'By Ali Alavi

  Before deploying your Django web app in the real world, you need to make sure your
  project is production-ready. Better to start implementing them earlier. It saves
  you and your team a lot of time and headache. Here are some points I lear...'
---

Par Ali Alavi

Avant de déployer votre application web Django dans le monde réel, vous devez vous assurer que votre projet est prêt pour la production. Mieux vaut commencer à les implémenter plus tôt. Cela vous fait économiser, à vous et à votre équipe, beaucoup de temps et de maux de tête. Voici quelques points que j'ai appris en cours de route :

1. Utilisez pipenv (ou requirements.txt + venv). Commitez Pipefile et Pipefile.lock (ou requirements.txt). Nommez votre venv.
2. Ayez un script de démarrage rapide.
3. Écrivez des tests. Utilisez le [Framework de test Django](https://docs.djangoproject.com/en/2.0/topics/testing/overview/) et [Hypothesis](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python).
4. Utilisez [environ](https://github.com/joke2k/django-environ) et [direnv](https://direnv.net/) pour gérer vos paramètres et charger automatiquement vos variables d'environnement.
5. Assurez-vous que tous les développeurs committent leurs migrations. Squash les migrations de temps en temps. Réinitialisez-les si nécessaire. Architecturez votre projet pour des migrations plus fluides. Lisez à propos des migrations.
6. Utilisez l'intégration continue. Protégez votre branche master.
7. Passez en revue la [liste de contrôle de déploiement officielle de Django](https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/).
8. Ne gérez pas votre propre serveur, mais si vous devez le faire, utilisez une structure de répertoire appropriée, et utilisez Supervisord, Gunicorn et NGINX.

Cette liste a grandi organiquement alors que je passais en revue la sortie de notre première application Django, et n'est pas exhaustive. Mais je pense que ce sont quelques-uns des points les plus importants dont vous devez être conscient.

Lisez la suite pour une discussion sur chacun des points.

## Gérez vos dépendances et environnements virtuels de la bonne manière

Vous et votre équipe devriez vous mettre d'accord sur une manière de gérer vos dépendances et environnements virtuels. Je recommande soit d'utiliser [pipenv](https://github.com/pypa/pipenv), qui est la nouvelle façon de gérer à la fois vos environnements virtuels et vos dépendances, soit d'utiliser la bonne vieille approche consistant à créer un venv et à suivre vos dépendances avec un fichier `requirements.txt`.

L'utilisation de l'approche `requirements.txt` est sujette aux erreurs humaines, car les développeurs ont tendance à oublier de mettre à jour la liste des paquets. Ce n'est pas un problème avec **pipenv**, car il met automatiquement à jour **Pipefile**. L'inconvénient de **pipenv** est qu'il n'a pas été utilisé assez longtemps. Même s'il est [officiellement recommandé](https://packaging.python.org/tutorials/managing-dependencies/) par la Python Software Foundation, vous pourriez avoir des problèmes à le faire fonctionner sur certaines machines. Personnellement, j'utilise encore l'ancienne approche, mais j'utiliserai **pipenv** pour mon prochain projet.

### Utilisation de venv et requirements.txt

Si vous utilisez Python ≥ 3.6 (ce que vous devriez faire), vous pouvez simplement en créer un avec `python -m venv ENV`. Assurez-vous de nommer votre environnement virtuel (au lieu d'utiliser `.`). Parfois, vous devez supprimer votre environnement virtuel et le recréer. Cela le rend plus facile. De plus, vous devriez ajouter le répertoire `ENV` à votre fichier `.gitignore` (je préfère le nom **ENV** au lieu de **venv**, **.env**, … car il se distingue lorsque je fais **ls** dans le dossier du projet).

Pour gérer les dépendances, chaque développeur exécute `pip freeze > requirements.txt` chaque fois qu'il installe un nouveau paquet, et l'ajoute et le commite dans le dépôt. Ils utiliseront `pip install -r requirements.txt` chaque fois qu'ils tirent depuis le dépôt distant.

### Utilisation de pipenv

Si vous utilisez **pipenv**, vous devez simplement ajouter [Pipfile et Pipfile.lock](https://github.com/pypa/pipenv/issues/598) à votre dépôt.

## Ayez un script de démarrage rapide

Cela aide à s'assurer que vos développeurs passent le moins de temps possible à travailler sur des choses non directement liées à leur travail.

Non seulement cela fait économiser du temps et de l'argent, mais cela garantit également qu'ils travaillent tous sur des environnements similaires (mêmes versions de Python et pip, par exemple).

Essayez donc d'automatiser autant de tâches de configuration que possible.

De plus, avoir un script de construction en une seule étape est exactement ce dont parle [la 2ème étape du Joel Test](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/).

Voici un petit script que j'utilise, qui économise à mes développeurs quelques frappes de touches :

```bash
#!/bin/bash
python3.6 -m venv ENV
source ENV/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
source .envrc
python ./manage.py migrate
python ./manage.py loaddata example-django/fixtures/quickstart.json
python ./manage.py runserver
```

## Écrivez des tests

Tout le monde sait qu'écrire des tests est une bonne pratique. Mais beaucoup l'ignorent, au nom, pensent-ils, d'un développement plus rapide. NE LE FAITES PAS. Les tests sont une nécessité absolue lorsqu'il s'agit d'écrire des logiciels utilisés en production, surtout lorsque vous travaillez en équipe. La seule façon de savoir que la dernière mise à jour n'a rien cassé est d'avoir des tests bien écrits. De plus, vous avez absolument besoin de tests pour l'intégration continue et la livraison de votre produit.

Django dispose d'un [Framework de test](https://docs.djangoproject.com/en/2.0/topics/testing/overview/) décent. Vous pouvez également utiliser des frameworks de test basés sur les propriétés tels que [Hypothesis](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python), qui vous aident à écrire des tests plus courts et mathématiquement rigoureux pour votre code. Dans de nombreux cas, écrire des tests basés sur les propriétés est plus rapide. En pratique, vous pourriez finir par utiliser ces deux frameworks pour écrire des tests complets, faciles à lire et à écrire.

## Utilisez des variables d'environnement pour les paramètres

Votre fichier **settings.py** est l'endroit où vous stockez tous les paramètres importants du projet : l'URL de votre base de données, les chemins vers les dossiers media et static, etc. Ceux-ci auront des valeurs différentes sur votre machine de développement et votre serveur de production. La meilleure façon de gérer cela est d'utiliser des variables d'environnement. La première étape consiste à mettre à jour votre [settings.py](https://gist.github.com/alialavia/da1c82a9f5194257d1de868decec933c) pour lire à partir des variables d'environnement, en utilisant [environ](https://github.com/joke2k/django-environ) :

```py
import environ
import os
root = environ.Path(__file__) - 2 # deux dossiers en arrière (/a/b/ - 2 = /)
env = environ.Env(DEBUG=(bool, False),) # définir les valeurs par défaut et le casting
GOOGLE_ANALYTICS_ID=env('GOOGLE_ANALYTICS_ID')

SITE_DOMAIN = env('SITE_DOMAIN') 
SITE_ROOT = root()

DEBUG = env('DEBUG') # False si non dans os.environ

DATABASES = {
    'default': env.db(), # Lève une exception ImproperlyConfigured si DATABASE_URL n'est pas dans os.environ
}

public_root = root.path('./public/')

MEDIA_ROOT = public_root('media')
MEDIA_URL = '/media/'

STATIC_ROOT = public_root('static')
STATIC_URL = '/static/'

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

..
```

Pour éviter de charger vos envvars manuellement, configurez [direnv](https://direnv.net/) sur vos machines de développement, et stockez les envvars dans un fichier `.envrc` dans votre répertoire de projet. Maintenant, chaque fois que vous faites `cd` dans le dossier de votre projet, les variables d'environnement sont automatiquement chargées. Ajoutez `.envrc` à votre dépôt (si tous les développeurs utilisent les mêmes paramètres), et assurez-vous d'exécuter `direnv allow` chaque fois qu'il y a un changement dans le fichier `.envrc`.

N'utilisez pas `direnv` sur votre serveur de production. Au lieu de cela, créez un fichier appelé **.server.envrc**, ajoutez-le à `.gitignore`, et mettez les paramètres de production là-bas. Maintenant, créez un script, `runinenv.sh`, pour sourcer automatiquement les variables d'environnement à partir de `.server.envrc`, activer l'environnement virtuel, et exécuter la commande fournie. Vous verrez comment il est utilisé dans la section suivante. Voici à quoi devrait ressembler `runinenv.sh` ([lien vers GitHub](https://gist.github.com/alialavia/7a29ea149870e151b4a27d53993d5d17)).

```bash
#!/bin/bash
WORKING_DIR=/home/myuser/example.com/example-django
cd ${WORKING_DIR}
source .server.envrc
source ENV/bin/activate
exec $@
```

## Gérez vos migrations correctement

Les migrations Django sont géniales, mais travailler avec elles, surtout en équipe, est loin d'être sans tracas.

Tout d'abord, vous devez vous assurer que tous les développeurs committent les fichiers de migration. Oui, vous pourriez (allez) finir par avoir des conflits, surtout si vous travaillez avec une grande équipe, mais c'est mieux que d'avoir un schéma incohérent.

En général, traiter avec les migrations n'est pas si facile. Vous devez savoir ce que vous faites, et vous devez suivre certaines bonnes pratiques pour assurer un flux de travail fluide.

Une chose que j'ai comprise est qu'il est généralement utile de squash les migrations de temps en temps (par exemple, sur une base hebdomadaire). Cela aide à réduire le nombre de fichiers et la taille du graphe de dépendances, ce qui entraîne un temps de construction plus rapide, et généralement moins (ou plus faciles à gérer) de conflits.

Parfois, il est plus facile de réinitialiser vos migrations et de les refaire, et parfois vous devez corriger manuellement les migrations en conflit ou les fusionner ensemble. En général, traiter avec les migrations est un sujet qui mérite son propre article, et il y a quelques bonnes lectures sur ce sujet :

* [Migrations Django et comment gérer les conflits](https://www.algotech.solutions/blog/python/django-migrations-and-how-to-manage-conflicts/)
* [Comment réinitialiser les migrations](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

De plus, la façon dont vos migrations de projet se terminent dépend de l'architecture de votre projet, de vos modèles, etc. Cela est particulièrement important lorsque votre base de code grandit, lorsque vous avez plusieurs applications, ou lorsque vous avez des relations compliquées entre les modèles.

Je vous recommande vivement de [lire cet excellent article sur la mise à l'échelle des applications Django](https://blog.doordash.com/tips-for-building-high-quality-django-apps-at-scale-a5a25917b2b5), qui couvre bien le sujet. Il contient également un petit script de migration utile.

## Utilisez l'intégration continue

L'idée derrière l'IC est simple : exécutez des tests dès que du nouveau code est poussé.

Utilisez une solution qui s'intègre bien avec votre plateforme de contrôle de version. J'ai fini par utiliser [CircleCI](https://circleci.com/). L'IC est particulièrement utile lorsque vous travaillez avec plusieurs développeurs, car vous pouvez être sûr que leur code passe tous les tests avant qu'ils n'envoient une pull request. Encore une fois, comme vous pouvez le voir, il est très important d'avoir des tests bien couverts en place. De plus, assurez-vous que votre branche master est protégée.

## Liste de contrôle de déploiement

Le site officiel de Django fournit une [liste de contrôle de déploiement pratique](https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/). Elle vous aide à assurer la sécurité et les performances de votre projet. Assurez-vous de suivre ces directives.

## Si vous devez gérer votre propre serveur...

Il y a de nombreuses bonnes raisons de ne pas gérer votre propre serveur. Docker vous offre plus de portabilité et de sécurité, et les architectures serverless, telles que AWS Lambda, peuvent vous offrir encore plus d'avantages pour moins d'argent.

Mais il y a des cas où vous avez besoin de plus de contrôle sur votre serveur (si vous avez besoin de plus de flexibilité, si vous avez des services qui ne peuvent pas fonctionner avec des applications conteneurisées — tels que les agents de surveillance de sécurité, etc.).

### Utilisez une structure de répertoire appropriée

La première chose à faire est d'utiliser une structure de dossiers appropriée. Si tout ce que vous voulez servir sur votre serveur est l'application Django, vous pouvez simplement cloner votre dépôt et l'utiliser comme votre répertoire principal. Mais ce n'est rarement le cas : généralement, vous devez également avoir quelques pages statiques (page d'accueil, contacts, ...). Elles doivent être séparées de votre base de code Django.

Une bonne façon de procéder est de créer un dépôt parent, qui a différentes parties de votre projet comme sous-modules. Vos développeurs Django travaillent sur un dépôt django, vos designers travaillent sur le dépôt de la page d'accueil, ... et vous intégrez le tout dans un dépôt :

```
example.com/
   example-django/
   homepage/
```

### Utilisez Supervisord, NGINX et Gunicorn

Bien sûr, `manage runserver` fonctionne, mais seulement pour un test rapide. Pour tout ce qui est sérieux, vous devez utiliser un serveur d'application approprié. [Gunicorn](http://gunicorn.org/) est la solution.

Gardez à l'esprit qu'un serveur d'application est un processus de longue durée. Et vous devez vous assurer qu'il continue de fonctionner, est redémarré automatiquement après une panne du serveur, enregistre les erreurs correctement, etc. À cette fin, nous utilisons `[supervisord](http://supervisord.org/)`.

Supervisord a besoin d'un fichier de configuration, dans lequel nous indiquons comment nous voulons que nos processus s'exécutent. Et il n'est pas limité à notre serveur d'application. Si nous avons d'autres processus de longue durée (par exemple, celery), nous devons les définir dans `/etc/supervisor/supervisord.conf`. Voici un exemple ([également sur GitHub](https://gist.github.com/alialavia/c3b5ec16823a1278833c66cfd3a638ca)) :

```
[supervisord]
nodaemon=true
logfile=supervisord.log

[supervisorctl]

[inet_http_server]
port = 127.0.0.1:9001

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[program:web-1]
command=/home/myuser/example.com/example-django/runinenv.sh gunicorn example.wsgi --workers 3 --reload --log-level debug --log-file gunicorn.log --bind=0.0.0.0:8000
autostart=true
autorestart=true
stopsignal=QUIT
stdout_logfile=/var/log/example-django/web-1.log
stderr_logfile=/var/log/example-django/web-1.error.log
user=myuser
directory=/home/myuser/example.com/example-django

[program:celery-1]
command=/home/myuser/example.com/example-django/runinenv.sh celery worker --app=example --loglevel=info
autostart=true
autorestart=true
stopsignal=QUIT
stdout_logfile=/var/log/example-django/celery-1.log
stderr_logfile=/var/log/example-django/celery-1.error.log
user=myuser
directory=/home/myuser/example.com/example-django

[program:beat-1]
command=/home/myuser/example.com/example-django/runinenv.sh celery beat --app=example --loglevel=info
autostart=true
autorestart=true
stopsignal=QUIT
stdout_logfile=/var/log/example-django/beat-1.log
stderr_logfile=/var/log/example-django/beat-1.error.log
user=myuser
directory=/home/myuser/example.com/example-django

[group:example-django]
programs=web-1,celery-1,beat-1
```

Remarquez comment nous utilisons `runinenv.sh` ici (lignes 14, 24 et 34). De plus, faites attention à la ligne 14, où nous disons à **gunicorn** de dispatcher 3 workers. Ce nombre dépend du nombre de cœurs de votre serveur. [Le nombre recommandé de workers est : 2*nombre_de_cœurs + 1.](http://docs.gunicorn.org/en/stable/design.html#how-many-workers)

Vous avez également besoin d'un proxy inverse pour connecter votre serveur d'application au monde extérieur. Utilisez simplement [NGINX](https://www.nginx.com/), car il a une large base d'utilisateurs et est très facile à configurer ([vous pouvez également trouver ce code sur GitHub](https://gist.github.com/alialavia/63805a95cb821c19c553d0c21a8da938)) :

```nginx
server {
    server_name www.example.com;
    access_log  /var/log/nginx/example.com.log;
    error_log    /var/log/nginx/example.com.error.log debug;
    root  /home/myuser/example.com/homepage;
    sendfile on;
    
# si l'uri n'est pas trouvé, cherchez index.html, sinon passez tout à gunicorn
    location / {
 index index.html;
 try_files $uri $uri/
     @gunicorn;
    }
    
# Django media
    location /media  {
        alias /home/myuser/example.com/example-django/public/media;      # vos fichiers media de votre projet Django
    }
    
# Django static files
    location /static {
        alias /home/myuser/example.com/example-django/public/static;   # vos fichiers statiques de votre projet Django
    }
    
location @gunicorn {

proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
 #proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_redirect off;
 
proxy_pass http://0.0.0.0:8000;
    }
    
client_max_body_size 100M;

listen 443 ssl; # géré par Certbot
    ssl_certificate /etc/letsencrypt/live/www.example.com/fullchain.pem; # géré par Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.example.com/privkey.pem; # géré par Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # géré par Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # géré par Certbot
    
}

server {
    server_name example.com;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/www.example.com/fullchain.pem; # géré par Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.example.com/privkey.pem; # géré par Certbot
    return 301 https://www.example.com$request_uri;
    
}

server {
    if ($host = www.example.com) {
        return 301 https://$host$request_uri;
    } # géré par Certbot
    
if ($host = example.com) {
        return 301 https://$host$request_uri;
    } # géré par Certbot
    
listen 80 default_server;
    listen [::]:80 default_server;
    server_name example.com www.example.com;
    return 301 https://$server_name$request_uri;
}
```

Stockez le fichier de configuration dans `/etc/nginx/sites-available`, et créez un lien symbolique vers celui-ci dans `/etc/nginx/sites-enabled`.

J'espère que vous avez trouvé cet article utile. Faites-moi savoir ce que vous en pensez, et montrez-lui un peu d'❤ si vous le souhaitez.