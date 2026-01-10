---
title: Obtenez une pratique concrète du développement piloté par les tests en C#
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-17T00:00:22.000Z'
originalURL: https://freecodecamp.org/news/tdd-explanation-hands-on-practice-with-c-a0124338be44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yZhtCFidrT5-pQHw7Bzvdw.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: unit testing
  slug: unit-testing
seo_title: Obtenez une pratique concrète du développement piloté par les tests en
  C#
seo_desc: 'By Moshe Binieli

  So let’s talk about TDD — what is it?

  TDD stands for Test Driven Development, and it’s a design process in software development.
  It relies on the repetition of a very short development cycle, and the requirements
  are turned into very...'
---

Par Moshe Binieli

### Parlons donc du TDD — qu'est-ce que c'est ?

TDD signifie **Test Driven Development** (Développement Piloté par les Tests), et c'est un processus de conception en développement logiciel. Il repose sur la répétition d'un cycle de développement très court, et les exigences sont transformées en cas de test très spécifiques.

Il y a quelques étapes dans le processus TDD :

1. Écrire un test unitaire qui échoue.
2. Écrire suffisamment de code pour faire passer le test — à cette étape, nous ne nous soucions pas du bon code.
3. Refactoriser votre code de l'étape précédente.

![Image](https://cdn-media-1.freecodecamp.org/images/6k9ojiN7VEFUUNKroUU62gZVf2pzzPnC5IbV)
_Cycle de vie du TDD_

### Quels sont les avantages de cette approche ?

Tout d'abord, vous obtenez une meilleure compréhension du code réel avant de l'écrire. C'est l'un des plus grands avantages du TDD. Lorsque vous écrivez les cas de test en premier, vous pensez plus clairement aux **exigences du système** et plus critiquement aux **cas particuliers**.

De plus, en parlant des **dépendances**, il est important de mentionner que travailler avec le TDD vous permet de vous concentrer sur la logique de vos classes. De cette manière, vous gardez toutes les dépendances à l'extérieur de vos classes. Il est également important de mentionner que votre code s'exécutera **plus en sécurité** puisque la logique n'aura pas à gérer différentes dépendances telles que les connexions à la base de données, les systèmes de fichiers, etc.

C'est aussi une manière plus sûre de **refactoriser** le code. Lorsque vous écrivez du TDD, il y a des tests pour une certaine partie de la logique. Lorsque vous refactorisez le code, vous pourriez casser quelque chose, mais avec cette approche, vous savez que les tests vous couvriront.

Lorsque vous utilisez le TDD, vous avez également un moyen plus rapide de **comprendre ce que fait le code**. Lorsque vous commencez à travailler sur une partie de code que vous ne connaissez pas, vous pouvez lire les cas de test de cette partie de code et comprendre son but. Ces tests sont également la **documentation** de votre code.

Et enfin, vous pouvez vous **concentrer** sur la construction des plus petits composants de la meilleure manière et éviter le casse-tête de la vision d'ensemble. Alors, comment cela aide-t-il ? Vous écriverez un test qui échoue, et vous vous concentrerez uniquement sur celui-ci pour le faire passer. Cela vous force à penser à de plus petits morceaux de fonctionnalité à la fois plutôt qu'à l'application dans son ensemble. Ensuite, vous pouvez construire de manière incrémentielle sur un test qui passe, plutôt que d'essayer de traiter la vision d'ensemble dès le départ, ce qui résultera probablement en plus de bugs.

#### Avant de commencer à écrire du TDD...

Pour être honnête, il y a plus d'articles dans lesquels vous pouvez lire encore plus profondément sur le TDD. Par conséquent, j'ai évité d'écrire toute la théorie du TDD ici car cela prendrait très longtemps à tout lire.

Par conséquent, j'ai simplement expliqué l'idée générale et les avantages du processus de conception TDD.

### Il est temps d'écrire quelques tests, alors faisons-le

#### Description et exigences

![Image](https://cdn-media-1.freecodecamp.org/images/x0FilcnpRO96SVtGpXFV84F-8PEfpXxTt63g)

Nous utiliserons C# pour écrire une implémentation de Stack. Pourquoi C# ? Eh bien, parce que j'aime C#, alors pourquoi pas ? 😊

Donc, nos exigences sont assez simples : nous voulons implémenter une classe Stack, donc les exigences sont :

1. Limiter la taille de la stack.
2. Ajouter un élément. (push)
3. Retirer un élément. (pop)
4. Vérifier quel était le dernier élément. (peek)
5. Obtenir la taille actuelle de la stack.
6. Avoir une classe qui peut accepter n'importe quel type de données.
7. Lorsque le client dépasse la taille de la Stack, nous devons lancer une exception appropriée.

Après avoir connu les exigences du système, nous pouvons commencer à définir comment nous allons résoudre cela. Nous l'implémenterons en utilisant un tableau.

#### Implémentation de Stack en TDD — Construction de l'infrastructure

J'utilise Visual Studio 2017. Dans celui-ci, j'ouvrirai un nouveau projet :
**Fichier -> Nouveau -> Projet**, choisissez **Application Console (.NET Framework)**.
Choisissez un nom de projet — comme « Stack ».

![Image](https://cdn-media-1.freecodecamp.org/images/Y2rHhYyKPIUf34LptmaFWnWX-Av0MAXKDsGa)
_Visualisation de la création de projet_

Maintenant, nous allons ouvrir un autre projet pour les tests uniquement et nous l'appellerons « StackTests ».

Ouvrez l'explorateur de solutions. Nous avons un projet appelé « Stack ». Maintenant, cliquez avec le bouton droit sur Solution et choisissez **Ajouter -> Nouveau Projet** et choisissez **Bibliothèque de Classes (.NET Framework)**.

![Image](https://cdn-media-1.freecodecamp.org/images/zaygc8z-e6Wbgq7ZiobS2sajg2OQ3b6AVTfE)
_Visualisation de l'explorateur de solutions_

Installons nos tests unitaires : cliquez avec le bouton droit sur le projet **StackTests**, choisissez **Gérer les Packages NuGet**, naviguez vers **« Parcourir »** et installez les packages suivants :

* NUnit
* NUnit3TestAdapter

Ajoutez une nouvelle classe au projet **StackTests** et appelez-la **StackTest**. Maintenant, la solution devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/UFItJ-fu07ExwLZ-SUNf4eNQ8EpNfgO44sgK)
_Visualisation de l'explorateur de solutions_

Le fichier **packages.config** devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/w0V0nqOXKJyAfosAO4augO3x-yUQIHz2e6nV)
_Visualisation de packages.config_

#### Implémentation de Stack en TDD — Écrire du code

Nous allons commencer à écrire nos tests unitaires dans le projet StackTests sous la classe StackTest.

Avant de pouvoir commencer à écrire le code, nous devons apprendre 3 choses importantes : **TestFixture, Test, et Assert**.

[**TestFixture**](http://nunit.org/docs/2.5/testFixture.html) est l'attribut qui marque une classe qui contient des tests et, optionnellement, des méthodes de [configuration](http://nunit.org/docs/2.2.7/setup.html) ou de [nettoyage](http://nunit.org/docs/2.2.7/teardown.html).

L'attribut [**Test**](http://nunit.org/docs/2.5/test.html) est l'une des façons de marquer une méthode à l'intérieur d'une classe TestFixture comme un test.

La classe [Assert](https://docs.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.assert?view=mstest-net-1.2.0) est une collection de classes d'assistance pour tester diverses conditions dans les tests unitaires. Si la condition testée n'est pas remplie, une exception est levée.

Importez **"NUnit.Framework"** et placez l'attribut **[TestFixture]** au-dessus de votre définition de classe.

![Image](https://cdn-media-1.freecodecamp.org/images/FvlbMWDWWLjdfFB4MXtyE64LvhaC05WglpPD)
_Visualisation de la classe_

#### Test de création

D'accord, il est temps d'écrire notre première fonction. Nous allons écrire un test de création, qui créera un nouvel objet de notre Stack, et il vérifiera que la taille de la Stack est de 0 au début.

![Image](https://cdn-media-1.freecodecamp.org/images/Efn9hvWquRlN12diRyxoFYSfj9NheCxR5PXk)
_Visualisation du test de création_

Maintenant, nous avons écrit notre premier test, alors exécutons-le.

Dans votre barre d'outils, cliquez sur **Test -> Exécuter -> Tous les Tests**.

> Si votre **Explorateur de Tests** n'est pas ouvert, cliquez sur **Test -> Fenêtres -> Explorateur de Tests**, et cela développera l'explorateur de tests.

Comme vous pouvez le voir, nous n'avons même pas notre classe Stack définie, donc nous obtenons une erreur de compilation. Maintenant, écrivons suffisamment de code pour faire passer le test.

Faisons fonctionner notre premier test :

* Créez une nouvelle classe dans le **projet Stack**, et appelez cette classe **"Stack"**. Faites de cette classe une classe de **type générique** (type T).
* Nous avons défini cette classe (Stack) pour être implémentée comme un tableau, donc nous définirons le champ membre comme un **tableau de type T**.
* Nous devons passer la **longueur maximale** de la stack au constructeur, donc nous créerons un constructeur qui prend un argument de taille.
* Et puisque nous exigeons de recevoir la taille actuelle de la stack à tout moment, nous définirons une propriété de **"Size"**. Bien sûr, personne ne pourra changer la taille, donc elle sera **private set**.

![Image](https://cdn-media-1.freecodecamp.org/images/HTO1zWDE-TKb1-ELfK-tzSKJseDCRmhWe1NJ)
_Visualisation de la classe Stack_

Maintenant, exécutons les tests à nouveau (voir ci-dessus comment exécuter les tests) et voyons les résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/fi2gGPLt5xJ2iIWomrWOa8XYIwdFoHYPTXPm)
_Statut des tests_

Et voilà, nous avons fait notre première itération avec la conception TTD ! Maintenant, nous devrions refactoriser notre code — mais à ce stade, nous n'avons vraiment rien à refactoriser, donc nous allons avancer.

#### Test Push & Pop

Maintenant, nous voulons tester la fonctionnalité push et pop, alors créons le cas de test.

* Push prendra un argument et l'ajoutera au sommet de la stack.
* Pop retirera l'élément de la stack et le retournera.

Nous ajouterons 3 éléments à la stack, puis nous prendrons le dernier élément. À ce stade, nous vérifierons que le dernier élément est exactement celui que nous nous attendons à obtenir et que la taille de la stack a diminué.

![Image](https://cdn-media-1.freecodecamp.org/images/AyHjiEOB0bvmEqDIFwbHNHh34TxCOsWsstLE)
_Cas de test Push et Pop_

Comme vous pouvez le voir, les fonctions push et pop n'existent même pas, donc lorsque nous exécutons les tests, nous obtenons un **échec** dans nos résultats de test. Allons dans la **classe Stack** et implémentons-les.

![Image](https://cdn-media-1.freecodecamp.org/images/LqO1cc6vrL2elw1fFoKJ-gqD7eUWplYzQbqO)
_Fonctions Push et Pop_

Exécutons nos tests à nouveau, et boom, tout fonctionne parfaitement ! Tous les tests ont réussi ✨

#### Erreur dépassant la taille autorisée

Nous voulons lancer des exceptions personnalisées lorsque nous :

1. Ajoutons un nouvel élément lorsque la stack est pleine.
2. Retirons un élément lorsqu'il n'y a pas d'éléments dans la stack.

Alors, comme vous le savez déjà... que devrions-nous faire maintenant ?

Correct ! Nous définissons des cas de test, puis nous faisons fonctionner le code.

![Image](https://cdn-media-1.freecodecamp.org/images/lI1Q6ai-kBUQn-1CsTzwaNK8u3BUdfbCJhu-)

Comme vous pouvez le voir, nous devons créer deux nouvelles exceptions personnalisées.

* **ExpenditureProhibitedException** — Cette exception se produira lorsque la stack est vide et que le client tente de retirer un nouvel élément.
* **ExceededSizeException** — Cette exception se produira lorsque la stack est pleine et que le client tente d'ajouter un nouvel élément à la stack.

Allez dans le **projet Stack** et créez une nouvelle classe appelée **CustomExceptions**. Dans cette classe, nous définirons nos nouvelles exceptions et elles hériteront de la classe Exception.

![Image](https://cdn-media-1.freecodecamp.org/images/APKB-pTmAEJqjO4dvZBws5mb-ytLSlPHds8b)
_Exceptions personnalisées_

Modifions notre fonctionnalité push et pop actuelle pour lancer une exception lorsque nécessaire.

![Image](https://cdn-media-1.freecodecamp.org/images/hXEd54LiqrHv57K3nYPOrvnYYfLfTpPRcbtu)
_Exceptions personnalisées_

Donc maintenant, dans le cadre du cycle de vie du TDD, nous exécutons les tests... et Hourra ! Tous les tests ont réussi.

#### Voir le dernier élément

Nous sommes sur le point de terminer avec les derniers tests. Nous voulons voir le dernier élément dans la stack. Si la stack est vide, nous lancerons une exception ExpenditureProhibitedException, sinon, nous retournerons le dernier élément.

Créons nos cas de test.

1. Tentative de voir l'élément lorsque la stack est vide. Dans ce test, nous lancerons une exception personnalisée.
2. Insérer quelques éléments dans la stack, puis voir un élément, s'assurer que c'est le bon élément, et vérifier que la taille du tableau n'a pas changé.

![Image](https://cdn-media-1.freecodecamp.org/images/kOKEws2MilsEGsv3dfdhVQyEOXeie-QPdiAJ)
_Cas de test Peek_

Lorsque nous exécutons les tests, ils échouent — la méthode peek n'existe même pas et il n'y a pas de fonctionnalité.

Nous **créerons** la fonction **Peek** dans la **classe Stack**.

![Image](https://cdn-media-1.freecodecamp.org/images/sGlrLEoqa8jMClXDh4w4idYPz1p543TDmgtN)
_Implémentation de Peek_

Maintenant, lorsque nous exécutons les tests à nouveau, nous pouvons voir que tous passent avec succès.

### En conclusion

Comme vous pouvez le voir, l'idée n'est pas compliquée et il existe de nombreux outils qui aident à implémenter les principes du TDD.

**Vous pouvez voir le code complet sur Pastebin.**

[Classe Stack — Cette classe contient toutes les implémentations de stack.](https://pastebin.com/G8ZnTBns)
[Classe StackTests — Contient tous les cas de test.](https://pastebin.com/5FcMXqYS)
[Classes CustomExceptions — Contient les exceptions requises par le système pour la conception TDD.](https://pastebin.com/z7rWFtxj)

Tous les commentaires et retours sont les bienvenus — si nécessaire, je corrigerai l'article.

N'hésitez pas à me contacter directement sur LinkedIn — [Cliquez Ici](http://www.linkedin.com/in/moshe-binieli-22b11a137).