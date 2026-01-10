---
title: Attaque Slow Loris utilisant JavaScript sur un serveur PHP [et sa prévention
  !]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-02T00:58:30.000Z'
originalURL: https://freecodecamp.org/news/slow-loris-attack-using-javascript-on-php-server
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/websec.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Security
  slug: web-security
seo_title: Attaque Slow Loris utilisant JavaScript sur un serveur PHP [et sa prévention
  !]
seo_desc: 'By Mehul Mohan

  Forget the post for a minute, let''s begin with what this title is about! This is
  a web security-based article which will get into the basics about how HTTP works.
  We''ll also look at a simple attack which exploits the way the HTTP proto...'
---

Par Mehul Mohan

Oubliez l'article pour un instant, commençons par ce dont parle ce titre ! Il s'agit d'un article sur la sécurité web qui abordera les bases du fonctionnement de HTTP. Nous examinerons également une attaque simple qui exploite le fonctionnement du protocole HTTP.

## Qu'est-ce que HTTP ?

**HTTP**, HyperText Transfer Protocol, est le protocole utilisé par le web pour la communication. Votre appareil, lorsque vous utilisez un navigateur, utilise ce protocole particulier pour envoyer des requêtes à des serveurs distants afin de demander des données. 

C'est un peu comme si vous disiez à votre mère : "Hé maman, j'ai besoin de manger l'article dans le frigo présent sur l'étagère 2, pourrais-tu me le donner ?"

Et votre mère dit : "Bien sûr, le voilà", et vous envoie cet article. Maintenant, HTTP est la manière dont vous avez pu communiquer cette information à votre mère, un peu comme la langue que vous avez utilisée pour communiquer.

## Comment fonctionne HTTP

Voici une vidéo TL;DR si vous êtes une personne visuelle. Sinon, poursuivez avec l'article :

%[https://www.youtube.com/watch?v=aE75gHVK16A]

HTTP (couche 7) est construit sur le protocole TCP (couche 4). Nous pouvons utiliser l'utilitaire `nc` (netcat) pour ouvrir une socket TCP brute vers n'importe quel site web fonctionnant sur HTTP (généralement le port 80). Voir l'exemple suivant sur la façon dont nous nous connectons au port HTTP 80 pour google.com en utilisant netcat :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-02-at-6.09.39-am.png)

Voyez les données que nous avons envoyées :

```shell
GET / HTTP/1.1
Host: google.com
X-header-1: somemoredata
X-header-2: somemoredata
<ligne vide>
```

Ignorez les en-têtes supplémentaires `X-header-*`, ce sont simplement des en-têtes aléatoires que vous pouvez envoyer avec votre requête. L'en-tête important à inclure dans la spécification HTTP/1.1 est l'en-tête `Host`.

Et la réponse que nous avons reçue :

```shell
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Tue, 01 Oct 2019 23:24:13 GMT
Expires: Thu, 31 Oct 2019 23:24:13 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Accept-Ranges: none
Via: HTTP/1.1 forward.http.proxy:3128
Connection: keep-alive

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

Ainsi, HTTP est un protocole en texte clair constitué des informations de requête envoyées par le client et de la réponse comme montré ci-dessus.

## Attaque Slow Loris

Une attaque Slow Loris exploite le fait que je pourrais faire une requête HTTP très très lentement. En d'autres termes, je peux initier une requête HTTP vers le serveur et continuer à envoyer des données au serveur très lentement afin de maintenir cette connexion active. Et en même temps, elle ne termine jamais cette connexion et ouvre plusieurs connexions de ce type pour épuisement du pool de connexions du serveur.

**Avertissement** - Tester la pénétration de tout service en ligne/hors ligne ne vous appartenant pas sans autorisation écrite préalable est **illégal** et je ne suis pas responsable des dommages causés. **Utilisez ce contenu à des fins éducatives uniquement.**

## Démonstration de Slow Loris :

%[https://www.youtube.com/watch?v=KUxd7FFDwTM]

Cela signifie que je pourrais continuer à envoyer des données supplémentaires au serveur sous forme d'en-têtes. Maintenant, je vais démarrer un simple serveur de développement PHP sur ma machine :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-02-at-6.16.34-am.png)

Et j'utilise un simple script Node pour effectuer ce que nous avons discuté ci-dessus sur mon serveur local :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-02-at-6.17.40-am.png)

Vous pouvez trouver le script Node utilisé [ici](https://gist.github.com/mehulmpt/49eee6cc0e84d6770b904336d0ad7f3e).

Après un certain temps, vous verrez que notre serveur PHP plante réellement !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-02-at-6.17.52-am.png)

C'est parce qu'il y a beaucoup trop de connexions ouvertes et que PHP ne peut pas gérer plus de connexions ouvertes (en raison des limites de mémoire/matériel).

Maintenant, bien sûr, cela fonctionne sans faille sur un serveur de développement local. Mais si vous êtes en mesure de trouver un serveur qui n'implémente pas de protections contre les attaques slow loris, c'est un gros problème pour eux.

## Protections contre une attaque Slow Loris



* Utilisez des solutions comme Cloudflare devant vos serveurs pour prévenir les attaques DoS/DDoS  
Citant le site de Cloudflare :

> Cloudflare **met en mémoire tampon les requêtes entrantes** avant de commencer à envoyer quoi que ce soit au serveur d'origine. En conséquence, le trafic d'attaque "lent et lent" comme les attaques Slowloris n'atteint jamais la cible prévue. En savoir plus sur la façon dont la protection DDoS de Cloudflare arrête les attaques slowloris.

* Limitez le nombre de connexions simultanées ouvertes par une adresse IP particulière à un petit nombre. Cela pourrait être réalisé en utilisant des serveurs proxy inverses frontaux simples comme nginx en utilisant leur implémentation de l'algorithme du seau qui fuit. Comment cela fonctionne, c'est quelque chose pour un autre jour !
* Augmenter la capacité du serveur - Maintenant, cela pourrait atténuer les petites attaques, mais honnêtement, l'attaquant peut et amplifiera facilement l'attaque originale en raison de la faible bande passante requise pour mener une telle attaque.

## Conclusion

De nombreux serveurs (nginx/apache2 nouvelles versions) sont livrés avec des protections contre les attaques slow loris par défaut. Mais pour de nombreux services internes, les serveurs pourraient être vulnérables à cette attaque simple. 

Vous pourriez vouloir vérifier vos services et implémenter les correctifs. La sécurité web est un domaine passionnant, et je prévois de faire une série web à ce sujet sur [codedamn](https://www.youtube.com/codedamn). Vous pouvez me contacter sur [twitter](https://twitter.com/mehulmpt) pour les mises à jour également. En attendant, restez en sécurité !