---
title: Comment être plus productif sur GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T16:16:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-be-more-productive-on-github-c3cedab043e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-Mc_lCYQhg5p45VrhbdfJQ.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment être plus productif sur GitHub
seo_desc: 'By Darren Burns

  With the recent announcement by GitHub of unlimited private repositories, let’s
  take a few minutes before we push our code we don’t want anyone else to see to the
  cloud, and make sure we’re making the most of what GitHub has to offer....'
---

Par Darren Burns

Avec l'annonce récente de GitHub concernant les [dépôts privés illimités](https://blog.github.com/2019-01-07-new-year-new-github), prenons quelques minutes avant de pousser notre code que nous ne voulons pas que quiconque voie dans le cloud, et assurons-nous de tirer le meilleur parti de ce que GitHub a à offrir.

GitHub est construit avec des raccourcis extrêmement utiles et des fonctionnalités qui boostent la productivité. Cependant, d'après mon expérience personnelle, il est clair que ces fonctionnalités passent souvent inaperçues parmi les développeurs.

Si j'ai déjà vu une fonctionnalité spécifique de GitHub surprendre ou aider quelqu'un, c'est sur cette page. Cela dit, ce qui suit n'est en aucun cas une liste exhaustive.

#### Recherche rapide et floue de fichiers dans les dépôts

C'est, sans aucun doute, le moyen le plus rapide de parcourir un dépôt lorsque vous savez ce que vous cherchez. Ouvrez n'importe quel dépôt et appuyez sur `t`. Vous pouvez maintenant rechercher le nom de n'importe quel fichier dans le dépôt, et utiliser les touches fléchées de votre clavier pour parcourir les résultats. Appuyez sur `Entrée` pour ouvrir le fichier.

![Image](https://cdn-media-1.freecodecamp.org/images/sN3jhoDd0p1mUiroNYprj8EyqoBVqv3I5TpA)

#### Suggestions de modifications de code dans les pull requests

Lorsque vous commentez un morceau de code dans une pull request, vous pouvez suggérer un code alternatif en utilisant la fonctionnalité "Suggested Changes". L'auteur de la pull request pourra appliquer votre suggestion instantanément sans quitter GitHub. Pour faire la suggestion, encadrez un extrait de code avec un extrait Markdown multi-ligne et ajoutez le tag "suggestion" :

![Image](https://cdn-media-1.freecodecamp.org/images/tFxJgPwY4B6I1ph7J18jxpOXoeRlR0JPvVtQ)
_Suggérer une modification dans une pull request…_

Maintenant que vous avez fait la suggestion, l'auteur de la pull request peut l'appliquer immédiatement à sa branche, sans le tracas de modifier manuellement le fichier !

![Image](https://cdn-media-1.freecodecamp.org/images/Qr1oLWlkwLYRsRC8POcEgEj3SYQznU8kgqLN)
_…et ensuite appliquer cette modification !_

#### Naviguer dans l'arborescence du code comme dans un IDE

Cela nécessite une extension Chrome non officielle, mais c'est un moyen légèrement plus familier de naviguer dans votre code, par rapport à l'interface par défaut. L'[extension Octotree](https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc) vous permet de parcourir les dépôts GitHub avec une vue en arborescence de la barre latérale similaire à ce que vous obtenez dans des applications comme VS Code.

![Image](https://cdn-media-1.freecodecamp.org/images/EvBpPVgtggPwadfc4ptsKe6mxm0Lla8V96yS)

#### Sauter à une fonction lors de la révision de code

Sauf si vous révisez une seule fonction, une révision de code implique souvent beaucoup de sauts entre les appels de fonction et leurs définitions (et donc beaucoup de défilement vers le haut et vers le bas). GitHub vous permet de sauter à un symbole en appuyant sur `t` lorsque vous regardez des fichiers dans une pull request.

![Image](https://cdn-media-1.freecodecamp.org/images/GtVvg9u3g5LxiMrQFKUJvnwBxSKJnqBIusRn)

#### Créer un permalien vers un fichier

Lorsque vous consultez un fichier ou un répertoire, appuyez sur `y`, et l'URL sera convertie en permalien, que vous pouvez partager en toute sécurité en sachant que le contenu du fichier ne changera jamais.

Si vous envoyez un lien vers un fichier ou un répertoire sur GitHub sans en faire un permalien, vous devrez accepter la possibilité que le fichier puisse disparaître demain, brisant le lien !

#### Visualisation du blame et de la heatmap de récence des modifications

Lorsque vous consultez un fichier, vous pouvez appuyer sur `b` pour voir le Git blame et une heatmap montrant à quel point chaque ligne a été modifiée récemment. Cela vous indiquera qui a modifié chaque ligne de code le plus récemment, et vous donnera un lien cliquable vous menant au commit complet dont la modification faisait partie.

Sur le côté droit de la gouttière (qui contient le message de commit et l'auteur), vous remarquerez une barre verticale orange. Plus cette barre est vive, plus la modification est récente, ce qui signifie que vous pouvez facilement parcourir le fichier pour trouver le code le plus récent !

![Image](https://cdn-media-1.freecodecamp.org/images/FR-8iyQXhZK6JQJFpAgZHwvNNZ3Id5wJLimf)

#### Recherche de code puissante

GitHub indexe la plupart du code et offre une fonctionnalité de recherche puissante. Si vous avez besoin de trouver quelque chose dans un dépôt, mais que vous ne prévoyez pas d'y apporter des modifications. Il est généralement inutile de cloner le dépôt. Appuyez sur `/` pour rechercher tout le code dans le dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/l8wrWB-R4yR8PuIt1v5-P9OnlZsRfQkjsCLx)

Si votre recherche contient plusieurs mots et que vous souhaitez rechercher des occurrences de votre requête de recherche spécifique, mettez des guillemets autour de la requête. Vous pouvez également filtrer vos recherches par d'autres choses, telles que la taille du fichier, l'extension, le chemin où se trouve le fichier, et bien plus encore.

#### Réponses enregistrées

Si vous vous retrouvez à répéter les mêmes commentaires, vous gagnerez du temps en créant une [réponse enregistrée](https://github.com/settings/replies). La prochaine fois que vous trouverez que vous allez taper ce commentaire à nouveau, vous pourrez simplement le sélectionner dans un menu déroulant :

![Image](https://cdn-media-1.freecodecamp.org/images/VTyPo1p4GAYysIzfHuYTzKsWi3fEUrK-JjHW)

Pour effectuer l'action ci-dessus sans utiliser ma souris, je peux faire `ctrl` + `/` suivi de `ctrl`+ `1`.

#### Conclusion

Merci d'avoir lu. J'espère que vous avez trouvé au moins une chose sur cette page qui fera de vous un utilisateur plus productif de GitHub. Si vous avez aimé cet article ou si vous avez des commentaires en général, faites-le moi savoir !

Si vous êtes intéressé par plus de contenu comme celui-ci, suivez-moi sur [Twitter](https://twitter.com/_darrenburns).

Publié à l'origine sur mon [blog](https://darrenburns.net/posts/github-tips).

**P.S.** Vous pouvez créer votre propre Octocat pour le partager comme celui de la photo de couverture sur [myoctocat.com](https://myoctocat.com) !