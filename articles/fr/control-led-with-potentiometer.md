---
title: Comment contrôler la luminosité d'une LED avec un potentiomètre
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2024-03-18T19:48:37.000Z'
originalURL: https://freecodecamp.org/news/control-led-with-potentiometer
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/cover-image-potentiometer.png
tags:
- name: arduino
  slug: arduino
- name: embedded systems
  slug: embedded-systems
seo_title: Comment contrôler la luminosité d'une LED avec un potentiomètre
seo_desc: 'Potentiometers are used in various electronic circuits and systems. You
  can use them in electronic devices to control volume, brightness, motor speed, voltage
  regulation, and so on.

  You''ve most likely used a potentiometer before with appliances like ...'
---

Les potentiomètres sont utilisés dans divers circuits et systèmes électroniques. Vous pouvez les utiliser dans des appareils électroniques pour contrôler le volume, la luminosité, la vitesse des moteurs, la régulation de tension, et ainsi de suite.

Vous avez probablement déjà utilisé un potentiomètre avec des appareils comme des radios, des fours à micro-ondes, des mixeurs, des ventilateurs électriques, des manettes de jeu, et autres.

Ils sont généralement utilisés pour fournir ou contrôler différentes plages de résistance variable dans les circuits électroniques.

Dans cet article, vous apprendrez les points suivants :

* Comment connecter un potentiomètre à une carte Arduino.
* Comment obtenir les valeurs d'un potentiomètre.
* Comment contrôler la luminosité d'une LED en utilisant un potentiomètre.

Vous pouvez également regarder la version vidéo de cet article ici :

%[https://youtu.be/dwZCgzlYfoA]

## Composants matériels

Voici les composants matériels dont vous aurez besoin pour suivre cet article :

* Carte Arduino.
* Potentiomètre.
* Plaque d'essai.
* LED.
* Résistance de 1K Ohm.
* Fils de connexion.

## Comment connecter un potentiomètre à une carte Arduino

Le potentiomètre est composé de trois bornes : deux bornes externes et la borne centrale. L'une ou l'autre des bornes externes peut être connectée soit à 5V, soit à GND (masse). C'est-à-dire :

* Si vous connectez la borne externe gauche à 5V, vous devez connecter la borne externe droite à GND.
* Si vous connectez la borne externe gauche à GND, vous devez connecter la borne externe droite à 5V.

La borne centrale sert de borne de sortie. Nous la connecterons à une broche analogique. Vous pouvez lire les valeurs variables du potentiomètre à partir de la borne de sortie.

Voici le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/circuit-diagram.png)
_schéma du circuit_

Voici comment le potentiomètre a été connecté dans le schéma ci-dessus :

* La borne externe gauche du potentiomètre a été connectée à GND.
* La borne externe droite a été connectée à 5V.
* La borne centrale (borne de sortie) a été connectée à la broche analogique A0 sur la carte Uno.

Voici comment la LED a été connectée :

* La patte la plus courte de la LED a été connectée à GND.
* La patte la plus longue a été connectée à la broche numérique 6 via une résistance de 1K Ohm.

Assurez-vous de connecter la LED à une broche numérique avec le symbole ~. Ces broches supportent la modulation de largeur d'impulsion, ce qui permet d'envoyer des signaux analogiques aux broches numériques.

```cpp
int potPin = A0;
int potValue = 0;
int brightness = 0;
int ledPin = 6;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  potValue = analogRead(potPin);
  brightness = (255.0/1023.0)*potValue;
  analogWrite(ledPin, brightness);
}
```

Analysons le code.

### Initialiser les variables

Nous avons commencé par initialiser nos variables :

```cpp
int potPin = A0;
int potValue = 0;
int brightness = 0;
int ledPin = 6;
```

La variable `potPin` a une valeur de A0. Cela représente la broche A0 connectée à la broche de sortie du potentiomètre.

Nous avons ensuite déclaré une variable `potValue`, qui sera utilisée pour stocker les valeurs de `potPin`.

La variable `brightness` sera utilisée pour contrôler la luminosité de la LED.

La broche de la LED a été connectée à la broche numérique 6 sur la carte Uno, donc nous avons initialisé une variable `ledPin` avec une valeur de 6 : `int ledPin = 6;`.

### Moniteur série et pinMode

Ensuite, dans la fonction `loop()`, nous avons initialisé le moniteur série et défini la broche de la LED pour qu'elle serve de broche de sortie :

```cpp
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}
```

### Créer la logique pour contrôler la luminosité de la LED

Dans la fonction `loop()`, nous avons trois lignes de code :

```cpp
void loop() {
  potValue = analogRead(potPin);
  brightness = (255.0/1023.0)*potValue;
  analogWrite(ledPin, brightness);
}
```

Dans la première ligne, nous avons utilisé la fonction `analogRead()` pour lire la valeur de `potPin`. Les valeurs lues ont été assignées à la variable `potValue`.

À ce stade, si vous affichez `potValue` sur le moniteur série en utilisant `Serial.println(potValue);`, vous obtiendrez une plage de valeurs de 0 à 1023 lorsque vous tournez le bouton du potentiomètre.

Pour la variable `brightness`, nous avons converti les valeurs du potentiomètre pour qu'elles se situent dans la plage de 0 à 255 : `brightness = (255.0/1023.0)*potValue;`. Cela est dû au fait que la fonction `analogWrite()` n'accepte que les valeurs dans cette plage, et non la plage par défaut de 0 à 1023 que produit le potentiomètre.

Enfin, nous avons utilisé la fonction `analogWrite()` pour envoyer des valeurs à la LED : `analogWrite(ledPin, brightness);`.

Le premier paramètre de la fonction `analogWrite()` est `ledPin`, qui indique la broche où les valeurs doivent être envoyées. Le deuxième paramètre est `brightness`, qui indique une plage de valeurs à envoyer à la LED (`ledPin`).

Lorsque vous téléversez le code sur votre carte, la LED devrait avoir différents niveaux de luminosité lorsque vous tournez le potentiomètre.

## Conclusion

Dans cet article, vous avez appris comment contrôler la luminosité d'une LED en utilisant un potentiomètre. Vous avez également vu comment connecter les composants aux broches numériques et analogiques d'une carte Arduino.

Enfin, vous avez appris comment faire fonctionner les composants ensemble en utilisant du code.

Vous pouvez trouver le code de ce projet [ici](https://github.com/ihechikara/control-led-with-potentiometer/blob/main/pot.ino). Vous pouvez regarder la version vidéo [ici](https://youtu.be/dwZCgzlYfoA?si=k9W9eAEjcc4yLxqe).

Consultez [mon blog](https://ihechikara.com/) pour des articles sur les systèmes embarqués, l'IoT et le développement web.

Bon codage !