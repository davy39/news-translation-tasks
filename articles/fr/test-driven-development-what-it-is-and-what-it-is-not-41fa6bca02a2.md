---
title: Développement piloté par les tests – Ce que c'est, et ce que ce n'est pas
subtitle: ''
author: Andrea Koutifaris
co_authors: []
series: null
date: '2018-07-02T23:11:08.000Z'
originalURL: https://freecodecamp.org/news/test-driven-development-what-it-is-and-what-it-is-not-41fa6bca02a2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W93Ke-ezhfWJ6cTbmCdaPQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Développement piloté par les tests – Ce que c'est, et ce que ce n'est pas
seo_desc: 'Test driven development has become popular over the last few years. Many
  programmers have tried this technique, failed, and concluded that TDD is not worth
  the effort it requires.

  Some programmers think that, in theory, it is a good practice, but tha...'
---

Le développement piloté par les tests est devenu populaire ces dernières années. De nombreux programmeurs ont essayé cette technique, échoué, et conclu que le TDD ne vaut pas l'effort qu'il nécessite.

Certains programmeurs pensent que, en théorie, c'est une bonne pratique, mais qu'il n'y a jamais assez de temps pour vraiment utiliser le TDD. Et d'autres pensent que c'est essentiellement une perte de temps.

Si vous vous sentez ainsi, je pense que vous ne comprenez peut-être pas ce qu'est vraiment le TDD. (D'accord, la phrase précédente était pour attirer votre attention). Il existe un très bon livre sur le TDD, [Test Driven Development: By Example, par Kent Beck](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530), si vous voulez le consulter et en apprendre davantage.

Dans cet article, je vais passer en revue les fondamentaux du développement piloté par les tests, en abordant les idées fausses courantes sur la technique TDD. Cet article est également le premier d'une série d'articles que je vais publier, tous sur le développement piloté par les tests.

### Pourquoi utiliser le TDD ?

Il existe des études, des articles et des discussions sur l'efficacité du TDD. Même si avoir quelques chiffres est définitivement utile, je ne pense pas qu'ils répondent à la question de savoir pourquoi nous devrions utiliser le TDD en premier lieu.

Disons que vous êtes un développeur web. Vous venez de terminer une petite fonctionnalité. Pensez-vous qu'il est suffisant de tester cette fonctionnalité simplement en interagissant manuellement avec le navigateur ? Je ne pense pas qu'il soit suffisant de se fier uniquement aux tests effectués manuellement par les développeurs. Malheureusement, cela signifie qu'une partie du code n'est pas assez bonne.

Mais la considération ci-dessus concerne les tests, et non le TDD lui-même. Alors pourquoi le TDD ? La réponse courte est « parce que c'est le moyen le plus simple d'obtenir à la fois un code de bonne qualité et une bonne couverture de test ».

La réponse plus longue vient de ce qu'est vraiment le TDD... Commençons par les règles.

### Règles du jeu

[Uncle Bob](https://en.wikipedia.org/wiki/Robert_C._Martin) décrit le TDD avec trois règles :

> * Vous n'êtes pas autorisé à écrire du code de production sauf si c'est pour faire passer un test unitaire en échec.

> * Vous n'êtes pas autorisé à écrire plus de test unitaire que ce qui est suffisant pour échouer ; et les échecs de compilation sont des échecs.

> * Vous n'êtes pas autorisé à écrire plus de code de production que ce qui est suffisant pour faire passer le test unitaire en échec.

J'aime aussi une version plus courte, que j'ai trouvée [ici](http://www.javiersaldana.com/tech/2014/11/26/refactoring-the-three-laws-of-tdd.html) :

> * Écrivez seulement assez de test unitaire pour échouer.

> * Écrivez seulement assez de code de production pour faire passer le test unitaire en échec.

Ces règles sont simples, mais les personnes qui abordent le TDD violent souvent une ou plusieurs d'entre elles. Je vous lance un défi : pouvez-vous écrire un petit projet en suivant **strictement** ces règles ? Par petit projet, j'entends quelque chose de réel, pas juste un exemple qui nécessite environ 50 lignes de code.

Ces règles définissent la mécanique du TDD, mais elles ne sont définitivement pas tout ce que vous devez savoir. En fait, le processus d'utilisation du TDD est souvent décrit comme un cycle Rouge/Vert/Refactorisation. Voyons de quoi il s'agit.

### Cycle Rouge Vert Refactorisation

![Image](https://cdn-media-1.freecodecamp.org/images/JN8oQMbYFGuFdXSJJEybTQ8rCFwVclmyRANN align="left")

*Rouge Vert Refactorisation*

#### Phase Rouge

Dans la phase rouge, vous devez écrire un test sur un comportement que vous êtes sur le point d'implémenter. Oui, j'ai écrit **comportement**. Le mot « test » dans le développement piloté par les tests est trompeur. Nous aurions dû l'appeler « développement piloté par le comportement » dès le départ. Oui, je sais, certaines personnes soutiennent que le BDD est différent du TDD, mais je ne sais pas si je suis d'accord. Donc dans ma définition simplifiée, BDD = TDD.

Voici une idée fausse courante : « D'abord j'écris une classe et une méthode (mais sans implémentation), puis j'écris un test pour tester cette méthode de classe ». En fait, cela ne fonctionne pas ainsi.

Faisons un pas en arrière. Pourquoi la première règle du TDD exige-t-elle que vous écriviez un test avant d'écrire le moindre morceau de code de production ? Sommes-nous des maniaques du TDD ?

Chaque phase du cycle R.G.R. représente une phase dans le cycle de vie du code et comment vous pourriez vous y rapporter.

Dans la phase rouge, vous agissez comme si vous étiez un utilisateur exigeant qui veut utiliser le code qui est sur le point d'être écrit de la manière la plus simple possible. **Vous devez écrire un test qui utilise un morceau de code comme s'il était déjà implémenté.** Oubliez l'implémentation ! Si, dans cette phase, vous pensez à la manière dont vous allez écrire le code de production, vous faites cela de manière incorrecte !

C'est dans cette phase que vous vous concentrez sur l'écriture d'une interface propre pour les futurs utilisateurs. **C'est la phase où vous concevez comment votre code sera utilisé par les clients.**

Cette première règle est la plus importante et c'est la règle qui rend le TDD différent des tests réguliers. Vous écrivez un test afin de pouvoir ensuite écrire du code de production. Vous n'écrivez pas un test pour tester votre code.

Regardons un exemple.

```python
// LeapYear.spec.js
describe('Calculateur d'année bissextile', () => {
  it('devrait considérer 1996 comme bissextile', () => {
    expect(LeapYear.isLeap(1996)).toBe(true);
  });
});
```

Le code ci-dessus est un exemple de la façon dont un test pourrait ressembler en JavaScript, en utilisant le framework de test Jasmine. Vous n'avez pas besoin de connaître Jasmine — il suffit de comprendre que `it(...)` est un test et que `expect(...).toBe(...)` est une manière de faire vérifier à Jasmine si quelque chose est tel qu'attendu.

Dans le test ci-dessus, j'ai vérifié que la fonction `LeapYear.isLeap(...)` retourne `true` pour l'année 1996. Vous pourriez penser que 1996 est un nombre magique et donc une mauvaise pratique. Ce n'est pas le cas. Dans le code de test, les nombres magiques sont bons, alors que dans le code de production, ils doivent être évités.

Ce test a en fait quelques implications :

* Le nom du calculateur d'année bissextile est `LeapYear`

* `isLeap(...)` est une méthode statique de `LeapYear`

* `isLeap(...)` prend un nombre (et non un tableau, par exemple) comme argument et retourne `true` ou `false`.

C'est un test, mais il a en fait de nombreuses implications ! Avons-nous besoin d'une méthode pour dire si une année est bissextile, ou avons-nous besoin d'une méthode qui retourne une liste d'années bissextiles entre une date de début et une date de fin ? Les noms des éléments sont-ils significatifs ? Ce sont les types de questions que vous devez garder à l'esprit lors de l'écriture de tests dans la phase Rouge.

Dans cette phase, vous devez prendre des décisions sur la manière dont le code sera utilisé. Vous basez cela sur ce dont vous avez vraiment besoin à ce moment-là et non sur ce que vous pensez qui pourrait être nécessaire.

Voici une autre erreur : ne pas écrire un ensemble de fonctions/classes que vous pensez pouvoir avoir besoin. Concentrez-vous sur la fonctionnalité que vous implémentez et sur ce qui est vraiment nécessaire. Écrire quelque chose que la fonctionnalité ne nécessite pas est de la sur-ingénierie.

Et l'abstraction ? Nous verrons cela plus tard, dans la phase de refactorisation.

#### Phase Verte

C'est généralement la phase la plus facile, car dans cette phase vous écrivez du code (de production). Si vous êtes un programmeur, vous faites cela tout le temps.

Voici une autre grande erreur : au lieu d'écrire assez de code pour faire passer le test rouge, vous écrivez tous les algorithmes. En faisant cela, vous pensez probablement à ce qui est l'implémentation la plus performante. Pas question !

Dans cette phase, vous devez agir comme un programmeur qui a une tâche simple : écrire une solution directe qui fait passer le test (et fait en sorte que le rouge alarmant dans le rapport de test devienne un vert amical). Dans cette phase, vous êtes autorisé à violer les meilleures pratiques et même à dupliquer du code. La duplication de code sera supprimée dans la phase de refactorisation.

Mais pourquoi avons-nous cette règle ? Pourquoi ne puis-je pas écrire tout le code qui est déjà dans mon esprit ? Pour deux raisons :

* Une tâche simple est moins sujette aux erreurs, et vous voulez minimiser les bugs.

* Vous ne voulez définitivement pas mélanger du code qui est en cours de test avec du code qui ne l'est pas. Vous pouvez écrire du code qui n'est pas en cours de test (aka legacy), mais la pire chose que vous puissiez faire est de mélanger du code testé et non testé.

Et le code propre ? Et la performance ? Et si l'écriture de code me fait découvrir un problème ? Et les doutes ?

La performance est une longue histoire, et est hors du cadre de cet article. Disons simplement que l'optimisation de la performance dans cette phase est, la plupart du temps, une optimisation prématurée.

La technique de développement piloté par les tests fournit deux autres choses : une liste de tâches et la phase de refactorisation.

La phase de refactorisation est utilisée pour nettoyer le code. La liste de tâches est utilisée pour écrire les étapes nécessaires pour compléter la fonctionnalité que vous implémentez. Elle contient également les doutes ou les problèmes que vous découvrez pendant le processus. Une liste de tâches possible pour le calculateur d'année bissextile pourrait être :

```python
Fonctionnalité : Toute année exactement divisible par quatre est une année bissextile, sauf pour les années exactement divisibles par 100, mais ces années centuriales sont bissextiles si elles sont exactement divisibles par 400.
```

```python
- divisible par 4
- mais pas par 100
- les années divisibles par 400 sont bissextiles de toute façon
```

```python
Qu'en est-il des années bissextiles dans le calendrier julien ? Et des années avant le calendrier julien ?
```

La liste de tâches est vivante : elle change pendant que vous codez et, idéalement, à la fin de l'implémentation de la fonctionnalité, elle sera vide.

#### Phase de Refactorisation

Dans la phase de refactorisation, vous êtes autorisé à changer le code, tout en gardant tous les tests verts, afin qu'il devienne meilleur. Ce que signifie « meilleur » dépend de vous. Mais il y a quelque chose d'obligatoire : **vous devez supprimer la duplication de code**. Kent Beck suggère dans son livre que supprimer la duplication de code est tout ce que vous devez faire.

Dans cette phase, vous jouez le rôle d'un programmeur pointilleux qui veut corriger/refactoriser le code pour l'amener à un niveau professionnel. Dans la phase rouge, vous montrez vos compétences à vos utilisateurs. Mais dans la phase de refactorisation, vous montrez vos compétences aux programmeurs qui liront votre implémentation.

Supprimer la duplication de code entraîne souvent une abstraction. Un exemple typique est lorsque vous déplacez deux morceaux de code similaires dans une classe d'assistance qui fonctionne pour les deux fonctions/classes où le code a été supprimé.

Par exemple, le code suivant :

```python
class Hello {
  greet() {
    return new Promise((resolve) => {
      setTimeout(()=>resolve('Hello'), 100);
    });
  }
}

class Random {
  toss() {
    return new Promise((resolve) => {
      setTimeout(()=>resolve(Math.random()), 200);
    });
  }
}

new Hello().greet().then(result => console.log(result));
new Random().toss().then(result => console.log(result));
```

pourrait être refactorisé en :

```python
class Hello {
  greet() {
    return PromiseHelper.timeout(100).then(() => 'hello');
  }
}

class Random {
  toss() {
    return PromiseHelper.timeout(200).then(() => Math.random());
  }
}

class PromiseHelper {
  static timeout(delay) {
    return new Promise(resolve => setTimeout(resolve, delay));
  }
}

const logResult = result => console.log(result);
new Hello().greet().then(logResult);
new Random().toss().then(logResult);
```

Comme vous pouvez le voir, afin de supprimer la duplication de code `new Promise` et `setTimeout`, j'ai créé une méthode `PromiseHelper.timeout(delay)`, qui sert à la fois les classes `Hello` et `Random`.

Gardez simplement à l'esprit que vous ne pouvez pas passer à un autre test tant que vous n'avez pas supprimé toute la duplication de code.

### Considérations finales

Dans cette section, je vais essayer de répondre à quelques questions et idées fausses courantes sur le développement piloté par les tests.

* Le T.D.D. nécessite beaucoup plus de temps que la programmation « normale » !

Ce qui nécessite vraiment beaucoup de temps, c'est l'apprentissage/la maîtrise du TDD ainsi que la compréhension de la manière de configurer et d'utiliser un environnement de test. Lorsque vous êtes familier avec les outils de test et la technique TDD, cela ne nécessite en fait pas plus de temps. Au contraire, cela aide à garder un projet aussi simple que possible et économise ainsi du temps.

* Combien de tests dois-je écrire ?

La quantité minimale qui vous permet d'écrire tout le code de production. La quantité minimale, car chaque test ralentit la refactorisation (lorsque vous changez le code de production, vous devez corriger tous les tests en échec). D'un autre côté, la refactorisation est beaucoup plus simple et plus sûre sur du code sous tests.

* Avec le développement piloté par les tests, je n'ai pas besoin de passer du temps sur l'analyse et la conception de l'architecture.

Cela ne pourrait pas être plus faux. Si ce que vous allez implémenter n'est pas bien conçu, à un certain moment vous penserez « Ouch ! Je n'ai pas considéré... ». Et cela signifie que vous devrez supprimer le code de production et de test. Il est vrai que le TDD aide avec la recommandation « Juste assez, juste à temps » des techniques agiles, mais ce n'est définitivement pas un substitut à la phase d'analyse/conception.

* La couverture de test doit-elle être de 100 % ?

Non. Comme je l'ai dit plus tôt, ne mélangez pas le code testé et non testé. Mais vous pouvez éviter d'utiliser le TDD sur certaines parties d'un projet. Par exemple, je ne teste pas les vues (bien que de nombreux frameworks rendent les tests d'interface utilisateur faciles) car elles sont susceptibles de changer souvent. Je m'assure également qu'il y a très peu de logique à l'intérieur des vues.

* Je suis capable d'écrire du code avec très peu de bugs, je n'ai pas besoin de tests.

Vous pouvez être capable de faire cela, mais cette considération est-elle valable pour tous les membres de votre équipe ? Ils modifieront éventuellement votre code et le casseront. Ce serait bien si vous écriviez des tests afin qu'un bug puisse être repéré immédiatement et non en production.

* Le TDD fonctionne bien sur des exemples, mais dans une application réelle, beaucoup de code n'est pas testable.

J'ai écrit un Tetris entier (ainsi que des applications web progressives au travail) en utilisant le TDD. Si vous testez d'abord, le code est clairement testable. C'est plus une question de comprendre comment simuler les dépendances et comment écrire des tests simples mais efficaces.

* Les tests ne doivent pas être écrits par les développeurs qui écrivent le code, ils doivent être écrits par d'autres, de préférence des personnes de l'assurance qualité.

Si vous parlez de tester votre application, oui, c'est une bonne idée de demander à d'autres personnes de tester ce que votre équipe a fait. Si vous parlez d'écrire du code de production, alors c'est la mauvaise approche.

### Qu'est-ce qui suit ?

Cet article concernait la philosophie et les idées fausses courantes sur le TDD. Je prévois d'écrire d'autres articles sur le TDD où vous verrez beaucoup de code et moins de mots. Si vous êtes intéressé par le développement de Tetris en utilisant le TDD, restez à l'écoute !