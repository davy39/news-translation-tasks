---
title: Qu'est-ce que Go ? Le langage de programmation Golang expliqué
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-10-07T15:26:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-go-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/golang.png
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Qu'est-ce que Go ? Le langage de programmation Golang expliqué
seo_desc: "Go, also known as Golang, is an open-source, compiled, and statically typed\
  \ programming language designed by Google. It is built to be simple, high-performing,\
  \ readable, and efficient. \nIn this article, you'll learn:\n\nWhere Go came from\
  \ and where it ..."
---

Go, également connu sous le nom de Golang, est un langage de programmation open-source, compilé et statiquement typé conçu par Google. Il est conçu pour être simple, performant, lisible et efficace.

Dans cet article, vous apprendrez :

* D'où vient Go et où il en est maintenant,
* Pourquoi je pense que vous devriez l'apprendre,
* Comment l'installer et l'exécuter sur Windows 10, et
* Comment écrire votre premier programme "Hello World" en Go

## Table des matières
- [Quel est le nom ? Go ou Golang ?](#heading-quel-est-le-nom-go-ou-golang)
- [Comment Go est apparu](#heading-comment-go-est-apparu)
- [Pourquoi vous devriez apprendre Go](#heading-pourquoi-vous-devriez-apprendre-go)
- [Comment installer et exécuter Go sur Windows 10](#heading-comment-installer-et-executer-go-sur-windows-10)
- [Comment écrire votre premier Hello World en Go](#heading-comment-ecrire-votre-premier-hello-world-en-go)
- [Conclusion](#heading-conclusion)


## Quel est le nom ? Go ou Golang ?

Vous pourriez entendre le langage appelé à la fois Go et Golang, ce qui peut être déroutant. Je pensais autrefois qu'il s'agissait de noms pour différents langages. Mais Golang n'est qu'un autre nom pour Go – et Go reste le nom officiel.

Golang provient du nom de domaine du site officiel de Go, golang.org. Ce qui est en fait très utile, car « Golang » est beaucoup plus recherchable que "Go" sur Google. Cela facilite donc un peu la vie de ceux qui pourraient chercher des informations sur le langage de programmation.

## Comment Go est apparu

Le langage de programmation Go est né parce que les choses devenaient beaucoup plus complexes dans les bases de code au sein de Google.

Il a été conçu par Robert Griesemer, Rob Pike et Ken Thompson, qui, selon les rapports, partagent tous une aversion pour C++.

Go a été annoncé au public en 2009, et il est devenu open source en 2012 lorsque sa première version, 1.0, a été publiée.

Go a rapidement gagné en popularité et est devenu le premier choix de nombreux développeurs en raison de sa simplicité, de sa lisibilité, de son efficacité et de sa nature concurrente. Concurrent signifie qu'il peut exécuter plusieurs tâches en même temps.

Go est utilisé pour la programmation côté serveur (backend), le développement de jeux, la programmation basée sur le cloud, et même la science des données. Il est également populaire pour la création d'outils en ligne de commande.

Aujourd'hui, de nombreux géants de la technologie utilisent Go comme Google, Netflix, Twitch, Ethereum, Dropbox, Kubernetes, Docker, Heroku, et bien d'autres.

Il n'est pas surprenant que des plateformes comme Kubernetes, Docker et Heroku utilisent Go, car la programmation basée sur le cloud est l'une des principales raisons pour lesquelles Go a été conçu.

## Pourquoi vous devriez apprendre Go

### Courbe d'apprentissage facile

Go est l'un des langages de programmation les plus simples qui existent. Il est facile à apprendre, surtout si vous avez déjà des connaissances dans un autre langage de programmation. Dans mon cas, j'ai appris les bases de Go en une seule séance.

Beaucoup de développeurs qui utilisent Go et qui sont confiants dans leurs capacités d'enseignement disent qu'ils peuvent amener un débutant absolu à créer une application avec Go en seulement quelques heures.

La simplicité de Go est l'une des principales raisons pour lesquelles il a grimpé de 5 places, passant du 10e au 5e langage de programmation le plus apprécié selon l'enquête StackOverflow Developer Survey 2020.

### Communauté active et bonne documentation

Go dispose d'une documentation solide et facile à lire. Vous pouvez lire la documentation sur le site officiel.

Outre la documentation, Go dispose également d'une communauté active et solide derrière lui, vous pouvez donc toujours obtenir de l'aide lorsque vous êtes bloqué.

Le hashtag #golang est couramment utilisé sur Twitter, donc au cas où vous seriez bloqué, vous pouvez tweeter votre question et y attacher le hashtag.

### Vous pouvez faire beaucoup de choses avec Go

Go est un langage de programmation polyvalent, ce qui signifie que vous pouvez l'utiliser pour de nombreuses choses telles que le développement web, la science des données, le cloud computing, et plus encore.

Si vous souhaitez faire carrière dans la programmation basée sur le cloud, vous devriez envisager d'apprendre Go, car des plateformes telles qu'Amazon Web Services, Kubernetes et Google Cloud Platform (GCP) prennent toutes en charge Go.

### Salaires attractifs

Selon l'enquête StackOverflow Developer Survey 2020, les développeurs Go sont les troisièmes mieux payés après Perl et Scala avec un salaire médian de 74 000 $. 

Ce chiffre continuera probablement à augmenter, car Go gagne en popularité chaque année et est en demande. Donc, si vous voulez gagner plus d'argent, vous devriez envisager d'apprendre Go.

## Comment installer et exécuter Go sur Windows 10

Pour installer Go sur votre machine Windows, vous devez d'abord [télécharger Go](https://golang.org/) depuis le site officiel. Il est disponible pour tous les systèmes d'exploitation populaires. Cliquez sur celui qui correspond à votre système d'exploitation et installez-le.

**Étape 1** : Avant d'installer Go, ouvrez votre invite de commande, tapez « go » et appuyez sur Entrée. Vous pouvez ouvrir l'invite de commande en entrant « cmd » dans la barre de recherche Windows, puis en sélectionnant la première application qui s'affiche.

Lorsque vous entrez « go » et appuyez sur Entrée, vous devriez obtenir un message indiquant que « 'go' n'est pas reconnu comme une commande interne ou externe, un programme exécutable ou un fichier batch ».

![ss-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-1.png)

Ne vous inquiétez pas, c'est parce que vous devez installer Go en double-cliquant sur l'installateur téléchargé depuis le site de Go.

**Étape 2** : Double-cliquez sur l'installateur téléchargé pour installer Go. Suivez les invites en conséquence et Go sera installé.

![ss-2](https://www.freecodecamp.org/news/content/images/2021/10/ss-2.png)
![ss-3](https://www.freecodecamp.org/news/content/images/2021/10/ss-3.png)

**Étape 3** : Après avoir installé Go via l'installateur, retournez à la ligne de commande et entrez « go » à nouveau. Cette fois-ci, vous devriez voir plusieurs commandes disponibles dans Go.

![ss-4](https://www.freecodecamp.org/news/content/images/2021/10/ss-4.png)

**Étape 4** : Mais vous ne pouvez pas simplement commencer à programmer en Go comme ça. Vous devez configurer votre espace de travail Go en configurant les variables d'environnement.

Alors, rendez-vous sur votre bureau et créez le dossier « go-workspace ». Vous pouvez le nommer comme vous le souhaitez. C'est le dossier où vos projets Go seront stockés. Seulement lorsque vous définissez la valeur de la variable `GOPATH` à celui-ci. Nous faisons cela dans les étapes suivantes.

**Étape 5** : Recherchez « env » dans la barre de recherche Windows et cliquez sur « Modifier les variables d'environnement système ».

![ss-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-5.png)

**Étape 6** : Cliquez sur « Variables d'environnement ».

![ss6-edited-1](https://www.freecodecamp.org/news/content/images/2021/10/ss6-edited-1.jpg)

Ce que vous allez faire ici est de changer la valeur de la variable `GOPATH` pour le dossier que vous avez créé dans l'**Étape 4**.

**Étape 7** : Assurez-vous que « GOPATH » est sélectionné, puis cliquez sur « Modifier... ».

![ss-7edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-7edited.jpg)

**Étape 8** : Cliquez sur « Parcourir le répertoire ».

![ss-8edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-8edited.jpg)

**Étape 9** : Sélectionnez le dossier que vous avez créé dans l'**Étape 4**. C'est-à-dire, « go-workspace », ou peu importe comment vous l'avez nommé.

![ss-9edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-9edited.jpg)

Cliquez sur « Ok ».

![ss-10edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-10edited.jpg)

Cliquez à nouveau sur "Ok".

![ss-11edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-11edited.jpg)

Et à nouveau "Ok".

![ss-12edited](https://www.freecodecamp.org/news/content/images/2021/10/ss-12edited.jpg)

C'est tout ! Vous pouvez maintenant commencer à programmer en Go sur votre machine Windows.

## Comment écrire votre premier Hello World en Go

**Étape 1** : Ouvrez le dossier « go-workspace » (ou peu importe comment vous l'avez nommé) avec VS Code (ou votre éditeur de code de choix) et créez un fichier nommé `main.go`. Vous pouvez nommer le fichier comme vous le souhaitez.

![ss-13](https://www.freecodecamp.org/news/content/images/2021/10/ss-13.png)

**Étape 2** : Lorsque vous appuyez sur Entrée, vous serez invité à installer l'extension Go pour VS Code. Assurez-vous de l'installer car elle donnera à votre éditeur de code quelques superpouvoirs Golang tels que la coloration syntaxique et les suggestions de snippets.

Vous devriez également être invité par VS Code à installer quelques extensions supplémentaires. Installez-les toutes. Dans mon cas, j'ai déjà installé tout pour mon VS Code et toutes mes extensions sont synchronisées, donc je n'ai pas reçu ces invites.

Collez le code suivant dans le fichier main.go (ou peu importe comment vous avez nommé le fichier) :

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

**Que fait le code ci-dessus ?**

La première ligne contient `package main`. « package » est une collection de fichiers et de code que chaque fichier Go possède. Considérez `package` comme un dossier contenant vos fichiers et codes Go.

Peu importe comment vous avez nommé votre fichier, assurez-vous que le « package main » est disponible en haut de votre code.

Après cela, `fmt` est importé. « fmt » est un package de la bibliothèque standard de Go. Il est utilisé pour formater des chaînes et imprimer des messages sur la ligne de commande. Il contient des méthodes pour faire des choses en Go.

L'une des méthodes est `Println`, signifiant « print line », que nous utiliserons pour imprimer notre texte « Hello World ».

À l'intérieur de la fonction « main », le package `fmt` a ensuite été utilisé pour sortir notre texte « Hello World » vers la console.

Pour exécuter ce code, ouvrez votre terminal, tapez `go run main.go`, et appuyez sur Entrée. Si vous avez nommé votre fichier autrement, faites `go run votreNomDeFichier.go`.

![ss-14](https://www.freecodecamp.org/news/content/images/2021/10/ss-14.png)

## Conclusion

Dans cet article, vous avez appris le langage de programmation Go et pourquoi il est bon de le connaître. Vous avez également appris comment installer Go sur une machine Windows et écrire votre premier programme Hello World.

Go est un langage de programmation puissant qui est là pour rester. Il est clair d'après l'enquête StackOverflow Developer Survey 2020 que les développeurs adorent Go, et sa popularité augmente d'année en année.

Go vaut définitivement votre temps. Maintenant, allez apprendre un peu de Go.