---
title: Comment Fork un Dépôt GitHub – Un Workflow Complet
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2022-02-11T18:02:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-fork-a-github-repository
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/freeCodeCamp-Cover.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: version control
  slug: version-control
seo_title: Comment Fork un Dépôt GitHub – Un Workflow Complet
seo_desc: "GitHub is a great application that helps you manage your Git repositories.\
  \ You can also use it to contribute to the open source ecosystem and collaborate\
  \ with other contributors. \nPublic repositories on GitHub often get lots of attention\
  \ from contrib..."
---

`GitHub` est une excellente application qui vous aide à gérer vos dépôts Git. Vous pouvez également l'utiliser pour contribuer à l'écosystème open source et collaborer avec d'autres contributeurs. 

Les dépôts publics sur GitHub attirent souvent beaucoup d'attention de la part des contributeurs, ce qui aide à améliorer le projet.

Alors, comment pouvez-vous facilement travailler sur un dépôt public ? L'outil de `forking` (bifurcation) de dépôt permet aux contributeurs de copier le dépôt de code source localement et d'y apporter les modifications qu'ils souhaitent. 

Mais si vous allez utiliser cet outil en tant que débutant, vous devez comprendre le workflow de la bifurcation de dépôt afin de pouvoir travailler sans problème avec d'autres dépôts publics.

Dans cet article, nous allons apprendre comment bifurquer un dépôt avec des exemples pratiques et du storytelling. Si vous aimez apprendre à partir de contenu vidéo, cet article est également disponible sous forme de vidéo YouTube.

%[https://www.youtube.com/watch?v=h8suY-Osn8Q&t=2s]

## Qu'est-ce que la Bifurcation de Dépôt GitHub ?

Supposons que vous adorez travailler sur un framework ou une bibliothèque particulier comme React.js. Un beau jour, vous trouvez un moyen d'améliorer vous-même la fonctionnalité de React. 

Le code source de React est disponible en tant que dépôt public sur GitHub, vous pouvez donc en faire une copie locale en le `bifurquant`.

Une fois que vous avez obtenu la copie locale du code, vous pouvez apporter les modifications pertinentes et demander à la communauté React de réviser vos modifications. 

Après avoir révisé vos modifications de code, la communauté React peut les approuver ou vous demander des modifications supplémentaires. Ils sont susceptibles de prendre vos modifications de code après approbation.

Alors, comprenons tout le workflow de `bifurcation` avec l'histoire de deux développeurs, Tom et Hari.

## Un Workflow Complet de Bifurcation

Tom et Hari sont deux développeurs qui ont leurs comptes GitHub individuels. Tom travaille sur un projet exceptionnel, et il gère son code source dans un dépôt public appelé `/tom/repo`. Hari est impressionné par l'idée et veut contribuer au projet. 

Maintenant, il y a deux façons pour Hari de s'y prendre.

* Hari demande à Tom : "Hey Tom, je veux contribuer à ton projet. Pourrais-tu s'il te plaît m'ajouter en tant que Contributeur ?". Eh bien, Tom peut être d'accord ou non. Comme le projet est déjà disponible en tant que dépôt public, il peut simplement demander de le bifurquer et de l'utiliser.
* La deuxième façon est que Hari bifurque simplement le dépôt lui-même et commence à travailler. Il n'a pas besoin d'attendre pour parler à Tom et faire en sorte que Tom l'ajoute spécifiquement en tant que contributeur.

Cette deuxième approche de `bifurcation` directe d'un dépôt est plus pratique pour tout contributeur. Alors, comment cela fonctionne-t-il ? Comprenons le workflow étape par étape.

1. Hari bifurque le dépôt `/tom/repo`. Nous appelons le dépôt `/tom/repo` le `Dépôt Upstream`.
2. Le dépôt est maintenant disponible dans le compte GitHub de Hari sous le nom `/hari/repo`. Nous appelons le `hari/repo` le `Dépôt Bifurqué`. De plus, c'est une copie exacte du dépôt upstream. Ce dépôt est entièrement détaché du dépôt de Tom et Hari peut commencer à apporter les modifications qu'il souhaite. Hari va d'abord cloner le dépôt et commencer à apporter des modifications pour cela.
3. Hari apporte les modifications nécessaires et pousse les modifications vers le dépôt bifurqué.
4. Enfin, Hari crée une `Pull Request` du dépôt bifurqué vers le dépôt upstream. Tom révise la pull request à sa convenance pour l'approuver et la fusionner si tout se passe bien.

Voilà tout le workflow—des moyens simples et directs de contribuer au dépôt public. Une image vaut mille mots. Voici une démonstration du workflow que nous avons discuté.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/GitHub-Fork.gif)
_Workflow - Bifurcation d'un Dépôt_

## Comment Bifurquer un Dépôt dans GitHub

Bifurquer un dépôt est une question de cliquer sur un bouton. 

Pour suivre, accédez à un dépôt public que vous souhaitez bifurquer. En haut à droite de la page, vous trouverez le bouton `Fork`. Cliquez sur le bouton et attendez quelques secondes. Vous verrez que le nouveau dépôt bifurqué est créé sous votre compte GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-29.png)
_Bouton Fork_

Suivez les étapes que nous avons apprises ci-dessus après avoir bifurqué le dépôt pour commencer à contribuer.

## Pratiquons la Bifurcation

En tant que débutant, souhaitez-vous pratiquer la `bifurcation` pour être plus confiant ? Faisons cela. Vous pouvez effectuer ces tâches pour pratiquer la bifurcation.

* Accédez à ce dépôt public : [https://github.com/atapas/fork-me](https://github.com/atapas/fork-me)
* Créez un dossier avec le même nom que votre identifiant GitHub (c'est atapas pour moi).
* Ajoutez un fichier `Readme.md` à l'intérieur du dossier avec un texte de votre choix.
* Créez une `Pull Request` upstream. Je vais la réviser et la fusionner si tout est correct.

Ne vous inquiétez pas si vous faites une erreur. Continuez à essayer, vous allez y arriver. Ce sera comme un terrain de jeu pour pratiquer la contribution à un dépôt open source.

## En Résumé

* Git est un outil de contrôle de version largement utilisé par la communauté des développeurs. Si vous êtes débutant avec Git, apprenez-en davantage [ici](https://www.youtube.com/watch?v=vWtu4mzUgQo).
* GitHub est une application populaire pour gérer les dépôts Git. Tout le monde peut contribuer à un dépôt public.
* La bifurcation est un excellent outil pour copier le code source d'un dépôt de quelqu'un vers votre dépôt et y contribuer.
* Le workflow de bifurcation est simple à apprendre et à démarrer.

## Avant de Terminer...

J'espère que vous avez trouvé l'article utile. Veuillez pratiquer la bifurcation et contribuer à des projets open source. Mes DM sont ouverts sur `Twitter` si vous souhaitez discuter davantage.

Restez connectés. Je partage mes apprentissages sur JavaScript, le Développement Web, la Carrière et le Blogging sur ces plateformes également :

* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary)
* [Abonnez-vous à ma Chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1)
* [Projets secondaires sur GitHub](https://github.com/atapas)

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.