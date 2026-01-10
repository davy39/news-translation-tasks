---
title: Comment et pourquoi vous devriez construire des appareils Internet des objets
  avec Node.js
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2020-02-13T14:54:48.000Z'
originalURL: https://freecodecamp.org/news/iot-and-node-js-how-to-catch-the-opportunity
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/Title_Images__1_-min.png
tags:
- name: iot
  slug: iot
- name: node
  slug: node
- name: Node.js
  slug: nodejs
seo_title: Comment et pourquoi vous devriez construire des appareils Internet des
  objets avec Node.js
seo_desc: 'In this article, we will discuss why and how you can use Node.js for the
  server-side of your Internet of Things (IoT) devices.

  Understand the business opportunity

  In 2019, the market revenue of IoT reached $212 billion. There are about 26.66 billion
  ...'
---

Dans cet article, nous discuterons de pourquoi et comment vous pouvez utiliser Node.js pour le côté serveur de vos appareils Internet des objets (IoT).

## Comprendre l'opportunité commerciale

En 2019, le [<ins>chiffre d'affaires du marché de l'IoT</ins>](https://www.statista.com/topics/2637/internet-of-things/) a atteint 212 milliards de dollars. Il y a environ 26,66 milliards d'appareils IoT connectés dans le monde, et ce nombre devrait atteindre 75,44 milliards d'ici 2025.  

Les Nations Unies estiment qu'en février 2020, la [<ins>population mondiale</ins>](https://www.worldometers.info/world-population/) est actuellement de 7,7 milliards de personnes. Un simple calcul nous indique que la personne moyenne possède environ 3 à 4 appareils IoT. En avez-vous un ? Peut-être une smartwatch ? Une smart TV ? Ou une voiture intelligente ?

En outre, la population devrait atteindre 8,1 milliards de personnes en 2025. Le même calcul nous montre qu'en 2025, une personne moyenne aura de 9 à 10 appareils intelligents en sa possession. 

Voyez-vous où je veux en venir ? Voulez-vous rejoindre cette niche de marché lucrative et faire de votre appareil IoT l'un de ces 9 à 10 ?

![Statistiques récupérées de Statista et des Nations Unies.](https://images.ctfassets.net/6xhdtf1foerq/6WhTKrEU5mebpDRnrSEexi/064db656bf882e4da1aff24eedcc6095/mHealth_revenues_reached__23_billion_in_2017__3_.png?fm=png&q=85&w=1000)
_Statistiques récupérées de Statista et des Nations Unies._

## Choisir le bon framework

Le côté client d'un appareil IoT est représenté par le matériel lui-même. Il est programmé avec C, C++, ou Lua – des langages de programmation de bas niveau et difficiles. Mais il n'y a pas grand-chose que vous puissiez faire à ce sujet en raison des limitations matérielles. 

Avec des performances élevées, les utilisateurs d'appareils IoT privilégient un faible coût et une efficacité énergétique. Ainsi, au moins pour l'instant, vous devriez continuer à travailler avec des langages de bas niveau.

D'autre part, le côté serveur des applications IoT vous offre plus de liberté de choix. Ici, vous n'êtes pas limité par le matériel, donc vous pouvez choisir n'importe quel langage de codage et framework que vous préférez. 

Je crois que le bon choix est Node.js. Voici pourquoi.

### Node.js est rapide et performant

Tout d'abord, tout appareil IoT travaille constamment avec des données dynamiquement changeantes. Cela signifie que vous avez besoin d'un framework capable de gérer des applications en temps réel et des flux de données lourds. 

Node.js est construit sur le moteur V8 JS de Google, qui est hautement efficace et parfaitement scalable. Grâce à cette fonctionnalité, **Node.js est le framework numéro un à utiliser avec les applications et plateformes en temps réel.** Les données constamment changeantes ne sont pas non plus un défi pour lui.

### Node.js est facile à intégrer avec les protocoles IoT

Les applications IoT utilisent activement un protocole de messagerie basé sur la publication-abonnement, MQTT. À son tour, pour le transport et l'encapsulation, ce protocole utilise WebSockets. **MQTT et WebSockets sont bien supportés et facilement intégrés avec Node.js.**

### Les modules Node.js facilitent le développement IoT

**Node.js est augmenté avec npm, le Node Package Manager, qui propose de nombreux modules IoT utiles.** Il y a environ 80 packages pour Intel IoT Edison, Arduino, ou Raspberry Pi. De plus, il propose plus de 30 packages pour différents capteurs, balises, et autres outils. 

C'est pourquoi le <ins>[développement de l'Internet des objets](https://keenethics.com/services-internet-of-things)</ins> est plus simple et plus rapide avec les modules IoT Node.js.

### Node.js est efficace en ressources et scalable

En général, les développeurs préfèrent travailler avec Node.js car il ne nécessite pas beaucoup de ressources. Le CPU et la RAM ne sont pas surchargés. 

De plus, Node.js est hautement scalable, ce qui est absolument nécessaire pour la plupart des entreprises modernes.

## Méfiez-vous des défis

Entrer dans la niche de l'IoT peut vous mener sur la voie du succès. Il n'est donc pas surprenant qu'il y ait beaucoup de défis et de pièges qui vous attendent sur votre chemin – le succès n'est jamais facile à atteindre. Et le premier et principal défi dont vous devez être conscient est la sécurité. 

La sécurité est l'un des principaux problèmes dans la sphère de l'IoT, et l'un des premiers pièges sur lesquels vous trébucherez. Alors, que devez-vous faire ?

### Authentification sécurisée

Commençons par l'authentification. Il existe de nombreux outils pour l'authentification dans Node.js : tokens, JSON web tokens, Auth0, et ainsi de suite. Chacun a ses avantages et ses inconvénients. Pour commencer, vous devriez les examiner du point de vue de l'IoT.

**D'une part, les tokens sont efficaces mais pas 100 pour cent sûrs.** Ils sont un moyen cool de configurer l'authentification car ils vous permettent d'identifier un utilisateur spécifique et de décider s'il faut lui accorder ou lui refuser l'accès. Un token peut être chiffré avec n'importe quel algorithme. 

Cependant, le matériel (scanners, capteurs, hubs, ou autres objets IoT) doit stocker ce token ou les données de login/mot de passe dans le firmware. Cela signifie que les attaquants peuvent voler le token s'ils ont un accès physique au matériel. La même histoire s'applique pour JWT ou Auth0.

**D'autre part, nous pouvons utiliser n'importe quel outil pour l'authentification côté serveur.** Vous pouvez facilement intégrer n'importe quel outil d'authentification sur la plateforme Node.js. 

Il existe de nombreux packages npm qui vous permettent de le faire manuellement : Auth0, Passport, et JWT. Il existe également des packages pour l'intégration avec les services IoT cloud : @azure-iot/authentication, aws-iot-device-sdk, et ainsi de suite.

### Requêtes HTTP sécurisées

Ensuite, soyez prudent avec les requêtes HTTP de vos appareils IoT. Vous devez vérifier si vous recevez une requête d'un appareil IoT approprié. 

Tout d'abord, vous devez implémenter HTTPS avec vos appareils IoT. Le matériel n'est pas un navigateur et vous devez implémenter HTTPS manuellement sur celui-ci. Pour le côté serveur, vous pouvez soit le faire manuellement, soit utiliser un hébergement avec une configuration HTTPS et des certificats. 

Dans Node.js, il est assez facile à implémenter :

```
const express = require('express');
const https = require('https');
const http = require('http');
const fs = require('fs');
const options = {
  key: fs.readFileSync('path/to/your/key.pem'),
  cert: fs.readFileSync('path/to/your/certificate.cert')
};
const app = express();
http.createServer(app).listen(80);
https.createServer(options, app).listen(443);
```

HTTPS utilise les protocoles SSL ou TLS pour le chiffrement des données. Cependant, pour être sûr que vous avez reçu une requête du serveur ou du client nécessaire, utilisez un chiffrement de données supplémentaire. Par exemple, voici comment vous pouvez utiliser une signature :

```
const fetch = require('node-fetch');
const verifier = crypto.createVerify('RSA-SHA1')
const SIGNATURE_FORMAT = 'base64';
//vérifiez si c'est une URL de confiance pour votre certificat
const trustedUrl = 'https://trustedUrl/'
const isTrustedUrl = trustedUrl.match(url);
If (isTrustedUrl) {
verifier.update(req.body, 'utf8')
	fetch(isTrustedUrl)
    .then(certificate => {
	// vérifier la signature
const isValidSignature = verifier.verify(certificate, reg.header.signature, SIGNATURE_FORMAT);
   })
    .catch(err => console.log(err));
}
```

Pour résumer cette partie :

1. Tout d'abord, vous devez vérifier l'URL de confiance de votre certificat.
2. Ensuite, vous signez un corps de requête avec la clé publique de votre certificat.
3. Enfin, vous comparez le corps signé avec la signature des en-têtes.

Il est extrêmement important de savoir que vous recevez des requêtes des appareils appropriés et que vous ne faites pas face à une attaque de l'homme du milieu.

## Découvrez ces exemples

### [<ins>Asama</ins>](https://asama.tech/ips/eng) – suivre le mouvement de vos employés

![asama](https://images.ctfassets.net/6xhdtf1foerq/3RxIwnrJoPHrRqGfleU4gT/4072f4db0e1214a3c3bd8088d9cd9ced/Screen_Shot_2019-10-23_at_3.25.42_PM.png?fm=png&q=85&w=1000)

Asama est un système de micro-localisation, qui utilise des smartwatches et des balises Bluetooth pour suivre le mouvement et l'activité des employés. Les balises transmettent un signal régulier. 

Selon ces signaux, la smartwatch définit la localisation d'un employé. La smartwatch analyse également si la bonne personne la porte et si l'employé dort ou travaille.

![Balise Asama](https://images.ctfassets.net/6xhdtf1foerq/4PtS0ph8qnZrL8tENAIsqW/b82c319d1fd95b0e8c0cbd91e6ba7f85/Screen_Shot_2019-10-23_at_3.11.59_PM.png?fm=png&q=85&w=1000)

![Suiveur Asama](https://images.ctfassets.net/6xhdtf1foerq/3757frFf2tQj7UBhOJsgXJ/b5edeb696b4944f36e980fb24dc036ed/Screen_Shot_2019-10-23_at_3.12.09_PM.png?fm=png&q=85&w=1000)

Les données sont ensuite transmises à l'application mobile, qui est installée et configurée sur le téléphone de l'employeur. Le système est alimenté par Node.js dans l'IoT.

De cette manière, les managers peuvent suivre leurs employés en temps réel, trouver la personne dont ils ont besoin immédiatement, et optimiser l'espace de travail. De plus, à la fin de la semaine, l'employeur reçoit un rapport détaillé sur l'activité des employés. Tout cela aide à améliorer les performances et la productivité de l'entreprise.

Cette solution peut ne pas convenir à une entreprise avec un petit bureau et des horaires flexibles. Pourtant, elle fonctionne parfaitement pour les usines industrielles, les chantiers de construction, les fabriques, les entrepôts, les centres commerciaux, les supermarchés, les hôtels, les agences de sécurité, les restaurants, ou les magasins. 

Elle est bien adaptée partout où vous, en tant qu'employeur, devez savoir si les employés arrivent trop tard ou partent trop tôt, sont absents du lieu de travail, ne travaillent pas activement tout au long de la journée, ou ne suivent pas les itinéraires et les horaires.

![clients asama](https://images.ctfassets.net/6xhdtf1foerq/1uoPqMXKlAZ1gG27fiy41Y/f406960d98805a8f747f130de2f4c9bf/Screen_Shot_2019-10-23_at_3.34.51_PM.png?fm=png&q=85&w=1000)

### [<ins>PREE</ins>](https://keenethics.com/project-pree) – retrouver vos affaires

PREE est un système de balises BLE et de logiciels mobiles qui aide les gens à arrêter de perdre leurs affaires. C'est un sauveur pour ceux qui oublient souvent leur téléphone, leur sac, leurs clés, leur portefeuille, ou tout autre objet de valeur. 

L'utilisateur peut voir la localisation de son objet en temps réel et la partager avec des contacts de confiance. Une fois que l'objet est hors de portée, ils recevront une notification, et il en sera de même pour leurs amis ou membres de la famille. Il ne spamme pas les autres avec des notifications lorsqu'elles ne sont pas nécessaires – par exemple, à la maison, l'utilisateur peut les mettre en sourdine pour une certaine zone.

Ce système Internet des objets est construit avec [<ins>Node.js</ins>](https://keenethics.com/services-web-development-node), [<ins>Express</ins>](https://keenethics.com/tech-back-end-express), et [<ins>Mongo</ins>](https://keenethics.com/tech-data-base-mongo) pour le backend et Ionic avec [<ins>Cordova</ins>](https://keenethics.com/tech-apps-cordova) pour le frontend. La combinaison de ces frameworks garantit la meilleure expérience utilisateur.

![PREE](https://images.ctfassets.net/6xhdtf1foerq/5egLeuuCpQFl0PFhtVdOn1/addd7e1d99ccd0b00dfe817db5c2c738/Screen_Shot_2019-10-23_at_3.42.38_PM.png?fm=png&q=85&w=1000)

## Validez votre idée

Une fois que vous avez une idée pour un produit IoT, commencez par la valider. Vous pouvez le faire de deux manières :

* Engagez une équipe de validation d'idée, qui vous aidera à tester la viabilité de votre produit avant d'investir dans le développement, ou
* Engagez une équipe de conception et de développement de logiciels, qui lancera un processus de [<ins>découverte de produit</ins>](https://keenethics.com/blog/product-discovery) approfondi.

## Postscriptum

Je voudrais envoyer un énorme merci à Volodya Andrushchak, le gourou de l'IoT chez KeenEthics, pour sa contribution et pour avoir essentiellement insufflé la vie à cet article.

Si vous avez apprécié l'article, vous devriez définitivement lire davantage sur Node.js : [Quels sont les avantages de Node.JS ?](https://keenethics.com/blog/what-are-the-advantages-of-node-js) ou [NodeJS vs Python : Comment choisir la meilleure technologie pour développer le backend de votre application web](https://keenethics.com/blog/nodejs-vs-python).

L'article original publié sur le blog de KeenEthics peut être trouvé ici : [IoT et Node.JS : Comment saisir l'opportunité ?](https://keenethics.com/blog/iot-and-node-js)