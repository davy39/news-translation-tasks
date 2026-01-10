---
title: Pourquoi j'ai changé ma façon de penser à la qualité du code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-19T23:18:01.000Z'
originalURL: https://freecodecamp.org/news/why-i-changed-the-way-i-think-about-code-quality-88c5d8d57e68
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mxwl0_gdFfhnpXeh8RozCA.jpeg
tags:
- name: Code Quality
  slug: code-quality
- name: code review
  slug: code-review
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Pourquoi j'ai changé ma façon de penser à la qualité du code
seo_desc: 'By John Cobb

  What do you think about when you think about code quality?

  Is it consistency? Enforcing a set of standards and best practices on your code
  through linter rules and formatters? How about ensuring your code has tests that
  run automatically...'
---

Par John Cobb

À quoi pensez-vous lorsque vous pensez à la qualité du code ?

Est-ce la cohérence ? L'application d'un ensemble de normes et de bonnes pratiques à votre code via des règles de linter et des formatteurs ? Ou peut-être garantir que votre code dispose de tests qui s'exécutent automatiquement pendant votre processus de build ? Qu'en est-il des pull requests et des revues de code — protéger votre branche master des commits directs et faire réviser votre code par vos pairs ?

Ce sont quelques-unes des choses qui me viennent à l'esprit. Des processus automatisés et des vérifications manuelles. Intelligents et efficaces. Pourtant, bien qu'ils soient tous utiles, ils ne traitent vraiment que la moitié du problème.

### Nous ne pouvons pas tout automatiser

L'automatisation est cruciale pour maintenir la qualité du code. L'analyse statique de votre syntaxe avec un linter et les tests automatisés devraient être obligatoires. Mais je peux écrire du code qui passe tous les processus automatisés sans aucune garantie de sa qualité réelle.

Le code suit-il des modèles établis ? Utilise-t-il des modules existants, ou duplique-t-il du code ? Tout est-il nommé de manière sensée ? Le code est-il au bon endroit dans la base de code ? Ce changement aura-t-il des implications plus larges et non intentionnelles ? Ce code traite-t-il ou résout-il vraiment ce qu'il est censé faire ? Fonctionne-t-il même ?

Les processus automatisés ne peuvent pas répondre à ces questions pour vous (pas encore). Si vous (ou un autre être humain) ne posez pas ces questions à propos de votre code, alors vous ne livrez probablement pas du code de _qualité_. C'est pourquoi nous avons des revues de code.

#### Une bonne revue de code devrait porter sur plus que le code

Bien sûr, une revue de code devrait porter sur le code (c'est même dans le nom après tout). Mais elle devrait aussi porter sur les questions plus larges posées ci-dessus, et aussi sur le produit final.

J'ai remarqué une tendance chez les développeurs à traiter les revues de code comme une formalité. Une vérification rudimentaire du code modifié. Un commentaire sur les erreurs évidentes (ou simplement pour chipoter un peu et avoir l'air occupé).

Cinq minutes, travail terminé. _Ça me semble bien_.

Mais le code qui ne répond pas aux exigences de la tâche n'est pas du code de qualité. Le code qui produit des erreurs de console ou des bugs visuels dans l'appareil/le navigateur n'est pas du code de qualité. Aucune de ces choses ne peut être détectée lors d'une revue de code superficielle. Vous ne pouvez pas réviser correctement le code à moins de _l'exécuter réellement_.

Je propose qu'une bonne revue de code _devrait_ impliquer au minimum :

* Récupérer la branche dans un environnement local.
* Construire le projet (et vérifier que le linter et les tests passent tous).
* Vérifier que le code s'exécute sans erreur dans les navigateurs/appareils cibles.
* Vérifier que le travail terminé correspond aux exigences de la tâche.

S'il y a des problèmes avec l'une de ces étapes, la pull request devrait être rejetée. Ne passez pas par la case départ. Ne collectez pas 200 $. Ne fusionnez pas avec master.

Les réviseurs devraient également utiliser la revue de code comme une opportunité pour poser des questions. Si vous ne comprenez pas le code, alors vous ne devriez pas approuver la pull request. Ne supposez pas que l'auteur en sait plus que vous — si cela n'a pas de sens pour vous, demandez des éclaircissements.

Le réviseur a une responsabilité égale à celle de l'auteur pour la qualité du code. C'est un état d'esprit essentiel pour maintenir la qualité du code.

Les revues de code complètes contribuent grandement à garantir la qualité du code. Mais il y a des étapes que vous pouvez suivre avant même d'ouvrir une pull request. De petites choses que vous pouvez faire pour améliorer la qualité de votre code et réduire l'effort nécessaire pour le réviser.

### Vérifiez vous-même que votre travail est complet

J'ai une habitude ennuyeuse. Lorsque j'ai fini d'écrire les dernières lignes de code pour une tâche, je coche mentalement la tâche comme _terminée_.

Si j'écoutais cette voix impatiente dans ma tête, je soumettrais ma pull request immédiatement. Mais ce code contiendrait probablement beaucoup, ou tous, des éléments suivants :

* Des exigences manquantes.
* Des cas de test manquants.
* Du code superflu, inutilisé ou en brouillon.
* Pas assez de commentaires dans le code.
* Des bugs visuels dans certains navigateurs/appareils.

Si l'un de ces éléments est vrai pour votre code, alors votre code n'est pas complet. Si l'un de ces éléments se retrouve dans la branche master, alors vous avez dégradé la qualité de la base de code.

Le point principal ici est le suivant : la qualité du code _commence_ avec l'auteur du code. Vous ne devriez pas compter sur les tâches automatisées, une revue de code, l'assurance qualité ou les tests d'acceptation utilisateur pour attraper vos erreurs.

La double vérification du travail pour s'assurer qu'il est complet est une première étape essentielle vers la qualité du code. C'est l'étape la plus facile à suivre, mais aussi la plus facile à ignorer.

Vous ne devriez ouvrir une pull request que lorsque vous êtes certain que votre code est complet.

### Effectuez une auto-révision de votre branche

Je suis toujours surpris du nombre de problèmes — ou d'opportunités pour affiner une solution — que je peux trouver dans mon propre code. Des problèmes et des opportunités qui ne deviennent visibles pour moi que lorsque je fais un pas en arrière et que je regarde mes changements de manière isolée.

Vous pouvez réviser votre travail et appliquer vos propres commentaires avant d'assigner un membre de l'équipe pour réviser votre travail. Vous pouvez également utiliser cette opportunité pour laisser des commentaires sur la pull request afin de clarifier quoi que ce soit pour le réviseur.

Prendre le temps de s'assurer que votre travail est complet, de corriger les erreurs évidentes ou d'évaluer votre solution, améliorera la qualité de votre code. Cela réduit également l'effort nécessaire pour le réviser.

Cela pourrait aussi vous éviter quelques embarrassements. Je sais que cela m'a évité des situations embarrassantes.

### Garantir la qualité du code devrait être une exigence inhérente à chaque tâche de développement

Vous pensez peut-être que cette approche ajoute du temps à la durée d'une tâche. Et vous avez raison, c'est le cas. Mais ce n'est pas une mauvaise chose.

L'efficacité est importante, mais la paresse et l'apathie sont nuisibles. L'apathie conduit à une base de code gonflée et incohérente. La paresse crée un backlog croissant de dettes techniques. Nous ne pouvons pas être passifs et maintenir la qualité du code. Cela nécessite du temps et des efforts.

Changer la culture autour de la qualité du code peut être difficile. Les chefs de projet et les propriétaires de produits ne se soucient généralement pas de la qualité du code — ils ont leurs propres préoccupations. Demander du temps supplémentaire pour les processus de qualité du code peut parfois tomber dans l'oreille d'un sourd. Cependant, maintenir la qualité du code ne devrait pas être considéré comme quelque chose d'_extra_ — cela devrait être une exigence inhérente à chaque tâche.

En tant que développeurs, si nous ne changeons pas la façon dont _nous_ pensons à la qualité du code, nous ne pouvons pas nous attendre à ce que quelqu'un d'autre le fasse.

Rien de ce dont j'ai parlé ici n'est particulièrement révolutionnaire, ni prescriptif. Toutes les équipes, lieux de travail ou projets ne sont pas les mêmes, et certains des points ci-dessus peuvent ne pas être applicables à vous.

Je crois qu'il y a souvent un écart entre la façon dont les développeurs pensent à la qualité du code et les actions réelles prises pour l'adresser. Si vous avez trouvé cela aussi, alors j'espère qu'il y a quelque chose que vous pouvez retenir de cet article — ou peut-être que vous avez déjà pris une approche différente pour l'adresser. J'adorerais entendre vos suggestions dans les commentaires.

Merci d'avoir lu !