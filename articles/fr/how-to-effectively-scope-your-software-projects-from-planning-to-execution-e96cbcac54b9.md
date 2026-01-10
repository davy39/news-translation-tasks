---
title: Comment définir efficacement la portée de vos projets logiciels
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T14:32:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-effectively-scope-your-software-projects-from-planning-to-execution-e96cbcac54b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7T526d-xon76QBW8rjX4sQ.jpeg
tags:
- name: agile
  slug: agile
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment définir efficacement la portée de vos projets logiciels
seo_desc: 'By Angela Zhang

  Since starting my career as a software engineer, I’ve learned that scoping is one
  of the hardest things to get right. Unfortunately, CS programs in universities don’t
  really teach you how to scope projects. So here’s my attempt at con...'
---

Par Angela Zhang

Depuis le début de ma carrière en tant qu'ingénieure logicielle, j'ai appris que la définition de la portée est l'une des choses les plus difficiles à bien faire. Malheureusement, les programmes d'informatique à l'université n'enseignent pas vraiment comment définir la portée des projets. Voici donc ma tentative de consolider ce que j'ai appris sur ce sujet.

La définition de la portée n'est pas quelque chose sur lequel vous pouvez passer une journée pendant le projet et ne plus jamais y penser. En fait, pour définir avec précision la portée d'un projet, vous devez prêter attention tout au long du projet pendant :

1. La phase de planification : les premières étapes de la définition du projet et de ses objectifs
2. La phase de définition de la portée : le moment où la plupart des gens pensent à la définition de la portée. C'est ici que vous essayez de lister le travail à faire étant donné les objectifs du projet, et d'estimer combien de temps sera nécessaire pour les accomplir.
3. La phase d'exécution : lorsque vous implémentez réellement le projet.

#### **La phase de planification**

L'une des choses les plus importantes à faire pendant cette période est de **définir des objectifs très spécifiques pour le projet**. Par exemple, au lieu de "améliorer X pour le rendre plus scalable et performant", un objectif meilleur et plus spécifique pourrait être de "améliorer X en ajoutant des tests unitaires, en supportant 20K requêtes par seconde, et en réduisant la moyenne plafonnée de la latence utilisateur à <= 200ms".

Avoir des objectifs très spécifiques vous permet de couper sans pitié tout ce qui ne contribue pas à ces objectifs, afin de ne pas souffrir de [l'inflation des fonctionnalités](https://en.wikipedia.org/wiki/Feature_creep). Dans cette optique, vous pourriez également envisager de définir explicitement des **anti-objectifs**, et de séparer les **indispensables** et les **agréables à avoir**.

**Minimisez la taille des lots du projet** en (1) établissant des jalons et des points de contrôle clairs pour le projet, et (2) en facilitant le lancement d'une seule partie du projet. Non seulement cela aide à décomposer le projet, mais cela permettra également à l'équipe de pause ou de couper le projet tôt si une autre tâche, de priorité plus élevée, survient.

**Réduisez les risques du projet dès que possible**. Deux moyens courants de réduire les risques d'un projet incluent (1) travailler sur les parties les plus risquées en premier, et (2) prototyper les parties les plus risquées en utilisant des données factices et/ou des échafaudages. Chaque fois qu'un nouveau système open-source ou un service externe est utilisé, cela représente généralement un grand risque.

N'optimisez pas pour la quantité totale de travail effectué. Au lieu de cela, **optimisez pour la quantité totale d'impact sur le temps**. Une fois que vous avez surmonté la partie la plus risquée, priorisez le travail sur la partie du projet qui entraînerait la plus grande quantité d'impact immédiatement.

Voici une façon de penser à cela : tracez l'impact d'un projet sur le temps, où l'axe Y est l'impact, et l'axe X est le temps. Au début du projet, l'impact est de 0 %, et à la fin du projet, l'impact est de 100 %. Vous voulez maximiser la surface sous la courbe en faisant d'abord les tâches à haut retour sur investissement.

Essayez d'**éviter de réécrire de grands systèmes à partir de zéro autant que possible**. Lors d'une réécriture, nous avons tendance à (1) sous-estimer la quantité de travail que cela représenterait, (2) être tenté d'ajouter de nouvelles fonctionnalités et améliorations, et (3) construire un système trop compliqué parce que nous sommes trop concentrés sur toutes les lacunes du premier système.

Au lieu de faire une grande réécriture, envisagez de remplacer progressivement les sous-systèmes. Ayez de bonnes couches d'abstraction qui supportent le remplacement d'une partie de l'ancien système à la fois, afin de ne pas avoir à attendre que tout soit terminé pour tester le nouveau système.

#### **La phase de définition de la portée**

* Seuls les **ingénieurs écrivant le code doivent être ceux qui définissent la portée** des tâches. Pas leurs managers, pas le chef de produit, ni les parties prenantes clés de l'entreprise.
* **Résistez à la tentation de sous-estimer la portée**. Soyez honnête sur la durée des tâches, pas sur la durée que vous ou quelqu'un d'autre (comme votre manager ou l'équipe Go To Market) souhaite qu'elles prennent.
* **Divisez le projet en petites tâches, chacune prenant deux jours ou moins**. Lorsque vous avez des tâches dont la portée est "**environ 1 semaine**", elles finissent souvent par prendre plus de temps parce que vous n'avez pas énuméré toutes les sous-tâches que vous pourriez devoir faire.
* Définissez des **jalons mesurables** pour atteindre l'objectif du projet. Planifiez chacun avec une date de calendrier spécifique représentant quand vous attendez que ce jalon soit atteint. Ensuite, établissez une sorte de responsabilité externe sur ces jalons en, par exemple, les engageant auprès de votre manager et en mettant en place des vérifications de jalons.
* **Pensez aux estimations de temps de projet comme à des distributions de probabilité**, pas à des scénarios optimistes. Au lieu de dire à quelqu'un qu'une fonctionnalité sera terminée en 6 semaines, dites-lui quelque chose comme "il y a 50 % de chances de terminer la fonctionnalité en 4 semaines, et 90 % de chances que nous la terminions en 8 semaines". Cela tend à forcer les gens à être plus réalistes.
* **Ajoutez une marge** pour tenir compte de : (1) Le temps de développement != temps de calendrier, en raison des réunions, des entretiens et des vacances. Je multiplie généralement le temps de développement par 1,5 pour obtenir le temps de calendrier. (2) Le temps des tâches de projet imprévues, car il y a toujours des tâches que vous n'avez pas réalisées devoir faire jusqu'à beaucoup plus tard, comme la refactorisation de l'ancien code, le débogage de comportements apparemment inexplicables, l'ajout de tests. Plus vous êtes expérimenté dans la définition de la portée, plus ce multiplicateur sera petit.
* **Utilisez des données historiques**. Gardez une trace de si vous avez tendance à surestimer ou sous-estimer les projets dans le passé (la plupart des gens ont tendance à sous-estimer). Ajustez votre définition de la portée en conséquence.
* Gardez à l'esprit que **2X le nombre de personnes ne signifie pas 1/2X le temps de développement**, en raison des frais généraux de communication, du temps de montée en puissance, etc.
* Envisagez de **limiter dans le temps les parties ouvertes du projet**. Au lieu de "trouver le meilleur framework de traitement de flux pour ce système", ce qui peut prendre des mois de recherche et de prototypage, limitez-le à "trouver un framework de traitement de flux adapté en une semaine". Utilisez votre jugement ici pour équilibrer cela contre l'incurrence de frais généraux opérationnels à long terme.

#### **La phase d'exécution**

**Redéfinissez régulièrement la portée** pendant l'exécution du projet. Pour chaque tâche, suivez combien de temps vous avez estimé que la tâche prendrait, puis combien de temps elle vous a réellement pris pour la compléter. Faites cela pour chaque jalon mesurable. Si votre définition de la portée est décalée de 50 % pour les premières parties du projet, il y a des chances que votre définition de la portée soit également décalée de 50 % pour le reste du projet.

**Utilisez les jalons pour répondre à la question "comment avance le projet ?"** En tant qu'ingénieurs, il est tentant de répondre "ce sera fait d'ici la semaine prochaine" ou "jusqu'à la fin de ce mois". Mais ces types de réponses vagues tendent à créer des projets qui sont _toujours_ à 2 semaines d'être terminés. Au lieu de cela, utilisez les jalons (redéfinis) pour donner une réponse concrète basée sur la quantité de travail restant.

Si le projet prend du retard, assurez-vous que tout le monde comprend pourquoi le projet a pris du retard. Ensuite, **développez une version réaliste et révisée du plan de projet**. Abandonner le projet ou le raccourcir est une option potentielle qui devrait être considérée. Lisez plus sur [L'erreur des coûts irrécupérables](https://youarenotsosmart.com/2011/03/25/the-sunk-cost-fallacy/) si vous êtes curieux de savoir pourquoi les gens tendent à être biaisés contre l'abandon d'un projet à mi-chemin.

Donnant le crédit là où il est dû, beaucoup d'informations ici proviennent de discussions avec des ingénieurs et des managers comme [Spencer Chan](https://www.quora.com/profile/Spencer-Chan) et [Nikhil Garg](https://www.quora.com/profile/Nikhil-Garg), de la lecture de livres comme [The Effective Engineer](https://www.effectiveengineer.com/book) par [Edmond Lau](https://www.quora.com/profile/Edmond-Lau), et de la définition personnelle de la portée de nombreux projets avec divers degrés de précision.

Enfin, si je suis honnête, je ne suis en aucun cas une experte en définition de la portée et je fais encore régulièrement des erreurs comme ne pas suivre certaines des meilleures pratiques ci-dessus. J'ai simplement pensé que je documenterais mes apprentissages jusqu'à présent afin de pouvoir m'y référer à l'avenir.

Si vous aimez cet article, [suivez-moi sur Twitter](https://www.twitter.com/zhangelaz) pour plus de contenu sur l'ingénierie, les processus et les systèmes backend.