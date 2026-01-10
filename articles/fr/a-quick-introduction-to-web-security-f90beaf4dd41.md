---
title: Une introduction rapide à la sécurité web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-15T15:22:19.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-web-security-f90beaf4dd41
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xw9gprMTI6h3U3NkKV0vUg.jpeg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une introduction rapide à la sécurité web
seo_desc: 'By Austin Tackaberry

  A web developer’s primer on CORS, CSP, HSTS, and all the web security acronyms!

  There are many reasons to learn about web security, such as:


  You’re a concerned user who is worried about your personal data being leaked

  You’re a c...'
---

Par Austin Tackaberry

#### Un guide pour les développeurs web sur CORS, CSP, HSTS et tous les acronymes de la sécurité web !

Il y a de nombreuses raisons d'apprendre la sécurité web, telles que :

* Vous êtes un utilisateur soucieux qui s'inquiète de la fuite de vos données personnelles
* Vous êtes un développeur web soucieux qui veut rendre ses applications web plus sûres
* Vous êtes un développeur web postulant à des emplois et vous voulez être prêt si vos recruteurs vous posent des questions sur la sécurité web

et ainsi de suite.

Ce post expliquera certains acronymes courants de la sécurité web de manière facile à comprendre mais toujours précise.

Avant cela, assurons-nous de comprendre quelques concepts de base de la sécurité.

### Deux concepts fondamentaux de la sécurité

#### **Personne n'est jamais à 100 % en sécurité.**

Il n'y a pas de notion d'être protégé à 100 % contre le piratage. Si quelqu'un vous dit cela, il a tort.

#### **Une seule couche de protection ne suffit pas.**

Vous ne pouvez pas simplement dire...

> Oh, parce que j'ai implémenté CSP, je suis en sécurité. Je peux rayer le cross-site scripting de ma liste de vulnérabilités car cela ne peut plus arriver.

Peut-être que cela semble évident pour certains, mais il est facile de se retrouver à penser de cette manière. Je pense qu'une des raisons pour lesquelles les programmeurs peuvent facilement se retrouver à penser ainsi est que beaucoup de codage est en noir et blanc, 0 ou 1, vrai ou faux. La sécurité n'est pas si simple.

Nous allons commencer par quelque chose que tout le monde rencontre assez tôt dans leur parcours de développement web. Et puis vous regardez sur StackOverflow et trouvez une série de réponses vous expliquant comment le contourner.

### Partage de ressources cross-origin (CORS)

Avez-vous déjà obtenu une erreur qui ressemblait à ceci ?

```
No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'null' is therefore not allowed access.
```

Vous n'êtes certainement pas seul. Et puis vous le googlez, et quelqu'un vous dit de télécharger cette extension qui fera disparaître tous vos problèmes !

> Super, non ?

**CORS est là pour vous protéger, pas pour vous nuire !**

Pour expliquer comment CORS vous aide, parlons d'abord des cookies, spécifiquement des **cookies d'authentification**. Les cookies d'authentification sont utilisés pour informer un serveur que vous êtes connecté, et ils sont automatiquement envoyés avec toute requête que vous faites à ce serveur.

Supposons que vous êtes connecté à Facebook, et qu'ils utilisent des cookies d'authentification. Vous cliquez sur `bit.ly/r43nugi` qui vous redirige vers `superevilwebsite.rocks`. Un script dans `superevilwebsite.rocks` fait une requête côté client à `facebook.com` qui envoie votre cookie d'authentification !

Dans un monde sans CORS, ils pourraient apporter des modifications à votre compte sans que vous le sachiez. Jusqu'à ce qu'ils publient `bit.ly/r43nugi` sur votre timeline, et que tous vos amis cliquent dessus, et puis ils publient `bit.ly/r43nugi` sur les timelines de tous vos amis et le cycle continue dans un schéma malveillant en largeur d'abord qui conquiert tous les utilisateurs de Facebook, et le monde est consommé par `superevilwebsite.rocks`. ?

Dans un monde avec CORS, cependant, Facebook ne permettrait que les requêtes avec une origine de `facebook.com` pour modifier les données sur leur serveur. En d'autres termes, ils limiteraient le partage de ressources cross-origin. Vous pourriez alors demander...

> Eh bien, superevilwebsite.rocks ne peut-il pas simplement changer l'en-tête d'origine de leur requête, pour qu'il semble qu'elle provienne de facebook.com ?

Ils peuvent essayer, mais cela ne fonctionnera pas car le navigateur l'ignorera simplement et utilisera l'origine réelle.

> D'accord, mais que se passe-t-il si superevilwebsite.rocks fait la requête côté serveur ?

Dans ce cas, ils pourraient contourner CORS, mais ils ne gagneront pas car ils ne pourront pas envoyer votre cookie d'authentification avec la requête. Le script devrait s'exécuter côté client pour accéder à vos cookies côté client.

### Politique de sécurité du contenu (CSP)

Pour comprendre CSP, nous devons d'abord parler de l'une des vulnérabilités les plus courantes sur le web : XSS, qui signifie cross-site scripting (youpi — un autre acronyme).

XSS est lorsqu'une personne malveillante injecte du JavaScript dans votre code côté client. Vous pourriez penser...

> Que peuvent-ils faire ? Changer une couleur de rouge en bleu ?

Supposons que quelqu'un a réussi à injecter du JavaScript dans le code côté client d'un site web que vous visitez.

Que pourraient-ils faire de malveillant ?

* Ils pourraient faire des requêtes HTTP à un autre site en se faisant passer pour vous.
* Ils pourraient ajouter une balise d'ancrage qui vous envoie vers un site web identique à celui sur lequel vous vous trouvez, avec quelques caractéristiques légèrement différentes et malveillantes.
* Ils pourraient ajouter une balise de script avec du JavaScript en ligne.
* Ils pourraient ajouter une balise de script qui récupère un fichier JavaScript distant quelque part.
* Ils pourraient ajouter un iframe qui couvre la page et semble faire partie du site web, vous incitant à insérer votre mot de passe.

Les possibilités sont infinies.

CSP essaie de prévenir cela en limitant :

* ce qui peut être ouvert dans un iframe
* quelles feuilles de style peuvent être chargées
* où les requêtes peuvent être faites, etc.

Alors, comment cela fonctionne-t-il ?

Lorsque vous cliquez sur un lien ou tapez une URL de site web dans la barre d'adresse de votre navigateur, votre navigateur fait une requête GET. Elle finit par atteindre un serveur qui sert du HTML avec certains en-têtes HTTP. Si vous êtes curieux de savoir quels en-têtes vous recevez, ouvrez l'onglet Réseau dans votre console et visitez quelques sites web.

Vous pourriez voir un en-tête de réponse qui ressemble à ceci :

```
content-security-policy: default-src * data: blob:;script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.virtualearth.net *.google.com 127.0.0.1:* *.spotilocal.com:* 'unsafe-inline' 'unsafe-eval' *.atlassolutions.com blob: data: 'self';style-src data: blob: 'unsafe-inline' *;connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net *.spotilocal.com:* wss://*.facebook.com:* https://fb.scanandcleanlocal.com:* *.atlassolutions.com attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' chrome-extension://boadgeojelhgndaghljhdicfkmllpafd chrome-extension://dliochdbjfkdbacpmhlcpmleaejidimm;
```

C'est la politique de sécurité du contenu de `facebook.com`. Reformattons-la pour la rendre plus facile à lire :

```
content-security-policy:
default-src * data: blob:;

script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.virtualearth.net *.google.com 127.0.0.1:* *.spotilocal.com:* 'unsafe-inline' 'unsafe-eval' *.atlassolutions.com blob: data: 'self';

style-src data: blob: 'unsafe-inline' *;

connect-src *.facebook.com facebook.com *.fbcdn.net *.facebook.net *.spotilocal.com:* wss://*.facebook.com:* https://fb.scanandcleanlocal.com:* *.atlassolutions.com attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' chrome-extension://boadgeojelhgndaghljhdicfkmllpafd chrome-extension://dliochdbjfkdbacpmhlcpmleaejidimm;
```

Maintenant, décomposons les directives.

* `**default-src**` restreint toutes les autres directives CSP qui ne sont pas explicitement listées.
* `**script-src**` restreint les scripts qui peuvent être chargés.
* `**style-src**` restreint les feuilles de style qui peuvent être chargées.
* `**connect-src**` restreint les URLs qui peuvent être chargées en utilisant des interfaces de script, comme fetch, XHR, ajax, etc.

Notez qu'il existe de nombreuses autres directives CSP que ces quatre-ci. Le navigateur lira l'en-tête CSP et appliquera ces directives à tout ce qui se trouve dans le fichier HTML qui a été servi. Si les directives sont définies de manière appropriée, elles permettent uniquement ce qui est nécessaire.

Si aucun en-tête CSP n'est présent, alors tout est permis et rien n'est restreint. Partout où vous voyez `*`, c'est un caractère générique. Vous pouvez imaginer remplacer `*` par n'importe quoi et cela sera autorisé.

### HTTPS ou HTTP Sécurisé

Vous avez certainement entendu parler de HTTPS. Peut-être avez-vous entendu certaines personnes dire...

> Pourquoi devrais-je me soucier d'utiliser HTTPS si je suis simplement sur un site web en train de jouer à un jeu.

Ou peut-être avez-vous entendu l'autre côté...

> Vous êtes fou si votre site n'a pas HTTPS. Nous sommes en 2018 ! Ne faites pas confiance à quiconque dit le contraire.

Peut-être avez-vous entendu que Chrome marquera désormais votre site comme non sécurisé s'il n'est pas en HTTPS.

À sa base, HTTPS est assez simple. HTTPS est chiffré et HTTP ne l'est pas.

Alors pourquoi cela compte-t-il si vous n'envoyez pas de données sensibles ?

Préparez-vous pour un autre acronyme... MITM, qui signifie Man in the Middle.

Si vous utilisez un Wi-Fi public sans mot de passe dans un café, il est assez facile pour quelqu'un de se faire passer pour votre routeur, de sorte que toutes les requêtes et réponses passent par lui. Si vos données ne sont pas chiffrées, alors ils peuvent en faire ce qu'ils veulent. Ils peuvent modifier le HTML, le CSS ou le JavaScript avant même qu'il n'atteigne votre navigateur. Étant donné ce que nous savons sur XSS, vous pouvez imaginer à quel point cela pourrait être grave.

> D'accord, mais comment se fait-il que mon ordinateur et le serveur sachent comment chiffrer/déchiffrer mais pas ce MITM ?

C'est là qu'interviennent SSL (Secure Sockets Layer) et plus récemment, TLS (Transport Layer Security). TLS a pris la relève de SSL en 1999 en tant que technologie de chiffrement utilisée dans HTTPS. Exactement comment TLS fonctionne est en dehors du cadre de ce post.

### HTTP Strict-Transport-Security (HSTS)

Celui-ci est assez simple. Utilisons à nouveau l'en-tête de Facebook comme exemple :

```
strict-transport-security: max-age=15552000; preload
```

* `max-age` spécifie combien de temps un navigateur doit se souvenir de forcer l'utilisateur à accéder à un site web en utilisant HTTPS.
* `preload` n'est pas important pour nos besoins. C'est un service hébergé par Google et ne fait pas partie de la spécification HSTS.

Cet en-tête ne s'applique que si vous avez accédé au site en utilisant HTTPS. Si vous avez accédé au site via HTTP, l'en-tête est ignoré. La raison est que, tout simplement, HTTP est si peu sécurisé qu'il ne peut pas être digne de confiance.

Utilisons l'exemple de Facebook pour illustrer davantage comment cela est utile en pratique. Vous accédez à `facebook.com` pour la première fois, et vous savez que HTTPS est plus sûr que HTTP, donc vous y accédez via HTTPS, `https://facebook.com`. Lorsque votre navigateur reçoit le HTML, il reçoit l'en-tête ci-dessus qui indique à votre navigateur de vous forcer à rediriger vers HTTPS pour les requêtes futures. Un mois plus tard, quelqu'un vous envoie un lien vers Facebook en utilisant HTTP, `http://facebook.com`, et vous cliquez dessus. Puisqu'un mois est inférieur aux 15552000 secondes spécifiées par la directive `max-age`, votre navigateur enverra la requête en HTTPS, empêchant une potentielle attaque MITM.

### Réflexions finales

La sécurité web est importante, peu importe où vous en êtes dans votre parcours de développement web. Plus vous vous exposez à cela, mieux vous serez. La sécurité est quelque chose qui devrait être important pour tout le monde, pas seulement pour les personnes qui l'ont explicitement dans leur titre de travail ! ?