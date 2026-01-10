---
title: Bonnes habitudes à avoir en tant que développeur aspirant/junior - et habitudes
  à éviter
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2019-09-13T10:36:36.000Z'
originalURL: https://freecodecamp.org/news/good-habits-to-have-as-an-aspiring-junior-developer-and-those-to-avoid
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/Good-habits-arrow-6x4.jpg
tags:
- name: best practices
  slug: best-practices
- name: coding
  slug: coding
- name: Habit Building
  slug: habit-building
seo_title: Bonnes habitudes à avoir en tant que développeur aspirant/junior - et habitudes
  à éviter
seo_desc: 'When you''re learning to code, it can be easy to pick up some nasty habits
  along the way. Here are some tips to avoid common bad habits, and the good habits
  to keep in mind.

  The good habits

  Let''s start with the positive shall we? These are the best ha...'
---

Lorsque vous apprenez à coder, il est facile de prendre de mauvaises habitudes en cours de route. Voici quelques conseils pour éviter les mauvaises habitudes courantes et les bonnes habitudes à garder à l'esprit.

## Les bonnes habitudes

Commençons par le positif, d'accord ? Ce sont les meilleures habitudes qui m'impressionnent souvent lorsque je travaille avec des développeurs juniors (et tous les développeurs, d'ailleurs).

## Commit/Push du code souvent

Il est probable que vous ayez rencontré des termes comme "Git", "GitHub", "source control" lors de votre parcours de codage. Si ce n'est pas le cas :

1) Où étiez-vous ?!?

2) Vous pouvez en apprendre davantage ici : [https://www.freecodecamp.org/news/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba/](https://www.freecodecamp.org/news/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba/)

Le contrôle de source est une chose merveilleuse. C'est une sauvegarde de votre code, il vous permet de suivre les changements et de revenir rapidement en arrière lorsque vous avez ce moment "oh m***! tout est cassé !" en codant.

Sans parler du fait qu'il rend la vie beaucoup, beaucoup plus facile lorsque vous travaillez en équipe. Je ne peux pas imaginer travailler sur du code de manière collaborative sans cela - partager du code par email et Slack ?! ***Frissons***.

Une bonne habitude à avoir est de **commiter le code souvent**, même pour vos propres projets secondaires comme pratique. Personnellement, j'aime "**check in**" mon code lorsque j'ai terminé une petite partie de mon projet. Par exemple, si je créais une application de liste de tâches, je commiterais et pousserais mon code lorsque j'aurais ajouté le '_bouton nouvelle tâche_', ou lorsque j'aurais terminé la '_fonctionnalité de case à cocher_'.

Il n'y a pas de règles strictes quant au moment de commiter le code. D'autres bons moments pour commiter le code sont :

* Si vous êtes sur le point de terminer pour la journée (voir une règle très importante ci-dessous)
* Avant de faire une refactorisation majeure ou un changement de code
* S'il y a un incendie dans le bâtiment (Je plaisante, la sécurité d'abord)

Il n'y a qu'une seule règle importante à suivre lors du commit de code.

> Le code doit se construire avec succès et les tests doivent passer

Cela compte-t-il comme 2 règles ? Peu importe, c'est important. Une chose qui est garantie de faire stopper n'importe quelle équipe de développement est le code cassé. Donc avant de commiter votre code, assurez-vous que le code se construit et que les tests passent !

Enfin, assurez-vous d'utiliser de **bons messages de commit**. "Corrigé un bug" n'est pas aussi clair que "Corrigé le problème avec le bouton 'save todo' qui n'appelait pas correctement la fonction onClick". Cela sera non seulement utile pour vous-même mais aussi pour vos coéquipiers.

## Utiliser des noms clairs pour les variables, fonctions et fichiers

Ah, le nommage. La seule chose dans le développement web que nous pensions tous facile, est parfois sournoisement difficile. Le nommage est important, car il rend notre code plus facile à lire et à comprendre.

Lorsque vous choisissez un nom pour vos variables, fonctions et fichiers, essayez de le rendre aussi descriptif que possible. Pourquoi ?

* Cela facilite la lecture rapide du code. Si vous voyez une méthode appelée `getUsers()`, sans avoir à regarder cette méthode, vous pouvez être assez sûr qu'elle va retourner une liste d'utilisateurs.
* Aide à renforcer la **séparation des préoccupations**. Oooh un nouveau terme fantaisiste ! Ne vous inquiétez pas, cela signifie simplement garder les choses liées ensemble. Par exemple, dans une application Node.js, si vous avez un endpoint `/users` et un endpoint `/products`, vous pourriez garder la logique `users` dans le même fichier (par exemple `usersService.js`) et garder la logique `products` dans un autre fichier. Cela ne rendrait-il pas plus facile de trouver les choses ?

Voici une fonction simple qui est mal nommée (comme les noms des paramètres) pouvez-vous deviner ce qu'elle fait ?

```js

const function1 = (x, y) => {
    return x + y
}

```

Cette fonction pourrait soit **ajouter 2 nombres**, soit **concaténer 2 chaînes**, mais son intention originale n'est pas claire. Disons que son intention était d'ajouter des nombres, mais qu'un autre développeur insoupçonné vient et l'utilise pour concaténer 2 chaînes. Cela pourrait être acceptable pour l'instant, mais plus tard, si nous refactorisons cette fonction pour _valider les nombres_, alors le code appelant cette fonction pour concaténer des chaînes se cassera. Oh non !

Voici la fonction avec un meilleur nommage :

```js

const addNumbers = (num1, num2) => {
    return num1 + num2
}

```

Maintenant, il est un peu plus clair ce que fait la fonction et ce que sont les paramètres.

## Pratiquer le débogage

Croiriez-vous que les développeurs web passent autant de temps (sinon plus) à corriger des bugs ? Oui, il y aura des bugs. Et la meilleure façon d'identifier et de corriger un bug est de **déboguer le code**. Le débogage est le processus de "parcours" de votre code, ligne par ligne, jusqu'à ce que vous découvriez quelque chose que vous n'attendiez pas.

Heureusement pour nous, les développeurs web, de nombreux IDE viennent avec des débogueurs intégrés qui rendent cela vraiment facile (voici un guide VS Code pour configurer le débogage pour différents langages. Pour d'autres IDE, vous pouvez consulter Google [https://code.visualstudio.com/docs/editor/debugging](https://code.visualstudio.com/docs/editor/debugging))

Alors, comment déboguer efficacement votre code ? Voici quelques conseils :

* **Reproduire le problème** - reproduisez le bug plusieurs fois pour comprendre exactement ce qui le cause
* **Réfléchir** - avant de plonger dans le code et de commencer à fouiller sans but, arrêtez-vous et réfléchissez. Pourquoi cela se produirait-il ? Quelles parties du code sont liées à cela ?
* **Investiguer le code** - une fois que vous avez une idée des parties du code que cela est susceptible d'affecter, commencez à creuser. Après avoir lu le code, vous pourriez repérer le problème. Hourra ! Si ce n'est pas le cas, il est temps de sortir le débogueur.
* **Déboguer** - Lancez le débogueur et parcourez le code ligne par ligne. Surveillez les valeurs des variables (et comment elles changent) et quelles fonctions sont appelées (et lesquelles ne le sont pas). Les bonnes branches d'une instruction `if` sont-elles appelées ? Les événements sont-ils déclenchés correctement ? Les calculs sont-ils effectués correctement ?

## Planifier avant de coder

Vous venez de vous réveiller après une bonne nuit de sommeil. Vous prenez votre petit-déjeuner et tout à coup une idée géniale de nouveau projet secondaire vous vient. Quelle idée fantastique ! Une révélation !

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-88.png)

Vous bondissez de votre chaise vers votre ordinateur portable, des cornflakes volant partout, et commencez à coder frénétiquement. (Ou est-ce juste moi ? OK, passons rapidement...)

Bien qu'il soit souvent tentant de sauter directement dans votre IDE et de commencer à coder, un peu de planification peut aller loin.

* Réduit la quantité de code "gâché"
* Réduit les changements de code
* Vous donne des objectifs solides à atteindre
* C'est une compétence impressionnante pour les développeurs juniors - cela montre votre pensée critique !

Je ne vais pas entrer dans trop de détails ici, car j'ai écrit un article plus complet sur ce sujet ici : **[Comment les développeurs pensent : Un aperçu de la planification et de la conception derrière une application web simple](https://www.freecodecamp.org/news/a-walk-through-the-developer-thought-process/)**

Voici un résumé rapide de l'article ci-dessus pour l'instant :

* "**Que fait-il ?**" - écrivez les fonctionnalités que vous voulez que votre application ait
* "**À quoi ressemble-t-il ?**" - faites un croquis rapide ou un wireframe de ce à quoi votre application devrait ressembler
* "**Comment positionner et styliser les éléments ?**" - une fois que vous avez vos wireframes, commencez à réfléchir à la façon dont vous allez positionner tout sur la page
* "**Comment se comporte-t-il ?**" - ensuite, commencez à réfléchir à la façon dont votre application se comporte. Réfléchissez aux fonctionnalités et à ce qui se passe lorsque l'utilisateur clique et agit
* "**À quoi ressemblera mon code ?**" - avec vos comportements et fonctionnalités en tête, commencez à planifier votre code. Quels composants allez-vous besoin ? Aurez-vous besoin de gestionnaires d'événements ? D'objets d'état ?
* "**Que dois-je tester ? Et ce qui peut mal tourner ?**" - réfléchissez aux tests, aux cas limites et aux parties de votre code qui pourraient mal tourner

## Les habitudes pas si bonnes

Maintenant, examinons quelques habitudes pas si bonnes qui sont faciles à prendre. Si vous en faites certaines maintenant, ne paniquez pas. Nous le faisons tous à un moment donné ! Avec un peu de pratique, vous pouvez les surmonter - et je vais vous donner quelques conseils sur la façon de le faire.

## Copier et coller du code aveuglément

Levez la main si vous avez déjà rencontré un problème ou si vous avez été bloqué en codant ? *_**lève la main**_.* Évidemment, nous rencontrons des problèmes tout le temps en codant. Cela fait partie du jeu et c'est notre travail de trouver comment surmonter ces problèmes.

La plupart du temps, nous avons recours à Google, StackOverflow, ou similaire à la recherche de réponses à nos problèmes. Maintenant, il n'y a rien de mal avec cette approche - on pourrait dire qu'elle devrait être encouragée car c'est l'une des meilleures/plus rapides façons pour un développeur de résoudre un problème lui-même.

Le problème est lorsque nous **copions/collons du code aveuglément sans le comprendre.**

> Mais si ça marche, quel est le problème ?!

Un point valable. Voici les raisons pour lesquelles cela peut causer des problèmes :

* Que se passe-t-il lorsque le code doit être changé ? Il sera difficile de changer le code que nous ne comprenons pas
* Si nous ne comprenons pas le code, comment pouvons-nous être sûrs qu'il résout vraiment le problème ?
* Pouvez-vous être sûr qu'il n'affecte pas d'autres parties de la base de code de manière négative ?

Alors, comment pouvons-nous éviter cela ?

* **Lire** - lisez-le ligne par ligne, et prenez le temps de comprendre le code
* **Taper** - tapez-le au lieu de copier et coller. Cela vous forera à lire/analyser chaque ligne au fur et à mesure que vous tapez

Il n'y a rien de mal à copier et coller, tant que nous comprenons exactement ce que fait le code. Si un développeur senior révise notre travail et que nous ne pouvons pas expliquer ce qui se passe parce que le code a été copié/collé, cela ne fera pas très bon effet.

## Ne pas écrire de tests

C'est probablement la pire habitude qui peut être prise en apprenant à coder. Beaucoup de tutoriels nous guident à travers le "**chemin heureux**" de la création d'une application, ce qui rend facile de négliger l'écriture de tests. Pourquoi les tests sont-ils si importants ?

* **Les tests prouvent que votre code fonctionne**. Personne ne peut argumenter sur le fonctionnement si le test passe !
* **Facilite la vérification que les nouvelles fonctionnalités n'ont rien cassé**. Pendant le codage, exécutez vos tests régulièrement. Quelques tests cassés ? **Vous savez tôt dans le processus de développement où les choses ont mal tourné.** Au lieu de le découvrir demain lorsque vous le rencontrez par accident
* **Une ceinture de sécurité pour la refactorisation.** Écrivez votre code. Écrivez vos tests. Refactorisez votre code. Exécutez les tests. Les tests passent ? Tout fonctionne encore, bons jours ! Maintenant, essayez de changer votre code sans avoir une suite de tests à exécuter. Comment pouvez-vous prouver que **_tout_** fonctionne comme il se doit ?

Alors assurez-vous de tester votre code. Vous n'avez pas à tester des choses comme de petits projets secondaires tout le temps, mais c'est bon de pratiquer de temps en temps. Lorsque vous obtenez un emploi, vous viserez à avoir une couverture de test pour la plupart de vos fonctionnalités. Pratiquez ces tests !

Il existe de nombreux excellents tutoriels sur la façon de tester votre code, selon vos projets actuels et votre stack technique, essayez de chercher sur Google "testing with {insert language}" ou "How to test {insert language} apps". [Voici un bon aperçu des tests JavaScript](https://medium.com/welldone-software/an-overview-of-javascript-testing-in-2019-264e19514d0a).

## Oublier la documentation

Documentation. Le "ruban rouge" ennuyeux qui accompagne tous les projets. Comme quelqu'un l'a dit un jour :

> Tous les développeurs détestent l'écrire, mais tous les développeurs la veulent

Ce qui est vrai. Êtes-vous déjà retourné à un ancien projet secondaire et avez oublié ce qu'il faisait ? Combien plus difficile serait-ce si vous essayiez d'utiliser une bibliothèque tierce et qu'il n'y avait aucune documentation pour expliquer comment elle fonctionnait ? Cela devient particulièrement plus apparent lorsque vous travaillez dans une grande entreprise de produits. Et si une autre équipe devait s'intégrer avec votre code, mais n'était pas sûre de l'API ?

C'est important, alors voici quelques conseils à pratiquer :

* README - GitHub vous permet d'ajouter un readme à votre projet. C'est l'endroit parfait pour stocker la documentation du projet, car il est facile à trouver
* Inclure ce que fait l'application et comment l'exécuter - Cela donne au lecteur un bon point de départ
* Expliquer d'autres "choses importantes" - telles que la logique compliquée, les bibliothèques et API tierces, ou les paramètres de configuration

---

### **Merci d'avoir lu ! Vous voulez plus d'articles comme celui-ci ?**

Espérons que cela vous a donné un aperçu de la création de bonnes habitudes de codage. Si vous souhaitez être informé lorsque je publie plus d'articles comme celui-ci, n'hésitez pas à rejoindre la liste de diffusion sur [chrisblakely.dev](https://www.chrisblakely.dev/#sign-up) ! Ou contactez-moi sur [Twitter](https://twitter.com/chrisblakely01) si vous avez envie de discuter :)