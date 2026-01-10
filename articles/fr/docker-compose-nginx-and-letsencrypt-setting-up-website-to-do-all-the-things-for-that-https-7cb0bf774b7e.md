---
title: Comment configurer votre site web pour un délicieux HTTPS avec Docker, Nginx
  et letsencrypt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T18:48:35.000Z'
originalURL: https://freecodecamp.org/news/docker-compose-nginx-and-letsencrypt-setting-up-website-to-do-all-the-things-for-that-https-7cb0bf774b7e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*m-xEibEV8ttbhv7W.png
tags:
- name: Docker
  slug: docker
- name: nginx
  slug: nginx
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment configurer votre site web pour un délicieux HTTPS avec Docker,
  Nginx et letsencrypt
seo_desc: 'By Russell Hammett Jr. (Kritner)

  I’ve used letsencrypt in the past for free certs. I have not successfully utilized
  it since moving over to docker/kestrel/nginx. That all changed today, and I had
  a hell of a time figuring out what I was doing to get ...'
---

Par Russell Hammett Jr. (Kritner)

J'ai utilisé [letsencrypt](https://letsencrypt.org/) par le passé pour des certificats gratuits. Je n'avais pas réussi à l'utiliser depuis que j'ai migré vers docker/kestrel/nginx. Tout cela a changé aujourd'hui, et j'ai eu un mal fou à comprendre ce que je faisais pour le faire fonctionner.

Tout ce monde Unix, docker, nginx, est assez nouveau (pour moi), donc peut-être que c'était juste quelque chose de simple que je manquais depuis le début. Néanmoins, j'espère que cela aidera quelqu'un d'autre, ou moi-même dans plusieurs mois si je décide de le refaire.

#### Configuration initiale

J'ai un site web [.net core](https://www.microsoft.com/net/download), hébergé via [kestrel](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-2.1), fonctionnant sur [docker](https://www.docker.com/), avec un proxy inverse via [nginx](https://www.nginx.com/). Jusqu'à présent, ce proxy inverse de nginx ne fonctionnait que sur http/port 80. Je ne connais pas grand-chose aux proxys inverses. D'après ce que j'ai compris, ils peuvent recevoir des requêtes et les transmettre à un emplacement spécifique au nom du demandeur. Dans mon cas, le conteneur nginx reçoit des requêtes http, et nginx transmet cette requête à mon site .net core hébergé par kestrel. Est-ce correct ? J'espère !

Comme mentionné précédemment, nginx ne fonctionnait qu'avec le trafic http. J'avais beaucoup de mal à le faire fonctionner avec https, la configuration initiale est la suivante :

docker-compose :

```
version: '3.6'services:    kritner-website-web:    image: ${DOCKER_REGISTRY}/kritnerwebsite    expose:      - "5000"    networks:      - frontend    restart: always    container_name: kritnerwebsite_web  kritner-website-nginx:    image: nginx:latest    ports:      - "80:80"    volumes:      - ../src/nginx/nginx.conf:/etc/nginx/nginx.conf    depends_on:      - kritner-website-web    networks:      - frontend    restart: always    container_name: kritnerwebsite_nginx
```

```
networks:  frontend:
```

Dans le fichier docker-compose, j'utilise deux conteneurs séparés — le site web, qui expose le port 5000 (sur le réseau docker, pas publiquement), et nginx qui fonctionne sur le port 80.

nginx.conf

```
worker_processes 4; events { worker_connections 1024; } http {    sendfile on;     upstream app_servers {        server kritner-website-web:5000;    }     server {        listen 80;         location / {            proxy_pass         http://app_servers;            proxy_redirect     off;            proxy_set_header   Host $host;            proxy_set_header   X-Real-IP $remote_addr;            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;            proxy_set_header   X-Forwarded-Host $server_name;        }    }}
```

Dans le fichier de configuration, nous configurons un serveur upstream avec le même nom que celui que nous utilisons pour notre service de conteneur dans le fichier docker-compose `kritner-website-web:5000`.

Notez que tout ce qui précède peut être trouvé à ce [point de commit](https://github.com/Kritner/KritnerWebsite/tree/0e86849c97bdcabf68d0df7ed7eb7e5eebdccd4f) dans le dépôt de mon site web.

#### Entrée en scène de HTTPS

Letsencrypt est une autorité de certification qui offre des certificats gratuits pour aider à sécuriser votre site web. Pourquoi HTTPS via TLS est-il important ? Eh bien, il y a beaucoup à dire à ce sujet et sur son fonctionnement. L'idée de base est que le trafic de l'utilisateur est chiffré à chaque extrémité avant d'être envoyé à l'autre extrémité. Cela signifie que si vous êtes sur un wifi public et sur https, quelqu'un qui "écouterait le fil" pour ainsi dire, verrait que le trafic se produit, mais pas le contenu dudit trafic. Puisque les deux extrémités chiffrent/déchiffrent ledit trafic avec la même clé de chiffrement.

Si vous étiez sur un site http, ce trafic serait envoyé et reçu en texte clair. Ce qui signifie que vos données sont en danger d'être espionnées ! Peut-être que j'écrirai un peu plus sur le chiffrement à un moment donné. (*note à moi-même*) Surtout puisque c'est quelque chose que je fais dans mon travail de jour !

Letsencrypt est un service que j'ai utilisé auparavant. Il existe diverses implémentations pour essayer de le rendre aussi facile à utiliser que possible. Lors de mes recherches pour ce post, je suis tombé sur [ceci](https://letsencrypt.org/docs/client-options/).

Bien que je n'aie pas trouvé cette page avant maintenant, elle aurait été utile avant de commencer mon aventure. Je voulais utiliser letsencrypt avec mon site web en conteneur docker et nginx, avec le moins de maintenance possible. Les certificats letsencrypt ne sont valables que 90 jours.

Lors de mes recherches, je suis tombé sur une image docker [linuxserver/letsencrypt](https://hub.docker.com/r/linuxserver/letsencrypt/) qui promet d'utiliser nginx, la génération de certificats letsencrypt, ET le renouvellement automatique. Cela semble génial ! Bien que la documentation de l'image semble globalement adéquate — pour quelqu'un bien versé dans tout ce processus. Je l'ai trouvée insuffisante. Le processus de configuration complet m'a pris un certain temps à comprendre. D'où ce post, pour aider la prochaine personne, ou moi-même dans le futur !

![Image](https://cdn-media-1.freecodecamp.org/images/uDVdXYEOt66dbf284uuJT0gybayII2EW3lTF)
_Logo Linux Server.IO_

#### Difficultés

Les choses avec lesquelles j'ai le plus lutté pour faire fonctionner cette image linuxserver/letsencrypt étaient :

* Comment les volumes docker "fonctionnent" et leur relation avec ce conteneur
* Comment configurer les volumes pour utiliser ma configuration (lié au point précédent) — J'avais initialement beaucoup de mal à comprendre pourquoi mes paramètres modifiés sur le conteneur étaient rétablis lors du rechargement dudit conteneur (parce que c'est ce qu'ils sont censés faire)
* Comment configurer la bonne configuration nginx — où la mettre, et quoi y mettre.

#### Volumes Docker

Volumes Docker ([doc](https://docs.docker.com/storage/volumes/)) :

> Les volumes sont le mécanisme préféré pour persister les données générées par et utilisées par les conteneurs Docker. Alors que les [bind mounts](https://docs.docker.com/storage/bind-mounts/) dépendent de la structure de répertoires de la machine hôte, les volumes sont entièrement gérés par Docker. Les volumes ont plusieurs avantages par rapport aux bind mounts

Letsencrypt a beaucoup de configuration à aller avec. Il m'a fallu un certain temps pour réaliser, mais j'avais besoin d'un volume qui mappait un répertoire sur l'**hôte docker** à un répertoire spécifique sur l'image letsencrypt. J'ai finalement accompli cela dans le fichier compose comme suit :

```
volumes:      - ${DOCKER_KRITNER_NGINX}:/config       - ./nginx.conf:/config/nginx/site-confs/default
```

Le premier élément du tableau (`${DOCKER_KRITNER_NGINX}:/config`) prend une nouvelle variable d'environnement qui mappe le répertoire de l'hôte (définie dans la variable) à `/config` dans le conteneur docker lui-même. Cela signifie que l'**hôte docker** (au chemin de la variable d'environnement) contiendra la même configuration que le **conteneur docker** à la deuxième partie du mappage de volume (`/config`)

Le deuxième élément (`./nginx.conf:/config/nginx/site-confs/default`) mappe mon fichier nginx.conf local du dépôt (le fichier où je configure le proxy inverse) pour remplacer le fichier `/config/nginx/site-confs/default` sur l'hôte docker et le conteneur.

La liste complète des fichiers que j'ai finalement dû modifier pour ma situation particulière était :

* `/config/dns-conf/dnsimple.ini`
* `/config/nginx/site-confs/default`

La configuration `dnsimple.ini` consistait à ajouter ma clé API, et le fichier `/default` contient la configuration nginx.

La configuration finale `default` que j'ai obtenue est :

```
upstream app_servers {        server kritnerwebsite:5000;}
```

```
## Version 2018/09/12 - Changelog: https://github.com/linuxserver/docker-letsencrypt/commits/master/root/defaults/default
```

```
# listening on port 80 disabled by default, remove the "#" signs to enable# redirect all traffic to httpsserver { listen 80; server_name kritnerwebsite; return 301 https://$host$request_uri;}
```

```
# main server blockserver { listen 443 ssl;
```

```
# enable subfolder method reverse proxy confs include /config/nginx/proxy-confs/*.subfolder.conf;
```

```
# all ssl related config moved to ssl.conf include /config/nginx/ssl.conf;  # enable for ldap auth #include /config/nginx/ldap.conf;
```

```
client_max_body_size 0;
```

```
location / {            proxy_pass         http://app_servers;            proxy_redirect     off;            proxy_set_header   Host $host;            proxy_set_header   X-Real-IP $remote_addr;            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;            proxy_set_header   X-Forwarded-Host $server_name;    }
```

```
}
```

```
# enable subdomain method reverse proxy confsinclude /config/nginx/proxy-confs/*.subdomain.conf;# enable proxy cache for authproxy_cache_path cache/ keys_zone=auth_cache:10m;
```

Il y a quelques changements par rapport à la configuration par défaut, que je vais essayer de mettre en évidence ensuite.

```
upstream app_servers {        server kritnerwebsite:5000;}
```

C'est assez cool, puisque docker a son propre DNS interne (je suppose ?). Vous pouvez configurer un serveur upstream par le nom du conteneur, dans mon cas "kritnerwebsite". (Note : Je l'ai changé par rapport à plus tôt dans le post, qui était "kritner-website-web".)

```
# listening on port 80 disabled by default, remove the "#" signs to enable# redirect all traffic to httpsserver { listen 80; server_name kritnerwebsite; return 301 https://$host$request_uri;}
```

J'ai décommenté cette section par défaut, appliqué mon server_name de "kritnerwebsite"

```
# main server blockserver { listen 443 ssl;
```

```
# enable subfolder method reverse proxy confs include /config/nginx/proxy-confs/*.subfolder.conf;
```

```
# all ssl related config moved to ssl.conf include /config/nginx/ssl.conf;  # enable for ldap auth #include /config/nginx/ldap.conf;
```

```
client_max_body_size 0;
```

```
location / {            proxy_pass         http://app_servers;            proxy_redirect     off;            proxy_set_header   Host $host;            proxy_set_header   X-Real-IP $remote_addr;            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;            proxy_set_header   X-Forwarded-Host $server_name;    }
```

```
}
```

Dans ce qui précède, c'est principalement du "défaut" sauf pour "location" et tout ce qui se trouve dans cet objet. Ici, nous configurons le proxy inverse pour transmettre les requêtes à "/" (n'importe quoi) à notre `http://app_servers` (kritnerwebsite selon notre upstream).

#### docker-compose.yml

Notre fichier docker-compose n'a pas changé *énormément* par rapport à l'initial. Il y a eu quelques changements notables, que je vais également décrire :

```
version: '3.6'services:    nginx:    image: linuxserver/letsencrypt    ports:      - "80:80"      - "443:443"    volumes:      - ${DOCKER_KRITNER_NGINX}:/config       - ./nginx.conf:/config/nginx/site-confs/default    depends_on:      - kritnerwebsite    networks:      - frontend    container_name: nginx    environment:      - PUID=1001 # obtenir sur dockerhost via la commande "id <user>"      - PGID=1001      - EMAIL=kritner@gmail.com      - URL=kritner.com      - SUBDOMAINS=www      - TZ=America/NewYork      - VALIDATION=dns # utilisant la validation dns      - DNSPLUGIN=dnsimple # via dnsimple, notez qu'il y a une configuration supplémentaire requise séparée de ce fichier      # - STAGING=true # cela devrait être décommenté lors des tests pour le succès initial, pour éviter certaines limitations de taux
```

```
kritnerwebsite:    image: ${DOCKER_REGISTRY}/kritnerwebsite    networks:      - frontend    expose:      - "5000"    restart: always    container_name: kritnerwebsite  networks:  frontend:
```

pour les nouvelles parties :

```
nginx:    image: linuxserver/letsencrypt
```

Utilisation d'une image différente — linuxserver/letsencrypt au lieu de nginx. Cette image inclut nginx, mais aussi certbot, ainsi qu'un cronjob pour exécuter certbot au démarrage de l'application.

```
ports:      - "80:80"      - "443:443"
```

Maintenant, nous utilisons les ports http et https (bien que notez, nous redirigeons les appels http vers https via la configuration nginx).

```
volumes:      - ${DOCKER_KRITNER_NGINX}:/config       - ./nginx.conf:/config/nginx/site-confs/default
```

Déjà discuté plus tôt dans le post, nous utilisons ces volumes pour configurer correctement la configuration nginx, avec notre clé API dnsimple, ainsi que notre proxy inverse vers kritnerwebsite.

```
environment:      - PUID=1001 # obtenir sur dockerhost via la commande "id <user>"      - PGID=1001      - EMAIL=kritner@gmail.com      - URL=kritner.com      - SUBDOMAINS=www      - TZ=America/NewYork      - VALIDATION=dns # utilisant la validation dns      - DNSPLUGIN=dnsimple # via dnsimple, notez qu'il y a une configuration supplémentaire requise séparée de ce fichier      # - STAGING=true # cela devrait être décommenté lors des tests pour le succès initial, pour éviter certaines limitations de taux
```

Les variables d'environnement nécessaires selon la documentation letsencrypt peuvent être trouvées [ici](https://hub.docker.com/r/linuxserver/letsencrypt/).

* PUID/PGID — obtenir sur dockerhost via la commande "id <user>"
* Email — eh bien, votre email (utilisé pour les emails d'expiration de certificat apparemment)
* URL — l'URL du domaine principal
* subdomains — tous les sous-domaines de l'URL à certifier
* TZ — fuseau horaire
* Validation — le type de validation à faire — J'utilise DNSimple, donc j'avais besoin de DNS dans ce champ. Autres options sont html, tls-sni
* dnsplugin — dnsimple — autres options sont `cloudflare`, `cloudxns`, `digitalocean`, `dnsmadeeasy`, `google`, `luadns`, `nsone`, `rfc2136` et `route53` selon la documentation letsencrypt
* Staging=true — Je l'ai utilisé pour tester toutes mes diverses tentatives avant de le faire fonctionner. letsencrypt a une limitation de taux lorsqu'il n'est pas en mode staging (ou du moins en staging il est plus difficile d'atteindre cette limite).

Tous les changements ci-dessus, les expérimentations, les échecs, et enfin la réussite peuvent être trouvés dans [cette pull request](https://github.com/Kritner/KritnerWebsite/pull/24/commits).

Le résultat final ?

![Image](https://cdn-media-1.freecodecamp.org/images/8p9oqF7gDeWHXY9oqutUsEB5rmbmH8zh9D8s)
_Awww yeah_

et de [https://www.ssllabs.com/](https://www.ssllabs.com/) —

![Image](https://cdn-media-1.freecodecamp.org/images/YcQFIv8RixHyyhSlurfdIZVZmbttLUOQi5V0)

Pas un "A+", mais vraiment pas mal pour utiliser une seule image docker pré-construite pour mes besoins HTTPS !

Articles connexes :

* [Passer d'un "A" à un "A+" sur ssllabs.com](https://medium.com/@kritner/going-from-an-a-to-an-a-on-ssllabs-com-570d2e245100)