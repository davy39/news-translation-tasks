---
title: Comment démarrer un projet Open Source sur GitHub – Conseils pour construire
  mon dépôt en tendance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-14T17:09:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-an-open-source-project-on-github-tips-from-building-my-trending-repo
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/github-on-the-hunt-for-a-new-diversity-lead-developers-techworld-github-universe-png-800_450.png
tags:
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: projects
  slug: projects
seo_title: Comment démarrer un projet Open Source sur GitHub – Conseils pour construire
  mon dépôt en tendance
seo_desc: "By Rishit Dagli\nDevelopers around the world use GitHub to share their\
  \ projects with the global developer community. \nIn this article, I'll give you\
  \ some opinionated tips to help you build a great open-source project you can start\
  \ using. You can also ..."
---

Par Rishit Dagli

Les développeurs du monde entier utilisent GitHub pour partager leurs projets avec la communauté mondiale des développeurs. 

Dans cet article, je vais vous donner quelques conseils pour vous aider à construire un excellent projet open-source que vous pouvez commencer à utiliser. Vous pouvez également utiliser ces conseils pour construire des projets de hackathon.

Récemment, j'ai atterri sur la célèbre page GitHub Trending. J'étais le #2 développeur en tendance sur tout GitHub – et pour Python également, ce qui a été une agréable surprise pour moi le matin du 7 septembre. Et cela était basé sur du code que j'ai écrit à 4h du matin.

J'ai également été présenté dans la newsletter quotidienne de GitHub, après avoir open-sourcé l'un de mes projets. 

Je vais partager quelques conseils dans cet article que vous devriez pouvoir appliquer à tous types de projets et pas seulement aux packages Python comme le mien.

Vous pouvez consulter mon dépôt [ici](https://github.com/Rishit-dagli/Fast-Transformer).

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-27.png)
_Mon projet sur la page [GitHub Trending](https://github.com/trending/developers)_

## Trouvez votre motivation

Il est presque impossible de manipuler la section GitHub Trending :

> La définition de GitHub (des tendances) prend en compte une définition à plus long terme des tendances et utilise des mesures plus complexes que le simple nombre d'étoiles, ce qui aide à empêcher les gens de manipuler le système.

Les fondateurs créent souvent des startups basées sur des problèmes qu'ils ont personnellement rencontrés. Avec du code open-source, vous allez probablement essayer de résoudre des problèmes que **les développeurs rencontrent couramment**. 

Et puisque manipuler la section GitHub Trending est presque impossible, vous avez besoin d'une forte motivation – un grand problème courant des développeurs – sur lequel travailler. Alors, comment tomber sur un problème de développeur ?

Eh bien, pour commencer, vous pouvez participer à des hackathons, construire des projets et expérimenter avec d'autres projets. Et vous trouverez bientôt quelque chose qui pourrait être transformé en une bibliothèque, quelque chose dont vous pourriez faire un utilitaire, et ainsi de suite. 

Votre motivation pour construire votre projet peut venir de n'importe où. Dans mon cas, j'explore de nouveaux articles sur le Machine Learning quotidiennement sur arXiv (une archive en accès libre pour les articles) et je lis ceux que je trouve intéressants. Un tel article que j'ai lu m'a motivé à construire mon package Python.

Une autre fois, j'étais dans un hackathon en train d'entraîner un modèle de Machine Learning et je voulais participer à d'autres festivités. Notre équipe a alors décidé de construire un autre projet open-source appelé [TF-Watcher](https://www.freecodecamp.org/news/how-to-monitor-ml-projects-on-mobile-devices/). 

Vous voyez, vous trouverez probablement toutes sortes de problèmes sur lesquels travailler lorsque vous construisez un projet.

Et juste pour noter – lorsque je dis que vous devriez avoir une forte motivation, je ne veux pas dire que le projet devrait être vraiment énorme ou vraiment complexe. Il pourrait certainement s'agir d'un projet simple qui pourrait faciliter la vie des développeurs. 

Réfléchissez-y de cette manière : si un projet comme celui que vous voulez développer existait, **l'utiliseriez-vous** ? Si la réponse est oui, vous avez suffisamment de motivation pour construire le projet, quelle que soit sa taille ou sa complexité. 

> Un homme à Oakland, en Californie, a perturbé le développement web dans le monde entier la semaine dernière en supprimant 11 lignes de code. — Keith Collins dans [Comment un programmeur a cassé Internet en supprimant un petit morceau de code](https://qz.com/646467/how-one-programmer-broke-the-internet-by-deleting-a-tiny-piece-of-code/)

Vous connaissez peut-être `left-pad`, un très petit package npm open-source avec seulement 11 lignes de code simples. Mais il était utilisé par des tonnes de développeurs dans le monde, ce qui renforce ce dont je parlais ci-dessus.

## Recherchez votre idée

Une fois que vous avez trouvé un problème de développeur que vous voulez résoudre et que vous avez suffisamment de motivation pour commencer à travailler dessus, vous voudrez idéalement passer beaucoup de temps à faire vos recherches. 

Je crois qu'il est bon de tenter de répondre à ces questions à travers vos recherches :

### Un projet ou un outil similaire existe-t-il déjà ?

Si cela n'a pas encore été fait, et qu'il y a un besoin, allez-y et commencez à le construire.

Si quelque chose de similaire existe, est bien développé et est également largement utilisé, vous pourriez vouloir passer à autre chose. 

Il existe déjà un grand nombre de projets open-source, et il est assez courant de trouver un dépôt faisant des choses similaires (plus courant que vous ne le pensez). Mais vous pouvez toujours travailler sur votre projet et l'améliorer.

### Si quelque chose de similaire existe, votre projet peut-il l'améliorer ?

Si quelque chose de similaire existe, vos objectifs pourraient être de le rendre plus modulaire ou plus efficace. Vous pourriez essayer de l'implémenter dans un autre langage ou de l'améliorer de toute autre manière. 

Une excellente façon de le faire est de jeter un coup d'œil aux problèmes du dépôt existant. Essayez de faire vos recherches avec les solutions existantes (si elles existent) et découvrez quel aspect du projet pourrait éventuellement être amélioré. Votre travail pourrait même être un dérivé de l'autre projet.

Dans mon cas, comme je l'ai mentionné, je me suis inspiré d'un article de recherche intéressant que j'ai lu (Fastformer: Additive Attention Can Be All You Need). J'ai également découvert une implémentation officielle du code et une implémentation communautaire de l'article, toutes deux en PyTorch. 

En fin de compte, mon dépôt, bien qu'il soit un dérivé des articles de recherche, était _assez différent des implémentations de code existantes_.

### Pouvez-vous expliquer votre projet comme si j'avais 5 ans ?

ELI5, ou expliquez-le comme si j'avais cinq ans, est un excellent exercice que j'aime faire dès que j'ai une idée pour un dépôt. 

J'essaie d'expliquer ce que le projet vise à accomplir ou comment il fonctionne ou pourquoi il est meilleur que les dépôts similaires – à un ami qui ne connaît pas beaucoup le sujet. Souvent avec quelques analogies utiles. 

En faisant cela, cela m'aide à développer ou à obtenir une compréhension claire de ce que je veux faire dans mes projets. Essayer d'expliquer le projet à un ami aide souvent également à repérer les défauts dans mon plan ou les hypothèses que j'aurais pu faire en réfléchissant au projet.

Ce processus m'aide vraiment lorsque je commence la phase de développement du projet. C'est aussi à ce moment-là que je commence à créer un tableau de projet. Vous pouvez créer un tableau de projet sur GitHub lui-même, ou vous pouvez utiliser Trello, JetBrains Spaces, et ainsi de suite. 

J'adore utiliser GitHub Projects et les listes de contrôle des problèmes à ce stade pour m'aider à gérer, prioriser et avoir une idée claire de haut niveau de ce que je dois faire.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Frame-1.png)
_GitHub Projects et listes de contrôle des problèmes_

### Que pouvez-vous apprendre des grands dépôts dans des catégories similaires ?

Vous pouvez souvent vous inspirer et apprendre des dépôts appartenant à des catégories similaires. Regardez comment leur code est structuré. Vous devriez essayer de repérer d'autres grands dépôts et lire leur code bien écrit.

Dans mon cas, j'ai vraiment aimé la façon dont [reformer-pytorch](https://github.com/lucidrains/reformer-pytorch) était écrit. Il est facile à utiliser dans vos projets en tant que bibliothèque Python, il s'attend à ce que vous vous souciez idéalement d'une seule classe abstraisant une grande partie du processus de construction du modèle, et retourne une instance de `torch.nn.Module` (dans Pytorch, une classe de base pour tous les modules de réseau de neurones) avec laquelle vous pouvez faire presque tout. J'ai fini par construire [Fast-Transformer](https://github.com/Rishit-dagli/Fast-Transformer) de manière assez similaire.

## Comment développer le dépôt de votre projet

Vous avez peut-être entendu la citation populaire :

> N'importe quel idiot peut écrire du code qu'un ordinateur peut comprendre. Les bons programmeurs écrivent du code que les humains peuvent comprendre. — Martin Fowler

Si les gens ne peuvent pas comprendre votre code, ils ne l'utiliseront pas. 

J'ai remarqué dans mes propres dépôts que, lorsque je passe plus de temps à essayer de rendre les choses simples et faciles à utiliser, ces projets finissent par obtenir plus d'attention. Essayez donc de passer du temps supplémentaire à rendre votre projet plus utilisable et intuitif.

En règle générale lors du développement de votre dépôt :

* Vous devriez inclure une licence lorsque vous lancez un projet open-source. Cela permet aux gens d'utiliser, copier, modifier et contribuer à votre projet tout en conservant le copyright. Vous pouvez facilement trouver une licence adaptée à votre projet sur [https://choosealicense.com/](https://choosealicense.com/).
* Créez un bon README : il y a une section entière à ce sujet ensuite car c'est super important.
* Utilisez des conventions de code cohérentes et des noms de fonctions/méthodes/variables clairs. Vous pouvez souvent utiliser un outil d'analyse de code statique comme [black](https://github.com/psf/black), [ktlint](https://ktlint.github.io/), et ainsi de suite.
* Assurez-vous que votre code est clairement commenté, documentez vos pensées et incluez les cas limites.
* Assurez-vous qu'il n'y a pas de matériaux sensibles dans l'historique des révisions, les problèmes ou les pull requests (par exemple, des clés API, des mots de passe ou d'autres informations non publiques).
* Si vous développez une application/bibliothèque, je vous recommande d'utiliser les releases GitHub. Essayez de maintenir des notes de release et des changelogs clairs chaque fois que vous faites une nouvelle release afin que la communauté puisse suivre ce qui est nouveau. Enregistrez les bugs qui ont été corrigés, et ainsi de suite. Voici un [super dépôt](https://github.com/PatilShreyas/NotyKT/releases) montrant cela.
* Enfin, vous devriez également inclure des directives de contribution dans le dépôt qui indiquent à votre audience comment participer à votre projet. Vous pouvez inclure des informations sur les types de contributions que vous attendez ou comment suggérer une demande de fonctionnalité ou un rapport de bug, et ainsi de suite.

## Comment écrire un bon README

Un bon README est sans aucun doute l'un des composants les plus importants du dépôt. Il est affiché sur la page d'accueil du dépôt.

Les contributeurs potentiels vérifient généralement d'abord le README, et ce n'est qu'alors, s'ils le trouvent intéressant, qu'ils regarderont le code ou envisageront même d'utiliser le projet. 

De plus, ce n'est pas un guide définitif pour écrire un README. Amusez-vous avec et expérimentez ce qui fonctionne pour votre projet.

Généralement, vous voudrez inclure ces composants dans votre README :

### Expliquez ce que fait le projet

Essayez de décrire le projet en seulement 3-4 lignes. Ne vous inquiétez pas d'inclure trop de détails ou de fonctionnalités – vous pouvez les ajouter dans les sections suivantes. C'est aussi la première chose que les visiteurs de votre dépôt liront, alors assurez-vous de la rendre intéressante.

### Ayez une grande image de couverture ou un logo pour votre projet

Si vous avez un logo ou une image de couverture pour votre projet, incluez-la ici. Cela aide les contributeurs à avoir une sorte de visuel. 

### Partagez vos badges

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-28.png)
_Badges dans le README_

Vous verrez souvent de petits badges en haut du README qui transmettent des métadonnées, comme si tous les tests passent pour le projet. 

Vous pouvez utiliser [shields.io](http://shields.io/) pour en ajouter à votre README. Ceux-ci donneront souvent beaucoup de crédibilité à votre projet sans que les visiteurs aient à parcourir tout votre code.

### Incluez des visuels

Vous devriez toujours essayer d'inclure des visuels dans votre README. Ceux-ci pourraient être un gif montrant votre projet en action ou une capture d'écran de votre projet. 

De bons graphiques dans le README peuvent vraiment aider à convaincre d'autres développeurs d'utiliser votre projet.

### Expliquez comment installer ou configurer votre projet

Vous devriez également inclure des directives d'installation spécifiques. Incluez toutes les dépendances requises et tout ce que les autres développeurs doivent installer pour utiliser votre projet. 

Si vous avez rencontré des problèmes lors de la configuration de votre projet ou de l'installation d'une dépendance, il est probable que les utilisateurs rencontrent également ce problème, assurez-vous d'en parler.

Cela peut être très simple :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-29.png)
_Ma section Installation_

### Donnez des exemples d'utilisation clairs et reproductibles

Je pense que c'est super important d'avoir dans votre README. Vous ne devriez pas vous attendre à ce que d'autres développeurs fassent beaucoup de travail ou lisent votre code – rendez-le aussi facile que possible pour eux. 

Assurez-vous toujours et vérifiez que vos exemples de code ou une section "Comment faire" sont facilement reproductibles. Assurez-vous également qu'ils sont compréhensibles pour un large éventail d'utilisateurs, et n'omettez aucune instruction requise pour les reproduire.

Puisque mon projet est un package Python, j'ai créé un notebook Colab accompagnant pour démontrer l'utilisation du package. Cela permet aux gens de l'essayer facilement sur leurs navigateurs sans avoir à installer quoi que ce soit sur leurs propres machines. 

Il existe plusieurs produits qui vous permettent de faire cela comme repl.it, Glitch, Codepen, et ainsi de suite.

### Expliquez ce que vous pouvez faire avec le projet

Il est souvent utile de lister les fonctionnalités de votre projet et les problèmes qu'il peut aider à résoudre. Vous n'avez pas à couvrir toutes les fonctionnalités sur lesquelles vous avez travaillé, mais partagez les principales. 

Cela aidera les développeurs à comprendre ce que votre projet peut faire et pourquoi ils devraient l'utiliser.

### Partagez comment les gens peuvent obtenir de l'aide ou contribuer au projet

Enfin, vous devriez clairement indiquer si vous êtes ouvert aux contributions et quelles sont vos exigences pour les accepter. Vous devriez également documenter les commandes pour lint le code ou exécuter des tests. 

Ces étapes aident à garantir une haute qualité de code et réduisent la probabilité que les changements cassent quelque chose par inadvertance.

### Documentation externe

Supposons que vous pensiez que votre README devient trop long. Dans ce cas, vous pouvez créer un site web de documentation supplémentaire et y faire un lien dans le README plutôt que d'omettre des informations importantes.

Puisque je travaille beaucoup avec Python, j'utilise généralement [Sphinx](https://www.sphinx-doc.org/en/master/) pour générer ma documentation à partir des docstrings Python. Je trouve Sphinx assez flexible et facile à configurer. 

Il existe de nombreuses options pour générer votre documentation : [mkdocs](https://www.mkdocs.org/), [Docsaurus](https://docusaurus.io/), [docsify](https://docusaurus.io/), et plus encore. Pour mon projet qui a commencé à être en tendance, cependant, je n'avais pas besoin d'un site web de documentation externe.

Voici un exemple de ce que je pense être un bon début pour un README de l'un de mes propres projets. Ce n'est pas le README complet, mais juste ce que j'ai pu inclure dans une seule image :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Untitled--1-.png)
_Exemple de ce que j'ajoute dans un README_

Enfin, pour plus d'inspiration, je vous suggère d'essayer d'utiliser le guide ["Make a README"](https://www.makeareadme.com/).

## Comment attirer des visiteurs sur votre page GitHub

Une fois que vous avez créé un beau README et rendu le projet public, vous devez penser à amener des gens sur la page GitHub. 

Tout d'abord, assurez-vous d'ajouter des tags pertinents à votre dépôt GitHub. Ces tags faciliteront grandement la découverte du projet par les personnes explorant GitHub.

### Partagez votre projet sur Hacker News, Twitter et Reddit

Les meilleurs endroits pour publier votre projet sont Hacker News et Reddit. Gardez simplement à l'esprit que faire en sorte que votre publication soit l'histoire principale ou le post principal sur l'une de ces plateformes est une tâche difficile.

Lorsque l'un de mes dépôts est devenu l'histoire principale, il a obtenu plus de cent étoiles en quelques heures. 

Mais lorsque j'ai initialement publié mon dépôt sur Hacker News, je n'avais pas un seul vote positif. Ce n'est que lorsque quelqu'un d'autre de la communauté a remarqué mon projet et l'a publié sur Hacker News qu'il est devenu l'histoire principale. Il faut donc souvent une bonne dose de planification et un peu d'aide de vos amis pour faire en sorte que votre projet soit en tête.

Dans mon cas, Twitter a été un excellent endroit pour obtenir les tout premiers visiteurs de mon projet et atteindre un public externe. 

Cela sert souvent de moyen idéal pour permettre aux gens de voir rapidement s'ils pourraient être intéressés à vérifier votre projet. Et vous n'avez qu'un nombre limité de caractères pour vendre votre dépôt aux gens.

%[https://twitter.com/rishit_dagli/status/1433795914888482822?s=20]

De plus, assurez-vous de ne pas trop publier sur votre projet sur une plateforme, car cela pourrait être signalé comme spam. 

### Les mentions sont importantes mais pas de la manière que vous pensez

Je reçois souvent des e-mails ou des messages sur la promotion d'un projet ou d'un livre. Mais je crois fermement que cela n'a pas beaucoup de sens. 

Si vous voulez que quelqu'un parle de votre projet, alors vous voudrez qu'il ait utilisé votre projet et l'ait trouvé utile avant de le promouvoir. Une manière plus facile de le faire est donc d'ajouter simplement un bouton "tweeter ce projet" au README. Ensuite, les personnes qui aiment le projet peuvent naturellement en parler.

De plus, gardez à l'esprit que les mentions ne vous apportent pas directement des étoiles. Les personnes venant des mentions ne mettront une étoile à votre projet que si elles l'aiment.

Cela ne signifie certainement pas que vous ne devriez pas demander de l'aide, des retours ou des revues de code aux gens. En effet, vous devriez toujours essayer de répondre à tous types de retours : améliorations, bugs, incohérences, et ainsi de suite. 

Soyez toujours prêt à accepter les retours négatifs et réfléchissez à la manière dont vous pouvez vous améliorer. Vous pourriez finir par apprendre quelques nouvelles choses :)

Dans mon cas, j'ai remarqué un nombre inhabituellement élevé de visiteurs venant sur le projet depuis Twitter. Mon projet était implémenté avec TensorFlow et Keras, et quelques jours plus tard (après avoir été mentionné), j'ai découvert que le créateur de Keras lui-même avait mentionné mon projet !

%[https://twitter.com/fchollet/status/1434214348650475522?s=20]

Cela était probablement dû au fait que j'ai ajouté un "Tweeter ce projet" en haut de mon README et que les découvertes sont venues d'elles-mêmes.

## Conseils de la communauté des développeurs sur la création d'un projet sur GitHub

En tant qu'exercice intéressant, j'ai essayé de demander à la communauté sur Twitter des conseils qu'ils pourraient avoir pour moi à inclure dans ce blog. En voici quelques-uns :

> (Vous devriez ajouter) 1. Documentation 2. Journaux de décision — Shreyas Patil

> De bons modèles de problèmes et de PR. Vous pourriez également utiliser les formulaires de problèmes GitHub. — Burhanuddin Rangwala

> Documentation (devrait être complète et) inclure l'architecture de l'application, l'emballage, le guide de style, la conversation de codage, les liens de la bibliothèque de framework technologique utilisée, les jetons prérequis, etc. — Chetan Gupta

## Conclusion

Merci de m'avoir suivi jusqu'à la fin. J'espère que vous repartirez avec une ou deux choses pour vos propres projets open-source et que vous en construirez de meilleurs. En incorporant ces conseils et en expérimentant – et en mettant beaucoup de travail acharné – vous pouvez créer un excellent projet.

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Un grand merci à [Santosh Yadav](https://www.santoshyadav.dev/) et [Shreyas Patil](https://shreyaspatil.dev/) pour m'avoir aidé à améliorer cet article.

Vous pouvez également me trouver sur Twitter [@rishit_dagli](https://twitter.com/rishit_dagli), où je tweete sur l'open-source, le machine learning et un peu d'Android.