---
title: Comment estimer plus précisément le temps de lecture des articles Medium en
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-more-accurately-estimate-read-time-for-medium-articles-in-javascript-fb563ff0282a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*d-tl9IZ4vRR2hvZw
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment estimer plus précisément le temps de lecture des articles Medium
  en JavaScript
seo_desc: 'By Pritish Vaidya

  Introduction

  Read Time Estimate is the estimation of the time taken by the reader to read an
  article. It has been a part of Medium’s core features since it launched in 2013.

  As explained in the New Yorker:


  The more we know about so...'
---

Par Pritish Vaidya

### Introduction

L'estimation du temps de lecture est l'estimation du temps nécessaire au lecteur pour lire un article. Cela fait partie des fonctionnalités principales de _Medium_ depuis son lancement en 2013.

Comme expliqué dans le [_New Yorker_](https://www.newyorker.com/tech/annals-of-technology/a-list-of-reasons-why-our-brains-love-lists) :

> Plus nous savons quelque chose — y compris précisément combien de temps cela prendra — plus nous avons de chances de nous engager.

Savoir à l'avance combien de temps il faudra pour lire un article aide à mieux gérer son temps en permettant de planifier plus loin.

### Pourquoi devrais-je utiliser un nouveau script ?

Oui, il existe de nombreuses bibliothèques open source disponibles sur [_npm_](https://npmjs.com), mais elles contiennent plusieurs défauts.

Avant cela, examinons ces deux articles sur Medium.

* [Temps de lecture — Support Medium](https://help.medium.com/hc/en-us/articles/214991667-Read-time)
* [Temps de lecture et vous](https://blog.medium.com/read-time-and-you-bc2048ab620c)

Les deux articles ci-dessus présentent les caractéristiques clés suivantes :

* Temps de lecture moyen (anglais) — 265 mots par minute
* Temps de lecture moyen (chinois, japonais et coréen) — 500 caractères/minute
* Temps de lecture des images — 12 secondes pour la première image, 11 pour la deuxième, et moins une seconde supplémentaire pour chaque image suivante. Les autres images sont comptées à 3 secondes.

La plupart des bibliothèques ne tiennent pas compte de toutes ces caractéristiques. Elles utilisent les chaînes HTML telles quelles sans omettre les _noms de balises_, ce qui augmente l'écart entre l'estimation et la valeur originale.

### Code

Le code peut être divisé en trois parties :

* Constantes
* Utilitaires
* Principal

#### Constantes

Les constantes peuvent être utilisées comme valeurs par défaut pour la fonction principale. La balise image a son propre usage, qui sera défini plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/I1qiIH1GSNr2GwXtOXCduq0ZBhLEBBv9oc-y)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/constants/index.js" rel="noopener" target="_blank" title=")_

#### Fonctions utilitaires

1. **Supprimer les espaces blancs**

Il s'agit d'une fonction utilitaire simple pour supprimer tous les espaces blancs en début et en fin de la chaîne fournie.

![Image](https://cdn-media-1.freecodecamp.org/images/GXs-gWsnAaFVaEhYkffcs6Do6XHAYwH4GIIG)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/strip-whitespace.js" rel="noopener" target="_blank" title=")_

**2. Temps de lecture des images**

Elle analyse la chaîne, recherche les balises HTML d'images en fonction des valeurs par défaut fournies dans les constantes et retourne le compte.

Si le nombre d'images est supérieur à 10, nous calculons le temps de lecture des 10 premières images en progression arithmétique décroissante à partir de 12 sec / `customReadTime` fourni par l'utilisateur en utilisant la formule simple `n * (a+b) / 2` et 3 sec pour les images restantes.

![Image](https://cdn-media-1.freecodecamp.org/images/QZLkHjy8hKGklv1dfJUw8QIq-nyxCMUBqWVm)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/image-read-time.js" rel="noopener" target="_blank" title=")_

**3. Supprimer les balises**

Ensuite, nous vérifions la présence de balises HTML (les deux) dans la chaîne et les supprimons pour n'en extraire que les mots.

![Image](https://cdn-media-1.freecodecamp.org/images/7C84Iy4AhG4sE7pkRqBzljPgwll6fpXK6agy)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/strip-tags.js" rel="noopener" target="_blank" title=")_

**4. Temps de lecture des mots**

Cette fonction utilitaire calcule le nombre de mots et les caractères _chinois / coréens et japonais_ en utilisant différentes plages de caractères _Unicode_.

Le temps est calculé en le divisant par les constantes définies ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/dlVpGaguE9EaHXH268Kj6ZXNy8CenaOkSElz)
_Crédit image : [GitHub](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/words-read-time.js" rel="noopener" target="_blank" title=")_

**5. Humaniser le temps**

Basé sur la [distance de temps en mots](https://api.rubyonrails.org/classes/ActionView/Helpers/DateHelper.html#method-i-distance_of_time_in_words), nous pouvons calculer et retourner la durée humanisée du temps nécessaire pour lire.

![Image](https://cdn-media-1.freecodecamp.org/images/y5NtDMmPJiq26c2Ry6LMdraRyaY3gmsrY0EI)
_Crédit image : [Github](https://github.com/dawnlabs/carbon" rel="noopener" target="_blank" title="">Carbon</a>. | Code : <a href="https://github.com/pritishvaidya/read-time-estimate/blob/master/src/utils/humanize-time.js" rel="noopener" target="_blank" title=")_

#### Principal

La fonction principale consolide simplement toutes les méthodes utilitaires dans le bon ordre.

![Image](https://cdn-media-1.freecodecamp.org/images/Ja78VfX78b32iztnVrpNGz8cvTcOg9ZcpeSm)

### À quel point ce script est-il précis ?

En prenant les tests sur la chaîne HTML (à partir de l'inspecteur Chrome) **avant cette section de l'article.**

![Image](https://cdn-media-1.freecodecamp.org/images/jadNXZgeEEgfSft4bwnZRnTnDbEJvijjssga)

![Image](https://cdn-media-1.freecodecamp.org/images/wQ8Rqazgd3WSlbZaa0RS-rbd2LGceCxQBJ2C)

Les tests et les [Pages](https://www.apple.com/in/pages/) donnent clairement la bonne estimation du nombre total de mots à partir du HTML analysé et du nombre d'images.

### Liens

J'ai consolidé le code complet sur [GitHub](https://github.com/pritishvaidya/read-time-estimate). Il est également disponible en tant que package npm [read-time-estimate](https://www.npmjs.com/package/read-time-estimate).

D'autres choses intéressantes peuvent être trouvées sur mes profils [**_StackOverflow_**](https://stackoverflow.com/users/6606831/pritish-vaidya) et [**_GitHub_**](https://github.com/pritishvaidya).

Suivez-moi sur [**_LinkedIn_**](https://www.linkedin.com/in/pritish-vaidya-506686128/), [**_Medium_**](https://medium.com/@pritishvaidya94), [**_Twitter_**](https://twitter.com/PritishVaidya) pour des mises à jour sur de nouveaux articles.

**Un applaudissement, deux applaudissements, trois applaudissements, quarante ?**

![Image](https://cdn-media-1.freecodecamp.org/images/i8DEAdbrJcjBay1E0rScJ481SHR9GqeWe5hG)

_Publié à l'origine sur [blog.pritishvaidya.com](https://blog.pritishvaidya.com/posts/2019-01-30-a-simple-and-more-accurate-estimation-of-read-time-for-medium-articles-in-javascript/) le 30 janvier 2019._