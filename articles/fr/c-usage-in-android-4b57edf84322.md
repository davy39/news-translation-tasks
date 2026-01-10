---
title: Comment commencer à utiliser du code C++ dans votre projet Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-14T15:43:14.000Z'
originalURL: https://freecodecamp.org/news/c-usage-in-android-4b57edf84322
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7WUOO46e_50vGPtv_BZmiQ.png
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment commencer à utiliser du code C++ dans votre projet Android
seo_desc: 'By Onur Tuna

  Last year I gave a talk at the GDG DevFest in Ankara, Turkey. I have been planning
  to share that talk here ever since. Now that I’m a PhD candidate and have a bit
  more time, I’m putting the post down here.

  If you would like to get the pr...'
---

Par Onur Tuna

L'année dernière, j'ai donné une conférence au GDG DevFest à Ankara, en Turquie. J'avais prévu de partager cette conférence ici depuis lors. Maintenant que je suis candidat au doctorat et que j'ai un peu plus de temps, je rédige cet article.

Si vous souhaitez obtenir la présentation, elle est disponible sur mon [drive](https://docs.google.com/presentation/d/19SYg_6QuU9ZGZ7mj2xHsuO2BwT7z1Sr6XtIAMoRja84/edit?usp=sharing).

#### **Échauffement**

Je voudrais commencer par expliquer le processus de construction d'une application sous Android. Parce que vous devez connaître certaines bases internes, ce sujet est quelque peu technique.

![Image](https://cdn-media-1.freecodecamp.org/images/CiOMuYEICXxQIaTnhTq2QDcUjDvxJ67U2qnP)

Vous n'avez pas besoin de connaître tout ce qui est montré dans l'image ci-dessus — mais c'est une bonne référence.

Maintenant, disons que vous écrivez une application pour Android en utilisant Java. Vous allez avoir :

* le code source de cette application
* une sorte de fichiers de ressources (comme des images ou des fichiers xml pour l'arrangement de l'interface graphique)
* et peut-être quelques fichiers AIDL, qui sont des interfaces Java qui permettent aux processus de communiquer entre eux.

Vous allez probablement aussi utiliser des bibliothèques supplémentaires et leurs fichiers associés dans votre projet.

Lors de la construction d'une application fonctionnelle, vous compilez d'abord ces codes sources ensemble. Un compilateur va produire un fichier DEX qui peut ensuite être lu par une machine virtuelle. Ce fichier lisible par machine et quelques informations supplémentaires sur l'application seront regroupés par un gestionnaire de paquets. Le paquet final — appelé un paquet APK — est l'application finale.

C'est le processus de construction d'un paquet Android en termes les plus simples.

#### Android Run Time

Maintenant, parlons du temps d'exécution. Vous avez une application, et lorsqu'elle commence à s'exécuter, elle est lue par une machine. Android dispose de deux types de machines virtuelles pour exécuter une application. Je ne vais pas présenter l'ancienne, appelée Dalvik, car aujourd'hui la plupart des appareils Android exécutent une machine virtuelle appelée Android Run Time, ART — c'est donc ce dont nous allons parler ici.

![Image](https://cdn-media-1.freecodecamp.org/images/YChoo3SiUcI378wJqem7nUIB0bsaS3egjrf1)

ART est une machine virtuelle à compilation anticipée (AOT). Alors, que signifie cela ? Laissez-moi expliquer. Lorsque votre application commence à s'exécuter pour la première fois, son code est compilé en code machine qui peut ensuite être lu par la machine réelle. Cela signifie que le code n'est pas compilé partie par partie au moment de l'exécution. Cela améliore le temps d'installation de l'application tout en réduisant l'utilisation de la batterie.

En somme, vous écrivez une application puis vous la compilez en code binaire qui est lu par l'ART. Ensuite, l'ART convertit ce code en code natif qui peut être lu par l'appareil lui-même.

#### ART & C++

![Image](https://cdn-media-1.freecodecamp.org/images/z7AduOu6vW2oHfZQ3f8e7etkODct3vYAYP7X)

Que se passe-t-il si vous écrivez une application Android en utilisant Java mais qu'il y a du code C++ en contact avec le Java ? Quel est l'effet de ce code C++ sur le processus de construction ou d'exécution de votre application ? Pas grand-chose.

Le code C++ est compilé directement en code machine réel par son compilateur. Donc, si vous utilisez du code C++, il sera empaqueté sous forme de code lisible par machine dans votre paquet. L'ART ne le retraitera pas lorsqu'il convertira le code lisible par ART en code lisible par machine lors de la première utilisation. Vous n'avez pas à vous soucier de ce processus. Vous êtes seulement responsable de l'écriture d'une interface qui permet à Java de communiquer avec C++. Nous allons en parler bientôt.

#### Processus de construction C++

![Image](https://cdn-media-1.freecodecamp.org/images/GC85hntQ4WtielAPH0Z8EVMCPRxI6fwQaPU6)

Nous devons maintenant parler du processus de construction C++. Le code source (les fichiers .cpp et .h) est transformé en code source étendu par un préprocesseur dans la toute première étape. Ce code source contient beaucoup de code. Bien que vous puissiez obtenir le fichier exécutable final en utilisant une commande comme celle ci-dessus, il est possible de couper les étapes de construction avec des flags associés. Vous pouvez obtenir le code source étendu en donnant le flag _-E_ au compilateur _g++_. J'ai un fichier de 40867 lignes pour un code source .cpp 'hello world' de 4 lignes.

> Utilisez g++ -E hello.cpp -o hello.ii afin d'obtenir le code source étendu.

La deuxième étape est l'étape de compilation réelle. Le compilateur compile notre code pour obtenir un fichier assembleur. Ainsi, la compilation réelle produit un fichier assembleur, et non l'exécutable. Ce fichier est assemblé par un assembleur. Le code résultant est appelé code objet. Lorsque nous avons plusieurs bibliothèques destinées à être liées entre elles, nous avons de nombreux codes objet. Ces codes objet sont liés par un éditeur de liens. Ensuite, nous obtenons un exécutable.

Il existe deux types de liaison : dynamique et statique.

![Image](https://cdn-media-1.freecodecamp.org/images/5lb-AjEa2LTfa12E3iNzGeaq80uCdHbmlqPs)

Il est maintenant temps d'approfondir un peu alors que nous discutons du C++ pur.

L'important : Vous pouvez considérer les bibliothèques liées statiquement comme faisant partie de votre code. Soyez donc prudent lorsque vous liez une bibliothèque à votre projet. Parce que la bibliothèque que vous utilisez peut ne pas avoir une licence appropriée pour être liée statiquement. La plupart des bibliothèques open source ont été restreintes pour être utilisées comme liées dynamiquement.

D'un point de vue technique, une bibliothèque liée statiquement est liée au projet au moment de la construction par le compilateur. D'autre part, une bibliothèque liée dynamiquement est liée par le système d'exploitation au moment de l'exécution. Vous n'avez donc pas besoin de distribuer votre projet avec le code de la bibliothèque que vous utilisez. Vous pouvez utiliser la bibliothèque d'un autre projet ou une bibliothèque système.

En raison de ce fait, la liaison dynamique peut causer une vulnérabilité dans votre projet. Bien que le cas de la sécurité soit hors du cadre de cet article.

### Quelques concepts

#### CMake et Gradle

Si nous voulons ajouter du code C++ dans notre projet Android, il est bon d'utiliser CMake pour gérer les opérations de construction. Vous vous souvenez du processus de construction que je viens de présenter ci-dessus ? Lorsque vous avez un ensemble de bibliothèques et de code source C++, il devient plus compliqué de gérer tous ces éléments. Un outil comme CMake facilite la réalisation du processus de construction.

CMake sera disponible par défaut lorsque vous choisissez d'inclure la prise en charge de C++ au début de votre projet. Vous devez également utiliser une fermeture Gradle afin d'empaqueter les bibliothèques dans votre APK.

![Image](https://cdn-media-1.freecodecamp.org/images/KQdZIREs7iuVrUMQbLpwrzRpWAz1bkMijSrf)

#### ABI

Comme vous le savez, Android est distribué pour une variété d'appareils. Chaque appareil peut avoir une architecture CPU différente. Lorsque vous développez une application Android contenant du code C++, vous devez vous soucier des plateformes sur lesquelles votre application s'exécutera.

Vous vous souvenez du mécanisme de construction C++ que j'ai introduit ci-dessus ? Le code C++ doit être compilé en tant que bibliothèque pour chaque plateforme que vous ciblez. Vous pouvez compiler la bibliothèque pour toutes les plateformes prises en charge, ou vous pouvez choisir de la compiler pour une seule plateforme.

Veuillez noter que la prise en charge de l'ABI 64 bits sera obligatoire avec la sortie d'Android Pie si vous souhaitez mettre votre application dans le Google Play Store.

![Image](https://cdn-media-1.freecodecamp.org/images/Nx7BBPjHD6Dn3bwH9cHuv7Kl0buNiStKpAnK)
_Tableau de support Android pour différents CPU._

#### JNI

C'est la dernière chose que je voudrais vous présenter concernant l'utilisation de C++ dans Android. Comme je l'ai mentionné précédemment, je vous présente ces concepts en considérant que vous souhaitez développer une application en utilisant Java.

JNI est l'abréviation de Java Native Interface. Il permet aux parties C++ et Java de communiquer entre elles en termes simples. Par exemple, si vous souhaitez appeler une fonction depuis C++ en Java, vous devez écrire une interface JNI à cet effet.

![Image](https://cdn-media-1.freecodecamp.org/images/jipzVE6uvyBsaoSwHDAM9VifTSIZSa3YxXhk)

Le fichier native-lib.cpp est l'interface et il connecte le code C++ au code Java. Dans l'exemple ci-dessus, le seul code C++ est le JNI lui-même. Cependant, vous pouvez inclure les bibliothèques que vous souhaitez utiliser et implémenter une fonction qui les appelle. Cette nouvelle fonction peut être appelée depuis la partie Java. Elle fonctionne donc comme un pont de cette manière.

### Choses à faire si vous voulez l'essayer

Ici, vous avez toutes les connaissances nécessaires et de base pour utiliser le C++ dans votre projet Android. Si vous souhaitez l'essayer, voici comment créer un simple projet Android avec du code C++.

Les images ci-dessous vous montrent les étapes pour démarrer un tel projet. Après les avoir terminées, vous pourriez vouloir relire cet article pour modifier et comprendre le mécanisme plus profondément.

![Image](https://cdn-media-1.freecodecamp.org/images/bnDl13uKInK-yDGhQnELCJQsNoBq-fuSV3A6)

![Image](https://cdn-media-1.freecodecamp.org/images/UQCYmz05inEFug2gtN4fKEEoMmwEVJQbi0ca)

Cet article n'était qu'une introduction. N'oubliez pas qu'il y a beaucoup plus de choses à apprendre. Cependant, j'ai visé à vous introduire les choses les plus importantes concernant le concept d'utilisation du C++.

![Image](https://cdn-media-1.freecodecamp.org/images/WRXTaytqujH3hU1-1PJ6K83BphnZPVJ4MjGk)