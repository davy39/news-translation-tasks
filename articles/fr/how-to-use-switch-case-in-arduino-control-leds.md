---
title: Comment utiliser l'instruction Switch Case dans Arduino – Contrôler des LEDs
  avec l'instruction Switch
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2024-10-08T14:39:47.209Z'
originalURL: https://freecodecamp.org/news/how-to-use-switch-case-in-arduino-control-leds
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728178146204/a1c1a6af-b4ce-4fe4-a73d-8861d63cc01e.png
tags:
- name: arduino
  slug: arduino
- name: embedded systems
  slug: embedded-systems
seo_title: Comment utiliser l'instruction Switch Case dans Arduino – Contrôler des
  LEDs avec l'instruction Switch
seo_desc: 'You can use a switch case statement to execute different blocks of code
  based on the value of a variable. It offers a more direct and cleaner approach to
  handling multiple conditions.

  In this article, you''ll learn how to control LEDs using a switch c...'
---

Vous pouvez utiliser une instruction `switch case` pour exécuter différents blocs de code en fonction de la valeur d'une variable. Cela offre une approche plus directe et plus propre pour gérer plusieurs conditions.

Dans cet article, vous apprendrez à contrôler des LEDs en utilisant une instruction `switch case` dans Arduino. Vous pouvez également trouver l'instruction `switch case` dans d'autres langages de programmation, donc cela peut servir d'exemple pratique de leur fonctionnement.

Voici une démonstration de ce que vous allez construire :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1728301474557/f67ddfe7-0cf1-47ee-9732-90f3a4b1649c.gif align="center")

Vous pouvez regarder la version vidéo de cet article ici :

%[https://www.youtube.com/watch?v=TAU_osZ6aGQ]

## **Composants matériels**

Voici les composants dont vous aurez besoin pour suivre ce tutoriel :

* Carte Arduino (Uno).
  
* Potentiomètre.
  
* Plaque d'essai.
  
* Trois LEDs.
  
* Résistances pour les LEDs.
  
* Fils de connexion.
  

## **Comment utiliser une instruction** `Switch Case` **dans Arduino**

Voici la syntaxe/structure d'une instruction `switch` :

```cpp
switch (variable) {
 
0case valeur1:
 
0 
0// code à exécuter si variable == valeur1
 
0 
0break;
 
0case valeur2:
 
0 
0// code à exécuter si variable == valeur2
 
0 
0break;
 
0default:
 
0 
0// code à exécuter si variable ne correspond à aucun cas
 
0 
0break;
}
```

Décomposons cela :

* `variable` : Cela désigne la variable étant évaluée. La valeur de la variable détermine comment les blocs de code seront exécutés.
  
* `case` : Chaque `case` représente une valeur qui peut correspondre à la variable étant évaluée. Si la `variable` et un `case` ont la même valeur, le code pour ce cas sera exécuté. Vous pouvez avoir autant de cas que vous le souhaitez.
  
* `break` : Après qu'un bloc de code dans un `case` a été exécuté, le mot-clé `break` termine le code. C'est-à-dire qu'il empêche le code de passer à d'autres cas car une correspondance a déjà été trouvée.
  
* `default` : Dans une situation où aucun des cas ne correspond à la `variable`, le code dans le bloc `default` sera exécuté.
  

Ensuite, utilisons une instruction `switch` pour contrôler des LEDs.

### Exemple de `Switch Case` dans Arduino

#### **Schéma de circuit**

Voici comment connecter vos composants :

![Schéma de circuit montrant un potentiomètre et des LEDs connectés à une carte Arduino Uno R3](https://cdn.hashnode.com/res/hashnode/image/upload/v1728177876221/e58910e9-f8be-430b-a220-cda2cc9b956a.png align="center")

L'objectif ici est de décider quelle LED (ou une combinaison de LEDs) s'allume en fonction de la valeur d'une variable.

#### **Connexion du potentiomètre**

* Connectez la borne gauche du potentiomètre à 5V.
  
* Connectez la borne droite à GND.
  
* Connectez la borne centrale à A0.
  

#### **Connexion des LEDs**

* Pour chaque LED, connectez la patte la plus courte à GND.
  
* Connectez chaque patte la plus longue à une broche numérique. Je recommande d'utiliser la broche 8 (pour la LED verte), 9 (pour la LED jaune) et 10 (pour la LED rouge) pour correspondre à ce que nous avons dans le schéma de circuit. Nous utiliserons également ces valeurs dans le code.
  

Voici le code complet du projet :

```cpp
int greenLED = 8;
int yellowLED = 9;
int redLED = 10;
int potPin = A0; 
int potValue;
int mappedPotValue;

void setup() {
 
0pinMode(greenLED, OUTPUT);
 
0pinMode(yellowLED, OUTPUT);
 
0pinMode(redLED, OUTPUT);
 
0Serial.begin(9600);
}

void loop() {
 
0potValue = analogRead(potPin);
 
0mappedPotValue = map(potValue, 0, 1023, 0, 5);

 
0switch (mappedPotValue) {
 
0 
0case 0:
 
0 
0 
0digitalWrite(greenLED, LOW);
 
0 
0 
0digitalWrite(yellowLED, LOW);
 
0 
0 
0digitalWrite(redLED, LOW);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0break;
 
0 
0case 1:
 
0 
0 
0digitalWrite(greenLED, HIGH);
 
0 
0 
0digitalWrite(yellowLED, LOW);
 
0 
0 
0digitalWrite(redLED, LOW);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0break;
 
0 
0case 2:
 
0 
0 
0digitalWrite(greenLED, LOW);
 
0 
0 
0digitalWrite(yellowLED, HIGH);
 
0 
0 
0digitalWrite(redLED, LOW);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0break;
 
0 
0case 3:
 
0 
0 
0digitalWrite(greenLED, LOW);
 
0 
0 
0digitalWrite(yellowLED, LOW);
 
0 
0 
0digitalWrite(redLED, HIGH);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0break;
 
0 
0case 4:
 
0 
0 
0digitalWrite(greenLED, HIGH);
 
0 
0 
0digitalWrite(yellowLED, HIGH);
 
0 
0 
0digitalWrite(redLED, HIGH);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0delay(500);
 
0 
0 
0digitalWrite(greenLED, LOW);
 
0 
0 
0digitalWrite(yellowLED, LOW);
 
0 
0 
0digitalWrite(redLED, LOW);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0delay(500);
 
0 
0 
0break;
  }
}
```

Décomposons le code.

#### **Initialisation des variables**

```cpp
int greenLED = 8;
int yellowLED = 9;
int redLED = 10;
int potPin = A0; 
int potValue;
int mappedPotValue;
```

Nous avons commencé par initialiser des variables pour correspondre aux connexions matérielles.

`greenLED`, `yellowLED` et `redLED` ont des valeurs de 8, 9 et 10, respectivement. Cela correspond aux broches auxquelles elles étaient connectées sur la carte Arduino. De même, `potPin`, qui est la variable pour le potentiomètre, a une valeur de A0.

Vous utiliserez la variable `potValue` pour stocker la valeur actuelle du potentiomètre. Nous avons également créé une variable `mappedPotValue` pour stocker la plage de valeurs nécessaires pour les LEDs dans une minute.

#### **pinMode et Moniteur Série**

```cpp
void setup() {
 
0pinMode(greenLED, OUTPUT);
 
0pinMode(yellowLED, OUTPUT);
 
0pinMode(redLED, OUTPUT);
 
0Serial.begin(9600);
}
```

Dans la fonction `setup()`, nous avons défini les LEDs comme des broches de sortie et initialisé le moniteur série.

#### **Logique pour l'instruction** `switch case`

Tout d'abord, nous avons lu la valeur du potentiomètre en utilisant la fonction `analogRead()` et l'avons stockée dans la variable `potValue` :

```cpp
potValue = analogRead(potPin);
```

Nous avons ensuite converti les valeurs du potentiomètre en une plage de 0 à 4 en utilisant la fonction `map` et les avons stockées dans la variable `mappedPotValue` :

```cpp
mappedPotValue = map(potValue, 0, 1023, 0, 5);
```

Ensuite, nous avons créé une instruction `switch`—la valeur étant évaluée est `mappedPotValue`. Rappelez-vous que c'est la variable où nous avons stocké les valeurs du potentiomètre. Donc, chaque fois que vous tournez le potentiomètre, la valeur change et correspond potentiellement à un `case` :

```cpp
 
0switch (mappedPotValue) {
 
0 
0case 0:
 
0 
0 
0digitalWrite(greenLED, LOW);
 
0 
0 
0digitalWrite(yellowLED, LOW);
 
0 
0 
0digitalWrite(redLED, LOW);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0break;
 
0 
0case 1:
 
0 
0 
0digitalWrite(greenLED, HIGH);
 
0 
0 
0digitalWrite(yellowLED, LOW);
 
0 
0 
0digitalWrite(redLED, LOW);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0break;
 
0 
0case 2:
 
0 
0 
0digitalWrite(greenLED, LOW);
 
0 
0 
0digitalWrite(yellowLED, HIGH);
 
0 
0 
0digitalWrite(redLED, LOW);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0break;
 
0 
0case 3:
 
0 
0 
0digitalWrite(greenLED, LOW);
 
0 
0 
0digitalWrite(yellowLED, LOW);
 
0 
0 
0digitalWrite(redLED, HIGH);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0break;
 
0 
0case 4:
 
0 
0 
0digitalWrite(greenLED, HIGH);
 
0 
0 
0digitalWrite(yellowLED, HIGH);
 
0 
0 
0digitalWrite(redLED, HIGH);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0delay(500);
 
0 
0 
0digitalWrite(greenLED, LOW);
 
0 
0 
0digitalWrite(yellowLED, LOW);
 
0 
0 
0digitalWrite(redLED, LOW);
 
0 
0 
0Serial.println(mappedPotValue);
 
0 
0 
0delay(500);
 
0 
0 
0break;
  }
```

Nous avons passé `mappedPotValue` comme paramètre à `switch` puisque c'est la variable comparée à différents cas : `switch (mappedPotValue)`.

* Pour `case 0`, toutes les LEDs seront éteintes.
  
* Pour `case 1`, seule la LED verte s'allume.
  
* Pour `case 2`, seule la LED jaune s'allume.
  
* Pour `case 3`, seule la LED rouge s'allume.
  
* Pour `case 4`, les trois LEDs clignoteront continuellement.
  

En utilisant une instruction `switch`, vous avez réussi à contrôler le comportement des LEDs en fonction de la valeur d'un potentiomètre !

## **Conclusion**

Dans cet article, vous avez appris à utiliser une instruction `switch case` dans Arduino en utilisant un exemple pratique.

Vous avez appris à contrôler différentes LEDs en fonction de la valeur d'un potentiomètre. Vous avez réalisé cela en utilisant différents cas dans une instruction `switch` pour correspondre à la valeur actuelle du potentiomètre et exécuter le code correspondant.

Les instructions `switch` peuvent être utilisées de différentes manières pour rendre un projet plus dynamique. Certains cas d'utilisation dans Arduino incluent :

* Gérer et interpréter les différentes valeurs, modes et états d'un composant ou d'un capteur.
  
* Effectuer des actions basées sur des commandes spécifiques. Par exemple, faire tourner un bras robotique à un angle/direction spécifique.
  
* Mapper les pressions de boutons aux entrées utilisateur, et ainsi de suite.
  

Vous pouvez regarder la version vidéo de ce projet [ici](https://www.youtube.com/watch?v=TAU_osZ6aGQ). Le code complet du projet est disponible sur [GitHub](https://github.com/ihechikara/switch-case-arduino).

Consultez [mon blog](https://ihechikara.com/) pour des articles sur les systèmes embarqués, l'IoT et le développement web.

Bon codage !