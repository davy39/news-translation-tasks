---
title: Comment Contribuer à un Dépôt Open Source
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-10-10T21:17:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-contribute-to-an-open-source-repository
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/0_x4Fcx54jFku92uw-.jpeg
tags:
- name: open source
  slug: open-source
- name: Tutorial
  slug: tutorial
seo_title: Comment Contribuer à un Dépôt Open Source
seo_desc: 'If you are reading this, it can be safely assumed you have heard about
  Git.

  Under your belt you have created a branch or two, you know your way around writing
  a decent commit message and you understand the basics of pulling and pushing commits
  to a b...'
---

Si vous lisez ceci, on peut supposer en toute sécurité que vous avez entendu parler de Git.

Vous avez déjà créé une ou deux branches, vous savez comment écrire un message de commit décent et vous comprenez les bases de la récupération et de l'envoi de commits vers une branche.

Si tout ce jargon vous semble pratiquement du charabia, je vous recommande vivement d'aller lire les bases fondamentales de [Git](https://git-scm.com/doc).

Je peux aussi supposer que vous lisez cet article pour l'une des deux raisons suivantes :

1. Vous voulez aider les autres et êtes une personne vraiment altruiste
2. Vous voulez rendre votre CV plus impressionnant

Les deux raisons sont valables et, après tout, si en aidant les autres vous vous aidez aussi vous-même, où est le mal, n'est-ce pas ?

# Pourquoi Contribuer ?

Si vous n'êtes pas encore convaincu des raisons pour lesquelles vous **devriez** contribuer à d'autres dépôts, laissez-moi vous présenter quelques preuves solides en faveur de cette démarche. En contribuant à un projet open source :

* Vous apprendrez à gérer du code et à communiquer avec d'autres personnes
* Vous serez perçu comme quelqu'un de proactif et passionné par la programmation
* Vous vous exposerez à diverses technologies et méthodologies de code différentes

# Par Où Commencer

Se lancer dans un dépôt peut sembler intimidant, car chaque projet peut différer en termes d'échelle et de langage de programmation. De plus, chaque projet peut avoir des règles et des directives spécifiques pour les contributeurs. Afin de faciliter votre transition vers le rôle de contributeur, voici quelques suggestions :

1. Ne vous lancez pas tête baissée dans un projet écrit dans un langage de programmation que vous ne maîtrisez pas. Choisissez un dépôt où vous comprenez les tenants et les aboutissants du langage de programmation
2. La plupart des dépôts open source manquent de documentation. Un point d'entrée facile peut être d'éditer la documentation existante ou d'aider à en créer une pour le projet
3. Les dépôts open source qui ont besoin d'aide ont une étiquette spéciale placée sur les problèmes, **« help wanted »**. Plus important encore, les problèmes que vous avez le plus de chances d'être équipé pour gérer sont ceux étiquetés **« first timers welcome »**
4. **N'ayez pas peur de poser des questions**. Si l'environnement de développement nécessaire pour exécuter le projet ne fonctionne pas correctement pour vous, faites-le savoir à quelqu'un. Si vous n'êtes pas sûr de la manière de corriger le problème ou si votre correction est la bonne approche, publiez un commentaire
5. Si vous vous sentez moins à l'aise pour traiter un problème, vous pouvez toujours parcourir les projets et ouvrir des problèmes pour eux

## Le Cycle de Contribution Git

Une fois que vous avez choisi un problème à résoudre et que vous avez informé les membres du projet que vous traitez ce problème, il est temps de faire un peu de travail. Tout d'abord, vous devrez **forker** le dépôt.

Cela peut être fait en cliquant sur le bouton fork qui est présent en haut à droite de chaque dépôt. Cela créera une copie du dépôt dans votre compte GitHub. Ensuite, vous devrez **cloner** le projet de votre compte sur votre machine, afin d'avoir une copie locale du projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_U1es19VPq8v_lYTzV0H6Rw-1.jpeg)

Une fois que vous avez réussi, **assurez-vous de configurer l'environnement de développement exactement comme indiqué dans le fichier readme du projet**. Lorsque l'environnement est prêt, vous pouvez créer une branche pour le problème que vous corrigez. La convention la plus courante pour le nom d'une branche peut être soit au format **« fix/issue-that-is-going-to-be-fixed »** soit **« feature/issue-that-is-going-to-be-fixed »**. Ensuite, faites les changements nécessaires pour résoudre le problème et validez-les. Assurez-vous de fournir un message de commit descriptif. Certains dépôts ont des directives à ce sujet également, alors assurez-vous d'en être conscient ou votre future pull request sera rejetée.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_bG7DQNZxp_ymHwX3jt3_rg.jpeg)

Il reste à **pousser votre commit** dans votre branche locale. Ensuite, si vous allez dans le dépôt à l'intérieur de votre compte GitHub, vous verrez en haut de la page une notification détaillant votre push vers votre branche avec un bouton étiqueté **« compare & pull request »**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_31pAY_CJvx5f2PR6SSpmFg.jpeg)

En cliquant sur le bouton, vous serez redirigé vers une page où vous pourrez ouvrir une pull request pour le propriétaire du dépôt. Il est d'usage de détailler les changements que vous avez apportés et de lier le problème que cette pull request résout. Une fois que vous avez tout rempli, vous pouvez cliquer sur le bouton étiqueté **« Create pull request »**.

Une fois vos changements approuvés, vous pouvez supprimer la branche sur laquelle vous travailliez.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_qQJz_PNuqGqjZ7IAyI5kFg.jpeg)

## Forker → Cloner → Commiter → Répéter

C'est tout ! Le processus a une légère courbe d'apprentissage, mais une fois fait correctement, vous vous y habituerez.

**Où allez-vous à partir de là ?** Eh bien, il existe une pléthore de [dépôts](https://github.com/search?q=first-contributions) qui vous permettent de simuler ce cycle complet.

Une fois que vous vous sentez suffisamment confiant, vous pouvez [rechercher](https://findanissue.com/) des dépôts auxquels contribuer.

Qu'attendez-vous ? Commencez à contribuer.