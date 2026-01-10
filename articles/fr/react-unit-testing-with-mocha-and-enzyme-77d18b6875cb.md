---
title: Tests unitaires React avec Mocha et Enzyme
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-31T09:15:48.000Z'
originalURL: https://freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Tk8MKzapWo7uPf0m5VF7Gg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Tests unitaires React avec Mocha et Enzyme
seo_desc: 'By Michael Shilman

  A step-by-step tutorial for UI testing in Meteor.

  This is a short tutorial to help you test your React UI components. It presents
  a simple UI testing pattern I contributed to the Meteor Guide (?) and Todos sample
  app (?).

  You shoul...'
---

Par Michael Shilman

#### Un tutoriel pas à pas pour les tests d'interface utilisateur dans Meteor.

Ce tutoriel court vous aidera à tester vos composants d'interface utilisateur React. Il présente un modèle simple de test d'interface utilisateur que j'ai contribué au [Guide](http://guide.meteor.com/) de Meteor ([?)](https://github.com/meteor/guide/pull/466) et à l'application exemple T[odos](https://github.com/meteor/todos/tree/react) (?[).](https://github.com/meteor/todos/pull/141)

Vous devriez lire ceci si vous :

1. Utilisez [React](https://facebook.github.io/react/) pour développer vos applications
2. Voulez une manière facile de tester automatiquement votre interface utilisateur
3. Utilisez [Meteor](https://www.meteor.com/) … **ou non** — la plupart de ceci fonctionnera dans n'importe quelle configuration React !

Voici les tests que nous allons écrire à gauche, et les composants d'interface utilisateur que nous allons tester à droite :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fxu5arW8UWdhVxeZi_zMmw.png)

En parcourant plusieurs tests en détail, vous apprendrez les éléments de base des tests d'interface utilisateur React et les meilleures pratiques pour structurer une suite de tests. Vous pouvez appliquer ces modèles à vos propres applications pour attraper les bugs, écrire du code plus rapidement, documenter le comportement du code et vous assurer que rien ne casse lorsque vous ajoutez de nouvelles fonctionnalités à votre application.

Le tutoriel suppose une familiarité de base avec React et [ES6](https://github.com/lukehoban/es6features), mais ne nécessite pas beaucoup de connaissances sur Meteor. Tout le code source est disponible dans l'application exemple [Todos](https://github.com/meteor/todos/tree/react) de Meteor afin que vous puissiez l'exécuter sur votre propre machine et jouer avec le code.

### Tests unitaires d'interface utilisateur

Il existe de nombreuses façons de tester votre logiciel, mais les tests unitaires d'interface utilisateur sont de petits tests isolés de composants d'interface utilisateur individuels, plutôt que des tests complets du système. Ils sont (relativement) faciles à configurer et rapides à exécuter.

Voici une capture d'écran de la suite actuelle de tests unitaires de Todos, incluant à la fois les tests Client (interface utilisateur) et Serveur. L'ensemble de la suite s'exécute en un peu plus d'une seconde sur mon ordinateur portable :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5FSjCZurIXQkazef3LVN_A.gif)

Parce que les tests s'exécutent si rapidement, vous pouvez les exécuter chaque fois que vous [validez du code](https://en.wikipedia.org/wiki/Continuous_integration) ou même chaque fois que vous [modifiez un fichier](https://wallabyjs.com/).

> _Avoir une suite de tests complète vous donne l'esprit tranquille que votre code fonctionne toujours comme vous vous y attendez._

### Technologies

Avant de plonger, quelques mots sur les différentes technologies open-source en jeu :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1e_oWbWMM_LK4d5HpUiqXw.png)

[Meteor](https://www.meteor.com/) est une plateforme JavaScript full-stack pour les applications web et mobiles modernes. Elle exécute Node.JS en backend et plusieurs frameworks d'interface utilisateur en frontend, y compris React. Les tests ont reçu un énorme coup de pouce dans la récente [version 1.3](http://info.meteor.com/blog/announcing-meteor-1.3), alors nous allons l'essayer aujourd'hui !

[React](https://facebook.github.io/react/) est la bibliothèque JavaScript de Facebook pour les interfaces utilisateur. C'est une manière populaire de développer des interfaces web modernes, et avec [React Native](https://facebook.github.io/react-native/), elle fait également des progrès dans les applications mobiles et de bureau natives.

[Mocha](https://mochajs.org/) est le framework de tests unitaires JavaScript le plus populaire. Tout comme nous ne couvrirons pas tout sur les tests, nous ne couvrirons pas tout sur les tests unitaires dans Mocha. Mais il devrait y avoir assez ici pour vous donner un bon départ.

[Enzyme](https://github.com/airbnb/enzyme) est la bibliothèque d'AirBnB pour les tests unitaires des composants React. Elle est géniale car elle facilite la simulation du contexte d'un composant React sans avoir à démarrer un navigateur, et vous pouvez toujours effectuer des sélections CSS et simuler des événements utilisateur.

À l'exception d'Enzyme, qui est spécifique à React, toutes ces bibliothèques fonctionnent indépendamment les unes des autres. Ensemble, elles constituent une excellente manière de construire des applications en temps réel.

> **_?:_** _D'accord. Pouvez-nous simplement commencer à tester ?_

Si vous avez l'application Todos configurée sur votre machine, ou si vous ne vous souciez pas d'exécuter réellement les tests, vous pouvez passer à la section suivante. Sinon, configurons votre machine. ?

### Configuration de la machine

Si vous souhaitez exécuter les tests sur votre machine locale, voici la configuration rapide pour Linux/Mac. Pour un guide beaucoup plus détaillé, le site de Meteor fournit un [tutoriel complet pour l'application Todos](https://www.meteor.com/tutorials/react/creating-an-app) :

REMARQUE : il y a actuellement [un problème](https://github.com/meteor/todos/issues/144) où il donne l'avertissement suivant sur la ligne de commande lors de l'exécution des tests :

```
Impossible de résoudre certains modules :
"react/addons" dans /path/to/react-compat.js
"react/lib/ReactContext" dans /path/to/react-compat.js
"react/lib/ExecutionEnvironment" dans /path/to/react-compat.js
```

Il est sûr d'ignorer ceci et vous devriez pouvoir voir les résultats de l'exécution des tests dans le navigateur à l'adresse [http://localhost:3000.](http://localhost:3000.)

Les résultats des tests proviennent de tous les fichiers avec le suffixe **.tests.js** dans l'arborescence des sources, et lorsque nous modifions des fichiers ou ajoutons de nouveaux fichiers avec ce schéma de nommage, la suite de tests s'exécutera automatiquement et mettra à jour la fenêtre du navigateur.

REMARQUE : de manière déroutante, il y a également un répertoire **tests/** au niveau supérieur de l'arborescence des sources. Celui-ci contient des tests de bout en bout, et vous devriez l'ignorer pour ce tutoriel. Pour plus d'informations, [voir le guide](http://guide.meteor.com/testing.html).

### Rendu des composants

Le test d'interface utilisateur le plus simple consiste à vérifier si un composant se rend correctement selon les données qui lui sont passées. Par exemple, si vous rendez un élément de todo, vous vous attendez à voir le nom de l'élément affiché dans l'étiquette, et son état coché reflété correctement sur la page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*asDZOHrIZND0FXK7rhsI7Q.png)

Voici à quoi cela ressemble dans Enzyme et Mocha :

Il y a quelques choses qui se passent ici.

**Structure.** Dans Mocha, _describe_ commence une suite de tests, et _it_ commence un cas de test unique. Pour notre premier test, nous utilisons la structure la plus simple possible. Notez que le contenu de _describe_ et _it_ sont simplement des fonctions, donc nous pouvons faire des choses comme sortir tôt pour forcer les tests à ne s'exécuter que côté client.

Dans chaque test, nous suivons un modèle **_configuration → exercice → vérification → nettoyage_** qui porte différents noms, mais est la [meilleure pratique courante](http://www.agile-code.com/blog/the-anatomy-of-a-unit-test/) en matière de tests unitaires :

**Configuration.** Tout d'abord, nous créons les données à rendre, qui dans ce cas est un objet JavaScript. Facile.

**Exercice.** Ensuite, utilisez la fonction _shallow_ pour rendre les données dans un composant. Ce rendu est ce que nous testons réellement, c'est pourquoi il fait partie de la phase _exercice_ plutôt que de la _configuration_. L'appel à _shallow_ retourne un objet _wrapper_ Enzyme qui contient l'instance du composant rendu, ainsi qu'un ensemble de fonctions utilitaires pour simuler des événements utilisateur comme les clics de souris et interroger l'état de l'interface utilisateur.

**Vérification.** Ensuite, nous utilisons _hasClass_, _find,_ et _prop_ pour interroger l'état de l'interface utilisateur afin de vérifier que le composant s'est rendu correctement. Toutes les instances de _TodoItem_ doivent avoir la classe _list-item_, et les éléments cochés doivent avoir la classe _checked_. Enfin, nous nous assurons que la valeur par défaut de l'entrée est « Embrassez l'écosystème » comme nous nous y attendions.

**Nettoyage.** Dans de nombreux tests, il y a également un peu de nettoyage à faire, mais dans ce cas, il n'y a rien à nettoyer puisque toutes les variables sont temporaires.

Pour ajouter ce test à l'application Todos, il suffit de copier le snippet dans un fichier **imports/ui/components/TodoItem-render.tests.js** sous le répertoire _todos_ (n'importe quel fichier avec le suffixe **.tests.js** en fait, mais nous le mettons dans le même répertoire que le composant par convention). Ce test sera redondant avec les tests déjà dans **TodoItem.tests.js**, mais maintenant vous savez comment ajouter les vôtres.

### Rendu avec état

Faisons un autre exemple légèrement plus complexe. L'en-tête de la liste a en fait deux états : un état normal et un état d'édition, et il affiche deux interfaces utilisateur différentes en fonction de l'état interne du composant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dgy5ayc59KGlIKvjwlVs9g.png)

Et voici à quoi ressemble le test :

**Structure.** Remarquez que nous avons divisé le code en deux blocs _describe_ pour lui donner un peu plus de structure. Cela aidera lorsque nous commencerons à ajouter plus de tests, car en plus de rendre différemment, l'interaction du composant change en fonction de l'état. Nous en parlerons plus en détail ci-dessous.

**Configuration/Exercice.** Comme d'habitude, sauf que nous avons utilisé la fonction _mount_ d'Enzyme pour rendre plutôt que _shallow_, que nous avons utilisée ci-dessus. Nous utilisons _mount_ pour simuler le contexte complet du composant. La différence est que _shallow_ ne rend que le composant passé, mais _mount_ nécessite que nous exécutions dans un contexte de navigateur (navigateur ou navigateur sans tête) et rend également les composants enfants.

**Test.** Nous avons utilisé l'utilitaire _setState_ d'Enzyme pour manipuler l'état du composant. C'est comme simuler un clic de souris, sauf que plutôt que de simuler directement l'utilisateur, nous simulons un changement provenant d'une autre partie de l'application.

**Vérification/Nettoyage.** Rien de spécial : interrogation du DOM et aucun nettoyage requis pour ce test simple.

### Interaction utilisateur

Le rendu n'est que la moitié de l'équation, et les choses deviennent plus intéressantes lorsque nous voulons tester l'interaction utilisateur. Tout d'abord, modélisons lorsque l'utilisateur clique sur la case à cocher d'un élément de todo :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6tSODdVWqKJex8HhcbtBdA.gif)

Et voici à quoi ressemble ce test :

**Structure.** Ce code suit la même structure _configuration → exercice → vérification → nettoyage_ que ci-dessus, mais dans ce cas, nous faisons réellement quelque chose de significatif à chaque étape.

**Configuration.** Celui-ci est intéressant car lorsque vous cliquez sur la case à cocher, le composant appelle en fait une [Méthode Meteor](http://guide.meteor.com/methods.html), qui demande au serveur de mettre à jour la base de données. Cependant, lorsque nous exécutons un test unitaire, il n'y a pas de serveur, et même s'il y en avait, nous ne voudrions pas modifier de données. Nous substituons donc la méthode en utilisant la bibliothèque [Sinon](http://sinonjs.org/) (communément utilisée avec Mocha). Elle remplace la fonction _call_ de la méthode _setCheckedStatus_ par un leurre qui ressemble à l'original, mais qui enregistre simplement le comportement de l'utilisateur et ne fait rien avec.

REMARQUE : Vous pourriez vous gratter la tête car jusqu'à présent, le rendu _shallow/mount_ faisait partie de la phase _exercice_, mais cette fois-ci, il est dans la _configuration_. C'est un point subtil, mais puisque l'accent de ce test est l'action d'interaction utilisateur, le rendu fait simplement partie de la configuration.

**Exercice.** Ensuite, nous utilisons la fonction _simulate_ pour effectuer le clic. Assez simple. Nous pouvons également simuler des événements clavier, des soumissions de formulaires, etc., mais nous n'en avons pas besoin pour ce test.

**Vérification.** Maintenant, nous pouvons voir comment le leurre entre en jeu. Nous affirmons que la méthode _setCheckedStatus_ a été appelée avec les arguments que nous attendons. Cela teste non seulement le comportement, mais fournit également une bonne documentation sur le fonctionnement de l'interaction.

**Nettoyage.** La configuration du leurre modifie en fait la méthode _setCheckedStatus_ globalement, donc à la fin du test, nous devons la nettoyer. restore remplace le leurre par la fonction originale.

Tous nos autres tests d'interaction suivent la même structure de base et vous pouvez les voir dans le [dépôt Todos](https://github.com/meteor/todos/tree/react).

### Structure de la suite de tests

En utilisant ces modèles de base ci-dessus pour tester le _rendu_ et l'_interaction_, vous devriez être en mesure de tester n'importe quel composant React dans l'exemple Todos et d'adapter facilement le modèle à vos propres applications. Mais si vous commencez à ajouter des tests sans aucune structure, les choses vont rapidement devenir incontrôlables. Je vais donc conclure le tutoriel en décrivant une structure de test de niveau supérieur.

J'ai mentionné ci-dessus comment l'utilisation de _describe_ de Mocha peut à la fois délimiter une structure logique et également économiser du code, et nous allons utiliser cela à notre avantage lorsque nous ajouterons plus de tests. Voyons comment cela fonctionne.

Rappelons notre exemple _ListHeader_ ci-dessus où nous avons distingué les états par défaut et d'édition. Le test avait la structure suivante :

Maintenant, refactorisons le code en utilisant la construction _beforeEach_ de Mocha qui s'exécute avant chacun des tests à l'intérieur de la suite _describe_ :

À première vue, ce changement semble être une perte nette : le code est devenu plus long et compliqué. Cependant, plus nous ajoutons de tests, plus nous obtenons de réutilisation et plus cette structure commence à avoir du sens. Voici la structure de test dans l'application Todos, et ce n'est qu'un test partiel de la fonctionnalité de l'en-tête :

Avant de vous lancer dans le code, vous devez noter que parce que _beforeEach_ s'exécute pour chaque test dans chaque bloc imbriqué, il est très facile d'écrire des tests inefficaces de cette manière. Par exemple, dans le code ci-dessus, un nouveau stub de routeur React est créé cinq fois, une fois pour chaque test _it_, bien qu'il ne soit vraiment nécessaire que pour l'un des tests. Dans ce cas, cela ne me dérangeait pas. Cependant, il est tentant de mettre toute votre configuration de test dans _beforeEach_, mais vous ne devriez généralement y mettre que ce dont vous avez besoin.

### Conclusion et prochaines étapes

Dans ce tutoriel, nous avons parcouru les bases des tests de composants d'interface utilisateur, avec des exemples bien documentés sur la façon de tester le rendu et l'interaction. Ce sont les éléments de base pour tester votre interface utilisateur, et en les utilisant, vous devriez être en mesure de tester la plupart des aspects de n'importe quelle interface utilisateur React que vous développez.

Voici quelques prochaines étapes pour en apprendre davantage :

1. **Vos devoirs**. Consultez l'application [Todos](https://github.com/meteor/todos) et ajoutez un test unitaire pour un comportement différent. Par exemple, l'application distingue les Todos publics et privés, mais les tests actuels ne couvrent pas cela. Ajoutez un test pour cela ! _Crédit supplémentaire : soumettez une pull request !_
2. **Plus de tests d'interface utilisateur React**. Le geek de Meteor [Arunoda](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) couvre [UI Testing in React](https://voice.kadira.io/ui-testing-in-react-74fd90a5d58b#.tek2zwsvq) beaucoup de terrain similaire, mais sous un angle différent. Et si vous êtes tenté, [Ken Wheeler](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) explique une configuration similaire pour [Unit Testing React Native](https://blog.formidable.com/unit-testing-react-native-with-mocha-and-enzyme-51518f13ba73).
3. **Tests en général**. Les tests unitaires d'interface utilisateur ne sont qu'une pièce du puzzle. [Eric Elliott](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/) donne cinq questions à répondre dans chaque test unitaire. La section [testing](http://guide.meteor.com/testing.html) du Meteor Guide est une excellente vue d'ensemble des autres types de tests dans Meteor, et des tests en général.

Commentez ci-dessous avec des questions ou des suggestions. Et suivez-moi ici ou [sur Twitter](https://twitter.com/mshilman) pour _plus de grands articles à venir._

**Et enfin, si cela vous a été utile, appuyez sur le bouton ? ci-dessous. Merci !**

_Merci beaucoup à [Tom Coleman](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) pour ses conseils sur Meteor/PR ; [Sean Moon](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) pour m'avoir initié aux tests ; [Keywon](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined), [Ross Geesman](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined), [Josh Owens](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined), [Sam Hatoum](https://www.freecodecamp.org/news/react-unit-testing-with-mocha-and-enzyme-77d18b6875cb/undefined) pour leurs excellents retours sur le brouillon._