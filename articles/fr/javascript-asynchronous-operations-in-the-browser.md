---
title: Comment fonctionnent les opérations asynchrones de JavaScript dans le navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-16T21:58:01.000Z'
originalURL: https://freecodecamp.org/news/javascript-asynchronous-operations-in-the-browser
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pankaj-patel-1IW4HQuauSU-unsplash.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionnent les opérations asynchrones de JavaScript dans le navigateur
seo_desc: "By Amazing Enyichi Agu\nJavaScript is a popular programming language used\
  \ for developing interactive front-end web applications, among other things. \n\
  It's widely known for its major features: it is single-threaded, non-blocking, and\
  \ asynchronous. But ..."
---

Par Amazing Enyichi Agu

JavaScript est un langage de programmation populaire utilisé pour développer des applications web interactives front-end, entre autres. 

Il est largement connu pour ses principales caractéristiques : il est _monothread_, _non bloquant_ et _asynchrone_. Mais que signifient ces trois choses ?

### Que signifie "Monothread" ?

Lorsque l'on dit qu'un langage de programmation est monothread, cela signifie que le langage ne peut exécuter qu'une seule instruction à la fois. Cela diffère des langages de programmation multithreads qui exécutent plusieurs instructions simultanément.

![Illustration représentant les processus monothread et multithread](https://www.freecodecamp.org/news/content/images/2023/05/single-and-multi-threads.png)
_Illustration représentant les processus monothread et multithread_

### Que signifie "Non bloquant" ?

Lorsque l'on dit qu'un langage de programmation est non bloquant, cela signifie que le langage n'attend pas qu'une instruction précédente spécifique ait fini de s'exécuter avant de passer à la suivante. Cela garantit qu'aucune instruction ne bloque ou n'obstrue l'exécution des instructions suivantes. 

Si un langage de programmation n'est pas non bloquant, cela pourrait entraîner des applications lentes.

![Illustration du comportement non bloquant de JavaScript](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2.png)
_Illustration du comportement non bloquant de JavaScript_

### Que signifie "Asynchrone" ?

JavaScript est également asynchrone (async), ce qui signifie qu'il peut gérer un grand nombre de tâches à la fois. C'est une caractéristique des langages de programmation multithreads, mais JavaScript y parvient avec un seul thread.

![Illustration du processus asynchrone](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-3.png)
_Illustration du processus asynchrone_

Maintenant, ces caractéristiques de JavaScript peuvent sembler contradictoires. Comment un langage qui est censé exécuter une seule tâche à la fois (monothread) peut-il gérer un grand nombre de tâches (asynchrone) simultanément ?

Dans cet article, vous comprendrez comment JavaScript parvient à rester monothread malgré l'exécution d'opérations asynchrones dans le navigateur. Nous explorerons également certains concepts nécessaires pour comprendre le processus.

Cet article suppose que vous avez des connaissances de base en JavaScript et que vous pouvez l'appliquer aux applications web. L'article couvre les étapes que JavaScript suit pour gérer les opérations async dans le navigateur. Il n'entre pas dans les détails pour enseigner les différentes fonctions async qui existent, ou comment les écrire. Il couvre uniquement leur processus d'exécution dans le navigateur.

La partie passionnante de tout cela est que l'article raconte une courte histoire, et utilise cette histoire comme une analogie pour expliquer le processus. Grâce à cette approche unique, vous obtiendrez plus d'informations sur le fonctionnement interne des opérations asynchrones.

Voici ce que nous allons couvrir :

1. [L'histoire qui aidera à expliquer ces concepts](#heading-lhistoire)
2. [Comment fonctionne le moteur JavaScript](#heading-comment-fonctionne-le-moteur-javascript)
3. [Comment fonctionne la pile d'appels](#heading-comment-fonctionne-la-pile-dappels)
4. [Opérations asynchrones et Web APIs](#heading-operations-asynchrones-et-web-apis)
5. [Fonctions de rappel](#heading-fonctions-de-rappel)
6. [File d'attente de rappel](#heading-file-dattente-de-rappel)
7. [Boucles d'événements](#heading-boucles-devenements)
8. [Conclusion](#heading-conclusion)

## L'histoire

C'est l'histoire de deux entreprises. L'une s'appelle _Lerdorf Corp_ tandis que l'autre est _Eich Agency_. Ces deux entreprises sont des agences de planification d'événements et elles s'occupent de clients qui ont besoin de services professionnels de planification d'événements.

Lerdorf Corp est une entreprise ancienne et prospère. Ils ont beaucoup de personnel et plusieurs départements spécialisés qui travaillent ensemble pour s'assurer qu'ils restent rentables. Ces départements incluent la restauration, l'enregistrement et la billetterie, la comptabilité, et plus encore.

Lorsque Lerdorf Corp obtient un contrat avec un client, leur processus de travail efficace se met en marche. L'entreprise décompose rapidement le projet en tâches gérables et les attribue aux départements respectifs responsables de leur exécution. Cette division du travail assure que chaque département peut se concentrer sur son domaine d'expertise spécifique, travaillant en synchronisation pour livrer des résultats.

Cette approche opérationnelle que Lerdorf Corp emploie est similaire à la façon dont les [langages de programmation multithreads](https://en.wikipedia.org/wiki/List_of_concurrent_and_parallel_programming_languages#Multi-threaded) fonctionnent. En programmation multithread, un programme peut être divisé en [threads](https://en.wikipedia.org/wiki/Thread_(computing)) séparés, chacun s'exécutant indépendamment des autres.

Revenant à notre histoire, concentrons-nous maintenant sur l'agence Eich. C'est une petite agence avec un personnel limité. Malgré leurs aspirations ambitieuses, il peut sembler assez risible qu'ils visent à rivaliser avec la bien établie Lerdorf Corp.

Lerdorf Corp ne les voyait initialement pas comme une concurrence. Ils ont donné à Eich Agency un mois ou deux pour quitter le marché. Eich Agency n'avait aucun département spécialisé. Pourtant, ils ont réussi à organiser de grands événements, exactement de la taille que l'on penserait que seule Lerdorf Corp pourrait réaliser. La base de clients d'Eich Agency s'est également régulièrement élargie au fil du temps.

Lerdorf Corp ne comprenait pas comment cela pouvait être le cas. Il était clair pour eux qu'Eich Agency n'avait pas suffisamment de ressources. Ils ont eu du mal à comprendre la situation et ont finalement tenu une réunion concernant ce problème.

Lors de la réunion, ils ont décidé d'enquêter sur la manière dont Eich Agency pouvait organiser des événements pour les clients si rapidement sans assez de ressources. Lerdorf a décidé de désigner un membre capable du personnel pour mener une enquête approfondie sur l'agence et compiler un rapport complet en une semaine. 

Après une semaine, le rapport a été complété, et le personnel exécutif de Lerdorf Corp l'a examiné ensemble.

## Comment fonctionne le moteur JavaScript

Avec l'enquête, il s'est avéré qu'Eich Agency avait une équipe centrale. L'équipe recevait des demandes de planification d'événements pour les clients. Cette équipe était responsable de la majeure partie de la planification. Ils généraient un plan pour le déroulement d'un événement.

L'équipe d'Eich Agency commandait généralement les petites tâches qu'ils devaient exécuter dans une feuille de route, puis ils commençaient de haut en bas, les exécutant dans l'ordre. Ils faisaient cela parce qu'ils n'avaient pas de départements séparés dédiés à un ensemble de tâches comme Lerdorf Corp.

JavaScript exécute les instructions de manière similaire à celle d'Eich Agency. Pour qu'un navigateur interprète le code JavaScript, il doit avoir un [moteur JavaScript](https://en.wikipedia.org/wiki/JavaScript_engine). Ce moteur JavaScript est un composant logiciel d'un navigateur web moderne qui accepte le code JavaScript, l'analyse et le transforme en instructions que l'appareil comprendra. Le moteur JavaScript peut être comparé à l'équipe centrale d'Eich Agency.

![Moteur JavaScript à l'intérieur du Runtime](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-1.png)
_Moteur JavaScript à l'intérieur du Runtime_

Le runtime JavaScript est l'environnement qui contient toutes les ressources nécessaires à l'exécution d'un programme JavaScript. Il inclut le moteur JavaScript mais aussi d'autres éléments que nous allons examiner.

Les différents navigateurs utilisent aujourd'hui différents moteurs JavaScript. Par exemple, le navigateur Chrome utilise le [moteur V8 de Google](https://v8.dev/), Firefox utilise un moteur appelé [Spidermonkey](https://spidermonkey.dev/), et le navigateur Opera utilisait auparavant le moteur [Carakan](https://dev.opera.com/blog/carakan/), avant de passer à V8.

Ces moteurs ont des différences individuelles, mais leurs tâches restent les mêmes. Ils traitent le code JavaScript.

## Comment fonctionne la pile d'appels

Alors que le personnel de Lerdorf Corp examinait le rapport, ils ont fait une découverte intrigante. Eich Agency, après avoir finalisé la séquence des tâches préparatoires pour un événement à venir, affichait la liste sur leur tableau. Avec cet ordre en place, l'équipe centrale savait quelle tâche commencer et quelle tâche continuer.

Le tableau qu'Eich Agency utilise pour lister publiquement l'ordre des tâches est similaire à la pile d'appels dans le moteur JavaScript. La pile d'appels est un composant du moteur JavaScript qui suit toutes les fonctions que le programme exécute. C'est une structure de données [pile](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) qui fonctionne avec deux opérations clés.

Ces opérations sont :

* Push : Cette opération ajoute ou pousse une nouvelle fonction au sommet de la pile. La pile ne peut ajouter de nouvelles entrées qu'au sommet.
* Pop : Cette opération retire ou fait sortir une nouvelle fonction du sommet de la pile. La pile ne peut retirer de nouvelles entrées qu'à partir du sommet.

**Dernier entré, premier sorti (LIFO)** est un terme qui résume le fonctionnement de la pile d'appels. La dernière opération entrée est la première opération qui quittera la pile.

![Illustration simple de la pile d'appels](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--1-.png)
_Illustration simple de la pile d'appels_

Après que le moteur JavaScript reçoit le code JavaScript, il analyse le code et place la première fonction qu'il rencontre sur la pile d'appels. Si, lors de l'exécution de cette fonction, le moteur JavaScript remarque qu'elle appelle d'autres fonctions, alors ces fonctions sont empilées au sommet de la pile d'appels. Cela est très important pour les fonctions imbriquées dans d'autres fonctions ainsi que pour les fonctions récursives.

La pile d'appels permet de suivre les fonctions en cours d'exécution et futures essentielles à l'exécution d'un programme. Pour que la pile retire une fonction, le moteur doit avoir terminé l'interprétation et l'exécution de cette fonction. Sinon, elle reste là. Un coup d'œil à la pile d'appels JavaScript pendant l'exécution d'un programme montre l'état actuel du programme.

Par exemple, considérons ces instructions JavaScript.

```javascript
function greeting() {
	console.log("Hello World")
}

function run() {
	greeting()
}

run()

```

Lors de l'exécution du code, la pile d'appels peut ressembler à ceci :

![La pile d'appels lors de la surveillance des fonctions](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--2-.png)
_La pile d'appels lors de la surveillance des fonctions_

Pour résumer, chaque fois que le moteur JavaScript reçoit du code, il l'analyse et utilise une pile d'appels pour surveiller l'exécution de ces instructions. Cela est similaire à la manière dont Eich Agency affiche l'ordre des tâches qu'ils doivent accomplir.

## Opérations asynchrones et Web APIs

La manière dont l'équipe centrale d'Eich Agency ordonnait les tâches qu'ils voulaient exécuter n'était pas étrange pour Lerdorf Corp. Ils employaient eux-mêmes une stratégie similaire lorsqu'ils voulaient travailler pour des clients, mais il y avait quelques distinctions.

Chez Lerdorf, chaque fois qu'ils obtenaient un contrat, la première chose qu'ils faisaient était de diviser la tâche en quelques morceaux plus petits. Après l'avoir décomposée, ils envoyaient ces morceaux à différents départements qu'ils avaient. Ils avaient beaucoup de départements et le processus était plus rapide si ces départements commençaient à travailler sur les tâches indépendamment.

Lerdorf Corp avait déjà chaque département individuel avec leur propre tableau similaire à celui utilisé par Eich Agency. Les départements l'utilisaient pour suivre les tâches à accomplir. 

En termes JavaScript, ils avaient de nombreuses "piles d'appels" qui fonctionnaient indépendamment. Pendant ce temps, Eich Agency n'avait qu'une seule "pile d'appels".

Cette révélation a encore plus intrigué l'équipe de Lerdorf Corp. Comment Eich Agency parvenait-il alors à organiser de grands événements correctement s'ils n'avaient pratiquement qu'un seul département ? C'était la question que tout le monde se posait.

Lors d'un examen plus approfondi du rapport, l'équipe de Lerdorf a fait une découverte choquante. Ils ont découvert que l'équipe centrale d'Eich Agency ne faisait pas tout le travail elle-même. Ils n'avaient pas de département de restauration ou audiovisuel, alors que ce sont des départements que Lerdorf Corp avait.

Mais sur la base des contrats que Eich Agency avait obtenus, ils étaient généralement censés fournir ces services. Lors de la rédaction de leurs listes de tâches, ils incluaient la fourniture de ces services, même si l'agence ne pouvait pas les fournir en interne.

Voici ce qu'ils ont fait à la place : lors de l'exécution de leurs tâches, chaque fois qu'Eich Agency rencontrait une tâche qu'ils ne pouvaient pas exécuter immédiatement, ils agissaient. Ils contactaient une autre entreprise offrant ce service spécifique et demandaient de l'aide. Après avoir contacté l'entreprise, ils revenaient à leur ordre de tâches.

Si, en suivant leur liste de tâches, ils rencontraient une autre tâche qu'ils ne pouvaient pas effectuer, ils répétaient le processus. Ils trouveraient un fournisseur de services séparé, discuteraient de leurs besoins avec eux et demanderaient le service requis.

En rapport avec JavaScript, même si JavaScript est monothread, il est également asynchrone. En programmation asynchrone, un langage peut exécuter plusieurs tâches simultanément. Tout comme Eich Agency, chaque fois que JavaScript rencontre des instructions asynchrones comme des requêtes vers des sites tiers, ou des actions basées sur un minuteur, il cherche de l'aide. 

Pour y parvenir, JavaScript utilise les **Interfaces de Programmation d'Applications Web (Web APIs)** fournies par le navigateur.

Une raison très importante d'écrire du code asynchrone est d'éviter un scénario où une fonction en cours d'exécution finit par bloquer le reste du code. Si cela se produit, cela peut causer des expériences utilisateur indésirables et rendre notre logiciel inefficace.

Les Web APIs sont un ensemble de fonctions fournies par le navigateur que le moteur JavaScript peut utiliser. Elles incluent des exemples tels que les méthodes de manipulation du Document Object Model (DOM), `fetch`, `setInterval`, `setTimeout`, les promesses, les fonctions async-await, et plus encore.

![Le moteur JavaScript interagissant avec les Web APIs](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--3-.png)
_Le moteur JavaScript interagissant avec les Web APIs_

### Fonctions de rappel

Revenons brièvement à l'histoire de Lerdorf Corp et Eich Agency. Rappelez-vous qu'Eich Agency contractait des fournisseurs de services et demandait leur assistance, puis continuait avec leur ordre d'exécution.

Chaque fois que l'un des fournisseurs de services externes rappelait l'agence pour livrer une réponse, comme notifier l'achèvement d'une demande, l'agence agissait ensuite sur cette nouvelle information. 

Lerdorf Corp a découvert que même si les fournisseurs externes géraient et complétaient de nombreux services, l'équipe centrale de l'agence devait encore prendre des mesures supplémentaires.

Par exemple, supposons que l'équipe centrale d'Eich Agency ait demandé à un fournisseur de services de restauration de fournir une certaine quantité de collations et de boissons. L'équipe centrale serait toujours responsable de la collecte des collations auprès des traiteurs et de leur incorporation dans leur inventaire d'articles pour l'événement. Dans ce scénario, les collations rejoindraient d'autres articles que Eich Agency avait préparés pour l'événement.

Cela est similaire à la façon dont JavaScript fonctionne dans le navigateur. Les opérations asynchrones fournissent une réponse après avoir été traitées à l'aide des Web APIs. Le but d'écrire une fonction asynchrone est d'utiliser la sortie de la fonction pour les opérations ultérieures. Nous appelons les fonctions qui dépendent de la réponse des opérations asynchrones des fonctions de rappel.

Une fonction de rappel est une fonction qui est passée en argument à une fonction parente, que la fonction parente doit invoquer après avoir terminé son processus. En JavaScript, les opérations asynchrones utilisent des fonctions de rappel pour traiter davantage les réponses qu'elles reçoivent des Web APIs.

L'exemple ci-dessous est une opération asynchrone avec une fonction de rappel.

```javascript
button.addEventListener('click', function () {
	console.log('J\'ai été cliqué !')
})
```

Maintenant, chaque fois que l'utilisateur clique sur le bouton, cela déclenche la fonction de rappel. Mais le rappel ne peut pas se produire à moins que la fonction parente ne l'appelle ou ne l'invoque, ce qui dépend de l'action de l'utilisateur.

Vous pouvez également observer l'utilisation de fonctions de rappel avec l'API **`fetch`**.

```javascript
fetch("<https://jsonplaceholder.typicode.com/users>")
.then((response) => response.json())
.then((response) => console.log(response))
```

Dans cet exemple, la méthode **`then`** de l'objet **`fetch`** accepte une fonction fléchée comme argument. L'exécution de cette fonction dépend de la réponse reçue de la requête fetch, ce qui en fait une fonction de rappel. 

De plus, dans la deuxième méthode **`then`**, vous pouvez voir l'utilisation d'un autre rappel. Cela est dû au fait que le premier rappel retourne une autre fonction asynchrone, nécessitant l'utilisation d'un rappel.

Pour résumer, une fonction de rappel est passée en argument à une fonction asynchrone et ne s'exécute que lorsque l'opération asynchrone a été complétée. Cela est similaire à la manière dont Eich Agency n'exécute certaines tâches que lorsque leurs fournisseurs tiers les ont rappelés.

### File d'attente de rappel

En continuant leur examen du processus d'exécution d'Eich Agency, l'équipe de Lerdorf Corp a également découvert qu'Eich Agency recevait souvent plusieurs "rappels" des fournisseurs qu'ils avaient contactés. Chacune de ces réponses nécessitait une action de l'équipe d'Eich Agency.

Eich Agency a rationalisé son processus en tenant une liste séparée. C'était une liste où, chaque fois qu'un fournisseur leur envoyait une réponse sur laquelle ils devaient agir, ils mettaient cette action à l'intérieur de la liste. 

C'est ce qu'ils ont fait pour chaque "rappel" qu'ils ont reçu. Eich Agency a finalement terminé avec une file d'attente de tâches supplémentaires à effectuer mais dans une liste séparée de celle affichée sur leur tableau.

Cette liste est similaire à la file d'attente de rappel dans le runtime JavaScript du navigateur. La file d'attente de rappel est un mécanisme logiciel qui stocke les fonctions de rappel à exécuter après que les Web APIs ont traité les fonctions asynchrones. Elle utilise la structure de données [file d'attente](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) qui fonctionne avec l'approche **Premier Entré, Premier Sorti (FIFO)**. Cela signifie que le premier rappel ajouté à cette file d'attente sera le premier rappel à en sortir.

![Runtime JavaScript montrant la file d'attente de rappel](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--4-.png)
_Runtime JavaScript montrant la file d'attente de rappel_

### Boucles d'événements

Eich Agency a mis en place une dernière étape pour s'assurer que tout se passait bien entre eux et leurs clients. Ils attendaient d'avoir terminé les tâches sur leur tableau initial avant de s'attaquer à la file d'attente des tâches supplémentaires.

Eich Agency a désigné un membre de leur équipe centrale pour gérer la file d'attente des tâches. Ce membre de l'équipe attendait que les tâches régulières soient terminées par les autres membres de l'équipe. Une fois les tâches initiales terminées, le membre de l'équipe désigné sélectionnait le premier élément de la file d'attente des tâches supplémentaires et l'affichait sur le tableau.

L'équipe centrale procédait ensuite à l'accomplissement de la tâche assignée, comme recevoir les fournitures de collations des fournisseurs. Une fois accomplie, le membre de l'équipe responsable de la gestion des tâches supplémentaires sélectionnait l'élément suivant et l'ajoutait au tableau. L'équipe centrale travaillait ensuite à l'accomplissement de cette tâche, et le processus se répétait en boucle jusqu'à ce que tous les éléments de la file d'attente des tâches supplémentaires soient épuisés.

Le membre de l'équipe responsable des tâches supplémentaires peut être comparé à la boucle d'événements dans le runtime JavaScript du navigateur. La boucle d'événements est une boucle qui vérifie en continu si la pile d'appels est vide. Lorsque la pile d'appels n'est pas vide, elle permet au processus en cours de continuer. Mais lorsque la pile d'appels devient vide, la boucle d'événements récupère la tâche en haut de la file d'attente de rappel et l'ajoute à la pile d'appels.

La boucle d'événements s'exécute en continu tant que le programme est en cours d'exécution, accomplissant toujours sa fonction jusqu'à ce que la file d'attente de rappel soit complètement vide. C'est pourquoi le moteur JavaScript exécute les rappels uniquement après que tout dans la pile d'appels a été traité.

Par exemple, considérons cet extrait de code.

```javascript
console.log('A')
setTimeout(() => console.log('B'), 0)
console.log('C')

// A
// C
// B

```

Il finit par logger A et C avant B, même si le délai était de 0 secondes. La raison en est que le rappel dans `setTimeout` a attendu dans la file d'attente de rappel (`setTimeout` utilise le Web API). Le moteur JavaScript a dû finir de traiter les fonctions synchrones avant de traiter les fonctions asynchrones. Il avait besoin de l'aide de la boucle d'événements pour envoyer la fonction de rappel à la pile d'appels.

![La boucle d'événements dans le runtime JavaScript](https://www.freecodecamp.org/news/content/images/2023/05/asynchronous-javascript---Page-2--5-.png)
_La boucle d'événements dans le runtime JavaScript_

Pour compléter l'histoire, après que Lerdorf Corp a compris comment Eich Agency fonctionnait, ils ont été impressionnés. Ils admiraient la manière dont Eich Agency utilisait ses ressources, mais ils ont immédiatement vu que cela représentait une menace pour eux et pourrait potentiellement impacter négativement leur entreprise.

Plus tard, cependant, Lerdorf Corp a réalisé que leur base de clients différait de celle d'Eich Agency. Alors qu'Eich Agency excellait dans la planification d'événements sociaux, Lerdorf Corp se spécialisait dans le travail avec les entreprises et l'organisation d'événements corporatifs. Il n'y avait pas besoin pour eux de se sentir menacés par le succès d'Eich Agency. :)

## Conclusion

Dans cet article, vous avez appris divers concepts importants qui illustrent la nature asynchrone de JavaScript. 

Nous avons commencé par discuter des trois caractéristiques fondamentales de JavaScript - qu'il est monothread, qu'il est non bloquant et qu'il est asynchrone - et nous avons reconnu qu'elles peuvent initialement sembler contradictoires. Après cela, nous avons clarifié cette apparente mécompréhension en expliquant les détails.

Vous avez appris certains concepts comme le moteur JavaScript dans le navigateur, la pile d'appels, les fonctions de rappel, la file d'attente de rappel et la boucle d'événements.

De plus, nous avons utilisé une histoire comme une analogie pour améliorer votre compréhension de ces concepts. Avec cela, vous devriez avoir acquis une compréhension solide du fonctionnement des opérations asynchrones dans le navigateur.