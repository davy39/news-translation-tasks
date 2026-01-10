---
title: 'Chapitre 1 : Premiers pas avec Arduino'
date: '2023-10-05T13:15:02.000Z'
author: Ihechikara Abba
authorURL: https://www.freecodecamp.org/news/author/Ihechikara/
originalURL: https://freecodecamp.org/news/the-arduino-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/The-Arduino-Handbook-Cover.png
tags:
- name: arduino
  slug: arduino
- name: embedded systems
  slug: embedded-systems
- name: handbook
  slug: handbook
seo_desc: 'Arduino is an open-source platform that combines hardware and software
  in designing and building electronic projects.

  Arduino can be applied in a variety of projects like:


  Home automation.

  Internet of Things (IoT).

  Audio and music.

  Automated and rem...'
---


Arduino est une plateforme open-source qui combine matériel (hardware) et logiciel (software) pour la conception et la fabrication de projets électroniques.

<!-- more -->

Arduino peut être utilisé dans une grande variété de projets tels que :

-   La domotique.
-   L'Internet des Objets (IoT).
-   L'audio et la musique.
-   Les systèmes automatisés et télécommandés.
-   L'automatisation dans l'agriculture.
-   Le prototypage électronique.
-   Les appareils connectés (wearables), et bien plus encore.

La partie matérielle d'Arduino comprend les cartes Arduino, les périphériques d'entrée et de sortie (incluant les broches numériques et analogiques, les capteurs et les actionneurs), les shields, les breadboards, les fils de liaison (jumpers), etc. Ces composants peuvent être combinés pour créer des projets dynamiques et interactifs.

Le logiciel est composé des outils de développement utilisés pour écrire, déboguer, compiler et téléverser du code sur les cartes Arduino. La plupart des outils logiciels se trouvent dans l'IDE Arduino (Environnement de Développement Intégré).

Ce guide vous aidera à comprendre comment fonctionne Arduino. Vous découvrirez les cartes Arduino, les composants qui constituent une carte et comment y connecter des périphériques.

Nous parlerons des périphériques d'entrée et de sortie qui aident le microcontrôleur (le cerveau de la carte Arduino) à traiter les informations provenant de l'environnement physique et à envoyer des sorties basées sur une logique programmée.

Vous découvrirez l'IDE Arduino, comment coder en utilisant le langage de programmation Arduino, et comment utiliser des capteurs, des actionneurs et d'autres composants pour construire des projets au fur et à mesure de votre apprentissage.

Vous découvrirez également la communication série, qui permet aux cartes Arduino de communiquer avec d'autres ordinateurs.

Ce guide est écrit pour les makers (étudiants, artistes, passionnés, programmeurs) qui sont débutants.

## Prérequis

Bien que cela soit utile, vous n'avez pas besoin de connaissances préalables en programmation pour utiliser ce guide. Vous apprendrez les bases de la programmation Arduino à partir de zéro. Cela peut également servir d'introduction à la programmation.

Pour faciliter l'apprentissage des débutants, nous n'aborderons pas certains aspects de l'électronique comme le courant et la tension, la résistance, les circuits (série et parallèle), et la plupart des lois et exigences électroniques/électriques de base pour les étudiants des domaines STIM (Sciences, Technologie, Ingénierie, Mathématiques).

Que vous connaissiez ces concepts ou non, vous pouvez apprendre Arduino grâce à ce guide.

Si vous savez utiliser une breadboard et une résistance, c'est tout ce dont vous aurez besoin en électronique pour suivre.

En résumé, ce guide s'adresse à tout le monde. Vous n'avez pas besoin d'un diplôme d'ingénieur pour devenir un maker Arduino !

## Table des matières :

-   [Prérequis][1]
-   [Chapitre 1 : Premiers pas avec Arduino][2]
-   [Chapitre 2 : Les bases de la programmation Arduino][3]
-   [Chapitre 3 : Comment utiliser les broches numériques avec Arduino][4]
-   [Chapitre 4 : Comment utiliser les broches analogiques avec Arduino][5]
-   [Chapitre 5 : Comment utiliser les capteurs et les actionneurs avec Arduino][6]
-   [Chapitre 6 : Comment utiliser le moniteur série avec Arduino][7]
-   [Chapitre 7 : Comment utiliser les écrans avec Arduino][8]

# Chapitre 1 : Premiers pas avec Arduino

Le processus de développement et de conception Arduino comprend à la fois du matériel et du logiciel. Il est donc important de savoir comment ils fonctionnent ensemble pour construire les bases solides de votre parcours.

Dans ce chapitre, vous découvrirez les différents composants qui constituent la carte Arduino Uno. Vous apprendrez également à installer l'IDE Arduino et à configurer votre environnement de développement.

Au moment de la rédaction de ce texte, une nouvelle carte Uno a été publiée — l'Arduino Uno R4. Ce guide utilisera la carte Uno R3, mais vous pouvez suivre avec l'une ou l'autre. La carte R4 existe en deux variantes — Arduino Uno R4 WiFi et Arduino Uno R4 Minima — avec de nouvelles fonctionnalités intéressantes que vous pouvez découvrir [ici][9].

## Composants de la carte Arduino Uno R3

Il existe de nombreux types de cartes Arduino comme l'Arduino Nano, l'Arduino Uno, l'Arduino Mega, l'Arduino Leonardo, etc.

Ces cartes ont des caractéristiques communes — elles ont toutes des broches numériques et de sortie, elles sont programmables et elles possèdent toutes un microcontrôleur.

Mais il existe aussi des différences. Chaque carte varie en taille et en forme, et possède généralement plus ou moins de composants par rapport aux autres cartes.

Les cartes les plus courantes que vous rencontrerez en tant que débutant sont les cartes Nano, Uno et Mega. La plus utilisée est la carte Uno, que nous utiliserons pour ce guide.

Voici quelques-uns des composants que vous trouverez sur la carte Uno R3 :

-   Un port d'alimentation.
-   Un connecteur USB.
-   Un microcontrôleur (ATmega328).
-   Des broches analogiques.
-   Des broches numériques.
-   Un bouton de réinitialisation (reset).
-   Des indicateurs TX et RX.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/UnoR3.png) _Carte Arduino Uno R3 (https://store.arduino.cc/products/arduino-uno-rev3)_

Vous utiliserez la plupart des composants listés ci-dessus au fur et à mesure de votre progression dans ce guide.

## Comment installer et configurer l'IDE Arduino

Vous pouvez utiliser l'IDE Arduino pour programmer les cartes Arduino. C'est-à-dire que vous écrivez le code dans l'IDE, puis vous le téléversez sur la carte.

Dans cette section, vous apprendrez à configurer l'IDE et à créer votre premier programme Arduino (également appelé sketch Arduino).

Vous pouvez télécharger la dernière version de l'IDE Arduino sur la [page de téléchargement du logiciel Arduino][10]. Vous pouvez télécharger l'IDE pour différents systèmes d'exploitation — Windows, MacOS et Linux.

Le processus d'installation est similaire pour les systèmes d'exploitation listés ci-dessus. Voici comment l'installer sur une machine Windows :

### Étape #1 – Télécharger l'IDE Arduino

La première étape consiste à télécharger l'IDE depuis la [page de téléchargement du logiciel Arduino][11]. Vous devriez voir une section de la page similaire à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/arduino-download-page-options.PNG)

Sur le côté droit de l'image ci-dessus se trouvent différentes options de téléchargement pour des systèmes d'exploitation spécifiques. Assurez-vous de télécharger l'option qui correspond à votre système d'exploitation.

J'utiliserai l'option du fichier ZIP pour Windows. Si vous décidez de télécharger un installateur à la place, vous pourrez suivre les étapes d'installation après avoir cliqué sur le fichier d'installation.

### Étape #2 – Décompresser le fichier téléchargé

Allez-y et décompressez le fichier téléchargé. Cela vous donne accès à toutes les ressources nécessaires pour exécuter l'IDE Arduino.

Après avoir décompressé le fichier, vous devriez voir des fichiers comme ceux-ci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/arduino-ide-unzipped.PNG) _Image montrant les fichiers que vous devriez voir_

Pour lancer l'IDE Arduino, cliquez sur le fichier nommé "Arduino IDE".

### Étape #3 – Aperçu de l'IDE Arduino

Maintenant que vous avez téléchargé et installé l'IDE Arduino, la partie suivante consiste à vous familiariser avec l'environnement de développement. Dans la section suivante, vous apprendrez comment téléverser du code sur une carte Arduino Uno en utilisant l'IDE.

Avant cela, jetons un coup d'œil à certaines options que vous trouverez dans l'IDE Arduino. Dans le coin supérieur gauche de l'IDE se trouvent cinq options — File (Fichier), Edit (Édition), Sketch (Croquis), Tools (Outils), Help (Aide) :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/ide.png) _Capture d'écran montrant ces options (File, Edit, Sketch, Tools, Help)_

L'option "File" vous permet de faire différentes choses comme créer un nouveau sketch (nous parlerons des sketches dans la section suivante), ouvrir un sketch existant, accéder à des exemples d'entraînement Arduino pour débutants, aux raccourcis clavier, aux options d'enregistrement, etc.

L'option "Edit" vous donne accès aux options de formatage de texte comme copier, coller, couper, commenter/décommenter le code, aux options de taille de police, aux options de recherche de texte, etc.

Vous pouvez utiliser l'option "Sketch" pour vérifier et compiler le code, téléverser le code sur les cartes Arduino, optimiser le code et ajouter des bibliothèques.

Vous pouvez utiliser l'option "Tools" pour gérer les bibliothèques, formater le code, accéder au moniteur série et au traceur série, sélectionner une carte Arduino et un port pour téléverser le code, choisir un processeur, etc.

L'option "Help" fournit des ressources pour le dépannage, des informations sur les mises à jour de l'IDE, des guides de démarrage, etc.

Ensuite, examinons d'autres parties et fonctionnalités de l'IDE que vous trouverez utiles. L'image ci-dessous, provenant de la [documentation Arduino][12], les met parfaitement en évidence :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/arduino-ide-icons.png) _[https://docs.arduino.cc/software/ide-v2/tutorials/getting-started-ide-v2][13]_

-   **Verify/Upload** : Vous pouvez utiliser ces options pour compiler et téléverser du code sur les cartes Arduino. Vous recevrez des messages d'erreur si le code ne se compile pas comme prévu.
-   **Select Board & Port** : Vous pouvez utiliser cette option pour sélectionner une carte et un numéro de port pour téléverser votre code. La version actuelle de l'IDE Arduino détecte automatiquement les cartes et les ports.
-   **Sketchbook** : Cela vous donne accès à tous les sketches créés sur votre ordinateur. Vous pouvez également accéder aux sketches enregistrés sur Arduino Cloud (principalement utilisé pour créer des projets IoT).
-   **Boards Manager** : L'IDE Arduino prend en charge différentes cartes. Au fur et à mesure de votre parcours, vous utiliserez différentes cartes et certaines d'entre elles pourraient ne pas être supportées par défaut par l'IDE. L'onglet Boards Manager vous permet d'installer et de gérer les packages requis pour utiliser ces cartes.
-   **Library Manager** : Vous pouvez utiliser des bibliothèques pour étendre certaines fonctionnalités du code. Grâce au Library Manager, vous pouvez installer de nombreuses bibliothèques qui vous aideront à simplifier le processus de développement.
-   **Debugger** : Utilisé pour le test et le débogage en temps réel des programmes Arduino.
-   **Search** : Vous pouvez utiliser l'outil de recherche pour trouver des mots-clés spécifiques dans votre code.
-   **Open Serial Monitor** : Vous pouvez utiliser le moniteur série pour communiquer avec les cartes Arduino, déboguer et tester le code, visualiser les données de vos cartes, interagir avec les entrées utilisateur, etc. Nous examinerons le moniteur série en profondeur dans un chapitre dédié.
-   **Open Serial Plotter** : Le traceur série est principalement utilisé pour la visualisation en temps réel de données numériques.

## Qu'est-ce qu'un sketch Arduino ?

Nous avons mentionné le terme "sketch" à plusieurs reprises dans la section précédente, mais de quoi s'agit-il ? Un sketch est un programme écrit avec le langage de programmation Arduino. C'est une autre façon de désigner un fichier de code écrit pour les projets Arduino.

Le langage de programmation Arduino est basé sur le langage C/C++, ils partagent donc une syntaxe et une structure similaires. Vous rencontrerez peut-être des ressources qui désignent le code Arduino comme du "C embarqué" ou du "C++ embarqué".

## Comment téléverser du code sur une carte Arduino

Pour téléverser du code sur une carte Arduino, vous aurez besoin à la fois de matériel et de logiciel. Le matériel est la carte, qui est la carte Uno dans notre cas, et le logiciel est le sketch Arduino dans l'IDE.

Voici les étapes :

### Étape #1 – Connecter la carte Arduino

Connectez la carte Arduino à votre ordinateur à l'aide du câble USB. Sans cette étape, vous ne pouvez pas aller plus loin.

### Étape #2 – Créer un sketch

Il est maintenant temps de lancer l'IDE et d'écrire du code.

Voici un exemple de code qui fait clignoter une LED :

```
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
```

Ne vous inquiétez pas si vous ne comprenez pas le code — nous couvrirons tout au fur et à mesure.

### Étape #3 – Sélectionner la carte et le port

Vous pouvez sélectionner la carte sur laquelle téléverser votre code depuis l'IDE. Voici une image montrant à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/port.png)

### Étape #4 – Vérifier le code

Vous pouvez utiliser le bouton "Verify" pour compiler le code et vérifier les erreurs. Si des erreurs existent, vous recevrez un message d'erreur indiquant la cause possible.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/verify.png) _Image montrant le bouton de vérification_

### Étape #5 – Téléverser le code

Vous pouvez téléverser le code en utilisant le bouton "Upload" (le bouton situé après le bouton de vérification).

S'il n'y a pas d'erreurs dans votre code, ces étapes aideront à téléverser le code sur votre carte. Si vous avez téléversé le code ci-dessus, vous devriez voir la LED intégrée (elle est connectée à la broche 13 par conception) sur la carte Uno clignoter.

Dans le chapitre suivant, vous apprendrez les bases du langage de programmation Arduino.

# Chapitre 2 : Les bases de la programmation Arduino

Avant de plonger dans la création de nos propres sketches et de commencer à bricoler, vous devez comprendre la logique qui permet à ces cartes de fonctionner comme prévu. Pour ce faire, vous devrez savoir comment coder en utilisant le langage de programmation Arduino.

Comme nous l'avons vu au chapitre précédent, le langage Arduino est basé sur le C/C++. Vous commencerez ce chapitre par l'apprentissage des bases de la programmation. Cela vous préparera pour tous les autres chapitres impliquant l'écriture de code.

J'ai conçu ce chapitre en pensant aux débutants. Si vous n'avez jamais écrit de code auparavant, cela peut vous servir de point de départ. Cela ne signifie pas que vous apprendrez à coder en C ou C++. Vous apprendrez à écrire du code Arduino qui partage une syntaxe similaire avec ces langages.

À la fin de ce chapitre, vous devriez être capable de comprendre et d'écrire du code Arduino.

## Variables et types de données dans Arduino

Les variables et les types de données sont utilisés dans la plupart des langages de programmation pour stocker et manipuler des données. Vous pouvez considérer les variables comme des conteneurs ou des unités de stockage. Les types de données, comme leur nom l'indique, sont le type de données stockées dans les variables.

En programmation Arduino, vous devez spécifier le type de données d'une variable avant de l'utiliser. C'est-à-dire :

```
dataType variableName = variableValue
```

Il existe différents types de données dans Arduino, et nous allons discuter de chacun d'eux avec des exemples de code.

### Type de données `int` dans Arduino

Le type de données `int` est utilisé pour stocker des valeurs entières. La carte Uno a une capacité d'entier de 16 bits, elle peut donc stocker des valeurs comprises entre -32 768 et 32 767.

```
int redLED = 6;
```

Dans le code ci-dessus, nous avons créé une variable entière appelée `redLED` avec une valeur de 6.

Le type de données `int` peut également stocker des entiers négatifs :

```
int redLED = -6;
```

### Type de données `long` dans Arduino

Le type de données `long` est similaire à `int` mais possède une plage de valeurs entières plus large. Il a une limite d'entier de 32 bits, comprise entre -2 147 483 648 et 2 147 483 647.

```
long largeNumber = 6000;
```

### Type de données `float` dans Arduino

Le type de données `float` peut être utilisé pour stocker des nombres décimaux. Les variables de type float peuvent stocker des valeurs allant jusqu'à 3,4028235E+38 et aussi basses que -3,4028235E+38.

```
float num = 10.5;
```

Bien que le type de données `float` soit principalement utilisé pour les nombres décimaux, il peut également accepter des nombres entiers. Mais il retournera toujours une valeur flottante. Donc, si vous stockez 10 dans un `float`, il retournera 10.00.

### Type de données `String` dans Arduino

Vous pouvez utiliser le type de données `String` pour stocker et manipuler du texte. Vous travaillerez occasionnellement avec des chaînes de caractères pour afficher des informations sous forme de texte lors de la construction de projets.

Voici un exemple de code :

```
String greeting = "Hello World!";
```

La valeur des chaînes de caractères est placée entre doubles guillemets, comme on peut le voir dans le code ci-dessus.

Notez que lors de la déclaration d'une chaîne, le "S" doit toujours être en majuscule.

### Type de données `char` dans Arduino

Le type de données `char` stocke des caractères uniques.

Voici un exemple :

```
char alphabet = 'A';
```

C'est différent du type de données `String` qui peut stocker plusieurs caractères.

Il existe deux différences principales entre `char` et `String` :

-   `char` utilise des guillemets simples ('A') tandis que `String` utilise des guillemets doubles ("Arduino").
-   `char` stocke des caractères uniques tandis que `String` stocke plusieurs caractères.

`char` peut également accepter des valeurs entières équivalentes à la valeur [ASCII][14] des lettres :

```
char charValue = 65;
```

Dans le code ci-dessus, nous avons initialisé une variable `char` avec la valeur 65. Lorsqu'elle est affichée sur le moniteur série (nous parlerons du moniteur série au [Chapitre 6 : Comment utiliser le moniteur série avec Arduino][15]), A sera retourné.

A est retourné car 65 correspond au caractère ASCII de A.

### Types de données `bool` et `boolean` dans Arduino

Vous pouvez utiliser à la fois `bool` et `boolean` pour stocker/désigner des valeurs booléennes soit `true` (vrai) soit `false` (faux).

```
bool roomIsCold = false;
```

Les valeurs booléennes sont principalement utilisées avec des opérateurs logiques et de comparaison, et des instructions conditionnelles (vous en apprendrez plus tard dans ce chapitre) pour manipuler et contrôler différents résultats dans un programme Arduino.

### Type de données `byte` dans Arduino

Le type de données `byte` a une limite d'entier non signé de 8 bits allant de 0 à 255. "Non signé" signifie qu'il ne peut pas stocker de valeurs négatives.

```
byte sensorValue = 200;
```

Le type de données `byte` n'est pas le seul type de données qui peut être non signé. Vous pouvez également utiliser les types de données `unsigned int`, `unsigned long` et `unsigned char` qui ont tous leurs plages d'entiers positifs respectives.

## Opérateurs dans Arduino

Les opérateurs sont des symboles ou des caractères qui peuvent être utilisés pour effectuer certaines opérations sur des opérandes. Un opérande est simplement toute valeur sur laquelle un opérateur agit.

Il existe différentes catégories d'opérateurs dans Arduino comme :

### Opérateurs arithmétiques

Les opérateurs arithmétiques sont utilisés pour effectuer des opérations mathématiques comme l'addition, la soustraction, la division, la multiplication, etc. Voici quelques opérateurs arithmétiques que vous devriez connaître :

#### Opérateur d'addition (+)

L'opérateur d'addition, désigné par le symbole `+`, additionne deux opérandes :

```
int a = 5;
int b = 10;

// nous utilisons l'opérateur d'addition pour additionner a et b ci-dessous
int c = a + b;

Serial.print(c);
// 15
```

#### Opérateur de soustraction (-)

L'opérateur de soustraction soustrait la valeur d'un opérande d'un autre opérande. Il est désigné par le symbole `-` :

```
int a = 5;
int b = 10;

// nous utilisons l'opérateur de soustraction pour soustraire a de b ci-dessous
int c = b - a;

Serial.print(c);
// 5
```

#### Opérateur de multiplication (*)

Vous pouvez utiliser l'opérateur de multiplication (`*`) pour multiplier deux opérandes :

```
int a = 5;
int b = 10;

// nous utilisons l'opérateur de multiplication pour multiplier a par b ci-dessous
int c = a * b;

Serial.print(c);
// 50
```

#### Opérateur de division (/)

L'opérateur de division divise un opérande par un autre :

```
int a = 5;
int b = 10;

// nous utilisons l'opérateur de division pour diviser b par a ci-dessous
int c = b / a;

Serial.print(c);
// 2
```

#### Opérateur modulo (%)

L'opérateur modulo retourne le reste d'une division entre deux opérandes :

```
int a = 5;
int b = 10;

// nous utilisons l'opérateur modulo pour diviser b par a ci-dessous
int c = b % a;

Serial.print(c);
// 0
```

#### Opérateur d'incrémentation (++)

L'opérateur d'incrémentation augmente la valeur d'une variable de 1 :

```
int num = 5;
num++;

Serial.print(num);
// 6
```

#### Opérateur de décrémentation (--)

L'opérateur de décrémentation diminue la valeur d'une variable de 1 :

```
int num = 5;
num--;

Serial.print(num);
// 4
```

### Opérateurs d'affectation

Les opérateurs d'affectation sont principalement utilisés pour attribuer des valeurs aux variables. Vous pouvez également les utiliser pour mettre à jour la valeur des variables.

L'opérateur d'affectation (`=`) est utilisé pour affecter et mettre à jour des variables. L'opérateur `=` ne doit pas être confondu avec "égal à" — ils ne sont pas identiques. Nous parlerons de l'opérateur "égal à" (`==`) dans la section des opérateurs de comparaison.

Voici un exemple montrant comment utiliser l'opérateur d'affectation :

```
int age = 1;
```

Dans le code ci-dessus, nous avons créé une variable appelée `age`, puis nous lui avons affecté la valeur 1 en utilisant l'opérateur `=`.

Mais ce n'est pas la seule façon d'affecter ou de mettre à jour la valeur des variables lors de l'utilisation de l'opérateur `=`. Vous pouvez également utiliser des opérateurs d'affectation composée.

#### Opérateurs d'affectation composée

Les opérateurs d'affectation composée vous permettent de combiner des opérateurs arithmétiques et l'opérateur `=`. Cette méthode offre une façon plus courte d'écrire le code. Voici un exemple :

```
int x = 5;
x += 5;

Serial.print(x)
// 10
```

Dans le code ci-dessus, nous avons créé une variable `x` et lui avons affecté la valeur 5. Mais sur la deuxième ligne, vous verrez que nous avons combiné l'opérateur arithmétique d'addition (`+`) et l'opérateur `=` pour affecter une nouvelle valeur à `x` :

```
x += 5;
```

La ligne de code ci-dessus est identique à celle-ci :

```
x = x + 5;
```

Ainsi, les opérateurs composés combinent deux opérateurs et vous permettent de faire la même chose de manière plus concise. Il n'y a rien de mal avec l'une ou l'autre méthode.

Voici d'autres exemples d'opérateurs composés :

```
int a = 10;
a -= 5; // Équivalent à a = a - 5 (a devient 5)

int b = 10;
b *= 5; // Équivalent à b = b * 5 (b devient 50)

int c = 10;
c /= 5; // Équivalent à c = c / 5 (c devient 2)

int d = 10;
d %= 5; // Équivalent à d = d % 3 (d devient 0)
```

### Opérateurs de comparaison

Vous pouvez utiliser les opérateurs de comparaison pour comparer deux valeurs/opérandes. Les opérateurs de comparaison retournent soit `true` (1), soit `false` (0) selon la relation entre les opérandes.

Les opérateurs de comparaison peuvent vous aider à prendre des décisions basées sur leurs valeurs de retour. Vous les verrez beaucoup lorsque nous commencerons à construire des projets.

Voici les opérateurs de comparaison que vous rencontrerez occasionnellement :

#### Opérateur égal à (==)

Cet opérateur compare les valeurs de deux variables. Si les valeurs sont identiques, il retourne `true`. Si les valeurs ne sont pas identiques, il retourne `false`. Voici un exemple :

```
int x = 10;
int y = 5; 

Serial.print(x == y)
// retourne 0
```

La valeur de retour de `x == y` dans le code ci-dessus est 0 (`false`) car les deux variables ne sont pas identiques. Rappelez-vous que l'opérateur `==` ne retourne 1 (`true`) que lorsque les deux variables ont la même valeur.

#### Opérateur différent de (!=)

L'opérateur différent de vérifie si deux valeurs sont différentes. Il fait l'opposé de l'opérateur `==`. Cela signifie qu'il retournera 1 (`true`) si les deux valeurs ne sont pas identiques et 0 (`false`) si les deux valeurs sont identiques.

Voici un exemple :

```
int x = 10;
int y = 5; 

Serial.print(x != y)
// retourne 1
```

#### Opérateur supérieur à (>)

L'opérateur supérieur à (`>`) vérifie si l'opérande de gauche est supérieur à l'opérande de droite. Si l'opérande de gauche est supérieur, il retourne 1. Si l'opérande de gauche est plus petit, il retourne 0.

```
int x = 10;
int y = 5; 

Serial.print(x > y)
// retourne 1
```

#### Opérateur inférieur à (<)

L'opérateur inférieur à (`<`) vérifie si l'opérande de gauche est inférieur à l'opérande de droite. Si l'opérande de gauche est plus petit, il retourne 1. Si l'opérande de gauche est supérieur, il retourne 0.

```
int x = 10;
int y = 5; 

Serial.print(x < y)
// retourne 0
```

#### Opérateur supérieur ou égal à (>=)

Comme son nom l'indique, l'opérateur `>=` vérifie si l'opérande de gauche est soit supérieur, soit égal à l'opérande de droite. Il retourne 1 si l'opérande de gauche est supérieur ou égal à l'opérande de droite, et 0 sinon.

Le "ou" implique que l'une ou l'autre des conditions peut être remplie. Si l'opérande de gauche n'est pas supérieur à l'opérande de droite mais lui est égal, vous obtiendrez toujours une valeur de 1.

```
int x = 10;
int y = 5; 

Serial.print(x >= y)
// retourne 1
```

#### Opérateur inférieur ou égal à (<=)

L'opérateur `<=` vérifie si l'opérande de gauche est soit inférieur, soit égal à l'opérande de droite. Si l'opérande de gauche est inférieur ou égal à l'opérande de droite, il retourne 1, et retourne 0 si l'opérande de gauche n'est ni inférieur ni égal à l'opérande de droite.

```
int x = 10;
int y = 5; 

Serial.print(x <= y)
// retourne 0
```

Opérateurs logiques

Les opérateurs logiques sont utilisés dans la plupart des langages de programmation pour évaluer et déterminer la relation entre les variables.

Voici les trois opérateurs logiques que vous devriez connaître pour la programmation Arduino :

#### Opérateur ET logique (&&)

L'opérateur ET logique (`&&`) retourne 1 si les deux affirmations sont vraies.

```
int x = 10;

Serial.print((x > 5) && (x > 3));
// retourne 1
```

L'expression ci-dessus — `(x > 5) && (x > 3)` — retourne 1 car les deux affirmations sont vraies. C'est-à-dire `x > 5` et `x > 3`. Si l'une ou les deux affirmations étaient fausses, nous aurions une valeur de retour de 0.

#### Opérateur OU logique (||)

L'opérateur OU logique (`||`) retourne 1 si au moins l'une des deux affirmations est vraie.

```
int x = 10;

Serial.print((x > 5) || (x > 15));
// retourne 1
```

Le code ci-dessus retourne 1 bien que l'une des affirmations soit fausse. C'est parce que l'opérateur `||` retourne 1 si l'une ou les deux affirmations sont vraies.

#### Opérateur NON logique (!)

L'opérateur NON (`!`) nie ou inverse la valeur de son opérande. Si l'affirmation de l'opérande est vraie, il retourne faux, et il retourne vrai si l'opérande est faux.

Voici un exemple :

```
int x = 10;

Serial.print(!(x > 5));
// retourne 0
```

Le code ci-dessus retourne 0, mais pourquoi ? `x > 5` est vrai donc le résultat attendu est 1.

Nous avons obtenu 0 car l'opérateur `!` a inversé la valeur de retour de l'opérande de 1 à 0.

## Instructions conditionnelles dans Arduino

Vous pouvez utiliser des instructions conditionnelles pour prendre des décisions ou exécuter du code basé sur des conditions spécifiques. Vous pouvez combiner instructions conditionnelles et logique (comme les opérateurs de la section précédente) pour contrôler la manière dont le code est exécuté.

Jetons un coup d'œil à quelques instructions conditionnelles et comment les utiliser :

### Instruction `if`

L'instruction `if` est utilisée pour exécuter du code si une condition est `true`. Voici à quoi ressemble la syntaxe :

```
if (condition) {
    // code à exécuter si la condition est vraie
}
```

Dans la syntaxe ci-dessus, `condition` désigne une logique spécifiée. Si la condition est `true`, alors le code entre accolades sera exécuté. Voici un exemple :

```
int x = 5;
if (x < 10) {
  Serial.print("x est inférieur à 10");
}

// x est inférieur à 10
```

Dans le code ci-dessus, nous avons donné une condition — `x < 10` — et un bloc de code entre accolades qui affiche "x est inférieur à 10". Le code entre accolades ne s'exécutera que si la condition est vraie.

C'est l'équivalent de dire "si x est inférieur à 10 alors affiche 'x est inférieur à 10' sur le moniteur série". Puisque x est inférieur à 10, la condition est évaluée comme `true` et nous obtenons le message affiché.

Mais que se passe-t-il si la condition est `false` ? Le code entre accolades ne s'exécutera pas, nous aurons donc besoin d'un type de logique différent pour gérer de telles situations. Nous pouvons le faire en utilisant l'instruction `else`.

### Instruction `else`

L'instruction `else` est utilisée pour exécuter du code si une condition est `false`.

```
int score = 20;
if (score > 50 ) {
  Serial.print("Vous avez réussi l'examen !");
} else {
  Serial.print("Vous devez repasser l'examen !");
}

// Vous devez repasser l'examen !
```

Dans le code ci-dessus, la condition donnée est `false`. Ainsi, le code de l'instruction `else` sera exécuté car la variable `score` n'est pas supérieure à 50.

Rappelez-vous : le code de l'instruction `else` ne s'exécute que lorsque la condition est `false`. Si la condition est `true`, alors le code de l'instruction `if` sera exécuté.

### Instruction `else if`

Vous pouvez utiliser l'instruction `else if` pour définir plusieurs conditions à vérifier. Voici la syntaxe :

```
if (condition1) {
    // code à exécuter si condition1 est vraie
} else if (condition2){
    // code à exécuter si condition2 est vraie
} else {
    // code à exécuter si condition1 et condition2 sont fausses
}
```

Dans la syntaxe ci-dessus, il y a deux conditions (vous pouvez en créer plus de deux). Si `condition1` est `true`, alors le code entre accolades pour `condition1` sera exécuté.

Si `condition1` est `false`, alors `condition2` sera évaluée. Si `condition2` est `true`, son bloc de code sera exécuté.

Si `condition1` et `condition2` sont toutes deux `false`, le code de l'instruction `else` sera exécuté.

```
int score = 80;
if (score > 50 ) {
  Serial.print("Vous avez réussi l'examen !");
} else if (score < 50) {
  Serial.print("Vous devez repasser l'examen !");
} else {
  Serial.print("Aucun enregistrement trouvé pour votre score d'examen !");
}

// Vous avez réussi l'examen !
```

### Instruction `switch-case`

Dans la section précédente, nous avons vu comment créer plusieurs conditions en utilisant des instructions `else if`. Votre code pourrait devenir difficile à lire si vous avez de nombreuses conditions. Nous pouvons le nettoyer et le rendre plus lisible en utilisant des instructions `switch`.

Voici à quoi ressemble la syntaxe :

```
switch (expression) {
    case 1:
        // Code à exécuter si l'expression est égale au cas 1
        break;
    case 2:
        // Code à exécuter si l'expression est égale au cas 2
        break;
     case 3:
        // Code à exécuter si l'expression est égale au cas 3
        break;
    default:
        // Code à exécuter si l'expression ne correspond à aucun cas
        break;
}
```

Décomposons la syntaxe :

-   L'`expression` est comparée à la valeur de chaque `case`.
-   Lorsqu'un `case` correspond à l'`expression`, le code de ce cas est exécuté.
-   Le mot-clé `break` arrête l'itération de l'instruction `switch` une fois qu'une correspondance pour l'`expression` a été trouvée.
-   Le code du mot-clé `default` est exécuté si aucun des cas ne correspond à l'`expression`.

Voici un exemple :

```
int day = 2;

switch (day) {
  case 1:
    Serial.print("Lundi");
    break;
  case 2:
    Serial.print("Mardi");
    break;
  case 3:
    Serial.print("Mercredi");
    break;
  case 4:
    Serial.print("Jeudi");
    break;
  case 5:
    Serial.print("Vendredi");
    break;
  case 6:
    Serial.print("Samedi");
    break;
  case 7:
    Serial.print("Dimanche");
    break;
  default:
    Serial.print("Nombre hors plage");
  }

// Mardi
```

Le code ci-dessus affiche "Mardi" car l'`expression` qui a une valeur de 2 correspond au `case 2`.

## Boucles dans Arduino

Vous pouvez utiliser des boucles pour exécuter du code de manière répétée jusqu'à ce qu'une certaine condition soit remplie. Vous pouvez également utiliser des boucles pour itérer sur une collection de données et exécuter du code sur tous les éléments de la collection.

Il existe différents types de boucles que vous pouvez utiliser dans Arduino comme la boucle `for`, la boucle `while` et la boucle `do-while`. Jetons un coup d'œil à leur syntaxe avec quelques exemples pratiques :

### Boucle `for`

Vous pouvez utiliser la boucle `for` pour itérer à travers une collection ou exécuter du code jusqu'à ce qu'une certaine condition soit remplie. Elle est couramment utilisée lorsque vous connaissez le nombre de fois que la boucle est censée s'exécuter.

Voici la syntaxe :

```
for (initialization; condition; increment/decrement) {
   // code à exécuter
}
```

Il y a trois mots-clés importants dans la syntaxe ci-dessus :

-   **initialization** désigne une variable initiale (généralement un entier) qui spécifie le point de départ de la boucle.
-   **condition** est utilisée pour contrôler le nombre de fois que la boucle est censée s'exécuter. La boucle s'arrête lorsque la condition est `false`.
-   **increment/decrement** augmente/diminue la valeur de la variable initiale après chaque itération.

Voici un exemple pour vous aider à comprendre les mots-clés :

```
for (int i = 0; i < 11; i++){
  Serial.println(i);
}

// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
```

Dans la boucle ci-dessus, nous avons créé une variable initiale appelée `i` avec une valeur de 0.

La condition indiquait `i < 11`, ce qui implique que la boucle continuera de s'exécuter tant que `i` est inférieur à 11.

En utilisant l'opérateur d'incrémentation `i++`, nous avons augmenté la valeur de `i` de 1 à chaque fois que la boucle s'exécutait.

Enfin, nous avons affiché la valeur de `i` à chaque itération. Dans le moniteur série, vous remarquerez les nombres de 0 à 10 affichés. C'est parce qu'après le nombre 10, `i` n'est plus inférieur à 11 (la condition donnée), donc la boucle se termine.

### Boucle `while`

La boucle `while` fonctionne exactement comme la boucle `for` — elle exécute du code tant que la condition donnée est `true`. Mais elle est souvent utilisée lorsque le nombre de fois que la boucle doit s'exécuter est inconnu.

Voici la syntaxe :

```
while (condition) {
    // Code à exécuter
}
```

Dans la syntaxe ci-dessus, le code continuera de s'exécuter jusqu'à ce que la `condition` devienne `false`.

```
int i = 0;
while (i < 11) {
  Serial.println(i);
  i++;
}

// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
```

### Boucle `do-while`

La boucle `do-while` est similaire à la boucle `while`, mais elle exécute son bloc de code une première fois avant de vérifier la validité de la condition donnée. C'est-à-dire qu'au début de la boucle, le code entre accolades s'exécutera en premier même si la condition est `false`. Après cela, elle commence à vérifier si la condition est `true` ou `false`, comme une boucle normale.

En résumé, le code d'une boucle `do-while` s'exécutera au moins une fois, quelle que soit la condition donnée. Voici un exemple :

```
do {
  // bloc de code à exécuter
}
while (condition);
```

Voici l'exemple de code :

```
int i = 0;

do {
  Serial.println(i);
  i++;
} while ( i < 11);

// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
```

## Tableaux dans Arduino

Vous pouvez utiliser des tableaux (arrays) dans Arduino pour stocker plusieurs variables du même type de données dans une seule variable. Chaque élément stocké dans un tableau peut être accédé en utilisant son numéro d'index.

### Déclaration de tableau

Déclarer un tableau signifie simplement en créer un. Vous pouvez le faire dans Arduino en utilisant la syntaxe ci-dessous :

```
dataType arrayName[arraySize]
```

Dans la syntaxe ci-dessus :

-   `dataType` représente les types de données qui seront stockés dans le tableau. Par exemple, si le type de données est `int`, alors seuls des entiers peuvent être stockés dans le tableau.
-   `arrayName` désigne le nom du tableau.
-   `arraySize` désigne le nombre d'éléments qui peuvent être stockés dans le tableau.

Voici un exemple de code de déclaration de tableau :

```
int ages[4];
```

Dans le code ci-dessus, nous avons créé un tableau appelé `ages`. Le tableau ne peut stocker que quatre éléments de type `int`.

### Initialisation de tableau

Initialiser un tableau signifie attribuer des valeurs au tableau. Dans la section précédente, nous avons créé un tableau appelé `ages`. Maintenant, attribuons-lui quelques éléments :

```
int ages[4] = {2, 4, 6, 8};
```

Vous pouvez voir dans l'exemple ci-dessus qu'il n'y a que quatre éléments dans le tableau — 2, 4, 6, 8. L'attribution d'un cinquième élément générerait une erreur car nous avons spécifié que le tableau ne peut avoir que quatre éléments entiers : `int ages[4];`.

Vous pouvez accéder aux éléments du tableau en utilisant leur numéro d'index. Les index commencent à zéro (0) – ainsi le premier élément a un index de 0, le deuxième élément un index de 1, le troisième élément un index de 2, et ainsi de suite.

```
int ages[4] = {2, 4, 6, 8};

Serial.print(ages[0]);
// 2
```

Comme on peut le voir ci-dessus, nous avons accédé au premier élément en utilisant le nom du tableau et l'index de l'élément entre crochets : `ages[0]`.

Vous pouvez également affecter et réaffecter des valeurs à un élément particulier en utilisant son index :

```
ages[0] = 10;
```

Notez que vous pouvez déclarer et initialiser un tableau en même temps. Je les ai seulement divisés en sections séparées pour vous aider à comprendre ce que signifie chaque terme.

## Fonctions dans Arduino

Dans le chapitre précédent, nous avons discuté de certaines fonctions intégrées dans Arduino qui peuvent être utilisées pour effectuer diverses tâches liées aux composants matériels et logiciels d'Arduino. Tout ce que nous avons fait a été d'écrire le nom de la fonction et de passer des paramètres si nécessaire pour obtenir le résultat souhaité.

Par exemple, la fonction `digitalWrite()` écrit des valeurs sur les broches numériques en utilisant deux paramètres (le numéro de la broche et la valeur à envoyer à la broche). Sous le capot, une certaine logique de code gère cette opération.

Supposons que la logique requise pour envoyer des valeurs aux broches numériques fasse une centaine de lignes de code. Sans les fonctions, vous devriez écrire ces cent lignes chaque fois que vous voudriez envoyer des valeurs aux broches numériques.

Les fonctions vous évitent d'avoir à réinventer la roue. Elles vous aident également à diviser votre code en parties plus petites, plus lisibles et plus faciles à gérer.

Tout comme les fonctions intégrées peuvent être réutilisées pour effectuer une tâche particulière de manière répétée, vous pouvez également créer vos propres fonctions pour des fonctionnalités spécifiques, et c'est exactement ce que vous apprendrez dans ce chapitre.

### Comment déclarer des fonctions dans Arduino

Il y a quatre parties principales dans une fonction Arduino :

-   Le type de données que la fonction retourne.
-   Le nom de la fonction.
-   Le(s) paramètre(s) de la fonction qui est facultatif.
-   Le corps de la fonction.

Voici à quoi cela ressemble :

```
dataType functionName(optionalParameters) {
    // corps de la fonction
}
```

Ainsi, d'après la syntaxe ci-dessus, `dataType` est le type de données que la fonction retourne. Cela peut être `int`, `String`, etc. Une fonction qui n'a pas d'instruction `return` utilise le type `void` comme type de données.

Le `functionName` est le nom donné à la fonction. Le nom est utilisé pour appeler la fonction afin d'exécuter la logique définie dans le corps de la fonction. Vous verrez des mots comme "appeler" (call), "déclencher" (fire) et "invoquer" (invoke) associés aux fonctions. Ils signifient tous la même chose — exécuter la logique de la fonction.

`optionalParameters` sont des variables que vous définissez lors de la création d'une fonction. Elles permettent aux fonctions d'accepter des données externes qui peuvent être utilisées dans le corps de la fonction. Les paramètres de fonction sont définis avec leurs types de données. Vous comprendrez cela en regardant quelques exemples.

Le corps de la fonction est l'endroit où va toute la logique. Ce que fait la fonction lorsqu'elle est invoquée est écrit dans le corps.

Maintenant que nous avons vu les différentes parties d'une fonction, créons-en quelques-unes !

### Comment déclarer une fonction avec le type `void`

Dans le chapitre précédent, nous avons discuté des fonctions `void setup()` et `void loop()`. Ce sont deux fonctions intégrées que vous utiliserez dans chaque sketch Arduino. Ces fonctions sont définies en utilisant le mot-clé `void` car elles ne retournent rien.

Voici à quoi ressemble la syntaxe pour les fonctions qui utilisent le type `void` :

```
void functionName(optionalParameters) {
    // logique du code
}
```

Dans la syntaxe ci-dessus, `functionName` désigne le nom de la fonction. Nous pouvons utiliser ce nom pour appeler la fonction afin d'exécuter le code défini dans la fonction.

`optionalParameters` sont utilisés pour passer des données externes à la fonction tandis que la logique du code qui s'exécute lorsque la fonction est appelée est écrite entre les accolades.

Voici un exemple :

```
// déclaration de fonction
void printName(String userName) {
  Serial.println("Bonjour " + userName);
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  printName("Ihechikara"); // appel de fonction
  delay(1000);
}
```

Dans le code ci-dessus, nous avons créé une fonction appelée `printName` qui accepte un paramètre de type chaîne appelé `userName`. La tâche de la fonction est d'afficher "Bonjour " suivi de la valeur du paramètre.

Dans le `void loop()`, nous avons appelé la fonction et lui avons passé un paramètre : `printName("Ihechikara")`. Dans le moniteur série, vous verrez "Bonjour Ihechikara" s'afficher.

Pour appeler une fonction, il vous suffit d'écrire le nom de la fonction avec des parenthèses : `printName()`. N'oubliez pas de passer les paramètres requis : `printName("Ihechikara")`.

L'utilisation d'un paramètre ayant un mauvais type de données entraînera une erreur. Par exemple, nous avons défini un paramètre de type chaîne dans notre exemple. L'utilisation d'un entier générera une erreur car la fonction attend une chaîne.

### Comment déclarer une fonction avec un type de données de retour

Dans cette section, j'utiliserai le type de données `int` pour vous montrer comment les fonctions déclarées sans le type `void` sont utilisées. La logique ici est la même pour les autres fonctions qui utilisent l'instruction `return`.

```
// déclaration de fonction
int addNums(int a, int b) {

  int result = a + b;
  return result;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(addNums(2, 10)); // appel de fonction
  delay(1000);
}
```

Dans le code ci-dessus, nous avons déclaré une fonction avec le type `int` : `int addNums(int a, int b) {...}`. Cela implique que la fonction est censée retourner une valeur entière.

La logique de la fonction additionne la valeur des deux paramètres (`a` et `b`) et retourne leur somme. Nous avons utilisé l'instruction `return` pour retourner la somme des paramètres.

Nous pouvons maintenant dire que la tâche de la fonction `addNums` est de retourner la somme de deux paramètres donnés. Cela peut être vu lorsque nous avons utilisé la fonction dans le `void loop()` :

```
Serial.println(addNums(2, 10));
```

Nous avons appelé la fonction avec deux paramètres et obtenu leur somme affichée dans le moniteur série.

### Ce que vous devriez savoir sur l'instruction `return`

Dans les deux dernières sections, nous avons vu comment utiliser les fonctions de deux manières différentes — les fonctions qui utilisent l'instruction `return` et les fonctions qui ne l'utilisent pas.

Mais que se passerait-il si vous utilisiez l'instruction `return` dans une fonction `void` ? Cela casserait-il le code ? La réponse est non. Je vais expliquer pourquoi.

L'utilisation principale du mot-clé `return` est de retourner une valeur de la fonction, puis de terminer la fonction. Considérez l'exemple ci-dessous :

```
int addNums(int a, int b) {

  int result = a + b;
  Serial.println(result);
  return result;

  // Cette partie sera ignorée
  Serial.println("Hello World");
}
```

La fonction ci-dessus prend deux paramètres — a et b — et retourne leur somme. Vous remarquerez que nous avons affiché "Hello World" après l'instruction `return`. La partie du code qui vient après l'instruction `return` ne sera pas exécutée car la fonction termine/arrête son opération dès qu'elle voit une instruction `return`.

Vous devez donc toujours vous rappeler que tout ce qui vient après l'instruction `return` sera ignoré.

Vous pouvez utiliser l'instruction `return` dans les fonctions `void` mais la convention est de ne pas le faire. Nous utilisons simplement le mot-clé `void` pour définir des fonctions qui n'ont pas besoin de l'instruction `return`.

## Fonctions intégrées couramment utilisées dans un sketch Arduino

Dans cette section, nous allons discuter de certaines des fonctions intégrées les plus couramment utilisées que vous rencontrerez lors de l'écriture ou de la lecture de code Arduino. Nous les utiliserons dans la plupart des chapitres à venir de ce guide.

Nous commencerons par les deux parties principales d'un sketch Arduino — les fonctions `setup()` et `loop()`.

### Fonctions `setup()` et `loop()` dans Arduino

Vous pouvez utiliser la fonction `setup()` pour configurer les broches analogiques et numériques, initialiser les variables et effectuer d'autres fonctionnalités de configuration. La fonction `setup()` est exécutée une seule fois — lorsque la carte est mise sous tension ou réinitialisée.

La fonction `loop()` s'exécute en continu. Cette partie du sketch est l'endroit où vous écrivez toute la logique du code. Vous pouvez utiliser la fonction `loop()` pour donner à la carte Arduino des instructions sur différents composants et capteurs.

```
void setup() {
  // placez votre code de configuration ici, pour qu'il s'exécute une fois :

}

void loop() {
  // placez votre code principal ici, pour qu'il s'exécute de manière répétée :

}
```

### Fonction `pinMode()` dans Arduino

La fonction `pinMode()` est utilisée pour configurer les broches en tant que broches d'entrée (INPUT) ou de sortie (OUTPUT). Elle peut également être utilisée pour configurer une résistance pour agir comme une résistance de pull-up ou de pull-down. Vous en apprendrez plus sur cette fonction dans le chapitre sur les capteurs et les actionneurs.

#### Syntaxe

```
pinMode(pin, mode)
```

-   `pin` désigne le numéro de la broche sur une carte Arduino.
-   `mode` désigne la configuration de la broche (`pin`) qui peut être INPUT, OUTPUT ou INPUT\_PULLUP.

### Fonction `digitalRead()` dans Arduino

Vous pouvez utiliser la fonction `digitalRead()` pour lire l'état des broches numériques. Elle retourne soit 0 (`LOW`), soit 1 (`HIGH`).

#### Syntaxe

```
digitalRead(pin)
```

Dans le code ci-dessus, `pin` désigne le numéro de la broche sur une carte Arduino.

### Fonction `digitalWrite()` dans Arduino

La fonction `digitalWrite()` affecte ou écrit des valeurs (soit `HIGH`, soit `LOW`) sur les broches numériques.

#### Syntaxe

```
digitalWrite(pin, value)
```

-   `pin` désigne le numéro de la broche sur une carte Arduino.
-   `value` désigne la valeur à affecter à la broche (`pin`). Peut être `HIGH` ou `LOW`.

### Fonction `analogRead()` dans Arduino

La fonction `analogRead()` lit les valeurs des broches analogiques et retourne des valeurs comprises entre 0 et 1023.

#### Syntaxe

```
analogRead(pin)
```

Dans le code ci-dessus, `pin` désigne le numéro de la broche sur une carte Arduino.

### Fonction `analogWrite()` dans Arduino

Cette fonction écrit ou affecte une valeur analogique à une broche.

#### Syntaxe

```
analogWrite(pin, value)
```

-   `pin` désigne le numéro de la broche sur une carte Arduino.
-   `value` désigne la valeur à affecter à la broche (`pin`). Plage de 0 à 255.

## Fonctions série dans Arduino

La communication série permet à une carte Arduino de communiquer avec l'ordinateur et d'autres appareils en utilisant le moniteur série intégré. Voici quelques-unes des fonctions les plus couramment utilisées :

### `Serial.begin()`

La fonction `Serial.begin()` initialise la communication série. C'est la première fonction que vous utilisez lorsque vous travaillez avec le moniteur série. La fonction prend un débit en bauds (baud rate) comme paramètre.

Dans ce cas, le baud rate représente le taux ou la vitesse de transfert des données dans la communication série.

Voici la syntaxe :

```
Serial.begin(baudRate)
```

### `Serial.print()` et `Serial.println()`

Vous pouvez utiliser les fonctions `print()` et `println()` pour afficher des données sur le moniteur série.

```
Serial.print(val)
Serial.println(val)
```

Dans le code ci-dessus, `val` désigne la valeur à afficher.

Nous parlerons davantage de la communication série au [Chapitre 6 : Comment utiliser le moniteur série avec Arduino][16].

### Fonction `delay()` dans Arduino

Vous pouvez utiliser la fonction `delay()` pour mettre le programme Arduino en pause pendant une durée spécifiée. Voici à quoi ressemble la syntaxe :

```
delay(ms)
```

Dans le code ci-dessus, `ms` désigne le temps spécifié en millisecondes.

# Chapitre 3 : Comment utiliser les broches numériques avec Arduino

Les broches numériques sont utilisées pour envoyer et recevoir des signaux numériques dans deux états — `HIGH` (haut) et `LOW` (bas). Les broches numériques d'une carte Arduino peuvent être configurées comme broches d'entrée ou de sortie.

Ces états peuvent également être représentés à l'aide de nombres (1 pour `HIGH` et 0 pour `LOW`), ou en volts (V) (5V pour `HIGH` et 0V pour `LOW`).

Le nombre et la disposition des broches diffèrent selon les cartes Arduino, mais elles servent le même but. Donc, si vous comprenez comment les utiliser dans ce chapitre, vous n'aurez aucun problème à travailler avec elles sur d'autres cartes.

La carte Uno possède 14 broches numériques numérotées de 0 à 13. Bien que chaque broche puisse être configurée pour servir d'entrée ou de sortie numérique, certaines d'entre elles possèdent des fonctionnalités supplémentaires comme :

-   Les broches 0 (RX) et 1 (TX) permettent à la carte Arduino de communiquer par liaison série. RX reçoit tandis que TX envoie.
-   Les broches ayant le symbole tilde (~) à côté d'elles supportent les signaux PWM (Modulation de Largeur d'Impulsion). Cela signifie que vous pouvez utiliser ces broches comme des broches analogiques (pour recevoir des valeurs analogiques).
-   Les broches 2 et 3 peuvent être utilisées pour des fonctionnalités basées sur les interruptions.

## Comment configurer les broches numériques comme broches d'entrée ou de sortie

Lorsqu'une broche numérique est configurée comme broche d'entrée (INPUT), elle sert de point de réception d'informations provenant de composants. De cette façon, vous obtenez des données de capteurs, de composants électroniques, etc.

Vous pouvez utiliser la fonction `pinMode()` pour configurer une broche afin qu'elle serve de broche d'entrée (INPUT) ou de sortie (OUTPUT). Notez que les broches d'une carte Uno sont réglées sur INPUT par défaut, donc si vous ne spécifiez rien avant de les utiliser, elles serviront de broches d'entrée.

Dans cette section, vous apprendrez à utiliser les broches numériques à la fois comme broches d'entrée et de sortie. Vous commencerez par les étudier individuellement, puis vous verrez comment combiner les signaux d'entrée et de sortie pour construire un mini-projet.

Nous commencerons par l'entrée (INPUT).

### Broches numériques en tant qu'INPUT

L'information ou le signal envoyé aux broches d'entrée peut être lu à l'aide de la fonction `digitalRead()`. Dans cette section, vous apprendrez à configurer et à lire les signaux d'une broche d'entrée numérique à l'aide de différentes fonctions intégrées.

Nous utiliserons les composants matériels suivants :

-   Arduino Uno.
-   Breadboard.
-   Bouton-poussoir.
-   Fils de liaison (jumpers).

Voici le schéma de connexion :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/circuit-diagram-digital-input-pushbtn.png) _Schéma de configuration – INPUT_

Voici le code :

```
int pushBtn = 7;
int push_btn_state;

void setup(){
  pinMode(pushBtn, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop(){
  push_btn_state = digitalRead(pushBtn);
  Serial.println(push_btn_state);
  delay(1000);
}
```

Décomposons le code.

Nous avons commencé par créer deux variables entières — `pushBtn` et `push_btn_state` :

```
int pushBtn = 7;
int push_btn_state;
```

`pushBtn` s'est vu affecter la valeur 7. Nous avons utilisé cette valeur pour désigner la broche 7 sur la carte Arduino. Nous avons déclaré la variable `push_btn_state` mais ne lui avons affecté aucune valeur car nous l'utiliserons plus tard pour stocker la valeur du bouton-poussoir.

Dans notre fonction `setup()`, nous avons configuré le bouton-poussoir pour agir comme une broche d'entrée à l'aide de la fonction `pinMode()` :

```
pinMode(pushBtn, INPUT_PULLUP);
```

La fonction a pris deux paramètres — la variable `pushBtn` qui désignait la broche 7, et `INPUT_PULLUP` qui configure la broche comme une entrée avec une résistance de pull-up interne.

Nous avons également initialisé le moniteur série à l'aide de `Serial.begin(9600)`.

À ce stade, nous avons configuré le logiciel et le matériel Arduino pour reconnaître la broche 7 comme une broche d'entrée.

Ensuite, nous avons utilisé la fonction `digitalRead()` pour lire les signaux provenant de la broche 7. Vous vous souvenez de la variable `push_btn_state` que nous avons créée ? C'est là que nous avons stocké le signal :

```
push_btn_state = digitalRead(pushBtn);
```

Après cela, nous avons affiché la valeur lue sur la broche 7 dans le moniteur série à l'aide de `Serial.println(push_btn_state);`.

Lorsque vous ouvrez le moniteur série, vous verrez 1 s'afficher de manière répétée. C'est l'état initial du bouton-poussoir utilisant une résistance de pull-up. Lorsque vous appuyez sur le bouton-poussoir, la valeur devient 0. Lorsque vous relâchez le bouton, la valeur redevient 1.

0 désigne `LOW` tandis que 1 désigne `HIGH`. Avec cet exemple, vous devriez comprendre comment configurer, lire et afficher les signaux d'une broche d'entrée.

### Broches numériques en tant qu'OUTPUT

L'utilisation principale d'une broche de sortie est d'envoyer des signaux. Puisque nous travaillons avec une sortie numérique, nous pouvons envoyer des signaux soit `HIGH` (5V), soit `LOW` (0V). Nous pouvons le faire pour les broches numériques à l'aide de la fonction `digitalWrite()`.

Dans cette section, nous utiliserons une LED (Diode Électroluminescente) pour démontrer comment configurer et envoyer des signaux aux composants.

Voici les composants que nous utiliserons :

-   Arduino Uno.
-   LED rouge.
-   Résistance de 1k Ohm.
-   Fils de liaison (jumpers).
-   Breadboard.

Voici le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/circuit-diagram-digital-output-led.png) _Schéma de configuration – OUTPUT_

```
int RedLED = 8;

void setup(){
  pinMode(RedLED, OUTPUT);
}

void loop(){
  digitalWrite(RedLED, HIGH);
  delay(1000);
  digitalWrite(RedLED, LOW);
  delay(1000);
}
```

Dans le code ci-dessus, nous avons configuré la LED rouge, qui est connectée à la broche 8 sur la carte Uno, comme une broche de sortie à l'aide de la fonction `pinMode()`.

Nous avons ensuite utilisé la fonction `digitalWrite()` pour envoyer des signaux à la broche :

```
  digitalWrite(RedLED, HIGH);
  delay(1000);
  digitalWrite(RedLED, LOW);
  delay(1000);
```

Avec le paramètre `HIGH`, nous envoyons 5V à la broche, ce qui allume la LED. Avec `LOW`, nous envoyons 0V, ce qui éteint la LED. Ainsi, la LED s'allume et s'éteint continuellement avec un délai de 1000 millisecondes. Cet exemple est communément appelé l'exemple "BLINK".

## Projet d'E/S numériques

Maintenant que nous avons compris comment envoyer et recevoir des signaux numériques avec Arduino, combinons les deux pour construire un projet interactif.

L'idée est de contrôler une LED à l'aide d'un bouton-poussoir. Lorsque vous appuyez sur le bouton, la LED s'éteint, et elle se rallume lorsque vous relâchez le bouton.

Nous combinerons les composants utilisés dans les exemples précédents :

-   Arduino Uno.
-   LED rouge.
-   Résistance de 1k Ohm.
-   Bouton-poussoir.
-   Fils de liaison (jumpers).
-   Breadboard.

![digital-IO-project](https://www.freecodecamp.org/news/content/images/2023/10/digital-IO-project.png) _Schéma de configuration - Projet d'entrée et de sortie_

Voici le code :

```
int pushBtn = 7;
int push_btn_state;
int RedLED = 8;

void setup(){
  pinMode(pushBtn, INPUT_PULLUP);
  pinMode(RedLED, OUTPUT);
}

void loop(){
  push_btn_state = digitalRead(pushBtn);

  if (push_btn_state == 1) {
    digitalWrite(RedLED, HIGH);
  } else {
    digitalWrite(RedLED, LOW);
  }
}
```

Voici une décomposition du code ci-dessus :

D'abord, nous avons connecté le bouton-poussoir à la broche 7 et la LED rouge à la broche 8.

Ensuite, nous avons configuré les deux broches — la broche 7 comme entrée, et la broche 8 comme sortie.

Ensuite, nous avons lu la valeur du bouton-poussoir à l'aide de la fonction `digitalRead()` et stocké la valeur dans une variable appelée `push_btn_state`.

À l'aide d'une instruction `if`, nous avons vérifié l'état du bouton-poussoir. Lorsque `push_btn_state` n'est pas enfoncé, il a une valeur de 1 (`HIGH`). Nous envoyons 5V à la LED à l'aide de `digitalWrite()`.

Lorsque `push_btn_state` est enfoncé, il a une valeur de 0, et nous envoyons 0V à la LED, ce qui l'éteint.

# Chapitre 4 : Comment utiliser les broches analogiques avec Arduino

Les broches analogiques peuvent être utilisées pour recevoir et envoyer des valeurs de tension de/vers différents capteurs et composants. Contrairement aux signaux numériques qui se limitent à deux états 0 (`LOW`) et 1 (`HIGH`), les valeurs analogiques ont une plage de valeurs plus large allant de 0 à 1023.

La carte Uno possède six broches analogiques — A0, A1, A2, A3, A4 et A5. Ces broches sont des broches d'entrée (INPUT) par défaut.

Similairement aux broches numériques, il existe des fonctions intégrées pour recevoir et envoyer des signaux de tension analogiques. Vous pouvez utiliser la fonction `analogRead()` pour lire/recevoir des valeurs analogiques depuis les broches, tandis que la fonction `analogWrite()` peut être utilisée pour écrire sur des broches spécifiques.

Notez que la fonction `analogWrite()` n'écrit pas ou n'envoie pas de valeurs analogiques aux broches analogiques. Elle envoie des valeurs de tension analogiques (qui sont converties en signaux numériques) aux broches numériques qui supportent le PWM (Modulation de Largeur d'Impulsion).

Vous pouvez trouver les broches numériques PWM sur la carte Arduino grâce au symbole (~) situé à côté d'elles. Sur la carte Uno, ce sont les broches 3, 5, 6, 9, 10 et 11.

Dans le projet de cette section, vous apprendrez à régler la luminosité d'une LED à l'aide d'un potentiomètre. Nous utiliserons le potentiomètre comme composant d'entrée, et enverrons sa tension à une LED pour augmenter/diminuer sa luminosité.

Voici les composants que nous utiliserons :

-   Arduino Uno.
-   LED jaune.
-   Potentiomètre.
-   Résistance de 1k Ohm.
-   Fils de liaison (jumpers).
-   Breadboard.

Voici le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/analog-IO.png) _Schéma de configuration_

Voici le code pour le circuit :

```
int potentiometer = A0;
int pot_value = 0;
float pot_in_PWM;
int yelowLED = 6;

void setup(){
  pinMode(potentiometer, INPUT);
  pinMode(yelowLED, OUTPUT);
}

void loop(){
  pot_value = analogRead(potentiometer);
  pot_in_PWM = pot_value * (255.0 / 1023.0);

  analogWrite(yelowLED, pot_in_PWM);
}
```

Dans le code ci-dessus, nous avons configuré le potentiomètre (connecté à la broche analogique A0) comme composant d'entrée. La LED jaune (connectée à la broche numérique 6) a été configurée comme composant de sortie. La LED est connectée à une broche PWM car nous allons lui envoyer des valeurs analogiques.

À l'aide de la fonction `analogRead()`, nous avons obtenu la valeur du potentiomètre et l'avons stockée dans une variable appelée `pot_value`. Le potentiomètre retourne des valeurs de 0 à 1023.

Nous avons ensuite converti les valeurs retournées par le potentiomètre en une plage de 0 à 255 qui correspond aux valeurs PWM. C'est parce que la fonction `analogWrite()` envoie des valeurs PWM qui se situent dans cette plage (0 à 255). La nouvelle plage de valeurs a été stockée dans une variable appelée `pot_in_PWM`.

Enfin, nous avons utilisé la fonction `analogWrite()` pour envoyer des valeurs PWM à la LED : `analogWrite(yelowLED, pot_in_PWM)`.

Lorsque vous vérifierez et téléverserez le code sur votre carte Arduino, vous pourrez contrôler la luminosité de la LED en tournant le bouton du potentiomètre.

# Chapitre 5 : Comment utiliser les capteurs et les actionneurs avec Arduino

Les capteurs et les actionneurs jouent un rôle crucial dans le développement de projets avec Arduino. Ils aident les microcontrôleurs à obtenir des informations sur les changements dans l'environnement physique et à prendre des décisions basées sur ces informations.

Le but de ce chapitre est de vous aider à comprendre la différence entre les capteurs et les actionneurs, et comment les utiliser. Bien sûr, il existe de nombreux capteurs et actionneurs, mais nous nous concentrerons sur quelques-uns seulement. Vous devriez être capable d'explorer d'autres capteurs par vous-même à la fin de ce chapitre.

Nous parlerons d'abord de ce que sont les capteurs, des types de capteurs et de la façon de travailler avec eux à l'aide de code. Nous ferons de même pour les actionneurs, et nous conclurons en examinant un exemple qui utilise à la fois des capteurs et des actionneurs dans un projet.

C'est parti !

## Que sont les capteurs dans Arduino ?

Un capteur est un dispositif qui écoute ou détecte les changements dans l'environnement. Les capteurs convertissent les informations qu'ils détectent dans l'environnement physique en signaux électriques qui sont ensuite envoyés au microcontrôleur (le cerveau de la carte).

Vous pouvez comparer les capteurs aux organes des sens humains — nous les utilisons pour recueillir des informations sur notre environnement. Chaque organe des sens (comme les yeux et les oreilles) dans le corps humain a une fonction spécifique et un mode de fonctionnement différent des autres organes.

De la même manière, les capteurs dans Arduino ont leurs fonctions et cas d'utilisation spécifiques. Par exemple, nous avons des capteurs qui peuvent mesurer et détecter la température, le mouvement, l'humidité, etc.

### Types de capteurs dans Arduino

Voici quelques capteurs couramment utilisés que vous rencontrerez en travaillant avec Arduino :

-   **Capteur de température** : Mesure la température et l'humidité de l'environnement.
-   **Photorésistance (LDR)** : Mesure/détecte l'intensité de la lumière.
-   **Capteur à ultrasons** : Mesure la distance d'un objet par rapport au capteur.
-   **Capteur de mouvement** : Détecte généralement les mouvements en captant les changements d'énergie/rayonnement infrarouge.
-   **Capteur d'humidité du sol** : Mesure le niveau d'humidité du sol.
-   **Capteur d'eau** : Mesure le niveau d'eau/détecte l'eau, et ainsi de suite.

Il existe d'autres types de capteurs que vous pouvez utiliser avec Arduino, mais nous nous concentrerons sur deux : la LDR (photorésistance) et le capteur à ultrasons.

Avec les exemples de cette section, vous pourrez explorer par vous-même le fonctionnement d'autres capteurs.

### Comment utiliser la photorésistance (LDR) dans Arduino

La photorésistance (LDR), également connue sous le nom de résistance dépendante de la lumière, est un composant électronique dont le niveau de résistance varie en fonction de l'intensité de la lumière.

Fondamentalement, vous pouvez utiliser ce capteur pour détecter la lumière. Vous pouvez faire des choses sympas avec, comme créer un système d'éclairage automatisé qui allume les lumières électriques de votre maison lorsqu'il fait sombre, ou une station météo qui suit et surveille l'ensoleillement, etc.

Une LDR ressemble généralement à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/ldr.png) _Schéma d'une LDR_

Voici à quoi ressemble la connexion du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/ldr-circuit.png) _Schéma de configuration_

Dans le circuit ci-dessus, une patte de la LDR est connectée au 5V (volts). L'autre patte est connectée à une résistance de 1K Ohm — une extrémité de la résistance est connectée à la masse (GND) tandis que l'autre extrémité est connectée à une broche analogique (A1 dans notre circuit).

Voici le code :

```
int ldrPin = A1;
int ldrValue;

void setup() {
  pinMode(ldrPin, INPUT);
  Serial.begin(9600); 
}

void loop() {
  ldrValue = analogRead(ldrPin);
  Serial.println(ldrValue);
  delay(1000); 
}
```

Dans le code ci-dessus, nous avons créé une variable appelée `ldrPin` avec une valeur de `A1`. Cela désigne la connexion faite dans le circuit où une patte de la LDR est connectée à la broche analogique. Cette broche nous aidera à connaître la valeur du capteur.

Nous avons ensuite créé une variable `ldrValue` qui sera utilisée pour stocker la valeur du capteur.

Dans la fonction `setup()`, nous avons configuré la LDR comme une broche d'entrée (INPUT). Nous avons également initialisé le moniteur série.

Ensuite, nous avons lu la valeur de la LDR à l'aide de la fonction `analogRead`, et stocké la valeur dans la variable `ldrValue` :

```
ldrValue = analogRead(ldrPin);
```

Enfin, nous avons affiché la valeur lue sur le moniteur série avec un délai de 1000 millisecondes (une seconde).

À ce stade, si vous augmentez l'exposition à la lumière sur la LDR, la valeur augmente. Si vous diminuez l'intensité lumineuse ou couvrez le capteur pour bloquer la lumière, la valeur diminuera ou deviendra nulle, respectivement.

## Comment utiliser le capteur à ultrasons dans Arduino

Le capteur à ultrasons est généralement utilisé pour mesurer la distance des objets. Vous pouvez utiliser ce capteur dans de nombreuses applications telles que :

-   La domotique (vous pouvez effectuer certaines actions lorsque la présence d'un objet/humain est détectée, comme allumer les lumières dans une pièce sombre).
-   Les portes automatisées.
-   Les systèmes de sécurité.
-   La mesure de distance, etc.

Comme pour les autres capteurs, il en existe différents types. Dans cet exemple, nous utiliserons le capteur à ultrasons HC-SR04. Ne vous inquiétez pas, le principe de fonctionnement est le même. Donc, si vous comprenez comment utiliser celui-ci, vous pourrez configurer et utiliser d'autres types de capteurs à ultrasons que vous rencontrerez.

Voici à quoi ressemble le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/ultra-sensor.png) _Schéma de configuration (source : https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/)_

Le capteur possède quatre broches — VCC, Trig, Echo et GND.

-   La broche VCC est connectée au 5V sur la carte Uno.
-   La broche Trig est connectée à la broche numérique 9.
-   La broche Echo est connectée à la broche numérique 10.
-   La broche GND est connectée au GND sur la carte Uno.

La broche Trig est utilisée pour "déclencher" (trigger) le capteur à ultrasons tandis que la broche Echo est utilisée pour calculer la distance des objets en fonction du temps que mettent les ondes/signaux ultrasonores pour revenir après avoir rebondi sur un objet.

Voici un exemple de code :

```
int trigPin = 9; 
int echoPin = 10;  

long duration, distance;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = (duration / 2) * 0.0343;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(1000);
}
```

Dans le code ci-dessus, la broche Trig désigne la broche numérique 9, et la broche Echo désigne la broche numérique 10.

Nous avons déclaré deux variables — duration et distance — pour stocker leurs valeurs respectives.

Nous avons déclenché le capteur en envoyant un signal `HIGH` à la broche trigger pendant 10 microsecondes. Sans cela, le capteur pourrait ne pas fonctionner :

```
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
```

Nous avons mesuré et stocké la durée de l'impulsion/des signaux ultrasonores à l'aide de la fonction `pulseIn(echoPin, HIGH)` et l'avons stockée dans la variable `duration`.

Nous avons ensuite calculé la distance en centimètres et l'avons stockée dans la variable `distance`.

Enfin, nous avons affiché la distance sur le moniteur série avec un délai de 1000 millisecondes.

À ce stade, vous pouvez placer un objet plus près ou plus loin du capteur et voir la valeur de la distance de l'objet changer dans le moniteur série.

## Que sont les actionneurs dans Arduino ?

Les actionneurs dans Arduino sont des composants qui convertissent les signaux électriques en mouvement physique/mécanique.

Voici quelques actionneurs :

-   LED (Diode Électroluminescente) : Utilisée comme indicateur lumineux/visuel.
-   Buzzer : Utilisé pour produire du son.
-   Modules relais : Utilisés pour contrôler des appareils à haute tension.
-   LCD (Écran à Cristaux Liquides) : Utilisé comme affichage visuel pour du texte, des images, des données de capteurs, etc. Nous consacrerons un chapitre séparé aux écrans.
-   Servomoteurs : Utilisés pour contrôler un mouvement angulaire ou rotatif (un exemple est le mouvement d'un bras robotique).

Nous nous concentrerons sur le buzzer et la LED dans cette section.

### Comment utiliser les LED dans Arduino

Les LED sont généralement les premiers composants que l'on découvre avec Arduino. Elles sont faciles à connecter et à utiliser.

Voici à quoi ressemble une LED :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/redLED.png)

Voici la connexion du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/led-circuit.png)

Dans le circuit ci-dessus, la patte la plus longue de la LED (l'anode ou patte positive) est connectée à la broche numérique 7.

La patte la plus courte (cathode) est connectée à la masse (GND).

Voici le code :

```
int redLED = 7;

void setup() {
  pinMode(redLED, OUTPUT);
}

void loop() {
  digitalWrite(redLED, HIGH);
  delay(1000);
  digitalWrite(redLED, LOW);
  delay(1000);
}
```

Le code ci-dessus fera clignoter la LED une fois le code téléversé.

### Comment utiliser un buzzer dans Arduino

Vous pouvez utiliser des buzzers pour produire du son. Il existe généralement deux types de buzzers : les buzzers actifs et passifs.

Les buzzers actifs ont généralement un type de son prédéfini qu'ils produisent lorsqu'une tension leur est fournie. Le son ne peut pas être modifié. Les buzzers actifs possèdent un circuit interne qui déclenche la production du son.

Les buzzers passifs sont un peu plus flexibles lorsqu'il s'agit de produire du son car ils dépendent de signaux externes. Cela signifie que vous pouvez déterminer la fréquence (ou les fréquences) du son produit par le buzzer.

Les buzzers peuvent être utilisés dans différentes applications telles que :

-   Les systèmes d'alarme.
-   Les indicateurs sonores pour les appareils ménagers.
-   Les sonnettes de porte.
-   Les dispositifs de communication pour signaler le début/la fin d'une transmission de signal, etc.

Nous travaillerons avec le buzzer passif en raison de sa flexibilité. Voici à quoi il ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/buzzer.png)

Le buzzer possède une borne positive et une borne négative. La borne positive est connectée à une broche numérique tandis que la borne négative est connectée à la masse.

Voici le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/buzzer-circuit.png)

Dans cet exemple, nous utiliserons le buzzer pour produire les notes de musique DO, RÉ, MI, FA, SOL, LA, SI.

Voici le code :

```
int buzzerPin = 7;

int notes[] = {262, 294, 330, 349, 392, 440, 494};

int noteDurations[] = {400, 400, 400, 400, 400, 400, 400};

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  for (int i = 0; i < 8; i++) {
    tone(buzzerPin, notes[i], noteDurations[i]);
    delay(noteDurations[i] + 50);
    noTone(buzzerPin);
  }

  delay(1000);
}
```

Dans le code ci-dessus, nous avons utilisé la variable `buzzerPin` pour désigner la broche 7 sur la carte Uno.

Nous avons ensuite créé un tableau appelé `notes[]` qui stocke la fréquence respective de chaque note, et un autre tableau appelé `noteDurations` qui stocke la durée de chaque note produite par le buzzer.

Dans la fonction `void loop()`, nous avons parcouru chaque note et les avons jouées à l'aide de la fonction `tone()`. La fonction prend trois paramètres — la broche connectée au buzzer, la fréquence et la durée.

Nous avons utilisé la fonction `noTone()` pour arrêter la génération du son. Enfin, nous avons ajouté un délai de 1000 millisecondes, ce qui correspond au temps nécessaire pour rejouer les notes depuis le début après que la dernière note a été jouée.

Si vous avez suivi jusqu'ici, vous devriez entendre les notes de musique DO, RÉ, MI, FA, SOL, LA, SI jouées par le buzzer.

## Exemple de capteur et d'actionneur Arduino

Maintenant que vous comprenez ce que sont les capteurs et les actionneurs et comment les utiliser, utilisons-les ensemble dans un seul projet.

Dans de nombreux systèmes embarqués, les capteurs et les actionneurs travaillent ensemble pour accomplir une tâche/fonctionnalité spécifique. Voici comment cela fonctionne :

-   Un capteur détecte les changements dans l'environnement et envoie des signaux au microcontrôleur pour l'informer des changements détectés.
-   Le microcontrôleur traite les signaux du capteur. En fonction de la logique existante (définie dans le code), il envoie des signaux à l'actionneur.
-   L'actionneur convertit le signal du microcontrôleur en mouvement physique/mécanique.

Démontrons cela à l'aide d'un exemple. L'idée ici est d'allumer une LED dans un environnement sombre et de l'éteindre lorsqu'il y a assez de lumière.

Le capteur sera le capteur LDR, le microcontrôleur sera la carte/logiciel Arduino Uno, et l'actionneur sera la LED.

Voici le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/ldr-led-circuit.png)

Voici le code :

```
int redLED = 7;

int ldrPin = A1;
int ldrValue;

void setup() {
  pinMode(ldrPin, INPUT);
  pinMode(redLED, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
  ldrValue = analogRead(ldrPin);

  if (ldrValue > 200) {
    digitalWrite(redLED, LOW);
  } else if (ldrValue < 200) {
    digitalWrite(redLED, HIGH);
  }

  Serial.println(ldrValue);
  delay(1000); 
}
```

Comme d'habitude, nous avons créé des variables pour représenter les broches Arduino connectées à la LED et à la LDR. Nous avons ensuite configuré la LDR comme entrée (INPUT) et la LED comme sortie (OUTPUT) dans la fonction `setup()`.

Nous avons lu la valeur de la LDR à l'aide de la fonction `analogRead()` et l'avons stockée dans la variable `ldrValue`.

Ensuite, nous avons utilisé une instruction `if` pour vérifier la valeur de la LDR.

Si la valeur est supérieure à 200, nous éteignons la LED. Si la valeur est inférieure à 200, nous allumons la LED.

# Chapitre 6 : Comment utiliser le moniteur série avec Arduino

Le moniteur série est un outil utile pour tout constructeur Arduino. Vous pouvez l'utiliser pour diverses tâches telles que :

-   Le débogage et le test du code/des composants.
-   La communication série entre la carte Arduino et l'ordinateur.
-   L'affichage des données et des lectures des capteurs et des composants.

Dans ce chapitre, vous apprendrez à initialiser et à utiliser le moniteur série à l'aide de l'IDE Arduino. Vous découvrirez différentes fonctions intégrées qui peuvent être utilisées pour envoyer et recevoir des données entre la carte Arduino et l'ordinateur.

Enfin, vous construirez un projet qui utilise les valeurs envoyées depuis le moniteur série pour alimenter des LED spécifiques connectées à la carte Arduino.

## Comment initialiser le moniteur série avec `Serial.begin()`

Vous pouvez utiliser la fonction `Serial.begin()` pour initialiser le moniteur série. Elle prend le débit en bauds (baud rate) comme paramètre. Voici à quoi ressemble la syntaxe :

```
Serial.begin(baudRate)
```

Le baud rate est la vitesse de transfert des données entre la carte Arduino et l'ordinateur ou tout autre appareil communiquant avec la carte Arduino via le moniteur série.

Le baud rate le plus couramment utilisé est 9600, mais vous rencontrerez également des ressources qui utilisent 115200, 57600, 38400, etc. Quel que soit le baud rate que vous spécifiez dans la fonction `Serial.begin()`, il doit toujours correspondre au baud rate affiché dans la fenêtre du moniteur série.

Par exemple, nous pouvons initialiser le moniteur série dans l'IDE à l'aide de la fonction `Serial.begin()` comme ceci :

```
void setup() {
  Serial.begin(9600);

}

void loop() {
  // placez votre code principal ici, pour qu'il s'exécute de manière répétée :

}
```

Dans le code ci-dessus, à l'aide de la fonction `Serial.begin()`, nous avons initialisé le moniteur série dans la fonction `setup()` avec un baud rate de 9600.

À ce stade, rien ne se passe. Vous pouvez vérifier que les baud rates correspondent en ouvrant la fenêtre du moniteur série. Une fois ouverte, le moniteur série devrait apparaître à la base de l'IDE. Vous verrez le baud rate du moniteur série dans la fenêtre, généralement écrit comme "9600 baud".

![Image](https://www.freecodecamp.org/news/content/images/2023/10/baud-rate.PNG) _Image montrant le baud rate_

Si vous utilisez une version plus ancienne de l'IDE, le moniteur série peut apparaître dans une fenêtre séparée. La fonctionnalité reste la même.

Maintenant que nous avons initialisé le moniteur série, voyons comment envoyer et recevoir des données avec lui.

## Comment envoyer des données avec le moniteur série

Vous pouvez utiliser différentes fonctions intégrées réservées à la communication série dans Arduino. Nous ne discuterons pas de toutes les fonctions série intégrées — nous examinerons seulement celles que vous utiliserez/rencontrerez régulièrement. Vous pouvez voir plus de fonctions [ici][17].

### Fonctions `print()` et `println()`

Les fonctions `print()` et `println()` affichent toutes deux des données sur le moniteur série. La différence entre les deux est que `print()` affiche les données sur la même ligne tandis que `println()` affiche chaque donnée sur une nouvelle ligne.

Voici quelques exemples :

```
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("Hello"); 
  delay(1000);
}
```

Dans le code ci-dessus, nous avons utilisé la fonction `print()` pour afficher "Hello" sur le moniteur série de manière répétée avec un délai de 1000 millisecondes. Voici à quoi ressemble la sortie dans le moniteur série :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/print.PNG)

Voici un autre exemple utilisant la fonction `println()` :

```
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Hi");
  delay(1000);
}
```

Voici la sortie dans le moniteur série :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/println.PNG)

## Comment recevoir des données avec le moniteur série

Nous allons discuter de quatre fonctions dans cette section — `available()`, `readString()`, `parseInt()` et `parseFloat()`. Vous pouvez vous renseigner sur les autres fonctions série [ici][18].

### Fonction `available()`

La fonction `Serial.available()` vérifie le nombre de caractères présents dans le port série. Elle est principalement utilisée pour n'exécuter du code que lorsque des données sont disponibles dans le moniteur série.

Voici un exemple de code :

```
int userInput;

void setup(){
  Serial.begin(9600);
}

void loop(){
  if (Serial.available() > 0) {
    userInput = Serial.parseInt();

    Serial.println(userInput);
  }

}
```

Dans le code ci-dessus, le bloc de code dans l'instruction `if` ne s'exécutera pas tant que le nombre de caractères dans le moniteur série n'est pas supérieur à 0.

Lorsque vous initialisez le moniteur série, le nombre de caractères lisibles sera de zéro car aucune donnée n'est encore disponible. La fonction `Serial.available()` vérifie et retourne le nombre de caractères disponibles dans le moniteur série. Elle est donc utilisée pour créer une logique qui ne permet l'exécution du code que lorsque des données sont disponibles.

### Fonction `readString()`

Vous pouvez utiliser la fonction `readString()` pour lire des caractères depuis le moniteur série. Elle retourne un objet String, donc toutes les valeurs/caractères que vous saisirez dans le moniteur série seront considérés comme des valeurs de chaîne lors de l'utilisation de la fonction `readString()`.

```
String userInput;

void setup(){
  Serial.begin(9600);
}

void loop(){
  if (Serial.available() > 0) {
    userInput = Serial.readString();

    Serial.println(userInput);
  }

}
```

### Fonction `parseInt()`

La fonction `parseInt()` retourne des valeurs entières valides à partir des données série entrantes. Les valeurs non entières seront retournées comme 0.

```
int userInput;

void setup(){
  Serial.begin(9600);
}

void loop(){
  if (Serial.available() > 0) {
    userInput = Serial.parseInt();

    Serial.println(userInput);
  }

}
```

### Fonction `parseFloat()`

La fonction `parseFloat()` retourne des nombres à virgule flottante valides à partir des données série entrantes.

```
float userInput;

void setup(){
  Serial.begin(9600);
}

void loop(){
  if (Serial.available() > 0) {
    userInput = Serial.parseFloat();

    Serial.println(userInput);
  }

}
```

## Projet Moniteur série

Dans cette section, vous allez construire un projet qui utilise des valeurs de chaîne provenant du moniteur série pour allumer des LED. Nous utiliserons certaines des fonctions série abordées dans les sections précédentes.

Voici le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/serial-communication-project.png)

Dans le schéma du circuit ci-dessus, nous avons trois LED. La LED rouge est connectée à la broche 6, la LED bleue à la broche 5 et la LED jaune à la broche 4.

Voici le code :

```
int redLED = 6;
int blueLED = 5;
int yellowLED = 4;

String userInput;

void setup(){
  pinMode(redLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  Serial.begin(9600);

  Serial.println("Choisissez une LED à allumer dans la liste ci-dessous :");
  Serial.println("red");
  Serial.println("blue");
  Serial.println("yellow");
}

void loop(){

  if (Serial.available() > 0) {

    userInput = Serial.readString();

    if (userInput == "red") {
      digitalWrite(redLED, HIGH);
      digitalWrite(blueLED, LOW);
      digitalWrite(yellowLED, LOW);
    } 

    if (userInput == "blue") {
      digitalWrite(redLED, LOW);
      digitalWrite(blueLED, HIGH);
      digitalWrite(yellowLED, LOW);
    }

    if (userInput == "yellow") {
      digitalWrite(redLED, LOW);
      digitalWrite(blueLED, LOW);
      digitalWrite(yellowLED, HIGH);
    }

  }

}
```

Décomposons le code ci-dessus.

Tout comme la connexion dans le schéma du circuit, nous avons initialisé les trois LED avec leurs numéros de broches respectifs. Nous avons également créé une variable String appelée `userInput` qui sera utilisée pour stocker les données du moniteur série :

```
int redLED = 6;
int blueLED = 5;
int yellowLED = 4;
```

Nous avons ensuite configuré les trois LED comme broches de sortie à l'aide de la fonction `pinMode()` :

```
pinMode(redLED, OUTPUT);
pinMode(blueLED, OUTPUT);
pinMode(yellowLED, OUTPUT);
```

Nous avons initialisé le moniteur série avec un baud rate de 9600, et affiché quelques chaînes de caractères pour donner aux utilisateurs une indication sur les valeurs attendues à utiliser dans le moniteur série :

```
Serial.begin(9600);

Serial.println("Choisissez une LED à allumer dans la liste ci-dessous :");
Serial.println("red");
Serial.println("blue");
Serial.println("yellow");
```

À ce stade, vous aurez une sortie comme celle-ci dans le moniteur série :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/project-output.PNG)

À l'aide de la fonction `Serial.available()`, nous vérifions la disponibilité des données série avant d'exécuter le code dans l'instruction `if` :

```
if (Serial.available() > 0) {
    ...
}
```

La chose suivante que nous avons faite a été de lire et de retourner les données entrantes sous forme de valeurs de chaîne, et de stocker les données dans la variable `userInput`. Nous l'avons fait en utilisant la fonction `readString()` :

```
userInput = Serial.readString();
```

Enfin, nous avons utilisé des instructions `if` pour vérifier quelle couleur de LED l'utilisateur a tapée/envoyée via le moniteur série, puis allumer/éteindre les LED respectives :

```
if (userInput == "red") {
  digitalWrite(redLED, HIGH);
  digitalWrite(blueLED, LOW);
  digitalWrite(yellowLED, LOW);
} 

if (userInput == "blue") {
  digitalWrite(redLED, LOW);
  digitalWrite(blueLED, HIGH);
  digitalWrite(yellowLED, LOW);
}

if (userInput == "yellow") {
  digitalWrite(redLED, LOW);
  digitalWrite(blueLED, LOW);
  digitalWrite(yellowLED, HIGH);
}
```

Si vous tapez et envoyez "red" via le moniteur série, la LED rouge s'allume tandis que les autres s'éteignent. La même logique s'applique à l'envoi de "blue" ou "yellow" via le moniteur série.

# Chapitre 7 : Comment utiliser les écrans avec Arduino

Vous pouvez utiliser des composants d'affichage dans Arduino pour représenter des données visuellement sous différents formats comme du texte, des images, etc.

Les écrans offrent une alternative à l'affichage des données autre que le moniteur série. Vous pouvez les utiliser pour afficher des valeurs de capteurs, des instructions aux utilisateurs, des entrées utilisateur, etc.

Il existe différents types de composants d'affichage lorsqu'il s'agit de construire avec Arduino, mais nous nous concentrerons sur le LCD (Écran à Cristaux Liquides).

Pour être plus précis, nous utiliserons le LCD 16 x 2 (HD44780). Voici à quoi il ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/lcd-component.png)

D'après l'image ci-dessus, il y a seize broches avec différentes valeurs. Nous utiliserons la plupart de ces broches pour effectuer les connexions à la carte Uno, ce qui nous permettra d'utiliser et de contrôler le composant.

Il existe généralement deux façons de connecter le LCD — en utilisant la bibliothèque intégrée ou en utilisant une bibliothèque tierce.

Avec la bibliothèque intégrée `LiquidCrystal`, vous utiliserez environ 12 broches sur le composant LCD. Lorsqu'il s'agit d'utiliser une bibliothèque tierce comme `LiquidCrystal_I2C`, vous n'utiliserez que 2 broches.

Nous utiliserons la première méthode — cela vous aidera à comprendre comment fonctionnent les broches. Parlons maintenant de ces broches.

## À quoi servent les broches d'un LCD ?

Les broches contrôlent des fonctionnalités telles que la gestion de la mémoire, le transfert de données et l'alimentation d'un LCD. Parlons-en en détail :

-   La première broche en partant de la gauche est la broche GND, qui est la broche de masse du LCD. Elle est connectée au GND de la carte Arduino. Sur certains modules LCD, elle peut être notée VSS.
-   La broche VCC est la broche d'alimentation qui est connectée au 5V de la carte Arduino. Sur certains modules LCD, elle peut être notée VDD.
-   La broche V0 est utilisée pour régler le contraste du LCD. Elle est connectée à un potentiomètre. Tourner le potentiomètre modifie le contraste des données affichées.
-   La broche RS (Register Select) peut être utilisée pour contrôler la mémoire du LCD. Elle est généralement connectée à une broche numérique.
-   La broche RW (Read/Write) contrôle si les données sont écrites ou lues sur le LCD. Elle est généralement connectée à la masse (GND), ce qui place le LCD en mode écriture — cela vous permet d'envoyer et d'afficher des données avec le LCD.
-   La broche E (Enable) "active" le transfert de données entre le microcontrôleur (dans notre cas, la carte Uno) et le LCD. Elle est généralement connectée à une broche numérique.
-   Les broches D0 à D7 (peuvent également être notées DB0 à DB7) sont les broches de données. Elles sont utilisées pour envoyer des données au LCD en bits. Dans la plupart des cas, les broches D4 à D7 sont utilisées. La principale différence est que les données sont envoyées en 4 bits avec les broches D0 à D3, tandis que les données sont envoyées en 8 bits avec les broches D4 à D7. Elles sont généralement connectées à des broches numériques.
-   Les broches LED sont utilisées pour contrôler le rétroéclairage du LCD. Sur certains modules LCD, elles peuvent être notées BLA et BLK, ou A et K. La première broche LED est connectée au 5V à l'aide d'une résistance tandis que la deuxième broche LED est connectée à la masse (GND).

## Exemple #1 – Comment connecter et utiliser un LCD avec Arduino

Dans la section précédente, nous avons parlé de la signification des broches d'un LCD. Dans cette section, vous verrez un exemple pratique sur la façon de les connecter dans un circuit et d'écrire du code pour afficher des données sur le LCD.

Nous utiliserons les composants suivants :

-   Arduino Uno.
-   LCD 16 x 2.
-   Potentiomètre.
-   Fils de liaison (jumpers).
-   Résistances.
-   Breadboard.

Voici à quoi ressemble le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/lcd.png)

Dans le circuit ci-dessus, nous avons effectué les connexions suivantes du LCD vers la carte Uno :

-   La broche GND du LCD a été connectée au GND de la carte Uno.
-   La broche VCC du LCD a été connectée au 5V de la carte Uno.
-   La broche V0 a été connectée au potentiomètre.
-   La broche RS a été connectée à la broche numérique 4 de la carte Uno.
-   La broche RW a été connectée au GND de la carte Uno.
-   La broche D4 du LCD a été connectée à la broche numérique 6 de la carte Uno.
-   La broche D5 du LCD a été connectée à la broche numérique 7 de la carte Uno.
-   La broche D6 du LCD a été connectée à la broche numérique 8 de la carte Uno.
-   La broche D7 du LCD a été connectée à la broche numérique 9 de la carte Uno.
-   La première broche LED a été connectée au 5V.
-   La deuxième broche LED a été connectée au GND.

Pour le potentiomètre, l'une des pattes extérieures (soit la gauche, soit la droite) a été connectée au 5V, l'autre patte extérieure a été connectée au GND. Ensuite, la patte centrale du potentiomètre a été connectée à la broche V0 du LCD. Cela vous permettra de contrôler le contraste du LCD.

Ensuite, nous allons écrire du code !

```
#include <LiquidCrystal.h>

LiquidCrystal lcd(4, 5, 6, 7, 8, 9);

void setup() {
  lcd.begin(16, 2);
  lcd.print("freeCodeCamp!");
}

void loop() {

}
```

Dans le code ci-dessus, nous avons d'abord inclus/importé la bibliothèque intégrée `LiquidCrystal` qui peut être utilisée pour interagir avec un LCD à l'aide du code Arduino : `#include <LiquidCrystal.h>`.

Nous avons ensuite initialisé l'objet `lcd` avec les numéros de broches requis : `LiquidCrystal lcd(4, 5, 6, 7, 8, 9)`. Le premier nombre désigne la broche RS. Le deuxième nombre désigne la broche E. Les quatre derniers nombres désignent les broches de données (D4 à D7).

Ensuite, nous avons initialisé le nombre de colonnes et de lignes à l'aide de la fonction `lcd.begin()` : `lcd.begin(16, 2)`. Nous avons 16 colonnes et 2 lignes.

La fonction `lcd.print` affiche les données sur le LCD. Si vous avez effectué toutes les connexions correctement, vous devriez voir "freeCodeCamp" affiché sur le LCD.

Dans les exemples suivants, nous travaillerons avec les entrées utilisateur et les données de capteurs, et nous verrons également d'autres fonctions `lcd`.

## Exemple #2 – Comment afficher l'entrée utilisateur avec un LCD dans Arduino

Dans cet exemple, nous accepterons une entrée de l'utilisateur à l'aide du moniteur série, et afficherons l'entrée accompagnée d'un message de bienvenue sur l'écran LCD.

Nous utiliserons le même circuit que dans l'exemple précédent. Voici le code :

```
#include <LiquidCrystal.h>
LiquidCrystal lcd(4, 5, 6, 7, 8, 9);

String userInput;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);

  lcd.print("Input name");

  lcd.setCursor(0, 1);
}

void loop() {
  if (Serial.available() > 0) {

    userInput = Serial.readString();
    lcd.print("Welcome " + userInput);
  }
}
```

Dans le code ci-dessus, nous avons créé une variable String appelée `userInput` qui sera utilisée pour stocker la valeur de l'entrée de l'utilisateur.

Nous avons ensuite initialisé le moniteur série — `Serial.begin(9600);`

Ensuite, nous avons défini les lignes et les colonnes du LCD à l'aide de la fonction `lcd.begin`.

À l'aide de la fonction `lcd.print`, nous avons affiché "Input name" sur l'écran LCD.

Ceci a été suivi par la fonction `lcd.setCursor(0, 1)` qui possède deux paramètres — 0 et 1. 0 représente la première colonne à gauche tandis que 1 représente la deuxième ligne. Ainsi, le curseur sera placé sur la deuxième ligne du LCD.

Nous avons réglé le curseur pour qu'il soit sur la deuxième ligne car nous avons déjà du texte ("input name") sur la première ligne, il serait donc plus idéal dans ce cas d'afficher le message à l'utilisateur sur la ligne suivante. Je vous montrerai une autre façon de faire après cet exemple.

Dans la fonction `void loop()`, nous avons utilisé la fonction `Serial.readString()` pour lire la valeur de l'entrée de l'utilisateur et l'avons stockée dans la variable `userInput`.

Enfin, nous avons affiché un message de bienvenue et le nom de l'utilisateur sur le LCD. Cela sera affiché sur la deuxième ligne car c'est là que nous avons placé le curseur.

Amusez-vous avec le code et voyez ce qui se passe lorsque vous ajustez les paramètres de la fonction `lcd.setCursor()`. Cela vous aidera à mieux la comprendre.

### Alternative à l'exemple #2

Une autre façon d'afficher le message à l'utilisateur est d'utiliser la même ligne que celle où le message initial a été affiché. Nous pouvons effacer tout ce qui est écrit sur la première ligne du LCD et afficher une valeur différente.

Voici comment :

```
#include <LiquidCrystal.h>
LiquidCrystal lcd(4, 5, 6, 7, 8, 9);

String userInput;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);

  lcd.print("Input name");
}

void loop() {
  if (Serial.available() > 0) {
    lcd.clear();
    userInput = Serial.readString();
    lcd.print("Welcome " + userInput);
  }
}
```

Dans cet exemple, nous avons utilisé la fonction `lcd.clear()` pour effacer le message de demande initial et afficher/imprimer le message de bienvenue à l'utilisateur. Le reste de la logique est le même.

Ainsi, lorsque vous tapez un nom dans le moniteur série et appuyez sur Entrée, le message de demande ("Input name") sera effacé tandis que le message de bienvenue sera affiché avec le nom que vous avez saisi.

## Exemple #3 – Comment afficher les données d'un capteur avec un LCD dans Arduino

Dans cet exemple, nous allons afficher les données d'un capteur sur le LCD. Nous utiliserons le capteur de température. La logique ici est de détecter la température d'une pièce et d'afficher les valeurs variables sur le LCD.

Voici les composants que nous utiliserons :

-   Arduino Uno.
-   LCD 16 x 2.
-   Photorésistance (LDR).
-   Potentiomètre.
-   Fils de liaison (jumpers).
-   Résistances.
-   Breadboard.

Voici le schéma du circuit :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/lcd-ldr.png)

Le schéma du circuit est presque le même que ceux des exemples précédents, sauf que nous avons ajouté une LDR pour mesurer l'intensité de la lumière. À l'aide de la LDR, nous allons lire, stocker et afficher la valeur de l'intensité lumineuse sur le LCD.

Voici le code :

```
#include <LiquidCrystal.h>
LiquidCrystal lcd(4, 5, 6, 7, 8, 9);

int ldrPin = A1;
int ldrValue;

void setup() {
  pinMode(ldrPin, INPUT);
  lcd.begin(16, 2);
}

void loop() {
  ldrValue = analogRead(ldrPin);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("LDR value:");

  lcd.setCursor(0, 1);
  lcd.print(ldrValue);

  delay(1000);
}
```

Décomposons le code.

Nous avons commencé par inclure la bibliothèque intégrée `LiquidCrystal` et initialisé les broches respectives pour travailler avec le LCD (référez-vous au premier exemple si vous ne comprenez pas comment fonctionnent la connexion et l'initialisation).

Nous avons ensuite créé deux variables : `ldrPin` qui désignait la broche analogique connectée à la LDR, et `ldrValue` pour stocker les lectures de la LDR.

Dans `void setup()`, nous avons configuré la LDR comme une broche d'entrée et défini les colonnes et les lignes du LCD.

Ensuite, nous avons lu la valeur de la LDR à l'aide de la fonction `analogRead` et stocké cette valeur dans la variable `ldrValue`.

À l'aide de la fonction `lcd.clear()`, nous effaçons l'affichage après chaque lecture. Cela aide à rendre la lecture plus précise. Si vous supprimez la fonction, certaines valeurs resteront affichées et rendront vos résultats inexacts (j'ai passé environ trente minutes à comprendre cela 😂).

Après cela, nous avons placé le curseur sur la première ligne et la première colonne du LCD : `lcd.setCursor(0, 0)`, et affiché un message ("LDR value:").

À l'aide de la fonction `lcd.setCursor(0, 1)`, nous avons déplacé le curseur vers le bas sur la deuxième ligne, et utilisé `lcd.print(ldrValue)` pour afficher la valeur de la LDR sur le LCD.

Enfin, nous avons ajouté un délai de 1000 millisecondes.

Vous pouvez maintenant voir la valeur de l'intensité lumineuse de votre environnement affichée sur le LCD.

Vous pouvez utiliser une lampe de poche pour augmenter et diminuer l'exposition à la lumière sur la LDR, puis observer les valeurs changer sur le LCD. C'est plutôt cool !

# Conclusion

Félicitations ! Nous sommes arrivés à la fin de ce guide. Vous avez maintenant suffisamment de connaissances pour entreprendre des projets plus importants.

Et cela devrait être votre prochain objectif — appliquer ces concepts à des projets qui vous aident, vous et les gens qui vous entourent. Il n'y a pas de limite à ce que vous pouvez créer. Vous pouvez commencer par regarder quelques vidéos pour voir le type de projets que les gens construisent, puis vous pourrez imaginer les vôtres.

Ce guide a couvert les parties nécessaires d'Arduino (à la fois matérielles et logicielles) dont vous aurez besoin en tant que débutant pour démarrer votre voyage.

La meilleure façon de s'améliorer et de retenir ce que vous avez appris est de pratiquer et de construire.

Bon bricolage !

[1]: #heading-prerequis
[2]: #heading-chapitre-1-premiers-pas-avec-arduino
[3]: #heading-chapitre-2-les-bases-de-la-programmation-arduino
[4]: #heading-chapitre-3-comment-utiliser-les-broches-numeriques-avec-arduino
[5]: #heading-chapitre-4-comment-utiliser-les-broches-analogiques-avec-arduino
[6]: #heading-chapitre-5-comment-utiliser-les-capteurs-et-les-actionneurs-avec-arduino
[7]: #heading-chapitre-6-comment-utiliser-le-moniteur-serie-avec-arduino
[8]: #heading-chapitre-7-comment-utiliser-les-ecrans-avec-arduino
[9]: https://blog.arduino.cc/2023/06/26/uno-r4-the-new-dimension-of-making/?_gl=1*18ccx2k*_ga*MTkzMTc3MDUxNC4xNjc5NjU4Mzkz*_ga_NEXN8H46L5*MTY4Nzk0Njg3Mi40LjEuMTY4Nzk0ODE3MS4wLjAuMA..
[10]: https://www.arduino.cc/en/software
[11]: https://www.arduino.cc/en/software
[12]: https://docs.arduino.cc/software/ide-v2/tutorials/getting-started-ide-v2
[13]: https://docs.arduino.cc/software/ide-v2/tutorials/getting-started-ide-v2
[14]: https://www.asciitable.com/
[15]: #heading-chapitre-6-comment-utiliser-le-moniteur-serie-avec-arduino
[16]: #heading-chapitre-6-comment-utiliser-le-moniteur-serie-avec-arduino
[17]: https://www.arduino.cc/reference/en/language/functions/communication/serial/
[18]: https://www.arduino.cc/reference/en/language/functions/communication/serial/