---
title: J'ai fait ma première contribution open source en 200 jours (et comment vous
  pouvez faire de même)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-04T20:03:51.000Z'
originalURL: https://freecodecamp.org/news/i-made-my-first-open-source-contribution-within-200-days-and-how-you-can-too-4d5bdbd63fad
coverImage: https://cdn-media-1.freecodecamp.org/images/1*w9oin5BRCHMbv0nfqdkuow.jpeg
tags:
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: J'ai fait ma première contribution open source en 200 jours (et comment
  vous pouvez faire de même)
seo_desc: 'By JavaScript Joe

  On December 22nd, 2016, I created a freeCodeCamp account. On July 1st, 2017, I got
  my first-ever pull request merged into an open-source project.

  I wanted to write this article to share my experience with others. I hope it will
  show...'
---

Par JavaScript Joe

Le 22 décembre 2016, j'ai créé un compte freeCodeCamp. Le 1er juillet 2017, j'ai obtenu ma première pull request fusionnée dans un projet open source.

Je voulais écrire cet article pour partager mon expérience avec les autres. J'espère qu'il vous montrera que contribuer à des projets open source est plus facile que vous ne le pensez.

### Pourquoi devriez-vous contribuer à l'open source ?

Vous avez probablement entendu dire que contribuer à l'open source est une bonne utilisation de votre temps en tant que développeur. Mais au cas où vous n'êtes pas encore convaincu, voici deux raisons à considérer :

#### Raison #1 : Cela vous aidera à trouver un emploi

C'est l'une des principales raisons pour lesquelles j'ai décidé de contribuer à un projet open source. Quelques développeurs seniors de mon groupe d'anciens élèves de l'université m'ont dit que cela pourrait m'aider à paraître plus employable.

Lorsque vous réalisez un projet seul via freeCodeCamp, ou pour un cours, vous êtes le seul à devoir approuver le code. Avec un projet open source, des centaines de milliers de personnes peuvent utiliser le code que vous écrivez. Il y a donc une pression supplémentaire pour écrire un code propre et réutilisable.

De plus, cette communauté de développeurs doit l'accepter. Donc, lorsqu'ils acceptent votre code, cela a beaucoup de poids, en raison du nombre de personnes qui l'ont vu.

Je pense qu'il est sûr de dire que les contributions open source en disent beaucoup plus aux employeurs que la plupart des projets personnels.

#### Raison #2 : C'est donner en retour à la communauté

Contribuer à des projets open source vous donne l'opportunité de consacrer votre temps à améliorer un projet utilisé par vous et votre communauté. C'est probablement l'un des aspects les plus cool de la programmation.

Quelqu'un construit un projet, puis il l'open source afin que le public puisse voir le code source. Ensuite, un groupe de personnes qui ne se connaissent pas contribuent au code. Et cela peut améliorer la vie des gens du monde entier. Peu de choses dans notre monde peuvent être comparées à cela.

### À quoi ressemblait le processus de contribution à l'open source ?

Vous vous demandez probablement comment je m'y suis pris. Tout d'abord, j'ai vérifié les applications et les sites web que j'utilisais régulièrement pour voir si certains étaient open source.

Ensuite, j'ai demandé à quelques-uns de mes amis codeurs proches (que j'ai rencontrés dans ma première [cohorte Chingu](https://tropicalchancer.github.io/projectus/) ;)) et nous avons tous convenu de relever le défi ensemble.

Nous avons choisi [Habitica](https://habitica.com/), un gestionnaire de tâches gamifié.

Nous l'avons choisi pour les raisons suivantes :

* Nous l'utilisons tous les jours
* Leur [wiki pour contribuer](http://habitica.wikia.com/wiki/Guidance_for_Blacksmiths) est bien écrit
* Ils encouragent les débutants à contribuer
* Leur base de code est principalement composée de JavaScript
* Ils ont un groupe où vous pouvez poser des questions et obtenir de l'aide lorsque vous êtes bloqué

Ensuite, nous avons discuté de ce que nous pensions être la meilleure façon de procéder.

Voici le plan d'action étape par étape que nous avons utilisé :

#### Étape #1 : Trouver un "mentor" — quelqu'un dans la communauté qui pourrait nous aider si nous étions perdus

Heureusement pour nous, Habitica a une guilde géniale pour les codeurs appelée "Aspiring Blacksmiths (Coding for Habitica)". Nous avons posté dans le groupe, et un membre a accepté de nous fournir quelques conseils.

#### Étape #2 : Trouver un problème adapté à notre niveau de compétence

Ensuite, nous avons regardé les problèmes sur le [dépôt Github de Habitica](https://github.com/HabitRPG/habitica/issues) et avons trouvé ceux étiquetés "medium-level coding". Nous avons choisi quatre options, puis avons demandé à notre mentor laquelle conviendrait le mieux pour notre première contribution. Après en avoir discuté au sein de notre groupe, nous avons choisi [celui-ci](https://github.com/HabitRPG/habitica/issues/8677#event-1146999223).

![Image](https://cdn-media-1.freecodecamp.org/images/-Zg72WsSWiHmd28rHb6p8VNAORx5fjUT3ZI8)

#### Étape #3 : Travailler dessus seul, mais aussi lors de sessions de pair-programming

Le problème a pris deux semaines, soit environ 14 à 18 heures pour être résolu. Nous y travaillons généralement entre 1 et 4 heures par jour. Nous avons passé la majorité de ce temps à déterminer quels fichiers nous devions modifier.

Nous avons passé des heures à parcourir le dossier du projet. Nous avons recherché différents termes comme "group" et "group approvals" jusqu'à ce que nous puissions localiser les lignes de code que nous devions corriger.

Après avoir trouvé les fichiers, nous avons été confrontés à un nouveau défi. Nous devions déterminer comment prendre des données de la base de données et pouvoir les appeler dans le fichier JSON pour les afficher sur la page "Group Plans Task Approval".

Nous avons examiné les objets dans la base de données et avons trouvé une paire clé-valeur de type de tâche avec les informations dont nous avions besoin. Ensuite, nous devions l'ajouter à un objet en tant que propriété sur un objet dans un fichier appelé `groupApprovalsController.js`. De cette façon, nous pouvions y faire référence dans le fichier JSON. Nous avons pu comprendre tout cela grâce à notre expérience avec JavaScript sur [freeCodeCamp](https://www.freecodecamp.org), le cours [Web Developer Bootcamp](https://www.udemy.com/the-web-developer-bootcamp/) de Colt Steele, et la lecture de [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS).

Le prochain défi auquel nous avons été confrontés était de pouvoir rendre le markdown et les emojis. Le projet utilise un package npm développé par l'un des principaux programmeurs du projet, donc les docs étaient faciles à suivre. Nous avons regardé les pages Jade similaires et reconnu des motifs dans la façon dont le markdown était rendu.

Une fois que nous avons connu la syntaxe pour le markdown et la page à laquelle nous devions l'ajouter. Nous pensions que le reste serait facile. Mais ce n'était pas le cas. Nous avons eu du mal à comprendre comment passer le texte spécifique dont nous avions besoin.

Après des heures de frustration et de nombreuses tentatives infructueuses, nous avons enfin compris. Nous devions passer un argument de "approval" dans une fonction appelée `approvalTitle` et définir le texte égal à cela. La ligne que nous avons finie par écrire était :

```
markdown(text = "approvalTitle(approval)")
```

Bien sûr, nous pensions avoir terminé... jusqu'à ce que nous remarquions que le nouveau code avait déplacé l'emplacement du bouton "Approve" sur la page.

![Image](https://cdn-media-1.freecodecamp.org/images/Ig76khuINvugUGKb4yBtEFW6a8V2-p8WPUHo)

Une solution a ouvert un nouveau problème, mais nous avons accepté le nouveau défi et persévéré. Après avoir fouillé, Rachel a pu trouver une solution Bootstrap qui l'a fait paraître un peu mieux.

![Image](https://cdn-media-1.freecodecamp.org/images/Hh4XU-6r1e4iQ6N6Znr373IAjFIII5Lid7Ub)

#### Étape #4 : Soumettre une Pull Request (PR) pour solliciter des commentaires

Notre correction n'était pas parfaite, mais elle résolvait la plupart des problèmes et n'avait que quelques problèmes de formatage mineurs. Nous avons demandé de l'aide dans la Guilde des Aspiring Blacksmiths. Ils nous ont conseillé de soumettre une pull request pour recevoir des commentaires. Nous en avons soumis une avec nos changements. Peu après, un autre développeur a fait quelques suggestions sur la façon de corriger le problème de formatage.

#### Étape #5 : Nettoyer le code et soumettre une PR finale

Après avoir nettoyé les commits et les avoir organisés de manière significative, nous avons soumis une PR finale.

#### Étape #6 : Célébrer après la fusion

Le samedi 1er juillet 2017, notre PR a été fusionnée et nous avons célébré.

![Image](https://cdn-media-1.freecodecamp.org/images/NZ4JxtCWvOKoqkaSn2RJBYyg58PrbSHeh78P)

### Qu'ai-je appris ?

Voici les principales choses que j'ai apprises de ma première contribution open source :

* Comment travailler sur du code écrit par d'autres personnes
* Comment travailler avec un autre développeur pour corriger un bug
* Comment soumettre une pull request
* Comment écrire des messages de commit significatifs
* Comment contribuer à un projet open source

Je suis reconnaissant pour tous les encouragements que nous avons reçus de la communauté Habitica. Et je suis heureux d'avoir pu travailler sur ce projet avec mon amie Rachel. Grâce à cette expérience, j'ai grandi en tant que développeur.

### Réflexions finales

Si vous êtes nouveau en programmation comme moi, je vous suggérerais de vous pencher sur la contribution à un projet open source. Cela peut sembler effrayant au début et certaines parties l'étaient définitivement. Cela signifie que vous allez dans la bonne direction.

Vous sortez de votre zone de confort et entrez en territoire inconnu. **C'est là que le vrai apprentissage se produit.** C'est là que vous serez mis au défi de manières que vous n'auriez pas pu imaginer.

Si vous avez contribué à un projet open source que vous pensez être bon pour les débutants, n'hésitez pas à commenter avec les noms ! :)

Merci d'avoir lu ! J'espère que vous avez trouvé cet article utile. Si c'est le cas, faites-le moi savoir en cliquant sur le ? ou en laissant un commentaire ci-dessous.