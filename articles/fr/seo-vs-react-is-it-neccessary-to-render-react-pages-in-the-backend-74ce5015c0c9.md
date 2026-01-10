---
title: 'SEO vs. React : Les robots d''indexation sont plus intelligents que vous ne
  le pensez'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-19T16:26:13.000Z'
originalURL: https://freecodecamp.org/news/seo-vs-react-is-it-neccessary-to-render-react-pages-in-the-backend-74ce5015c0c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T1b83o47E1AI0lTpwzHVvA.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: SEO
  slug: seo
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'SEO vs. React : Les robots d''indexation sont plus intelligents que vous
  ne le pensez'
seo_desc: 'By Patrick Hund

  Many people still worry that if you build a websites using tools like React, Angular,
  or Ember, it will hurt your search engine ranking.

  The thinking goes something like this: the web crawlers that search engines use
  won’t be able cra...'
---

Par Patrick Hund

Beaucoup de gens s'inquiètent encore du fait que si vous construisez un site web en utilisant des outils comme React, Angular ou Ember, cela nuira à votre classement dans les moteurs de recherche.

Le raisonnement est le suivant : les robots d'indexation utilisés par les moteurs de recherche ne pourront pas explorer correctement une page à moins qu'elle ne soit entièrement rendue dans le navigateur de l'utilisateur. Au lieu de cela, ils ne verront que le code HTML livré par le backend.

Si ce code HTML ne contient rien de plus que quelques méta-balises et balises de script, le moteur de recherche supposera que votre page est essentiellement vide et vous classera mal.

Je vois souvent des consultants en optimisation pour les moteurs de recherche (SEO) recommander de rendre votre page sur le backend, afin que les robots d'indexation puissent voir beaucoup de joli code HTML qu'ils peuvent ensuite indexer.

Pour moi, ce conseil semble déraisonnable et irréaliste. Nous sommes en 2016. Les utilisateurs s'attendent à ce que les pages soient dynamiques et leur offrent une expérience utilisateur réactive. Ils ne veulent pas attendre qu'une nouvelle page HTML se charge à chaque fois qu'ils cliquent sur quelque chose.

Alors, l'affirmation « le rendu côté client nuit à votre classement de page » est-elle toujours valable ?

### Faire des recherches

![Image](https://cdn-media-1.freecodecamp.org/images/1*WjGkGUHaw5k-LRVPXPdmdw.gif)

Tout d'abord, une mise en garde : je ne suis en aucun cas un expert en SEO. Mais j'ai lu un peu sur le sujet, et voici ce que j'ai trouvé.

Voici une [annonce](https://webmasters.googleblog.com/2015/10/deprecating-our-ajax-crawling-scheme.html) de Google sur leur blog pour les webmasters d'octobre 2015 :

> Aujourd'hui, tant que vous n'empêchez pas Googlebot d'explorer vos fichiers JavaScript ou CSS, nous sommes généralement capables de [rendre et comprendre vos pages web comme les navigateurs modernes](http://googlewebmastercentral.blogspot.com/2014/05/understanding-web-pages-better.html). Pour refléter cette amélioration, nous avons récemment [mis à jour nos directives techniques pour les webmasters](http://googlewebmastercentral.blogspot.com/2014/10/updating-our-technical-webmaster.html) pour recommander de ne pas empêcher Googlebot d'explorer les fichiers CSS ou JS de votre site.

Voici un article de Search Engine Land [article](http://searchengineland.com/tested-googlebot-crawls-javascript-heres-learned-220157) de mai 2015 :

> Nous avons mené une série de tests qui ont vérifié que Google est capable d'exécuter et d'indexer JavaScript avec une multitude d'implémentations. Nous avons également confirmé que Google est capable de rendre la page entière et de lire le DOM, indexant ainsi le contenu généré dynamiquement.

> Les signaux SEO dans le DOM (titres de page, méta-descriptions, balises canoniques, balises méta robots, etc.) sont respectés. Le contenu inséré dynamiquement dans le DOM est également explorable et indexable. De plus, dans certains cas, les signaux du DOM peuvent même prendre le pas sur les déclarations contradictoires dans le code source HTML. Cela nécessitera plus de travail, mais c'était le cas pour plusieurs de nos tests.

Ces deux sources suggèrent qu'il est effectivement sûr d'utiliser une mise en page rendue côté client.

### Le test Preactjs.com

J'ai récemment tweeté une plainte concernant les consultants en SEO qui critiquent mon cher React. Pour être précis, je suis en train de migrer vers [Preact](http://www.preactjs.com/), une alternative légère au React de Facebook. J'ai reçu cette réponse de [Jason Miller](https://twitter.com/_developit), l'un des développeurs travaillant sur Preact :

Outre l'article de blog de Search Engine Land que j'ai cité ci-dessus, Jason a tweeté un lien vers une recherche Google pour la [page d'accueil de Preact](http://www.preactjs.com), qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BmlCGUpoCeo-M-mJh4SEmQ.png)

Cette page est entièrement rendue côté client, en utilisant Preact, comme le prouve un coup d'œil à son code source :

```
<!DOCTYPE html><html><head>
```

```
<meta charset="utf-8">
```

```
<title>Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.</title>
```

```
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,minimal-ui">
```

```
<meta name="mobile-web-app-capable" content="yes">
```

```
<meta name="apple-mobile-web-app-capable" content="yes">
```

```
<meta name="format-detection" content="telephone=no">
```

```
<meta name="theme-color" content="#673AB8">
```

```
<link rel="manifest" href="/manifest.json">
```

```
<link rel="icon" type="image/png" href="/assets/app-icon-192.png" sizes="192x192">
```

```
<script>(function(url){window['_boostrap_'+url]=fetch(url);})('/content'+location.pathname.replace(/^\/(repl)?\/?$/, '/index')+'.md');</script>
```

```
<link rel="shortcut icon" href="/favicon.ico">
```

```
<link href="/style.6bae35e4ff9d687cb418.css" rel="stylesheet">
```

```
</head><body>
```

```
<script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','//www.google-analytics.com/analytics.js','ga');ga('create', 'UA-6031694-20', 'auto');ga('send', 'pageview');</script>
```

```
<script type="text/javascript" src="/bundle.a0afd09fd48712ed0f26.js"></script>
```

```
</body></html>
```

Si le Googlebot n'était pas capable de lire le code HTML rendu par Preact, il ne montrerait pas plus que le contenu des méta-balises.

Et pourtant, voici à quoi ressemblent les résultats Google lors de la recherche de _site:preactjs.com_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nBjY1kfpImRn2lsPdSdkGg.png)

Un autre [article](http://andrewhfarmer.com/react-seo/) d'[Andrew Farmer](https://twitter.com/ahfarmer) de mars 2016 met en garde contre le manque de support JavaScript par les moteurs de recherche autres que Google :

> Dans mes recherches, je n'ai pas trouvé de preuves que Yahoo, Bing ou Baidu supportent JavaScript dans leurs robots d'indexation. Si le SEO sur ces moteurs de recherche est important pour vous, vous devrez utiliser le rendu côté serveur, dont je parlerai dans un futur article.

J'ai donc décidé d'essayer le test de Jason avec d'autres moteurs de recherche :

### ✅ Bing

L'avertissement d'Andrew concernant Bing semble infondé. Voici les [résultats Bing](http://www.bing.com/search?q=site%3Apreactjs.com) lors de la recherche de _site:preactjs.com_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bCcM0TRVImaOF_hVs8HPtg.png)

### ✅ Yahoo

Et les [résultats Yahoo](https://de.search.yahoo.com/search?p=site%3Apreactjs.com&fr=yfp-t-911) lors de la recherche de _site:preactjs.com_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TYNb6bd-o3jQG-sPMGVEIA.png)

### ✅ Duck Duck Go

Et les [résultats Duck Duck Go](https://duckduckgo.com/?q=site%3Apreactjs.com&t=h_&ia=web) lors de la recherche de _site:preactjs.com_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WjfXMyYZz_0W1q_1std4QA.png)

### ⚠️ Baidu

Le moteur de recherche chinois Baidu a des problèmes avec preactjs.com. Voici [ses résultats](http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=site%3Apreactjs.com&rsv_pq=95cb9d6800010ec6&rsv_t=6911YYLRspihOnU5UaDpw8Yo%2FPGDwlfONvdplHywgiMlqY198%2BLvxU6yzwI&rqlang=cn&rsv_enter=1&rsv_sug3=17&rsv_sug2=0&inputT=37643&rsv_sug4=37643) lors de la recherche de _site:preactjs.com_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LNI0cw0ZM42y-0uoYRosCQ.png)

Il semblerait donc que, sauf si être bien classé dans ce qui est essentiellement un moteur de recherche uniquement chinois est une priorité pour vous, il n'y a rien de mal à rendre vos pages web côté client en utilisant JavaScript, tant que vous suivez quelques règles de base (citées de l'[article de blog d'Andrew Farmer](http://andrewhfarmer.com/react-seo/)) :

* Rendez vos composants avant de faire quoi que ce soit d'asynchrone.
* Testez chacune de vos pages avec _Fetch as Google_ pour vous assurer que le Googlebot trouve votre contenu.

Merci d'avoir lu !

### Mise à jour du 25 octobre 2016

[Andrew Ingram](https://medium.com/@andrewingram) a effectué les mêmes tests que j'ai effectués et est parvenu à une conclusion différente.

Citation d'Andrew :

> Voici combien de pages divers moteurs de recherche ont indexées en utilisant la requête « site:preactjs.com »

> Google : 17 Bing : 6 Yahoo : 6 Baidu : 1

> L'un des résultats Google est une page d'erreur, mais elle ne peut probablement pas être désindexée automatiquement en raison de l'absence d'un moyen de déclarer un équivalent 404 dans les SPAs.

> J'ai également lu (je ne me souviens pas où) que Google a une latence de quelques jours lorsqu'il s'agit d'indexer les SPAs par rapport aux applications rendues côté serveur. Cela peut ne pas être un problème pour vous, mais c'est bon à savoir.

Son hypothèse de travail est que les robots des moteurs de recherche autres que Google sont capables d'**indexer** les pages rendues côté client, mais pas de les **explorer**, c'est-à-dire suivre les liens et indexer d'autres pages d'un site web.

→ [Suivez la discussion sur Hacker News](https://t.co/IzQFvr11fL)

### Remerciements

Merci à Adam Audette ([Search Engine Land](http://searchengineland.com/)) et [Andrew Farmer](http://andrewhfarmer.com/) pour leurs excellents articles de blog que j'ai cités, [Jason Miller](https://twitter.com/_developit) pour ses contributions et son inspiration, mes collègues du [eBay Classifieds Group](http://www.ebayclassifiedsgroup.com/) pour leur soutien et Quincy Larson de [Free Code Camp](https://medium.freecodecamp.com/) pour la publication de cet article !