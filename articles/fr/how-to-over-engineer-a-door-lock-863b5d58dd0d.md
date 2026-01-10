---
title: Comment sur-ingénier une serrure de porte
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-13T20:26:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-over-engineer-a-door-lock-863b5d58dd0d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TP9VbFU7DwDvY78ApjObtg.jpeg
tags:
- name: Iot Portal
  slug: iot-portal
- name: Cloud Solutions
  slug: cloud-solutions
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
seo_title: Comment sur-ingénier une serrure de porte
seo_desc: 'By Steven Chan

  My company’s Internet of Things (IoT) side project began when we couldn’t reset
  the door lock that we inherited from a previous tenant. It was one of those minor
  details we learned about after moving in to our new last-minute office.

  N...'
---

Par Steven Chan

Le projet secondaire sur l'Internet des Objets (IoT) de mon entreprise a commencé lorsque nous n'avons pas pu réinitialiser la serrure de la porte dont nous avions hérité d'un locataire précédent. C'était l'un de ces détails mineurs que nous avons découverts après avoir emménagé dans nos nouveaux bureaux de dernière minute.

Normalement, les gens en achètent simplement une nouvelle. Mais notre équipe était trop radine pour remplacer la serrure et personne ne voulait jamais aller répondre à la sonnette. De plus, nous sommes des ingénieurs et nous voulions bricoler un peu de matériel.

Notre objectif était d'ouvrir la porte avec un téléphone ou une technologie portable (wearable). Nous avions plusieurs options pour aborder le problème. En théorie, nous pouvions utiliser une application, une intégration dans une autre plateforme, ou n'importe quoi capable d'envoyer un signal pour déclencher la serrure.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZMY8DHIrRVUYDOEm25cW-Q.jpeg)
_Chima Open Door sur Pebble et iOS_

À ce stade de notre expérience de serrure de porte, nous avons développé des solutions pour une intégration Slack, des applications natives iOS et Android, l'Apple Watch et la Pebble. Je vais me concentrer sur l'architecture des applications mobiles. J'admets que le produit final est un peu sur-ingénié, mais nous l'adorons tout simplement !

### **_Architecture iOS et Android_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*_a0ivz5iXmx8CLBTWspoXg.png)
_L'architecture de notre projet de serrure de porte IoT_

Que se passe-t-il exactement lorsque vous appuyez sur le bouton dans notre application iOS / Android ? Une requête HTTP est envoyée au serveur cloud, qui déclenche ensuite un message vers le démon de la serrure via le serveur client, lequel indique ensuite à une carte de relais d'ouvrir la serrure.   
   
Traditionnellement, la serrure s'ouvre avec un bouton situé à côté de la porte. Mais avec la technologie moderne, les possibilités s'étendent au-delà d'un bouton physique direct. En plus du bouton physique qui déclenche le `Doorlock Daemon` dans le schéma, nous avons ajouté deux autres déclencheurs : un déclencheur basé sur le cloud et un déclencheur Bluetooth Low Energy (BLE), grâce à notre choix de matériel.  
   
Cet article se concentre sur le déclencheur basé sur le cloud, dont dépend notre application de serrure.

### Du clic sur le bouton à l'enregistrement sur le serveur Skygear.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y_5ir6hlMnHyXWrMwLA3Vg.png)

Lorsqu'un utilisateur appuie sur le bouton d'ouverture de la porte sur l'application mobile, l'application accède au serveur cloud.   
   
Deux choses se produisent dans le serveur cloud. La première est qu'un enregistrement est sauvegardé sur le serveur de notre choix, [Skygear Cloud Database](https://docs.skygear.io/guides/), qui vous permet de synchroniser vos données sur le cloud. Le serveur enregistrera le moment où l'accès à la porte est demandé.

Une fois l'enregistrement sauvegardé, cela déclenche une fonction `after_save` fournie par [Skygear Cloud Functions](https://docs.skygear.io/guides/), qui exécute notre code dans le cloud sans se soucier du déploiement du serveur.  
   
La fonction `after_save` est déclenchée après la sauvegarde d'un enregistrement. `def after_open_door_save(record, original_record, db):` est déclenchée de manière asynchrone lorsqu'un enregistrement de type `'OpenDoor'` est sauvegardé. La fonction publie un message sur le canal `'xxx-channel'`.

### Le client Node et le serveur Clojure sur Raspberry Pi

L'étape suivante consiste à créer un écouteur pour la requête. C'est là qu'interviennent le client Node et un serveur Clojure sur Raspberry Pi. Le client Node écoute le message dans le canal spécifié sur le serveur Skygear. Le serveur Clojure est le seul à avoir le droit d'accéder au circuit du Raspberry Pi 3. Ensuite, le client Node émet une requête vers le serveur Clojure dès qu'il entend un message.   
   
Voici le script pour le client Node, qui inclut le code lié à notre configuration spécifique pour Skygear. L'endpoint et la clé API servent à accéder au serveur principal sur Skygear. `skygear.on('xxx-channel', onReceiveOpenDoor)` signifie s'abonner au rappel de fonction (`onReceiveOpenDoor`) lors de la réception d'un message sur le canal `'xxx-channel'`.

Le serveur Clojure contrôle directement les entrées/sorties à usage général (GPIO) sur un Raspberry Pi. Les GPIO sont les broches du Raspberry Pi 3. Le GPIO se connecte au circuit externe qui est relié à l'aimant de la porte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d80-lFQeMHleoRI30NzgTA.png)

Voici le code Clojure montrant comment le Raspberry Pi ouvre la porte. Une fois que le serveur Clojure reçoit la requête du client Node, il ouvre la porte et la maintient ouverte pendant 3 secondes. Cependant, si une nouvelle requête arrive pendant ces 3 secondes, la porte réinitialise la minuterie pour 3 secondes supplémentaires. Lorsque le compte à rebours est terminé, la porte se verrouille à nouveau.

Une petite note en passant : Skygear utilise AWS aux États-Unis, tandis que la porte et le Raspberry Pi sont à Hong Kong. En pratique, notre requête « 芝麻開門 » (Chima Open Door) fait le tour du monde avant d'atteindre la porte.

### Pourquoi le Raspberry Pi ?

Maintenant, vous vous demandez peut-être pourquoi nous avons spécifiquement choisi le Raspberry Pi. Nous avons envisagé d'utiliser des cartes Arduino parce que nous en avions au bureau. La raison pour laquelle nous ne pouvions pas utiliser notre modèle d'Arduino spécifique était que nous voulions synchroniser les données via le SDK JS de Skygear et que cet Arduino spécifique ne peut pas configurer de serveur Node.  
   
 De plus, le Raspberry Pi est compatible avec le Bluetooth Low Energy (ce qui signifie que nous pourrions accéder à la serrure en utilisant une troisième méthode, le Bluetooth).

![Image](https://cdn-media-1.freecodecamp.org/images/1*2SCzzCP-Xf2OrwKvw4Zh1A.jpeg)
_Le Raspberry Pi basé sur Linux est compatible avec la plateforme serverless open-source d'Oursky, Skygear_

![Image](https://cdn-media-1.freecodecamp.org/images/1*c47bsti5RIuXdrNrm1YbIA.jpeg)

### Intégrations supplémentaires

Étant donné que l'application est réservée à un usage interne, nous avons lancé une commande personnalisée [Slack](http://www.slack.com/) `/chima-open-door` pour ouvrir la porte, puisque chaque membre d'Oursky a accès à [Slack](http://www.slack.com/).

Plus tard, d'autres collègues d'Oursky se sont impliqués dans ce projet et ont aidé à écrire l'application WatchOS et l'application Android publiées sur la plateforme interne. En plus d'appuyer sur le bouton à l'intérieur de l'application, nous proposons également des alternatives telles que le 3D Touch iOS, l'extension Today, un widget Android et même une intégration Pebble parce que certains de nos développeurs l'utilisent.

Et voilà ! Avant de vous lancer, il y a deux autres facteurs principaux à considérer : le flux électrique inverse (dans ce cas pour le Raspberry Pi) et la sécurité de chacune de vos intégrations. Par exemple, nous avons également intégré l'accès via une application Bluetooth avec le Bluetooth Low Energy (BLE), qui possède une authentification de type 2FA implémentée par nos soins. D'autres intégrations que vous pouvez inclure sont des notifications lorsque la porte est ouverte (sonnette, LED).  
   
 Si vous souhaitez en savoir plus sur l'un des points ci-dessus, n'hésitez pas à nous contacter !

**Lien vers le dépôt / fichiers**  
Doorlock : [https://github.com/oursky/doorlock](https://github.com/oursky/doorlock)

Je tiens à remercier mes collègues [David Ng](https://www.freecodecamp.org/news/how-to-over-engineer-a-door-lock-863b5d58dd0d/undefined), Boris ([akiroz](https://www.freecodecamp.org/news/how-to-over-engineer-a-door-lock-863b5d58dd0d/undefined)), Brian ([b壹貳參肆零零](https://www.freecodecamp.org/news/how-to-over-engineer-a-door-lock-863b5d58dd0d/undefined)), et [May Yeung](https://www.freecodecamp.org/news/how-to-over-engineer-a-door-lock-863b5d58dd0d/undefined) pour avoir travaillé respectivement sur l'application Android, l'implémentation du circuit et Clojure, l'application Pebble, et cet article de blog. Vive le travail d'équipe !

Chez Oursky, notre mission est d'aider les marques et les entrepreneurs à concrétiser leurs idées, ainsi que nos confrères développeurs — notre dernier projet Skygear ([https://skygear.io](https://skygear.io)), une plateforme serverless open source ([https://github.com/skygeario](https://github.com/skygeario)) pour les applications mobiles, web et IoT — vous aide à construire de meilleures applications plus rapidement. ✨