---
title: Langage de programmation Go (Golang)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T22:07:00.000Z'
originalURL: https://freecodecamp.org/news/go-golang-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/golang-gopher-2.jpg
tags:
- name: golang
  slug: golang
- name: programming languages
  slug: programming-languages
seo_title: Langage de programmation Go (Golang)
seo_desc: "Go (or golang) is a programming language created at Google in 2007 by Robert\
  \ Griesemer, Rob Pike, and Ken Thompson. It is a compiled, statically-typed language\
  \ in the tradition of Algol and C. \nGo has garbage collection, limited structural\
  \ typing, me..."
---

**Go** (ou **golang**) est un langage de programmation créé chez Google en 2007 par Robert Griesemer, Rob Pike et Ken Thompson. C'est un langage compilé et statiquement typé dans la tradition d'Algol et de C. 

Go dispose d'un ramasse-miettes, d'un typage structurel limité, d'une sécurité mémoire et de fonctionnalités de programmation concurrente de style CSP. Le compilateur et les autres outils de langage développés à l'origine par Google sont tous libres et open source. 

La popularité de Go augmente rapidement. C'est un excellent choix pour construire des applications web.

Pour plus d'informations, rendez-vous sur la [page d'accueil de Go](https://golang.org/). Vous voulez une visite rapide de Go ? Consultez la documentation [ici](https://tour.golang.org/welcome/1).

Voyons maintenant comment installer et commencer avec Go.

## **Installation**

### Installer Golang avec Homebrew :

```bash
$ brew update
$ brew install golang
```

### **Installer Go sur MacOS en utilisant un tarball**

#### **Lien vers le tarball**

Vous pouvez obtenir le lien vers l'archive tarball MacOS à partir de la section Latest Stable de la [page de téléchargement de golang](https://golang.org/dl/).

#### **Processus d'installation**

Dans ce processus d'installation, nous utiliserons la dernière version stable à ce jour (go 1.9.1). Pour une version plus récente ou plus ancienne, remplacez simplement le lien dans la première étape. Consultez la [page de téléchargement de golang](https://golang.org/dl/) pour voir les versions actuellement disponibles.

##### **Installation de Go 1.9.1**

```text
$ curl -O https://storage.googleapis.com/golang/go1.9.1.darwin-amd64.tar.gz
$ sudo tar -C /usr/local -xzf go1.9.1.darwin-amd64.tar.gz
$ export PATH=$PATH:/usr/local/go/bin
```

### **Installer Golang sur Ubuntu avec apt**

Utiliser le gestionnaire de paquets source d'Ubuntu (apt) est l'une des méthodes les plus simples pour installer Go. Vous n'obtiendrez pas la dernière version stable, mais pour les besoins de l'apprentissage, cela devrait suffire.

```sh
$ sudo apt-get update
$ sudo apt-get install golang-go
```

#### **Vérifier l'installation et la version de Go**

Pour vérifier si Go a été installé avec succès, exécutez :

```sh
$ go version
> go version go1.9.1 linux/amd64
```

Cela affichera la version de Go installée dans la console. Si vous voyez une version de Go, vous saurez que l'installation s'est déroulée sans problème.

## Configurer l'espace de travail

### Ajouter des variables d'environnement :

Tout d'abord, vous devez indiquer à Go l'emplacement de votre espace de travail.

Nous allons ajouter quelques variables d'environnement dans la configuration du shell. L'un de ces fichiers se trouve dans votre répertoire personnel : bash_profile, bashrc ou .zshrc (pour Oh My Zsh Army).

```bash
$ vi .bashrc
```

Puis ajoutez ces lignes pour exporter les variables requises.

#### **Voici votre fichier .bashrc**

```bash
export GOPATH=$HOME/go-workspace # n'oubliez pas de changer votre chemin correctement !
export GOROOT=/usr/local/opt/go/libexec
export PATH=$PATH:$GOPATH/bin
export PATH=$PATH:$GOROOT/bin
```

## Créer votre espace de travail

### Créer l'arborescence des répertoires de l'espace de travail :

```bash
$ mkdir -p $GOPATH $GOPATH/src $GOPATH/pkg $GOPATH/bin
$GOPATH/src : Où se trouvent vos projets/programmes Go
$GOPATH/pkg : contient tous les objets de paquets
$GOPATH/bin : Le répertoire des binaires compilés
```

## Le bac à sable Golang

Apprendre à installer Go sur votre machine locale est important. Mais si vous voulez commencer à jouer avec Go directement dans votre navigateur, alors le bac à sable Go est l'environnement parfait pour commencer immédiatement !

Ouvrez simplement une nouvelle fenêtre de navigateur et allez sur le [bac à sable](https://play.golang.org/).

Une fois là-bas, vous aurez les boutons :

1. Exécuter
2. Formater
3. Imports
4. Partager

Le bouton **Exécuter** envoie simplement les instructions pour compiler le code que vous avez écrit aux serveurs Google qui exécutent le backend Golang.

Le bouton **Formater** implémente le style de formatage idiomatique du langage. Vous pouvez en lire plus à ce sujet [ici](https://golang.org/pkg/fmt/).

**Imports** vérifie simplement les paquets que vous avez déclarés dans import(). Un chemin d'importation est une chaîne qui identifie de manière unique un paquet. Le chemin d'importation d'un paquet correspond à son emplacement dans un espace de travail ou dans un dépôt distant (expliqué ci-dessous). Vous pouvez en lire plus [ici](https://golang.org/doc/code.html#ImportPaths).

Avec **Partager**, vous obtenez une URL où le code que vous venez d'écrire est sauvegardé. Cela est utile lorsque vous demandez de l'aide en montrant votre code.

Vous pouvez faire une visite plus approfondie de Go [ici](https://tour.golang.org/welcome/4) et en apprendre plus sur le bac à sable dans l'article [Inside the Go Playground](https://blog.golang.org/playground).

## Les maps en Go

Une map, appelée _dictionnaire_ dans d'autres langages, "mappe" les clés aux valeurs. Une map est déclarée comme ceci :

```go
var m map[Key]Value
```

Cette map n'a pas de clés et aucune clé ne peut y être ajoutée. Pour créer une map, utilisez la fonction `make` :

```go
m = make(map[Key]Value)
```

N'importe quoi peut être utilisé comme clé ou comme valeur.

## Modifier les maps

Voici quelques actions courantes avec les maps.

### Insérer/Modifier des éléments

Créer ou modifier l'élément `foo` dans la map `m` :

```go
m["foo"] = bar
```

### Obtenir des éléments

Obtenir l'élément avec la clé `foo` dans la map `m` :

```go
element = m["foo"]
```

### Supprimer des éléments

Supprimer l'élément avec la clé `foo` dans la map `m` :

```go
delete(m, "foo")
```

### Vérifier si une clé a été utilisée

Vérifier si la clé `foo` a été utilisée dans la map `m` :

```go
element, ok = m["foo"]
```

Si `ok` est `true`, la clé a été utilisée et `element` contient la valeur à `m["foo"]`. Si `ok` est `false`, la clé n'a pas été utilisée et `element` contient sa valeur zéro.

## Littéraux de map

Vous pouvez créer directement des littéraux de map :

```go
var m = map[string]bool{
	"Go": true,
	"JavaScript":false,
}

m["Go"] // true
m["JavaScript"] = true // Définir JavaScript à true
delete(m, "JavaScript") // Supprimer la clé et la valeur "JavaScript"
language, ok = m["C++"] // ok est false, language est la valeur zéro de bool (false)
```

## Plus d'informations sur Go :

* [Apprendre Go en 7 heures avec ce cours vidéo gratuit](https://www.freecodecamp.org/news/go-golang-course/)
* [Comment construire un bot Twitter](https://www.freecodecamp.org/news/creating-a-twitter-bot-from-scratch-with-golang-e1f37a66741/) avec Go