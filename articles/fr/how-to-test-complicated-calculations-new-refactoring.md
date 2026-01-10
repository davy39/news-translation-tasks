---
title: Comment simplifier et rendre plus expressifs les tests de calcul avec ces nouveaux
  refactorings
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2021-02-03T17:32:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-complicated-calculations-new-refactoring
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/unit-testing-calculations.JPG
tags:
- name: refactoring
  slug: refactoring
- name: Testing
  slug: testing
- name: unit testing
  slug: unit-testing
seo_title: Comment simplifier et rendre plus expressifs les tests de calcul avec ces
  nouveaux refactorings
seo_desc: 'It is a good idea to make tests as descriptive as possible – to achieve
  Tests as Documentation. Including the calculations in the test is a big part of
  this, and avoids the Hard Coded Test Data smell.

  For example, if a test looks like this, it is har...'
---

Il est judicieux de rendre les tests aussi descriptifs que possible pour atteindre l'objectif de [Tests as Documentation](http://xunitpatterns.com/Goals%20of%20Test%20Automation.html#Tests%20as%20Documentation). Inclure les calculs dans les tests fait partie intégrante de cette approche et évite l'odeur de code [Hard Coded Test Data](http://xunitpatterns.com/Obscure%20Test.html#Hard-Coded%20Test%20Data).

Par exemple, si un test ressemble à ceci, il est difficile de savoir quel est le problème lorsqu'il échoue, car les données de test sont toutes codées en dur. Le test ne vous donne que très peu d'informations sur la manière dont le système sous test (SUT) devrait se comporter, et ne sert donc pas de documentation.

```python
assert sut.wake_erosion_rate(0.03) == 0.8

```

Cependant, si vous supprimez cette odeur de code et incluez le calcul dans le test, il devient évident de savoir quel est le problème en cas d'échec, et le test sert alors de documentation.

Vous pourriez également vouloir remplacer les valeurs `2.5` et `0.05` par les noms des constantes qu'elles représentent.

```python
ambient_turbuluence = 0.03

assert 
    sut.wake_erosion_rate(ambient_turbuluence) 
    == 2.5 * ambient_turbuluence + 0.05

```

Cet article fait référence au livre excellent [XUnit Test Patterns book](https://www.goodreads.com/review/show/2179089513), qui définit le lexique le plus largement accepté sur les motifs et pratiques des tests unitaires.

## Exemple de calcul

Le reste de cet article discutera de la [classe ConstructionMarginCalculator](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator.py#L31), et décrira les refactorings qui simplifient les tests et permettent d'inclure les calculs de manière réalisable.

Le calcul fait environ 30 lignes de long, et vaut un rapide coup d'œil si vous avez le temps. Mais si ce n'est pas le cas, ne vous inquiétez pas, le reste de cet article aura toujours du sens.

Il y a quelques instructions conditionnelles et une boucle, et au total, cela conduit à 2^9, ou 512, chemins à travers le code ! Eek ! Il est clairement pas réalisable (ou utile) de tester tous ces chemins, d'où la nécessité de trouver des moyens de simplifier cela.

Cet exemple de code a un [test naïf initial](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator.py#L17), qui fait environ 30 lignes de long. Il n'inclut pas les calculs, et les introduire rendrait le test encore plus long et plus compliqué, donc difficile à justifier.

Chacune des sections suivantes décrit un refactoring, et inclut des liens vers le code exemple refactorisé. Ces refactorings s'appuient sur les [test refactorings](http://xunitpatterns.com/Test%20Refactorings.html) existants de [XUnit Test Patterns](https://www.goodreads.com/review/show/2179089513).

Les refactorings réduisent le nombre de chemins à travers le code et simplifient les tests. Cela signifie que moins de tests sont nécessaires, et que les tests deviennent suffisamment petits et simples pour inclure les calculs.

## Extraire le calcul de la boucle

Le code calcule initialement des valeurs pour une _liste de_ `steps`, ce qui signifie que tout test pour celui-ci doit prendre en charge cette complication.

La configuration du test est plus difficile, car nous devons créer une liste plutôt qu'une seule valeur. Les assertions sont plus difficiles car nous devons faire des assertions sur une liste plutôt que sur une seule valeur. Enfin, nous devrions avoir plusieurs tests (probablement pour 0, 1 et plusieurs éléments dans la liste).

La solution facile est simplement de refactoriser le code pour qu'il ne calcule qu'un seul `step`. Cela déplace le code d'itération vers un autre endroit, qui pourrait avoir besoin d'être testé. Cependant, cela peut être testé en utilisant un Mock, donc seule l'itération doit être testée (par opposition à l'itération _et_ le calcul), ce qui est simple, et potentiellement si simple que vous n'avez pas besoin de le tester.

Ce refactoring signifie qu'au lieu de nécessiter 3 tests (pour 0, 1 et plusieurs éléments dans la liste), il n'y en a maintenant qu'un seul. Cela réduit le nombre de chemins à travers le code de 2^9 à 2^7, ou 128. C'est déjà beaucoup mieux, mais toujours trop pour être testé !

* [Calcul refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_without_loop.py#L31)
* [Test refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_remove_loop.py#L11)

## Introduire des abstractions mockables

Les détails du calcul de l'inflation ne sont pas montrés dans l'exemple, mais ils sont raisonnablement compliqués.

Pour éviter cela, nous pouvons modifier le code pour accepter un `InflationCalculator`. Le calcul de l'inflation utilise toujours la même `date_of_financial_close`, `inflation_rate` et `inflation_mode`, ce qui signifie qu'il peut prendre ces valeurs dans le constructeur. Cela signifie à son tour que le calcul principal n'a plus besoin de `inflation_rate` et `inflation_mode`.

Ensuite, dans les tests, nous pouvons créer un mock `InflationCalculator`. Celui-ci pourrait, par exemple, toujours retourner une valeur de `2`, ce qui rend le calcul global beaucoup plus simple.

Il est également facile d'imaginer que les calculs d'inflation se produisent dans d'autres parties du code, donc l'abstraction sera largement utile.

Cette étape signifie qu'au lieu de 4 branches conditionnelles dans le calcul de l'inflation, il n'y en a maintenant qu'une seule. Cela réduit le nombre de chemins à travers le code de 2^7 à 2^3, ou seulement 8. Il est également nécessaire de tester le `InflationCalculator`, et celui-ci a 4 branches, donc il a besoin de 4 tests, mais cela ne fait toujours que 12 tests au total. Hourra pour le code faiblement couplé !

Nous avons maintenant un nombre réalisable de tests à écrire, mais inclure le calcul dans le test reste très fastidieux. Heureusement, nous avons encore quelques refactorings dans notre manche.

* [Calcul refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_mockable_abstraction.py#L29)
* [Test refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_mockable_abstraction.py#L11)

## Tester les branches conditionnelles en isolation

Le code se divise en fonction de certaines conditions. Nous pouvons simplement rendre certaines de ces conditions `False`, puis tester chaque branche du code en isolation. De cette manière, chaque test n'a qu'à inclure le calcul pour la branche qui le concerne.

Par exemple, nous pouvons définir `in_selling_mode` comme étant `False` et `step.start_of_step` comme étant différent de `date_of_financial_close`. Cela rend le test suffisamment simple pour qu'il soit réalisable de faire le même calcul que le code.

Cela signifie à son tour que le test communique clairement que le `turbine_cost_including_margin` devrait être le `turbine_costs * fraction_of_spend * inflation`. Cela aide les lecteurs à comprendre le calculateur, et atteint l'objectif de [Tests as Documentation](http://xunitpatterns.com/Goals%20of%20Test%20Automation.html#Tests%20as%20Documentation).

Pour l'instant, le test est encore assez long. Cependant, comme nous ne testons qu'une petite partie du calcul, beaucoup de ces informations sont maintenant irrelevantes (la variable `any_double`). Cela signifie que nous pouvons maintenant créer un [Test Data Builder](http://natpryce.com/articles/000714.html), ou utiliser des fonctions d'aide pour rendre les choses plus concises. Nous verrons un exemple de cela dans le prochain refactoring.

* [Aucun changement dans le calcul](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_mockable_abstraction.py#L29)
* [Test refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_isolate_branches.py#L16)

## Tester les valeurs en isolation

"Test Conditional Branches in Isolation" est une technique utile, mais elle peut encore nous laisser avec certaines complications si une valeur est calculée/mise à jour dans plusieurs branches.

Un bon exemple de cela est `balance_of_plant_cost_including_margin`, qui est défini initialement, puis mis à jour dans la branche `if (in_selling_mode)`.

Tester `balance_of_plant_cost_including_margin` en isolation permet au test de se concentrer uniquement sur cette valeur/calcul, ce qui signifie que beaucoup moins de configuration est nécessaire. Le motif [Test Data Builder](http://natpryce.com/articles/000714.html) masque les [Irrelevant Information](http://xunitpatterns.com/Obscure%20Test.html#Irrelevant%20Information), et le test devient plus concis et expressif.

Inclure le calcul continue de rendre le test communiquer clairement son intention et agit comme une documentation. Intéressamment, le code de calcul du test n'est plus une copie exacte du code de calcul du SUT, car il sait déjà qu'il est en `in_selling_mode`, donc il n'a pas besoin d'une instruction conditionnelle. Cela signifie que le test est plus simple que le code, ce qui aide à éviter l'odeur de [Obscure Test](http://xunitpatterns.com/Obscure%20Test.html).

* [Aucun changement dans le calcul](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_mockable_abstraction.py#L29)
* [Test refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_isolate_values.py#L18)

## Tester les valeurs partielles en isolation

Parfois, le calcul des valeurs individuelles est très complexe et ne peut pas être divisé par des branches conditionnelles. Cela peut rendre difficile l'inclusion du calcul dans le test. `construction_profit` est un exemple raisonnable de cela, qui est calculé comme suit :

```python
step.turbine_cost_including_margin = 
 turbine_costs * inflation * fraction_of_spend;

step.balance_of_plant_cost_including_margin = 
 balance_of_plant_costs_at_financial_close * inflation * fraction_of_spend;

step.construction_profit = 
 -1 * 
 (step.turbine_cost_including_margin + step.balance_of_plant_cost_including_margin) *
 epc_margin

```

`inflation`, `fraction_of_spend` et `epc_margin` ont un effet multiplicatif, donc si nous les définissons à `1`, ils n'auront aucun effet et nous pourrons facilement écrire un test pour le reste de la logique.

`step.turbine_cost_including_margin` et `step.balance_of_plant_cost_including_margin` ont un effet additif, donc si nous les définissons à `0`, encore une fois, ils n'auront aucun effet et nous pourrons facilement écrire un test pour le reste de la logique.

Tester seulement une portion de `construction_profit` en isolation permet au test de se concentrer uniquement sur cette partie du calcul, ce qui, comme avant, rend le test plus court et plus simple, et évite l'odeur de [Obscure Test](https://hackmd.io/4xuiUbrAQimsWCknJiqXNw?both).

* [Aucun changement dans le calcul](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_mockable_abstraction.py#L29)
* [Test refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_isolate_partial_values.py#L14)

## Introduire le motif Blackboard

Le motif Blackboard est une technique plus complexe et souvent mal comprise. Mais essentiellement, il implique l'utilisation d'un "blackboard" pour briser les dépendances au sein de calculs compliqués.

Dans cet exemple, le `construction_profit` dépend de `turbine_cost_including_margin` et `balance_of_plant_cost_including_margin`, qui sont eux-mêmes calculés à partir des entrées. Cela rend les tests plus difficiles.

Pour tester le `construction_profit`, vous devez essentiellement aussi tester `turbine_cost_including_margin` et `balance_of_plant_cost_including_margin`.

Lorsque nous introduisons le motif blackboard, un calculateur écrit le `turbine_cost_including_margin` et `balance_of_plant_cost_including_margin` sur le blackboard, et lors du calcul du `construction_profit`, nous lisons ces valeurs à partir du blackboard.

Cela brise la connexion entre les deux choses, donc lors des tests, nous pouvons simplement ajouter des valeurs pour `turbine_cost_including_margin` et `balance_of_plant_cost_including_margin` au blackboard.

* [Calcul refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_blackboard_pattern.py#L15)
* [Test refactorisé](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_blackboard_pattern.py#L12)

## Conclusion

Lors des tests de calculs, il est important d'inclure le calcul dans les tests. Cela évite l'odeur de [Hard Coded Test Data](http://xunitpatterns.com/Obscure%20Test.html#Hard-Coded%20Test%20Data), permet aux tests d'exprimer clairement leur intention et d'atteindre [Tests as Documentation](http://xunitpatterns.com/Goals%20of%20Test%20Automation.html#Tests%20as%20Documentation).

Les refactorings décrits dans cet article vous permettent de faire cela tout en vous assurant que les tests sont concis et compréhensibles.