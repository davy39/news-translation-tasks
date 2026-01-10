---
title: Simplifiez votre planification complexe avec timeboard, une bibliothèque Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-06T14:42:11.000Z'
originalURL: https://freecodecamp.org/news/introducing-timeboard-a-python-business-calendar-package-a2335898c697
coverImage: https://cdn-media-1.freecodecamp.org/images/0*yr9qoXFRXXNOeiZK.
tags:
- name: business
  slug: business
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Simplifiez votre planification complexe avec timeboard, une bibliothèque
  Python
seo_desc: 'By Maxim Mamaev

  timeboard is a Python library that creates schedules of work periods and performs
  calendar calculations over them. You can build standard business day calendars as
  well as a variety of other schedules, simple or complex.

  You can find ...'
---

Par Maxim Mamaev

`timeboard` est une bibliothèque Python qui crée des plannings de périodes de travail et effectue des calculs de calendrier sur ceux-ci. Vous pouvez construire des calendriers de jours ouvrables standard ainsi que divers autres plannings, simples ou complexes.

**Vous pouvez trouver la documentation [ici](http://timeboard.readthedocs.io/en/latest/).**

**Consultez le dépôt GitHub [ici](https://github.com/mmamaev/timeboard).**

**Trouvez-le sur PyPI [ici](https://pypi.python.org/pypi/timeboard).**

### L'histoire

Tout a commencé avec le cas du nombre d'employés. Notre entreprise a introduit des KPI impliquant le revenu par employé, donc nous devions connaître le nombre moyen annuel d'employés de chaque équipe. J'écrivais déjà des scripts Python, donc je n'étais pas intimidé.

Pour obtenir un nombre d'employés, je devais calculer le nombre de jours ouvrables que chaque employé avait passés avec l'entreprise au cours de l'année. Pandas s'en occuperait en un clin d'œil, ai-je pensé. Mais il s'est avéré que Pandas ne pouvait pas.

Le calendrier des jours ouvrables en Russie est encombrant. Ils échangent les jours de la semaine avec les samedis ou dimanches pour combler les écarts entre les jours fériés et les week-ends. Par exemple, vous devez venir travailler un samedi en février pour être remboursé avec un lundi gratuit précédant un mardi férié quelque part en mai.

Le schéma pour chaque année est unique. Le calendrier des jours ouvrables de Pandas ne supporte que les amendements unilatéraux pour les observations des jours fériés. Ainsi, je pouvais transformer un jour ouvrable en un jour de congé, mais pas l'inverse.

Ensuite, il y avait les opérateurs du centre d'appels, et mon anxiété a basculé de l'autre côté. Ils travaillent en équipes de durée variable, et une équipe en service est suivie de trois équipes hors service. Pour obtenir les statistiques du centre d'appels, je n'avais pas besoin du calendrier des jours ouvrables. Pourtant, je devais compter le nombre d'équipes particulières d'un opérateur sur une période de temps.

Et enfin, un problème inhabituel. Dans ma concession Honda locale, les mécaniciens travaillent selon des plannings hebdomadaires alternés : lundi, mardi, samedi et dimanche cette semaine, et mercredi à vendredi la semaine suivante. Je voulais toujours être servi par un mécanicien particulier, car l'autre avait une fois mal réparé les freins. Je voulais une manière simple de déterminer le prochain service de « mon » mécanicien.

Ces cas ont une base commune. Leurs solutions reposeraient sur un planning de périodes « en service » et « hors service ». Nous devrions être capables de construire divers plannings structurés adaptés à différents cas d'entreprise. Les requêtes et calculs exécutés sur le planning doivent distinguer les périodes « en service » et « hors service ».

Je n'ai pas trouvé de package Python qui fournissait les moyens de construire et d'interroger de tels plannings. Comme il se trouve, j'avais un peu de temps libre pour l'écrire moi-même.

![Image](https://cdn-media-1.freecodecamp.org/images/i7RmM4xORdvi4kS1KEjvqxeq5lZT9OI9KAjo)

### Le concept

`timeboard` est une bibliothèque Python qui crée des plannings de périodes de travail et effectue des calculs de calendrier sur ceux-ci. Ces objets eux-mêmes sont appelés timeboards.

Il y a trois étapes majeures dans le raisonnement sur un timeboard.

Vous commencez avec un intervalle de temps qui définit les limites de votre calendrier. Tout sera confiné à cet intervalle. Il est appelé le cadre (de référence). Le cadre se compose d'unités de base. Une unité de base est la plus petite période de temps dont vous avez besoin pour jauger votre calendrier. Par exemple, si vous raisonnez en termes de jours ouvrables, alors l'unité de base est un jour. Alternativement, si vous construisez un planning de services de plusieurs heures, alors l'unité de base est une heure.

![Image](https://cdn-media-1.freecodecamp.org/images/sI-5OZ10OfBSQP2EOH3I738uzuJA1bXjHufU)

À l'étape suivante, vous définissez les règles de marquage du cadre en périodes de travail. Les périodes de travail sont des périodes de temps qui vous intéressent. Elles constituent votre calendrier. Ce sont les périodes de travail que vous voulez planifier ou compter. Dans un calendrier standard de jours ouvrables, une période de travail est un jour (et l'unité de base est aussi un jour, donc elles coïncident).

Dans un centre d'appels, une période de travail est une période de plusieurs heures pendant laquelle une équipe particulière d'opérateurs est en service. L'unité de base est probablement une heure, et chaque période de travail comprend un nombre (probablement variable) d'unités de base.

La séquence de périodes de travail remplissant le cadre est appelée la timeline.

Enfin, vous créez un ou plusieurs plannings. Un planning est comme un pochoir posé sur la timeline. Son but est de distinguer les périodes de travail en service des périodes de travail hors service.

Un planning a besoin de quelque chose pour travailler afin de déclarer une période de travail en service ou hors service. C'est pourquoi vous fournissez une étiquette pour chaque période de travail, ou plutôt une règle pour les étiqueter pendant que le cadre est marqué en timeline. Chaque planning définit une fonction de sélection qui inspecte l'étiquette de la période de travail et retourne True pour les périodes de travail en service et False sinon. À moins que vous ne la remplaciez, une timeline est accompagnée du planning par défaut dont le sélecteur retourne la valeur booléenne de l'étiquette.

Parfois, vous voulez définir plusieurs plannings pour la même timeline. Par exemple, dans un centre d'appels, il y aura le planning pour le centre d'appels dans son ensemble, et un planning séparé pour chaque équipe d'opérateurs. La même période de travail peut être trouvée en service sous certains plannings et hors service sous d'autres.

![Image](https://cdn-media-1.freecodecamp.org/images/MlUNZdQm8rr9PwqqoqCm5YLfoeXz99sR6i-q)

Timeboard = timeline + plannings. Plus précisément, _timeboard_ est une collection de plannings de travail basés sur une timeline spécifique de périodes de travail construite sur un cadre de référence.

Une fois que vous avez un timeboard, vous pouvez effectuer le travail utile : faire des calculs de calendrier afin de résoudre les problèmes comme ceux décrits dans le prologue.

Chaque calcul effectué avec timeboard est conscient du service. La méthode invoquée « voit » uniquement les périodes de travail avec le service spécifié et ignore les autres. Afin de révéler le service des périodes de travail, la méthode doit recevoir un planning. Par conséquent, chaque calcul sur le timeboard est paramétré avec un service et un planning.

Par défaut, le service est « on » et le planning est le planning par défaut du timeboard. Par exemple, si vous appelez `count()` sans arguments sur un intervalle d'un timeboard, vous obtiendrez le nombre de périodes de travail dans l'intervalle qui sont déclarées en service sous le planning par défaut. Ces valeurs par défaut facilitent la vie car en pratique vous voudrez traiter principalement avec les périodes de travail en service.

### L'API

La documentation complète de timeboard est disponible sur [Read the Docs](https://timeboard.readthedocs.io/).

Le package peut être installé avec la commande habituelle `pip install timeboard`.

#### Configurer un timeboard

La manière la plus simple de commencer est d'utiliser un calendrier préconfiguré qui est fourni avec le package. Prenons un calendrier de jours ouvrables régulier pour les États-Unis.

```
 >>> import timeboard.calendars.US as US >>> clnd = US.Weekly8x5()
```

L'objet `clnd` est un timeboard (une instance de la classe `timeboard.Timeboard`). Il n'a qu'un seul planning par défaut qui sélectionne les jours de la semaine comme périodes de travail en service tandis que les week-ends, ainsi que les observations des jours fériés fédéraux des États-Unis, sont déclarés hors service.

Les outils pour construire votre propre timeboard seront brièvement passés en revue plus tard après avoir vu ce que vous pouvez faire avec un timeboard.

#### Jouer avec les périodes de travail

Appeler une instance de timeboard `clnd()` avec un seul point dans le temps récupère la période de travail qui contient ce point. Maintenant que vous avez une période de travail, vous pouvez interroger son service :

**Une certaine date est-elle un jour ouvrable ?**

```
>>> ws = clnd('27 May 2017')>>> ws.is_on_duty()False
```

En effet, c'était un samedi.

Vous pouvez également regarder dans le futur ou dans le passé à partir de la période de travail actuelle :

**Quand était le prochain jour ouvrable ?**

```
>>> ws.rollforward()Workshift(6359) of 'D' at 2017–05–30
```

La période de travail retournée a le numéro de séquence 6359 et représente le jour du 30 mai 2017, qui, soit dit en passant, était le mardi après le jour férié du Memorial Day.

**Si nous devions terminer le projet en 22 jours ouvrables à partir du 01 mai 2017, quand serait notre date limite ?**

```
>>> clnd('01 May 2017') + 22Workshift(6361) of 'D' at 2017–06–01
```

C'est la même chose que :

```
>>> clnd('01 May 2017').rollforward(22)Workshift(6361) of 'D' at 2017–06–01
```

#### Jouer avec les intervalles

Appeler `clnd()` avec un ensemble différent de paramètres produit un objet représentant un intervalle sur le calendrier. L'intervalle ci-dessous contient toutes les périodes de travail du mois de mai 2017 :

```
>>> may2017 = clnd('May 2017', period='M')
```

**Combien de jours ouvrables y avait-il en mai ?**

```
>>> may2017.count()22
```

**Combien de jours de congé ?**

```
>>> may2017.count(duty='off')9
```

**Combien d'heures de travail ?**

```
>>> may2017.worktime()176
```

Un employé était dans l'entreprise du 3 avril 2017 au 15 mai 2017. **Quelle portion du salaire d'avril la société leur devait-elle ?**

Notez qu'appeler `clnd()` avec un tuple de deux points dans le temps produit un intervalle contenant toutes les périodes de travail entre ces points, inclusivement.

```
>>> time_in_company = clnd(('03 Apr 2017','15 May 2017'))>>> time_in_company.what_portion_of(clnd('Apr 2017', period='M'))1.0
```

En effet, le 1er et le 2 avril 2017 tombaient un week-end, donc, ayant commencé le 3, l'employé a travaillé tous les jours ouvrables du mois.

**Et quelle portion de celui de mai ?**

```
>>> time_in_company.what_portion_of(may2017)0.5
```

**Combien de jours l'employé avait-il travaillés en mai ?**

L'opérateur de multiplication retourne l'intersection de deux intervalles.

```
>>> (time_in_company * may2017).count()11
```

**Combien d'heures ?**

```
>>> (time_in_company * may2017).worktime()88
```

Un employé était dans l'entreprise du 01 janvier 2016 au 15 juillet 2017. **Combien d'années cette personne avait-elle travaillées pour l'entreprise ?**

```
>>> clnd(('01 Jan 2016', '15 Jul 2017')).count_periods('A')1.5421686746987953
```

![Image](https://cdn-media-1.freecodecamp.org/images/jsj2ogpaBTEwK2iz4RVJmVLuwBi4jyp1cPvW)

#### Construisez votre propre timeboard

À des fins d'introduction, je vais simplement plonger dans deux exemples. Si cela semble trop abrupt, veuillez trouver une discussion approfondie des outils de construction dans la [documentation du projet](https://timeboard.readthedocs.io/en/latest/making_a_timeboard.html).

L'instruction d'importation pour cette section :

```
>>> import timeboard as tb
```

Permettez-moi de revenir à un planning de périodes de travail dans la concession automobile que j'ai mentionné dans le prologue. Un mécanicien travaille le lundi, mardi, samedi et dimanche cette semaine, et le mercredi, jeudi et vendredi la semaine suivante ; puis le cycle bihebdomadaire se répète. Le timeboard est créé par le code suivant :

```
>>> biweekly = tb.Organizer(marker='W',...     structure=[[1,1,0,0,0,1,1], [0,0,1,1,1,0,0]])>>> clnd = tb.Timeboard(base_unit_freq='D', ...     start='01 Oct 2017', end='31 Dec 2018', ...     layout=biweekly)
```

Il est logique de regarder la dernière instruction en premier. Elle crée un timeboard nommé `clnd`. Les trois premiers paramètres définissent le cadre comme une séquence de jours ('D') du 01 octobre 2017 au 31 décembre 2018. Le paramètre `layout` indique comment organiser le cadre en timeline de périodes de travail. Ce travail est confié à un `Organizer` nommé `biweekly`.

La première instruction crée cet `Organizer` qui prend deux paramètres : `marker` et `structure`. Nous utilisons un `marker` pour placer des marques sur le cadre. Les marques sont une sorte de jalons qui divisent le cadre en sous-cadres, ou « spans ». Dans l'exemple `marker='W'` place une marque au début de chaque semaine de calendrier. Par conséquent, chaque span représente une semaine.

Le paramètre `structure` indique comment créer des périodes de travail dans chaque span. Le premier élément de `structure`, la liste `[1,1,0,0,0,1,1]`, est appliqué au premier span (c'est-à-dire à la première semaine de notre calendrier). Chaque unité de base (c'est-à-dire chaque jour) dans le span devient une période de travail. Les périodes de travail reçoivent des étiquettes de la liste, dans l'ordre.

Le deuxième élément de `structure`, la liste `[0,0,1,1,1,0,0]`, est appliqué de manière analogue au deuxième span (la deuxième semaine). Après cela, puisque nous n'avons plus obtenu d'éléments, une `structure` est rejouée en cycles. Par conséquent, la troisième semaine est servie par le premier élément de `structure`, la quatrième semaine par le deuxième, et ainsi de suite.

En résultat, notre timeline devient la séquence de jours étiquetés avec le nombre `1` lorsque le mécanicien est en service et avec le nombre `0` lorsqu'il ou elle ne l'est pas. Nous n'avons pas spécifié de planning, car le planning qui est construit par défaut nous convient parfaitement. Le planning par défaut considère la valeur booléenne de l'étiquette, donc `1` se traduit par 'en service', et zéro par 'hors service'.

Avec ce timeboard, nous pouvons faire tout type de calculs que nous avons faits précédemment avec le calendrier des jours ouvrables. Par exemple, si une personne était employée selon ce planning à partir du 4 novembre 2017, et que le salaire est payé mensuellement, quelle portion du salaire de novembre l'employé a-t-il gagné ?

```
>>> time_in_company = clnd(('4 Nov 2017', None))>>> nov2017 = clnd('Nov 2017', period='M')>>> time_in_company.what_portion_of(nov2017)0.8125
```

Dans le deuxième exemple, nous allons construire un timeboard pour un centre d'appels. Le centre d'appels fonctionne 24 heures sur 24 en équipes de durée variable : 08:00 à 18:00 (10 heures), 18:00 à 02:00 (8 heures), et 02:00 à 08:00 (6 heures). Le planning d'un opérateur se compose d'une équipe en service suivie de trois équipes hors service. Par conséquent, quatre équipes d'opérateurs sont nécessaires. Elles sont désignées par 'A', 'B', 'C' et 'D'.

```
>>> day_parts = tb.Marker(each='D', ...     at=[{'hours':2}, {'hours':8}, {'hours':18}])>>> shifts = tb.Organizer(marker=day_parts, ...     structure=['A', 'B', 'C', 'D'])>>> clnd = tb.Timeboard(base_unit_freq='H', ...     start='01 Jan 2009 02:00', end='01 Jan 2019 01:59',...     layout=shifts)>>> clnd.add_schedule(name='team_A', ...    selector=lambda label: label=='A')
```

Il y a quatre différences clés par rapport au cas de la concession automobile. Nous allons les examiner une par une.

Premièrement, l'unité de base du cadre est maintenant une période d'une heure (`base_unit_freq='H'`) au lieu d'une période d'une journée du calendrier de la concession automobile.

Deuxièmement, la valeur du paramètre `marker` de l'Organizer est maintenant un objet complexe au lieu d'une seule fréquence de calendrier comme c'était le cas auparavant. Cet objet est une instance de la classe `Marker`. Il est utilisé pour définir des règles de placement de marques sur le cadre lorsque la simple division du cadre en unités de calendrier uniformes n'est pas suffisante. La signature du Marker ci-dessus est presque lisible — elle dit : placez une marque chaque jour ('D') à 02:00 heures, 08:00 heures et 18:00 heures.

Troisièmement, la valeur de `structure` est maintenant plus simple : il s'agit d'une liste à un niveau des étiquettes des équipes. Lorsqu'un élément de `structure` n'est pas un itérable d'étiquettes mais simplement une étiquette, son application à un span produit une seule période de travail qui, littéralement, couvre le span.

Dans notre exemple, le tout premier span comprend six unités de base d'une heure commençant à 2, 3, 4 … 7 heures du matin du 01 janvier 2009. Toutes ces unités de base sont combinées en une seule période de travail avec l'étiquette 'A'. Le deuxième span comprend dix unités de base d'une heure commençant à 8, 9, 10 … 17 heures. Ces unités de base sont combinées en une seule période de travail avec l'étiquette 'B', et ainsi de suite. Lorsque toutes les étiquettes ont été prises, la structure est rejouée, donc le cinquième span (08:00:00–17:59:59 le 01 janvier 2009) devient une période de travail avec l'étiquette 'A'.

Pour résumer, si un élément de `structure` est une liste d'étiquettes, chaque unité de base du span devient une période de travail et reçoit une étiquette de la liste. Si un élément de `structure` est une seule étiquette, toutes les unités de base du span sont combinées pour former une seule période de travail qui reçoit cette étiquette.

Et enfin, nous avons explicitement créé un planning pour l'équipe A. Le planning par défaut ne sert pas notre objectif car il retourne « toujours en service ». Cela est vrai pour le centre d'appels dans son ensemble mais pas pour une équipe particulière. Pour le nouveau planning, nous fournissons le nom et la fonction de sélection qui retourne True pour toutes les périodes de travail étiquetées avec 'A'. Pour une utilisation pratique, vous voudrez créer les plannings pour les autres équipes également.

Ce timeboard est aussi bon à utiliser que n'importe quel autre. Cependant, cette fois, nous devrons spécifier explicitement le planning que nous voulons utiliser.

```
>>> schedule_A = clnd.schedules['team_A']
```

**Combien de services les opérateurs de l'équipe A ont-ils effectués en novembre 2017 ?**

```
>>> nov2017 = clnd('Nov 2017', period='M', schedule=schedule_A)>>> nov2017.count()22
```

**Et combien d'heures y avait-il au total ?**

```
>>> nov2017.worktime()176
```

Une personne était employée comme opérateur dans l'équipe A à partir du 4 novembre 2017. Le salaire est payé mensuellement. **Quelle portion du salaire de novembre l'employé a-t-il gagné ?**

```
>>> time_in_company = clnd(('4 Nov 2017',None), schedule=schedule_A)>>> time_in_company.what_portion_of(nov2017)0.9090909090909091
```

#### Plus de cas d'utilisation

Vous pouvez trouver plus de cas d'utilisation (presque tirés de la vie réelle) dans le [notebook jupyter](https://timeboard.readthedocs.io/en/latest/_downloads/use_cases.ipynb) qui fait partie de la [documentation du projet](https://timeboard.readthedocs.io/en/latest/use_cases.html).

N'hésitez pas à utiliser `timeboard` et n'hésitez pas à laisser des commentaires ou à ouvrir des problèmes sur [GitHub](https://github.com/mmamaev/timeboard/issues).