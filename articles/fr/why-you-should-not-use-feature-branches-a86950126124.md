---
title: Pourquoi vous ne devriez pas utiliser de branches de fonctionnalités (longues)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-30T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-not-use-feature-branches-a86950126124
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iBt55gRsIwnNX3D_9uJVTA.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: Git
  slug: git
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Pourquoi vous ne devriez pas utiliser de branches de fonctionnalités (longues)
seo_desc: 'By Jean-Paul Delimat

  Isn’t the git history in the picture above nice to work with? There are probably
  many problems in that repository, but one of them is most definitely the use of
  feature branches. Let’s see how such a bad thing became such a commo...'
---

Par Jean-Paul Delimat

Le historique git dans l'image ci-dessus n'est-il pas agréable à utiliser ? Il y a probablement de nombreux problèmes dans ce dépôt, mais l'un d'eux est certainement l'utilisation de branches de fonctionnalités. Voyons comment une telle mauvaise pratique est devenue si courante.

Lorsque git est venu remplacer SVN, il a apporté une méthode ridiculement facile pour créer des branches.

> _L'idée derrière git est de faciliter votre travail en tant que développeur travaillant sur plusieurs fonctionnalités en même temps. Pas de pousser des branches partout et de les lier à l'ensemble du processus de développement de votre équipe._

Lorsque JIRA et d'autres sont arrivés, des entreprises comme Atlassian ont commencé à promouvoir le "workflow git" et les branches de fonctionnalités. Le bouton "Créer une branche" est apparu dans vos tâches JIRA et boom, les branches de fonctionnalités sont nées ! Atlassian vous explique tout cela dans [cet article intéressant](https://www.atlassian.com/agile/software-development/branching). J'aime beaucoup les produits d'Atlassian. Gardez à l'esprit cependant que leur activité principale est la gestion des tâches pour les équipes de développement. Plus c'est enchevêtré avec des branches et du code, mieux c'est.

Dix ans plus tard, les branches de fonctionnalités sont une norme dans la plupart des équipes, alors qu'en fait elles n'apportent aucun bénéfice à votre objectif final : livrer un logiciel de qualité en production. Non seulement les branches de fonctionnalités n'apportent aucun bénéfice, mais elles vous ralentissent !

Pour plus de clarté : cet article suppose qu'une branche de fonctionnalités portera l'ensemble de la fonctionnalité que vous développez et qu'il s'agit d'une branche de fonctionnalités dite "longue" qui durera 1 semaine ou plus. Ce n'est pas un mantra "pas de branches du tout".

> "La fonctionnalité est prête. Je dois juste la fusionner !"

J'ai entendu cela bien trop souvent. Cela relève de la même catégorie que les déclarations comme "Ça compile donc ça marche".

En pratique, la fusion conduit au "syndrome de livraison imprévisible". Cela peut être rapide ou révéler une incompatibilité majeure, qui doit être corrigée dans l'urgence. Vous avez soit de la chance, soit... votre calendrier est décalé et la qualité du code diminue.

> _Le vrai problème avec les branches de fonctionnalités est la raison pour laquelle elles sont si populaires : elles flattent l'ego du développeur et vous font vous sentir bien dans votre travail._

Votre branche de fonctionnalités est votre propre jardin parfait et vous pouvez le garder propre et brillant. Mais il est séparé des autres jardins de votre équipe. Plus vous travaillez séparément, plus il est difficile de réconcilier.

Je suis un grand fan du livre de management "Le but". Il montre comment, avec le temps, les gens tendent à utiliser des métriques qui mettent en avant les optimums locaux d'un processus parce que c'est plus confortable. Ils perdent simplement de vue leur objectif global. Le livre parle d'une usine de production, mais l'analogie tient. Votre branche de fonctionnalités est un optimum local avec un code de haute qualité. Elle peut aussi être si éloignée de la branche principale qu'elle est inutile pour la prochaine version.

### Le développement basé sur le tronc à la rescousse

Comme le suggère le nom, dans le développement basé sur le tronc, toute l'équipe pousse continuellement vers la branche principale ou utilise des branches très courtes (1 ou 2 jours maximum).

Voici une [description détaillée](https://trunkbaseddevelopment.com/) de l'idée. Je n'ai aucun lien avec le site web lié. C'est juste un excellent aperçu du concept.

Lorsque vous poussez votre travail vers la branche principale à chaque push, la quantité de code à fusionner est bien plus petite et cela devient trivial. Il y a un bénéfice bien plus grand cependant : vous et votre équipe pouvez repérer les problèmes avant qu'ils ne deviennent douloureux. Il se peut que votre refactorisation entre en conflit avec une autre fonctionnalité. Ou vous vous éloignez des conventions du projet ou des motifs d'architecture. C'est là la vraie valeur du processus. Comme je le prêche dans chaque endroit où je me trouve :

> _C'est le travail d'équipe qui fait ou défait les projets logiciels._

Travailler des jours sur du code qui n'arrivera jamais à temps pour la version est le plus grand échec qu'une équipe puisse connaître.

Un autre avantage de pousser vers la branche principale est que vos changements s'exécuteront en direct dans un environnement. Il est toujours bon de déployer et de tester votre code, même en cours de développement, dans un vrai déploiement.

#### Objection 1 : "WIP" dans la branche principale !!!

Si vous avez lu jusqu'ici, vous pensez probablement "C'est fou, comment puis-je pousser mon travail à moitié terminé vers la branche principale alors qu'il sera probablement déployé en production très bientôt !!!".

Voici les objections courantes que l'on pourrait avoir et une solution tentante.

#### Objection 2 : Je ne peux pas exposer un travail non terminé !

Utilisez des bascules de fonctionnalités. Elles peuvent être des variables d'environnement ou tout ce qui vous convient le mieux pour activer et désactiver votre travail en cours. Rendez-le défensif bien sûr pour que votre code à moitié terminé ne s'active pas en production par erreur.

Toute votre équipe adorera cela : vous pouvez activer le code sur n'importe quel environnement à tout moment pour voir à quoi il ressemble ou comment il performe. Les testeurs peuvent se préparer à tester tôt. Les propriétaires de produits peuvent commenter votre travail en cours de route. Tout est en direct et facile d'accès pour tout le monde ! Si votre travail vient de commencer, cela apporte peu de valeur. Mais le diable se cache dans les détails. Il faut généralement la moitié du temps pour atteindre 90 % d'achèvement et une autre moitié pour terminer les 10 % restants. Partager votre travail dans cet état d'achèvement à 90 % est toujours une bonne idée ;)

Une autre chose qui vient gratuitement : vous pouvez désactiver la fonctionnalité en production si un problème survient après le déploiement. Après quelques jours ou semaines, une fois que la fonctionnalité tourne sans problème, supprimez simplement la bascule du code.

#### Objection 3 : Et si je casse la branche principale pour tout le monde ?

Nous sommes en 2019. Si vous n'avez pas une configuration d'intégration continue qui construit et exécute des tests automatiquement... alors configurez-la hier. Si vous cassez quelque chose, vous serez averti avant que cela ne devienne un problème pour toute l'équipe.

Dans le développement basé sur le tronc pur, le feedback viendra après la fusion et devra être corrigé immédiatement. Si vous utilisez des branches courtes, la fusion devrait être bloquée par votre outil CI. Une branche courte est quelque chose qui devrait durer 1 ou 2 jours maximum et porter un morceau de code cohérent qui contribue à la fonctionnalité que vous construisez.

#### Objection 4 : Il doit y avoir une revue de code avant de fusionner !

C'est un point valable. Les revues de code n'ont pas besoin de branches de fonctionnalités cependant. Si la culture de la revue de code est forte dans votre équipe, elle peut très bien être faite sur le commit vers la branche principale. Le relecteur s'arrêterait chez l'auteur du commit et discuterait de ce qui doit être corrigé. La correction viendrait dans un autre commit. Encore mieux, faites la revue de code ensemble avant de pousser le commit en premier lieu.

Si ce n'est pas acceptable pour votre équipe d'avoir des revues de code post-fusion (parce que soyons honnêtes, c'est moins pratique car les outils ne le supportent pas vraiment), utilisez des branches courtes et appliquez votre processus de revue de code là.

#### Objection 5 : **Je veux voir le code lié à une tâche**

Si vous avez une branche donnée par fonctionnalité, il est facile de suivre le code jusqu'à votre tableau agile. Vous pouvez naviguer d'une tâche à la branche qui l'implémente.

Cela semble cool, alors qu'en réalité, c'est inutile ! Combien de personnes pouvez-vous avoir dans une équipe agile ? Jusqu'à 5 ? Jusqu'à 10 ? À quel point est-il difficile de demander à la personne qui exécute une tâche ou une histoire quels commits vous devez regarder pour plonger dans l'implémentation ?

Après un certain temps, une fois les tâches terminées depuis longtemps, lier les tâches au code n'a plus de sens. Les développeurs s'appuient sur git blame pour savoir qui, sur le contenu du code pour savoir comment, et espérons-le sur les commentaires pour savoir pourquoi.

### La cerise sur le gâteau : l'opt-in sur les nouvelles fonctionnalités

Il est devenu courant de voir des fonctionnalités ou mises à jour majeures de l'UI publiées en utilisant une approche "opt-in". Github, Bitbucket, Gmail, ... pour n'en nommer que quelques-uns.

Le concept est que les changements majeurs sont introduits en utilisant une bannière "Hey, nous avons cette nouvelle fonctionnalité / tableau de bord amélioré / peu importe. Cliquez ici pour l'essayer". Vous pouvez opter pour, et généralement vous désister aussi facilement si vous n'aimez pas le changement. C'est une très bonne stratégie de test d'adoption car elle implique les utilisateurs finaux dans le processus de décision. Si les gens optent pour et restent là, cela signifie que vous améliorez l'expérience. S'ils optent pour et se désistent... vous savez que vous avez changé les choses pour le pire.

Si vous utilisez des bascules de fonctionnalités dès le départ, les exposer sur une base par utilisateur à l'exécution devient très facile.

### Conclusion

Si vous n'avez jamais pensé au développement basé sur le tronc comme une alternative au mantra des branches de fonctionnalités, j'espère que cet article vous a donné une certaine perspective et que vous essaierez.

Le meilleur, c'est que pour y parvenir, vous devrez configurer ou améliorer tous les autres aspects de votre processus (CI, tests automatisés, revues de code). C'est un bon chemin à prendre. Nous recommandons évidemment Fire CI comme [outil d'intégration continue](https://fire.ci/).

Rappelez-vous que votre objectif final est de mettre un logiciel de qualité devant vos utilisateurs. Plus votre code est proche de l'environnement de production à tout moment, mieux c'est.

Maintenant, bien que l'article soit très orienté "développement basé sur le tronc", notez qu'il ne s'agit peut-être pas d'une approche valable pour votre équipe.

Si votre équipe est très distribuée, dans différents fuseaux horaires, compte de nombreux développeurs juniors qui doivent apprendre les conventions et l'architecture du projet, l'utilisation de branches de fonctionnalités plus longues peut mieux fonctionner.

L'idée principale de cet article est :

**Plus vous intégrez rapidement les différentes pièces ensemble et vérifiez que tout fonctionne, plus vous êtes en sécurité pour avoir un produit fonctionnel à la fin.**

Un bon terrain d'entente est d'utiliser des branches courtes qui durent 1 ou 2 jours maximum et de les fusionner dans la branche principale. De cette façon, vous pouvez contrôler humainement ce qui entre et intégrer rapidement le code.

**Merci d'avoir lu ! Si vous trouvez l'article utile, cliquez sur le bouton d'applaudissements ci-dessous. Cela signifierait beaucoup pour moi et cela aide d'autres personnes à voir l'histoire !**

_Publié à l'origine sur [fire.ci](https://fire.ci/blog/why-you-should-not-use-feature-branches/) le 30 mars 2019._