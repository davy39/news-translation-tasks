---
title: Comment fabriquer un voltmètre numérique avec Arduino
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-23T17:34:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-digital-voltmeter-using-arduino-b4dbf5b94d6f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Vnn6OGrwT4RHyHEwHBQI7Q.jpeg
tags:
- name: arduino
  slug: arduino
- name: Electronics
  slug: electronics
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment fabriquer un voltmètre numérique avec Arduino
seo_desc: 'By Harshita Arora

  Last Sunday, while I was explaining the basics of electronics and Arduino to my
  roommate, she challenged me to understand how a voltmeter works and build one from
  scratch just using the stuff I own already. I accepted the challenge,...'
---

Par Harshita Arora

Dimanche dernier, alors que j'expliquais les bases de l'électronique et d'Arduino à ma colocataire, elle m'a lancé le défi de comprendre comment fonctionne un voltmètre et d'en construire un à partir de zéro en utilisant uniquement le matériel que je possède déjà. J'ai relevé le défi, j'ai commencé à bidouiller, coder, tester, recoder et retester, et finalement, j'avais mon voltmètre prêt et fonctionnel à l'heure du dîner !

J'ai utilisé un Arduino Uno (pour collecter la tension en analogique et alimenter le LCD), un petit écran LCD que j'ai reçu dans mon kit de démarrage Arduino (pour afficher la tension), une plaque d'essai (pour connecter tout) et des fils de connexion.

Si vous cherchez un projet facile pour apprendre l'électronique, alors fabriquer un voltmètre numérique sera amusant. Commençons !

### **Le Circuit Électrique**

#### Étape 1

Prenez une plaque d'essai (j'ai utilisé une petite avec 30 rangées) et connectez un écran LCD à celle-ci. Ensuite, à l'aide d'un fil, connectez un fil de la broche GND (état de masse) sur l'Arduino à la charge négative sur la plaque d'essai, et un fil de la broche 5V à la charge positive. Cela fournit du courant électrique aux colonnes de la plaque d'essai, que nous pouvons maintenant connecter au LCD.

![Image](https://cdn-media-1.freecodecamp.org/images/SNHrp53F6h8pqVjr2-VY80Gs2Zhq44lZY8rU)
_Ceci est la configuration de base après l'Étape 1._

#### Étape 2

Maintenant, nous allons connecter les broches du LCD à la plaque d'essai pour pouvoir l'alimenter. Connectez la Broche 1 du LCD à une charge négative, la Broche 2 à une charge positive, la Broche 3 à une charge négative, la Broche 5 à une charge négative, la Broche 15 à une charge positive, et la Broche 16 à une charge négative. Branchez votre Arduino pour tester et voir si le LCD s'allume !

![Image](https://cdn-media-1.freecodecamp.org/images/T0WP8iFl9qbX-VnI0GYUhcL6OAhA8iSUYhOa)
_Le LCD s'allume !_

#### Étape 3

Connectons maintenant le LCD à l'Arduino afin que nous puissions afficher la tension (que nous allons collecter à partir d'une broche analogique) sur le LCD. Connectez les Broches 4, 6, 11, 12, 13 et 14 du LCD à n'importe quelle broche numérique de l'Arduino (par exemple, la Broche 2). Ensuite, placez un fil dans le GND et un autre dans une broche analogique, comme A5. Les deux fils sont maintenant vos sondes de test.

![Image](https://cdn-media-1.freecodecamp.org/images/NW8m7mJlEFP7xsorvz6EW9Y35KRTDN1bjXTM)
_Circuit électrique terminé !_

Nous avons maintenant terminé avec l'électronique/le matériel. Passons au code.

### **Le Code**

Le code est assez simple. Nous voulons simplement collecter le signal analogique que l'Arduino reçoit à la Broche A5 (ou toute autre broche analogique) et le convertir en numérique. Nous voulons ensuite afficher les résultats sur l'écran LCD.

Voici le code que vous pouvez copier-coller.

```
#include <LiquidCrystal.h> int Vpin=A5;float voltage;float volts;LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
```

```
void setup() {Serial.begin(9600);lcd.begin(16,2);}
```

```
void loop() {
```

```
voltage = analogRead(Vpin); volts = voltage/1023*5.0; Serial.println(volts);lcd.print("voltage = ");lcd.print(volts);delay(200);lcd.clear();}
```

Que se passe-t-il ici ?

Nous importons d'abord la bibliothèque LCD, puis nous créons une variable nommée Vpin (qui sera la tension collectée à partir de A5). Ensuite, nous créons deux autres variables pour la tension, puis une variable de type LiquidCrystal. Enfin, nous faisons la configuration avec le moniteur série (qui est un outil vraiment utile dans Arduino ! Un peu comme une console de débogage), nous convertissons la tension analogique en tension numérique, et nous affichons cette valeur sur l'écran LCD.

Et c'est tout ! Allez et testez diverses piles et points ! Voici des photos de quelques tests que j'ai effectués :

![Image](https://cdn-media-1.freecodecamp.org/images/VOnX6XrnL4cNqEZ-aBzU0Aj8AtRiEYuf5YQb)
_Fils neutres._

![Image](https://cdn-media-1.freecodecamp.org/images/IUX4cbowtANkEPD2YBOzWv7tQUN63NJ0WNc3)
_Test d'une pile AA de 1,5V._

De plus, si vous souhaitez rendre la lecture sur le LCD plus lisible, placez une résistance de 1k ohm dans le chemin vers la Broche 3 (qui est pour les ajustements de contraste). En limitant le courant électrique qui circule vers cette broche, vous améliorerez le contraste de l'écran.

**Note importante également** : Dans ce voltmètre, toute tension que vous testez sera directement envoyée à l'Arduino, vous ne devez donc tester que des éléments qui sont dans la plage de volts que l'Arduino peut gérer en toute sécurité (0–5V). Tester avec une pile de 9V grillera votre Arduino.

Merci à ce [tutoriel vidéo](https://youtu.be/OZM6wm16uPU) pour m'avoir aidé à comprendre le circuit électrique. Un merci spécial à mes amis [Nick Arner](https://twitter.com/nickarner) et [Johnny Wang](https://twitter.com/johnny___wang) pour m'avoir aidé à corriger des choses. Et merci à [Laura Deming](https://twitter.com/LauraDeming) pour le défi ! :)

D'autres articles et tutoriels sur l'électronique/le matériel et les interfaces cerveau-ordinateur à venir ! :D

Si vous avez des commentaires à partager, n'hésitez pas à m'envoyer un email à harshita@harshitaapps.com. J'ai hâte d'avoir de vos nouvelles !