---
title: 'Hashnode : Comment lancer votre propre blog de développeur sur votre propre
  domaine en quelques minutes'
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-01-21T21:47:51.000Z'
originalURL: https://freecodecamp.org/news/devblog-launch-your-developer-blog-own-domain
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9da4740569d1a4ca38da.jpg
tags:
- name: Blogging
  slug: blogging
seo_title: 'Hashnode : Comment lancer votre propre blog de développeur sur votre propre
  domaine en quelques minutes'
seo_desc: 'Hashnode recently released a tool that lets you set up your own developer
  blog on your own domain within minutes.

  In case your wondering, I am not sponsored by Hashnode. They don''t even know I''m
  writing this article. I''m just incredibly impressed wit...'
---

Hashnode a récemment publié un outil qui vous permet de configurer votre propre blog de développeur sur votre propre domaine en quelques minutes.

Au cas où vous vous poseriez la question, je ne suis pas sponsorisé par Hashnode. Ils ne savent même pas que j'écris cet article. Je suis simplement incroyablement impressionné par leurs outils, et j'ai pensé les partager avec vous.

Tout d'abord, vous pourriez vous demander : pourquoi ne pas simplement utiliser Medium ou une autre plateforme de publication ouverte ?

Eh bien, voici quelques raisons majeures pour lesquelles Hashnode est meilleur pour les développeurs.

## Raison n°1 : Vous pouvez héberger votre blog Hashnode sur votre propre domaine.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/All_I_Really_Need_to_Know_About_InfoSec__I_learned_from_Mr__Robot-1.png)
_J'ai publié cet article sur mon blog Hashnode et il est maintenant disponible sur le sous-domaine de mon site personnel._

C'est une grande affaire si vous souhaitez développer le référencement de votre blog sur un horizon temporel plus long.

Cela vous évite également de devenir dépendant des plateformes de blogging qui ont une fâcheuse tendance à afficher des publicités ou des popups sur vos articles (ou même à mettre des paywalls / murs de connexion devant vos articles de blog).

Je veux dire, bien sûr - vous pourriez toujours simplement migrer vos articles plus tard lorsque ces plateformes deviennent trop spammeuses. Mais la migration peut être un énorme casse-tête. (Et oui - je parle d'expérience.)

> "La possession est neuf dixièmes de la loi." - Un éminent avocat en propriété intellectuelle de la Silicon Valley à qui j'ai parlé

## Raison n°2 : Hashnode est conçu en pensant aux développeurs.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Write_Blog_Post-1.jpg)
_Un aperçu de la mise en évidence de la syntaxe Python de Hashnode sur mon article de blog Hashnode_

Vous pouvez taper en utilisant le markdown. Et vos extraits de code obtiennent également une mise en évidence de la syntaxe.

Toutes les images que vous téléchargez sont mises en cache dans le CDN de Hashnode pour plus de rapidité, donc vous ne faites pas de hot-linking ou ne dépendez pas de CDN qui pourraient être bloqués dans certains pays (comme ceux de Google ou de Facebook).

### Raison n°3 : Hashnode distribuera votre article à travers son réseau afin que vous puissiez obtenir plus de lecteurs

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Popular_Stories_-_Hashnode.png)
_Mon article de blog Hashnode apparaissant dans le fil d'actualités algorithmique mondial de Hashnode_

De nombreux auteurs de Hashnode bloguent sur leurs propres domaines personnels. Mais leurs articles apparaissent toujours automatiquement sur le site web de Hashnode dans ses fils d'actualités algorithmiques.

Cela signifie que votre blog commencera avec un public de base que vous pourrez faire croître à partir de là.

## Autres raisons pour lesquelles les blogs Hashnode sont meilleurs :

* Vous possédez vos propres données.
* Vous pouvez personnaliser votre blog Hashnode bien plus que la plupart des autres sites de blogging ne le permettent.
* Le blog Hashnode est gratuit. Vous n'avez même pas besoin de payer pour votre propre serveur ou pour des appels de fonctions serverless.
* Hashnode crée automatiquement un certificat SSL pour vous et le maintient à jour pour vous.

## OK - alors comment configurer un blog Hashnode ?

La bonne nouvelle est que c'est assez simple. Vous pouvez créer le blog en allant sur [https://hashnode.com/](https://hashnode.com/) et en vous connectant.

Vous devez simplement choisir un nom et vous êtes prêt à partir. Ensuite, vous pouvez revenir pour composer votre premier article après avoir configuré votre domaine.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Claim_your_blog_-_Hashnode.png)
_Le flux de création de blog Hashnode_

Votre blog Hashnode obtiendra immédiatement un sous-domaine hashnode.dev.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Devblog_-_Hashnode-1.png)
_Ce que vous voyez après avoir créé votre blog Hashnode et avant de l'avoir configuré._

Après avoir créé votre blog Hashnode, vous verrez un écran comme celui-ci. Entrez votre nom de domaine (avec votre sous-domaine si vous en utilisez un) et cliquez sur "mettre à jour". Ensuite, cliquez sur "Accéder au tableau de bord" pour le configurer.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Dashboard_-_Quincy_Larson_s_Blog.jpg)

Il existe de nombreuses façons de personnaliser votre blog Hashnode. Mais aujourd'hui, nous allons nous concentrer uniquement sur sa mise en ligne sur votre propre domaine.

Hashnode recommande d'utiliser un sous-domaine pour cela afin que vous puissiez accéder à leur CDN mondial et à leur mise en cache de bord, c'est donc ce que nous allons faire dans ce tutoriel.

Si vous n'avez pas encore acheté de domaine, vous pouvez le faire. Je recommande de choisir un nom de domaine où vous pouvez acheter le même nom pour .com, .org et .net, car ce sont les "trois grands" domaines de premier niveau originaux qui existent depuis les années 1990. (Avant [la grande ruée vers l'or des TLD](https://www.zdnet.com/article/new-top-level-domains-a-money-grab-and-a-mistake-paul-vixie/).)

Vous n'avez besoin de configurer votre blog Hashnode que pour l'un de vos domaines. Vous pouvez ensuite rediriger vos autres domaines vers celui-ci.

Voici comment vous devez configurer votre DNS. Notez que ceci est le tableau de bord DNS de NameCheap, mais la plupart des tableaux de bord seront similaires, et tous auront une option CNAME :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Advanced_DNS.png)
_Une image de mon tableau de bord de nom de domaine personnel sur Namecheap. Le sous-domaine du blog pointe vers mon blog Hashnode et les domaines www et racine redirigent vers mon compte Twitter personnel._

Créez un enregistrement CNAME et définissez l'hôte sur ce que vous voulez que votre sous-domaine soit (j'ai choisi `blog`).

Ensuite, définissez sa valeur sur `hashnode.network`

Hashnode gérera l'émission de votre certificat SSL pour vous, donc vous obtiendrez automatiquement un joli `https` au début de l'URL de votre blog. ?

J'ai défini le TTL à 1 minute pour qu'il se rafraîchisse plus rapidement, mais vous n'aurez peut-être pas à faire cela.

Presto. Vous pouvez aller sur `https://[votre sous-domaine].[votre domaine].[votre TLD]` et voir votre blog Hashnode.

Par exemple, mon blog Hashnode est à [https://blog.quincylarson.com](https://blog.quincylarson.com).

## Vous avez terminé.

Je vous avais dit que c'était rapide.

Maintenant, vous pouvez utiliser l'éditeur markdown de Hashnode pour créer votre premier article de blog.

Bon blogging.