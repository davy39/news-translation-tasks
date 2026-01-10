---
title: La limitation de débit NGINX en bref
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-24T11:23:45.000Z'
originalURL: https://freecodecamp.org/news/nginx-rate-limiting-in-a-nutshell-128fe9e0126c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c5HqrBfCv8ZdNsOZUJHEUw.jpeg
tags:
- name: Devops
  slug: devops
- name: nginx
  slug: nginx
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: La limitation de débit NGINX en bref
seo_desc: 'By Sébastien Portebois

  NGINX is awesome… but I found its documentation on rate limiting to be somewhat…
  limited. So I’ve written this guide to rate-liming and traffic shaping with NGINX.

  We’re going to:


  describe the NGINX directives

  explain NGINX’s ...'
---

Par Sébastien Portebois

NGINX est génial… mais j'ai trouvé sa documentation sur la limitation de débit quelque peu… limitée. J'ai donc écrit ce guide sur la limitation de débit et la gestion du trafic avec NGINX.

Nous allons :

* décrire les directives NGINX
* expliquer la logique d'acceptation/rejet de NGINX
* vous aider à visualiser comment un véritable pic de trafic est traité en utilisant divers paramètres : limitation de débit, politique de trafic et autorisation de petits pics

En bonus, j'ai inclus un [dépôt GitHub](https://github.com/sportebois/nginx-rate-limit-sandbox) et l'image [Docker résultante](https://hub.docker.com/r/sportebois/nginx-rate-limit-sandbox/) afin que vous puissiez expérimenter et reproduire les tests. C'est toujours plus facile d'apprendre en pratiquant !

### Directives de limitation de débit NGINX et leurs rôles

![Image](https://cdn-media-1.freecodecamp.org/images/1*TlPXt7Z1zfWXANysXUzscg.png)

Cet article se concentre sur le [ngx_http_limit_req_module](https://nginx.org/en/docs/http/ngx_http_limit_req_module.html), qui vous fournit les directives `limit_req_zone` et `limit_req`. Il fournit également `limit_req_status` et `limit_req_level`. Ensemble, celles-ci vous permettent de contrôler le code de statut de réponse HTTP pour les requêtes rejetées, et comment ces rejets sont journalisés.

La plupart des confusions proviennent de la logique de rejet.

Tout d'abord, vous devez comprendre la directive `limit_req`, qui nécessite un paramètre `zone`, et fournit également des paramètres **optionnels** `burst` et `nodelay`.

Plusieurs concepts entrent en jeu ici :

* `zone` vous permet de définir un seau, un espace partagé dans lequel compter les requêtes entrantes. Toutes les requêtes entrant dans le même seau seront comptées dans la même limite de débit. C'est ce qui vous permet de limiter par URL, par IP, ou autre chose de plus sophistiqué.
* `burst` est optionnel. S'il est défini, il détermine combien de requêtes excédentaires vous pouvez accepter au-delà du débit de base. Une chose importante à noter ici : _burst est une valeur absolue, ce n'est pas un débit_.
* `nodelay` est également optionnel et n'est utile que lorsque vous définissez également une valeur `burst`, et nous verrons pourquoi ci-dessous.

### Comment NGINX décide-t-il si une requête est acceptée ou rejetée ?

Lorsque vous définissez une zone, vous définissez un débit, comme `300r/m` pour permettre 300 requêtes par minute, ou `5r/s` pour permettre 5 requêtes chaque seconde.

Par exemple :

* `limit_req_zone $request_uri zone=zone1:10m rate=300r/m;`
* `limit_req_zone $request_uri zone=zone2:10m rate=5r/s;`

Il est important de comprendre que ces 2 zones ont les mêmes limites. Le paramètre `rate` est utilisé par NGINX pour calculer une fréquence : quel est l'intervalle de temps avant d'accepter une nouvelle requête ? NGINX appliquera l'algorithme du seau percé avec ce taux de rafraîchissement des jetons.

Pour NGINX, `300r/m` et `5r/s` sont traités de la même manière : permettre une requête toutes les 0,2 secondes pour cette zone. Toutes les 0,2 seconde, dans ce cas, NGINX définira un drapeau pour se souvenir qu'il peut accepter une requête. Lorsqu'une requête arrive qui correspond à cette zone, NGINX définit le drapeau sur false et la traite. Si une autre requête arrive avant que le minuteur ne s'incrémente, elle sera immédiatement rejetée avec un code de statut 503. Si le minuteur s'incrémente et que le drapeau était déjà défini pour accepter une requête, rien ne change.

### Avez-vous besoin de limitation de débit ou de gestion du trafic ?

Voici le paramètre `burst`. Pour le comprendre, imaginez que le drapeau que nous avons expliqué ci-dessus n'est plus un booléen, mais un entier : le nombre maximal de requêtes que NGINX peut accepter dans un pic.

Ce n'est plus un algorithme de seau percé, mais un algorithme de seau à jetons. Le `rate` contrôle la rapidité avec laquelle le minuteur s'incrémente, mais ce n'est plus un jeton vrai/faux, mais un compteur allant de `0` à `1+valeur de burst`. Chaque fois que le minuteur s'incrémente, le compteur est incrémenté, sauf s'il est déjà à sa valeur maximale de `b+1`. Maintenant, vous devriez comprendre pourquoi le paramètre `burst` est une valeur, et non un débit.

Lorsqu'une nouvelle requête arrive, NGINX vérifie si un jeton est disponible (c'est-à-dire que le compteur est > 0), sinon, la requête est rejetée. Si un jeton est disponible, la requête est acceptée et sera traitée, et ce jeton sera consommé (le compteur est décrémenté).

D'accord, donc NGINX acceptera la requête si un jeton de pic est disponible. _Mais quand NGINX traitera-t-il cette requête ?_

Vous avez demandé à NGINX d'appliquer un débit maximal de `5r/s`, NGINX accepte les requêtes excédentaires si des jetons de pic sont disponibles, mais attendra qu'il y ait de la place pour les traiter dans cette limite de débit maximale. Par conséquent, **ces requêtes de pic seront traitées avec un certain délai**, ou elles expireront.

En d'autres termes, NGINX ne dépassera pas la limite de débit définie dans la déclaration de zone, et mettra donc en file d'attente les requêtes supplémentaires et les traitera avec un certain délai, au fur et à mesure que le minuteur de jetons s'incrémente et que moins de requêtes sont reçues.

Pour utiliser un exemple simple, supposons que vous avez un débit de `1r/s`, et un pic de `3`. NGINX reçoit 5 requêtes en même temps :

* La première est acceptée et traitée
* Parce que vous autorisez 1+3, il y a 1 requête qui est immédiatement rejetée, avec un code de statut 503
* Les 3 autres seront traitées, une par une, mais pas immédiatement. Elles seront traitées au rythme de `1r/s` pour rester dans la limite que vous avez définie. Si aucune autre requête n'arrive, en consommant déjà ce quota. Une fois la file d'attente vide, le compteur de pic commencera à être incrémenté à nouveau (le seau à jetons commencera à être rempli à nouveau)

Si vous utilisez NGINX comme proxy, l'amont recevra la requête à un débit maximal de `1r/s`, et il ne sera pas conscient d'un pic de requêtes entrantes, tout sera plafonné à ce débit.

Vous venez de faire de la gestion de trafic, en introduisant un certain délai pour réguler les pics et produire un flux plus régulier en dehors de NGINX.

#### Entrée de nodelay

`nodelay` indique à NGINX que les requêtes qu'il accepte dans la fenêtre de pic doivent être traitées immédiatement, comme des requêtes régulières.

Par conséquent, les pics se propageront aux amonts de NGINX, mais avec une certaine limite, définie par la valeur `burst`.

### Visualisation des limites de débit

Parce que je crois que la meilleure façon de se souvenir de cela est de l'expérimenter de manière pratique, j'ai mis en place une petite image Docker avec une configuration NGINX exposant divers paramètres de limitation de débit pour voir les réponses à un emplacement de base à débit limité, à un emplacement à débit limité avec `burst` activé, et à un emplacement à débit limité avec `burst` et `nodelay`, jouons avec cela.

Ces exemples utilisent cette simple configuration NGINX (que nous fournirons sous forme d'image Docker à la fin de cet article pour que vous puissiez tester plus facilement) :

```
limit_req_zone $request_uri zone=by_uri:10m rate=30r/m;

server {
    listen 80;

    location /by-uri/burst0 {
        limit_req zone=by_uri;
        try_files $uri /index.html;
    }

    location /by-uri/burst5 {
        limit_req zone=by_uri burst=5;
        try_files $uri /index.html;
    }

    location /by-uri/burst5_nodelay {
        limit_req zone=by_uri burst=5 nodelay;
        try_files $uri /index.html;
    }
}
```

En commençant avec cette configuration, tous les exemples ci-dessous enverront 10 requêtes concurrentes à la fois. Voyons :

* combien sont rejetées par la limitation de débit ?
* quel est le taux de traitement des requêtes acceptées ?

#### Envoi de 10 requêtes parallèles à un point de terminaison à débit limité

![Image](https://cdn-media-1.freecodecamp.org/images/1*bqER3OkNtH4MNWZTCjF4Zg.gif)
_10 requêtes atteignant un point de terminaison à débit limité en même temps_

Cette configuration permet 30 requêtes par minute. Mais 9 des 10 requêtes sont rejetées dans ce cas. Si vous avez suivi les étapes précédentes, cela devrait avoir du sens : `30r/m` signifie qu'une nouvelle requête est autorisée toutes les 2 secondes. Ici, 10 requêtes arrivent en même temps, une est autorisée, les 9 autres sont vues par NGINX avant que le minuteur de jetons ne s'incrémente, et sont donc toutes rejetées.

#### Mais je suis d'accord pour tolérer un certain pic pour certains clients/points de terminaison

D'accord, ajoutons donc l'argument `burst=5` pour permettre à NGINX de gérer de petits pics pour ce point de terminaison de la zone à débit limité :

![Image](https://cdn-media-1.freecodecamp.org/images/1*R9D2q4zmUdDQO2k0AvrOWA.gif)
_10 requêtes concurrentes envoyées à la fois à un point de terminaison avec un argument burst=5_

Que se passe-t-il ici ? Comme prévu avec l'argument `burst`, 5 requêtes supplémentaires sont acceptées, nous sommes donc passés de 1/10 à 6/10 succès (et le reste est rejeté). Mais la manière dont NGINX rafraîchit son jeton et traite les requêtes acceptées est assez visible ici : le débit sortant est plafonné à `30r/m`, ce qui équivaut à 1 requête toutes les 2 secondes.

La première est retournée après 0,2 seconde. Le minuteur s'incrémente après 2 secondes, et une des requêtes en attente est traitée et retournée, avec un temps de traitement total de 2,02 secondes. 2 secondes plus tard, le minuteur s'incrémente à nouveau, traitant une autre requête en attente, qui est retournée avec un temps de traitement total de 4,02 secondes. Et ainsi de suite…

L'argument `burst` vous permet simplement de transformer la limitation de débit NGINX d'un simple filtre de seuil en une passerelle de politique de gestion du trafic.

#### Mon serveur a une capacité supplémentaire. Je veux utiliser une limitation de débit pour l'empêcher de dépasser cette capacité.

Dans ce cas, l'argument `nodelay` sera utile. Envoyons les mêmes 10 requêtes à un point de terminaison `burst=5 nodelay` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wVpU5zy5Yfg6c_lx2VIrAw.gif)
_10 requêtes concurrentes envoyées à un point de terminaison configuré avec burst=5 nodelay_

Comme prévu avec `burst=5`, nous avons toujours le même nombre de statuts 200 et 503. Mais maintenant, le débit sortant n'est plus strictement contraint au rythme de 1 requête toutes les 2 secondes. Tant que des jetons de pic sont disponibles, toute requête entrante est acceptée et traitée immédiatement. Le rythme d'incrémentation du minuteur est toujours aussi important qu'avant pour contrôler le taux de rafraîchissement/remplissage de ces jetons de pic, mais les requêtes acceptées ne subissent plus aucun délai supplémentaire.

_Note_ : dans ce cas, la `zone` utilise `$request_uri`, mais tous les tests suivants fonctionnent exactement de la même manière pour une configuration `$binary_remote_addr` qui limiterait le débit par IP client. Vous pourrez jouer avec cela dans l'image Docker.

### Récapitulons

Si nous essayons de visualiser comment NGINX accepte les requêtes entrantes, puis les traite en fonction du `rate`, `burst` et du paramètre `nodelay`, voici une vue synthétique.

Pour garder les choses simples, nous montrerons le nombre de requêtes entrantes (puis acceptées ou rejetées, et traitées) par étape de temps, la valeur de l'étape de temps dépendant de la limite de débit définie par la zone. Mais la durée réelle de cette étape n'a pas d'importance en fin de compte. Ce qui est significatif, c'est le nombre de requêtes que NGINX doit traiter dans chacune de ces étapes.

Voici donc le trafic que nous allons envoyer à travers divers paramètres de limitation de débit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8yyo8Qb1sv28w1NLEvIUOg.png)
_Requêtes entrantes, et la limite de débit définie dans cette zone_

![Image](https://cdn-media-1.freecodecamp.org/images/1*nPsLpvnDxuNRR7mHNaqqeA.png)
_Requêtes acceptées et rejetées lorsqu'aucun paramètre de pic n'est défini_

Sans utiliser le pic (c'est-à-dire `burst=0`), nous avons vu que NGINX agit comme un pur acteur de limitation de débit/politique de trafic. Toutes les requêtes sont soit traitées immédiatement, si le minuteur de débit s'est incrémenté, soit rejetées immédiatement sinon.

Maintenant, si nous voulons permettre un petit pic pour utiliser la capacité inutilisée sous la limite de débit, nous avons vu que l'ajout d'un argument `burst` nous permet de le faire, ce qui implique un certain délai supplémentaire dans le traitement des requêtes consommant les jetons de pic :

![Image](https://cdn-media-1.freecodecamp.org/images/1*sEQ-tyF2VyrA8Xle5Mgf7A.png)
_Requêtes acceptées, acceptées avec délai et rejetées lorsque le pic est utilisé_

Nous pouvons voir que le nombre total de requêtes rejetées est plus faible, et NGINX traite plus de requêtes. Seules les requêtes supplémentaires lorsque aucun jeton de pic n'est disponible sont rejetées. Dans cette configuration, NGINX effectue une véritable gestion du trafic.

Enfin, nous avons vu que NGINX peut être utilisé pour faire soit de la politique de trafic, soit pour limiter la taille du pic, mais propage toujours une partie de ces pics aux travailleurs de traitement (amonts ou locaux), ce qui, en fin de compte, génère un débit sortant moins stable, mais avec une meilleure latence, si vous pouvez traiter ces requêtes supplémentaires :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dj7MfuYzk6c9aVO8-EEaFA.png)
_Requêtes acceptées et traitées et requêtes rejetées lorsque le pic est utilisé avec nodelay_

### Jouer avec le bac à sable de limitation de débit vous-même

Maintenant, vous pouvez explorer le code, cloner le dépôt, jouer avec l'image Docker, et vous familiariser rapidement pour mieux solidifier votre compréhension de ces concepts. [https://github.com/sportebois/nginx-rate-limit-sandbox](https://github.com/sportebois/nginx-rate-limit-sandbox)

### Mise à jour (14 juin 2017)

NGINX a publié il y a quelques jours leur propre explication détaillée de leur mécanisme de limitation de débit. Vous pouvez maintenant en apprendre plus à ce sujet dans leur article de blog [Rate Limiting with NGINX and NGINX Plus](https://www.nginx.com/blog/rate-limiting-nginx/).