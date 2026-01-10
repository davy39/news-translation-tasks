---
title: Les méthodes apply, call et bind de JavaScript expliquées en organisant un
  barbecue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-30T01:00:42.000Z'
originalURL: https://freecodecamp.org/news/javascripts-apply-call-and-bind-explained-by-hosting-a-cookout-84b85977ee11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FHLfdvXWAWi0HEBC83P8nw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Les méthodes apply, call et bind de JavaScript expliquées en organisant
  un barbecue
seo_desc: 'By Kevin Kononenko

  If you have ever been in charge of operating the grill at a family event or party,
  then you can understand apply, call and bind in JavaScript.

  If you want to write clear code that you (or a teammate) can re-read at a later
  date, he...'
---

Par Kevin Kononenko

**Si vous avez déjà été responsable du grill lors d'un événement familial ou d'une fête, alors vous pouvez comprendre apply, call et bind en JavaScript.**

Si vous souhaitez écrire un code clair que vous (ou un coéquipier) pourrez relire plus tard, voici une règle courante : ne vous répétez pas !

Si vous créez des méthodes ou des fonctions répétitives, votre code sera plus difficile à maintenir. Vous créerez des bugs simplement en oubliant de mettre à jour plusieurs versions du même code.

Si vous avez une bonne compréhension du [concept de _this_ en JavaScript](https://blog.codeanalogies.com/2018/03/12/javascripts-this-explained-by-starting-a-high-school-band/), vous savez que cela peut être particulièrement difficile lorsque vous essayez de suivre le **contexte d'exécution**. Il s'agit de la relation entre la **fonction** et l'**objet** sur lequel elle est appelée.

Pour écrire un code plus propre, vous pouvez utiliser les **méthodes apply, call et bind** pour manipuler intentionnellement le contexte d'exécution. Différents objets peuvent partager des méthodes sans les réécrire pour chaque objet individuel.

Apply, call et bind sont parfois appelés **méthodes de fonction**, car ils sont appelés avec une fonction.

Si vous cherchez une explication plus technique, je recommande le guide de [JavaScriptIsSexy](http://javascriptissexy.com/javascript-apply-call-and-bind-methods-are-essential-for-javascript-professionals/).

### En quoi cela ressemble-t-il à la cuisine, exactement ?

Ces trois méthodes sont un peu comme l'application de compétences culinaires pour préparer de la nourriture pour un barbecue. Pensez aux différents contextes dans lesquels vous pourriez avoir besoin de cuisiner :

1. Un repas général que vous pouvez cuisiner à peu près n'importe quand et qui rend tout le monde heureux (pâtes et sauce)
2. Un barbecue qui pourrait aussi être une fête (burgers, hot-dogs, etc.)
3. Un dîner chic pour vous et votre partenaire (poisson et vin)
4. Préparer un dessert pour un repas partagé (gâteau)

Chacun de ces cas nécessite un ensemble différent de techniques culinaires. Certaines sont uniques à un contexte individuel, tandis que d'autres sont plus généralisées. Je vais expliquer plus en détail dans un instant.

Dans ce cas, chaque contexte culinaire est un peu comme un objet. Si vous dites que vous allez cuisiner sur le grill, par exemple, cela implique que vous avez quelques compétences... comme utiliser un grill !

Ainsi, si nous avons une méthode individuelle pour chacune des techniques culinaires que vous pourriez utiliser, il y aura certaines méthodes uniques à chaque objet, et certains cas où une méthode peut être appliquée à plusieurs objets.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7trEAvHGVHWAL1UH.)

Dans le code ci-dessus, faire bouillir de l'eau est une compétence généralisée qui peut probablement être appliquée dans n'importe quel contexte.

Prenons un exemple. La méthode grill() est dans le contexte de l'objet barbecue. Cela signifie que si vous organisez un barbecue, vous vous attendez à devoir utiliser ces compétences de grill.

Mais attendez. Vous n'oubliez pas comment utiliser le grill lorsque le barbecue se termine ! Supposons que vous et votre partenaire souhaitez cuisiner un steak pour un dîner chic, comme l'objet fancyDinner. Vous souhaitez toujours pouvoir emprunter cette méthode grill() de l'objet barbecue. C'est là que apply, call et bind interviennent.

Cette relation entre les compétences culinaires (méthodes) et les contextes culinaires (objets) sera le principal moyen que j'utiliserai pour montrer comment utiliser apply, call et bind().

Pour comprendre ce tutoriel, vous devez comprendre _this_ en JavaScript. Consultez mon [tutoriel sur le _this_ de JavaScript](https://blog.codeanalogies.com/2018/03/12/javascripts-this-explained-by-starting-a-high-school-band/) si vous devez réviser cela.

### Introduction à la méthode Bind

Imaginons que vous organisez un barbecue pour la fête des 10 ans de votre fils ou de votre fille. Vous souhaitez cuisiner trois types de viande sur le grill pour satisfaire tout le monde : du poulet, des burgers et du steak. Apparemment, tous les invités sont des amateurs de viande.

Cependant, vous n'avez aucune idée de ce que chaque personne veut individuellement ! Vous allez donc devoir demander à chaque invité à leur arrivée à la fête. Chaque type de viande nécessite généralement les mêmes étapes :

1. Ajouter des épices
2. Le mettre sur le grill
3. Retirer du grill après un certain temps

Il n'y a donc aucun intérêt à écrire une méthode séparée pour chaque type de viande. La seule chose qui varie est le temps de cuisson. Les burgers prennent 15 minutes, le poulet prend 20 minutes et le steak prend 10 minutes.

Nous voulons utiliser le même processus général pour tous ces types de viande. Les détails varieront.

Vous pourriez penser : « Oh, c'est le moment idéal pour une fonction ! » Mais c'est un peu plus compliqué que cela. Comme nous l'avons dit ci-dessus, nous essayons d'utiliser le concept de **contexte d'exécution** pour montrer nos compétences culinaires. Vous ne voudriez pas cuisiner des burgers, du poulet et du steak pour la première fois pour une fête entière. Nous devons donc représenter les compétences que vous avez acquises au fil des années de cuisine et comment vous allez les appliquer à ce scénario particulier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MKGALKHF_hr9Equr.)

Dans ce cas, notre méthode grill se contente d'enregistrer une phrase sur le moment où la nourriture de la personne sera prête. Nous allons utiliser bind() pour stocker un **contexte d'exécution**. Pour être clair, le contexte d'exécution aura deux détails importants.

1. Une référence à l'objet _barbecue_ pour s'assurer que nous utilisons le bon objet
2. Le nombre de minutes de cuisson

Cela représente nos connaissances existantes sur la façon de cuisiner les différents types de viande. Dans chaque cas, nous stockons l'objet et le nombre de minutes, afin de pouvoir traiter rapidement les demandes de tous les invités de la fête.

Chaque variable — cookBurger, cookChicken et cookSteak — est une nouvelle fonction qui peut être exécutée à tout moment avec un argument supplémentaire : le nom de la personne. Voici donc trois personnes et leurs demandes de nourriture :

1. Jack veut un burger
2. Jill veut un steak
3. David veut du poulet

En utilisant nos nouvelles fonctions, nous pouvons traiter rapidement ces demandes sans réécrire la méthode grill. Chacun des exemples ci-dessous prend l'argument final nécessaire pour que la fonction s'exécute dans le contexte de l'objet barbecue.

![Image](https://cdn-media-1.freecodecamp.org/images/0*v7q9FTcaIthuVPqT.)

Imaginez si vous ne pouviez pas utiliser la méthode bind ici ! Ce serait un peu comme si vous cuisiniez des burgers, du poulet et du steak pour la première fois lorsque la fête a commencé. Vous alimenteriez trois arguments dans une méthode grill() générale, sans planification préalable.

Au lieu de cela, nous utilisons l'**application partielle de fonction** pour montrer que nous savons comment cuisiner chaque type de viande. Nous devons simplement entendre ce que chaque invité individuel veut manger. Cette division représente votre expérience culinaire réelle.

### Introduction à la méthode Call

Voici un autre scénario. Supposons que lorsque vous et votre partenaire cuisinez un dîner chic, vous aimez généralement faire du poisson et du vin. Comme vous pouvez le voir dans le premier extrait de code, vous aimez généralement cuisiner le poisson au four.

Mais, vous décidez qu'un soir, vous aimeriez faire un steak à la place. Vous allez devoir utiliser le grill pour faire ce steak, évidemment.

![Image](https://cdn-media-1.freecodecamp.org/images/0*iXscRKRPeC-xTKBj.)

Voici le problème : votre méthode grill() est dans le contexte de l'objet barbecue ! Mais maintenant, vous voulez utiliser ces compétences culinaires dans l'objet fancyDinner. Rappelez-vous, **vous ne voulez pas réécrire la méthode grill —** cela rendra votre code plus difficile à maintenir.

Au lieu de cela, vous pouvez utiliser la méthode call() de JavaScript pour appeler la méthode grill dans le contexte de l'objet _fancyDinner_. En utilisant ce nouveau contexte, vous n'aurez pas besoin de la réécrire. Voici le code complet avant d'entrer dans les détails.

![Image](https://cdn-media-1.freecodecamp.org/images/0*RF3pUlTfHzWhEA_X.)

Ainsi, notre boisson par défaut pour les barbecues est le soda, et la boisson par défaut pour les dîners chics est le vin. Maintenant, nous devons simplement ajouter la partie inhabituelle comme **argument** dans la méthode call() — « steak ». Voici la différence entre l'utilisation de la méthode normalement et l'utilisation de call().

![Image](https://cdn-media-1.freecodecamp.org/images/0*oebh09RPKpZeIJB-.)

Le premier exemple devrait être assez simple : tout est dans le contexte de l'objet barbecue. Mais dans le deuxième exemple, le premier argument a changé le contexte de _this_ en l'objet _fancyDinner_ !

Lorsque vous arrivez à l'instruction console.log dans la méthode grill(), vous pouvez voir qu'elle fait référence à un seul argument, _meal_, ainsi qu'à _this.drink_.

Lorsque vous utilisez fancyDinner comme premier argument de la méthode call, cela définit le contexte sur l'objet fancyDinner. Maintenant, vous êtes en mesure d'utiliser ces compétences de grill dans un autre contexte.

### Introduction à la méthode Apply

La méthode apply() est très similaire à call(), à une différence importante près. Elle peut accepter un tableau d'arguments, au lieu de déclarer des paramètres individuels. Cela signifie que vous pouvez créer une **fonction variadique** — c'est-à-dire une fonction avec un nombre quelconque d'arguments. Pour cette raison, elle ne peut accepter que deux paramètres : le contexte et un tableau d'arguments.

Revenons à notre exemple original de fête d'anniversaire. Vous organisez un barbecue pour la fête des 10 ans de votre fils ou de votre fille. 12 enfants ont répondu et dit qu'ils viendraient, mais vous ne savez pas combien viendront réellement. Vous devez donc être prêt à griller pour un nombre inconnu de personnes.

Cependant, contrairement à bind(), les fonctions appelées avec apply() seront invoquées immédiatement.

Nous devons donc créer une fonction qui peut gérer un tableau d'un nombre inconnu de commandes de repas et retourner la liste complète des aliments que vous devrez mettre sur le grill. Nous pouvons conserver la structure organisationnelle du tableau, ce qui nous aide à donner l'ordre dans lequel les demandes sont arrivées.

Il y a quelques points importants à noter ici. Tout d'abord, remarquez que la méthode grill n'a aucun paramètre. Cela est différent du passé ! Pour résoudre cela, nous utilisons l'objet arguments à la ligne 4. L'[objet arguments en JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) nous donne un objet de type tableau rempli des arguments de la fonction.

Pour le convertir en un tableau réel, nous devons utiliser la méthode slice() du prototype de tableau. Cela est une autre application pratique de la méthode call(), puisque la méthode slice() n'est pas native aux objets.

Enfin, nous devons invoquer la fonction en utilisant apply() afin d'accéder au tableau dans la propriété mealOrders. Voici comment faire.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5IRJN6HVTnIPtWYU.)

Nous devons toujours utiliser _barbecue_ comme premier argument, car tout comme call(), nous devons déclarer le contexte d'exécution. Ensuite, nous pouvons alimenter le tableau de la propriété mealOrders.

Cela nous permet d'utiliser un nombre indéfini d'éléments dans la méthode grill() puisque nous pouvons passer un tableau comme deuxième argument.

### Obtenez les derniers tutoriels

Avez-vous aimé ce tutoriel ? Applaudissez-le pour que d'autres puissent le trouver aussi. Ou inscrivez-vous pour recevoir mes derniers tutoriels visualisés du [blog CodeAnalogies](http://codeanalogies.com) ici :