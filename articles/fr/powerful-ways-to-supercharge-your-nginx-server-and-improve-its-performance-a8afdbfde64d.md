---
title: Façons puissantes de booster votre serveur NGINX et d'améliorer ses performances
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T19:14:54.000Z'
originalURL: https://freecodecamp.org/news/powerful-ways-to-supercharge-your-nginx-server-and-improve-its-performance-a8afdbfde64d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ruRaN0YaGlKpZ13eP3dxqA.jpeg
tags:
- name: Devops
  slug: devops
- name: nginx
  slug: nginx
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Façons puissantes de booster votre serveur NGINX et d'améliorer ses performances
seo_desc: 'By HaKr

  NGINX is perhaps the most versatile web server out there, and it can beat other
  servers when configured correctly. It can also do other important things, such as
  load balancing, HTTP caching, and can be used as a reverse proxy.

  Over the years...'
---

Par HaKr

[**NGINX**](http://nginx.org) est probablement le serveur web le plus polyvalent qui existe, et il peut surpasser d'autres serveurs lorsqu'il est correctement configuré. Il peut également faire d'autres choses importantes, telles que l'équilibrage de charge, la mise en cache HTTP, et peut être utilisé comme un proxy inverse.

Au fil des ans, nous avons vu tant de configurations qui améliorent la sécurité et augmentent les performances de votre application web dans son ensemble — vous permettant de suivre les dernières tendances.

Je vais partager la configuration NGINX minimaliste que j'ai trouvée la plus optimisée et que j'utilise pour mon nouvel outil [VisaList](https://visalist.io). J'ai dû faire beaucoup de recherches pour améliorer les performances de mon site web, et j'ai pensé que ce processus pourrait aider au moins quelques autres — alors je le partage ici.

### Pourquoi ?

Avec ces changements, j'ai pu obtenir les résultats suivants pour ma nouvelle application web :

**Score de vitesse de page :** [Page Speed Insights](https://developers.google.com/speed/pagespeed/insights/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*japLOsbLszo0zdJIkRcgag.png)

**Score Lighthouse :** [Chrome Dev Tools Lighthouse](https://developers.google.com/web/tools/lighthouse/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*8P0556MeGprSMNTIFk4acQ.jpeg)

**Score du serveur :** [Qualys SSL Server Test](https://www.ssllabs.com/ssltest/index.html)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xd1NNM6nhvezzm2-7D7jEQ.png)

Vous aussi pouvez obtenir facilement ces avantages de performance. Vous **n'avez pas** besoin d'être un expert DevOps pour faire ces optimisations. Donc, toute personne nouvelle dans les applications web et utilisant NGINX trouvera cela très utile.

Si vous êtes un expert, vous pouvez laisser vos opinions dans les commentaires afin que les nouveaux développeurs comme moi puissent apprendre et construire une communauté web forte et positive autour de nous. ✨**Allez les développeurs web !**✨

Cet article suppose que vous avez un serveur Ubuntu 16.04 (Xenial) et une application WebApp rendue côté serveur avec Vue.js (ou tout autre framework JS) prête à être servie via NGINX avec le serveur API. Si vous n'avez pas installé NGINX et avez besoin d'aide pour le faire, vous pouvez consulter cet [**article**](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04).

Alors, quelles sont ces optimisations dont je parle ? Regardons le code !

### Optimisations

La bonne nouvelle est que vous n'avez à vous soucier que de deux fichiers. L'un est votre configuration NGINX globale, qui s'applique à toutes les applications web (vous pouvez avoir plusieurs applications web comme un site web, une API, un serveur statique, etc.). L'autre est spécifique à votre domaine, que nous appellerons `example.com`. Remplacez `example.com` par votre propre domaine. Ici, j'utilise uniquement le domaine nu sans `www`. Je couvrirai cela bientôt.

Ouvrez votre fichier de configuration NGINX ou spécifique au domaine en utilisant ces commandes :

```bash
sudo nano /etc/nginx/nginx.conf

sudo nano /etc/nginx/sites-available/example.com
```

#### **Compression de contenu**

**Brotli** est-il meilleur que **GZip** ? Oui et non. Lorsque le navigateur demande une page web, le serveur ne l'envoie pas directement octet par octet. Au lieu de cela, il l'envoie dans un état compressé en fonction des encodages acceptés par le navigateur. Aujourd'hui, presque tout le monde utilise Gzip, et vous pouvez vous demander pourquoi ? Parce qu'il existe depuis plus d'une décennie.

Voici Brotli, qui est le dernier algorithme d'encodage développé par Google. Brotli est ~20 % plus efficace que Gzip. Gardez simplement à l'esprit que vous devez envoyer le contenu en Gzip lorsque Brotli n'est pas supporté. Brotli fonctionne mieux avec les fichiers statiques plutôt qu'avec le contenu dynamique.

Assurez-vous également d'activer le type Brotli pour les données JSON de l'API uniquement lorsque votre bibliothèque HTTP côté client le supporte. Par exemple, la bibliothèque Axios ne supporte pas encore l'encodage Brotli.

```
http {

... 

    # Paramètres Gzip
    gzip on;
    gzip_disable "msie6";
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_buffers 32 16k;
    gzip_http_version 1.1;
    gzip_min_length 250;
    gzip_types image/jpeg image/bmp image/svg+xml text/plain text/css application/json application/javascript application/x-javascript text/xml application/xml application/xml+rss text/javascript image/x-icon;
    
    # Paramètres Brotli
    brotli on;
    brotli_comp_level 4;
    brotli_buffers 32 8k;
    brotli_min_length 100;
    brotli_static on;
    brotli_types image/jpeg image/bmp image/svg+xml text/plain text/css application/json application/javascript application/x-javascript text/xml application/xml application/xml+rss text/javascript image/x-icon;
...

}
```

Une fois que vous avez ajouté ces changements, vous pouvez vérifier que le content-encoding affiche `br` dans les en-têtes de réponse dans les outils de développement Chrome :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6bM7se1Eqgm4F63n-Q2krg.png)

#### **Améliorer la sécurité**

Par défaut, votre NGINX n'a pas tous les en-têtes de sécurité importants requis, ce qui est en fait assez simple. Ceux-ci empêchent les attaques par clickjacking, les attaques par scripts inter-sites et autres attaques par injection de code.

L'en-tête `Strict-Transport-Security` est pour **HTTP Strict Transport Security** (HSTS) qui protège également contre les attaques de [rétrogradation de protocole](https://en.wikipedia.org/wiki/Downgrade_attack).

```
http {

...
   # en-têtes de sécurité
   add_header X-Frame-Options "SAMEORIGIN" always;
   add_header X-XSS-Protection "1; mode=block" always;
   add_header X-Content-Type-Options "nosniff" always;
   add_header Referrer-Policy "no-referrer-when-downgrade" always;
   add_header Content-Security-Policy "default-src * data: 'unsafe-eval' 'unsafe-inline'" always;

   add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
...

}
```

#### **Optimiser SSL et les sessions**

SSL : Utilisez TLS et désactivez SSL (SSL est assez ancien et obsolète et présente de nombreuses vulnérabilités). Optimisez les suites de chiffrement, car elles sont au cœur de TLS. C'est là que le chiffrement se produit.

Cache de session : Créer un cache des paramètres de connexion TLS réduit le nombre de poignées de main, et peut ainsi améliorer les performances de votre application. Le cache est configuré à l'aide de la directive `ssl_session_cache`.

Tickets de session : Les tickets de session sont une alternative au cache de session. Dans le cas du cache de session, les informations sur la session sont stockées sur le serveur.

OSCP : Pour avoir une connexion sécurisée à un serveur, le client doit vérifier le certificat présenté par le serveur. Afin de vérifier que le certificat n'a pas été révoqué, le client (navigateur) contactera l'émetteur du certificat. Cela ajoute un peu plus de surcharge à l'initialisation de la connexion (et donc à notre temps de chargement de page).

Utilisez ces directives dans votre configuration NGINX et vous êtes prêt pour l'optimisation SSL.

```
http {
 
...  
   # Paramètres SSL
   ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   ssl_prefer_server_ciphers on;
   ssl_ciphers ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GC$
   
   # Optimiser le cache de session
   ssl_session_cache shared:SSL:50m;
   ssl_session_timeout 1d;
   
   # Activer les tickets de session
   ssl_session_tickets on;
   
   # OCSP Stapling
   ssl_stapling on;
   ssl_stapling_verify on;
   resolver 8.8.8.8 8.8.4.4 208.67.222.222 208.67.220.220 valid=60s;
   resolver_timeout 2s;
...

}
```

#### **Améliorer les performances : Support HTTP/2**

HTTP/2 présente de nombreux avantages par rapport à HTTP, comme permettre au navigateur de télécharger des fichiers en parallèle et permettre au serveur de pousser des ressources, entre autres. Tout ce que vous avez à faire est de remplacer `http` par `http2` dans votre bloc serveur par défaut. C'est tout, et vous obtenez beaucoup d'avantages.

```
server{

...

listen 443 http2 default_server;
    listen [::]:443 http2 default_server;
    server_name example.com;
...

}
```

Tapez cette commande `curl -I -L https://example.com` et vérifiez la réponse.

```
HTTP/2 200
server: nginx
date: Wed, 18 Jul 2018 02:13:32 GMT
content-type: text/html; charset=utf-8
content-length: 216641
vary: Accept-Encoding
....
```

#### **Réduire le scraping / les attaques**

Limiter les requêtes vers le serveur est crucial, car cela peut facilement épuiser les ressources et entraîner des factures élevées. Il est également important de se défendre contre ceux qui veulent scraper et attaquer nos serveurs. Il existe trois types de directives :

* Limitation des requêtes `**limit_req**` **:** Limiter le nombre de requêtes par IP
* Limitation des connexions `**limit_conn**` **:** Limiter le nombre de connexions par IP
* Limitation de la bande passante/débit `**limit_rate**` **:** Limiter le débit de bande passante des données envoyées

Avec la directive ci-dessous, vous pouvez être tranquille :

```
http {

...
   # Limites
   limit_req_log_level warn;
   limit_req_zone $binary_remote_addr zone=reqlimit:10m rate=10r/m;

   limit_conn_zone $binary_remote_addr zone=connlimit:100m;
   limit_conn servers 1000; # Connexions simultanées
...

}
```

```
...
server {
...
   location /api/ {
      # Limitation du débit
      limit_req zone=reqlimit burst=20; # Rafale maximale de requêtes
      limit_req_status 460; # Statut à envoyer
      
      # Limitation des connexions
      limit_conn connlimit 20; # Nombre de téléchargements par IP       
      
      # Limitation de la bande passante
      limit_rate 4096k; # Limite de vitesse (ici en kb/s)
   }
...
}
```

#### **Mise en cache côté client**

La mise en cache des fichiers statiques dans le navigateur est facile et économise beaucoup de requêtes vers le serveur. Tout ce que vous avez à faire est d'ajouter ces deux blocs de code et de spécifier l'expiration comme vous le souhaitez. Vous pouvez inclure toute autre extension de fichier statique que vous jugez digne d'être mise en cache.

```
server {

...
    location / {
       ...
       ...
    }
    ...
    ...
    location ~* \.(jpg|jpeg|png|gif|ico)$ {
       expires 30d;
    }
    location ~* \.(css|js)$ {
       expires 7d;
    }
...

}
```

#### **Microcaching**

Si vous n'en avez pas entendu parler jusqu'à présent, alors vous avez de la chance aujourd'hui ! Le **Microcaching** est une technique de mise en cache dans laquelle le contenu est mis en cache pendant une très courte période, peut-être aussi peu qu'une seconde. Cela signifie effectivement que les mises à jour du site sont retardées d'au plus une seconde, ce qui dans de nombreux cas est parfaitement acceptable. Cela est particulièrement utile pour les réponses API qui sont les mêmes pour tous les utilisateurs.

Utilisez ces directives pour définir le microcaching avec le chemin à `/tmp/cacheapi` avec un cache de 100 Mo avec une taille maximale de 1 Go de dossier de cache qui met à jour le cache en arrière-plan. En savoir plus à ce sujet [**ici**](https://www.nginx.com/blog/benefits-of-microcaching-nginx/) et [**ici**](https://www.nginx.com/blog/nginx-caching-guide/).

```
proxy_cache_path /tmp/cacheapi levels=1:2 keys_zone=microcacheapi:100m max_size=1g inactive=1d use_temp_path=off;
...

server {

...
   location /api/ {

      # Micro caching
      proxy_cache microcacheapi;
      proxy_cache_valid 200 1s;
      proxy_cache_use_stale updating;
      proxy_cache_background_update on;
      proxy_cache_lock on;
      ...
      ...
      
   }
...

}
```

```
http {

...
   add_header X-Cache-Status $upstream_cache_status;
...

}
```

#### **Certificat SSL**

**Let's Encrypt** est une autorité de certification (CA) qui fournit un moyen facile d'obtenir et d'installer des certificats TLS/SSL gratuits. Cela permet le HTTPS chiffré sur les serveurs web. Il simplifie le processus en fournissant un client logiciel, Certbot, qui tente d'automatiser la plupart (sinon toutes) des étapes requises.

Installez [Let's Encrypt](https://letsencrypt.org) :

```bash
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx
```

Créez un certificat SSL Let's Encrypt avec cette commande :

```bash
sudo certbot --nginx -d example.com -d www.example.com
```

puis ajoutez ces certificats à votre fichier de configuration de domaine comme ceci :

```
server {

    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;
...
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
...

}
```

#### **Rediriger WWW**

Google préfère que vous choisissiez un domaine avec `www` plutôt que sans. Il est préférable de choisir le domaine nu car il est plus petit et supprime le `www` redondant. Vous pouvez maintenant rediriger tous les utilisateurs `www` vers votre domaine nu en ajoutant ces directives ci-dessous.

```
server {
...
...
}
server {
    listen 80;
    listen [::]:80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}
server {
    listen 80;
    listen [::]:80;
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name www.example.com;
    return 301 https://example.com$request_uri;
}
```

#### **Module Pagespeed**

Le [Module Pagespeed](https://www.modpagespeed.com) est une pépite inconnue de beaucoup. Il s'agissait à l'origine d'un projet Google qui fait maintenant partie de l'incubateur Apache. Pagespeed peut automatiquement prendre en charge presque toutes les méthodes connues pour améliorer les performances de votre site web.

[**Installez**](https://www.digitalocean.com/community/tutorials/how-to-add-ngx_pagespeed-to-nginx-on-ubuntu-14-04) ou [mettez à niveau](https://www.digitalocean.com/community/questions/how-to-add-pagespeed-on-existent-nginx-ubuntu-server) NGINX avec Pagespeed. Ce n'est pas une tâche facile, et c'est pourquoi je l'ai gardée pour la fin. Suivez ces instructions, et vous devriez pouvoir le faire sans aucun problème. Une fois que vous avez terminé, tout ce que vous avez à faire est de l'activer et voilà !

```
server{

...  
    # Module Pagespeed
    pagespeed on;
    
    pagespeed FileCachePath /var/cache/ngx_pagespeed_cache;
    location ~ "\.pagespeed\.([a-z]\.)?[a-z]{2}\.[^.]{10}\.[^.]+" {
    add_header "" "";
    }
    location ~ "^/pagespeed_static/" { }
    location ~ "^/ngx_pagespeed_beacon$" { }
    
    pagespeed RewriteLevel PassThrough;
    pagespeed EnableCachePurge on;
    pagespeed PurgeMethod PURGE;
    
    pagespeed EnableFilters prioritize_critical_css;
...
}
```

Il existe de nombreux filtres que vous pouvez activer, mais gardez simplement à l'esprit que la plupart des frameworks modernes comme (Nuxt.js, Angular, Next.js et autres) ont certaines de ces optimisations dans leur processus de construction, donc cela peut être contre-intuitif. Choisissez les filtres dont vous avez besoin et activez uniquement ceux-ci. Ce n'est en aucun cas un ensemble exhaustif de filtres, mais cela amènera définitivement votre site à 100/100 sur pagespeed.

```
pagespeed EnableFilters rewrite_css;
pagespeed EnableFilters collapse_whitespace,remove_comments;
pagespeed EnableFilters flatten_css_imports;
pagespeed EnableFilters combine_css;
pagespeed EnableFilters combine_javascript;
pagespeed EnableFilters defer_javascript;
pagespeed EnableFilters extend_cache;
pagespeed EnableFilters pedantic;
pagespeed EnableFilters inline_google_font_css;
pagespeed FetchHttps enable;
pagespeed EnableFilters inline_css,move_css_above_scripts;
pagespeed EnableFilters inline_javascript;
pagespeed EnableFilters inline_import_to_link;
pagespeed EnableFilters lazyload_images;
pagespeed EnableFilters insert_dns_prefetch;
pagespeed EnableFilters inline_preview_images;
pagespeed EnableFilters resize_mobile_images;
pagespeed EnableFilters rewrite_images;
pagespeed EnableFilters responsive_images,resize_images;
pagespeed EnableFilters responsive_images_zoom;
pagespeed EnableFilters rewrite_javascript;
pagespeed EnableFilters rewrite_style_attributes,convert_meta_tags;
```

Vous pouvez en savoir plus sur les différents types de filtres disponibles [**ici**](https://modpagespeed.com/doc/filters)**.**

<iframe src="https://giphy.com/embed/ely3apij36BJhoZ234" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

Ainsi, la configuration finale de NGINX et la configuration de domaine ressemblent à ceci :

[https://gist.github.com/1hakr/01cb00dfce8c92a15c0d9faee9052042](https://gist.github.com/1hakr/01cb00dfce8c92a15c0d9faee9052042)

Maintenant, tout ce que vous avez à faire est de recharger votre fichier de configuration NGINX en tapant les commandes ci-dessous et vous avez boosté votre serveur NGINX :

```
sudo nginx -t

sudo systemctl restart nginx
```

Astuce Pro : Si vous trouvez cet article hors de votre portée, il existe un site web simple qui peut obtenir le fichier de configuration final pour vous : consultez [**NGINX Config**](https://nginxconfig.io/)**.**

J'espère que vous aimez cette configuration NGINX et que vous êtes en mesure de booster vos applications web. Utilisez-vous déjà quelque chose de similaire ou avez-vous une opinion différente ? Faites-le moi savoir dans les commentaires.

C'est ma nouvelle microstartup, [VisaList](https://visalist.io), où j'ai appliqué ces optimisations. Elle peut vous aider à trouver les exigences de visa pour tous les pays du monde de manière simple et utile.

[**Trouver des pays à visiter à travers le monde**](https://visalist.io)  
[_Recherchez dans la liste des pays que vous pouvez visiter avec un visa gratuit, un visa à l'arrivée et d'autres exigences de plus de
200 pays._](https://visalist.io)  
[visalist.io](https://visalist.io)

C'est tout pour aujourd'hui ! C'est [**HaKr**](https://1hakr.com) qui se déconnecte. Merci d'avoir lu, et si vous avez trouvé cela utile, cliquez sur ? pour recommander cet article à d'autres afin qu'ils puissent le trouver aussi.

Je construis des [**microstartups**](https://dworks.io) tout en voyageant lorsque je le peux. Si vous trouvez ce genre de choses intéressant, vous pouvez me suivre sur [Twitter](https://twitter.com/1hakr) et consulter mes travaux open-source sur [GitHub](https://github.com/1hakr).