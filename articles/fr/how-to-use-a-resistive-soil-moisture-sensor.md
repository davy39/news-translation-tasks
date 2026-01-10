---
title: Comment utiliser un capteur résistif d'humidité du sol
subtitle: ''
author: Michael Ikoko
co_authors: []
series: null
date: '2025-07-10T00:19:07.364Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-resistive-soil-moisture-sensor
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752106699262/6ae871df-e1fb-4019-a446-9bd8cca1cab0.png
tags:
- name: arduino
  slug: arduino
- name: embedded systems
  slug: embedded-systems
- name: Programming Blogs
  slug: programming-blogs
seo_title: Comment utiliser un capteur résistif d'humidité du sol
seo_desc: 'A resistive soil moisture sensor is a widely used, simple, and affordable
  way of estimating the amount of water in the soil.

  In this tutorial, you will learn how to interface a resistive soil moisture sensor
  with an Arduino UNO microcontroller. You w...'
---

Un capteur résistif d'humidité du sol est une méthode largement utilisée, simple et abordable pour estimer la quantité d'eau dans le sol.

Dans ce tutoriel, vous apprendrez à interfacer un capteur résistif d'humidité du sol avec un microcontrôleur Arduino UNO. Vous en apprendrez davantage sur les parties et les composants du capteur, comment étalonner le capteur pour votre type de sol, et comment lire les données de sortie analogiques et numériques du capteur.

Vous mettrez en œuvre deux exemples pratiques dans ce tutoriel :

1. Le premier exemple illustre comment vous pouvez lire les données de sortie analogiques du capteur et convertir la lecture analogique en une valeur en pourcentage.

2. Le second exemple illustre comment vous pouvez utiliser la sortie numérique du capteur pour déterminer si le sol est humide ou sec, et indiquer le résultat à l'aide d'une LED rouge et verte.

À la fin du tutoriel, vous aurez une compréhension solide du fonctionnement d'un capteur résistif d'humidité du sol et de la manière d'intégrer le capteur dans vos projets basés sur des microcontrôleurs.

## Prérequis

Pour suivre efficacement ce tutoriel, vous devez avoir les composants suivants :

* Arduino UNO

* Capteur résistif d'humidité du sol

* Plaque d'essai

* 5 LEDs (n'importe quelle couleur pour l'exemple analogique)

* 1 LED rouge et 1 LED verte (pour l'exemple numérique)

* Résistances de 220 ohms (une par LED)

* Fils de connexion

## Table des matières

* [Qu'est-ce qu'un capteur d'humidité du sol ?](#heading-qu-est-ce-qu-un-capteur-d-humidité-du-sol)

* [Types de capteurs d'humidité du sol](#heading-types-de-capteurs-d-humidité-du-sol)

* [Parties d'un capteur résistif d'humidité du sol](#heading-parties-d-un-capteur-résistif-d-humidité-du-sol)

* [Comment étalonner le capteur pour votre sol](#heading-comment-étalonner-le-capteur-pour-votre-sol)

* [Exemple 1 : Comment déterminer le niveau d'humidité du sol en pourcentage à partir de la sortie analogique](#heading-exemple-1-comment-déterminer-le-niveau-d-humidité-du-sol-en-pourcentage-à-partir-de-la-sortie-analogique)

* [Exemple 2 : Comment déterminer l'état d'humidité du sol à partir de la sortie numérique](#heading-exemple-2-comment-déterminer-l-état-d-humidité-du-sol-à-partir-de-la-sortie-numérique)

* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un capteur d'humidité du sol ?

Un capteur d'humidité du sol est un dispositif qui estime la teneur en humidité du sol. Les capteurs d'humidité du sol fonctionnent généralement en mesurant les propriétés électriques du sol, telles que la constante diélectrique et la résistance. Certains capteurs d'humidité du sol utilisent également des méthodes de domaine temporel pour déterminer la vitesse de propagation des ondes électromagnétiques à travers le sol.

Les capteurs d'humidité du sol ont diverses applications dans différents domaines. Ces applications incluent, sans s'y limiter :

* Recherche climatique et environnementale

* Système d'irrigation automatisé/intelligent

* Systèmes de surveillance de serre

* Planification urbaine

## Types de capteurs d'humidité du sol

Les capteurs d'humidité du sol sont classés en fonction de la propriété du sol qu'ils mesurent comme indicateur de la teneur en humidité. Les capteurs d'humidité du sol les plus courants pour les projets à petite échelle sont :

* Capteurs résistifs d'humidité du sol

* Capteurs capacitifs d'humidité du sol

### Capteur résistif d'humidité du sol

Un capteur résistif d'humidité du sol estime la teneur en humidité en fonction de la relation entre la teneur en eau et la résistivité du sol. La résistivité électrique du sol diminue de manière exponentielle à mesure que la teneur en eau augmente.

Le capteur résistif d'humidité du sol possède deux sondes insérées dans le sol. Il mesure la résistance électrique du sol entre les deux sondes.

### Capteur capacitif d'humidité du sol

Un capteur capacitif d'humidité du sol détermine la teneur en humidité du sol en fonction de la relation entre la teneur en eau et les propriétés diélectriques du sol. La constante diélectrique d'un sol augmente à mesure que la teneur en eau augmente.

Un capteur capacitif d'humidité du sol possède généralement une plaque positive et une plaque négative avec un espace entre elles. Lorsque les sondes sont insérées dans le sol, le sol devient le milieu diélectrique entre les deux plaques. Le capteur mesure le changement de la propriété diélectrique du sol.

### Comment choisir entre les capteurs résistifs et capacitifs

Le choix entre un capteur résistif et capacitif d'humidité du sol dépend de plusieurs facteurs :

* **Coût** : Un capteur résistif d'humidité du sol est généralement moins cher qu'un capteur capacitif.

* **Précision** : Les capteurs capacitifs d'humidité du sol sont plus précis que leurs homologues résistifs. Des facteurs comme le type de sol et l'application d'engrais ont un effet moindre sur la sensibilité du capteur capacitif d'humidité du sol.

* **Utilisation à long terme** : Les capteurs résistifs d'humidité du sol sont sujets à la corrosion avec une utilisation fréquente. Cela se produit parce que le courant circulant à travers les sondes en contact avec le sol provoque l'électrolyse des électrodes métalliques dans les sondes. En revanche, les capteurs capacitifs d'humidité du sol sont résistants à la corrosion. Cela est dû au fait que les plaques de contact sont intégrées dans des matériaux résistants à la corrosion et n'ont pas besoin d'être en contact direct avec le sol.

## Parties d'un capteur résistif d'humidité du sol

Le module de capteur résistif d'humidité du sol est généralement composé de deux parties : les sondes du capteur et le module comparateur de tension.

### Les sondes du capteur

Les sondes sont la partie du capteur qui est placée dans le sol. Les sondes sont utilisées pour détecter la résistance électrique entre deux points dans le sol.

![Diagramme étiqueté des sondes du capteur](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909048810/7c2367b5-872c-4e98-acf8-d8b2f0851f6c.jpeg align="center")

Comme le montre le diagramme ci-dessus, les sondes du capteur ont les composants suivants :

* **Électrodes** : Les électrodes métalliques conduisent le courant à travers le sol. Lorsque le capteur est alimenté, le courant circule d'une électrode à travers le sol vers l'autre électrode et retourne au module comparateur. Le capteur mesure ensuite la résistance du sol au signal électrique circulant à travers le sol entre les électrodes pour déterminer le niveau d'humidité.

* **Broches de connecteur non polarisées** : Les deux broches de connecteur sont utilisées pour connecter les sondes au module comparateur de tension. Les broches n'ont pas de polarité et peuvent être connectées dans n'importe quel ordre aux broches de connecteur respectives sur le module comparateur de tension. La sonde est connectée au module comparateur à l'aide de fils de connexion femelle-femelle.

### Le module comparateur de tension

Le module comparateur de tension interprète le signal électrique des sondes, traite les signaux et fournit des sorties analogiques et numériques qui peuvent être lues par le microcontrôleur.

![Diagramme étiqueté du module comparateur de tension du capteur](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909173338/454ae6bf-2d34-4131-af88-c990eb988cbd.jpeg align="center")

Le module comparateur de tension a les composants suivants :

* **Puce comparateur LM393** : Le comparateur LM393 est un comparateur double qui compare le signal électrique des sondes à une référence définie par le potentiomètre et produit une sortie numérique. Le signal de référence correspond à un certain niveau d'humidité du sol (seuil) et est défini à l'aide du potentiomètre.

  * Le comparateur émet un signal `HIGH` lorsque le signal analogique lu à partir des sondes est supérieur à la référence, ce qui signifie que le sol a moins d'humidité que le niveau d'humidité seuil.

  * Le comparateur émet un signal `LOW` lorsque le signal analogique lu à partir des sondes est inférieur à la référence ; cela signifie que le sol a plus d'humidité que le niveau d'humidité seuil.

* **Potentiomètre** : Le potentiomètre est utilisé pour définir le signal électrique de référence qui est utilisé par la puce comparateur LM393. Le potentiomètre augmente ou diminue le niveau d'humidité seuil. Il se compose d'un bouton qui peut être tourné dans le sens des aiguilles d'une montre ou dans le sens inverse.

* **Indicateur d'alimentation (PWR-LED)** : L'indicateur d'alimentation est une LED qui s'allume lorsque le module est sous tension.

* **Indicateur de sortie numérique (DO-LED)** : L'indicateur de sortie numérique est une LED qui s'allume lorsque le capteur détecte un sol humide. C'est-à-dire que le niveau d'humidité actuel lu par le capteur est supérieur au seuil, et le comparateur émet un signal `LOW`.

* **Broche d'alimentation (VCC)** : Cette broche est utilisée pour alimenter le capteur. Le module du capteur peut être alimenté par une source de tension de 5V ou 3.3V. Vous devez noter que le changement de la source de tension modifie également la sortie analogique du capteur. Dans ce tutoriel, vous utiliserez l'une des broches numériques pour alimenter le capteur. Les broches numériques de l'Arduino émettent 5V. Le capteur a généralement un courant de fonctionnement de 15mA, et la broche de sortie numérique de l'Arduino peut fournir un courant maximal de 40mA, donc elle peut alimenter le capteur en toute sécurité.

* **Broche de masse (GND)** : Cette broche est utilisée pour fournir une référence de masse pour le capteur. Elle est généralement connectée à n'importe quelle broche de masse de votre microcontrôleur.

* **Broche de sortie numérique (DO)** : La broche de sortie numérique émet un signal `HIGH` ou `LOW` en fonction de la valeur obtenue du comparateur LM393. Cette broche est généralement utilisée par un microcontrôleur pour lire la sortie numérique du comparateur LM393.

* **Broche de sortie analogique (AO)** : La broche de sortie analogique fournit une valeur de tension analogique de 10 bits. Les valeurs varient de 0 à 1023, et elles indiquent le niveau d'humidité du sol. Typiquement, dans la plupart des capteurs, des valeurs analogiques plus élevées indiquent un sol plus sec et des valeurs analogiques plus basses indiquent un sol plus humide.

* **Broches de connecteur de sonde de capteur** : Ces deux broches sont utilisées pour connecter les sondes du capteur au module comparateur de tension.

## Comment étalonner le capteur pour votre sol

Comme expliqué précédemment dans l'article, le capteur résistif d'humidité du sol est sensible au type de sol. Cela signifie qu'il est important que vous étalonniez le capteur pour le type de sol que vous prévoyez d'utiliser. Vous faites cela pour améliorer la précision de vos lectures sur un sol particulier.

Une façon d'étalonner le capteur est de déterminer la plage possible de valeurs pour le type de sol. Cela signifie que vous mesurez la sortie du capteur lorsque le sol est totalement sec et lorsque le sol est totalement humide. Vous pouvez ensuite utiliser cette plage de valeurs pour mapper la lecture du capteur à une nouvelle échelle, comme un pourcentage. Les étapes suivantes décrivent comment vous pouvez étalonner le capteur :

### Étape 1 : Connecter le capteur à l'Arduino

![Diagramme schématique pour l'étalonnage du sol](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909238974/d84a8df3-52d0-4f5e-90a4-9a4fa6c198fb.jpeg align="center")

En utilisant l'image ci-dessus comme référence, connectez le capteur au microcontrôleur Arduino comme suit :

1. Connectez la broche **VCC** ou **Power** du module du capteur à la broche numérique **7** de l'Arduino. Cela vous permet de contrôler la tension d'alimentation du capteur dans le croquis Arduino, en vous assurant que le capteur n'est alimenté que lorsque vous souhaitez prendre une lecture. Faire cela peut aider à améliorer la durabilité du capteur.

2. Connectez la broche **GND** du module du capteur à une broche de masse du microcontrôleur.

3. Connectez la broche de sortie analogique **AO** du module du capteur à la broche analogique **A0** de l'Arduino. C'est la broche où vous lirez les données analogiques du capteur.

4. Connectez les deux broches des sondes aux deux broches de connecteur du module du capteur. Les broches de connecteur n'ont pas de polarité.

### Étape 2 : Télécharger le croquis d'étalonnage vers le microcontrôleur

Téléchargez le croquis suivant dans l'Arduino :

```cpp
const int sensorPin = A0; // Broche d'entrée analogique pour le capteur
const int powerPin = 7; // Broche numérique pour alimenter le capteur

int getAverageReading(int analogPin, int powerPin, int samples = 10) {
  long total = 0;

  digitalWrite(powerPin, HIGH); // Alimentation ON du capteur
  delay(500); // Attendre que le capteur se stabilise
  
  for (int i = 0; i < samples; i++) {                    
 total += analogRead(analogPin);
    delay(10); // Court intervalle entre les cycles
 }

  digitalWrite(powerPin, LOW); // Alimentation OFF du capteur
  return total / samples;
}

void setup() {
  Serial.begin(9600);
  
  pinMode(powerPin, OUTPUT);
  digitalWrite(powerPin, LOW); // Assurer que le capteur est éteint au démarrage

  Serial.println("Mode étalonnage : Insérer dans un sol SEC ou HUMIDE et observer les valeurs.");
}

void loop() {
  int avgReading = getAverageReading(sensorPin, powerPin, 20); // Prendre 20 échantillons moyennés
  Serial.print("Lecture analogique moyenne : ");
  Serial.println(avgReading);
  delay(2000); // Mise à jour toutes les 2 secondes
}
```

Dans le croquis, vous commencez par définir les broches pour alimenter le capteur et lire les données analogiques du capteur. La broche numérique `7` alimente le capteur, et la broche analogique `A0` lit les données du capteur.

La fonction `getAverageReading` alimente le capteur, prend plusieurs lectures du capteur, éteint le capteur et retourne la moyenne des lectures prises. La fonction a trois paramètres :

* `analogPin` – La broche d'entrée analogique, qui lit les données du capteur vers le microcontrôleur.

* `powerPin` – La broche utilisée pour alimenter le capteur. Le capteur est alimenté uniquement lorsque vous souhaitez prendre une lecture.

* `samples` – Le nombre de lectures prises à partir du capteur. Cela vaut par défaut `10`. Vous prenez plusieurs lectures comme moyen de filtrer le bruit dans les données du capteur.

Dans la fonction `setup`, vous commencez par définir le débit en bauds, qui est `9600` pour Arduino UNO et diffère selon les différents microcontrôleurs. Ensuite, vous définissez la broche numérique `7` utilisée pour alimenter le capteur comme une broche de sortie, et écrivez un `LOW` sur le capteur pour vous assurer qu'il est éteint au démarrage.

Enfin, dans la fonction `loop`, vous obtenez la lecture analogique moyenne à partir de la fonction `getAverageReading` et l'imprimez sur le moniteur série. Vous devez noter que dans le croquis, les lectures sont prises toutes les 2 secondes – ce délai doit être plus long dans une application pratique afin d'améliorer la durabilité du capteur.

### Étape 3 : Enregistrer la valeur pour le sol sec

Insérez la sonde du capteur dans un échantillon de sol complètement sec, et enregistrez la lecture analogique moyenne. Vous pouvez sécher le sol en le cuisant dans un four pour éliminer l'humidité. Notez que vous devez laisser le sol refroidir avant d'insérer la sonde du capteur. Un sol chaud peut endommager le capteur. Les lectures analogiques du capteur diffèrent selon le type de sol mais sont généralement très élevées pour un sol sec. Voici ce que j'ai obtenu pour un échantillon de sol sec :

![Moniteur série montrant la lecture analogique pour un sol sec](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909305339/35d99200-d169-4419-9292-e54a9c544d77.png align="center")

### Étape 4 : Enregistrer la valeur pour le sol humide

Insérez la sonde du capteur dans un échantillon de sol complètement humide, et enregistrez la lecture analogique moyenne. La valeur est généralement basse lorsque le sol est saturé. Voici ce que j'ai obtenu pour un échantillon de sol humide :

![Moniteur série montrant la lecture analogique pour un sol humide](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909623291/5478b034-ce56-4f9b-a6d7-758508eb0c1a.png align="center")

Vous utiliserez ces valeurs analogiques enregistrées pour le sol humide et sec dans la section suivante comme points de référence pour mapper les lectures futures sur une échelle de pourcentage. Dans l'exemple fourni plus tard dans ce tutoriel, le niveau d'humidité est exprimé en pourcentage, entre 0 % (sec) et 100 % (humide). L'utilisation des valeurs d'étalonnage garantit que la sortie en pourcentage reflète avec précision les conditions de votre type de sol.

## Exemple 1 – Comment déterminer le niveau d'humidité du sol en pourcentage à partir de la sortie analogique

Dans cet exemple, vous apprendrez à lire les données analogiques du capteur d'humidité du sol, à convertir la lecture analogique en une valeur en pourcentage et à représenter visuellement le niveau d'humidité à l'aide de cinq LEDs.

La lecture analogique du capteur est inversement proportionnelle au niveau d'humidité du sol. Cela signifie que des lectures analogiques plus élevées indiquent un sol plus sec et des lectures plus basses indiquent un sol plus humide.

Les LEDs servent d'indicateur visuel du pourcentage d'humidité. Les LEDs s'allument en fonction d'une plage de niveaux d'humidité du sol :

* 1 LED : 0-20 % (très sec)

* 2 LEDs : 20-40 %

* 3 LEDs : 40-60 %

* 4 LEDs : 60-80 %

* 5 LEDs : 80-100 % (très humide)

### Schéma de circuit

![Schéma de circuit pour l'exemple 1](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909722810/0aff204d-2ddd-44d5-80b5-5765b9cf5fe9.jpeg align="center")

En utilisant le schéma ci-dessus comme référence, concevez le circuit comme suit :

1. Connectez le capteur à l'Arduino de la même manière que celle décrite dans la section d'étalonnage. C'est-à-dire, connectez la broche d'alimentation du capteur (VCC) à la broche numérique 7, la broche de sortie analogique **AO** à la broche analogique **A0**, et la broche de masse à n'importe quelle broche de masse du microcontrôleur.

2. Connectez chacune des LEDs en série avec une résistance de 220 ohms.

3. Connectez l'anode des cinq LEDs aux broches numériques 3, 4, 5, 6 et 8 du microcontrôleur.

Voici à quoi ressemblait ma configuration :

![Configuration physique pour le projet 1](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909770251/226bd848-2a58-4e2f-9bf4-796a54983d47.jpeg align="center")

### Code Arduino

Téléchargez le croquis suivant sur votre Arduino :

```cpp
const int sensorPin = A0; // Entrée analogique du capteur d'humidité du sol
const int powerPin = 7; // Broche numérique pour alimenter le capteur

// Broches de la barre de LEDs (de la plus basse à la plus haute)
const int ledPins[5] = {3, 4, 5, 6, 8};

// Valeurs analogiques étalonnées - remplacez par vos valeurs
const int dryValue = 1005;
const int wetValue = 254;

// Variable globale pour stocker la dernière valeur analogique
int lastAnalogReading = 0;

// Lire et calculer le pourcentage d'humidité du sol
int getMoisturePercent(int analogPin, int powerPin, int samples = 10) {
  unsigned long total = 0;

  digitalWrite(powerPin, HIGH);
  delay(10); // Permettre au capteur de se stabiliser

  for (int i = 0; i < samples; i++) {
 total += analogRead(analogPin);
    delay(10);
 }

  digitalWrite(powerPin, LOW);

  int avgReading = total / samples;
 lastAnalogReading = avgReading;

  int percent = map(avgReading, dryValue, wetValue, 0, 100);
  return constrain(percent, 0, 100);
}

// Mettre à jour les états des LEDs en utilisant un tableau booléen
void updateLEDBar(int percent) {
  bool ledStates[5] = {0, 0, 0, 0, 0}; // Par défaut toutes éteintes

  if (percent <= 20) {
    ledStates[0] = true;
 } else if (percent <= 40) {
    ledStates[0] = ledStates[1] = true;
 } else if (percent <= 60) {
    ledStates[0] = ledStates[1] = ledStates[2] = true;
 } else if (percent <= 80) {
    ledStates[0] = ledStates[1] = ledStates[2] = ledStates[3] = true;
 } else {
    for (int i = 0; i < 5; i++) ledStates[i] = true;
 }

 // Écrire les états des LEDs sur les broches
  for (int i = 0; i < 5; i++) {
    digitalWrite(ledPins[i], ledStates[i] ? HIGH : LOW);
 }
}

void setup() {
  Serial.begin(9600);
  pinMode(sensorPin, INPUT);
  pinMode(powerPin, OUTPUT);
  digitalWrite(powerPin, LOW); // Démarrer avec le capteur éteint

  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW); // Assurer que toutes les LEDs démarrent éteintes
 }

  Serial.println("Moniteur d'humidité du sol avec barre de 5 LEDs (Tableau booléen)");
}

void loop() {
  int moisturePercent = getMoisturePercent(sensorPin, powerPin, 20);

 // Imprimer à la fois la lecture analogique et le pourcentage
  Serial.print("Lecture analogique : ");
  Serial.print(lastAnalogReading);
  Serial.print("  |  Humidité : ");
  Serial.print(moisturePercent);
  Serial.println(" %");

  updateLEDBar(moisturePercent);

  delay(2000); // Mise à jour toutes les 2 secondes
}
```

Dans le croquis, vous commencez par définir la broche analogique pour lire les données du capteur et la broche numérique pour alimenter le capteur. Vous définissez également les variables suivantes, qui seront utilisées dans le code :

* `ledPins[5]` – Un tableau qui stocke les broches numériques utilisées pour alimenter chaque LED. Les broches sont disposées de la première LED à la dernière. C'est l'ordre d'affichage visuel de gauche à droite.

* `dryValue` – Cette variable stocke la valeur analogique enregistrée pour un sol sec pendant la section d'étalonnage.

* `wetValue` – Cette variable stocke la valeur analogique enregistrée pour un sol humide pendant la section d'étalonnage.

* `lastAnalogReading` – Cette variable stocke la dernière lecture prise par le capteur. Vous utilisez cette variable pour enregistrer la lecture analogique réelle sur le moniteur série.

La fonction `getMoisturePercent` alimente le capteur, prend plusieurs lectures, éteint le capteur, calcule la lecture analogique moyenne, représente la lecture analogique en pourcentage et retourne la valeur en pourcentage. La fonction sauvegarde également la lecture analogique moyenne dans la variable `lastAnalogReading`. Vous pouvez l'imprimer directement ici, mais ce croquis la sauvegarde dans une variable séparée afin que vous puissiez l'imprimer plus tard dans la fonction `loop` pour une meilleure lisibilité.

Vous pouvez exprimer la lecture analogique moyenne en pourcentage avec la fonction `map(avgReading, dryValue, wetValue, 0, 100)`. La fonction remappe la lecture moyenne stockée dans `avgReading` de la plage de vos valeurs d'étalonnage `dryValue` et `wetValue` à une nouvelle plage entre `0` et `100` (où `0` est le plus sec et `100` est le plus humide). Vous utilisez ensuite la fonction `constrain` pour maintenir les valeurs dans la plage `0` et `100`.

La fonction `updateLEDBar` affiche la valeur en pourcentage à l'aide des LEDs. Le tableau `ledStates` dans la fonction stocke l'état logique de chaque LED. Vous commencez par éteindre toutes les LEDs – c'est-à-dire avoir un état `0`. La partie suivante de la logique est une simple instruction `if` où vous allumez les LEDs requises correspondant à une plage de pourcentage particulière en définissant les éléments du tableau sur `true` (équivalent à `1`). Vous terminez la fonction en écrivant les états dans `ledStates` sur les broches dans `ledPins`.

La fonction `setup` est assez routinière : vous définissez le débit en bauds pour la communication série, définissez les broches numériques d'entrée et de sortie, et écrivez un `LOW` sur les broches de sortie numérique pour vous assurer qu'elles sont toutes éteintes au démarrage.

Dans la fonction `loop`, vous appelez la fonction `getMoisturePercent` pour obtenir la valeur de pourcentage d'humidité. Vous imprimez ensuite la valeur en pourcentage et la lecture analogique moyenne sur le moniteur série pour plus de clarté. Enfin, vous appelez la fonction `updateLEDBar` avec la valeur en pourcentage comme paramètre pour allumer les LEDs respectives afin d'indiquer le niveau d'humidité.

### Tester le système

Vous pouvez procéder au test de l'exemple avec différents niveaux d'humidité. Par exemple :

* À environ 37 % d'humidité, deux LEDs sont allumées.

![Test exemple 1 avec 37 % d'humidité](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909854736/5312e441-d9fd-498f-bd87-b902231b27f4.jpeg align="left")

* À environ 76 % d'humidité, quatre LEDs sont allumées.

![Test exemple 1 avec 76 % d'humidité](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909910096/eabf2f8d-7499-4c6a-be49-74d4c8a3da30.jpeg align="left")

Vous pouvez également simuler l'exemple sur Tinkercad ici : [https://www.tinkercad.com/embed/6s47ZvIrNOP](https://www.tinkercad.com/embed/6s47ZvIrNOP).

![Image de simulation Tinkercad de l'exemple 1](https://cdn.hashnode.com/res/hashnode/image/upload/v1752100775640/12f92988-7697-4069-9068-86f663b20794.png align="center")

## Exemple 2 – Comment déterminer l'état d'humidité du sol à partir de la sortie numérique

Dans le projet précédent, vous avez appris à lire les données analogiques du capteur et à convertir la valeur en pourcentage. Si votre application nécessite une sortie binaire, vous pouvez utiliser la broche de sortie numérique. Dans cette section, vous apprendrez à utiliser la broche de sortie numérique du capteur.

La broche de sortie numérique n'a que deux états :

* `LOW` – Cet état correspond à 0V et est la sortie lorsque le sol est humide, c'est-à-dire que le niveau d'humidité est supérieur au seuil défini.

* `HIGH` – Cet état correspond à 5V et est la sortie lorsque le sol est sec, c'est-à-dire que le niveau d'humidité est inférieur au niveau d'humidité seuil.

### Schéma de circuit

L'exemple construit dans cette section est très simple. Il se compose d'une LED rouge et verte. Lorsque le capteur émet un signal `LOW` à partir de la broche de sortie numérique, ce qui signifie que le sol est humide, la LED verte s'allume. Lorsque le capteur émet un signal `HIGH` à partir de la broche de sortie numérique, ce qui signifie que le sol est sec, la LED rouge s'allume.

![Schéma de circuit pour l'exemple 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751909967743/761e3422-ad95-4f8e-9b4d-4963970c926e.jpeg align="left")

En utilisant le schéma de circuit ci-dessus comme référence, concevez le circuit comme suit :

1. Placez le module du capteur sur la plaque d'essai.

2. Comme dans le projet précédent, connectez la broche d'alimentation (VCC) du module du capteur à la broche numérique 7 du microcontrôleur, et la broche de masse (GND) à une broche de masse du microcontrôleur.

3. Connectez la broche de sortie numérique (DO) du capteur à la broche numérique 2 du microcontrôleur. Cette broche est celle où vous lirez les données du capteur.

4. Connectez les LEDs rouge et verte chacune à une résistance de 220 ohms en série.

5. Connectez l'anode des LEDs rouge et verte aux broches numériques 12 et 13 du microcontrôleur, respectivement.

Voici à quoi ressemblait ma connexion physique :

![Configuration physique pour l'exemple 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1751910000801/55382b8f-cdd4-4f85-9b6a-342af252329b.jpeg align="left")

### Comment définir le niveau d'humidité seuil

Avant d'utiliser la broche de sortie numérique du module du capteur de sol, vous devez d'abord définir un niveau d'humidité seuil.

Le module du capteur possède un potentiomètre intégré qui vous permet d'ajuster le niveau d'humidité, qui sera utilisé comme seuil. Le capteur possède également un comparateur LM393 intégré, qui compare en continu la lecture réelle du capteur au seuil défini par le potentiomètre et émet l'état approprié.

Vous pouvez définir le niveau d'humidité seuil en tournant le bouton du potentiomètre. Tourner le potentiomètre dans le sens des aiguilles d'une montre abaisse le seuil. Tourner le potentiomètre dans le sens inverse des aiguilles d'une montre élève le seuil. Le module du capteur possède également une LED intégrée étiquetée **DO-LED** qui s'allume lorsque la sortie du capteur est `LOW`. Définissez le seuil comme suit :

1. Placez la sonde du capteur dans un sol juste assez sec pour nécessiter une irrigation. C'est-à-dire le sol dont le niveau d'humidité vous souhaitez utiliser comme seuil. Notez que la DO-LED doit être éteinte.

2. Utilisez un petit tournevis pour tourner le potentiomètre dans le sens des aiguilles d'une montre jusqu'à ce que la DO-LED s'allume. Tourner dans le sens des aiguilles d'une montre réduit le niveau de seuil jusqu'à ce qu'il soit légèrement inférieur au niveau d'humidité actuel, déclenchant ainsi l'indicateur de sortie numérique (DO-LED) pour s'allumer.

3. Tournez la vis légèrement dans le sens inverse des aiguilles d'une montre juste assez pour éteindre la LED numérique intégrée. Étant donné que le niveau d'humidité actuel du sol est suffisamment sec pour nécessiter un arrosage, vous souhaitez toujours que le capteur lise ce niveau comme sec. Ainsi, tourner dans le sens inverse des aiguilles d'une montre réduit le seuil à un niveau juste au-dessus du niveau d'humidité actuel du sol, ce qui déclenche l'extinction de la DO-LED.

### Code Arduino

Téléchargez le croquis suivant sur l'Arduino :

```cpp
const int sensorPower = 7; // Broche numérique pour alimenter le capteur
const int sensorPin = 2; // Entrée numérique du capteur
const int greenLED = 13; // Broche de la LED verte
const int redLED = 12; // Broche de la LED rouge

int getSensorReading(int digitalPin, int powerPin) {  
  digitalWrite(powerPin, HIGH); // Alimentation ON du capteur
  delay(500); // Attendre que le capteur se stabilise

  int reading = digitalRead(digitalPin);

  digitalWrite(powerPin, LOW); // Alimentation OFF du capteur
  return reading;
}

void setup() {
  Serial.begin(9600);
  
  pinMode(sensorPower, OUTPUT);
  pinMode(sensorPin, INPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);

 // Assurer que tout démarre éteint
  digitalWrite(sensorPower, LOW);
  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW);
}

void loop() {
  int sensorReading = getSensorReading(sensorPin, sensorPower);

  Serial.println("===================================");
  Serial.print("Lecture numérique : ");
  Serial.println(sensorReading);

  if (sensorReading == HIGH) {
    Serial.println("Statut : L'humidité du sol est FAIBLE (sec)");
    Serial.println("Action : Arroser le sol");
    digitalWrite(redLED, HIGH);
    digitalWrite(greenLED, LOW);
 } else {
    Serial.println("Statut : L'humidité du sol est BONNE (humide)");
    Serial.println("Action : Aucun arrosage nécessaire");
    digitalWrite(greenLED, HIGH);
    digitalWrite(redLED, LOW);
 }

  Serial.println("===================================");
  Serial.println(); 
  delay(2000); // Mise à jour toutes les 2 secondes
}
```

Dans le croquis, vous définissez la broche numérique utilisée pour lire les données du capteur, les broches numériques pour alimenter le capteur, et les LEDs verte et rouge.

La fonction `getSensorReading` alimente le capteur, prend la lecture numérique du capteur, éteint le capteur et retourne la lecture numérique prise à partir du capteur.

La fonction `setup` est routinière : vous définissez le débit en bauds, définissez les broches numériques comme entrée ou sortie, et écrivez un `LOW` sur les broches de sortie pour vous assurer qu'elles sont éteintes au démarrage.

Dans la fonction `loop`, vous appelez `getSensorReading` pour obtenir la lecture numérique du capteur. Si le capteur émet un signal `HIGH`, vous allumez la LED rouge et imprimez un message indiquant que le sol est sec. Si le capteur émet un signal `LOW`, vous allumez la LED verte et imprimez un message indiquant que le sol est humide.

### Tester le système

Vous pouvez procéder au test du projet en utilisant différents niveaux d'humidité. Par exemple :

* Pour un sol humide, c'est-à-dire si le niveau d'humidité est supérieur au seuil, vous devriez avoir la sortie suivante :

![Test exemple 2 avec un sol humide](https://cdn.hashnode.com/res/hashnode/image/upload/v1751910035826/19edc7e0-09a2-404a-8ce4-fb978c5b9f6b.jpeg align="left")

* Pour un sol sec, c'est-à-dire si le niveau d'humidité est inférieur au seuil, vous devriez avoir la sortie suivante :

![Test exemple 2 avec un sol sec](https://cdn.hashnode.com/res/hashnode/image/upload/v1751910068607/33881bb3-ba7b-41fd-a637-001016298312.jpeg align="left")

Vous pouvez également simuler l'exemple sur Tinkercad ici : [https://www.tinkercad.com/embed/2wHwfKherNz](https://www.tinkercad.com/embed/2wHwfKherNz).

![Simulation Tinkercad de l'exemple 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1752100906816/cd1b3de4-f5e6-4760-ab03-8f46443ba270.png align="center")

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est un capteur résistif d'humidité du sol, comment étalonner le capteur pour votre type de sol, et comment utiliser les données analogiques et numériques du capteur pour déterminer le niveau d'humidité du sol.

Les exemples fournis constituent une base solide pour travailler avec le capteur. Vous pouvez étendre ces exemples à des projets plus complexes, tels qu'un système d'irrigation automatisé ou une surveillance à distance de l'humidité du sol.

Pour les projets nécessitant une plus grande précision et un fonctionnement fréquent ou soutenu du capteur, vous devriez explorer le capteur capacitif.

Vous pouvez accéder à tout le code sur [GitHub](https://github.com/michaelikoko/resistive-soil-moisture-sensor).