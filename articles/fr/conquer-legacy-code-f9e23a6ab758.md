---
title: Comment maîtriser le code hérité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-01T03:47:46.000Z'
originalURL: https://freecodecamp.org/news/conquer-legacy-code-f9e23a6ab758
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sbh9nL_Q1pr5PcXnIdaicA.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment maîtriser le code hérité
seo_desc: 'At some point in your developer career, your boss will hand you a piece
  of legacy code — code that someone else wrote a long time ago. Your boss will tell
  you to learn this legacy code, fix it, and add new features to it.

  I’ve been in this situation ...'
---

À un moment donné dans votre carrière de développeur, votre patron vous remettra un morceau de code hérité — du code écrit par quelqu'un d'autre il y a longtemps. Votre patron vous demandera d'apprendre ce code hérité, de le corriger et d'y ajouter de nouvelles fonctionnalités.

J'ai été dans cette situation à de nombreuses reprises au cours des deux dernières décennies. Je peux vous aider.

#### Comment comprendre le code hérité

Si vous avez de la chance, vous aurez de la documentation, ou au moins des commentaires en ligne. Peut-être qu'un ou deux des auteurs originaux seront encore là pour vous aider. Mais la plupart du temps, vous n'aurez pas cette chance.

Parlons de ce que vous allez faire dans ces cas moins chanceux.

Tout d'abord, vous devez être humble. Respectez le code et les développeurs qui l'ont écrit.

Il est facile de regarder le travail qui vous précède et de décider qu'il n'est pas bon et que vous pouvez faire mieux. C'est la mauvaise attitude. Cela vous mènera sur un chemin très dangereux.

Si vous empruntez ce chemin dangereux, vous commencerez à faire des changements avant de bien comprendre l'impact de ces changements. Vous "corrigerez" des choses qui ne sont pas cassées, simplement parce qu'elles sont écrites dans un style que vous n'aimez pas, ou basées sur une ancienne façon de faire les choses. Finalement, vous perdrez un temps incroyable avec cette attitude.

Alors arrêtez. Prenez du recul et réalisez que tout dans cette base de code a été fait d'une certaine manière pour une raison.

Jusqu'à ce que vous connaissiez le code sur le bout des doigts, vous devez supposer qu'il y avait de bonnes raisons pour qu'il soit écrit de cette manière, et que vous ne les avez pas encore comprises.

C'est une attitude beaucoup plus productive, et elle vous évitera de tout casser, puis de vouloir sauter par la fenêtre quand vous ne pourrez pas tout remettre ensemble assez vite.

Ne faites pas un Humpty Dumpty de votre base de code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P7oCy28AjxYcIv8F_Wbo3w.gif)
_"Oui, donc cette 'correction rapide' du code hérité a en fait tout cassé et je ne sais pas pourquoi. Ciao !"_

La meilleure façon que j'ai trouvée pour apprendre une base de code est de commencer au niveau de l'interface utilisateur, puis de remonter dans le code.

Choisissez un seul flux utilisateur, comme se connecter, passer une commande, écrire un avis, ou ce qui est pertinent pour votre application particulière. Parcourez le flux en tant qu'utilisateur final. Ensuite, regardez le code, en commençant par le code de l'interface utilisateur — il devrait être le plus facile à reconnaître — et suivez chaque étape en arrière, jusqu'à la base de données.

Au fur et à mesure, dessinez un **diagramme de séquence** pour illustrer ce qui se passe. Si vous n'êtes pas sûr de ce qu'est un diagramme de séquence, ou comment en dessiner un, [consultez ce tutoriel gratuit.](http://www.newthinktank.com/2012/11/uml-2-0-sequence-diagrams/) Si vous n'avez pas un bon outil pour dessiner des UML, [en voici un gratuit.](https://www.visual-paradigm.com/solution/freeumltool/)

![Image](https://cdn-media-1.freecodecamp.org/images/0*OKAdzneO7BJkr_QW.)
_Exemple de diagramme de séquence UML. <br>source: [UML 2 Sequence Diagrams: An Agile Introduction](http://agilemodeling.com/artifacts/sequenceDiagram.htm" rel="noopener" target="_blank" title=")_

Une fois que vous avez terminé votre premier diagramme de séquence, en utilisant une copie locale de la base de code que vous pouvez facilement restaurer, commencez à apporter des modifications subtiles à certains des composants que vous avez rencontrés. Voyez si vous pouvez prédire les effets de vos modifications sur l'application. C'est un bon moyen de tester votre compréhension.

Continuez à répéter ce processus, en ajoutant à vos diagrammes jusqu'à ce que vous ayez une image complète de l'ensemble de l'application (ou au moins de toutes les parties dont vous êtes responsable).

Pour des points bonus, assurez-vous de partager vos notes et diagrammes. Placez-les dans un endroit bien visible où le prochain développeur qui viendra pourra facilement les découvrir. Ne vous inquiétez pas de les rendre parfaits, ou même jolis. Faites simplement ce que vous pouvez. Chaque petit détail aide.

Dans l'ensemble, la chose la plus importante est d'être patient et d'éviter de vous en vouloir. Le code est une chose complexe. Comprendre le code hérité prend du temps. Restez calme.

#### Comment corriger le code hérité

Le plus grand défi auquel vous serez confronté lors de la correction de code hérité est de décider jusqu'où aller avec votre correction. Je vous conseille vivement de faire d'abord le _changement viable minimum_. Cela signifie que vous devez faire le changement le moins perturbateur qui corrige complètement le problème avant d'essayer de nettoyer et de refactoriser le code.

Cela vous donne une issue de secours. Dans le pire des cas, si vous êtes appelé à traiter une autre priorité — ou si vous êtes sous un délai serré — au moins vous aurez assemblé un code fonctionnel sur lequel vous pourrez vous rabattre.

Une fois que vous avez fait fonctionner votre code, si vous avez encore du temps, vous pouvez commencer à faire des améliorations petites et incrémentielles.

Martin Fowler a rassemblé un catalogue de refactorisations qui vous donnera une bonne idée des types de changements que vous pouvez apporter pour améliorer progressivement une base de code. [Consultez-le ici](http://refactoring.com/catalog/). L'idée est de toujours laisser le code dans un meilleur état que lorsque vous l'avez trouvé.

Parfois, vous rencontrerez un bug qui est en fait le résultat d'un défaut structurel. Ces bugs ne peuvent pas être corrigés par un simple changement de logique conditionnelle. Ils nécessitent des changements plus invasifs.

C'est là que les choses se compliquent. Vous devez être brutalement honnête avec vous-même sur ce qu'est le changement viable minimum. Chaque fibre de votre être voudra décomposer le code et tout réécrire. Ne le faites pas !

Restez sur une correction rapide, suivie d'une amélioration incrémentielle qui le refactorise et le nettoie autant que le temps le permet. Votre objectif est simplement de rendre le code un peu meilleur à chaque fois. Plus vous maintenez la base de code longtemps, meilleure elle deviendra.

Pour que cette approche fonctionne vraiment, assurez-vous de toujours gonfler vos estimations pour permettre un peu de temps pour la refactorisation.

Parfois, les défauts structurels sont si graves qu'une stratégie de correction perpétuelle ne fonctionnera tout simplement pas. Cette situation est en fait beaucoup plus rare que vous ne le pensez.

Encore une fois, vous devez être brutalement honnête avec vous-même sur le coût/bénéfice d'une réécriture ou d'une reconception. Vous devez accepter que, finalement, ce sera une décision commerciale et non technique.

Préparez-vous à présenter votre cas en termes commerciaux. Quel sera le coût d'une restructuration majeure du code ? Quels sont les risques commerciaux réels de ne pas le faire ? Si vous avez un cas solide, vous serez éventuellement entendu. Ne soyez pas surpris si cela prend quelques cycles de correction supplémentaires d'abord, cependant.

Rappelez-vous : si vous faites une révision majeure, assurez-vous d'abord qu'il y a un soutien pour le changement et un budget raisonnable pour l'accompagner. N'essayez pas de voler sous le radar avec cela. À moins, bien sûr, que vous ne vous délectiez de conversations gênantes avec la direction lorsque vous commencez à casser des choses et à manquer des délais.

#### Comment ajouter de nouvelles fonctionnalités au code hérité

Enfin, vous serez éventuellement appelé à ajouter des fonctionnalités au code hérité. À ce stade, vous avez une décision importante à prendre. Allez-vous "suivre le flux" de la base de code actuelle, ou prendre les choses dans une nouvelle direction ?

Encore une fois, je vous conseille d'être brutalement honnête dans votre évaluation. Continuer à suivre les modèles et pratiques évidents dans la base de code existante la rendrait-elle pire, ou ajouterait-il à un problème existant ?

La plupart du temps, vous voudrez garder les choses stables. Faites simplement des ajouts incrémentiels en utilisant les modèles et pratiques existants du code. Réutilisez les éléments existants. Faites les changements les moins perturbateurs possibles, tout en faisant des améliorations petites et incrémentielles en nettoyant et en refactorisant.

Si vous pensez qu'une nouvelle direction est absolument nécessaire, alors vous devrez trouver un moyen d'isoler vos changements et de les coupler le plus faiblement possible à la base de code existante.

Essayez de découper la nouvelle fonctionnalité en tant que projet séparé. Vous pouvez ensuite exposer une API qui permet au code hérité de se brancher à votre nouveau code. Cela fait en sorte que votre nouveau code et l'ancien code hérité n'ont pas besoin de se connaître beaucoup.

Cela commence à devenir un peu délicat lorsque vous devez utiliser des fonctionnalités du code hérité afin d'implémenter la nouvelle fonctionnalité. La meilleure façon d'isoler l'ancien code du nouveau code est d'utiliser le modèle d'adaptateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mCss9lg7sm43hARTj3Jo3w.jpeg)
_Pas ce genre de modèle d'adaptateur (celui-ci ne fonctionnera pas, au cas où vous vous poseriez la question)_

[DO Factory](http://www.dofactory.com) a une bonne explication du modèle d'adaptateur :

> "Le modèle d'adaptateur traduit une interface (les propriétés et méthodes d'un objet) en une autre. Les adaptateurs permettent aux composants de programmation de travailler ensemble, ce qui autrement ne serait pas possible en raison d'interfaces incompatibles. Le modèle d'adaptateur est également appelé le modèle de wrapper.

> Un scénario où les adaptateurs sont couramment utilisés est lorsque de nouveaux composants doivent être intégrés et travailler ensemble avec des composants existants dans l'application.

> Un autre scénario est la refactorisation dans laquelle des parties du programme sont réécrites avec une interface améliorée, mais l'ancien code s'attend toujours à l'interface d'origine."

Voici quelques liens vers des explications et des exemples dans divers langages.

* [**JavaScript** exemple du modèle d'adaptateur](http://www.dofactory.com/javascript/adapter-design-pattern)
* [**C#** exemple du modèle d'adaptateur](http://www.dofactory.com/net/adapter-design-pattern)
* [**Java** exemple du modèle d'adaptateur](http://www.tutorialspoint.com/design_pattern/adapter_pattern.htm)

#### Points clés à retenir

En résumé, voici les points clés qui vous aideront à aborder et à maîtriser toute base de code :

1. Ne jugez jamais le code hérité ou ne le changez pas avant d'avoir pris le temps de le comprendre pleinement.
2. Les diagrammes de séquence sont vos amis.
3. Préférez les petites améliorations incrémentielles aux réécritures ou changements en gros.
4. Chaque changement devrait tenter de laisser le code un peu meilleur qu'il ne l'était lorsque vous l'avez trouvé.
5. Si vous devez faire des grands changements, faites un cas commercial et obtenez l'approbation d'abord.
6. Lorsque vous ajoutez de nouvelles fonctionnalités, essayez de "suivre le flux".
7. Si vous devez prendre le code dans une nouvelle direction, isolez vos changements et utilisez le modèle d'adaptateur pour l'intégrer.

J'espère que vous avez trouvé cet article utile. Ma mission est d'aider autant de développeurs que possible. Veuillez ❤️ recommander ❤️ cet article en utilisant le cœur vert ci-dessous pour aider à diffuser le message.

**Vous voulez coder mieux ?** Rejoignez des milliers de développeurs qui reçoivent des articles et des informations précieux comme celui-ci de ma part chaque semaine **gratuitement**. Il suffit de [cliquer ici.](https://devmastery.com/signup/index.html)