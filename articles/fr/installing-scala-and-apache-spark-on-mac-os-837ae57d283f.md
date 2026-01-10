---
title: Comment installer Scala et Apache Spark sur MacOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-10T20:41:57.000Z'
originalURL: https://freecodecamp.org/news/installing-scala-and-apache-spark-on-mac-os-837ae57d283f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Pa7PO1v7bANI7C-eHMS_PQ.png
tags:
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Scala
  slug: scala
- name: spark
  slug: spark
seo_title: Comment installer Scala et Apache Spark sur MacOS
seo_desc: 'By Jose Marcial Portilla

  Here is a Step by Step guide to installing Scala and Apache Spark on MacOS.

  Step 1: Get Homebrew

  Homebrew makes your life a lot easier when it comes to installing applications and
  languages on a Mac OS. You can get Homebrew b...'
---

Par Jose Marcial Portilla

Voici un guide étape par étape pour installer Scala et Apache Spark sur MacOS.

#### Étape 1 : Obtenir Homebrew

Homebrew facilite grandement l'installation d'applications et de langages sur un Mac OS. Vous pouvez obtenir Homebrew en suivant les instructions sur son [site web](http://brew.sh/).

Ce qui vous indique essentiellement d'ouvrir votre terminal et de taper :

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Il y a des instructions plus détaillées sur l'installation sur la [page GitHub du projet](https://github.com/Homebrew/brew/blob/master/docs/Installation.md#installation). L'installation de tout via Homebrew devrait automatiquement ajouter tous les paramètres de PATH appropriés à votre profil.

#### Étape 2 : Installer xcode-select

Pour installer Java, Scala et Spark via la ligne de commande, nous devrons probablement installer xcode-select et les outils de développement en ligne de commande. Allez dans votre terminal et tapez :

```
xcode-select --install
```

Vous obtiendrez une invite qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/FfIidYg0docKBqK3RPLGGMOZmTCA3l2mMVMB)

Allez-y et sélectionnez installer.

#### Étape 3 : Utiliser Homebrew pour installer Java

Scala dépend de Java, vous devrez peut-être l'installer. La manière la plus simple de l'installer est d'utiliser HomeBrew :

Dans votre terminal, tapez :

```
brew cask install java
```

Vous devrez peut-être entrer votre mot de passe à un moment donné pour compléter l'installation de Java. Après avoir exécuté cela, Homebrew devrait avoir pris en charge l'installation de Java. Nous pouvons maintenant passer à Scala.

#### Étape 4 : Utiliser Homebrew pour installer Scala

Maintenant que Homebrew est installé, allez dans votre terminal et tapez :

```
brew install scala
```

#### Étape 5 : Utiliser Homebrew pour installer Apache Spark

Maintenant que Scala est installé, allez dans votre terminal et tapez :

```
brew install apache-spark
```

Homebrew va maintenant télécharger et installer Apache Spark, cela peut prendre un certain temps en fonction de votre connexion Internet.

#### Étape 5 : Démarrer le Shell Spark

Essayez maintenant cette commande :

```
spark-shell
```

Vous devriez voir un flot de texte et d'avertissements, mais finalement quelque chose comme ceci :

```
Welcome to      ____              __     / __/__  ___ _____/ /__    _\ \/ _ \/ _ `/ __/  '_/   /___/ .__/\_,_/_/ /_/\_\   version 2.0.1      /_/
```

```
Using Scala version 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_102)Type in expressions to have them evaluated.Type :help for more information.
```

```
scala>
```

Vous pouvez confirmer que cela fonctionne en tapant le code scala :

```
val s = "hello world"
```

Félicitations ! Vous êtes prêt !

_Problème courant : Définir le PATH dans bash._

Homebrew devrait avoir tout pris en charge, mais au cas où vous devriez ajouter spark à votre PATH, vous voudrez utiliser :

```
export SPARK_HOME=/usr/local/Cellar/apache-spark/2.0.1/libexecexport PYTHONPATH=/usr/local/Cellar/apache-spark/2.0.1/libexec/python/:$PYTHONP$
```

Tapez cela directement dans votre terminal.

Je suis Jose Portilla, et j'enseigne à plus de 200 000 étudiants la programmation, la science des données et le machine learning sur Udemy. Vous pouvez consulter tous mes cours [ici](https://www.udemy.com/user/joseporitlla/).

Si vous êtes intéressé par l'apprentissage de Python pour la science des données et le machine learning, [consultez mon cours ici](https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp/?couponCode=2017PYTHONDSML15). (J'enseigne aussi le [Développement Web Full Stack avec Django !](https://www.udemy.com/python-and-django-full-stack-web-developer-bootcamp/?couponCode=2017DJANGO15))