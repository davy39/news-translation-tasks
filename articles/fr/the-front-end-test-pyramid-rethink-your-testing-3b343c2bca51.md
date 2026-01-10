---
title: 'La Pyramide de Tests Front-End : Comment Repenser Vos Tests'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-08T17:21:32.000Z'
originalURL: https://freecodecamp.org/news/the-front-end-test-pyramid-rethink-your-testing-3b343c2bca51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6A85taNWuTlwoqas2ei4aQ.jpeg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Testing
  slug: testing
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: 'La Pyramide de Tests Front-End : Comment Repenser Vos Tests'
seo_desc: 'By Edd Yerburgh

  If you’re testing front end apps, you should know about the front-end test pyramid.

  In this article we’ll look at what the front-end test pyramid is, and how to use
  it to create comprehensive test suites.

  The front-end test pyramid

  Th...'
---

Par Edd Yerburgh

Si vous testez des applications front-end, vous devriez connaître **la pyramide de tests front-end**.

Dans cet article, nous examinerons ce qu'est la pyramide de tests front-end et comment l'utiliser pour créer des suites de tests complètes.

### La pyramide de tests front-end

La pyramide de tests front-end est une représentation de la manière dont une suite de tests front-end doit être structurée.

La suite de tests idéale est composée de tests unitaires, de quelques tests de snapshot et de quelques tests end-to-end (e2e).

![Image](https://cdn-media-1.freecodecamp.org/images/oXby3yFqAcCEeB6skWrlCnCFYoa1zswnhMzW)
_La pyramide de tests front-end_

Il s'agit d'une version révisée de la [pyramide de tests](https://martinfowler.com/bliki/TestPyramid.html), spécifique aux tests des applications front-end.

Dans cet article, nous allons passer en revue à quoi ressemblent chacun de ces types de tests. Pour cela, nous allons créer une suite de tests pour une application exemple.

### L'application

Pour en apprendre davantage sur la pyramide de tests front-end en détail, nous allons examiner comment tester une application web.

L'application est une simple application modale. Cliquer sur un bouton ouvre une modale, et cliquer sur un bouton OK dans la modale ferme la modale.

![Image](https://cdn-media-1.freecodecamp.org/images/SynF5P9JozzoGnS8e7HMk5KH5yfV-6vZA5W7)
_L'application terminée_

Nous allons construire l'application à partir d'un framework basé sur des composants. Ne vous inquiétez pas des spécificités — nous allons garder cela à un niveau élevé.

L'application est composée de trois composants — un composant `Button`, un composant `Modal` et un composant `App`.

Les premiers tests que nous allons écrire sont des tests unitaires. Dans la pyramide de tests front-end, la majorité de nos tests sont des tests unitaires.

### Tests unitaires

Les tests unitaires testent des unités d'une base de code.

Ils appellent des fonctions — ou unités — directement et s'assurent qu'elles retournent le résultat correct.

Dans notre application, nos composants sont des unités. Nous allons donc écrire des tests unitaires pour Button et Modal. Il n'est pas nécessaire d'écrire des tests pour notre composant `App` car il n'y a pas de logique dedans.

Les tests unitaires vont **rendre superficiellement** les composants et vérifier qu'ils se comportent correctement lorsque nous interagissons avec eux.

Le [rendu superficiel](https://reactjs.org/docs/shallow-renderer.html) signifie que nous rendons le composant à un niveau de profondeur. Ainsi, nous pouvons nous assurer que nous testons uniquement le composant, notre unité, et non un composant enfant plusieurs niveaux plus bas.

Dans nos tests, nous allons déclencher des actions sur les composants et vérifier que les composants se comportent comme prévu.

Nous ne regarderons pas le code. Mais les spécifications pour nos composants ressemblent à ceci :

* Modal a la classe is-active lorsque displayModal est vrai
* Modal n'a pas la classe is-active lorsque displayModal est faux
* Modal appelle toggleModal lorsque le bouton de succès est cliqué
* Modal appelle toggleModal lorsque le bouton de suppression est cliqué
* Button appelle toggleModal lorsque le bouton est cliqué

Nos tests vont rendre superficiellement les composants et vérifier que chaque spécification fonctionne.

Il y a plusieurs raisons pour lesquelles les tests unitaires devraient constituer la majorité de notre suite de tests :

#### Les tests unitaires sont rapides.

Une suite de centaines de tests unitaires s'exécute en quelques secondes.

Cela rend les tests unitaires utiles pour le développement. Lors du refactoring de code, nous pouvons changer le code et exécuter les tests unitaires pour vérifier que les changements n'ont pas cassé le composant. Nous saurons en quelques secondes si nous avons cassé quelque chose, car l'un des tests échouera.

#### Les tests unitaires sont granulaires

En d'autres termes, ils sont très spécifiques.

Si un test unitaire échoue, le test cassé nous dira comment et pourquoi il échoue.

Les tests unitaires sont bons pour vérifier les détails fins du fonctionnement de notre application. Ils sont le meilleur outil à utiliser lors du développement, surtout si vous suivez le développement piloté par les tests.

Mais ils ne peuvent pas tout tester.

Pour nous assurer que nous rendons le style correct, nous devons utiliser des tests de snapshot.

### Tests de snapshot

Les tests de snapshot sont des tests qui prennent une image de votre composant rendu et la comparent avec une image précédente de votre composant.

La meilleure façon d'écrire des tests de snapshot en JavaScript est avec [Jest](https://facebook.github.io/jest/).

Au lieu de prendre une image du composant rendu, Jest prend un snapshot du markup du composant rendu. Cela rend les tests de snapshot de Jest beaucoup plus rapides que les tests de snapshot traditionnels.

Pour enregistrer un test de snapshot dans Jest, vous devez ajouter quelque chose comme le code ci-dessous :

```
const renderedMarkup = renderToString(ModalComponent)expect(renderedMarkup).toMatchSnapshot()
```

Une fois que vous avez enregistré un snapshot, Jest s'occupe de tout le reste. Chaque fois que les tests unitaires sont exécutés, il régénère un snapshot et le compare avec le snapshot précédent.

Si le code change, Jest lance une erreur et avertit que le markup a changé. Le développeur peut alors vérifier manuellement qu'aucune classe n'a été supprimée par accident.

Dans le test ci-dessous, quelqu'un a supprimé la classe `modal-card-foot` du `<footer>`.

![Image](https://cdn-media-1.freecodecamp.org/images/Uws6tkMtvhv3RzJFCxyp3Z3OVDfcpzpLofMf)
_Un test de snapshot échoué_

Les tests de snapshot sont un moyen de vérifier que rien n'a changé concernant le style ou le markup d'un composant.

Si les tests de snapshot passent, nous savons que notre changement de code n'a pas affecté l'affichage de nos composants.

Si les tests échouent, alors nous savons que nous avons affecté le rendu des composants et pouvons vérifier manuellement que le style est toujours correct.

Vous devriez avoir au moins 1 test de snapshot par composant. Un test de snapshot typique rend le composant avec un certain état pour vérifier qu'il se rend correctement.

Maintenant que nous avons des tests unitaires et des tests de snapshot, il est temps de regarder les tests end-to-end (e2e).

### Tests end-to-end

Les tests end-to-end (e2e) sont des tests de haut niveau.

Ils effectuent les mêmes actions que nous ferions si nous testions une application manuellement.

Dans notre application, nous avons un parcours utilisateur. Lorsque l'utilisateur clique sur le bouton, la modale s'ouvre, et lorsqu'il clique sur le bouton dans la modale, la modale se ferme.

Nous pouvons écrire un test end-to-end qui parcourt ce parcours. Le test ouvrira le navigateur, naviguera vers la page web et exécutera chaque action pour s'assurer que l'application se comporte correctement.

Ces tests nous indiquent que nos unités fonctionnent ensemble correctement. Cela nous donne une grande confiance que la fonctionnalité principale de l'application fonctionne.

Il existe plusieurs façons d'écrire des tests end-to-end pour les applications JavaScript. Il existe des programmes comme TestCafe qui enregistrent vos actions dans un navigateur et les rejouent en tant que tests.

Il existe également des projets comme Nightwatch qui vous permettent d'écrire les tests en JavaScript. Je recommanderais d'utiliser une bibliothèque comme Nightwatch. Elle est facile à prendre en main et les tests s'exécutent plus rapidement que les tests enregistrés.

Cela dit, les tests Nightwatch sont encore relativement lents. Une suite de 200 tests unitaires prend quelques secondes à s'exécuter, une suite de 200 tests end-to-end prend des minutes à s'exécuter.

L'autre problème avec les tests end-to-end est qu'ils sont difficiles à déboguer. Lorsqu'un test échoue, il est difficile de trouver pourquoi il a échoué, car les tests couvrent beaucoup de fonctionnalités.

### Conclusion

Pour tester efficacement les applications web front-end basées sur des composants, vous avez besoin de trois types de tests : des tests unitaires, des tests de snapshot et des tests e2e.

Vous devriez avoir plusieurs tests unitaires pour chaque composant, un ou deux tests de snapshot par composant, et un ou deux tests end-to-end qui testent plusieurs composants connectés ensemble.

Globalement, les tests unitaires constitueront la majorité de vos tests, vous aurez quelques tests de snapshot et quelques tests e2e.

Si vous suivez la pyramide de tests front-end, vous créerez des applications web maintenables avec des suites de tests exceptionnelles.

_Vous pouvez voir un [exemple de dépôt de l'application avec des tests de snapshot, des tests unitaires et des tests end-to-end sur GitHub](https://github.com/eddyerburgh/example-front-end-test-pyramid-app)._