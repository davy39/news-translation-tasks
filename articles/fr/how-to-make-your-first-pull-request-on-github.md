---
title: Comment faire votre première Pull Request sur GitHub
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2019-07-11T06:27:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-pull-request-on-github
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/pr.png
tags:
- name: Collaboration
  slug: collaboration
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
seo_title: Comment faire votre première Pull Request sur GitHub
seo_desc: 'Many tutorials exist about this topic but they make things overly complicated
  by assuming one has to contribute code to a project.

  What if they just need to edit a file, maybe the project README to fix a typo?

  You don''t need to know how to code or ho...'
---

De nombreux tutoriels existent sur ce sujet, mais ils compliquent trop les choses en supposant qu'il faut contribuer du **code** à un projet.

Et si vous deviez simplement modifier un fichier, peut-être le README du projet pour corriger une faute de frappe ?

Vous n'avez pas besoin de savoir coder ou utiliser Git pour cela. Mais une fois que vous commencez à faire des Pull Requests, vous pouvez faire beaucoup plus de choses et collaborer sur des projets avec d'autres personnes ! Et peut-être que cela vous poussera à contribuer du code plus tard.

Je suppose que vous avez déjà un compte GitHub (gratuit). Si ce n'est pas le cas, rendez-vous sur [github.com](https://github.com) et créez-en un.

Laissez-moi vous montrer le processus.

Je suis allé sur cette page [https://web.dev/prefers-color-scheme/](https://web.dev/prefers-color-scheme/) et j'ai trouvé une possible faute de frappe. Cette ligne manque un point à la fin.

![article-i-want-to-edit](https://www.freecodecamp.org/news/content/images/2019/07/article-i-want-to-edit.png)

> Je ne suis pas un puriste de la grammaire, c'est juste pour l'exemple ?

Je sais que ce site est hébergé sur GitHub, et que cet article exact est hébergé ici : [https://github.com/GoogleChrome/web.dev/tree/master/src/site/content/en/blog/prefers-color-scheme](https://github.com/GoogleChrome/web.dev/tree/master/src/site/content/en/blog/prefers-color-scheme)

![github-folder-for-article](https://www.freecodecamp.org/news/content/images/2019/07/github-folder-for-article.png)

J'ouvre le fichier index.md [https://github.com/GoogleChrome/web.dev/blob/master/src/site/content/en/blog/prefers-color-scheme/index.md](https://github.com/GoogleChrome/web.dev/blob/master/src/site/content/en/blog/prefers-color-scheme/index.md) directement sur GitHub et j'appuie sur l'icône de crayon dans la barre d'outils du fichier. En survolant, il est écrit "Fork this project and edit the file".

![the-index-md-file](https://www.freecodecamp.org/news/content/images/2019/07/the-index-md-file.png)

Cela ouvre une vue d'éditeur avec cette information :

> Vous modifiez un fichier dans un projet pour lequel vous n'avez pas les droits d'écriture. Soumettre une modification à ce fichier l'écrira dans une nouvelle branche de votre fork flaviocopes/web.dev, afin que vous puissiez envoyer une pull request.

![the-editor-view](https://www.freecodecamp.org/news/content/images/2019/07/the-editor-view.png)

Je peux ajouter ce point, puis dans le formulaire en bas, j'explique les modifications que j'ai apportées :

![propose-file-change](https://www.freecodecamp.org/news/content/images/2019/07/propose-file-change.png)

J'ai appuyé sur le bouton "Propose File Change" et une vue de comparaison est apparue.

![compare-view](https://www.freecodecamp.org/news/content/images/2019/07/compare-view.png)

Là, je peux passer en revue les modifications que j'ai apportées, pour m'assurer que tout est correct, et enfin je peux cliquer sur le bouton "Create Pull Request". Actuellement, les modifications ont été apportées à *votre fork* du projet, qui a été créé automatiquement par GitHub lorsque vous avez cliqué sur l'icône de crayon.

![open-pull-request](https://www.freecodecamp.org/news/content/images/2019/07/open-pull-request.png)

En haut de cette vue, vous pouvez voir que je suis sur le point de soumettre une PR au projet `GoogleChrome/web.dev` depuis mon fork `flaviocopes/web.dev`, de ma branche `patch-2` vers leur branche `master`.

Appuyer sur le bouton "Create Pull Request" affiche un autre formulaire où je peux écrire une description détaillée pour la Pull Request.

Les Pull Requests peuvent contenir de nombreuses modifications différentes, donc en théorie, vous pourriez avoir beaucoup de fichiers modifiés dans la même PR, c'est pourquoi vous pouvez ajouter un résumé.

Ce dépôt a un modèle pour le texte de la PR, pour aider l'équipe à le gérer. Notre PR est très simple, donc je supprime le modèle et je colle simplement le contenu du message de commit précédent.

Remarquez l'indice à droite ? Ils me disent que le projet a un fichier CONTRIBUTING.md, qui explique comment contribuer et les directives. Plutôt cool.

![contributing](https://www.freecodecamp.org/news/content/images/2019/07/contributing.png)

Il semble que nous devions signer un CLA (Contributor License Agreement) pour finaliser notre PR. J'ai déjà signé un Google CLA dans le passé, donc cette étape est claire pour moi, mais vous devrez peut-être le faire. La plupart des projets n'en ont pas vraiment besoin.

J'ai cliqué sur "Create pull request" et la PR est maintenant envoyée !

![pull-request-sent](https://www.freecodecamp.org/news/content/images/2019/07/pull-request-sent.png)

Maintenant, c'est aux mainteneurs du projet de prendre le relais et de l'accepter, vous devez simplement attendre un email vous informant qu'elle a été fusionnée, ou tout commentaire d'autres personnes.

[... quelques heures se sont écoulées...]

J'ai reçu un email en retour, la PR a été rejetée car ce point était en fait à la bonne place ! (Je ne le savais pas).

Mais voici une chose que je voulais ajouter : ne soyez pas en colère ou contrarié si une PR que vous soumettez n'est pas acceptée. Les mainteneurs du projet y travaillent depuis des mois ou des années et ils savent mieux que vous ce qui est bon pour lui.

De plus, surtout avec le code, les avis peuvent être très différents et une PR que vous pensez géniale peut ne pas être la bienvenue.

Il est également préférable de demander avant de travailler sur une PR substantielle, pour voir si c'est quelque chose dont le projet a vraiment besoin.

Les corrections de bugs sont des débuts faciles.

---

Je suis Flavio. J'écris des tutoriels pour les développeurs sur [flaviocopes.com](http://flaviocopes.com)