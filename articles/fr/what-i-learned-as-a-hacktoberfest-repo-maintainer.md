---
title: Ce que j'ai appris en maintenant un dépôt pendant le Hacktoberfest et en fusionnant
  356 PR
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-11-02T16:17:06.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-as-a-hacktoberfest-repo-maintainer
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-5.56.25-PM.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: hacktoberfest
  slug: hacktoberfest
- name: lessons learned
  slug: lessons-learned
- name: open source
  slug: open-source
seo_title: Ce que j'ai appris en maintenant un dépôt pendant le Hacktoberfest et en
  fusionnant 356 PR
seo_desc: 'Hacktoberfest is a month long celebration of open source. And this year
  I participated as a maintainer for freeCodeCamp''s Developer Quiz Site.

  I merged a total of 356 pull requests and helped a lot of new contributors get started
  with open source. We...'
---

Hacktoberfest est une célébration d'un mois de l'open source. Et cette année, j'ai participé en tant que mainteneur pour le [Site de Quiz pour Développeurs de freeCodeCamp](https://github.com/freeCodeCamp/Developer_Quiz_Site).

J'ai fusionné un total de 356 pull requests et j'ai aidé de nombreux nouveaux contributeurs à se lancer dans l'open source. Nous avons pu ajouter un total de 477 nouvelles questions de quiz au [Site de Quiz pour Développeurs](https://developerquiz.org/). 

Voici quelques statistiques supplémentaires : 

### Statistiques au 1er octobre 2022

Nombre de questions : 694

Forks : 61

Stars : 42

### Statistiques au 1er novembre 2022

Nombre de questions : 1171

Forks : 246

Stars : 109

Ce voyage d'un mois a été fou, productif, amusant et éducatif. Voici toutes les choses que j'ai apprises pendant le Hacktoberfest 2022.

## Table des Matières

- [Comment tout a commencé](#heading-comment-tout-a-commence)
- [Préparation pour le Hacktoberfest](#heading-preparation-pour-le-hacktoberfest)
  - [Étape 1 : Ajout du sujet Hacktoberfest et des labels](#heading-etape-1-ajout-du-sujet-hacktoberfest-et-des-labels)
  - [Étape 2 : Création de modèles d'issues](#heading-etape-2-creation-de-modeles-dissues)
  - [Étape 3 : Mise à jour de la documentation de contribution](#heading-etape-3-mise-a-jour-de-la-documentation-de-contribution)
  - [Étape 4 : Création d'issues bien définies](#heading-etape-4-creation-dissues-bien-definies)
  - [Étape 5 : Ajout de réponses sauvegardées](#heading-etape-5-ajout-de-reponses-sauvegardees)
  - [Étape 6 : Ouverture des discussions GitHub](#heading-etape-6-ouverture-des-discussions-github)
- [Leçons apprises pendant le Hacktoberfest](#heading-lecons-apprises-pendant-le-hacktoberfest)
  - [Diriger avec patience, empathie et gentillesse](#heading-diriger-avec-patience-empathie-et-gentillesse)
  - [Ne pas se laisser submerger par le spam](#heading-ne-pas-se-laisser-submerger-par-le-spam)
  - [Comment fermer gracieusement les PR qui ne seront pas acceptées](#heading-comment-fermer-gracieusement-les-pr-qui-ne-seront-pas-acceptees)
- [Conclusion](#heading-conclusion)

## Comment tout a commencé

En décembre 2021, freeCodeCamp lançait leur [jeu Learn to Code RPG](https://www.freecodecamp.org/news/learn-to-code-rpg/). C'est un roman visuel interactif qui suit le rêve de Lydia de devenir développeuse. 

J'ai participé à la création de questions de quiz sur des sujets comme HTML, CSS, informatique, Python, et bien d'autres pour le lancement initial. 

Environ une semaine avant le lancement, Quincy m'a approché, ainsi que quelques autres, pour construire un [Site de Quiz pour Développeurs](https://developerquiz.org/). Cela devait être un site compagnon au [jeu Learn to Code RPG](https://www.freecodecamp.org/news/learn-to-code-rpg/) et fournir aux campeurs un moyen de pratiquer plus de questions de quiz en dehors du jeu. 

Le lancement initial du [Site de Quiz pour Développeurs](https://developerquiz.org/) comportait environ 600+ questions de quiz. Nous avons également créé quelques issues ouvertes dans le [dépôt](https://github.com/freeCodeCamp/Developer_Quiz_Site) pour que la communauté puisse ajouter plus de questions au site. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.11.55-PM.png)

Pendant une partie de l'année 2022, il y a eu une activité modérée dans le dépôt, mais la plupart du temps, elle est restée plutôt lente. Mais une fois septembre arrivé, j'ai pensé à inscrire le [Site de Quiz pour Développeurs](https://developerquiz.org/) au Hacktoberfest.

J'ai contacté Quincy et il a trouvé que c'était une excellente idée car nous pouvions utiliser cette opportunité pour obtenir plus de questions de quiz de la communauté.

## Préparation pour le Hacktoberfest

Il restait environ 3 semaines avant le début du Hacktoberfest. Voici comment j'ai utilisé ce temps pour préparer le dépôt.

### Étape 1 : Ajout du sujet Hacktoberfest et des labels

La première étape a été d'ajouter le sujet Hacktoberfest au dépôt afin que les gens sachent que nous participions à l'événement de cette année. J'ai embelli la section À propos et ajouté les labels appropriés pour aider à inviter les gens à contribuer au dépôt. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.41.14-PM.png)

J'ai ensuite veillé à créer le label `hacktoberfest-accepted` afin de pouvoir l'appliquer à chaque PR approuvée pour nous aider à suivre le nombre total de PR pour le Hacktoberfest. J'ai également ajouté les labels `spam`, `hacktoberfest`, et `first-timers-only` car je savais qu'ils seraient utiles. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.45.45-PM.png)

### Étape 2 : Création de modèles d'issues

Les [modèles d'issues GitHub](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) sont un excellent moyen de s'assurer que les contributeurs fournissent toutes les informations nécessaires pour les corrections de bugs, les changements de documentation, les demandes de fonctionnalités ou les problèmes généraux. 

J'ai décidé de configurer 5 catégories d'issues et de rendre certains champs obligatoires afin que les contributeurs fournissent un certain niveau de détail aux issues qu'ils créaient.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.57.28-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-6.53.25-PM.png)

### Étape 3 : Mise à jour de la documentation de contribution

Lorsque le dépôt a été initialement créé, la documentation de contribution pointait vers les [directives générales de contribution de freeCodeCamp](https://contribute.freecodecamp.org./#/). Bien que cette documentation soit très complète, elle n'était pas assez spécifique sur la manière dont les gens pouvaient contribuer au [dépôt du site de quiz pour développeurs](https://github.com/freeCodeCamp/Developer_Quiz_Site) en particulier. 

J'ai décidé de réviser complètement la documentation et de créer un nouveau fichier approfondi spécialement pour le Site de Quiz pour Développeurs. Comme je prévoyais que nous aurions beaucoup de débutants avec Git et GitHub, j'ai essayé de la rendre aussi accessible et conviviale pour les débutants que possible.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-7.08.50-PM.png)

### Étape 4 : Création d'issues bien définies

Pour attirer des contributeurs vers notre dépôt, je savais que nous devions avoir des issues clairement définies. Si les issues étaient trop vagues, je savais que les gens auraient des tonnes de questions ou pourraient ne pas être intéressés à contribuer.

J'ai veillé à inclure toutes les directives nécessaires pour la soumission, y compris des extraits de code pour le formatage approprié, des liens vers le Code de Conduite, les documents de contribution, et des liens vers les fichiers qu'ils devaient modifier. 

Voici un exemple de l'une des issues que j'ai créées pour encourager plus de questions JavaScript.

#### Exemple d'issue

[developerquiz.org](developerquiz.org) contient actuellement plus de 600 questions de quiz. Nous cherchons à développer les questions JavaScript et nous encourageons d'autres développeurs à ajouter leurs questions de quiz au site.

**Veuillez noter : nous nous concentrons uniquement sur les questions JavaScript générales plutôt que sur les questions spécifiques aux bibliothèques et frameworks.**

Vous pouvez trouver la liste complète des questions ci-dessous.
https://github.com/freeCodeCamp/Developer_Quiz_Site/blob/main/src/data/javascript-quiz.ts

Vous pouvez ajouter vos propres questions en haut de ce fichier.
**Veuillez d'abord vérifier que votre question n'existe pas déjà dans le fichier avant de créer une PR.**

Voici un exemple de format pour les questions. 

```
  {
    Question:
      "En JavaScript, quel est le nom de la méthode utilisée pour supprimer les espaces blancs au début et à la fin d'une chaîne ?",
    Answer: ".trim()",
    Distractor1: ".substring()",
    Distractor2: ".reduce()",
    Distractor3: ".slice()",
    Explanation:
      "La méthode .trim() supprime les espaces blancs (y compris les espaces, les tabulations, etc.) des deux extrémités d'une chaîne et retourne une nouvelle chaîne sans modifier l'originale.",
    Link: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim",
  },
```
Pour le champ `link`, veuillez utiliser un article freeCodeCamp, une vidéo YouTube freeCodeCamp ou une documentation officielle.
Si vous choisissez de référencer une vidéo, veuillez inclure le timestamp pour le sujet couvert.

Vous pouvez en savoir plus sur la création de timestamps dans cet [article utile](https://www.lifewire.com/link-to-specific-part-of-youtube-video-1616414#). 

Cette issue ne sera attribuée à personne et restera ouverte pour plusieurs contributeurs. 

**Veuillez ne pas vous attribuer cette issue ou la fermer.**

Bonne contribution !

Pour la plupart de nos issues, je voulais que plusieurs contributeurs puissent participer. J'ai donc ajouté un avertissement en bas pour informer les gens qu'elle resterait ouverte et ne serait attribuée à personne. 

J'ai également veillé à ajouter les labels `good-first-issue`, `help-wanted`, et `hacktoberfest` pour attirer plus de contributeurs. 

### Étape 5 : Ajout de réponses sauvegardées

Les [réponses sauvegardées](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/creating-a-saved-reply) sont une fonctionnalité de GitHub où vous pouvez créer et sauvegarder vos propres messages que vous prévoyez d'utiliser de manière répétée dans les issues et les pull requests. 

J'ai décidé de créer les réponses suivantes :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-7.59.09-PM.png)

Je voulais des réponses pour féliciter à la fois les nouveaux contributeurs et ceux qui reviennent, car ils ont pris le temps de rendre notre dépôt meilleur. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-8.01.40-PM.png)

Je voulais également créer une réponse où je remerciais le contributeur pour sa contribution et demandais des modifications à la pull request. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-8.05.29-PM.png)

La dernière réponse que j'ai créée était pour informer les contributeurs que leur pull request avait été examinée mais ne serait pas acceptée. J'ai vu que le dépôt principal [freeCodeCamp learn repository](https://github.com/freeCodeCamp/freeCodeCamp) utilisait une réponse similaire, alors j'ai voulu l'inclure dans le dépôt du Site de Quiz pour Développeurs. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-8.09.14-PM.png)

### Étape 6 : Ouverture des discussions GitHub

Quelques jours avant le début du Hacktoberfest, je voulais ouvrir une autre voie pour que les contributeurs puissent poser des questions et proposer de nouvelles fonctionnalités. J'ai donc décidé d'ouvrir les [discussions GitHub](https://docs.github.com/en/discussions).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-10-31-at-8.14.52-PM.png)

Lorsque j'ai créé ce post, quelques nouvelles personnes dans le dépôt se sont senties les bienvenues pour contribuer et étaient heureuses qu'il y ait un endroit pour se connecter avec moi et d'autres contributeurs. 

Maintenant que tout était en place, le compte à rebours pour le Hacktoberfest était en cours.

## Leçons apprises pendant le Hacktoberfest

Dès le premier jour, j'ai été assez occupé à examiner les pull requests et à aider les nouveaux contributeurs à se lancer dans l'open source. Mais toute l'expérience a été très éducative et gratifiante. 

Voici quelques leçons que j'ai apprises pendant cette période.

### Diriger avec patience, empathie et gentillesse

Nous avons tous été débutants un jour, et parfois, il est effrayant d'apprendre quelque chose de nouveau. J'ai veillé à diriger avec gentillesse et empathie parce que je me souviens de ce que c'était que de commencer dans l'open source. 

Chaque fois qu'une nouvelle question arrivait, je m'assurais de répondre et de fournir autant d'assistance que possible pour les aider à résoudre le problème. Cela a abouti à un environnement accueillant et sûr pour apprendre.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-01-at-6.25.48-PM.png)

Nous avons également eu des moments où certains contributeurs voulaient ajouter des questions de quiz mais étaient nerveux parce que l'anglais n'est pas leur langue maternelle. Mon travail était de les rassurer en leur disant que j'étais là pour les aider et non pour juger les erreurs d'orthographe ou de grammaire. 

Je crois que cela a aidé à obtenir un plus grand volume de questions de quiz.

### Ne pas se laisser submerger par le spam

L'un des inconvénients du Hacktoberfest est l'augmentation du nombre de pull requests de spam pour les mainteneurs de l'open source. Bien que cela soit frustrant à gérer, j'ai rapidement appris à simplement fermer la PR, à la labelliser comme spam et à passer à autre chose.

Il n'y avait aucun intérêt à argumenter avec eux ou à se mettre en colère car c'est une perte d'énergie. La majorité des gens voulaient contribuer de manière significative et c'est là que j'ai choisi de consacrer mon énergie.

### Comment fermer gracieusement les PR qui ne seront pas acceptées

L'un des problèmes surprenants qui est survenu était que des gens voulaient prendre des questions de quiz et des explications d'autres sites de quiz et les ajouter au [Site de Quiz pour Développeurs de freeCodeCamp](https://github.com/freeCodeCamp/Developer_Quiz_Site). Les premières fois que cela s'est produit, j'ai fermé la pull request et je leur ai fait savoir que c'était du plagiat et que nous ne pouvions pas accepter cela. 

Eh bien, j'ai reçu une réponse d'un contributeur disant qu'il ne s'en était pas rendu compte et qu'il voulait savoir s'il pouvait réessayer. Je lui ai assuré qu'il était libre de créer une nouvelle PR et que je pouvais l'aider avec l'orthographe ou la grammaire. 

Cela m'a amené à réviser ma réponse pour informer les contributeurs qu'ils n'étaient pas en difficulté et qu'ils étaient libres de contribuer à nouveau à l'avenir avec leurs propres questions.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-01-at-6.42.40-PM.png)

Cela a aidé à maintenir un environnement open source sain et la plupart de ces cas se sont avérés être des contributeurs prolifiques après avoir compris les règles. 

## Conclusion

Je suis vraiment heureux d'avoir participé en tant que mainteneur au Hacktoberfest de cette année. J'ai appris beaucoup de choses sur la communication, l'empathie, la patience et le leadership.

J'espère que mon article vous encouragera à vous impliquer dans l'open source, soit en tant que mainteneur ou contributeur à l'avenir.