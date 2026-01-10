---
title: Comment utiliser le Dev Huddle pour aligner vos développeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-02T04:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-dev-huddle-to-get-your-developers-on-the-same-page
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/huddle.jpg
tags:
- name: agile
  slug: agile
- name: agile development
  slug: agile-development
seo_title: Comment utiliser le Dev Huddle pour aligner vos développeurs
seo_desc: 'By Mario Fernandez

  How do you make sure that the developers on your team are aligned with your technical
  direction? That’s a difficult question.

  Every team has its own idiosyncrasies. As a tech lead, I’ve thought a lot about
  it and ended up with vagu...'
---

Par Mario Fernandez

Comment vous assurer que les développeurs de votre équipe sont alignés avec votre direction technique ? C'est une question difficile.

Chaque équipe a ses propres idiosyncrasies. En tant que [tech lead](https://www.patkua.com/blog/the-definition-of-a-tech-lead/), j'ai beaucoup réfléchi à ce sujet et j'ai fini avec des idées vagues comme l'_autonomisation_ ou les _objectifs partagés_. Mais celles-ci ne sont pas très actionnables.

Cependant, un rituel a très bien fonctionné dans les équipes dont j'ai fait partie. Je veux parler du _dev huddle_.

## Qu'est-ce qu'un dev huddle ?

![Alignement](https://www.freecodecamp.org/news/content/images/2020/09/developers-aligning.jpg)
_Les développeurs alignent les attentes_

Il existe de nombreux noms pour cela : Dev Huddle, Tech Huddle, Dev Meeting. Peu importe comment vous l'appelez, c'est une réunion récurrente pour les développeurs d'une équipe.

Alors, qu'est-ce que cela accomplit ? Eh bien, c'est un forum pour discuter de sujets techniques et prendre des décisions concernant l'architecture, les conventions ou tout autre aspect de la pile technologique.

"Wow, c'est _si_ innovant !" pourriez-vous penser. Oui, ce n'est rien de révolutionnaire. Le diable est dans les détails, cependant.

Animer un dev huddle efficace peut être délicat. Rien ne frustrera davantage un groupe de développeurs que d'avoir encore une autre réunion inutile. Si vous prenez leur temps, vous feriez mieux de le rendre utile.

## Pourquoi devrais-je le faire ?

Avant de se concentrer sur le _comment_, examinons d'abord le _pourquoi_. Que cherchons-nous à accomplir ?

### Créer l'alignement

Les développeurs peuvent travailler en étroite collaboration (parfois _trop_ littéralement), mais construire un logiciel comme s'ils ne s'étaient jamais rencontrés auparavant. Sont-ils d'accord sur les conventions de codage ? Quelle est la bibliothèque préférée pour analyser le JSON ?

Il y a des tonnes de petites décisions à prendre. Avec le temps, celles-ci forment une compréhension cohésive de la construction de logiciels qui est cruciale pour toute équipe performante.

### Favoriser l'innovation

Vous ne réécrirez pas votre application tous les six mois avec la technologie la plus tendance, mais vous voulez encourager les expériences. Les [améliorations continues](https://www.creativesafetysupply.com/articles/continuous-improvement/) s'accumulent avec le temps.

J'ai fait partie d'équipes qui semblaient désespérées au début. Après un an de nombreuses petites améliorations, nous faisons du [déploiement continu](https://www.atlassian.com/continuous-delivery/continuous-deployment#:~:text=Continuous%20Deployment%20(CD)%20is%20a,cycle%20has%20evolved%20over%20time). Cela arrive rarement en une seule grande poussée, cependant.

### Encourager le débat

Certaines équipes pratiquent ce que j'appelle la _discussion par ancienneté_, où les personnes les plus expérimentées de l'équipe prennent les décisions technologiques, et les autres, eh bien, les suivent. Si elles ont la chance de découvrir ces décisions, bien sûr.

Vos collègues expérimentés ont l'expérience et les instincts, mais tout le monde peut contribuer également.

## Préparation

J'aime structurer les huddles autour d'un backlog d'idées.

Quelque chose d'aussi simple qu'un post-it sur le mur ou une liste de problèmes sur Github fonctionne. Chacun peut être simplement un titre simple - ils sont là pour commencer une conversation.

Quelques exemples :

* Essayons [strikt](https://strikt.io/), une nouvelle bibliothèque d'assertions
* Refactorisons nos appels API pour utiliser [React hooks](https://reactjs.org/docs/hooks-intro.html)
* Documentation manquante pour notre dernier microservice

![Tableau de huddle](https://www.freecodecamp.org/news/content/images/2020/09/huddle-board.png)

Qui ajoute de nouveaux sujets ? Tout le monde !

Trouvez un candidat pour le refactoring en pairant ? Lisez cet article [dev.to](https://dev.to/) sur cette nouvelle bibliothèque ?

Ajoutez-le simplement au mur.

Au début, vous serez le seul à poster des idées. Avec le temps, le reste de l'équipe se sentira plus à l'aise et contribuera. Nous verrons comment choisir de quoi parler dans un instant.

### Trouver un moment

Certains pourraient dire : "Réunissons-nous simplement quand c'est nécessaire. Nous sommes agiles !"

Selon mon expérience, cela ne fonctionne pas. Il y a toujours quelque chose d'urgent, ou quelqu'un n'a pas le temps maintenant.

Mon conseil ? Choisissez un créneau fixe : même jour et même heure, chaque semaine.

Idéalement, quand c'est le moins perturbant. Après le daily, juste après le déjeuner - cela n'a pas vraiment d'importance. Les gens s'y habitueront et en tiendront compte dans leur emploi du temps.

Une demi-heure devrait suffire pour avoir des conversations significatives.

Le flux du tableau est un bon indicateur. Si vous collectez de plus en plus de sujets dont vous ne parlez jamais, peut-être que vos dev huddles doivent être un peu plus longs. Si vous manquez de sujets, peut-être pouvez-vous finir plus tôt, ou même passer à des huddles bihebdomadaires.

## Comment animer un dev huddle

Animer un dev huddle consiste à parcourir la liste des sujets, à les discuter, à parvenir à une conclusion et à la documenter. Cela semble facile, n'est-ce pas ?

![Modérateur](https://www.freecodecamp.org/news/content/images/2020/09/moderator.jpg)
_Modération en cours_

Pas si vite. Tout d'abord, il **doit** y avoir un facilitateur.

Un bon facilitateur suit le temps total, en s'assurant qu'aucun sujet ne consomme tout le créneau horaire. Ils donnent également à chacun une chance de parler.

Sans ce rôle, vous pourriez finir par avoir une discussion de pub, mais sans la bière.

Je dirigeais toutes les huddles dans une équipe précédente. Je n'ai réalisé que beaucoup plus tard quelle erreur c'était.

Les réunions finissent par devenir les vôtres alors qu'elles devraient appartenir à toute l'équipe. Il est difficile de faciliter et d'être un participant actif en même temps.

Faites tourner la facilitation à la place. Tout le monde s'entraîne à modérer, et vous avez aussi droit à une partie du plaisir !

Si vous avez trop de sujets, vous devez choisir ceux à aborder. Vous pouvez les prendre dans l'ordre de création, ou faire un [vote par points](https://en.wikipedia.org/wiki/Dot-voting) juste avant de commencer.

Certaines personnes apporteront plus de points que d'autres. Essayez de garder l'équilibre. Un grand changement architectural nécessite plus que quelques minutes, donc peut-être qu'une réunion de suivi est nécessaire.

Et puis, la discussion s'ensuit.

Un huddle ne réparera pas une culture brisée, mais c'est un bon test. Énoncez-vous des opinions ou des faits ? Vous battez-vous pour placer un mot ? Si c'est le cas, un huddle est le moindre de vos problèmes.

Voici une liste de contrôle échantillon pour aider les modérateurs moins expérimentés :

```text
- Y a-t-il des points ouverts de la dernière fois ?
- Choisir les sujets pour aujourd'hui
* Pour chaque sujet
    
    Le propriétaire présente le problème afin que tout le monde soit sur la même page
    Parlez-en (Gardez un timebox !)
    Résolution
        Qu'avons-nous décidé ?
        Assigner un propriétaire pour s'occuper du suivi
  
- Avons-nous pris des décisions qui doivent être reflétées dans les ADR ?
- Terminer à l'heure, sauf s'il y a quelque chose qui ne peut absolument pas attendre
```

## Le résultat

Faire parler l'équipe entre eux est déjà _quelque chose_. Si aucun résultat n'en sort, ce n'est pas vraiment une réunion mais une réunion sociale.

Alors, notez vos conclusions. Typiquement, il s'agira de choses que vous voulez faire ou de choses que vous ferez à partir de ce moment-là.

### Histoires techniques / Éléments Slack

N'écoutez pas les [micromanagers aux cheveux pointus](https://en.wikipedia.org/wiki/Pointy-haired_Boss) qui veulent enregistrer chaque action entreprise, peu importe à quel point elle est insignifiante. Pour les petites choses, gardez la comptabilité à un minimum et comptez sur le [temps de slack](https://www.solutionsiq.com/resource/blog-post/the-importance-of-slack-in-achieving-speed-and-quality/).

Pour les choses plus importantes, écrivez des histoires techniques et assurez-vous de les intégrer dans votre backlog régulier. Il y a beaucoup à dire [à ce sujet](https://www.thoughtworks.com/insights/blog/treat-devops-stories-user-stories).

TLDR : Tenez une histoire technique aux mêmes normes que les histoires utilisateur.

### Garder une trace des décisions

![Enregistrements de décisions](https://www.freecodecamp.org/news/content/images/2020/09/decision-records.jpg)
_Archivage des décisions_

Imaginez ceci : tout le monde est motivé pour le huddle. Cela devient intense, mais vous parvenez à un accord sur l'utilisation ou non de points-virgules. _Les choses avancent_. Mais personne ne l'écrit, et vous devez tout recommencer la semaine prochaine.

Infuriant, n'est-ce pas ?

Puis-je vous intéresser à quelques [enregistrements de décisions d'architecture légers](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records) ? Cela peut sembler formel et peu agile, mais ce n'est vraiment pas le cas. Vous avez simplement un endroit où vous gardez une trace des décisions que vous prenez.

Un fichier Markdown avec un titre, ce que vous décidez, et une explication du contexte est tout ce dont vous avez besoin. J'ai vu des gens écrire des romans pour vanter les mérites de Kafka alors qu'un simple document fonctionnerait tout aussi bien :

```text
Titre : Utiliser Kotlin au lieu de Java pour les nouveaux services

Date : 2018/10

Décision : Nous utiliserons Kotlin chaque fois que nous démarrerons un nouveau service, mais nous laisserons les services existants

Contexte : Nous pensons que Kotlin nous aidera à créer des services plus légers tout en améliorant la qualité grâce à la sécurité null
```

Il existe [de nombreux modèles](https://github.com/joelparkerhenderson/architecture_decision_record#adr-example-templates) que vous pouvez utiliser. L'important est d'être discipliné et de refléter ce sur quoi vous vous êtes mis d'accord.

## Commencez à vous réunir !

En regardant en arrière, toutes les équipes dont j'ai fait partie ont considérablement bénéficié d'avoir un lieu pour aligner les développeurs. Ce n'est qu'un petit investissement d'efforts et de temps.

Allez-y et essayez-le, puis trouvez la configuration qui fonctionne le mieux pour vous.