---
title: Notre équipe a rompu avec les versions instantanément obsolètes et vous pouvez
  en faire autant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-05T13:47:05.000Z'
originalURL: https://freecodecamp.org/news/our-team-broke-up-with-instant-legacy-releases-and-you-can-too-d129d7ae96bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4HwxRppmVvjdyhlytqVXsg.jpeg
tags:
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Notre équipe a rompu avec les versions instantanément obsolètes et vous
  pouvez en faire autant
seo_desc: 'By Jonathan Solórzano-Hamilton

  The concept of legacy conveys permanence, value, and the greatness we bequeath to
  our children and our successors in the community.

  People make ludicrously generous donations to charitable causes to establish their
  lega...'
---

Par Jonathan Solórzano-Hamilton

Le concept de **patrimoine** évoque la permanence, la valeur et la grandeur que nous léguons à nos enfants et à nos successeurs dans la communauté.

Les gens font des dons ridiculement généreux à des causes caritatives pour établir leur héritage. Ils créent des dotations ou des bâtiments éponymes et s'efforcent de protéger le nom que leurs enfants hériteront.

Il est donc frappant de constater que les développeurs de logiciels ont si catastrophiquement mal compris leur « patrimoine ».

Recherchez « legacy » sur Google, et vous verrez que la première définition correspond à ce que je vous ai présenté ici. C'est une définition qui persiste depuis le 14e ou 15e siècle.

La deuxième définition offre un contraste choquant :

> legacy. adjectif (informatique) « désignant un logiciel ou un matériel qui a été remplacé mais qui est difficile à remplacer en raison de son utilisation généralisée. »

Les dictionnaires sur internet sont d'accord avec cette définition. Elle ne s'applique qu'au domaine de l'informatique. Nous, les développeurs, avons réussi à inverser la définition de notre propre héritage dans le clin d'œil historique qu'est l'informatique. C'est presque impressionnant !

Si vous êtes un développeur expérimenté, vous avez certainement été chargé de maintenir au moins un système hérité dans votre carrière. Pour les non-initiés, eh bien — achetez beaucoup de boissons caféinées.

Je vais vous raconter brièvement l'histoire de notre relation toxique avec notre base de code héritée. Je décrirai ensuite comment nous avons rompu avec elle, et ce que nous avons changé pour éviter de retomber dans de mauvaises relations avec du code à haute maintenance.

### La rupture

Il a fallu huit mois de semaines de sept jours et de journées de douze heures pour terminer notre dernière révision du système hérité.

Nos prédécesseurs avaient poussé du code en production pendant des années sans écrire une seule ligne de documentation. En fait, une partie n'était même pas dans le contrôle de source, comme nous l'avons appris plus tard. Mais c'est une autre histoire.

Je suis sûr que vous avez déjà vu des pépites comme celle-ci :

```
... des centaines de lignes de code incompréhensibles
```

```
// TODO: Corriger ce bug !!!
```

```
... des centaines de lignes de plus dans la même méthode, sans idée de l'endroit ou du bug
```

C'est à peu près le ratio et la qualité de la seule documentation que nous avions sur le projet.

![Image](https://cdn-media-1.freecodecamp.org/images/mNqLDDzKAdUWBbGtK6vTgbtPhFYfANA3-Btv)
_Je me demande s'ils avaient Tom Felton qui travaillait en moonlight comme développeur de support de production pour le garder blanc de Slytherin ([source](http://tomfelton.org/" rel="noopener" target="_blank" title="))_

Je n'ai pas été exposé à la lumière directe du soleil avant avril, et j'en avais assez. Il était temps de rompre.

### L'importance de la documentation

Dans son livre « The Art of Unit Testing », Roy Osherove définit le code hérité comme tout code qui n'a pas de tests. Il était optimiste. Je considère plus librement comme hérité tout code qui contient **plus de dette technique** que le **temps qu'il a fallu pour l'écrire**.

Comme notre organisation l'a fait, de nombreuses équipes de développement tombent dans le piège du **code instantanément obsolète** : du code qui porte déjà l'étiquette de « code hérité » au moment de sa sortie.

Selon mon expérience, la documentation est l'aspect le plus important pour éviter un tel code hérité.

Je n'ai pas encore rencontré de développeur qui aime l'idée de la documentation. D'un autre côté, je n'ai jamais rencontré non plus de développeur qui aime se plonger dans le crâne d'un inconnu pour reverse-engineer une implémentation héritée sans aucune documentation.

Comme on dit, rompre est difficile à faire. Mais dans ce cas, je vous promets que cela en vaudra la peine.

Alors commençons à convertir votre héritage en quelque chose dont vous serez fier de léguer à vos successeurs. Commençons à documenter !

### Notre approche : quatre couches de documentation

Nous avons créé, et commencé à suivre rigoureusement, une architecture de documentation en quatre couches. Nous maintenons trois couches de documentation persistante pour le projet tout au long de son cycle de vie. Nous communiquons également à travers une couche de documentation éphémère pendant notre processus de gestion des versions.

Les trois couches persistantes de documentation correspondent à trois vitesses différentes dans notre processus de développement. Nous incluons la révision de la documentation dans le cadre de la révision du code pour éviter de retomber dans de mauvaises habitudes.

#### // Les premières lignes : les commentaires en ligne gardent les mainteneurs sains d'esprit

Le niveau le plus granulaire de documentation explicite est dans le code. Nous effectuons une documentation complète de toutes les classes et méthodes, leurs entrées, sorties attendues et chemins d'exception. Nous documentons également le code « inhabituel » en ligne.

En tant que principal utilisateur de C#, nous utilisons la documentation /// de manière omniprésente. Cela décore les déclarations de classe, d'interface et de méthode. L'assistant /// génère automatiquement des stubs XML pour documenter les tenants et aboutissants de l'API.

Celles-ci apparaissent lorsque votre code est référencé par un projet externe ou une DLL (bibliothèque de liens dynamiques), à condition que vous ayez distribué les fichiers de débogage. Notre IDE (environnement de développement intégré) rend cela sous forme d'aide de bulle partout où une référence apparaît. Cela aide grandement les développeurs, qui plongent dans notre code pour la première fois, lorsqu'ils essaient de corriger un bug ou de l'étendre pour un nouveau cas d'utilisation.

Il est utile de rechercher votre langage et IDE de choix pour apprendre comment l'étendre avec une aide contextuelle pour vos bibliothèques.

Nous incluons également des commentaires réguliers // au-delà de la documentation de l'API. Nous les ajoutons partout où le code est contre-intuitif, ou si nous avons trouvé une solution particulièrement élégante à un problème. Nous les utilisons également pour créer des « à faire » pour un refactoring ultérieur lors de la mise en place d'une correction rapide et sale.

Ceux-ci sont inestimables pour quiconque doit venir et [annuler le changement](https://blog.kentcdodds.com/please-don-t-commit-commented-out-code-53d0b5b26d5f) ou corriger le code.

Parce qu'il est en ligne avec le code source, cette documentation change à la vitesse la plus élevée — en même temps que le code qu'elle supporte.

#### README : rendre l'implémentation facile

Nous utilisons les fichiers README comme guide de l'implémenteur. Cette documentation est pour quiconque utilisera nos bibliothèques. Elle sert un but secondaire comme documentation de niveau tactique des particularités de l'implémentation.

Nous utilisons GitHub pour le contrôle de source, donc nous plaçons des fichiers readme.md ([Markdown](https://daringfireball.net/projects/markdown/syntax)) dans chaque dossier de notre dépôt GitHub. GitHub rend très bien les fichiers Markdown et montre automatiquement les fichiers readme.md rendus dans chaque dossier. Cela donne un fichier d'aide beaucoup plus utilisable qu'un simple document .txt.

![Image](https://cdn-media-1.freecodecamp.org/images/SlYVVWgXbpOClWHuVRLfoQc0ZMjQyjyCpCuu)
_Le logo [Markdown](https://daringfireball.net/projects/markdown/syntax" rel="noopener" target="_blank" title=")_

Stocker cette documentation dans la base de code aide les développeurs à maintenir la documentation. Toute personne apportant une modification au code peut facilement ouvrir le fichier .MD dans son éditeur de code source ou un éditeur markdown en ligne, et mettre immédiatement à jour la documentation.

Ainsi, les fichiers Markdown sous contrôle de source vivent à côté, mais pas dans, le code qu'ils supportent. C'est aussi un peu plus « zoomer » que les commentaires en ligne. Ces deux facteurs entraînent une vitesse de mise à jour plus faible pour cette documentation. Parce que vous pouvez toujours l'inclure dans les mêmes commits, elle change avec une vitesse plus élevée que la documentation hors ligne.

Le dernier avantage de ce format est que toute personne qui télécharge le code source a un accès immédiat aux guides d'implémentation. Couplé avec la documentation en ligne, cela fournit aux mainteneurs et aux consommateurs une documentation suffisante. Ils peuvent développer une compréhension de base du projet sans sauter dans un autre système, comme un wiki.

#### Wiki : où les affaires rencontrent le développement

Nous utilisons la documentation de niveau wiki pour marier l'implémentation aux exigences commerciales. Cette documentation se compose principalement d'exigences, de diagrammes et de considérations d'architecture d'entreprise, et de diagrammes tactiques tels que des diagrammes de flux et de classes en langage de modélisation unifié (UML).

Nous utilisons également des pages (sur le même wiki) comme comptes rendus de réunion et pour enregistrer les décisions. Nous utilisons un wiki qui a un versionnage afin que nous puissions voir un historique complet de l'évolution des exigences et des conceptions au fil du temps.

Nous garantissons ainsi un historique complet du processus d'exigences et de sa relation avec l'architecture changeante. Accessoirement, GitHub propose également une fonctionnalité de wiki, mais nous utilisons un wiki tiers qui s'intègre à notre logiciel de gestion de projet.

#### Gestion des versions : commentaires de commit et de pull request

Notre processus de gestion des versions inclut la **révision de code**. Notre révision de code inclut la **révision de la documentation**.

Comme GitHub est notre plateforme de contrôle de source, nous intégrons la révision de code dans nos pull requests. La plateforme supporte les commentaires lors de l'enregistrement, les fils de commentaires en ligne sur des portions de commits, et un fil de conversation sur la pull request.

La clé pour utiliser ces canaux de communication avec succès est de s'assurer que toutes les discussions aboutissent à un résultat tangible. Soit clarifiez le code lui-même, soit étendez la documentation permanente en réponse aux questions.

Si le réviseur ne comprend pas le code tel qu'il est écrit, les futurs développeurs ne le comprendront pas non plus. Réécrivez le code pour qu'il soit plus auto-explicatif, ou étendez la documentation en ligne ou readme.

Il n'est pas suffisant de terminer la conversation en répondant au fil de discussion : nous traitons cette documentation comme éphémère, et sur une base de code à longue durée de vie, il est pénible de revoir l'historique complet des commits.

#### Tour bonus : le code auto-documenté

Enfin, une rapide promotion pour le soi-disant « code auto-documenté ». Je suis un fervent croyant que le code devrait être auto-explicatif à la surface. La documentation explicite devrait fournir du contexte ou améliorer la maintenabilité.

Il existe déjà de bons articles à ce sujet, donc je ne vais pas entrer dans les détails ici.

### Réflexions finales

J'espère que vous apprendrez de notre expérience. Notre architecture de documentation en quatre couches peut ne pas fonctionner pour vous, mais il est important de trouver ce qui fonctionnera.

Les grands enseignements ? Premièrement, il est nécessaire de développer une compréhension saine de vous-même et de vos propres besoins avant de vous engager avec une nouvelle base de code.

Deuxièmement, il est plus facile de rester hors d'une mauvaise relation avec le code hérité que de vous en extraire une fois que vous êtes déjà engagé.

Et troisièmement, vous ne laissez qu'un seul héritage. Mais chaque commit que vous faites contribue à celui-ci. Ils ne seront pas tous bons, ils ne seront pas tous mauvais, mais ils devraient au moins être clairs. Veuillez penser à ce que vous laissez pour ceux qui viennent après vous.

Ensemble, nous pouvons récupérer notre héritage en tant que développeurs.

Si vous avez aimé cet article et que vous en voulez plus comme celui-ci, veuillez ? pour montrer votre soutien !

Jonathan est le directeur adjoint de l'architecture et des opérations au département des systèmes d'information de recherche de l'UCLA. Il a obtenu un diplôme en physique de l'Université de Stanford et a depuis passé plus de 10 ans à travailler dans l'architecture des systèmes d'information, l'amélioration des processus commerciaux basés sur les données et la gestion organisationnelle. Il est également le fondateur de [Peach Pie Apps Workshop](http://www.peachpieapps.com), une entreprise qui se concentre sur la construction de solutions de données et de formation pour les organisations à but non lucratif.