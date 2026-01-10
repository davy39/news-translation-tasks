---
title: Voici quelques avantages incroyables de Go dont on ne parle pas beaucoup
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-01T09:51:02.000Z'
originalURL: https://freecodecamp.org/news/here-are-some-amazing-advantages-of-go-that-you-dont-hear-much-about-1af99de3b23a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NDXd5I87VZG0Z74N7dog0g.png
tags:
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Voici quelques avantages incroyables de Go dont on ne parle pas beaucoup
seo_desc: 'By Kirill Rogovoy

  In this article, I discuss why you should give Go a chance and where to start.

  Golang is a programming language you might have heard about a lot during the last
  couple years. Even though it was created back in 2009, it has started t...'
---

Par Kirill Rogovoy

Dans cet article, je discute des raisons pour lesquelles vous devriez donner une chance à Go et par où commencer.

Golang est un langage de programmation dont vous avez peut-être beaucoup entendu parler ces dernières années. Bien qu'il ait été créé en 2009, il a commencé à gagner en popularité seulement récemment.

![Image](https://cdn-media-1.freecodecamp.org/images/5-ox2W2rahUeBEg6F-Pen5p5rh28x8whSRuM)
_Popularité de Golang selon Google Trends_

Cet article ne traite pas des principaux arguments de vente de Go que vous voyez habituellement.

Au lieu de cela, je souhaite vous présenter quelques fonctionnalités plutôt petites mais toujours significatives que vous ne découvrez qu'après avoir décidé de donner une chance à Go.

Ce sont des fonctionnalités incroyables qui ne sont pas évidentes à première vue, mais elles peuvent vous faire économiser des semaines ou des mois de travail. Elles peuvent également rendre le développement logiciel plus agréable.

Ne vous inquiétez pas si Go est quelque chose de nouveau pour vous. Cet article ne nécessite aucune expérience préalable avec le langage. J'ai inclus quelques liens supplémentaires en bas, au cas où vous souhaiteriez en apprendre un peu plus.

Nous allons aborder des sujets tels que :

* GoDoc
* Analyse statique de code
* Framework de test et de profiling intégré
* Détection des conditions de course
* Courbe d'apprentissage
* Réflexion
* Opinionatedness
* Culture

Veuillez noter que la liste ne suit aucun ordre particulier. Elle est également très subjective.

### GoDoc

La documentation dans le code est prise très au sérieux dans Go. Tout comme la simplicité.

[GoDoc](https://godoc.org/) est un outil d'analyse statique de code qui crée de belles pages de documentation directement à partir de votre code. Une chose remarquable à propos de GoDoc est qu'il n'utilise aucun langage supplémentaire, comme JavaDoc, PHPDoc ou JSDoc, pour annoter les constructions dans votre code. Juste l'anglais.

Il utilise autant d'informations que possible à partir du code pour structurer et formater la documentation. Et il a toutes les clochettes et sifflets, tels que les références croisées, les exemples de code et les liens directs vers votre dépôt de système de contrôle de version.

Tout ce que vous pouvez faire est d'ajouter un bon vieux commentaire du genre `// MyFunc transforme Foo en Bar` qui serait reflété dans la documentation, aussi. Vous pouvez même ajouter des [exemples de code](https://blog.golang.org/examples) qui sont **réellement exécutables** via l'interface web ou localement.

GoDoc est le seul moteur de documentation pour Go qui est utilisé par toute la communauté. Cela signifie que chaque bibliothèque ou application écrite en Go a le même format de documentation. À long terme, cela vous fait économiser des tonnes de temps lors de la navigation dans ces docs.

Voici, par exemple, la page GoDoc pour mon récent projet personnel : [pullkee — GoDoc](https://godoc.org/github.com/kirillrogovoy/pullkee).

### Analyse statique de code

Go repose fortement sur l'analyse statique de code. Les exemples incluent [godoc](https://godoc.org/) pour la documentation, [gofmt](https://golang.org/cmd/gofmt/) pour le formatage de code, [golint](https://github.com/golang/lint) pour le linting de style de code, et bien d'autres.

Il y en a tellement que même un projet tout-en-un appelé [gometalinter](https://github.com/alecthomas/gometalinter#supported-linters) a été créé pour les composer tous en une seule utilité.

Ces outils sont généralement implémentés comme des applications en ligne de commande autonomes et s'intègrent facilement avec tout environnement de codage.

L'analyse statique de code n'est pas vraiment quelque chose de nouveau dans la programmation moderne, mais Go la porte à l'absolu. Je ne peux pas surestimer le temps qu'elle m'a fait économiser. De plus, elle vous donne un sentiment de sécurité, comme si quelqu'un vous couvrait.

Il est très facile de créer vos propres analyseurs, car Go dispose de packages intégrés dédiés pour analyser et travailler avec les sources Go.

Vous pouvez en apprendre plus à partir de cette conférence : [GothamGo Kickoff Meetup: Go Static Analysis Tools by Alan Donovan](https://vimeo.com/114736889).

### Framework de test et de profiling intégré

Avez-vous déjà essayé de choisir un framework de test pour un projet Javascript que vous commencez à partir de zéro ? Si oui, vous comprenez peut-être cette lutte contre la paralysie de l'analyse. Vous avez peut-être aussi réalisé que vous n'utilisiez pas environ 80 % du framework que vous avez choisi.

Le problème se répète une fois que vous devez faire du profiling fiable.

Go vient avec un outil de test intégré conçu pour la simplicité et l'efficacité. Il vous fournit l'API la plus simple possible et fait des hypothèses minimales. Vous pouvez l'utiliser pour différents types de tests, de profiling, et même pour fournir des exemples de code exécutables.

Il produit une sortie compatible avec CI, et l'utilisation est généralement aussi simple que d'exécuter `go test`. Bien sûr, il supporte également des fonctionnalités avancées comme l'exécution de tests en parallèle, les marquer comme ignorés, et bien plus encore.

### Détection des conditions de course

Vous avez peut-être déjà entendu parler des Goroutines, qui sont utilisées dans Go pour atteindre l'exécution concurrente de code. Si ce n'est pas le cas, [voici](https://gobyexample.com/goroutines) une explication très brève.

La programmation concurrente dans des applications complexes n'est jamais facile, quel que soit le langage ou la technique spécifique, en partie à cause de la possibilité de conditions de course.

En termes simples, les conditions de course se produisent lorsque plusieurs opérations concurrentes se terminent dans un ordre imprévisible. Cela peut conduire à un grand nombre de bugs, qui sont particulièrement difficiles à traquer. Avez-vous déjà passé une journée à déboguer un test d'intégration qui ne fonctionnait que dans environ 80 % des exécutions ? C'était probablement une condition de course.

Tout cela dit, la programmation concurrente est prise très au sérieux dans Go et, heureusement, nous avons un outil assez puissant pour traquer ces conditions de course. Il est entièrement intégré dans la chaîne d'outils de Go.

Vous pouvez en lire plus à ce sujet et apprendre à l'utiliser ici : [Introducing the Go Race Detector — The Go Blog](https://blog.golang.org/race-detector).

### Courbe d'apprentissage

Vous pouvez apprendre TOUTES les fonctionnalités du langage Go en une soirée. Je le pense vraiment. Bien sûr, il y a aussi la bibliothèque standard et les meilleures pratiques dans différents domaines plus spécifiques. Mais deux heures suffiraient amplement pour vous permettre d'écrire en toute confiance un simple serveur HTTP ou une application en ligne de commande.

Le projet dispose d'une [documentation merveilleuse](https://golang.org/doc/), et la plupart des sujets avancés ont déjà été couverts sur leur blog : [The Go Programming Language Blog](https://blog.golang.org/).

Go est beaucoup plus facile à introduire dans votre équipe que Java (et sa famille), Javascript, Ruby, Python ou même PHP. L'environnement est facile à configurer, et l'investissement que votre équipe doit faire est beaucoup plus petit avant qu'ils ne puissent compléter votre premier code de production.

### Réflexion

La réflexion de code est essentiellement une capacité à regarder sous le capot et à accéder à différents types de méta-informations sur vos constructions de langage, telles que les variables ou les fonctions.

Étant donné que Go est un langage typé statiquement, il est exposé à un certain nombre de limitations variées lorsqu'il s'agit de programmation abstraite plus faiblement typée. Surtout comparé à des langages comme Javascript ou Python.

De plus, Go [n'implémente pas un concept appelé Generics](https://golang.org/doc/faq#generics), ce qui rend encore plus difficile le travail avec plusieurs types de manière abstraite. Néanmoins, beaucoup de gens pensent que c'est en fait bénéfique pour le langage en raison de la complexité que les Generics apportent. Et je suis totalement d'accord.

Selon la philosophie de Go (qui est un sujet à part entière), vous devriez essayer de ne pas sur-ingénier vos solutions. Et cela s'applique également à la programmation typée dynamiquement. Restez autant que possible aux types statiques et utilisez des interfaces lorsque vous savez exactement avec quels types de données vous travaillez. Les interfaces sont très puissantes et omniprésentes dans Go.

Cependant, il existe encore des cas dans lesquels vous ne pouvez pas savoir avec quel type de données vous êtes confronté. Un excellent exemple est JSON. Vous convertissez tous les types de données dans vos applications. Des chaînes, des buffers, tous types de nombres, des structures imbriquées et plus encore.

Pour y parvenir, vous avez besoin d'un outil pour examiner toutes les données en temps d'exécution qui agit différemment en fonction de son type et de sa structure. La réflexion à la rescousse ! Go dispose d'un package de première classe [reflect](https://golang.org/pkg/reflect/) pour permettre à votre code d'être aussi dynamique que dans un langage comme Javascript.

Un point important à noter est de savoir quel prix vous payez pour l'utiliser — et de ne l'utiliser que lorsqu'il n'y a pas de moyen plus simple.

Vous pouvez en lire plus à ce sujet ici : [The Laws of Reflection — The Go Blog](https://blog.golang.org/laws-of-reflection).

Vous pouvez également lire du code réel à partir des sources du package JSON ici : [src/encoding/json/encode.go — Source Code](https://golang.org/src/encoding/json/encode.go)

### Opinionatedness

Au fait, existe-t-il un tel mot ?

Venant du monde Javascript, l'un des processus les plus décourageants auxquels j'ai été confronté était de décider quelles conventions et quels outils j'avais besoin d'utiliser. Comment devrais-je styliser mon code ? Quelle bibliothèque de test devrais-je utiliser ? Comment devrais-je aborder la structure ? Quels paradigmes de programmation et approches devrais-je utiliser ?

Ce qui m'a parfois bloqué. Je faisais cela au lieu d'écrire le code et de satisfaire les utilisateurs.

Pour commencer, je devrais noter que je comprends totalement d'où devraient venir ces conventions. C'est toujours vous et votre équipe. De toute façon, même un groupe de développeurs Javascript expérimentés peut facilement se retrouver avec la plupart de l'expérience avec des outils et des paradigmes entièrement différents pour atteindre des résultats similaires.

Cela fait exploser le nuage de paralysie de l'analyse sur toute l'équipe, et rend également plus difficile l'intégration des individus entre eux.

Eh bien, Go est différent. Vous n'avez qu'un seul guide de style que tout le monde suit. Vous n'avez qu'un seul framework de test qui est intégré dans la chaîne d'outils de base. Vous avez beaucoup d'opinions fortes sur la façon de structurer et de maintenir votre code. Comment choisir les noms. Quels modèles de structuration suivre. Comment faire mieux de la concurrency.

Bien que cela puisse sembler trop restrictif, cela vous fait économiser des tonnes de temps pour vous et votre équipe. Être quelque peu limité est en fait une bonne chose lorsque vous codez. Cela vous donne un moyen plus direct d'avancer lors de l'architecture de nouveau code, et rend plus facile le raisonnement sur l'existant.

En conséquence, la plupart des projets Go se ressemblent beaucoup au niveau du code.

### Culture

Les gens disent que chaque fois que vous apprenez une nouvelle langue parlée, vous absorbez également une partie de la culture des personnes qui parlent cette langue. Ainsi, plus vous apprenez de langues, plus vous pouvez subir de changements personnels.

C'est la même chose avec les langages de programmation. Peu importe comment vous allez appliquer un nouveau langage de programmation à l'avenir, il vous donne toujours une nouvelle perspective sur la programmation en général, ou sur certaines techniques spécifiques.

Que ce soit la programmation fonctionnelle, la correspondance de motifs ou l'héritage prototypal. Une fois que vous l'avez appris, vous portez ces approches avec vous, ce qui élargit l'ensemble d'outils de résolution de problèmes que vous avez en tant que développeur logiciel. Cela change également la façon dont vous voyez la programmation de haute qualité en général.

Et Go est un excellent investissement ici. Le principal pilier de la culture de Go est de garder un code simple et terre-à-terre sans créer de nombreuses abstractions redondantes et en mettant la maintenabilité au premier plan. Il fait également partie de la culture de passer le plus de temps à travailler réellement sur la base de code, au lieu de bidouiller avec les outils et l'environnement. Ou de choisir entre différentes variations de ceux-ci.

Go est également tout à fait d'accord avec « il ne devrait y avoir qu'une seule façon de faire une chose ».

Une petite note en passant. Il est également partiellement vrai que Go se met souvent en travers de votre chemin lorsque vous devez construire des abstractions relativement complexes. Eh bien, je dirais que c'est le compromis pour sa simplicité.

Si vous devez vraiment écrire beaucoup de code abstrait avec des relations complexes, vous seriez mieux de utiliser des langages comme Java ou Python. Cependant, même lorsque ce n'est pas évident, c'est très rarement le cas.

Toujours utiliser le meilleur outil pour le travail !

### Conclusion

Vous avez peut-être entendu parler de Go auparavant. Ou peut-être est-ce quelque chose qui est resté hors de votre radar pendant un certain temps. Dans les deux cas, il y a des chances que Go puisse être un très bon choix pour vous ou votre équipe lorsque vous commencez un nouveau projet ou améliorez celui existant.

Ce n'est pas une liste complète de toutes les choses incroyables à propos de Go. **Juste celles qui sont sous-estimées**.

Veuillez, donnez une chance à Go avec [A Tour of Go](https://tour.golang.org) qui est un endroit incroyable pour commencer.

Si vous souhaitez en apprendre plus sur les avantages de Go, vous pouvez consulter ces liens :

* [Pourquoi devriez-vous apprendre Go ? — Keval Patel — Medium](https://medium.com/@kevalpatel2106/why-should-you-learn-go-f607681fad65)
* [Adieu Node.js — TJ Holowaychuk — Medium](https://medium.com/@tjholowaychuk/farewell-node-js-4ba9e7f3e52b)

Partagez vos observations dans les commentaires !

Même si vous ne cherchez pas spécifiquement un nouveau langage à utiliser, cela vaut la peine de passer une heure ou deux à en avoir un aperçu. Et peut-être qu'il pourrait devenir assez utile pour vous à l'avenir.

Toujours à la recherche des meilleurs outils pour votre métier !

Si vous aimez cet article, veuillez envisager de me suivre pour plus de contenu, et cliquez sur ces petites mains vertes amusantes juste en dessous de ce texte pour partager. ???

Consultez mon [Github](https://github.com/kirillrogovoy/) et suivez-moi sur [Twitter](https://twitter.com/krogovoy) !