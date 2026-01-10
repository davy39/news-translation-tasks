---
title: Développement d'applications mobiles avec Dart et Flutter
subtitle: ''
author: Mark Mahoney
co_authors: []
series: null
date: '2025-10-30T01:08:25.714Z'
originalURL: https://freecodecamp.org/news/mobile-app-development-with-dart-and-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761786494585/5f335412-1621-4d5c-9861-29390381797c.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: Mobile Development
  slug: mobile-development
seo_title: Développement d'applications mobiles avec Dart et Flutter
seo_desc: Mobile app development lets you build applications that run on multiple
  platforms. Flutter is Google's UI toolkit for building applications for mobile,
  web, and desktop from a single codebase. Flutter apps are written in Dart, a statically
  typed, obj...
---

Le développement d'applications mobiles vous permet de créer des applications qui s'exécutent sur plusieurs plateformes. Flutter est le toolkit d'interface utilisateur (UI) de Google pour créer des applications pour le mobile, le web et le bureau à partir d'une seule base de code. Les applications Flutter sont écrites en Dart, un langage orienté objet à typage statique.

Le développement mobile moderne nécessite de comprendre les widgets, la gestion d'état (state management), la navigation et le stockage de données. L'écosystème comprend des milliers de packages gratuits qui vous donnent accès aux capteurs de l'appareil, aux services cloud, et plus encore.

Ce tutoriel couvre les fondamentaux de Dart, les bases de Flutter et quelques options de stockage de données. Il contient 20 programmes qui vous guident dans la construction d'applications mobiles à partir de zéro. Il est structuré autour d'un groupe de *code playbacks* annotés.

Chaque playback montre comment j'ai construit un programme étape par étape. Ils incluent un tuteur IA intégré si vous avez des questions que je n'ai pas abordées. Pour une démonstration rapide du fonctionnement des code playbacks, regardez cette courte vidéo :

%[https://youtu.be/uYbHqCNjVDM] 

Vous pouvez accéder au tutoriel gratuit ici : [https://playbackpress.com/books/flutterbook](https://playbackpress.com/books/flutterbook)

**Prérequis** : Ceci n'est pas une introduction générale à la programmation, vous aurez donc besoin de quelques connaissances de base en programmation pour suivre. Si vous comprenez les variables, les boucles, les fonctions et les classes dans n'importe quel langage, tout devrait bien se passer. Si vous avez besoin d'une introduction à la programmation, consultez mes autres tutoriels en [C++](https://playbackpress.com/books/cppbook) ou [Python](https://playbackpress.com/books/pybook) sur [Playback Press](https://playbackpress.com/books).

## **Table des matières**

### **1\. Dart**

* [1.1 Hello World !!! et instructions d'installation de Flutter/Dart](https://playbackpress.com/books/flutterbook/chapter/1/1)
    
* [1.2 Types simples en Dart](https://playbackpress.com/books/flutterbook/chapter/1/2)
    
* [1.3 Listes (conteneurs basés sur des tableaux)](https://playbackpress.com/books/flutterbook/chapter/1/3)
    
* [1.4 Maps et Sets](https://playbackpress.com/books/flutterbook/chapter/1/4)
    
* [1.5 Altérer le flux de contrôle](https://playbackpress.com/books/flutterbook/chapter/1/5)
    
* [1.6 Closures](https://playbackpress.com/books/flutterbook/chapter/1/6)
    
* [1.7 Code asynchrone en Dart](https://playbackpress.com/books/flutterbook/chapter/1/7)
    
* [1.8 Classes en Dart](https://playbackpress.com/books/flutterbook/chapter/1/8)
    

### **2\. Flutter**

* [2.1 Flutter Hello World](https://playbackpress.com/books/flutterbook/chapter/2/1)
    
* [2.2 flutter create demo\_app](https://playbackpress.com/books/flutterbook/chapter/2/2)
    
* [2.3 ListViews](https://playbackpress.com/books/flutterbook/chapter/2/3)
    
* [2.4 Mise en page des widgets](https://playbackpress.com/books/flutterbook/chapter/2/4)
    
* [2.5 Navigation dans Flutter](https://playbackpress.com/books/flutterbook/chapter/2/5)
    
* [2.6 Formulaires](https://playbackpress.com/books/flutterbook/chapter/2/6)
    
* [2.7 Utilisation de packages dans Flutter](https://playbackpress.com/books/flutterbook/chapter/2/7)
    

### **3\. Stockage des données d'une application**

* [3.1 Stockage des données de l'application dans un fichier](https://playbackpress.com/books/flutterbook/chapter/3/1)
    
* [3.2 Stockage des données de l'application dans une base de données SQLite](https://playbackpress.com/books/flutterbook/chapter/3/2)
    
* [3.3 Stockage des données de l'application sur un serveur](https://playbackpress.com/books/flutterbook/chapter/3/3)
    
* [3.4 Stockage des données de l'application dans Firebase Cloud Firestore](https://playbackpress.com/books/flutterbook/chapter/3/4)
    
* [3.5 Authentification Firebase](https://playbackpress.com/books/flutterbook/chapter/3/5)
    

## **Commencer**

Commencez par le chapitre sur Dart si vous découvrez le langage. Si vous avez de l'expérience en JavaScript, Java ou C#, cela devrait vous sembler familier. Ensuite, passez aux playbacks Flutter. Travaillez sur les playbacks à votre propre rythme.

Des questions ou des commentaires ? Contactez-moi à [mark@playbackpress.com](mailto:mark@playbackpress.com)