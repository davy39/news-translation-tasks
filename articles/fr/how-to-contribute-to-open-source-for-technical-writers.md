---
title: Comment contribuer à l'Open Source – un guide pour les rédacteurs techniques
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2022-10-24T21:20:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-contribute-to-open-source-for-technical-writers
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-william-fortunato-6393024.jpg
tags:
- name: open source
  slug: open-source
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
seo_title: Comment contribuer à l'Open Source – un guide pour les rédacteurs techniques
seo_desc: 'Contributing to open source can be a daunting prospect, especially if you
  haven''t done so before, or if you''re used to working on documentation rather than
  code.

  This guide will help technical writers get started contributing to open-source projects,...'
---

Contribuer à l'open source peut sembler intimidant, surtout si vous ne l'avez jamais fait auparavant, ou si vous êtes habitué à travailler sur de la documentation plutôt que du code.

Ce guide aidera les rédacteurs techniques à commencer à contribuer à des projets open source, et à identifier certains des pièges courants que vous pourriez rencontrer lorsque vous commencez à contribuer.

Il mettra également en lumière certains des avantages de contribuer à l'open source, et fournira des ressources supplémentaires pour commencer à contribuer à l'open source en tant que rédacteur technique.

## Ce que vous allez apprendre

Cet article couvrira comment les rédacteurs techniques peuvent contribuer à l'open source, quels sont les avantages, et certains des inconvénients potentiels. Nous passerons également en revue quelques ressources pour bien démarrer.

## Qu'est-ce que l'Open Source ?

L'open source est une manière collaborative de développer et de distribuer des logiciels. Des personnes du monde entier contribuent à des projets open source en ajoutant des fonctionnalités, en corrigeant des bugs, en répondant à des questions, en traduisant du texte, ou en écrivant des tutoriels.

## Pourquoi contribuer ?

Contribuer à des logiciels open source est l'une des meilleures façons pour les rédacteurs techniques et autres travailleurs du savoir de redonner et de faire une différence.

Vous pouvez aider à améliorer les logiciels que vous utilisez tous les jours, ou vous pouvez apprendre de l'exemple des autres qui ont contribué avant vous. De plus, c'est un excellent moyen de rencontrer des personnes ayant des intérêts communs. Et lorsque vos contributions sont appréciées, vous vous sentirez comme faisant partie de la communauté.

Vous vous demandez peut-être – quand devrais-je contribuer ? Eh bien, si vous êtes nouveau dans l'open source, contribuez à votre propre rythme – ne vous inquiétez pas d'essayer de faire trop trop tôt. Vous trouverez ce avec quoi vous êtes à l'aise.

Contribuer à l'open source augmentera non seulement votre ensemble de compétences, mais vous permettra également de développer des contacts au sein de la communauté et même de créer des opportunités pour du travail freelance.

Cela prend un certain temps pour acquérir les connaissances et les compétences nécessaires pour devenir un contributeur actif (surtout parce que la documentation nécessite souvent un ensemble de compétences différent de la programmation), mais cela en vaut l'investissement.

## Défis de la contribution

Les rédacteurs techniques peuvent rencontrer plusieurs défis lorsqu'ils commencent à contribuer à des projets open source. L'un des plus courants est de ne pas être sûr de la meilleure façon de contribuer, surtout si vous ne connaissez pas encore le projet.

Vous pourriez également ne pas être sûr de l'endroit où votre travail devrait aller ou de ce qui est attendu des contributeurs. Il existe quelques moyens de contourner ce problème : vous pouvez lire le fichier `README` du projet et/ou la documentation pour voir s'ils ont des directives de contribution. Vous pouvez également contacter l'équipe derrière le projet et demander de l'aide.

## Comment contribuer à des projets Open Source

Tout d'abord, vous voudrez trouver un projet sur [GitHub](https://github.com/) auquel vous souhaitez contribuer. Vous pouvez [lire ce tutoriel](https://www.freecodecamp.org/news/github-search-tips/) sur la façon de rechercher sur GitHub et de trouver des projets.

Ensuite, vous voudrez ouvrir le README et vous assurer de bien comprendre les instructions données.

Puis, forkez le dépôt en cliquant sur Fork situé en haut à droite de votre écran.

![Image](https://lh5.googleusercontent.com/x3IyU70meecZi1qYS4_CCZW0cOZqpcTdVfKjG3_TpM1TJj_tH15FhNaKmrAL2bl8fTU7fcUAditd6AzqJbJItmCavBxQObpD2bAJCRlYds-sX-Z3iyA4b_pajXsOnAJM1_8tbPdbyOGNrXyxCfu1Qk-x3AyDrtDrFxbbxlmIaSSwaj3kYX87ELMUSQ)

Clonez le dépôt forké sur votre ordinateur local en utilisant la commande suivante :

```bash
git clone <LIEN VERS LE DÉPÔT>
```

Vous verrez le lien du dépôt lorsque vous cliquerez sur le menu déroulant du code.

Une fois que vous l'avez cloné, ouvrez le répertoire contenant votre nouveau fork et commencez à ajouter votre contribution.

Lorsque vous avez terminé, poussez vos changements sur GitHub en utilisant les instructions suivantes :

```bash
git status //affiche les modifications qui ont été préparées
git add . // ajoute les changements au dépôt cloné
git commit -m "changes" //effectue un commit vers le dépôt cloné
git branch -M changes //crée une nouvelle branche
git push -u origin changes //pousse les changements
```

GitHub vous invitera à créer une pull request après avoir poussé vos changements vers le dépôt cloné. Allez-y et créez la pull request, puis attendez que les mainteneurs fusionnent votre dépôt cloné avec le dépôt principal.

**Assurez-vous d'incorporer les modifications en amont dans votre dépôt local** si vous avez forké le projet il y a un certain temps.

Si vous rencontrez un fichier volumineux, installez `git-lfs` s'il n'est pas déjà installé avec la commande suivante : `brew install git-lfs`

En téléchargeant les versions appropriées des fichiers volumineux lentement, l'extension Git LFS (Large File Storage), créée par Atlassian, GitHub et quelques autres contributeurs open source, réduit l'impact des fichiers volumineux dans votre dépôt.

Vous pouvez également utiliser la [documentation suivante](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) pour installer `git-lfs`.

### Bonnes pratiques lors de la contribution à l'open source

1. Identifiez un domaine où vous pourriez être utile et trouvez le projet pertinent sur GitHub.
2. Lisez la documentation de tout projet ou programme similaire à celui qui vous intéresse. Cela vous donnera une meilleure compréhension de ce qui est impliqué dans la contribution et de ce que d'autres personnes ont contribué.
3. Recherchez les problèmes étiquetés "good first issue" et lisez-les – ceux-ci sont généralement assez faciles à résoudre.
4. Préparez votre code en suivant les directives de contribution du projet.
5. Rédigez une pull request avec votre solution et expliquez pourquoi elle résout le problème en question. Incluez des liens vers des ressources connexes comme des tutoriels si nécessaire.
6. Soumettez votre pull request pour examen. L'équipe discutera de son acceptation dans le dépôt et vous informera de sa décision.
7. Si ils décident de ne pas accepter votre pull request, demandez-leur comment vous pourriez répondre à leurs préoccupations afin qu'ils reconsidèrent l'acceptation à une date ultérieure.
8. Si ils acceptent votre pull request, remerciez-les !
9. Continuez à rechercher de nouveaux problèmes à résoudre et partagez vos progrès en cours de route !

## Quels types de contributions puis-je faire ?

Vous pouvez contribuer à ces projets de nombreuses manières, notamment en soumettant des pull requests pour des corrections de bugs ou des ajouts de fonctionnalités, en écrivant de la documentation sur l'utilisation du logiciel, en améliorant la documentation actuelle, en traduisant le texte dans une autre langue, et en corrigeant les fautes de frappe.

Vous devriez vous impliquer en choisissant un projet qui vous intéresse et en lisant sa documentation avant de vous lancer.

Écrire pour un projet open source est un excellent moyen de vous établir en tant qu'expert dans votre domaine et de vous positionner pour de futures opportunités freelance.

Une chose que les rédacteurs techniques doivent toujours garder à l'esprit lorsqu'ils écrivent pour des projets open source est que leur public est principalement des développeurs. Cela signifie qu'ils ont besoin de plus de détails techniques que ce que vous trouveriez dans d'autres types d'écriture.

## Où puis-je trouver des projets Open Source ?

Il existe une variété d'endroits où vous pouvez trouver des projets open source. GitHub est l'endroit le plus populaire pour les projets open source, mais il existe également des dépôts sur BitBucket, Gitlab et d'autres sites.

Si vous avez une idée pour un projet open source qui n'existe pas encore, commencez par rassembler votre plan dans un fichier `README`. Si vous n'êtes pas sûr de comment commencer à contribuer à un projet existant, consultez sa documentation ou lisez quelques pull requests avant d'en soumettre une vous-même.

## **Projets exemples**

* [Le projet HTML5 Boilerplate](https://github.com/h5bp/html5-boilerplate) est un projet open source populaire pour les développeurs web qui fournit du code HTML, CSS et Javascript pour construire un site web ou une application web.
* [Le framework Bootstrap](https://github.com/twbs), également un projet open source, est une collection d'outils pour aider les développeurs à créer rapidement des sites web responsives.
* [Jekyll](https://jekyllrb.com/docs/contributing/) est un générateur de site statique écrit en Ruby, conçu pour les blogs personnels.
* [Documentation React.js](https://github.com/reactjs/reactjs.org) - La documentation React.js fournit des informations officielles sur l'utilisation de React.js
* [GitHub pages](https://github.com/github/docs) - Elles contiennent tout ce que vous devez savoir sur GitHub.
* [Projet Galaxy (matériel de formation)](https://github.com/galaxyproject/training-material) - Une collection de matériaux de formation sur le projet Galaxy, qui est une plateforme open source basée sur le web pour la recherche computationnelle intensive en données, allant au-delà des sciences biologiques.
* [CNCF (Cloud Native Computing Foundation)](https://github.com/cncf) - CNCF est l'informatique cloud-native open source qui héberge des projets tels que Kubernetes et Prometheus pour rendre le cloud-native omniprésent et durable.

Vous pouvez également consulter [Google Season of Docs](https://developers.google.com/season-of-docs) qui offre une assistance aux projets open source pour améliorer leur documentation et permet aux rédacteurs techniques qualifiés d'acquérir de l'expérience dans l'open source.

Il existe de nombreuses façons différentes de contribuer, ce qui signifie qu'il y a quelque chose pour tout le monde.

## **Conclusion**

Contribuer à l'open source est un excellent moyen pour les rédacteurs techniques et autres créateurs de contenu de partager leurs connaissances avec le monde.

Il existe de nombreuses façons différentes de contribuer, ce qui signifie qu'il y a quelque chose pour tout le monde.