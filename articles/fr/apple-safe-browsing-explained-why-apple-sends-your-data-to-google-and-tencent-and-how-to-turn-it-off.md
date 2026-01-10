---
title: Explication du navigateur sécurisé d'Apple - Pourquoi Apple envoie vos données
  à Google et Tencent et comment le désactiver
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-10-15T15:53:18.000Z'
originalURL: https://freecodecamp.org/news/apple-safe-browsing-explained-why-apple-sends-your-data-to-google-and-tencent-and-how-to-turn-it-off
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ff0740569d1a4ca459d.jpg
tags:
- name: iOS
  slug: ios
- name: Security
  slug: security
seo_title: Explication du navigateur sécurisé d'Apple - Pourquoi Apple envoie vos
  données à Google et Tencent et comment le désactiver
seo_desc: If you use Safari on certain versions of iOS, then your IP address is being
  sent to Google or Tencent by default. Tencent is the Chinese equivalent of Facebook,
  who owns the popular WeChat mobile app. Tencent also works closely with the Chinese
  gover...
---

Si vous utilisez Safari sur certaines versions d'iOS, votre adresse IP est envoyée à Google ou Tencent par défaut. Tencent est l'équivalent chinois de Facebook, qui possède l'application mobile populaire WeChat. Tencent travaille également en étroite collaboration avec le gouvernement chinois. Il est possible d'empêcher vos données d'être envoyées à ces entreprises.

Les appareils envoient des données à Tencent si le code de région est défini sur la Chine continentale. Tous les autres appareils envoient des données à Google.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-59.png)
_Notification sur iPhone que vos données seront envoyées à Google et Tencent._

Voici ce qu'un porte-parole d'Apple a déclaré à propos de cette fonctionnalité dans une déclaration à _The Register_ :

> Apple protège la vie privée des utilisateurs et sauvegarde vos données avec l'avertissement de site Web frauduleux de Safari, une fonctionnalité de sécurité qui signale les sites Web connus pour être malveillants.

> Lorsque la fonctionnalité est activée, Safari vérifie l'URL du site Web par rapport aux listes de sites Web connus et affiche un avertissement si l'URL que l'utilisateur visite est suspectée de conduite frauduleuse comme le phishing. Pour accomplir cette tâche, Safari reçoit une liste de sites Web connus pour être malveillants de Google, et pour les appareils dont le code de région est défini sur la Chine continentale, il reçoit une liste de Tencent.

> L'URL réelle d'un site Web que vous visitez n'est jamais partagée avec un fournisseur de navigation sécurisée et la fonctionnalité peut être désactivée.

Bien que l'URL réelle que vous visitez ne soit pas partagée, votre adresse IP est partagée. Votre adresse IP peut révéler votre emplacement général et d'autres détails vous concernant. Elle est partagée afin de déterminer si le site Web que vous visitez est un site frauduleux.

Ces données sont partagées automatiquement par beaucoup de personnes. Safari a une part de marché aux États-Unis de plus de 50 % depuis qu'il est le navigateur par défaut sur les appareils iOS.

De plus, même si vous utilisez un navigateur tiers sur votre appareil iOS, vos données peuvent toujours être envoyées à Google et Tencent. Lorsque vous consultez une page Web depuis une application, les pages s'ouvrent dans une version du navigateur Safari. Comme de nombreuses applications ouvrent Safari depuis l'application, il est presque impossible d'éviter Safari.

Pour empêcher votre adresse IP d'être envoyée à Google et Tencent, vous devez désactiver l'"Avertissement de site Web frauduleux". Gardez à l'esprit que la désactivation de cette fonctionnalité peut vous rendre plus vulnérable à l'accès à des sites Web frauduleux.

Voici comment désactiver l'"Avertissement de site Web frauduleux" dans iOS :

1. Dans les paramètres iOS, sélectionnez "Safari".
2. Faites défiler un peu et basculez l'"Avertissement de site Web frauduleux" en position d'arrêt.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-60.png)
_Comment désactiver l'envoi de données à Google et Tencent._

### Qu'est-ce que la "Navigation sécurisée" ?

Le service "Avertissement de site Web frauduleux" utilise Google Safe Browsing et Tencent Safe Browsing. Il s'agit d'un service initialement développé par Google. Les utilisateurs rencontrent parfois des sites malveillants et des pages de phishing. Google dispose d'une grande liste de ces sites et a créé la "navigation sécurisée" pour aider à notifier les utilisateurs lorsque le site auquel ils accèdent pourrait être malveillant.

Voici comment Google fournit ce service, appelé "Update API", selon le chercheur en cryptographie [Matthew Green](https://blog.cryptographyengineering.com/2019/10/13/dear-apple-safe-browsing-might-not-be-that-safe/) :

> 1. Google calcule d'abord le hachage SHA256 de chaque URL non sécurisée dans sa base de données, et tronque chaque hachage en un préfixe de 32 bits pour économiser de l'espace.

> 2. Google envoie la base de données de hachages tronqués à votre navigateur.

> 3. Chaque fois que vous visitez une URL, votre navigateur la hache et vérifie si son préfixe de 32 bits est contenu dans votre base de données locale.

> 4. Si le préfixe est trouvé dans la copie locale du navigateur, votre navigateur envoie maintenant le préfixe aux serveurs de Google, qui renvoient une liste de tous les hachages complets de 256 bits des URL correspondantes, afin que votre navigateur puisse vérifier une correspondance exacte.

Présumément, la même méthode est utilisée par Tencent en Chine. Mais au lieu que le préfixe haché soit envoyé à Google, il est envoyé à Tencent.

Ce processus devrait être sécurisé puisque les URL réelles que vous visitez ne sont pas envoyées, seulement une version hachée de l'URL. Cependant, certains chercheurs en sécurité ont souligné qu'en analysant les centaines d'URL hachées envoyées à ce service par un seul utilisateur, il pourrait être possible de désanonymiser cet utilisateur.

Safari n'est pas le seul navigateur utilisant Google Safe Browsing. Les navigateurs Google Chrome, Firefox, Vivaldi et GNOME Web utilisent le service Google Safe Browsing. Donc, si vous ne voulez pas que vos données soient envoyées à Google, choisissez un navigateur qui n'est pas dans cette liste ou désactivez le service dans les paramètres du navigateur.

Beaucoup de gens pensent qu'il vaut la peine de partager leurs adresses IP avec Google et/ou Tencent pour obtenir une meilleure protection contre les sites malveillants. Vous devez décider par vous-même si cela vaut le risque.