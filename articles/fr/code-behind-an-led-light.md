---
title: Comment installer une lumière LED et la faire clignoter avec du code
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2020-06-08T21:50:21.000Z'
originalURL: https://freecodecamp.org/news/code-behind-an-led-light
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-25-at-4.15.01-PM-1.png
tags:
- name: Electronics
  slug: electronics
- name: hardware
  slug: hardware
- name: software
  slug: software
seo_title: Comment installer une lumière LED et la faire clignoter avec du code
seo_desc: 'Coding an LED Light is introductory project that shows you how software
  and hardware interact with each other. It''s a simple project you can complete in
  a weekend that''ll help you learn some basic aspects of hardware.

  By the end of the project, you w...'
---

Coder une lumière LED est un projet d'introduction qui montre comment le logiciel et le matériel interagissent entre eux. C'est un projet simple que vous pouvez réaliser en un week-end et qui vous aidera à apprendre quelques aspects de base du matériel.

À la fin du projet, vous aurez codé votre propre lumière LED, vous aurez les connaissances pour manipuler la LED pour l'allumer/éteindre à des intervalles de votre choix, et vous apprendrez les principes de base du matériel.

Le kit de démarrage [Elegoo Uno](https://www.amazon.com/ELEGOO-Project-Tutorial-Controller-Projects/dp/B01D8KOZF4) contient tout le matériel ainsi que les instructions dont vous avez besoin pour créer une simple lumière LED. La lumière LED est le premier projet proposé avec leur kit.

Elegoo Uno comprend de nombreux autres projets et vous guide à travers des projets pour débutants jusqu'à des projets avancés. Chaque projet dans la boîte fait progresser vos compétences de manière simple et facile à suivre.

## Composants dont vous aurez besoin

### Elegoo Uno R3

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-24-at-7.49.14-PM.png align="left")

*Elegoo Uno R3*

L'Elegoo Uno R3 est une carte microcontrôleur. Les microcontrôleurs sont intégrés dans les appareils pour contrôler les actions et les fonctionnalités d'un produit. Ce sont des circuits intégrés compacts conçus pour contrôler les opérations.

Le microcontrôleur inclus dans l'Elegoo Uno R3 dispose de 14 broches d'entrée/sortie numériques, 6 entrées analogiques, une connexion USB, une prise d'alimentation et un bouton de réinitialisation. Cette carte contient tout ce dont vous avez besoin pour supporter le microcontrôleur. Il suffit de brancher le câble USB pour allumer le microcontrôleur.

### Câble USB

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-24-at-7.49.22-PM.png align="left")

*Câble USB*

Vous avez besoin d'un câble USB pour connecter l'Elegoo Uno R3 à votre ordinateur et l'allumer. USB signifie Universal Serial Bus. L'USB est utilisé pour connecter votre ordinateur à des appareils tels que des caméras numériques, des imprimantes, des scanners et des disques durs externes.

Dans notre projet, nous utiliserons un câble USB pour connecter notre microcontrôleur à notre ordinateur.

### LEDs

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-161.png align="left")

*Lumière LED*

LED signifie diode électroluminescente. Elle a une borne positive et négative. Le côté le plus long est la borne positive.

## Comment assembler les composants

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-25-at-4.15.01-PM.png align="left")

Dans ce projet, nous allons simplement faire clignoter la LED.

Tout d'abord, nous devons brancher le câble USB à la carte puis à l'ordinateur.

Ensuite, nous devons brancher la LED à GND (GND est le point de référence dans un circuit électrique à partir duquel les tensions sont mesurées, et est un chemin de retour commun pour le courant électrique) et à l'entrée 13 sur la carte.

### Code pour faire clignoter la LED :

Après avoir branché la carte microcontrôleur à l'ordinateur et la LED sur la carte elle-même, nous devons écrire un simple code pour faire clignoter la LED.

```php
// la fonction setup s'exécute une fois lorsque vous appuyez sur reset ou alimentez la carte

void setup() {
  // initialiser la broche numérique LED_BUILTIN comme une sortie.
  pinMode(LED_BUILTIN, OUTPUT);
}

// la fonction loop s'exécute encore et encore indéfiniment
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // allumer la LED 
  delay(1000);                       // attendre une seconde
  digitalWrite(LED_BUILTIN, LOW);    // éteindre la LED
  delay(1000);                       // attendre une seconde
}
```

Le code ci-dessus allume essentiellement la LED pendant 1 seconde puis l'éteint pendant une seconde.

Cette fonction est dans une boucle continue. La fonction `digitalWrite` prend 2 paramètres, `LED_BUILTIN` et `HIGH || LOW`. La boucle prend essentiellement la LED, puis met la tension à `HIGH` ce qui l'allume. Ensuite, après 1 seconde, elle éteint la même LED en mettant la tension à `LOW`.

### Voici le produit final :

%[https://youtu.be/D6IkSkKcY5s] 

Le but de ce petit projet de codage de lumière LED était de vous introduire aux principes élémentaires de la combinaison du matériel et du logiciel. J'espère que vous l'avez apprécié !