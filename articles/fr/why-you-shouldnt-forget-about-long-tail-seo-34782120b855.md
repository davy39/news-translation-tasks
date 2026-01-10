---
title: Pourquoi vous ne devriez pas oublier le SEO de longue traîne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T10:06:08.000Z'
originalURL: https://freecodecamp.org/news/why-you-shouldnt-forget-about-long-tail-seo-34782120b855
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ExbW2LM_HyyFQBkfLBRgnA.jpeg
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: General Programming
  slug: programming
- name: SEO
  slug: seo
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi vous ne devriez pas oublier le SEO de longue traîne
seo_desc: 'By Ben Rudolph

  A few months ago, I wrote about how I built ThingsOnReddit. It’s a site that finds
  the best Amazon products posted to Reddit and uses Amazon Affiliates to monetize
  it. I became HN famous for a few days or so, and then slowly disappeare...'
---

Par Ben Rudolph

Il y a quelques mois, j'ai [écrit](https://medium.com/swlh/my-journey-to-unlocking-amazon-affiliates-202faf99a098) sur la façon dont j'ai construit [ThingsOnReddit](https://thingsonreddit.com/). C'est un site qui trouve les meilleurs produits Amazon postés sur Reddit et utilise Amazon Affiliates pour le monétiser. Je suis devenu célèbre sur HN pendant quelques jours, puis j'ai lentement disparu dans l'oubli. C'est alors que j'ai réalisé que je finirais par manquer de sites qui me donnaient ce pic rapide de visites, et que je devrais me concentrer sur la construction du SEO pour le site web.

J'ai initialement rencontré quelques obstacles, mais j'ai lentement construit un trafic prévisible et croissant vers le site. En cours de route, j'ai appris beaucoup plus sur la façon dont mon site était utilisé, et je me suis concentré sur l'amélioration du site pour ce cas d'utilisation.

### Repenser la stratégie SEO

Au début, j'ai essayé d'optimiser pour des mots-clés qui pourraient potentiellement amener les utilisateurs à ma page d'accueil. Mon raisonnement était le suivant : l'utilisateur arrive sur la page d'accueil, trouve un subreddit et/ou un produit intéressant, puis achète ledit produit sur Amazon. J'ai même créé une nouvelle page d'accueil pour les utilisateurs, un peu plus conviviale, et offrant un moyen plus facile de naviguer vers les subreddits.

C'était une mauvaise stratégie.

Le tableau qui a changé mon paradigme est ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/WrUleKQjTcxZZFvQf39j1xZ6QqVilyrHSd24)
_Répartition des pages sur lesquelles les utilisateurs atterrissent au cours des 30 derniers jours_

Il est difficile de le voir, mais la page d'accueil, qui a le plus de vues de pages à l'atterrissage, ne représente que 11,27 % du total. La plupart des utilisateurs atterrissent directement sur un subreddit ou une page de produit.

Il est devenu abondamment clair que mon approche SEO devrait être basée sur l'ampleur des pages de mon site web.

![Image](https://cdn-media-1.freecodecamp.org/images/0ykGyr-et1YWK3mY3OC86k1YrbXUInXh7ZyP)
_Ce graphique montre combien de pages Google a indexées au fil du temps_

C'est alors que j'ai commencé à réaliser la puissance du SEO de longue traîne. **Le SEO de longue traîne signifie que vous ciblez des mots-clés niche de Google (généralement 3+ mots ou plus) qui ont une faible concurrence**. Cela s'est naturellement produit sur mon site — il y a des centaines de milliers de pages de produits avec toutes sortes de mots-clés étranges résultant des commentaires des Redditors sur le produit.

#### Sitemaps

Les sitemaps informent un moteur de recherche sur la structure de votre site web. Ce n'est généralement pas nécessaire si votre site est petit et bien lié, mais mon site était immense et étendu.

J'ai créé un sitemap pour inclure le nombre maximum d'URL, 50 000. ThingsOnReddit a une page pour chaque subreddit et produit Amazon mentionné sur Reddit, donc il y a _beaucoup_ de pages potentielles à indexer (beaucoup plus que 50 000). Google prend son temps pour indexer vos pages, mais à mesure qu'il indexait mes pages, ma présence SEO a augmenté de plus de 1000 %.

![Image](https://cdn-media-1.freecodecamp.org/images/hsOqon6PMdG3rI8VFvtm9QN2qNVO6xGjdwvO)
_Utilisateurs venant à ThingsOnReddit via la recherche organique_

#### Balises de lien

Les obtenir correctement est essentiel pour optimiser votre présence SEO. J'ai initialement lancé ThingsOnReddit sans y penser. C'était une erreur.

`**<link rel="canonical" href="**`"/>

Cela est crucial si vous avez un site qui fait une sorte de pagination. Cette balise indique à Google que la page actuelle est en fait la même que l'URL dans l'attribut `href`. Cela est souvent utilisé lorsque des blogs (comme Medium) repostent des articles d'autres sites, mais c'est aussi nécessaire lorsque vous avez des schémas d'URL comme ci-dessous :

```
https://thingsonreddit.com/things/r/buildapc?page=1https://thingsonreddit.com/things/r/buildapc?page=2https://thingsonreddit.com/things/r/buildapc?page=3
```

Ou même :

```
https://thingsonreddit.com/things/r/buildapc?order_by=n_references_in_subreddithttps://thingsonreddit.com/things/r/buildapc?order_by=created_utchttps://thingsonreddit.com/things/r/buildapc?order_by=score
```

Le problème que j'ai rencontré était que Google indexait l'URL :

```
https://thingsonreddit.com/things/r/buildapc?page=7
```

Et cette URL apparaissait dans les résultats de recherche Google. Ensuite, un utilisateur atterrissait sur la page 7 alors que je voulais évidemment qu'il atterrisse sur la page 1. `rel="canonical"` indiquera à Google d'ignorer tous les paramètres d'URL et d'indexer uniquement `https://thingsonreddit.com/things/r/buildapc`.

`**<link rel="next|prev" href="**`"/>

Cela indique à Google que la page logique suivante (ou précédente si vous spécifiez `prev`) est l'URL dans l'attribut `href`. Google [dit](https://support.google.com/webmasters/answer/1663744?hl=en) qu'ils peuvent généralement le comprendre par eux-mêmes, mais selon mon expérience, ils ne l'ont pas bien compris. Il faut un certain temps à Google pour apporter des ajustements, alors faites-le bien dès la première fois.

#### Liens internes

Lors de la construction d'un site de liens d'affiliation, il est tentant de construire votre site web pour amener l'utilisateur à Amazon (ou tout autre site d'affiliation) le plus rapidement possible. Initialement, c'était ce que je cherchais à faire.

![Image](https://cdn-media-1.freecodecamp.org/images/Utv-VN-z97upVMvUS8Tk40-PSr5tq6aQrLYk)

Dans la première implémentation, les utilisateurs étaient directement envoyés à Amazon pour obtenir le clic d'affiliation le plus rapidement possible.

Ce que j'ai finalement appris, c'est que les utilisateurs qui vont acheter un produit cliqueront éventuellement sur le lien Amazon s'ils veulent le produit. **Il est bien plus important d'avoir des pages de produits individuelles pour chaque produit afin que chacune puisse être indexée individuellement et apparaître dans les résultats de recherche.**

#### Analytics

Faire partie d'une meilleure présence SEO consiste à construire une bonne expérience utilisateur. Plus l'expérience utilisateur est bonne, plus votre taux de rebond est faible, et plus Google considérera favorablement votre site. Une partie clé de la compréhension de la façon de créer une bonne expérience est de suivre toutes les choses.

Il est plus difficile de dire comment la modification de l'expérience utilisateur modifie directement votre taux de rebond ou votre classement dans la recherche Google, sauf si vous faites une sorte de test A/B, mais les analyses peuvent vous orienter dans la bonne direction.

Par exemple, j'étais sous l'impression qu'il est _toujours_ bon de construire une liste de diffusion. J'ai donc commencé à montrer agressivement une modale d'inscription à la newsletter lorsque l'utilisateur fait défiler jusqu'en bas de la page :

![Image](https://cdn-media-1.freecodecamp.org/images/wc9okpLcdMLsNBB-eggiDbKrN7Pjo9o-k1Xy)
_Ma modale d'inscription à la newsletter conviviale_

J'ai essayé cela pendant des mois, et j'ai obtenu **0 inscriptions** après avoir montré la modale **609 fois**. Inutile de dire que cette fonctionnalité est extrêmement ennuyeuse et n'a donné aucune inscription, alors je l'ai supprimée.

### Les résultats

Après avoir laissé ThingsOnReddit fonctionner seul pendant un certain temps, je suis heureux d'annoncer de meilleurs résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/CScgnaOlhEsM32d3UuPxVEmqID1dArRYuG3f)

Le mois qui a reçu le plus de clics vers Amazon (jusqu'à présent) était novembre, mais c'était aussi le mois avec le moins de revenus. La plupart de ces clics ont été générés via le trafic social lorsque j'ai essayé de faire passer le site de force via divers sites de médias sociaux.

Il s'avère que **se concentrer sur la recherche organique est non seulement meilleur pour des utilisateurs récurrents durables, mais aussi pour des utilisateurs qui veulent réellement acheter des produits et sont plus susceptibles de convertir**.

À l'avenir, je vais continuer à améliorer le classement de recherche Google du site, en affinant l'expérience du site ainsi qu'en essayant de faire croître le nombre de sites liant à ThingsOnReddit.