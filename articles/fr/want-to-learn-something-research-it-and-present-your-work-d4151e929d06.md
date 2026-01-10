---
title: Vous voulez apprendre quelque chose ? Faites des recherches et présentez votre
  travail.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-24T02:14:45.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-something-research-it-and-present-your-work-d4151e929d06
coverImage: https://cdn-media-1.freecodecamp.org/images/1*37cCD5B_EJ7247jSVy_mzA.jpeg
tags:
- name: learning
  slug: learning
- name: life
  slug: life
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Vous voulez apprendre quelque chose ? Faites des recherches et présentez
  votre travail.
seo_desc: 'By Josh Bowen

  When I’m learning about something, I eventually hit a plateau. It’s hard to fight
  past this feeling. I’ve found that researching and then presenting that research
  helps me get unstuck.

  You don’t have to be a student or professor to do t...'
---

Par Josh Bowen

Quand j'apprends quelque chose, je finis par atteindre un plateau. Il est difficile de surmonter ce sentiment. J'ai découvert que faire des recherches et ensuite présenter ces recherches m'aide à me débloquer.

Vous n'avez pas besoin d'être étudiant ou professeur pour faire cela. J'encourage tout le monde à essayer. Tout comme poster votre code sur GitHub contribue à l'open source, présenter (et publier) vos recherches contribue au corpus de connaissances scientifiques.

### Création d'un projet

J'ai commencé ce projet en janvier 2017 pour en apprendre davantage sur le machine learning et la cybersécurité. Ce sont deux sujets que j'ai lus mais que je n'ai jamais appliqués. Comme je ne connaissais pas l'état actuel de la recherche dans ces domaines, j'ai décidé de m'attaquer à un problème de cybersécurité.

Après un peu de tri, j'ai trouvé [un rapport gouvernemental de 2009](https://www.dhs.gov/sites/default/files/publications/CSD-DHS-Cybersecurity-Roadmap.pdf). Il décrivait les problèmes actuels et les domaines nécessitant plus de recherche. J'ai été attiré par la section sur les menaces internes, alors j'ai décidé d'appliquer le machine learning aux menaces internes.

Je me suis dit — À quel point cela peut-il être difficile ?

J'étais enthousiaste à propos du projet, mais je n'avais pas encore lu d'articles dans ce domaine. J'ai commencé à réfléchir à des moyens d'évaluer comment une personne moyenne utilise un ordinateur par rapport à un initié avec des intentions malveillantes. Comme mon ordinateur portable fonctionne sous Ubuntu et que je suis souvent dans le terminal, l'idée d'examiner les commandes m'est venue à l'esprit.

J'ai décidé de capturer les commandes au fur et à mesure qu'elles se produisent, de faire des évaluations et d'essayer d'arrêter les commandes malveillantes et erronées dans leur élan. Je ne savais pas dans quoi je m'embarquais. J'ai écrit un résumé (disponible [ici](https://gist.github.com/Skraelingjar/39092ccb8eca4c9df3c56b1e392cb5d6)) et je me suis mis au travail.

### La Recherche

Un mois plus tard, j'avais fait quelques recherches préliminaires (minimales). J'ai ensuite soumis mon résumé à l'AZ/NV Academy of Science. Comme ils l'ont accepté, j'avais l'impression d'être sur la bonne voie.

Je n'étais pas pressé de terminer quoi que ce soit. J'avais des mois devant moi avant de présenter ! C'était une mauvaise mentalité. Au moment où mon poster a été accepté, je n'avais plus que cinq semaines pour me préparer. J'ai couru pour rassembler un corpus de recherche raisonnable sur lequel construire.

À ma grande surprise, j'ai trouvé plusieurs articles qui ont tenté de résoudre ce problème. En fait, quelqu'un a essayé la même approche que j'ai choisie en 1999 et leur recherche a été prouvée inefficace quelques années plus tard ! Comment pouvais-je continuer ?

J'ai continué à lire la [pile d'articles](https://github.com/Skraelingjar/cyberml/blob/master/bibliography.txt) que j'avais accumulée. Puis il m'est venu à l'esprit que personne n'appliquait réellement ces concepts à une situation de la vie réelle. Là était mon différenciateur : une application pratique.

### Les Données

Avant de pouvoir commencer à écrire du code, j'avais besoin de données pour mon modèle de machine learning. J'avais environ 60 000 commandes dans mon propre fichier .zsh_history, mais ce n'était pas suffisant. Il ne contenait pas non plus beaucoup d'erreurs et il n'y avait aucun comportement malveillant.

J'ai décidé de solliciter des entreprises pour leurs logs — peut-être que je pourrais en obtenir assez. Puis il m'est venu à l'esprit de vérifier si quelqu'un avait déjà collecté des bases de données de commandes.

Il s'avère que l'Université Purdue a collecté un grand [ensemble de données de commandes UNIX](https://archive.ics.uci.edu/ml/datasets/UNIX+User+Data) sur quelques années. Et l'Université de Californie, Irvine l'a sauvegardé. J'étais en affaires.

Mon fichier d'historique et les données UNIX contenaient des bits inutiles dont je devais me débarrasser. J'ai donc écrit un peu de Python pour m'en occuper parce que je ne voulais pas passer en revue 100 000+ lignes à la main. Premier à l'ordre du jour : mon fichier d'historique. Pas trop difficile.

```
# Exemples de ce que je traite : 1474850643:0;ls: 1474851038:0;cd# Examiner chaque ligne et écrire dans la sortiepour ligne dans fichier :    avant, sep, après = line.rpartition(";")    output.write(after.rstrip())
```

La partie difficile était de gérer les données de Purdue. Elles étaient remplies de choses comme EOF, SOF, des représentations d'arguments, de drapeaux et de pipes qui étaient tous sur des lignes séparées.

Je devais comprendre comment ces éléments s'assemblaient pour ne pas nourrir mon modèle avec du charabia. J'ai conçu un enchevêtrement désordonné d'instructions `if` imbriquées de près de 50 lignes de long.

Je n'ai jamais été à la fois aussi excité et déçu par du code que j'ai écrit. Il est difficile d'être fier d'un tel désordre. Mais j'ai passé tant d'heures dessus que j'étais soulagé d'avoir quelque chose qui fonctionnait.

Les deux programmes ont tout sauvegardé dans un format CSV pour un téléchargement facile vers le service S3 d'Amazon. De là, il est importé dans le modèle de machine learning et évalué.

### Le Logiciel

Maintenant que j'avais traité les données, je pouvais enfin commencer à écrire le programme de démonstration. À quel point cela pouvait-il être difficile ?

Il me restait moins de trois semaines. Il était assez facile d'envoyer et de recevoir des données de l'API de machine learning d'Amazon. Faire des évaluations basées sur ces réponses n'était pas trop difficile non plus. Je savais même comment je gérerais les commandes malveillantes et erronées.

Mais je ne savais rien sur la capture de ce que l'utilisateur tapait avant que la commande ne soit exécutée. J'ai lu la documentation Python et essayé les exemples. J'ai fouillé l'internet, et même regardé dans les e-books Linux que j'avais obtenus dans un Humble Bundle. Rien. J'ai passé presque la moitié de mon temps à suivre une voie menant à [nulle part](https://github.com/Skraelingjar/cyberml/blob/master/demo/readr.py).

J'ai finalement abandonné et [posté sur Stack Overflow](https://stackoverflow.com/questions/42916636/how-do-i-read-user-commands-in-bash-on-the-fly-with-python/42916902#42916902) à la recherche d'un guru pour me guider dans la bonne direction. Je suis reconnaissant qu'Ian ait répondu. Même si ce n'était pas la réponse que je cherchais, c'était la réponse dont j'avais besoin :

> _D'accord, cela semble vraiment utile. Alors pourquoi ne pas faire quelque chose comme while(input=raw_input("user: ")): #Code ML si c'est tout bon: subprocess(input.split()) else: #fermer le tout_

> _Ian Harvey — 21 mars à 4:30_

Il me restait un peu plus d'une semaine. Je me suis lancé et j'ai écrit un programme simple qui crée une fausse invite, lit l'entrée et évalue la commande. Vous pouvez trouver le programme complet [ici](https://github.com/Skraelingjar/cyberml/blob/master/demo/demo.py).

Il y avait un gros problème avec ce programme. Même si j'ai passé `KeyboardInterrupt` et `SystemExit`, `Ctrl + C` permettait à n'importe qui de contourner le programme.

L'autre gros problème était que de nombreuses commandes ne fonctionnaient pas, comme `cd`. C'était mauvais à un point risible, mais je l'ai installé sur un Raspberry Pi et j'ai invité quelques hackers à l'essayer. Inutile de dire que mon programme n'a pas duré longtemps.

### Le Poster

Saviez-vous que la norme pour la conception de posters académiques est Power Point ? Je n'arrivais pas à le croire. Malheureusement, il n'y a pas d'alternative. Celui qui construira [Prezi](https://prezi.com/) pour les posters académiques peut avoir mon argent.

J'ai fini par trouver un [beau poster SVG](http://blog.felixbreuer.net/2010/10/24/poster.html) utilisé pour la recherche en mathématiques et je l'ai converti pour mon projet. Au début, c'était brillant. Je suis habitué à Inkscape, et je n'aurais pas à m'inquiéter de l'échelle lorsque je redimensionnais les choses. L'inconvénient était que je devais supprimer tous les symboles mathématiques un par un.

Écrire le contenu du poster était un défi. J'ai eu du mal à mettre mes pensées en mots. Cela a mal tourné dans mes premiers brouillons. Je ne me suis pas non plus rendu compte à quel point je devais agrandir la police pour qu'elle soit lisible à quelques mètres de distance.

J'avais besoin de quelque chose pour distinguer mon poster. J'ai pensé à expliquer les menaces internes ou le machine learning comme concepts. Finalement, j'ai opté pour une tentative d'explication du logiciel de démonstration afin que tout le monde puisse comprendre. J'ai écrit des titres simples et utilisé quelques icônes Font Awesome pour démontrer le point.

Par la suite, j'ai réalisé qu'il y avait encore trop d'espace vide. J'ai ajouté des extraits de code pour chaque section. Ce n'est que plus tard que j'ai réalisé que cela pourrait aider à démystifier le code pour mon public. Ils étaient principalement des étudiants et des professeurs en sciences — mais pas en informatique.

### La Présentation

J'étais nerveux à l'idée de présenter mon poster. Je craignais que les gens posent des questions complexes sur le machine learning. Ou qu'ils me jugent parce qu'il s'est avéré que ce projet était "sans succès".

Je me trompais. Toutes les personnes avec qui j'ai parlé étaient intéressées et comprenaient les échecs du projet. Certains ont même trouvé que le design était agréable. Personne n'a posé les questions techniques complexes que je redoutais.

Mais j'aurais dû m'entraîner d'abord — je n'avais pas une présentation concise de cinq minutes prête à l'emploi.

### Réflexions Finales

Alors, qu'ai-je appris de ce projet ? **Nous avons besoin de plus de données ouvertes.** Le modèle de machine learning était biaisé parce que la majorité des données que je possédais tombaient dans la catégorie normale. Les entreprises devraient publier des logs nettoyés après une faille. Ces données pourraient alors aider à développer des modèles capables d'arrêter efficacement des attaques similaires.

Cette approche ne fonctionnera vraiment pas tant que je n'aurai pas trouvé un moyen de lire les commandes au fur et à mesure que l'utilisateur les entre, tout en permettant au terminal de fonctionner normalement. Je devrai prendre en compte les commandes personnalisées, les alias et ce qui constitue le comportement "normal" de quelqu'un. Ajouter des variables telles que la vitesse de frappe et les données d'accès pourrait également aider.

Je prévois de continuer à travailler sur [ce projet](https://github.com/skraelingjar/cyberml) parce que je crois qu'il peut être viable.

**Je vous encourage tous à poursuivre vos idées, à entreprendre des projets pour apprendre de nouvelles choses et à ne jamais abandonner.**

Si vous avez aimé cet article, donnez-moi quelques applaudissements pour que plus de gens le voient. J'écris sur le machine learning, la cybersécurité, l'IoT et l'apprentissage de la programmation. Retrouvez-moi sur [twitter](http://twitter.com/_josh) ou sur mon [site web](http://joshuabowen.info).