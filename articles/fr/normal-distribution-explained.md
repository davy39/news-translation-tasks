---
title: Règle 68-95-99 – Distribution normale expliquée en français
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-07T16:46:51.000Z'
originalURL: https://freecodecamp.org/news/normal-distribution-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c995b740569d1a4ca1f43.jpg
tags:
- name: Math
  slug: math
seo_title: Règle 68-95-99 – Distribution normale expliquée en français
seo_desc: "By Neil Kakkar\nMeet Mason. He's an average American 40-year-old: 5 foot\
  \ 10 inches tall and earning $47,000 per year before tax.\nHow often would you expect\
  \ to meet someone who earns 10x as much as Mason? \nAnd now, how often would you\
  \ expect to meet so..."
---

Par Neil Kakkar

Rencontrez Mason. C'est un Américain moyen de 40 ans : il mesure 1,78 mètre et gagne 47 000 dollars par an avant impôts.

À quelle fréquence vous attendez-vous à rencontrer quelqu'un qui gagne 10 fois plus que Mason ?

Et maintenant, à quelle fréquence vous attendez-vous à rencontrer quelqu'un qui est 10 fois plus grand que Mason ?

Vos réponses aux deux questions ci-dessus sont différentes, car la distribution des données est différente. Dans certains cas, 10 fois au-dessus de la moyenne est courant. Alors que dans d'autres, ce n'est pas courant du tout.

## Qu'est-ce que les distributions normales ?

Aujourd'hui, nous nous intéressons aux distributions normales. Elles sont représentées par une courbe en cloche : elles ont un pic au milieu qui s'amincit vers chaque bord. Beaucoup de choses suivent cette distribution, comme votre taille, votre poids et votre QI.

Cette distribution est passionnante car elle est symétrique – ce qui la rend facile à utiliser. Vous pouvez réduire beaucoup de mathématiques compliquées à quelques règles de base, car vous n'avez pas à vous soucier des cas particuliers bizarres.

Par exemple, le pic divise toujours la distribution en deux. Il y a une masse égale avant et après le pic.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/normal_dist_symmetric.jpg)

Une autre propriété importante est que nous n'avons pas besoin de beaucoup d'informations pour décrire une distribution normale.

En effet, nous n'avons besoin que de deux choses :

1. La moyenne. La plupart des gens l'appellent simplement "la moyenne". C'est ce que vous obtenez si vous additionnez la valeur de toutes vos observations, puis divisez ce nombre par le nombre d'observations. Par exemple, la moyenne de ces trois nombres : `1, 2, 3 = (1 + 2 + 3) / 3 = 2`
2. Et l'écart-type. Cela vous indique à quel point une observation serait rare. La plupart des observations se situent dans un écart-type de la moyenne. Moins d'observations sont à deux écarts-types de la moyenne. Et encore moins sont à trois écarts-types (ou plus).

Ensemble, la moyenne et l'écart-type constituent tout ce que vous devez savoir sur une distribution.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/multiple_normal_dist.jpg)

### La règle 68-95-99

La règle 68-95-99 est basée sur la moyenne et l'écart-type. Elle dit :

> 68 % de la population se situe dans 1 écart-type de la moyenne.
>
> 95 % de la population se situe dans 2 écarts-types de la moyenne.
>
> 99,7 % de la population se situe dans 3 écarts-types de la moyenne.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/normal_dist_68_rule.jpg)

## Comment calculer les distributions normales

Pour continuer notre exemple, la taille moyenne des hommes américains est de 1,78 mètre, avec un écart-type de 10 centimètres. Cela signifie :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/normal_dist_68_rule_heights.jpg)

Maintenant, la partie amusante : appliquons ce que nous venons d'apprendre.

Quelle est la probabilité de voir quelqu'un avec une taille entre 1,78 mètre et 1,88 mètre ? (C'est-à-dire entre 178 et 188 centimètres.)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/normal_dist_68_rule_heights_example1.jpg)

C'est 34 % ! Nous utilisons les deux propriétés : la distribution est symétrique, ce qui signifie que les probabilités pour (166-178) centimètres et (178-188) centimètres sont toutes deux de 68/2 = 34 %.

Essayons un exemple plus difficile. Quelle est la probabilité de voir quelqu'un avec une taille entre 162 et 166 centimètres ?

![Image](https://www.freecodecamp.org/news/content/images/2020/08/normal_dist_68_rule_heights_example2.jpg)

C'est (95-68)/2 = 13,5 %. Les deux bords extérieurs ont le même pourcentage.

Et maintenant votre dernier (et plus difficile) test : Quelle est la probabilité de voir quelqu'un avec une taille supérieure à 208 centimètres ?

![Image](https://www.freecodecamp.org/news/content/images/2020/08/normal_dist_68_rule_heights_example3.jpg)

Ici, nous utilisons également la dernière propriété : tout doit faire 100 %. Donc les bords extérieurs (c'est-à-dire les tailles inférieures à 158 et les tailles supérieures à 208) font ensemble (100 % - 99,7 %) = 0,3 %.

N'oubliez pas, vous pouvez appliquer cela à n'importe quelle distribution normale. Essayez de faire de même pour les tailles féminines : la moyenne est de 165 centimètres, et l'écart-type est de 8,9 centimètres.

Donc, la probabilité de voir quelqu'un avec une taille entre 165 et 173,9 centimètres serait : ___.

...

...

34 % ! C'est exactement la même chose que notre premier exemple. C'est +1 écart-type.

## Conclusion

Connaître cette règle rend très facile l'étalonnage de vos sens. Puisque tout ce dont nous avons besoin pour décrire une distribution normale est la moyenne et l'écart-type, cette règle s'applique à _toutes_ les distributions normales du monde !

La partie difficile, en effet, est de déterminer si la distribution est normale ou non.

Vous voulez en savoir plus sur l'étalonnage de vos sens et la pensée critique ? Consultez [Bayes Theorem: A Framework for Critical Thinking](https://neilkakkar.com/Bayes-Theorem-Framework-for-Critical-Thinking.html).