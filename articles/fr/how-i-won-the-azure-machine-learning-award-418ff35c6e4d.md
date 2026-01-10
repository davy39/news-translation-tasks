---
title: Comment j'ai construit un jeu qui a remporté le prix Azure Machine Learning
  2016
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-17T20:02:56.000Z'
originalURL: https://freecodecamp.org/news/how-i-won-the-azure-machine-learning-award-418ff35c6e4d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JQcCZ8tOoE-MztriV1QKTg.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: learning
  slug: learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit un jeu qui a remporté le prix Azure Machine Learning
  2016
seo_desc: 'By Déborah Mesquita

  Every year, Microsoft hosts the Imagine Cup. Young developers often call it the
  “Olympics of Technology” and consider it one of the top competitions related to
  software design. As a result, it attracts lots of young participants f...'
---

Par Déborah Mesquita

Chaque année, Microsoft organise la [Imagine Cup](https://compete.imagine.microsoft.com/pt-br/category/0?skillLevel=0). Les jeunes développeurs l'appellent souvent les "[Jeux Olympiques de la Technologie](https://en.wikipedia.org/wiki/Imagine_Cup)" et la considèrent comme l'une des principales compétitions liées à la conception de logiciels. En conséquence, elle attire de nombreux jeunes participants du monde entier, qui collaborent pour résoudre certains des défis les plus difficiles du monde.

En 2016, ils ont organisé le [Hello Cloud Machine Learning Award](https://compete.imagine.microsoft.com/pt-br/competition/17554), où les gagnants ont été sélectionnés parmi toutes les candidatures en fonction de la qualité, de la créativité et de l'efficacité de leur utilisation d'Azure Machine Learning Studio.

Je me suis lancée dans la compétition pour en apprendre davantage sur le machine learning et j'ai fini par être l'une des gagnantes du défi. Ce qui m'a intéressée en premier lieu, c'était l'objectif de la compétition : **construire des systèmes créatifs et inventifs utilisant le machine learning**.

Lorsque qu'un utilisateur cesse d'utiliser un bien ou un service (dans ce cas, un jeu), nous appelons cela le "churn". Sur la base de l'historique des joueurs ou des données de joueurs similaires au fil du temps, nous pouvons créer un modèle de machine learning pour prédire quand un joueur est le plus susceptible d'abandonner.

Dans la première partie de la compétition, nous devions construire, entraîner, évaluer et noter un modèle pour faire exactement cela dans Azure ML Studio. Ensuite, nous devions prendre un jeu de base fourni par eux, le connecter au service Azure ML et le publier sur le web.

![Image](https://cdn-media-1.freecodecamp.org/images/yUfCcScpLhgfjRihX7SrPf4fzVPjmY94VAob)
_Ce fut mon premier Game Design Document (plus là-dessus plus tard)_

L'un des facteurs clés qui fait qu'un joueur abandonne un jeu est son niveau de difficulté. S'il est trop facile, le jeu devient ennuyeux, et s'il est trop difficile, il démotive l'utilisateur de continuer à jouer.

J'ai décidé d'utiliser la dynamique pierre-papier-ciseaux dans le jeu. Pour gagner de nouveaux superpouvoirs dans le jeu, les joueurs (des étudiants en mathématiques) devaient résoudre des équations mathématiques (utilisées comme des attaques dans un jeu de combat).

Sur la base des données de chaque joueur, nous pouvions ajuster la difficulté des équations mathématiques pour les motiver à continuer à jouer. Nous pouvions également identifier quel type d'équations posait le plus de problèmes aux enfants (soustraction ? multiplication ?). C'est une opportunité incroyable d'aider les enseignants et tous ceux qui sont impliqués dans le processus d'apprentissage.

#### Principe 1 : Se concentrer sur le fait d'être différent

Une chose que je sais avec certitude dans les compétitions est la suivante : **concentrez-vous sur le fait d'être différent au lieu de vous concentrer uniquement sur le fait d'être meilleur**. Nous ne connaissons pas le nombre exact de concurrents, mais selon ce que nous avons entendu à Seattle, le concours comptait près de 1 000 candidatures. C'est beaucoup de jeux à évaluer pour les juges. Vous devez faire tout ce que vous pouvez pour vous démarquer dans une foule de cette taille.

Je parie que lorsque vous lisez le mot "différent", votre première pensée a été "Super, maintenant je dois inventer quelque chose de grand et d'étrange de nulle part." Ne vous inquiétez pas, ce n'est pas le cas. Parce qu'il y a une autre chose que je sais avec certitude : **pour être différent, vous pouvez simplement vous concentrer sur le fait d'être vous-même**. Je sais que cela semble cliché, mais élaborons sur ce point.

> "Soyez vous-même ; tout le monde est déjà pris." – [**Oscar Wilde**](https://www.goodreads.com/author/show/3565.Oscar_Wilde)

Vous êtes vous, n'est-ce pas ? Personne d'autre dans le monde n'a eu les expériences que vous avez eues, n'a fait tout ce que vous avez fait ou n'a ressenti exactement tout ce que vous avez ressenti. C'est tout, vous devez simplement utiliser _cela_ pour être différent (et original). Revenons maintenant à ce que j'ai fait dans le concours.

J'ai acheté ma première tablette Wacom à temps pour la compétition, et honnêtement, je cherchais simplement des excuses pour l'utiliser. J'aime m'aventurer dans d'autres domaines, et je sais que c'est quelque chose qui me différencie. J'ai donc décidé de travailler et de changer les assets du jeu.

![Image](https://cdn-media-1.freecodecamp.org/images/ckRicVJo9uAxb8ay1LeQcMPGnkgT8-8cnkf4)
_L'asset qu'ils nous ont donné et l'asset que j'ai créé (hé, je ne suis pas illustratrice, ok, prenez-le facilement)_

#### Principe 2 : Commencez par ce que vous connaissez

Dans la compétition, nous devions d'abord suivre un tutoriel. Ce n'est qu'après cela que nous pouvions commencer à créer notre propre version du jeu. C'est une excellente façon de concevoir le flux de travail de nos projets (et projets secondaires) : **trouvez toujours un moyen de rendre la phase de démarrage facile**.

J'ai entendu ce conseil pour la première fois dans le livre [Think Like a Programmer](https://www.nostarch.com/thinklikeaprogrammer). C'est vrai pour la programmation, mais c'est aussi vrai pour de nombreux autres aspects de notre vie.

> Une fois que vous avez divisé le problème en morceaux, par exemple, allez-y et complétez tous les morceaux que vous savez déjà comment coder. Avoir une solution partielle fonctionnelle peut donner des idées sur le reste du problème. De plus, comme vous l'avez peut-être remarqué, **un thème commun dans la résolution de problèmes est de faire des progrès utiles pour construire la confiance que vous accomplirez finalement la tâche**. En commençant par ce que vous connaissez, **vous construisez la confiance et l'élan vers l'objectif**. – [V](https://www.goodreads.com/author/show/3565.Oscar_Wilde). Anton Spraul, [Think Like a Programmer](https://www.nostarch.com/thinklikeaprogrammer)

Soyons honnêtes : la programmation est difficile. Pendant la compétition, j'ai eu quelques moments de frustration, mais des choses comme voir mon premier modèle prédictif fonctionner et voir les pièces du jeu commencer à fonctionner ensemble m'ont motivée. Assurez-vous de pouvoir commencer à voir des progrès dans un projet, dès le début.

#### Principe 3 : S'adapter

C'était le facteur clé pour gagner la compétition, car sans cela, ma candidature n'aurait même pas été soumise. **Le temps est une ressource limitée**. Tout le monde le sait, mais c'est quelque chose que nous devons toujours nous rappeler – surtout nous, les programmeurs.

Si vous jetez un coup d'œil à mon Game Design Document ci-dessus, vous pouvez voir que mon idée initiale pour le jeu comportait de nombreuses fonctionnalités. Par exemple, nous avions des niveaux pour les joueurs, des objets qu'ils pourraient collecter, des effets de guérison, et ainsi de suite. À l'approche de la date limite, j'ai réalisé que je n'avais pas le temps de réaliser toutes ces idées. J'ai donc dû réfléchir : quelle est la seule chose que je devrais avoir dans le jeu pour m'assurer qu'il atteindrait mon objectif ? La réponse était les équations mathématiques et la dynamique pierre-papier-ciseaux, et c'est ce que j'ai implémenté.

Il n'est pas facile de donner des instructions sur la façon de s'adapter, car chaque situation est différente. Mais vous devez savoir que vous devrez **faire des choix** en cours de route. Votre objectif principal devrait être de terminer le projet à temps, afin de pouvoir effectivement participer au concours.

Eh bien, comme vous le savez peut-être maintenant, mon projet a été l'un des deux gagnants du défi (youpi !). J'ai gagné un voyage pour la finale mondiale de l'Imagine Cup et j'ai eu des séances de mentorat avec des membres de la plateforme de données Microsoft.

Avec ce projet, j'ai enfin trouvé mon objectif de carrière principal : **concevoir des systèmes de Machine Learning qui permettent aux humains de faire ce qui les intéresse**.