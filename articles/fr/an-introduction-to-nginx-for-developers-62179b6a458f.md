---
title: Une introduction à NGINX pour les développeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T11:05:27.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-nginx-for-developers-62179b6a458f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jD-jS_oVIVHZJxLSM3_c1A.jpeg
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction à NGINX pour les développeurs
seo_desc: 'By Stefanos Vardalos

  Picture this - you’ve created a web application and are now searching for the right
  web server to host it from.

  Your application might consist of multiple static files — HTML, CSS, and JavaScript,
  a backend API service or even mu...'
---

Par Stefanos Vardalos

Imaginez ceci - vous avez créé une application web et vous recherchez maintenant le bon serveur web pour l'héberger.

Votre application peut consister en plusieurs fichiers statiques — HTML, CSS et JavaScript, un service d'API backend ou même plusieurs services web. Utiliser Nginx pourrait être ce que vous recherchez, et il y a plusieurs raisons à cela.

NGINX est un serveur web puissant et utilise une architecture non threadée, pilotée par événements, qui lui permet de surpasser Apache s'il est configuré correctement. Il peut également faire d'autres choses importantes, telles que l'équilibrage de charge, la mise en cache HTTP, ou être utilisé comme un proxy inverse.

![Image](https://cdn-media-1.freecodecamp.org/images/RooSvbKlAWsOjkz8JPactXH-GPf4Pe6DC3Ue)
_Architecture NGINX_

Dans cet article, je vais couvrir quelques étapes de base sur la façon d'installer et de configurer les parties les plus courantes de NGINX.

#### Installation de base — Architecture

Il existe deux façons d'installer NGINX, soit en utilisant un binaire pré-compilé, soit en le construisant à partir des sources.

La première méthode est beaucoup plus simple et rapide, mais construire à partir des sources permet d'inclure divers modules tiers qui rendent NGINX encore plus puissant. Cela nous permet de le personnaliser pour répondre aux besoins de l'application.

Pour installer un package Debian pré-compilé, la seule chose que vous avez à faire est :

```
sudo apt-get updatesudo apt-get install nginx
```

Après que le processus d'installation soit terminé, vous pouvez vérifier que tout est OK en exécutant la commande ci-dessous, qui devrait imprimer la dernière version de NGINX.

```
sudo nginx -vnginx version: nginx/1.6.2
```

Votre nouveau serveur web sera installé à l'emplacement `/etc/nginx**/**`. Si vous allez dans ce dossier, vous verrez plusieurs fichiers et dossiers. Les plus importants qui nécessiteront notre attention plus tard sont le fichier `nginx.conf` et le dossier `sites-available`.

#### Paramètres de configuration

Les paramètres principaux de NGINX se trouvent dans le fichier `nginx.conf`, qui par défaut ressemble à ceci.

```
user www-data;worker_processes 4;pid /run/nginx.pid;events {	worker_connections 768;	# multi_accept on;}http {	sendfile on;	tcp_nopush on;	tcp_nodelay on;	keepalive_timeout 65;	types_hash_max_size 2048;	# server_tokens off;	# server_names_hash_bucket_size 64;	# server_name_in_redirect off;	include /etc/nginx/mime.types;	default_type application/octet-stream;	access_log /var/log/nginx/access.log;	error_log /var/log/nginx/error.log;	gzip on;	gzip_disable "msie6";	# gzip_vary on;	# gzip_proxied any;	# gzip_comp_level 6;	# gzip_buffers 16 8k;	# gzip_http_version 1.1;	# gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;	include /etc/nginx/conf.d/*.conf;	include /etc/nginx/sites-enabled/*;}
```

Le fichier est structuré en **Contextes**. Le premier est le contexte **events**, et le second est le contexte **http**. Cette structure permet une certaine stratification avancée de votre configuration, car chaque contexte peut avoir d'autres contextes imbriqués qui héritent de tout de leur parent mais peuvent également remplacer un paramètre si nécessaire.

Différentes choses dans ce fichier peuvent être ajustées en fonction de vos besoins, mais NGINX est si simple à utiliser que vous pouvez vous en sortir même avec les paramètres par défaut. Certains des éléments les plus importants du fichier de configuration NGINX sont :

* **worker_processes :** Ce paramètre définit le nombre de processus de travail que NGINX utilisera. Comme NGINX est monothread, ce nombre doit généralement être égal au nombre de cœurs CPU.
* **worker_connections :** Il s'agit du nombre maximum de connexions simultanées pour chaque processus de travail et indique à nos processus de travail combien de personnes peuvent être servies simultanément par NGINX. Plus il est grand, plus NGINX pourra servir d'utilisateurs simultanés.
* **access_log & error_log :** Ce sont les fichiers que NGINX utilisera pour journaliser toute erreur et tentative d'accès. Ces journaux sont généralement examinés pour le débogage et le dépannage.
* **gzip :** Ce sont les paramètres pour la compression GZIP des réponses NGINX. Activer celui-ci ainsi que les divers sous-paramètres qui par défaut sont commentés entraînera une amélioration assez importante des performances. Parmi les sous-paramètres de GZIP, il faut prendre soin du gzip_comp_level, qui est le niveau de compression et varie de 1 à 10. Généralement, cette valeur ne doit pas être supérieure à 6 — le gain en termes de réduction de taille est insignifiant, car il nécessite une utilisation beaucoup plus importante du CPU. gzip_types est une liste de types de réponse sur lesquels la compression sera appliquée.

Votre installation NGINX peut supporter bien plus qu'un seul site web, et les fichiers qui définissent les sites de votre serveur se trouvent dans le répertoire /etc/nginx/sites-available.

Cependant, les fichiers de ce répertoire ne sont pas « actifs » — vous pouvez avoir autant de fichiers de définition de site ici que vous le souhaitez, mais NGINX ne fera rien avec eux à moins qu'ils ne soient liés symboliquement dans le répertoire /etc/nginx/sites-enabled (vous pourriez également les copier là-bas, mais la liaison symbolique garantit qu'il n'y a qu'une seule copie de chaque fichier à suivre).

Cela vous donne une méthode pour mettre rapidement des sites web en ligne et les mettre hors ligne sans avoir à supprimer réellement des fichiers — lorsque vous êtes prêt pour qu'un site soit mis en ligne, liez-le symboliquement dans sites-enabled et redémarrez NGINX.

Le répertoire `sites-available` inclut les configurations pour les hôtes virtuels. Cela permet au serveur web d'être configuré pour plusieurs sites qui ont des configurations séparées. Les sites dans ce répertoire ne sont pas actifs et ne sont activés que si nous créons un lien symbolique dans le dossier `sites-enabled`.

Soit créez un nouveau fichier pour votre application, soit modifiez celui par défaut. Une configuration typique ressemble à celle ci-dessous.

```
upstream remoteApplicationServer {    server 10.10.10.10;}upstream remoteAPIServer {    server 20.20.20.20;    server 20.20.20.21;    server 20.20.20.22;    server 20.20.20.23;}server {    listen 80;    server_name www.customapp.com customapp.com    root /var/www/html;    index index.html        location / {            alias /var/www/html/customapp/;            try_files $uri $uri/ =404;        }        location /remoteapp {            proxy_set_header   Host             $host:$server_port;            proxy_set_header   X-Real-IP        $remote_addr;            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;            proxy_pass http://remoteAPIServer/;        }        location /api/v1/ {            proxy_pass https://remoteAPIServer/api/v1/;            proxy_http_version 1.1;            proxy_set_header Upgrade $http_upgrade;            proxy_set_header Connection 'upgrade';            proxy_set_header Host $host;            proxy_cache_bypass $http_upgrade;            proxy_redirect http:// https://;        }}
```

Tout comme le `nginx.conf`, celui-ci utilise également le concept de contextes imbriqués (et tous ceux-ci sont également imbriqués dans le contexte **HTTP** de nginx.conf, donc ils héritent également de tout ce qui s'y trouve).

Le contexte **server** définit un serveur virtuel spécifique pour gérer les requêtes de vos clients. Vous pouvez avoir plusieurs blocs de serveur, et NGINX choisira entre eux en fonction des directives `listen` et `server_name`.

À l'intérieur d'un bloc de serveur, nous définissons plusieurs contextes **location** qui sont utilisés pour décider comment gérer les requêtes des clients. Chaque fois qu'une requête arrive, NGINX essaiera de faire correspondre son URI à l'une de ces définitions de location et la traitera en conséquence.

Il existe de nombreuses directives importantes qui peuvent être utilisées sous le contexte de location, telles que :

* **try_files** essaiera de servir un fichier statique trouvé sous le dossier qui pointe vers la directive root.
* **proxy_pass** enverra la requête à un serveur proxy spécifié.
* **rewrite** réécrira l'URI entrant en fonction d'une expression régulière afin qu'un autre bloc de location puisse le traiter.

Le contexte **upstream** définit un groupe de serveurs vers lesquels NGINX proxyfiera les requêtes. Après avoir créé un bloc upstream et défini un serveur à l'intérieur, nous pouvons ensuite le référencer par son nom à l'intérieur de nos blocs de location. De plus, un contexte upstream peut avoir de nombreux serveurs assignés sous lui afin que NGINX effectue un certain équilibrage de charge lors du proxy des requêtes.

#### Démarrer NGINX

Après avoir terminé la configuration et avoir déplacé notre application web vers le dossier approprié, nous pouvons démarrer NGINX en utilisant la commande ci-dessous :

```
sudo service nginx start
```

Après cela, chaque fois que nous changeons quelque chose dans notre configuration, nous n'avons qu'à la recharger (sans temps d'arrêt) en utilisant la commande ci-dessous.

```
service nginx reload
```

Enfin, nous pouvons vérifier l'état de NGINX en utilisant la commande ci-dessous.

```
service nginx status
```

#### Conclusion

Avec tant de fonctionnalités disponibles dès la sortie de la boîte, NGINX peut être un excellent moyen de servir votre application ou même d'être utilisé comme un proxy HTTP ou un équilibreur de charge pour vos autres serveurs web. Comprendre le fonctionnement de NGINX et la manière dont il gère les requêtes donnera beaucoup de puissance pour mettre à l'échelle et équilibrer la charge de vos applications.