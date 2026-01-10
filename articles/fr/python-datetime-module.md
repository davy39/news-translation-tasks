---
title: Module datetime de Python – Comment gérer les dates en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-01T15:59:54.000Z'
originalURL: https://freecodecamp.org/news/python-datetime-module
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6022ad400a2838549dcc1f89.jpg
tags:
- name: modules
  slug: modules
- name: Python
  slug: python
seo_title: Module datetime de Python – Comment gérer les dates en Python
seo_desc: "By Suchandra Datta\nIn this quick guide to Python's datetime module, you'll\
  \ learn how to parse dates, extract meaningful information from dates, handle timedelta\
  \ objects and much more. \nSo without further ado let's start counting time with\
  \ Python!\nMos..."
---

Par Suchandra Datta

Dans ce guide rapide sur le module `datetime` de Python, vous apprendrez à analyser les dates, extraire des informations significatives des dates, gérer les objets `timedelta` et bien plus encore. 

Alors sans plus attendre, commençons à compter le temps avec Python !

La plupart des langages de programmation fournissent des bibliothèques pour une gestion facile des dates. Python offre le puissant module `datetime` avec ses nombreuses fonctions et sa documentation claire qui facilite l'analyse des dates. 

Cet article liste certaines des fonctions les plus importantes de ce module, comment il peut être appliqué pour des situations réelles, et quelques points délicats à surveiller lors de son utilisation. 

## Comment convertir des timestamps en objets `datetime` en utilisant `strptime()`

Les dates peuvent nous donner beaucoup d'informations comme le mois, l'année, le jour, le jour de la semaine et si c'est un jour férié ou non. `strptime()` convertit un timestamp sous forme de chaîne en un objet `datetime` qui nous donne beaucoup de fonctionnalités supplémentaires. Cette fonction attend une chaîne et le format du timestamp. 

```
from datetime import datetime

d = datetime.strptime("21-02-2021 18:46:00", "%d-%m-%Y %H:%M:%S")
```

La chaîne 21-02-2021 18:46:00 est convertie en un `datetime` approprié en utilisant le format spécifié. Certains des directives les plus utiles sont :

* `%d` pour le jour du mois sous forme de décimal avec zéro initial comme 01, 02, 03 
* `%m` pour le mois sous forme de nombre décimal avec zéro initial
* `%Y` pour l'année avec le siècle sous forme de nombre décimal
* `%H` pour l'horloge de 24 heures avec une valeur d'heure avec zéro initial
* `%M` pour les minutes avec zéro initial, et 
* `%S` pour les secondes avec zéro initial.

Cette collection de spécificateurs de format est suffisante pour bien démarrer. Pour plus d'options, vous pouvez parcourir la documentation liée [ici](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior). 

### Comment obtenir la valeur du timestamp actuel

Supposons que vous souhaitiez stocker des données dans une base de données avec le timestamp actuel comme clé. Pour obtenir le timestamp actuel, vous n'avez besoin que d'une ligne de code :

```python
#Obtenir le timestamp actuel

from datetime import datetime
print(datetime.now())
```

### Comment savoir quel jour nous sommes 

Disons que nous devons connaître le jour de la semaine. Nous pouvons utiliser la fonction `weekday()` qui retourne un code numérique pour le jour de la semaine, de zéro à six, où zéro représente lundi, un représente mardi, et ainsi de suite. 

La sortie pourrait être utilisée avec une instruction switch pour convertir le code numérique en nom de jour requis ou vous pourriez utiliser une liste comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-169.png)

### Comment générer une liste de dates à partir d'une date donnée

Disons que nous savons combien de pizzas les gens ont commandées jusqu'à aujourd'hui et que nous sommes intéressés à prédire les ventes de pizzas pour la semaine prochaine. 

Ainsi, étant donné la date d'aujourd'hui, nous avons besoin de toutes les dates de la semaine prochaine pour notre analyse requise. Mais nous ne voulons pas nous soucier des années bissextiles, des années siècles, et ainsi de suite. Voici une façon de le faire.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-137.png)

### Comment travailler avec les objets `timedelta`

Comme le nom le suggère, les objets `timedelta` représentent une durée entre deux dates. Disons que nous avons deux dates et que nous devons savoir combien de temps s'est écoulé entre elles.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-138.png)

Les objets `timedelta` nécessitent plusieurs arguments comme les jours, les secondes, les microsecondes, les millisecondes, les minutes, les heures et les semaines. Les valeurs par défaut pour tous sont zéro. Trouvons la différence en heures entre 2 dates.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-139.png)

Qu'est-ce qui n'a pas fonctionné ? `timedelta` ne stocke rien en interne sauf les jours, les secondes et les microsecondes, donc nous devons les convertir comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-141.png)

### Comment obtenir une représentation en chaîne des dates à partir des objets `datetime` ou Date en utilisant `strftime`

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-170.png)

Si nous imprimons l'objet `datetime` lui-même, la date est imprimée au format ISO. En utilisant `strftime`, nous passons une chaîne de format pour contrôler la représentation en chaîne de la date.

## Conclusion

Si vous avez lu jusqu'ici, félicitations – vous avez appris à analyser les dates selon un format spécifié, obtenir la valeur du timestamp actuel, obtenir le jour de la semaine, obtenir une liste de dates, utiliser les objets timedelta, et obtenir la date sous forme de chaîne à partir des objets. Ouf !

Ceci est une collection compilée basée sur mes nombreuses recherches sur Internet et ma lecture sans fin de la documentation officielle. 

Merci d'avoir pris un peu de temps dans votre emploi du temps chargé pour lire ceci. J'espère que vous avez apprécié la lecture autant que j'ai aimé l'écrire. Amusez-vous bien à analyser les dates en Python !