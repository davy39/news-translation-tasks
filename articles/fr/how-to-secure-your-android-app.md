---
title: Comment sécuriser votre application Android – Quatre bonnes pratiques de sécurité
  que tout développeur Android doit connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-28T16:01:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-your-android-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/android-app-coding-security.jpg
tags:
- name: android app development
  slug: android-app-development
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
seo_title: Comment sécuriser votre application Android – Quatre bonnes pratiques de
  sécurité que tout développeur Android doit connaître
seo_desc: "By Andrej Kovacevic\nIf you've been following the news lately, you may\
  \ have noticed a worrisome tech trend. The frequency and severity of cybersecurity\
  \ attacks are exploding. \nWe've seen news of a sprawling hack involving the SolarWinds\
  \ management pla..."
---

Par Andrej Kovacevic

Si vous avez suivi l'actualité récemment, vous avez peut-être remarqué une tendance technologique préoccupante. La fréquence et la gravité des cyberattaques explosent. 

Nous avons vu des nouvelles d'un piratage massif impliquant la plateforme de gestion SolarWinds. Cette attaque a peut-être compromis les systèmes de [plus de 18 000 clients de SolarWinds](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack). 

Ensuite, nous avons découvert qu'une faille zero-day dans le serveur de messagerie Exchange omniprésent de Microsoft a provoqué le piratage des systèmes affectés [plus rapidement que les experts ne pouvaient compter](https://www.zdnet.com/article/microsoft-exchange-server-attacks-theyre-being-hacked-faster-than-we-can-count-says-security-company/).

Pour le développeur logiciel moyen (comme moi), c'est tout simplement effrayant. Après tout, si de grandes entreprises multimilliardaires comme celles-ci ne sont pas à l'abri des piratages désastreux, quelles sont les chances que mon code reste en sécurité ?

Eh bien, il s'avère qu'il y a de bonnes et de mauvaises nouvelles sur ce front. 

La bonne nouvelle est que les types d'attaques à grande échelle que nous avons vues récemment sont justement cela – à grande échelle. En d'autres termes, les types de groupes (ou États-nations) qui peuvent mener des attaques comme celles-ci ne se soucient pas vraiment des petits projets logiciels sur lesquels je travaille.

Mais la mauvaise nouvelle est la suivante : il y a beaucoup de pirates à petite échelle qui seront plus que heureux de rendre votre vie de développeur misérable. Et ils le feront si vous les laissez faire. 

Mais vous pouvez faire quelque chose à ce sujet. Vous pouvez faire de votre mission de mettre autant d'obstacles que possible sur leur chemin. En couvrant les angles d'attaque les plus probables sur votre logiciel, vous pouvez augmenter les chances qu'un attaquant potentiel passe votre code et cherche une cible plus facile.

Maintenant, j'ai déjà écrit abondamment sur une variété de sujets de sécurité logicielle. Mais parce que je travaille actuellement sur une application Android – et [parce qu'Android est une cible favorite des pirates](https://thehackernews.com/2020/05/stranhogg-android-vulnerability.html) – j'ai décidé de partager quatre des principes de sécurité les plus importants pour les applications Android que vous pouvez inclure dans vos applications sur la plateforme. Je les fais une priorité de mes efforts de sécurité, et vous devriez en faire autant. 

## 1. Protégez la couche de transport de votre application

L'une des premières choses qu'un attaquant recherchera lors du ciblage d'une application Android est de voir s'il peut intercepter une partie des données passant entre celle-ci et le backend de votre serveur. 

En écoutant ces communications, ils peuvent en apprendre beaucoup sur votre application. Et si vous êtes vraiment malchanceux, ils pourraient même être en mesure d'utiliser les données pour découvrir comment usurper votre application et obtenir un accès inapproprié aux données côté serveur.

Ainsi, la première étape de votre effort pour sécuriser une application Android est simple : protégez sa couche de transfert de données en employant un chiffrement fort. 

Vous pouvez le faire en utilisant des protocoles comme [SSL](https://www.freecodecamp.org/news/openssl-command-cheatsheet-b441be1e8c4a/) et [TLS](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/), qui sont simples à ajouter à votre code et très difficiles à compromettre. Et une fois que vous avez une solution en place, prenez le temps de faire de la [modélisation des menaces](https://www.freecodecamp.org/news/threat-modeling-goran-aviani/) pour décider si vous avez fait assez pour protéger le trafic de votre application.

Si vous traitez des données particulièrement sensibles, vous pouvez même vouloir aller un peu plus loin et construire une solution de type VPN directement dans votre application. Si vous n'avez jamais implémenté un VPN dans une application Android auparavant, vous pouvez lire les bases de l'ajout d'un VPN [ici dans le guide du développeur Android](https://developer.android.com/guide/topics/connectivity/vpn). 

Si vous choisissez cette voie, vous pouvez même promouvoir cette fonctionnalité à vos clients (ou aux utilisateurs finaux si vous construisez quelque chose de public). Les applications VPN Android sont si courantes de nos jours que la simple mention de la fonctionnalité fera savoir aux utilisateurs que vous prenez au sérieux la sécurité de leurs données – et c'est toujours un bon bonus en termes de relations publiques.

## 2. Rendez l'authentification à toute épreuve

![Image](https://www.freecodecamp.org/news/content/images/2021/05/app-authorization-bulletproof-2fa.jpg)
_Image : thodonal / Adobe Stock_

Outre les flux de données de votre application, le prochain vecteur d'attaque le plus courant à éliminer est toute faiblesse dans ses méthodes d'authentification. 

Le problème avec cela, ce sont vos utilisateurs. Ce que je veux dire, c'est que vous devez rendre le processus d'authentification de votre application aussi sécurisé que possible sans le rendre si fastidieux que vos utilisateurs se révolteront (et si j'avais un dollar pour chaque fois qu'un client m'a demandé si la 2FA était _vraiment_ nécessaire, je serais à la retraite maintenant).

Quoi qu'il en soit, la 2FA est à la fois nécessaire et vaut la peine d'être implémentée. 

En plus de cela, vous devez également prêter attention à la manière dont vous gérez les échanges de clés. Au minimum, vous devriez utiliser le chiffrement AES pour garder ces transactions sécurisées.

Et enfin, mais non des moindres, vous devez vous assurer d'[utiliser une sécurité basée sur des jetons](https://auth0.com/learn/token-based-authentication-made-easy/) pour authentifier les requêtes légitimes de votre application vers son backend. Cela rend la réalisation de telles requêtes suffisamment difficile pour que même si un attaquant trouve un moyen de visualiser un flux de données en direct, il n'aura aucun moyen d'utiliser ces informations pour lancer une attaque.

## 3. Protégez-vous contre l'injection de code

La prochaine chose à laquelle vous devriez vous soucier est la partie publique de votre application. Parce que la plupart des applications sont interactives, elles fourniront aux utilisateurs la possibilité de saisir des données d'une manière ou d'une autre. Cela peut être par le biais de champs de saisie de texte comme des formulaires, ou par le biais de téléchargements directs de données pour échanger des éléments comme des documents et des images. 

Et chaque fois que vous ajoutez une fonctionnalité de saisie utilisateur, vous devez prendre grand soin de vous assurer que personne ne peut les utiliser contre vous.

La première façon d'aborder cela est d'utiliser une validation d'entrée appropriée. Si votre application attend un texte spécifique dans un champ, assurez-vous qu'elle n'acceptera rien d'autre. Vous pouvez le faire en ajoutant un [module de validation de texte pré-construit](https://www.simplifiedcoding.net/android-form-validation-tutorial/) ou en [construisant le vôtre](https://www.freecodecamp.org/news/form-validation-with-html5-and-javascript/) (si vous avez le temps et l'inclination). 

Si vous prévoyez de permettre à un utilisateur de télécharger des images ou d'autres fichiers spécifiques, vous devez inclure une capacité pour l'application à scanner le fichier téléchargé pour vous assurer qu'il est bien ce qu'il prétend être. 

Encore une fois, cela est possible en utilisant l'un des nombreux modules pré-construits. J'ai tendance à favoriser [JMimeMagic](https://github.com/arimus/jmimemagic) car il peut gérer une variété de types MIME, mais vous pouvez utiliser la solution qui fonctionne le mieux dans le contexte de votre projet.

## 4. Minimisez et sécurisez le stockage côté client

Enfin, mais non des moindres, vous devriez vous efforcer de construire votre application avec la plus petite empreinte de données locales possible pour accomplir la tâche. 

C'est parce que toute donnée que vous stockez sur un appareil client est hors de votre contrôle et est donc vulnérable aux menaces externes. 

Si l'appareil d'un utilisateur est compromis par une attaque qui donne accès aux données qui y sont stockées, vous pourriez involontairement donner à l'attaquant une feuille de route pour voler des informations de votre application.

Maintenant, ne stocker aucune donnée côté client est presque impossible – surtout si vous avez besoin que votre application conserve une partie ou la totalité de sa fonctionnalité hors ligne. Donc, au minimum, assurez-vous que toutes les données côté client que vous stockez restent chiffrées en tout temps. 

Et, essayez d'éliminer le stockage de toute donnée qui pourrait poser un problème si un attaquant mettait la main dessus. Des choses comme les listes de contacts, les historiques de messages ou tout type d'historique d'utilisation viennent à l'esprit.

Et au-delà du stockage, vous voudrez tester votre application pour voir si elle n'est pas vulnérable aux fuites de mémoire qui pourraient exposer des données critiques. 

Pour ce faire, vous devriez vous familiariser avec des outils comme le [OWASP Zed Attack Proxy (ZAP)](https://www.zaproxy.org/). Il vous aidera à trouver toute vulnérabilité dans l'utilisation de la mémoire de votre application avant que les attaquants ne puissent les utiliser contre vous. 

Cela peut être un peu complexe à maîtriser, mais il y a beaucoup de bonne documentation et une fantastique communauté d'utilisateurs qui vous aidera.

## Verrouillé en toute sécurité

Je souhaiterais pouvoir vous dire que toute application construite en utilisant ces quatre principes sera invulnérable à toute menace. Mais les attaquants travaillent pour trouver de nouvelles failles chaque minute de chaque jour, et à moins que vous ne fassiez de la lutte contre eux votre travail également, il est peu probable que vous trouviez une solution parfaite. 

Mais en couvrant ces principaux vecteurs d'attaque, vous rendrez au moins leur travail suffisamment difficile pour que cela ne vaudra pas la peine d'essayer (sauf si votre application contient quelque chose de grande valeur verrouillé à l'intérieur). 

Et à la fin de la journée, c'est tout ce que l'on peut vous demander en tant que développeur, à moins qu'ils ne soient prêts à vous payer grassement pour vous protéger contre chaque menace possible – et hé, ne serait-ce pas agréable ?

_Image en vedette : Arthur Shevtsov / Adobe Stock_