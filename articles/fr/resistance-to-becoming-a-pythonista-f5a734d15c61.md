---
title: Comment j'ai surmonté ma résistance à devenir un Pythonista
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-28T00:36:41.000Z'
originalURL: https://freecodecamp.org/news/resistance-to-becoming-a-pythonista-f5a734d15c61
coverImage: https://cdn-media-1.freecodecamp.org/images/0*8-Fy9RNpdEIE4XTW
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment j'ai surmonté ma résistance à devenir un Pythonista
seo_desc: 'By Semi Koen

  For over a decade, my main ‘mother tongue’ has been C#. I have been using it since
  version 1, and loved the journey through features such as generics, anonymity, LINQ,
  and async and combining this with design patterns, SOLID principles, ...'
---

Par Semi Koen

Pendant plus d'une décennie, mon principal "langage maternel" a été C#. Je l'utilise depuis la version 1, et j'ai adoré le voyage à travers des fonctionnalités telles que les génériques, l'anonymat, LINQ, et async, en combinant cela avec des modèles de conception, les principes SOLID, les styles architecturaux et TDD/BDD, je vis et respire maintenant C#. Je regardais autrefois avec dédain les langages de script...

_Comment pouvez-vous vous appeler ingénieur logiciel et utiliser un langage de script ? Doh !_

Je travaille dans une organisation financière dans la City. Les langages de choix ont été Java et C#, pour les applications Front et Back Office. La science des données et l'apprentissage automatique sont devenus deux des technologies modernes les plus en vogue et ils se développent également dans les institutions financières. Comme mon parcours est en informatique (avec mon mémoire sur l'exploration de données et l'intelligence artificielle), j'ai pensé que je devrais vérifier cela...

J'ai dû rafraîchir mes connaissances en mathématiques, et après une [introduction au ML sur Pluralsight](https://www.pluralsight.com/courses/understanding-machine-learning) et [une autre sur Python](https://www.pluralsight.com/courses/python-getting-started), je n'ai pas compris tout ce tapage.

_Pourquoi utiliser Python ? Je peux faire toutes ces choses en C#... et en fait beaucoup mieux !_

J'ai dit fièrement à mon collègue : "Je ne suis pas un 'cowboy codeur'... Vous ne pouvez pas écrire une application Python SOLID".
Et il a dit : "Pourquoi pas ? SOLID sont juste des principes. Vous pouvez les appliquer dans n'importe quel langage".

_Cela a été une révélation pour moi._

J'ai commencé à rechercher Python : Il est dans le top trois des langages de programmation (en décembre 2018) [selon TIOBE](https://www.tiobe.com/tiobe-index). StackOverflow confirme qu'il [a dépassé C#](https://insights.stackoverflow.com/survey/2018/#most-popular-technologies). Il en va de même pour le [Rapport HackerRank](https://research.hackerrank.com/developer-skills/2018).

_Quoi ? Est-ce que je rate quelque chose ?_

C'est ainsi que mon voyage pour devenir un Pythonista a commencé... J'ai dû être convaincu que cela en valait la peine.

Voici les réponses à deux de mes principales réserves, c'est-à-dire :

1. J'aime ma carrière dans le secteur financier. _Qu'est-ce qui fait que les organisations financières utilisent Python ?_
2. Je ne suis pas un 'cowboy' ('cowgirl' plutôt). _Les principes SOLID s'appliquent-ils en Python ?_

### Pourquoi les organisations financières utilisent-elles Python ?

Mes recherches m'ont montré qu'il y a plusieurs raisons :

**— Mise sur le marché rapide :** Vous pouvez passer de "zéro à héros" assez rapidement. Il existe un ensemble riche de bibliothèques qui ont à peu près tout ce que vous utiliserez jamais. Écrire des programmes Python, c'est comme construire une tour avec des Lego. Vous pouvez trouver les blocs individuels et tout ce que vous avez à faire est de les coller ensemble pour construire votre algorithme.

**— Pont entre l'économie et l'IT :** Les quants et les personnes d'affaires techno-savvy peuvent comprendre et aussi écrire leurs algorithmes en Python. Les développeurs peuvent ensuite les intégrer dans une application full stack.

**— Embrasse l'analyse :** Anaconda vient avec une installation du notebook Jupyter. C'est le terrain de jeu de chaque développeur et scientifique de données pour analyser les données et créer des visualisations. Le trading, les prix du marché, la modélisation des risques financiers sont quelques domaines applicables.

### Les principes SOLID s'appliquent-ils en Python ?

OUI — Ils le font ! Les principes ne sont pas une fin en soi. Ce sont plutôt des directives pour écrire un meilleur et plus propre code. Cependant, il n'y a pas de solution miracle pour les appliquer dans les langages fonctionnels/dynamiques.

Néanmoins, voici ce que j'ai trouvé :

**— Responsabilité unique :** Une classe ne doit avoir qu'une seule raison de changer.

C'est assez simple, il suffit de regrouper les fonctions qui changent pour la même raison dans une seule classe/méthode/entité. Comme en C#.

**— Ouvert/Fermé :** Les classes doivent être ouvertes pour l'extension et fermées pour la modification. La classe de base/abstraite est fermée pour la modification. Des sous-classes concrètes sont créées pour modifier leur comportement.

De nombreuses façons d'y parvenir incluent : l'héritage, la composition, les modèles de conception (Decorator, Strategy, etc.). Python permet l'héritage multiple des classes, autre que cela, c'est la même chose qu'en C#.

**— Substitution de Liskov :** Si S est un sous-type de T, alors les objets de type T peuvent être remplacés par des objets de type S sans altérer aucune des propriétés souhaitables de T. En d'autres termes, la classe dérivée doit étendre sa classe parente sans changer son comportement.

Tant que vous pouvez distinguer la différence entre la composition et l'héritage, alors Bob est votre oncle. Soyez également conscient du monkey patching car cela brisera certainement ce principe.

**— Ségrégation des interfaces :** Les clients ne doivent pas être forcés de dépendre d'interfaces qu'ils n'utilisent pas.

Il n'y a pas d'interfaces en Python, donc cela n'est pas trop pertinent. Mais en général, il s'agit de garder les classes et les méthodes exposées à un minimum ainsi que la capacité d'hériter de plusieurs classes concrètes afin de fournir aux clients des comportements spécifiques.

**— Inversion des dépendances :** Les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. Les deux doivent dépendre des abstractions. Les abstractions ne doivent pas dépendre des détails — les détails doivent dépendre des abstractions.

En tant que langage dynamique, Python n'exige pas l'utilisation d'abstractions pour faciliter le découplage.

Ce que j'espérais trouver lorsque j'ai commencé cette analyse, c'est que C# gagne la 'Bataille des Langages' contre Python, mais j'ai réalisé que c'est un mauvais programmeur dont la boîte à outils de développement ne contient qu'un seul langage de programmation !

J'utiliserais personnellement C# pour construire une application à grande échelle, d'entreprise (surtout côté serveur), mais je suis totalement converti à Python pour un développement plus rapide et des preuves de concept — principalement lorsqu'il s'agit des domaines de la science des données ou de l'apprentissage automatique !

Merci d'avoir lu mon premier article ?