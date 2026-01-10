---
title: Comment fonctionnent les licences open source et comment les ajouter à vos
  projets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-17T07:40:05.000Z'
originalURL: https://freecodecamp.org/news/how-open-source-licenses-work-and-how-to-add-them-to-your-projects-34310c3cf94
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FFYtzf28XKPFBdknfXf-jg.jpeg
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment fonctionnent les licences open source et comment les ajouter à
  vos projets
seo_desc: 'By Radu Raicea

  Recently, there was some exciting news for developers around the world. Facebook
  changed the license of multiple libraries they develop. They switched from BSD-3+patents
  to a MIT.

  That seems good, but what does it mean? What are the im...'
---

Par Radu Raicea

Récemment, il y a eu des nouvelles passionnantes pour les développeurs du monde entier. Facebook a changé la licence de plusieurs bibliothèques qu'ils développent. Ils sont passés de **BSD-3+patents** à **MIT**.

Cela semble une bonne chose, mais qu'est-ce que cela signifie ? Quelles sont les implications des différentes licences open source ?

Cet article vous donnera une compréhension rapide des licences populaires. Il vous apprendra également comment les appliquer à vos projets open source sur GitHub.

### L'Autorité

Les licences open source les plus populaires ont un aspect important en commun. L'[Open Source Initiative](https://opensource.org/) (OSI) les a approuvées.

L'OSI a été formée en 1998 dans le but de promouvoir les logiciels open source. Elle a créé l'[Open Source Definition](https://opensource.org/osd) (OSD) pour définir ce qu'est un logiciel open source.

Voici comment ils se décrivent :

> L'Open Source Initiative (OSI) est une organisation à but non lucratif d'envergure mondiale formée pour éduquer et plaider en faveur des avantages de l'open source et pour établir des ponts entre les différentes parties prenantes de la communauté open source.

### Les Licences

La plupart des licences open source incluent les déclarations suivantes :

1. Le logiciel peut être modifié, utilisé commercialement et distribué.
2. Le logiciel peut être modifié et utilisé en privé.
3. Une licence et un avis de droit d'auteur doivent être inclus dans le logiciel.
4. Les auteurs du logiciel ne fournissent aucune garantie avec le logiciel et ne sont responsables de rien.

Nous allons passer en revue les licences les plus populaires, de la plus restrictive à la plus permissive (du point de vue de l'utilisateur).

#### GNU General Public License, version 3 (GPLv3)

La [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) est l'une des licences les plus restrictives. Elle offre une protection élevée à l'auteur du logiciel.

* Le code source doit être rendu **public** chaque fois qu'une distribution du logiciel est effectuée.
* Les modifications du logiciel doivent être publiées sous la **même licence**.
* Les modifications apportées au code source **doivent être documentées**.
* Si du matériel breveté a été utilisé dans la création du logiciel, elle accorde aux utilisateurs le droit de l'utiliser. Si l'utilisateur poursuit quiconque pour l'utilisation du matériel breveté, il perd le droit d'utiliser le logiciel.

[**GPLv2**](https://www.gnu.org/licenses/gpl-2.0.html) est également très populaire. La principale différence par rapport à la GPLv3 est la clause sur l'octroi de brevets.

Cette clause a été ajoutée dans la version 3 pour empêcher les entreprises de [faire payer les utilisateurs pour l'utilisation de leurs brevets](http://www.nytimes.com/2006/11/22/technology/22soft.html).

Les projets populaires utilisant la GPLv3 sont [**Bash**](https://www.gnu.org/software/bash/) et [**GIMP**](https://www.gimp.org). [**Linux**](https://github.com/torvalds/linux) utilise la GPLv2.

[Ezequiel Foncubierta](https://www.freecodecamp.org/news/how-open-source-licenses-work-and-how-to-add-them-to-your-projects-34310c3cf94/undefined) a souligné un point important pour les licences GPL :

> La licence de votre code source doit être compatible avec la licence du code open source auquel vous vous liez. Par exemple, si votre code est propriétaire, vous ne serez pas autorisé à utiliser une bibliothèque sous licence GPL. C'est là que les gens ont tendance à faire le plus d'erreurs.

#### Apache License 2.0

L'[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) offre plus de flexibilité aux utilisateurs.

* Le code source **n'a pas besoin d'être public** lorsqu'une distribution du logiciel est effectuée.
* Les modifications du logiciel peuvent être publiées sous **n'importe quelle licence**.
* Les modifications apportées au code source **doivent** être documentées.
* Elle offre la même protection d'utilisation des brevets que la GPLv3.
* Elle interdit explicitement l'utilisation des noms de marques déposées trouvés dans le projet.

Les projets populaires utilisant l'Apache License 2.0 sont [**Android**](https://github.com/aosp-mirror/platform_system_core/blob/master/NOTICE), [**Apache**](https://httpd.apache.org), et [**Swift**](https://github.com/apple/swift).

#### Berkeley Software Distribution (BSD)

La BSD a deux versions principales : [2-clause](https://opensource.org/licenses/BSD-2-Clause) et [3-clause](https://opensource.org/licenses/BSD-3-Clause). Elles offrent toutes deux plus de flexibilité aux utilisateurs que l'Apache License 2.0.

* Le code source **n'a pas besoin d'être public** lorsqu'une distribution du logiciel est effectuée.
* Les modifications du logiciel peuvent être publiées sous **n'importe quelle licence**.
* Les modifications apportées au code source **peuvent** **ne pas** être documentées.
* Elle n'offre aucune position explicite sur l'utilisation des brevets.
* La licence et l'avis de droit d'auteur doivent être inclus dans la documentation de la **version compilée** du code source (par opposition à seulement dans le code source).
* La BSD 3-clause stipule que les noms de l'auteur et des contributeurs ne peuvent pas être utilisés pour promouvoir des produits dérivés du logiciel sans autorisation.

Les projets populaires utilisant la licence BSD sont [**Go**](https://github.com/golang/go) (3-clause), [**Pure.css**](https://github.com/yahoo/pure) (3-clause), et [**Sentry**](https://github.com/getsentry/sentry) (3-clause).

#### Licence MIT

La [MIT](https://mit-license.org) est l'une des licences les plus permissives. C'est aussi la plus populaire. Elle offre une protection très faible à l'auteur du logiciel.

* Le code source **n'a pas besoin d'être public** lorsqu'une distribution du logiciel est effectuée.
* Les modifications du logiciel peuvent être publiées sous **n'importe quelle licence**.
* Les modifications apportées au code source **peuvent** **ne pas** être documentées.
* Elle n'offre aucune position explicite sur l'utilisation des brevets.

Les projets populaires utilisant la MIT sont [**Angular.js**](https://github.com/angular/angular.js), [**jQuery**](https://github.com/jquery/jquery), [**Rails**](https://github.com/rails/rails), [**Bootstrap**](https://github.com/twbs/bootstrap), et bien d'autres.

[**React.js**](https://github.com/facebook/react) de Facebook avait une licence BSD-3+patents jusqu'au 25 septembre. Elle combinait la licence BSD-3 avec une clause supplémentaire sur l'utilisation des brevets.

En résumé, si vous poursuivez Facebook ou l'une de ses filiales, vous perdez le droit d'utiliser React (ou tout autre logiciel sous la même licence).

React est désormais sous licence MIT. Vous pouvez maintenant poursuivre Facebook et continuer à utiliser React. Quel soulagement !

### Appliquer une licence à vos projets open source

Appliquer une licence à vos projets est facile. Vous devez ajouter un fichier `LICENSE`, `LICENSE.txt` ou `LICENSE.md` dans le répertoire racine de votre dépôt.

GitHub rend cela encore plus facile :

1. Ouvrez votre dépôt GitHub dans un navigateur.
2. Dans le répertoire racine, cliquez sur `**Create new file**`.
3. Nommez le fichier « LICENSE ».
4. Cliquez sur `**Choose a license template**`.
5. Choisissez l'une des licences (toutes celles mentionnées dans cet article s'y trouvent).
6. Une fois choisie, cliquez sur `**Review and submit**`.
7. `**Commit**` le fichier.

### En résumé…

* L'une des licences les plus restrictives est la **GPL**.
* L'une des licences les plus permissives est la **MIT**.
* Les autres licences populaires sont l'**Apache License 2.0** et la **BSD**.
* Pour appliquer une licence sur votre projet GitHub, vous devez créer un fichier `LICENSE` en utilisant les modèles de licence de GitHub.

**Consultez mon [explication](https://medium.freecodecamp.org/how-i-used-python-to-find-interesting-people-on-medium-be9261b924b0) sur la façon dont j'ai utilisé Python pour trouver des personnes intéressantes à suivre sur Medium !**

Pour plus de mises à jour, suivez-moi sur [Twitter](https://twitter.com/radu_raicea).