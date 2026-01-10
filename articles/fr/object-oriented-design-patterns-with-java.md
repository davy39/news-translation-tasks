---
title: Modèles de conception orientés objet avec Java
subtitle: ''
author: Mark Mahoney
co_authors: []
series: null
date: '2025-07-28T20:36:16.232Z'
originalURL: https://freecodecamp.org/news/object-oriented-design-patterns-with-java
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1753734965769/4d53f28e-7d85-4571-831f-1760490e06dc.png
tags:
- name: design patterns
  slug: design-patterns
- name: Java
  slug: java
seo_title: Modèles de conception orientés objet avec Java
seo_desc: In this article I will introduce some of the most useful object-oriented
  design patterns. Design patterns are solutions to common problems that show up over
  and over again. These problems will show up in many different contexts but always
  have the sa...
---

Dans cet article, je vais présenter certains des modèles de conception orientés objet les plus utiles. Les modèles de conception sont des solutions à des problèmes courants qui se posent encore et encore. Ces problèmes apparaissent dans de nombreux contextes différents mais ont toujours le même problème à la racine.

Un modèle de conception tente de décrire une solution efficace au problème de manière générique afin qu'elle puisse être appliquée à un ensemble spécifique de circonstances.

Je vais utiliser Java pour construire un exemple de chaque modèle. Je suppose que vous avez une certaine expérience de la programmation en Java. En particulier, vous devriez être (au moins quelque peu) familiarisé avec les concepts d'héritage et de polymorphisme. Ces modèles de conception montrent vraiment la puissance de l'héritage et du polymorphisme, donc si vous commencez à apprendre ces sujets, c'est une excellente opportunité d'approfondir.

Et si vous n'êtes pas un programmeur Java ? Si vous êtes familiarisé avec un langage orienté objet, vous tirerez probablement encore beaucoup des exemples. Essayez !

## **Lectures de code**

Pour rendre les modèles de conception plus accessibles, j'ai développé un tutoriel interactif qui utilise des lectures de code annotées pour parcourir les caractéristiques clés des modèles de conception étape par étape.

Chaque modèle de conception est présenté sous forme de lecture de code qui montre comment un programme évolue au fil du temps, accompagné de mes explications sur ce qui se passe. Ce format vous aide à vous concentrer sur le raisonnement derrière les changements de code.

Vous pouvez accéder gratuitement au "livre" des lectures de code ici :

> [Modèles de conception OO avec Java](https://playbackpress.com/books/patternsbook), par Mark Mahoney (c'est moi)

Pour visualiser une lecture de code, cliquez sur les commentaires dans le panneau de gauche. Chaque commentaire met à jour le code dans l'éditeur et met en évidence les modifications. Lisez l'explication et étudiez le code. Si vous êtes bloqué, utilisez l'assistant IA comme un tuteur pour vous aider à expliquer ce qui se passe dans le code.

Pour plus d'informations sur les lectures de code, vous pouvez regarder une courte démonstration ici.

%[https://youtu.be/uYbHqCNjVDM] 

## Modèles de conception clés que vous devriez connaître

### **Modèle Stratégie**

Le [**Modèle Stratégie**](https://www.freecodecamp.org/news/a-beginners-guide-to-the-strategy-design-pattern/) est utilisé pour définir une "famille" d'algorithmes, encapsuler chacun d'eux et les rendre interchangeables. Les développeurs de logiciels utilisent le modèle Stratégie lorsqu'ils savent qu'il existe de nombreuses façons différentes d'accomplir un certain comportement. Plutôt que d'inclure toutes les différentes façons dans une seule classe, ils les séparent en classes individuelles et les intègrent lorsque cela est nécessaire.

Ce programme crée des classes pour stocker les notes des étudiants. Certains instructeurs aiment ajuster l'ensemble des notes du cours pour les rendre plus élevées. Certains instructeurs le font en supprimant la note la plus basse de chaque étudiant. D'autres instructeurs "ajustent" chaque devoir. Puisqu'il existe plusieurs options différentes, je vais utiliser le **Modèle Stratégie** pour les isoler et laisser le client choisir celle qu'il préfère.

Commencez par examiner les classes `Assignment`, `Student` et `Course`. Une fois que vous êtes familiarisé avec les classes principales, regardez comment je modifie le code pour implémenter deux approches différentes pour *ajuster* les notes en utilisant le **Modèle Stratégie** :

> [**Modèle Stratégie** Ajustement des notes dans un cours](https://playbackpress.com/books/patternsbook/chapter/1/1)

### **Modèle Singleton**

Il arrive que vous deviez vous assurer qu'il n'y a qu'une seule instance d'une classe et qu'elle est accessible partout dans votre code. C'est le problème que le [**Modèle Singleton**](https://en.wikipedia.org/wiki/Singleton_pattern) résout.

Dans ce programme, je vais créer une classe qui génère des nombres aléatoires. Je vais m'appuyer sur la classe `Random` intégrée de Java, mais je pourrai reproduire exactement la même séquence de nombres aléatoires en mode "test". Je vais m'assurer qu'il n'y a qu'une seule instance de ce générateur de nombres aléatoires en utilisant le **Modèle Singleton** :

> [**Modèle Singleton** Une classe de nombres aléatoires testable](https://playbackpress.com/books/patternsbook/chapter/1/2)

### **Modèle Composite**

Souvent, nous créons des structures arborescentes de contenu tout/partie. Par exemple, dans un système de fichiers, il y a des fichiers simples. J'appelle ces éléments simples des *primitifs*. Nous pouvons regrouper des primitifs pour former des *composites* plus grands. Les fichiers peuvent être regroupés en répertoires. Ces composites (répertoires) peuvent être regroupés en composites encore plus grands, et ainsi de suite.

Nous pourrions traiter les composites et les primitifs différemment. Mais il est souvent logique de les traiter de la même manière. Devoir distinguer entre les types d'objets rend l'application plus complexe.

Le [**Modèle Composite**](https://en.wikipedia.org/wiki/Composite_pattern) décrit comment utiliser la composition récursive afin que les clients n'aient pas besoin de faire cette distinction.

Ce programme crée des classes pour imprimer une collection hiérarchique de fichiers et de répertoires en utilisant le **Modèle Composite** :

> [**Modèle Composite** Affichage d'un système de fichiers hiérarchique](https://playbackpress.com/books/patternsbook/chapter/1/3)

### **Modèle Décorateur**

Parfois, nous voulons ajouter des responsabilités à des objets individuels, et non à une classe entière. Le [**Modèle Décorateur**](https://en.wikipedia.org/wiki/Decorator_pattern) nous permet de créer des *décorateurs* pour fournir une alternative flexible à l'héritage pour étendre une classe.

Dans ce programme, je crée une interface pour journaliser les messages pendant l'exécution d'un programme. J'utilise l'interface pour créer un `ConsoleLogger` qui imprime les messages de journalisation à l'écran. Ensuite, je commence à ajouter des objets décorateurs qui entourent, ou enveloppent, le `ConsoleLogger`. J'ajoute des décorateurs pour attacher la date, le nom de l'auteur et l'heure aux messages de journalisation en utilisant le **Modèle Décorateur** :

> [**Modèle Décorateur** Journalisation avec des décorateurs](https://playbackpress.com/books/patternsbook/chapter/1/4)

### **Modèle État**

Parfois, il existe des systèmes qui réagissent différemment en fonction de l'"état" dans lequel ils se trouvent. Un état est une période pendant laquelle un système réagira aux événements selon certaines règles. Ce comportement basé sur l'état est implémenté en utilisant le [**Modèle État**](https://en.wikipedia.org/wiki/State_pattern).

Je vais vous montrer comment parcourir les caractères d'une chaîne et l'analyser pour tenir compte des guillemets qu'elle contient. Par exemple, la chaîne suivante :

`"hamburgers chips 'hot dogs' pickles 'french fries'"`

peut être divisée en une collection comme ceci :

`["hamburgers", "chips", "hot dogs", "pickles", "french fries"]`

Il existe de nombreuses façons d'accomplir cela en Java, mais je vais montrer une approche basée sur l'état. Lorsqu'un guillemet simple est rencontré dans une chaîne, je vais l'utiliser comme un événement et passer entre différents états en utilisant le **Modèle État** :

> [**Modèle État** Division de chaîne pour les barres de recherche](https://playbackpress.com/books/patternsbook/chapter/1/5)

### **Modèle Observateur**

Le [**Modèle Observateur**](https://en.wikipedia.org/wiki/Observer_pattern) est utilisé lorsque la mise à jour d'une seule donnée dans un objet doit être propagée à une collection d'autres objets.

Par exemple, lorsque la valeur d'une cellule dans une feuille de calcul change, plusieurs autres cellules peuvent avoir besoin d'être informées de ce changement afin qu'elles puissent se mettre à jour. De même, dans une application de réseau social, lorsqu'un utilisateur publie un message, tous ses amis doivent être informés afin que leurs flux puissent être mis à jour. Ces deux cas sont essentiellement le même problème que le **Modèle Observateur** résout.

Ce programme crée une classe pour stocker une heure de la journée appelée `MyTime`. Ensuite, je crée deux types différents d'`Observers` qui seront informés lorsque l'heure change. Les deux observateurs réafficheront l'heure chaque fois qu'elle change en utilisant le **Modèle Observateur** :

> [**Modèle Observateur** Observation du changement d'heure](https://playbackpress.com/books/patternsbook/chapter/1/6)

### **Modèle Proxy**

Parfois, nous concevons un ensemble d'objets qui ont une relation client/serveur, mais nous décidons plus tard que les deux objets ne doivent pas interagir directement. Ce programme montre comment utiliser le [**Modèle Proxy**](https://en.wikipedia.org/wiki/Proxy_pattern) pour placer une nouvelle fonctionnalité entre deux classes précédemment coopérantes.

Je crée une classe `Card` et `Deck` pour les jeux de cartes. Le `Deck` commence par être hébergé sur la même machine que le `Driver`. Ensuite, je sépare le `Driver` et la classe `Deck` afin qu'ils puissent être exécutés sur différentes machines en utilisant le **Modèle Proxy** :

> [**Modèle Proxy** Distribution de cartes depuis un deck distant](https://playbackpress.com/books/patternsbook/chapter/1/7)

### **Modèle Fabrique**

Le [**Modèle Fabrique**](https://en.wikipedia.org/wiki/Factory_method_pattern) fournit un mécanisme pour créer des "familles" d'objets apparentés sans spécifier leurs classes concrètes. L'instanciation d'objets concrets dans une application rend difficile la modification de ces objets plus tard.

Dans ce programme, je vais créer deux familles différentes de classes pour un système d'aide pour deux plateformes informatiques différentes en utilisant le **Modèle Fabrique** :

> [**Modèle Fabrique** Obtenir de l'aide sur Mac et Windows](https://playbackpress.com/books/patternsbook/chapter/1/8)

### **Modèle Visiteur**

Le [**Modèle Visiteur**](https://en.wikipedia.org/wiki/Visitor_pattern) vous permet d'ajouter des fonctionnalités à une hiérarchie de classes sans changer son interface.

La raison pour laquelle cela est important est qu'il arrive que nous ne puissions pas changer une hiérarchie de classes existante. Peut-être que j'utilise une hiérarchie de classes que je ne contrôle pas, mais je veux ajouter une nouvelle fonctionnalité. C'est là que le **Modèle Visiteur** intervient.

Dans ce programme, j'ajouterai des fonctionnalités aux classes `File` et `Directory` du programme *Composite* que j'ai écrit précédemment avec des modifications minimales de ces classes.

Je crée un *visiteur* pour compter le nombre de fichiers et de répertoires dans un répertoire de haut niveau. Ensuite, j'écris un *visiteur* pour collecter uniquement les noms de fichiers dans un répertoire, y compris ses sous-répertoires, en utilisant le **Modèle Visiteur** :

> [**Modèle Visiteur** Ajout de fonctionnalités à une hiérarchie de classes (Fichier et Répertoire)](https://playbackpress.com/books/patternsbook/chapter/1/9)

## **Conclusion**

J'espère que vous avez apprécié apprendre les modèles de conception orientés objet. Si vous êtes intéressé par d'autres paradigmes de programmation, vous pouvez consulter certains de mes autres "livres" [ici](https://playbackpress.com/books).

Les questions et les commentaires sont toujours les bienvenus ici : [mark@playbackpress.com](mailto:mark@playbackpress.com)

Si vous souhaitez soutenir mon travail et aider à garder Playback Press gratuit pour tous, envisagez de faire un don en utilisant [GitHub Sponsors](https://github.com/sponsors/markm208). J'utilise toutes les donations pour les coûts d'hébergement. Votre soutien m'aide à continuer à créer du contenu éducatif comme celui-ci. Merci !