---
title: Comment utiliser Arduino pour vérifier le statut de réponse de votre serveur
  web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T21:13:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-arduino-to-check-your-web-servers-response-status-9e47e02a61cc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bQ91iaTCYt1SEHw-S3Rmxg.jpeg
tags:
- name: arduino
  slug: arduino
- name: Electronics
  slug: electronics
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment utiliser Arduino pour vérifier le statut de réponse de votre serveur
  web
seo_desc: 'By Harshita Arora

  Last year, I created Crypto Price Tracker (an app which was acquired by Redwood
  City Ventures this year). A back end member of my team had been using an Arduino
  setup to check web server response statuses continuously to get updates...'
---

Par Harshita Arora

L'année dernière, j'ai créé [Crypto Price Tracker](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8) (une application qui a été acquise par Redwood City Ventures cette année). Un membre de l'équipe backend utilisait un montage Arduino pour vérifier en continu les statuts de réponse du serveur web afin de recevoir des mises à jour en temps réel. J'ai trouvé ce montage assez utile et intéressant.

J'ai fait des recherches à ce sujet et j'ai recréé le montage pour moi-même. Dans cet article, je vais vous montrer comment vous pouvez le construire vous-même.

#### Ce dont vous avez besoin :

1. [Arduino Uno](https://store.arduino.cc/usa/arduino-uno-rev3)
2. [Bouclier Ethernet pour Arduino](http://a.co/d/cLNijNF) (pour connecter l'Arduino à Internet)
3. Câble Ethernet
4. Câble USB 2.0 de type A/B (câble d'alimentation pour Arduino)
5. Câbles de pontage mâle-mâle (x2)
6. Plaque d'essai
7. LED (x1, n'importe quelle couleur)
8. Résistance (x1, >100 ohms)

#### Installation

1. Montez/Insérez le bouclier Ethernet sur l'Arduino.
2. Insérez l'extrémité positive (plus longue) de la LED dans l'emplacement 6a de la plaque d'essai et l'extrémité négative (plus courte) dans l'emplacement 5a.
3. Insérez une extrémité de la **résistance** dans l'emplacement 1b de la plaque d'essai et l'autre dans l'emplacement 5b.
4. Insérez une extrémité du **premier** câble de pontage dans l'emplacement 1e de la plaque d'essai. Insérez l'autre extrémité dans l'emplacement GND du bouclier Ethernet.
5. Insérez une extrémité du **deuxième** câble de pontage dans l'emplacement 6e de la plaque d'essai. Insérez l'autre extrémité dans l'emplacement de broche 2 du bouclier Ethernet.
6. Connectez le **câble Ethernet** de votre routeur à votre bouclier Ethernet.

Voici à quoi ressemble mon montage :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qbA3umNhKDiZy1bBrQZy1g.jpeg)

7. Ouvrez une interface de ligne de commande sur votre machine et vérifiez et notez votre passerelle par défaut. Cela peut être fait en utilisant la commande `ipconfig` sur Windows ou la commande `netstat -nr | grep default` sur Linux/Mac.

8. Téléchargez et installez l'IDE Arduino si ce n'est pas déjà fait.

9. Ouvrez l'IDE et allez dans Fichier -> Exemples -> Ethernet -> WebClientRepeating. Vous devriez voir le code suivant :

10. Modifiez la **ligne 37** pour qu'elle soit une adresse IP dans la plage (1-254) de votre IP de passerelle par défaut. Par exemple, si ma passerelle par défaut est 10.0.0.1, alors je peux utiliser une adresse IP de 10.0.0.2 à 10.0.0.254. Il est cependant important de s'assurer que l'IP que vous utilisez n'entre pas en conflit avec d'autres adresses IP sur votre réseau.

Pour cet exemple, j'ai modifié la ligne de code pour qu'elle soit :

`**IPAddress ip(10, 0, 0, 2);**`

11. Changez le DNS dans la **ligne 40** pour qu'il soit **8.8.8.8** (c'est le DNS public de Google et c'est juste quelque chose que je préfère, vous pouvez utiliser un DNS que vous préférez).

Pour cet exemple, j'ai modifié la ligne de code pour qu'elle soit :

`**IPAddress myDns(8, 8, 8, 8);**`

12. Changez l'URL dans la **ligne 45** pour qu'elle corresponde à l'URL de votre serveur web. Si vous souhaitez utiliser une adresse IP à la place, alors commentez la **ligne 45** et décommentez la **ligne 46**. Puisque j'utilise un serveur web que j'héberge localement, pour cet exemple, j'utiliserai une adresse IP.

Pour cet exemple, j'ai modifié la ligne de code pour qu'elle soit :

`//char server[] = "[www.arduino.cc](http://www.arduino.cc)";`  
`IPAddress server(127,0,0,1);`

Notez que le port ou le chemin ici n'est pas encore important. Seule l'adresse IP est nécessaire. Si vous souhaitez changer le port utilisé pour la requête GET, vous pouvez le modifier à la **ligne 94**.

Pour cet exemple, j'ai hébergé mon serveur web local sur le port 3000. Ainsi, je vais modifier le code à la **ligne 94** pour qu'il ressemble à ceci :

`if (client.connect(server, 3000)) {`

13. Modifiez la requête **GET** qui est pré-écrite aux **lignes 97 - 100** pour suivre ce modèle :

`client.println("GET /path_to_url HTTP/1.1");`  
`client.println("Host: 127.0.0.1");`  
`client.println("Connection: close");`  
`client.println();`

14. Nous pouvons maintenant commencer à programmer le comportement de la LED en fonction du statut et de la réponse du serveur web. Pour ce faire, nous devons d'abord déclarer la broche que nous utilisons pour la LED sur notre bouclier Ethernet.

Ajoutez la ligne de code suivante après les deux premières déclarations **include** du programme :

`int LED = 2;`

15. Ajoutez les lignes de code suivantes au début de la fonction _setup()_.

`pinMode(LED, OUTPUT);`

`digitalWrite(LED, LOW); // le programme commence avec la LED éteinte`

16. Ajoutez la ligne de code suivante après la ligne de requête GET que nous avons précédemment modifiée :

`digitalWrite(LED, LOW);`

17. Enfin, ajoutez cette ligne de code au début de l'instruction **else** de la même condition :

`digitalWrite(LED, HIGH);`

Et voilà, vous avez terminé !

Téléchargez le programme sur votre Arduino. Ouvrez le moniteur série depuis la partie supérieure droite de l'IDE et observez la réponse. Si votre serveur ne répond pas, la LED s'allume, sinon, la LED reste éteinte :)

Vous pouvez consulter mon code final [ici](https://gist.github.com/harshitaarora/1e096fe2ba7915964742e3f324f15184).

#### Vérification de la réponse

Si vous souhaitez également **valider** la réponse que vous recevez de votre serveur web, vous pouvez les ajouter à l'intérieur de la condition suivante du programme.

`if (client.available()) {`  
`char c = client.read();`  
`Serial.write(c);`  
`}`

La variable **c** est l'endroit où la réponse est stockée. Vous pourriez la vérifier comme ceci :

`if (client.available()) {`

`char c = client.read();`  
`if(c == "arduino est génial"){`  
 `digitalWrite(LED, LOW); // réponse correcte`  
`}`  
`else{`  
`digitalWrite(LED, HIGH); // mauvaise réponse`  
`}`  
`Serial.write(c);`  
`}`

Notez que, si vous essayez de faire cela, il est préférable de supprimer l'instruction digitalWrite après la requête GET. Selon votre réponse, vous devrez peut-être analyser des valeurs JSON. Il existe plusieurs façons de faire cela et de nombreux tutoriels/articles à ce sujet ! Assurez-vous de les consulter !

Amusez-vous bien ! N'hésitez pas à m'envoyer un email à `harshita (at) harshitaapps.com` pour toute question, commentaire ou idée !

Assurez-vous de consulter l'application [Crypto Price Tracker](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8) si vous êtes intéressé/investi dans les cryptomonnaies ! :)