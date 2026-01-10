---
title: Comment configurer un reverse proxy facile et sécurisé avec Docker, Nginx et
  Letsencrypt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T04:50:41.000Z'
originalURL: https://freecodecamp.org/news/docker-nginx-letsencrypt-easy-secure-reverse-proxy-40165ba3aee2
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/john-salvino-bqGBbLq_yfc-unsplash.jpg
tags:
- name: Docker
  slug: docker
- name: nginx
  slug: nginx
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment configurer un reverse proxy facile et sécurisé avec Docker, Nginx
  et Letsencrypt
seo_desc: 'By Kasper Siig

  Introduction

  Ever tried setting up some sort of server at home? Where you have to open a new
  port for every service? And have to remember what port goes to which service, and
  what your home ip is? This is definitely something that work...'
---

Par Kasper Siig

## Introduction

Avez-vous déjà essayé de configurer un type de serveur à la maison ? Où vous devez ouvrir un nouveau port pour chaque service ? Et vous devez vous souvenir de quel port correspond à quel service, et quelle est votre adresse IP à la maison ? C'est définitivement quelque chose qui fonctionne, et les gens le font depuis longtemps.

Cependant, ne serait-il pas agréable de taper _plex.example.com_, et d'avoir un accès instantané à votre serveur multimédia ? C'est exactement ce qu'un reverse proxy fera pour vous, et en le combinant avec Docker, c'est plus facile que jamais.

## Prérequis

### Docker & Docker-Compose

Vous devez avoir Docker version 17.12.0+, et Compose version 1.21.0+.

### Domaine

Vous devez avoir un domaine configuré, et avoir un certificat SSL associé. Si vous n'en avez pas, alors [suivez mon guide ici](https://medium.com/devopslinks/docker-letsencrypt-dns-validation-75ba8c08a0d) pour obtenir un certificat gratuit avec LetsEncrypt.

## Ce que cet article couvrira

Je suis un fervent croyant en la compréhension de ce que vous faites. Il fut un temps où je suivais des guides, et je n'avais aucune idée de comment dépanner les échecs. Si c'est ainsi que vous voulez procéder, [voici un excellent tutoriel](https://medium.freecodecamp.org/docker-compose-nginx-and-letsencrypt-setting-up-website-to-do-all-the-things-for-that-https-7cb0bf774b7e), qui couvre comment le configurer. Bien que mes articles soient longs, vous devriez finir par comprendre comment tout cela fonctionne.

Ce que vous apprendrez ici, c'est ce qu'est un reverse proxy, comment le configurer, et comment vous pouvez le sécuriser. Je fais de mon mieux pour diviser le sujet en sections, divisées par des en-têtes, alors n'hésitez pas à sauter une section, si vous en avez envie. Je recommande de lire l'article entier une fois avant de commencer à le configurer.

## Qu'est-ce qu'un Reverse Proxy ?

### Proxy Régulier

Commençons par le concept d'un proxy régulier. Bien que ce soit un terme très répandu dans la communauté technologique, ce n'est pas le seul endroit où il est utilisé. Un proxy signifie que les informations passent par un tiers avant d'atteindre la destination.

Disons que vous ne voulez pas qu'un service connaisse votre IP, vous pouvez utiliser un proxy. Un proxy est un serveur qui a été configuré spécifiquement à cet effet. Si le serveur proxy que vous utilisez est situé, par exemple, à Amsterdam, l'IP qui sera affichée au monde extérieur est l'IP du serveur à Amsterdam. Les seuls à connaître votre IP sont ceux qui contrôlent le serveur proxy.

### Reverse Proxy

Pour le simplifier, un proxy ajoute une couche de masquage. C'est le même concept dans un reverse proxy, sauf qu'au lieu de masquer les connexions sortantes (vous accédant à un serveur web), ce sont les connexions entrantes (les gens accédant à votre serveur web) qui seront masquées. Vous fournissez simplement une URL comme _example.com_, et chaque fois que les gens accèdent à cette URL, votre reverse proxy s'occupera de l'endroit où cette requête est envoyée.

Disons que vous avez deux serveurs configurés sur votre réseau interne. Le Serveur1 est sur _192.168.1.10_, et le Serveur2 est sur _192.168.1.20._ Actuellement, votre reverse proxy envoie les requêtes provenant de _example.com_ vers le Serveur1. Un jour, vous avez des mises à jour à faire sur la page web. Au lieu de mettre le site web hors ligne pour maintenance, vous faites simplement la nouvelle configuration sur le Serveur2. Une fois terminé, vous changez simplement une seule ligne dans votre reverse proxy, et maintenant les requêtes sont envoyées au Serveur2. En supposant que le reverse proxy est configuré correctement, vous ne devriez avoir absolument aucun temps d'arrêt.

Mais peut-être le plus grand avantage d'avoir un reverse proxy, c'est que vous pouvez avoir des services fonctionnant sur une multitude de ports, mais vous n'avez à ouvrir que les ports 80 et 443, HTTP et HTTPS respectivement. Toutes les requêtes arriveront sur votre réseau sur ces deux ports, et le reverse proxy s'occupera du reste. Tout cela aura du sens une fois que nous commencerons à configurer le proxy.

## Configuration du Conteneur

### Ce qu'il faut faire

`docker-compose.yaml` :

```yaml
version: '3'

services:
  reverse:
    container_name: reverse
    hostname: reverse
    image: nginx
    ports:
      - 80:80
      - 443:443
    volumes:
      - <path/to/your/config>:/etc/nginx
      - <path/to/your/certs>:/etc/ssl/private
```

Tout d'abord, vous devez ajouter un nouveau service à votre fichier docker-compose. Vous pouvez l'appeler comme vous le souhaitez, dans ce cas, j'ai choisi _reverse_. Ici, j'ai simplement choisi _nginx_ comme image, cependant, dans un environnement de production, il est généralement bon de spécifier une version au cas où il y aurait des changements majeurs dans les futures mises à jour.

Ensuite, vous devez lier deux dossiers en volume. _/etc/nginx_ est l'endroit où tous vos fichiers de configuration sont stockés, et _/etc/ssl/private_ est l'endroit où vos certificats SSL sont stockés. Il est TRÈS important que votre dossier de configuration n'existe PAS sur votre hôte la première fois que vous démarrez le conteneur. Lorsque vous démarrez votre conteneur via docker-compose, il créera automatiquement le dossier et le remplira avec le contenu du conteneur. Si vous avez créé un dossier de configuration vide sur votre hôte, il le montera, et le dossier à l'intérieur du conteneur sera vide.

### Pourquoi cela fonctionne

Il n'y a pas grand-chose à cette partie. C'est surtout comme démarrer n'importe quel autre conteneur avec docker-compose. Ce que vous devez remarquer ici, c'est que vous liez les ports 80 et 443. C'est ici que toutes les requêtes arriveront, et elles seront transférées vers le service que vous spécifierez.

## Configuration de Nginx

### Ce qu'il faut faire

Maintenant, vous devriez avoir un dossier de configuration sur votre hôte. En changeant pour ce répertoire, vous devriez voir un tas de fichiers différents et un dossier appelé `conf.d`. C'est à l'intérieur de `conf.d` que tous vos fichiers de configuration seront placés. Pour l'instant, il y a un seul fichier `default.conf`, vous pouvez aller de l'avant et le supprimer.

Toujours à l'intérieur de `conf.d`, créez deux dossiers : `sites-available` et `sites-enabled`. Naviguez dans `sites-available` et créez votre premier fichier de configuration. Ici, nous allons configurer une entrée pour [Plex](https://plex.tv), mais n'hésitez pas à utiliser un autre service que vous avez configuré si vous le souhaitez. Cela n'a pas vraiment d'importance comment le fichier est appelé, cependant je préfère le nommer comme `plex.conf`.

Maintenant, ouvrez le fichier et entrez ce qui suit :

```
upstream plex {
  server        plex:32400;
}

server {
  listen        80;
  server_name   plex.example.com;

  location / {
    proxy_pass  http://plex;
  }
}
```

Allez dans le répertoire `sites-enabled`, et entrez la commande suivante :

```
ln -s ../sites-available/plex.conf .
```

Cela créera un lien symbolique vers le fichier dans l'autre dossier. Maintenant, il n'y a plus qu'une seule chose à faire, et c'est de changer le fichier `nginx.conf` dans le dossier de configuration. Si vous ouvrez le fichier, vous devriez voir ce qui suit comme dernière ligne :

```
include /etc/nginx/conf.d/*.conf;
```

Changez cela en :

```
include /etc/nginx/conf.d/sites-enabled/*.conf;
```

Pour que le reverse proxy fonctionne réellement, nous devons recharger le service nginx à l'intérieur du conteneur. Depuis l'hôte, exécutez `docker exec <container-name> nginx -t`. Cela exécutera un vérificateur de syntaxe contre vos fichiers de configuration. Cela devrait indiquer que la syntaxe est correcte. Maintenant, exécutez `docker exec <container-name> nginx -s reload`. Cela enverra un signal au processus nginx pour qu'il se recharge, et félicitations ! Vous avez maintenant un reverse proxy en cours d'exécution, et vous devriez pouvoir accéder à votre serveur à l'adresse _plex.example.com_ (en supposant que vous avez redirigé le port 80 vers votre hôte dans votre routeur).

Même si votre reverse proxy fonctionne, vous utilisez HTTP, qui ne fournit aucune encryption. La prochaine partie sera comment sécuriser votre proxy, et obtenir un score parfait sur [SSL Labs](https://www.ssllabs.com/ssltest/analyze.html).

### Pourquoi cela fonctionne

**Le fichier de configuration**

Comme vous pouvez le voir, le fichier `plex.conf` se compose de deux parties. Une partie `upstream` et une partie `server`. Commençons par la partie `server`. C'est ici que vous définissez le port recevant les requêtes entrantes, quel domaine cette configuration doit correspondre, et où elle doit être envoyée.

La façon dont ce serveur est configuré, vous devez créer un fichier pour chaque service auquel vous souhaitez proxyfier les requêtes, donc évidemment vous avez besoin d'un moyen de distinguer quel fichier doit recevoir chaque requête. C'est ce que fait la directive `server-name`. En dessous, nous avons la directive `location`.

Dans notre cas, nous n'avons besoin que d'un seul `location`, cependant vous pouvez avoir autant de directives `location` que vous le souhaitez. Imaginez que vous avez un site web avec un frontend et un backend. Selon l'infrastructure que vous utilisez, vous aurez le frontend comme un conteneur et le backend comme un autre conteneur. Vous pourriez alors avoir `location / {}` qui enverra les requêtes au frontend, et `location /api/ {}` qui enverra les requêtes au backend. Soudain, vous avez plusieurs services fonctionnant sur un seul domaine mémorable.

En ce qui concerne la partie `upstream`, elle peut être utilisée pour l'équilibrage de charge. Si vous êtes intéressé à en apprendre davantage sur son fonctionnement, vous pouvez consulter [la documentation officielle ici](http://nginx.org/en/docs/http/ngx_http_upstream_module.html). Pour notre cas simple, vous définissez simplement le nom d'hôte ou l'adresse IP du service auquel vous souhaitez proxyfier, et le port auquel il doit être proxyfié, puis vous faites référence au nom upstream dans la directive `location`.

**Nom d'hôte vs. Adresse IP**

Pour comprendre ce qu'est un nom d'hôte, prenons un exemple. Supposons que vous êtes sur votre réseau domestique _192.168.1.0._ Vous configurez ensuite un serveur sur _192.168.1.10_ et exécutez Plex dessus. Vous pouvez maintenant accéder à Plex sur _192.168.1.10:32400_, tant que vous êtes toujours sur le même réseau. Une autre possibilité est de donner un nom d'hôte au serveur. Dans ce cas, nous lui donnerons le nom d'hôte _plex_. Vous pouvez maintenant accéder à Plex en entrant _plex:32400_ dans votre navigateur !

Ce même concept a été introduit dans docker-compose dans la version 3. Si vous regardez le fichier docker-compose plus tôt dans cet article, vous remarquerez que je lui ai donné une directive `hostname: reverse`. Maintenant, tous les autres conteneurs peuvent accéder à mon reverse proxy par son nom d'hôte. Une chose très importante à noter est que le nom du service doit être le même que le nom d'hôte. C'est quelque chose que les créateurs de docker-compose ont choisi d'imposer.

Une autre chose vraiment importante à retenir est que, par défaut, les conteneurs Docker sont placés sur leur propre réseau. Cela signifie que vous ne pourrez pas accéder à votre conteneur par son nom d'hôte si vous êtes assis sur votre ordinateur portable sur votre réseau hôte. Seuls les conteneurs peuvent accéder les uns aux autres via leur nom d'hôte.

Donc, pour résumer et rendre cela très clair. Dans votre fichier docker-compose, ajoutez la directive `hostname` à vos services. La plupart du temps, vos conteneurs obtiendront une nouvelle IP chaque fois que vous redémarrez le conteneur, donc en y faisant référence via le nom d'hôte, cela signifie qu'il n'a pas d'importance quelle IP votre conteneur obtient.

**Sites-available & Sites-enabled**

Pourquoi créons-nous les répertoires `sites-available` et `sites-enabled` ? Ce n'est pas quelque chose de ma création. Si vous installez Nginx sur un serveur, vous verrez qu'il vient avec ces dossiers. Cependant, comme Docker est construit avec les microservices à l'esprit, où un conteneur ne doit faire qu'une seule chose, ces dossiers sont omis dans le conteneur. Nous les recréons à nouveau, en raison de la manière dont nous utilisons le conteneur.

Et oui, vous pourriez définitivement simplement créer un dossier `sites-enabled`, ou héberger directement vos fichiers de configuration dans `conf.d`. En faisant cela, vous pouvez avoir des configurations passives. Supposons que vous faites de la maintenance et que vous ne voulez pas que le service soit actif ; vous supprimez simplement le lien symbolique et le remettez en place lorsque vous voulez que le service soit actif à nouveau.

**Liens symboliques**

Les liens symboliques sont une fonctionnalité très puissante du système d'exploitation. Personnellement, je ne les avais jamais utilisés avant de configurer un serveur Nginx, mais depuis, je les utilise partout où je peux. Supposons que vous travaillez sur 5 projets différents, mais que tous ces projets utilisent le même fichier d'une manière ou d'une autre. Vous pouvez soit copier le fichier dans chaque projet et y faire référence directement, soit placer le fichier à un seul endroit, et dans ces 5 projets, créer des liens symboliques vers ce fichier.

Cela présente deux avantages : vous occupez 4 fois moins d'espace que vous ne l'auriez fait autrement, et surtout, vous modifiez le fichier à un seul endroit, et il est modifié dans les 5 projets à la fois ! C'était un peu une digression, mais je pense que cela vaut la peine d'être mentionné.

## Sécurisation du Proxy Nginx

### Ce qu'il faut faire

Allez dans votre dossier de configuration et créez 3 fichiers, puis remplissez-les avec les entrées suivantes :

`common.conf` :

```
add_header Strict-Transport-Security    "max-age=31536000; includeSubDomains" always;
add_header X-Frame-Options              SAMEORIGIN;
add_header X-Content-Type-Options       nosniff;
add_header X-XSS-Protection             "1; mode=block";
```

`common_location.conf` :

```
proxy_set_header    X-Real-IP           $remote_addr;
proxy_set_header    X-Forwarded-For     $proxy_add_x_forwarded_for;
proxy_set_header    X-Forwarded-Proto   $scheme;
proxy_set_header    Host                $host;
proxy_set_header    X-Forwarded-Host    $host;
proxy_set_header    X-Forwarded-Port    $server_port;
```

`ssl.conf` :

```
ssl_protocols               TLSv1 TLSv1.1 TLSv1.2;
ssl_ecdh_curve              secp384r1;
ssl_ciphers                 "ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384 OLD_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 OLD_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256";
ssl_prefer_server_ciphers   on;
ssl_dhparam                 /etc/nginx/dhparams.pem;
ssl_certificate             /etc/ssl/private/fullchain.pem;
ssl_certificate_key         /etc/ssl/private/privkey.pem;
ssl_session_timeout         10m;
ssl_session_cache           shared:SSL:10m;
ssl_session_tickets         off;
ssl_stapling                on;
ssl_stapling_verify         on;
```

Maintenant, ouvrez le fichier `plex.conf` et modifiez-le comme suit (remarquez les lignes 6, 9, 10 et 14) :

```
upstream plex {
  server        plex:32400;
}

server {
  listen        443 ssl;
  server_name   plex.example.com;

  include       common.conf;
  include       /etc/nginx/ssl.conf;

  location / {
    proxy_pass  http://plex;
    include     common_location.conf;
  }
}
```

Retournez à la racine de votre dossier de configuration et exécutez la commande suivante :

```
openssl dhparam -out dhparams.pem 4096
```

Cela prendra beaucoup de temps à se terminer, même jusqu'à une heure dans certains cas.

Si vous avez suivi mon article sur l'obtention d'un certificat SSL LetsEncrypt, vos certificats devraient être situés dans `</path/to/your/letsencrypt/config>/etc/letsencrypt/live/<domain>/`.

Lorsque j'ai aidé un ami à configurer cela sur son système, nous avons rencontré des problèmes où il ne pouvait pas ouvrir les fichiers lorsqu'ils étaient situés dans ce répertoire. Très probablement à cause de problèmes de permissions. La solution facile à cela est de créer un répertoire SSL, comme `</path/to/your/nginx/config>/certs`, puis de le monter dans le dossier `/etc/ssl/private` du conteneur Nginx. Dans le dossier nouvellement créé, vous devez ensuite créer des liens symboliques vers les certificats dans le dossier de configuration de votre LetsEncrypt.

Lorsque la commande `openssl` a terminé son exécution, vous devez exécuter `docker exec <container-name> nginx -t` pour vous assurer que toute la syntaxe est correcte, puis la recharger en exécutant `docker exec <container-name> nginx -s reload`. À ce stade, tout devrait fonctionner, et vous avez maintenant un reverse proxy fonctionnel et parfaitement sécurisé !

### Pourquoi cela fonctionne

En regardant dans le fichier `plex.conf`, il n'y a qu'un seul changement majeur, et c'est le port sur lequel le reverse proxy écoute, et lui dire qu'il s'agit d'une connexion ssl. Ensuite, il y a 3 endroits où nous incluons les 3 autres fichiers que nous avons créés. Bien que SSL soit assez sécurisé en soi, ces autres fichiers le rendent encore plus sécurisé. Cependant, si pour une raison quelconque vous ne souhaitez pas inclure ces fichiers, vous devez déplacer `ssl-certificate` et `ssl-certificate-key` à l'intérieur du fichier `.conf`. Ceux-ci sont nécessaires pour avoir une connexion HTTPS fonctionnelle.

**Common.conf**

En regardant dans le fichier `common.conf`, nous ajoutons 4 en-têtes différents. Les en-têtes sont quelque chose que le serveur envoie au navigateur à chaque réponse. Ces en-têtes indiquent au navigateur d'agir d'une certaine manière, et c'est ensuite au navigateur de faire respecter ces en-têtes.

[**Strict-Transport-Security (HSTS)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)

Cet en-tête indique au navigateur que les connexions doivent être établies via HTTPS. Une fois cet en-tête ajouté, le navigateur ne vous permettra pas d'établir une connexion HTTP simple avec le serveur, garantissant que toute communication est sécurisée.

[**X-Frame-Options**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)

En spécifiant cet en-tête, vous spécifiez si d'autres sites peuvent intégrer votre contenu dans leurs sites. Cela peut aider à éviter les attaques de [clickjacking](https://en.wikipedia.org/wiki/Clickjacking).

[**X-Content-Type-Options**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options)

Disons que vous avez un site où les utilisateurs peuvent télécharger des fichiers. Il n'y a pas assez de validation sur les fichiers, donc un utilisateur télécharge avec succès un fichier `php` sur le serveur, où le serveur s'attend à ce qu'une image soit téléchargée. L'attaquant peut alors être en mesure d'accéder au fichier téléchargé. Maintenant, le serveur répond avec une image, cependant le type MIME du fichier est `text/plain`. Le navigateur "reniflera" le fichier, puis rendra le script php, permettant à l'attaquant de faire une exécution de code à distance (RCE).

Avec cet en-tête défini sur "nosniff", le navigateur ne regardera pas le fichier et le rendra simplement comme ce que le serveur indique au navigateur.

[**X-XSS-Protection**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection)

Bien que cet en-tête était plus nécessaire dans les anciens navigateurs, il est si facile à ajouter que vous pourriez aussi bien le faire. Certaines attaques XSS (Cross-site Scripting) peuvent être très intelligentes, tandis que d'autres sont très rudimentaires. Cet en-tête indiquera aux navigateurs de scanner les vulnérabilités simples et de les bloquer.

**Common_location.conf**

**X-Real-IP**

Parce que vos serveurs sont derrière un reverse proxy, si vous essayez de regarder l'IP de la requête, vous verrez toujours l'IP du reverse proxy. Cet en-tête est ajouté pour que vous puissiez voir quelle IP demande réellement votre service.

**X-Forwarded-For**

Parfois, la requête d'un utilisateur passera par plusieurs clients avant d'atteindre votre serveur. Cet en-tête inclut un tableau de tous ces clients.

**X-Forwarded-Proto**

Cet en-tête montrera quel protocole est utilisé entre le client et le serveur.

**Host**

Cela garantit qu'il est possible de faire une recherche DNS inverse sur le nom de domaine. Il est utilisé lorsque la directive `server_name` est différente de ce à quoi vous faites un proxy.

**X-Forwarded-Host**

Montre quel est le vrai hôte de la requête au lieu du reverse proxy.

**X-Forwarded-Port**

Aide à identifier le port sur lequel le client a demandé le serveur.

**Ssl.conf**

SSL est un sujet énorme en soi, et trop grand pour commencer à expliquer dans cet article. Il existe de nombreux excellents tutoriels sur le fonctionnement des poignées de main SSL, et ainsi de suite. Si vous souhaitez examiner ce fichier spécifique, je suggère de regarder les protocoles et les chiffrements utilisés, et la différence qu'ils font.

## Redirection HTTP vers HTTPS

Les plus observateurs ont peut-être remarqué que nous n'écoutons jamais que sur le port 443 dans cette version sécurisée. Cela signifierait que toute personne essayant d'accéder au site via _https://*_ passerait, mais essayer de se connecter via _http://*_ obtiendrait simplement une erreur. Heureusement, il y a une solution très facile à cela. Créez un fichier `redirect.conf` avec le contenu suivant :

```
server {
  listen        80;

  server_name   _;

  return 301 https://$host$request_uri;
}
```

Maintenant, assurez-vous simplement qu'il apparaît dans votre dossier `sites-enabled`, et lorsque vous avez rechargé le processus Nginx dans le conteneur, toutes les requêtes vers le port 80 seront redirigées vers le port 443 (HTTPS).

## Réflexions finales

Maintenant que votre site est opérationnel, vous pouvez vous rendre sur [SSL Labs](https://www.ssllabs.com/ssltest/analyze.html) et exécuter un test pour voir à quel point votre site est sécurisé. Au moment de la rédaction de cet article, vous devriez obtenir un score parfait. Cependant, il y a une chose importante à noter à ce sujet.

Il y aura toujours un équilibre entre la sécurité et la commodité. Dans ce cas, les poids sont fortement du côté de la sécurité. Si vous exécutez le test sur SSL Labs et que vous faites défiler vers le bas, vous verrez qu'il y a plusieurs appareils qui ne pourront pas se connecter à votre site, car ils ne supportent pas les nouvelles normes.

Gardez donc cela à l'esprit lorsque vous configurez cela. Pour l'instant, je ne fais fonctionner qu'un serveur à la maison, où je n'ai pas à me soucier du fait que beaucoup de gens puissent y accéder. Mais si vous faites une analyse sur Facebook, vous verrez qu'ils n'auront pas un score aussi bon, cependant leur site peut être accessible par plus d'appareils.