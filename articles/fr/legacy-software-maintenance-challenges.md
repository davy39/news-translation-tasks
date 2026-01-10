---
title: Pourquoi votre logiciel hérité est difficile à maintenir - et que faire à ce
  sujet.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-28T17:06:30.000Z'
originalURL: https://freecodecamp.org/news/legacy-software-maintenance-challenges
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c5f740569d1a4ca31cb.jpg
tags:
- name: software
  slug: software
seo_title: Pourquoi votre logiciel hérité est difficile à maintenir - et que faire
  à ce sujet.
seo_desc: 'By Alfrick Opidi

  Believe it or not, some organizations still rely on legacy software to carry out
  operations even though newer and more versatile options are available. We know that
  “old is gold”, but legacy applications cannot glitter forever. As su...'
---

Par Alfrick Opidi

Croyez-le ou non, certaines organisations s'appuient encore sur des logiciels hérités pour effectuer des opérations même si des options plus récentes et plus polyvalentes sont disponibles. Nous savons que « l'ancien est l'or », mais les applications héritées ne peuvent pas briller éternellement. Ainsi, ces anciens programmes sont devenus difficiles à maintenir.

Récemment, le Government Accountability Office (GAO) des États-Unis a publié un [rapport](https://www.gao.gov/products/gao-19-471#summary) qui a souligné les systèmes fédéraux hérités les plus critiques qui doivent être modernisés. Cela est dû au fait qu'ils sont basés sur des langages de programmation archaïques, sont sujets à des failles de sécurité et sont difficiles à maintenir.

Êtes-vous dans la même situation ?

Dans cet article, je vais parler franchement des défis auxquels vous serez confronté lors de la maintenance des applications logicielles héritées, et comment vous pouvez les surmonter.

## Les systèmes hérités sont inefficaces

La maintenance logicielle est importante – elle aide à améliorer l'efficacité du produit et réduit la marge d'erreur. Sans maintenance suffisante, une application peut devenir inefficace et difficile à utiliser.

Tout d'abord, maintenir [un système hérité](https://www.freecodecamp.org/news/conquer-legacy-code-f9e23a6ab758/) peut être difficile car le code utilisé est ancien par rapport au code utilisé dans tout logiciel moderne. L'ancien code a tendance à être volumineux, long et incompatible avec la plupart des systèmes modernes.

Par exemple, les fonctions fléchées JavaScript, introduites dans ES6 en 2015, offrent aux développeurs un moyen d'écrire une syntaxe de fonction plus courte et plus propre, plus facile à maintenir.

```javascript
let total = (x, y) => x + y;

/* Cette fonction fléchée est une forme plus courte de :
let total = function(x, y) {
  return x + y;
};
*/

console.log(total(5, 2) ); 
// 7

```

## Coûts de maintenance élevés

Un autre défi auquel sont confrontés la plupart des systèmes hérités est le coût élevé de la maintenance, qui peut être hors de portée pour la plupart des entreprises.

Par exemple, selon le rapport du GAO mentionné ci-dessus, le gouvernement américain prévoyait de dépenser plus de 90 milliards de dollars en 2019 pour les services informatiques, dont la majeure partie est allée à la maintenance des systèmes vieillissants.

De plus, à mesure que la technologie évolue, la conformité devient un problème majeur pour la protection des applications destinées aux consommateurs. Atteindre la conformité avec les systèmes hérités est chronophage et coûteux. Cela ne se fera pas aussi rapidement que pour les nouvelles applications, souvent conformes par défaut. Cela nécessite également beaucoup de tests pour s'assurer qu'une infrastructure héritée est conforme aux réglementations données.

Le coût de la maintenance d'un système hérité augmente souvent avec le temps, à mesure qu'il devient lentement obsolète en raison des avancées technologiques. De plus, la modification d'un système existant est une entreprise risquée, qui nécessite beaucoup de temps et de ressources.

## Manque de compétences suffisantes

Pour maintenir un logiciel hérité, vous avez besoin d'un développeur familiarisé avec son fonctionnement. Cependant, la plupart des développeurs préparent leurs applications pour l'avenir avec de nouvelles technologies. Ainsi, trouver quelqu'un capable de travailler avec un ancien système peut être un défi.

Dans certains cas, vous devrez peut-être réformer les développeurs sur le fonctionnement du système hérité, ce qui augmente les coûts opérationnels d'une entreprise.

De plus, gérer et contrôler les changements survenant dans le logiciel peut être difficile. Beaucoup de temps et d'efforts sont nécessaires pour maintenir les systèmes opérationnels, ce qui est coûteux et chronophage.

## Incompatibilité avec d'autres solutions informatiques

Actuellement, il existe des outils modernes qui peuvent être utilisés pour permettre une maintenance rapide et fluide des logiciels. Cependant, la plupart des infrastructures informatiques héritées sont incompatibles avec de telles solutions, ce qui complique leur maintenance.

Si les fonctionnalités d'un système hérité ne sont pas compatibles avec celles des nouvelles solutions informatiques, les développeurs peuvent trouver difficile de les intégrer dans leurs environnements.

La difficulté d'introduire de nouvelles fonctionnalités dans les systèmes hérités ajoute également aux défis de leur maintenance. Comme la plupart des systèmes hérités se cassent facilement, essayer de les restructurer et de les rendre plus maintenables peut ne pas fonctionner comme prévu.

## Solutions aux défis

Pour rivaliser favorablement dans le paysage informatique dynamique d'aujourd'hui, les technologies héritées ont besoin de modernisation. Les applications héritées mises à jour conduisent à une productivité accrue des utilisateurs, à une réduction des coûts de maintenance et à des expériences plus utiles.

Selon une récente étude d'[Avanade](https://www.avanade.com/en/media-center/press-releases/it-modernization-research), la modernisation des systèmes informatiques peut conduire à une croissance des revenus d'environ 14 %. Par conséquent, choisir [différentes options de modernisation de logiciels](https://www.scnsoft.com/services/application/modernization) pourrait entraîner des avantages significatifs pour votre entreprise.

Il est important de noter que les logiciels ne doivent pas être déclarés obsolètes simplement parce qu'ils sont anciens. Certains des logiciels « anciens » peuvent encore contenir des fonctionnalités riches, qui peuvent être utiles au fonctionnement optimal d'une application.

Par conséquent, pour surmonter les défis de la maintenance des logiciels vieillissants, les développeurs peuvent opter pour le refactoring du code source du système. De cette façon, ils peuvent utiliser un code propre et moderne qui est réutilisable et facile à déboguer.

Lors du refactoring, vous modifiez votre système logiciel pour améliorer sa structure interne. Mais vous n'interférez pas avec le comportement externe du code. De cette façon, les fonctionnalités du logiciel sont optimisées grâce aux améliorations internes du code.

Lors du refactoring du code hérité, les mises à jour et les modifications doivent être suffisamment testées pour éviter les ruptures et le mauvais fonctionnement de l'application. Par exemple, des tests de régression peuvent être effectués pour s'assurer que tout fonctionne comme souhaité.

De plus, lorsque les ressources le permettent, les développeurs peuvent opter pour la réécriture de l'ensemble du code source du logiciel, tout en employant des approches de programmation modernes.

Si vous souhaitez continuer à maintenir votre code hérité sans le casser, vous pouvez utiliser l'une des trois méthodes suivantes :

1. Identifier les points de changement dans le code
2. Isoler votre code
3. Envelopper le code

Parlons de chacune des méthodes.

### Identifier les points de changement dans le code

Comme souligné précédemment, maintenir un code hérité peut être difficile. Parfois, le problème peut être causé par une section qui a été mal programmée. Par conséquent, vous pouvez surmonter cela en identifiant un emplacement qui vous permet de changer le comportement de l'application sans altérer le code source.

Par exemple, supposons que vous avez le code JavaScript suivant dans une application héritée qui se connecte à une base de données :

```js
export class DataConnection {
     // du code ici

  connector() {
    // du code pour se connecter à la base de données
  }
}
```

Si vous souhaitez exécuter des tests sur le code ci-dessus mais que la méthode **connector()** pose des problèmes, vous pouvez identifier où modifier le comportement du code sans affecter le code source.

Dans ce cas, vous pouvez étendre la classe **DataConnection** et l'empêcher d'établir une connexion à une base de données réelle :

```js
class FakeConnection extends DataConnection {
  
    connector() {
    // résoudre les problèmes d'appels à la base de données
        
    console.log("Établissement d'une connexion")
  }
}
```

Par conséquent, après avoir modifié le comportement du code sans affecter le code source, vous pouvez exécuter des tests sur le code et le maintenir sans aucun problème.

### Isoler votre code

Une autre technique qui peut vous permettre de maintenir facilement votre code hérité consiste à l'isoler et à apporter des modifications dans un environnement différent. Vous devez simplement identifier un point d'insertion où vous pouvez appeler ce code modifié à partir du code hérité existant.

Voici un exemple :

```js
class BooksData {
  // du code ici

  addBooks(books) {
    for (let book of books) {
      book.addDate()
    }

    // du code ici

    booksRecords.getNumberOfBooks().add(books)
  }

  // du code ici
}
```

Supposons que vous souhaitiez optimiser la référence **books** dans le code hérité ci-dessus, mais que **addBooks()** vous pose des problèmes.

Vous pouvez donc isoler le code dans une nouvelle méthode, comme **newBooks().**

Ensuite, vous pouvez exécuter des tests sur cette nouvelle méthode avec succès car elle est séparée du reste du code. Par la suite, vous pouvez inclure un appel à la nouvelle méthode dans le code existant, non modifié. De cette façon, il y aura des changements minimaux et des risques minimaux pour le code hérité.

Voici comment :

```js
class BooksData {
  // du code ici

  newBooks(books) {
    // une logique intelligente et testable pour optimiser les livres
  }

  addBooks(books) {
    const newBooks = this.newBooks(books)

    for (let book of newBooks) {
      book.addDate()
    }

    // du code ici

     booksRecords.getNumberOfBooks().add(books)
  }

  // du code ici
}
```

### Envelopper le code

Si vous souhaitez apporter des modifications qui doivent avoir lieu avant ou après le code existant, l'envelopper peut également être une autre solution.

Vous pouvez y parvenir en donnant à l'ancienne méthode que vous souhaitez envelopper un nouveau nom, en ajoutant une nouvelle méthode avec le même nom et la même signature que l'ancienne méthode, et en appelant la nouvelle méthode à partir de la nouvelle méthode. Enfin, vous devez placer la nouvelle logique avant ou après l'appel de l'ancienne méthode.

Avec la nouvelle logique, vous pouvez exécuter des tests ou apporter des modifications que vous souhaitez – sans affecter le code source.

Par exemple, voici le code que nous avons utilisé précédemment :

```js
class BooksData {
  // du code ici

  addBooks(books) {
    for (let book of books) {
      book.addDate()
    }

    // du code ici

    booksRecords.getNumberOfBooks().add(books)
  }

  // du code ici
}
```

Voici comment résoudre le problème par enveloppement :

```js
class BooksData {
  // du code ici

  addBooks(books) {
    // une logique intelligente pour obtenir des livres
    this.addMoreNewBooks(moreBooks)
  }

  addMoreNewBooks(books) {
    for (let book of books) {
      book.addDate()
    }

    // du code ici

    booksRecords.getNumberOfBooks().add(books)
  }

  // du code ici
}
```

## Conclusion

Bien que la modernisation des logiciels antiques soit compliquée, exigeante et risquée, les résultats valent généralement le risque. Continuer à dépendre des systèmes informatiques hérités revient à continuer à utiliser la poste pour envoyer un message urgent, alors qu'un email pourrait faire l'affaire en un clic.

De plus, en tant que programmeur, vous équipez-vous de compétences de codage modernes ? Ou bien, vous appuyez-vous encore sur des approches anciennes ?

Par exemple, dans le monde passionnant de la programmation JavaScript, nous avons assisté à une montée en puissance des frameworks, comme React et Angular, qui définissent l'avenir du langage. Passer du temps à les apprendre pourrait vous éviter de tomber dans l'obsolescence.

Êtes-vous d'accord ?