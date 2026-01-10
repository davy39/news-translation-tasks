---
title: Comment nous avons obtenu 1 500 étoiles GitHub en mélangeant une technologie
  éprouvée avec une nouvelle interface utilisateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-16T06:43:00.000Z'
originalURL: https://freecodecamp.org/news/how-we-got-1-500-github-stars-by-mixing-time-tested-technology-with-a-fresh-ui-b310551cba22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dRitLnbV0KDrtHFtsI2ZzQ.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment nous avons obtenu 1 500 étoiles GitHub en mélangeant une technologie
  éprouvée avec une nouvelle interface utilisateur
seo_desc: 'By Roman Hotsiy

  Recently we released an open-source tool called GraphQL Voyager. Surprisingly, it
  got to the first page of Hacker News and GitHub trending and gained 1,000+ stars
  in the first few days. As of now it has more than 1,600 stars.

  People l...'
---

Par Roman Hotsiy

Récemment, nous avons publié un outil open-source appelé [GraphQL Voyager](https://github.com/APIs-guru/graphql-voyager). Étonnamment, il a atteint la première page de Hacker News et GitHub trending et a gagné plus de 1 000 étoiles dans les premiers jours. À ce jour, il compte plus de [1 600 étoiles](https://github.com/APIs-guru/graphql-voyager/stargazers).

Les gens ont adoré l'interface utilisateur élégante, les fonctionnalités interactives et les animations. Nous avons utilisé TypeScript, React, Redux, webpack et même PostCSS, mais ceci **N'EST PAS** **un autre article à leur sujet**. Regardons sous le capot...

### Notre histoire

Tout a commencé il y a quelques mois. Mon ami et moi (nous nous appelons [APIs.guru](https://apis.guru)) cherchions une idée pour un projet autour de [GraphQL](https://graphql.org/) (un langage de requête pour les API développé par Facebook). Après quelques recherches, un outil intéressant a attiré notre attention — [GraphQL Visualizer](http://nathanrandal.com/graphql-visualizer/).

![Image](https://cdn-media-1.freecodecamp.org/images/xrsITDwSIv3dVd8gMfx1kOaKP3Cc6Rw0EkQr)
_Sortie de GraphQL Visualizer_

Nous voulions ajouter :

* des couleurs (le noir et blanc semblait trop ennuyeux)
* un panoramique et un zoom
* des fonctionnalités interactives comme la sélection de nœuds et d'arêtes

Mais après avoir examiné le code source, nous avons trouvé un [défaut fatal](http://www.drdobbs.com/windows/a-brief-history-of-windows-programming-r/225701475) dans cet outil : il utilisait [Graphviz](http://www.graphviz.org/) — un outil vieillard écrit en C pur et compilé en JavaScript illisible en utilisant [Emscripten](https://github.com/kripken/emscripten).

![Image](https://cdn-media-1.freecodecamp.org/images/8tWF9RgASDSh2i-jlgIKWbwMb3fekhX5M9CL)
_Encore pire que la sortie habituelle de Uglify.js_

Comment pourrions-nous utiliser quelque chose des années 2000 ? Nous sommes des hipsters, bon sang ! ReactJS, D3, webpack, TypeScript, PostCSS — c'est avec ça que nous travaillons ! Pas avec des outils écrits en C à l'ancienne ?.

Après une petite recherche, nous avons trouvé la meilleure bibliothèque pour la tâche — [Cytoscape.js](http://js.cytoscape.org/). Elle était écrite dans le merveilleux JavaScript et supportait même l'exécution de sélecteurs de type CSS sur le graphe lui-même. Quel excellent résultat !

Après une semaine de codage intensif, le résultat était moins que satisfaisant. Voyez par vous-même :

![Image](https://cdn-media-1.freecodecamp.org/images/suwBiGVSkhBNW5B9dZMTQQ7UNCTnrQY6HZjf)
_Graphe visualisé en utilisant Cytoscape.js_

Et cela sans même afficher tous ces détails sur le graphe ! Quel désordre !

Bien que le code était beaucoup plus propre, le résultat final était bien pire par rapport à l'outil original. Complètement inutilisable.

Il est apparu qu'il n'y avait aucun moyen pour cytoscape.js d'avoir des arêtes qui ne croisent pas les nœuds. Nous avons tout essayé de notre boîte à outils. Nous avons googlé. Nous avons posé des questions sur StackOverflow. Nous avons même dérangé quelques gourous SVG que nous connaissions. Zéro succès :(

En dernier recours, j'ai même essayé de bidouiller cytoscape.js pour produire un résultat lisible. Un peu plus de recherche m'a fait abandonner : apparemment, la visualisation de graphes **est** une science de fusée (même lorsque vous avez un master en mathématiques appliquées).

Nous avons été vaincus...

Et puis une idée nous est venue. Et si nous prenions la sortie de Graphviz (qui est juste du SVG pur) et que nous l'assaisonnions avec un peu de CSS et de JS ?

Et cela a fait l'affaire ✨

![Image](https://cdn-media-1.freecodecamp.org/images/nW0lS1sFHqG7xOiU0t0N9mSpTTKMYDOcgwTe)

Beaucoup mieux ! Et moins d'une journée de codage ?.

En ajoutant un peu de couleur, un logo, une animation de chargement, quelques fonctionnalités utiles de plus et nous voilà :

![Image](https://cdn-media-1.freecodecamp.org/images/3AwUl3XL7ZuJOXV4HfwdtAy8F-rccxjDFzFa)
_Le résultat final_

Oui, nous avons écrit quelques centaines de lignes de manipulations DOM laides. Oui, nous avons emballé tout ce désordre en tant que composant NOT PURE ? React/Redux. Et oui, le code Graphviz est si énorme que nous l'avons divisé en un fichier séparé de 2 Mo. Mais cela fonctionne et personne ne s'en soucie. 1 600 étoiles sur GitHub le confirment.

**MISE À JOUR :** depuis la soumission de l'article, le projet a été adopté par des entreprises du domaine (par exemple, Graphcool, Neo4j) et il a été présenté à GraphQL Europe, donc ce ne sont pas seulement 1600 étoiles qui le confirment :)

### Leçons apprises

> « Si j'ai vu un peu plus loin, c'est en montant sur les épaules de géants. » — Isaac Newton

Ne jugez pas le code par son âge. Surtout s'il a été écrit par des géants de la technologie comme [AT&T Labs](https://en.wikipedia.org/wiki/AT%26T_Labs) (l'endroit où Unix et les langages C et C++ sont nés).

Malheureusement, nous avons été affectés par un biais cognitif : l'ancien code est mauvais. Mais la vérité peut être l'inverse. L'ancien code est testé par des milliers d'utilisateurs dans des centaines de projets différents. La plupart des bugs critiques ont été corrigés, la documentation est complète, il y a des tonnes de questions et de réponses sur StackOverflow et Quora.

Nous vivons en 2017, et une interface utilisateur des années 2000 n'est définitivement pas acceptable. Mais les graphes et les mathématiques qui les sous-tendent ne changent pas beaucoup.

La même ligne de pensée peut être appliquée à de nombreux autres domaines. Donc l'ancien code devrait être donné une chance, surtout puisque vous pouvez toujours l'envelopper dans une interface utilisateur moderne.

C'est pourquoi nous voyons un énorme potentiel dans [Web Assembly](http://webassembly.org/). Il permettra de fusionner des implémentations d'algorithmes éprouvées avec des interfaces utilisateur modernes. Nous avons hâte de voir les choses incroyables que les gens construiront avec cela.

### « Emm.. vous avez promis de me dire comment obtenir beaucoup d'étoiles »

Oups... OK. Vous m'avez eu. Je voulais rendre le titre assez accrocheur.

Ci-dessous se trouve une liste de contrôle des conseils et astuces les plus importants que nous utilisons pour notre projet open-source :

* Essayez d'utiliser le nom de votre technologie comme partie du nom de votre projet (par exemple, graphql-quelquechose, react-quelquechose, etc.). De cette façon, votre projet aura un meilleur classement dans les résultats de recherche GitHub pour ces technologies.
* Votre README devrait attirer l'attention des gens. Nous avons ajouté un gif animé en haut de notre README afin que les gens puissent comprendre immédiatement de quoi il s'agit. Si c'est une application console — ajoutez un gif avec la console (voici un exemple [awesome](https://github.com/graphcool/graphql-up)).
* Plus de clochettes et de sifflets : ajoutez des badges, ajoutez un logo attrayant, ajoutez des emojis ? ?
* Configurez une démonstration si possible, et ajoutez un lien vers celle-ci dans le champ de description du dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/YTnNgu5HMPJZVAjPeCM3ljlLsxRmDOHuhD3v)

* Encore une fois, **configurez une démonstration** ! Et n'oubliez pas d'ajouter un lien de la démonstration vers GitHub (nous utilisons [GitHub Corners](http://tholman.com/github-corners/)).
* Avant de le publier sur HackerNews/Reddit/etc., obtenez un nombre initial d'étoiles (5–10) en le publiant sur des ressources moins populaires, ou en le partageant avec vos amis. Les gens sont moins susceptibles de cliquer sur « star » pour les projets avec zéro étoile.
* Essayez d'obtenir 30–40 étoiles le premier jour. De cette façon, vous êtes susceptible d'être mis en avant sur GitHub trending pour votre langage, ce qui est une autre source de trafic.
* **Faites quelque chose d'utile**.

Il y a quelques autres articles sur la façon de promouvoir des projets open-source : [ici](https://blog.cwrichardkim.com/how-to-get-hundreds-of-stars-on-your-github-project-345b065e20a2#.iudi1mx0q), [ici](https://medium.com/@zenorocha/how-did-clipboard-js-get-5000-stars-in-a-few-days-2b2248ba7bd8#.wvvstia5n), et [ici](https://medium.com/developer-relations/how-talks-affect-an-open-source-project-e4dd1db81a6d#.ecb0kqb1p).

C'est tout, les amis. Si vous avez déjà enveloppé un ancien code dans une nouvelle interface utilisateur brillante ? racontez votre histoire dans les commentaires ci-dessous.