---
title: Comment les développeurs non-chinois peuvent exploiter les 1,1 milliard d'utilisateurs
  actifs mensuels de WeChat
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T17:24:26.000Z'
originalURL: https://freecodecamp.org/news/how-non-chinese-developers-can-leverage-wechats-1-1b-monthly-active-users-285083836bb9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-YhMcu5J_3HtuxLOJOJgWg.jpeg
tags:
- name: china
  slug: china
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: WeChat
  slug: wechat
seo_title: Comment les développeurs non-chinois peuvent exploiter les 1,1 milliard
  d'utilisateurs actifs mensuels de WeChat
seo_desc: 'By William Kwan

  Over a million WeChat Mini-Programs have been published since the platform launched
  two years ago. By comparison, it took the App Store a decade to reach two million
  apps.

  The average WeChat user spends 66 minutes a day on WeChat. Min...'
---

Par William Kwan

Plus d'un million de Mini-Programmes WeChat ont été publiés depuis le lancement de la plateforme il y a deux ans. En comparaison, il a fallu une décennie à l'App Store pour atteindre deux millions d'applications.

L'utilisateur moyen de WeChat passe **66 minutes par jour sur WeChat**. Les Mini-Programmes émulent l'expérience d'une application mobile légère, sans nécessiter que l'utilisateur quitte WeChat ou attende un long téléchargement. Cela accélère l'intégration, à la fois en ligne (les Mini-Programmes sont principalement accessibles via le partage social) et hors ligne (généralement via des codes QR).

L'idée que l'on peut obtenir plus d'utilisateurs en contournant le processus de téléchargement a été discutée dans la scène technologique occidentale. À peu près au même moment où la plateforme Mini-Programme a été lancée, nous avons suivi le train de la hype pour les Chatbots Messenger. Android Instant a trouvé quelques cas d'utilisation de niche, mais n'a jamais vraiment décollé.

En tant que développeur logiciel canadien d'origine chinoise, je ne pense pas que nous devrions adopter cette expérience utilisateur tout-en-un ici. Les sites web optimisés pour mobile et les applications mobiles natives couvrent déjà tous les cas d'utilisation importants.

Mais en Chine, WeChat a été l'application monolithique pour tout, bien avant l'arrivée des Mini-Programmes. Tout, de la réservation d'un taxi au paiement d'un repas, en passant par la connexion avec des inconnus à proximité, se fait via WeChat. Les Mini-Programmes sont l'évolution naturelle, créant une plateforme semi-ouverte dans un pays où le gouvernement a historiquement bloqué les concurrents étrangers.

Des marques occidentales emblématiques en Chine ont déjà commencé à passer des applications natives aux Mini-Programmes. Des chaînes de restauration rapide comme McDonald's et KFC vous permettent de commander de la nourriture et de réclamer des coupons dans leur Mini-Programme. Des marques de luxe comme [Gucci et Burberry créent des jeux et des promotions](https://jingdaily.com/burberry-wechat-mini-program/) pour commercialiser leurs produits.

De nombreux Mini-Programmes sont conçus pour compléter les entreprises locales chinoises telles que les magasins, les restaurants et les hôtels. Pour les Mini-Programmes axés sur la technologie, les jeux sont la catégorie leader. Plusieurs moteurs de jeu offrent un support pour les Mini-Programmes, y compris [Cocos](https://docs.cocos.com/creator/manual/en/publish/publish-wechatgame.html).

Mais la plateforme est également un terrain fertile pour les startups technologiques. La plus notable est Pinduoduo, l'application d'achat groupé qui est devenue publique aux États-Unis en juillet 2018 avec une valorisation de 23,8 milliards de dollars et cherche actuellement à lever 1,5 milliard de dollars supplémentaires seulement six mois plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nzQ2FFx8FyU8Aw05lup4ZQ.png)
_Crédit image : GGV Capital_

J'ai travaillé récemment sur un Mini-Programme, et comme je n'ai jamais appris à lire le chinois (malgré une enfance de disputes de mes parents), surmonter les barrières linguistiques et culturelles est vraiment difficile. Non seulement une grande partie de la documentation de WeChat est uniquement en chinois, mais les logiciels chinois ont également des normes différentes pour l'expérience utilisateur. Il ne suffit pas de traduire une application destinée au marché occidental.

De plus, il y a des défis techniques impliqués :

* Les Mini-Programmes sont limités à 10 Mo pour garantir un téléchargement rapide
* L'accès au matériel est limité à ce que WeChat fournit via leur API (notamment, vous ne pouvez pas utiliser le NFC)
* Les liens vers des sites web ne sont pas autorisés (Tencent veut que les utilisateurs restent sur WeChat, et uniquement sur WeChat)

Malgré les obstacles, cette opportunité est trop grande pour être ignorée. Les Chinois sont les utilisateurs de médias sociaux les plus actifs au monde, et ils adorent déjà les produits occidentaux de haute qualité, tout comme nous admirons la fabrication japonaise. « Made in China » est ironiquement une mauvaise façon de promouvoir un produit en Chine. Les startups technologiques occidentales pourraient utiliser cela à leur avantage, mais presque aucune d'entre elles n'adopte une stratégie « China-first ».

Si vous souhaitez être l'un des rares développeurs courageux à tenter votre chance sur le marché chinois, j'ai créé ce tutoriel pour vous apprendre à créer votre premier Mini-Programme. Si vous êtes familiarisé avec le développement web full stack JavaScript, vous apprendrez rapidement la pile technologique. Elle se compose d'un client et d'un serveur JavaScript, d'une version modifiée de HTML/CSS et d'une base de données JSON.

Si vous avez trouvé le tutoriel utile, j'adorerais créer plus de contenu comme celui-ci et construire une communauté pour les développeurs WeChat anglophones. N'hésitez pas à poser toutes vos questions sur le développement WeChat dans les commentaires et je ferai de mon mieux pour vous aider !