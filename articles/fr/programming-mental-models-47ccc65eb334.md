---
title: Le Grand Concours de Jargon de Programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-20T16:29:43.000Z'
originalURL: https://freecodecamp.org/news/programming-mental-models-47ccc65eb334
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d55K-aHn7CPPe-M83e_n5g.jpeg
tags:
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le Grand Concours de Jargon de Programmation
seo_desc: 'By Preethi Kasireddy

  Imperative vs. Declarative. Pure vs. Impure. Static vs. Dynamic.

  Terminology like this is sprinkled throughout programming blog posts, conference
  talks, papers, and text books.

  But don’t be turned off by this jargon. Let’s jump r...'
---

Par Preethi Kasireddy

Impératif vs. Déclaratif. Pur vs. Impur. Statique vs. Dynamique.

Des termes comme ceux-ci sont éparpillés dans les articles de blog sur la programmation, les conférences, les articles et les manuels.

Mais ne vous laissez pas rebuter par ce jargon. Plongeons directement et décomposons certains de ces concepts, afin que vous puissiez comprendre de quoi parlent tous ces développeurs autour de vous.

### Typage Statique vs. Dynamique

Cela concerne le moment où les informations de type sont acquises — soit au moment de la compilation, soit à l'exécution.

Vous pouvez utiliser ces informations de type pour détecter les erreurs de type. Une erreur de type se produit lorsqu'une valeur n'est pas du type attendu.

#### Vérification de Type Statique

Le processus de vérification de la sécurité des types d'un programme basé sur l'analyse du code source du programme. En d'autres termes, la vérification des types se fait au moment de la compilation, permettant de détecter les erreurs de type plus tôt.

![Image](https://cdn-media-1.freecodecamp.org/images/GD1KhgaCFzdaiATtb-MnKj3L-ZXUiIoydrc8)

#### Vérification de Type Dynamique

Le processus de vérification de la sécurité des types d'un programme à l'exécution. Avec la vérification de type dynamique, les erreurs de type se produisent à l'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/r0NYTBqJGSc8XLHqK8Et-rMW0tkOd3VI7I5u)

### Typage Fort vs. Faible

Il est important de noter que le typage fort vs. faible n'a pas de signification technique universellement acceptée. Par exemple, même si Java est typé statiquement, chaque fois que vous utilisez la réflexion ou un cast, vous reportez la vérification de type à l'exécution.

De même, la plupart des langages à typage fort convertiront automatiquement entre les entiers et les flottants. Par conséquent, vous devriez éviter d'utiliser ces termes car appeler un système de types "fort" ou "faible" en soi ne communique pas grand-chose.

#### Typage Fort

Dans un langage à typage fort, le type d'une construction ne change pas — un `int` est toujours un `int`, et essayer de l'utiliser comme une `string` entraînera une erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/qQuFtQHI0nVeCYYPFiwmtPXD0I0VtUfQS3VH)

#### Typage Faible

Le typage faible signifie que le type d'une construction peut changer en fonction du contexte. Par exemple, dans un langage à typage faible, la chaîne "123" peut être traitée comme le nombre 123 si vous ajoutez un autre nombre.

Cela signifie généralement que le système de types peut être contourné (invalidant toute garantie) car vous pouvez convertir une valeur d'un type à un autre.

![Image](https://cdn-media-1.freecodecamp.org/images/iKBgNAycyEVpLytn2tivoY3U0wN-osYulEJr)

### Données Mutables vs. Immuables

#### Données Immuables

Lorsque qu'un objet n'est pas modifiable après sa création, vous pouvez dire qu'il est "immuable", ce qui est un mot savant pour "inchangable". Cela signifie que vous allouerez plutôt une nouvelle valeur pour chaque changement.

![Image](https://cdn-media-1.freecodecamp.org/images/D3tF-qLMqDUXzFdHRRXy9jZm5ZrZ-DJVxi-p)

#### Données Mutables

Lorsque vous pouvez modifier un objet après sa création, il est "mutable". Lorsque vous avez une référence à un objet mutable, par exemple, le contenu de l'objet peut changer.

![Image](https://cdn-media-1.freecodecamp.org/images/lKF181TAlPPvUz0ln8VLksubyCYCbs8ocB73)

### Fonctions Pures vs. Impures

#### Fonctions Pures

Une fonction pure a deux qualités :

1. Elle ne dépend que de l'entrée fournie — et non d'un état externe qui pourrait changer pendant son évaluation ou entre les appels.
2. Elle ne provoque aucun effet secondaire observable sémantiquement, comme la modification d'un objet global ou d'un paramètre passé par référence.

![Image](https://cdn-media-1.freecodecamp.org/images/ir5sDGMoxckbC-wpR8JikApucz6DLkkPzGZx)

#### Fonctions Impures

Toute fonction qui ne répond pas à ces deux exigences pour une fonction pure est "impure".

![Image](https://cdn-media-1.freecodecamp.org/images/J02vTF9q3BE9lIYoi2jV1QbJAqjRcMZJBw8L)

### Évaluation Paresseuse vs. Évaluation Impatiente

#### Évaluation Paresseuse

L'évaluation paresseuse n'évalue pas les arguments de fonction sauf si leurs valeurs sont nécessaires pour évaluer l'appel de fonction lui-même.

En d'autres termes, les expressions ne sont évaluées que lorsque l'évaluation d'une autre expression dépend de l'expression actuelle.

La paresse permet aux programmes de calculer des structures de données potentiellement _infinies_ sans planter.

![Image](https://cdn-media-1.freecodecamp.org/images/uxczq1DSf-SYP34fDk02eeBqbbEFaqwsUwP0)

#### Évaluation Impatiente

L'évaluation impatiente — également connue sous le nom d'évaluation stricte — évalue toujours complètement les arguments de fonction avant d'invoquer la fonction. En d'autres termes, une expression est évaluée dès qu'elle est liée à une variable.

![Image](https://cdn-media-1.freecodecamp.org/images/SHUGZI2HS4n8mSPAWoUfWySxt8D4X0N5CXu-)

### Programmation Déclarative vs. Impérative

#### Programmation Déclarative

Les programmes déclaratifs expriment un ensemble d'opérations sans révéler comment elles sont implémentées, ou comment les données circulent à travers elles. Ils se concentrent sur "ce que" le programme doit accomplir (en utilisant des expressions pour décrire la logique) plutôt que sur "comment" le programme doit atteindre le résultat.

Un exemple de programmation déclarative est SQL. Les requêtes SQL sont composées d'instructions qui décrivent à quoi devrait ressembler le résultat d'une requête, tout en abstraisant le processus interne de récupération des données :

```
SELECT EMP_ID, FIRST_NAME, LAST_NAMEFROM EMPLOYEESWHERE CITY = 'SAN FRANCISCO'ORDER BY EMP_ID;
```

Voici un exemple de code déclaratif :

![Image](https://cdn-media-1.freecodecamp.org/images/KJkzhjbfo5EYE2flsvDS9gT0JqAIcKcfklcA)

#### Programmation Impérative

La programmation impérative se concentre sur la description de la manière dont un programme doit atteindre un résultat en utilisant des instructions qui spécifient le flux de contrôle ou les changements d'état. Elle utilise une séquence d'instructions pour calculer un résultat.

Voici un exemple de code impératif :

![Image](https://cdn-media-1.freecodecamp.org/images/nWC5LzuByaWllxXsVXJS1pcYokOWlKxkZor2)

### Avec État vs. Sans État

Un état est une séquence de valeurs calculées progressivement, qui contient les résultats intermédiaires d'un calcul.

#### Avec État

Les programmes avec état ont un mécanisme pour suivre et mettre à jour l'état. Ils ont une mémoire du passé et se souviennent des transactions précédentes qui peuvent affecter la transaction actuelle.

![Image](https://cdn-media-1.freecodecamp.org/images/2MCDlKSDdS9imKRxHECiksWO2jjxjeV1ndVB)

#### Sans État

Les programmes sans état, en revanche, ne gardent pas trace de l'état. Il n'y a pas de mémoire du passé. Chaque transaction est effectuée comme si c'était la première fois. Les programmes sans état donneront la même réponse à la même requête, fonction ou appel de méthode — à chaque fois.

![Image](https://cdn-media-1.freecodecamp.org/images/O4aqQxCiZF-tsYmo4yl34wrLs8wGOsWODvy3)

### Programmation Fonctionnelle vs. Orientée Objet

#### Programmation Fonctionnelle

La programmation fonctionnelle est un paradigme qui met un accent majeur sur l'utilisation de fonctions. Le but de la programmation fonctionnelle est d'utiliser des fonctions pour abstraire les flux de contrôle et les opérations sur les données, et pour éviter les effets secondaires.

Ainsi, la programmation fonctionnelle utilise des fonctions pures et évite les données mutables, ce qui fournit à son tour la _transparence référentielle_.

Une fonction a une transparence référentielle lorsque vous pouvez librement remplacer une expression par sa valeur sans changer le comportement du programme. Dit un peu différemment : pour une entrée donnée, elle retourne toujours les mêmes résultats.

Certains exemples de langages qui mettent l'accent sur la programmation fonctionnelle incluent Haskell, Lisp, Clojure et Elm. Mais vous pouvez utiliser des concepts de programmation fonctionnelle dans la plupart des langages, y compris JavaScript.

#### Programmation Orientée Objet

Le paradigme de programmation orientée objet met un accent majeur sur l'utilisation d'objets. Cela résulte en des programmes qui sont constitués d'objets qui interagissent les uns avec les autres. Ces objets peuvent contenir des données (sous forme de champs ou d'attributs) et des comportements (sous forme de méthodes).

C'est un style de partitionnement (ou d'encapsulation) de l'état d'un programme via des objets pour rendre l'analyse de l'effet des changements tractable [1].

De plus, les programmes orientés objet utilisent l'héritage et/ou la composition comme principaux mécanismes de réutilisation de code. L'héritage signifie qu'une nouvelle classe peut être définie en termes de classes existantes en spécifiant simplement comment la nouvelle classe est différente. Il représente une relation "est-un" (par exemple, une classe Bird qui étend une classe Animal). La composition, en revanche, est lorsque les classes contiennent des instances d'autres classes qui implémentent la fonctionnalité souhaitée. Elle représente une relation "a-un" (par exemple, une classe Bird a une instance d'une classe Wing comme membre).

Le polymorphisme est également un mécanisme important pour la réutilisation de code en programmation orientée objet. C'est lorsque qu'un langage peut traiter des objets différemment en fonction de leur type de données ou de leur classe.

Certains exemples de langages qui mettent l'accent sur la programmation orientée objet incluent Java, C++, Ruby. Encore une fois, vous pouvez appliquer ces concepts dans la plupart des langages, y compris JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/N8MHF9tH7WY137DollJShA9icCiaduLFJS9O)

### Déterministe vs. Non Déterministe

#### Déterministe

Les programmes déterministes retournent toujours le même résultat chaque fois qu'ils sont appelés avec un ensemble spécifique de valeurs d'entrée et le même état donné.

![Image](https://cdn-media-1.freecodecamp.org/images/QZcUv8Ergv0DU4N3SSrR6SFbajhNRXzagcTr)

#### Non Déterministe

Les programmes non déterministes peuvent retourner des résultats différents chaque fois qu'ils sont appelés, même avec le même ensemble spécifique de valeurs d'entrée et d'état initial.

Le non-déterminisme est une propriété de tout système concurrent — c'est-à-dire, tout système où plusieurs tâches peuvent se produire en même temps en s'exécutant sur différents threads. Un algorithme concurrent qui modifie l'état peut se comporter différemment à chaque fois, selon le thread que le planificateur décide d'exécuter.

Par exemple :

```
declare Xthread X=1 endthread X=2 end
```

L'ordre d'exécution des deux threads n'est pas fixe. Nous ne savons pas si X sera lié à 1 ou 2. Le système choisira pendant l'exécution du programme, et il est libre de choisir quel thread exécuter en premier.

Un autre exemple de non-déterminisme :

![Image](https://cdn-media-1.freecodecamp.org/images/V0yGj2uPPh5HUKf25kTgQiGZwLG8eAsRjkXM)

### Ouf ! Nous avons terminé.

Comme toujours, vos commentaires et suggestions sont très importants pour moi. Je lis et prends en compte chaque commentaire, alors n'hésitez pas à répondre !

Enfin, vous pouvez également consulter la [présentation Prezi](http://prezi.com/fftgbgltl-6u/?utm_campaign=share&utm_medium=copy&rc=ex0share) que j'ai créée pour cet article.

[1] Merci à [Kent Beck](https://www.freecodecamp.org/news/programming-mental-models-47ccc65eb334/undefined) pour ses contributions sur ce sujet.