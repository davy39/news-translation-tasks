---
title: Si vous voulez parler d'accessibilité, alors nous devons parler des problèmes
  de lisibilité.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T14:14:17.000Z'
originalURL: https://freecodecamp.org/news/reading-accessibility-82d24841ac7e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*XasHqwgzIbn-rNW4
tags:
- name: Accessibility
  slug: accessibility
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: writing
  slug: writing
seo_title: Si vous voulez parler d'accessibilité, alors nous devons parler des problèmes
  de lisibilité.
seo_desc: 'By Code Girl

  Before I became a web developer, I was a college professor, and my major during
  my doctoral program was language and literacy acquisition. That’s a technical way
  of saying I studied how we learn to read and write. I worked with strugglin...'
---

Par Code Girl

Avant de devenir développeuse web, j'étais professeure d'université, et ma spécialité pendant mon programme doctoral était l'acquisition du langage et de la littératie. C'est une manière technique de dire que j'ai étudié comment nous apprenons à lire et à écrire. J'ai travaillé avec des lecteurs en difficulté de tous âges, spécifiquement au collège mais aussi avec des adultes.

Saviez-vous que le niveau de lecture moyen des adultes vivant aux États-Unis se situe entre la 7e et la 8e année, soit le niveau du collège ? C'est un fait triste. De plus, les gens préfèrent lire des textes d'environ deux niveaux scolaires en dessous de leur niveau de lecture, car c'est plus confortable.

En ce qui concerne le contenu technique, le niveau de lecture d'une personne diminue considérablement. Ils ne peuvent tout simplement pas comprendre le vocabulaire technique inconnu, la structure complexe des phrases et les mots à la mode qui n'ont aucun contexte pour eux.

Cela est d'une importance critique pour le contenu des sites web que vous construisez. Votre section **À propos**, vos **FAQ** et vos **Directives** sont généralement rédigées par des membres d'une équipe ayant une solide formation éducative, un niveau de lecture entre le lycée et l'université, et des compétences substantielles en rédaction. En d'autres termes, ce que vous écrivez pourrait ne pas être compréhensible par votre public.

En matière d'accessibilité, vous devez absolument vérifier la lisibilité de tout ce que vous voulez que votre public lise et comprenne. Et cela est important à garder à l'esprit pour les locuteurs natifs et non natifs de l'anglais.

Pour illustrer ce problème, je veux partager avec vous une expérience que j'ai eue au printemps de cette année. J'ai proposé mon aide à une organisation à but non lucratif fabuleuse, [Bank on Atlanta](http://bankonatlanta.org/), pour construire leur site web (travaillant sur la Phase 2 maintenant). Leur objectif est d'aider les citoyens à faible revenu et à faible littératie à apprendre la littératie financière, le prêt prédateur et la sécurisation de leur argent.

L'objectif du site web est d'afficher des informations clés puisque les participants travailleront directement avec des conseillers formés. Voici un lien vers la [Phase 1](https://fwallacephd.github.io/BOAClone/) du site web où l'organisation est décrite (intégrée ci-dessous). Prenez une minute et lisez cette description. En la lisant, essayez de deviner le niveau scolaire de ce passage.

![Image](https://cdn-media-1.freecodecamp.org/images/CK-AWdp0ljnfhrm7z8saAUnBcFNQPQ8T91Pp)
_Description de la Phase 1_

### Le score de facilité de lecture de Flesch et le niveau scolaire de Flesch-Kincaid

Bien qu'il existe de nombreux algorithmes pour évaluer la lisibilité, il existe deux principales mesures utilisées pour définir la lisibilité : le score de facilité de lecture de Flesch et le niveau scolaire de Flesch-Kincaid.

Le département de la Défense des États-Unis utilise le score de facilité de lecture de Flesch pour les documents et formulaires. La Floride l'utilise pour évaluer les polices d'assurance. Les forces armées utilisent le niveau scolaire de Flesch-Kincaid pour évaluer les manuels techniques.

Ces algorithmes (intégrés ci-dessous) mesurent la lisibilité en examinant la longueur moyenne des phrases (mesurée par le nombre de mots) et le nombre moyen de syllabes par mot (les mots avec des syllabes de 3 ou plus sont extrêmement difficiles pour les lecteurs en difficulté).

Un score élevé sur le score de facilité de lecture de Flesch indique une facilité de lecture, donc un score de 100 est idéal. Ce type de texte va droit au but avec des phrases courtes, aucun mot de plus de 2 syllabes, et aucun mot à la mode. Un score de 60–70 est considéré comme un score moyen.

Le niveau scolaire de Flesch-Kincaid est largement utilisé dans le domaine de l'éducation et utilise les mêmes mesures que le score de facilité de lecture de Flesch. La différence est qu'au lieu de présenter un score numérique, un niveau scolaire américain est attribué au passage, ce qui facilite la compréhension et l'adaptation des éducateurs, parents, bibliothécaires et autres à la capacité de l'élève.

![Image](https://cdn-media-1.freecodecamp.org/images/rcAHP9BCBFquAKA8i7-LHkq9o2lgKB-uwahj)
_de [Readable.io](https://readable.io/blog/the-flesch-reading-ease-and-flesch-kincaid-grade-level/" rel="noopener" target="_blank" title=")_

Quel niveau scolaire avez-vous deviné pour le passage sur Bank on Atlanta ?

Le passage sur le site de Bank on Atlanta a obtenu un score de 30,7 sur le score de facilité de lecture de Flesch, ce qui signifie difficile à lire. Sur le niveau scolaire de Flesch-Kincaid, le passage a obtenu un niveau de 14,2, ce qui signifie niveau universitaire.

Comme mentionné précédemment, les adultes de ce pays ont un niveau de lecture moyen entre la 7e et la 8e année, et le niveau de lecture des locuteurs non natifs de l'anglais varie considérablement.

Le diagramme ci-dessous illustre clairement ces résultats :

![Image](https://cdn-media-1.freecodecamp.org/images/38LeDRDDoIe7-sVvrPBWZFW4SgKmiE2JJ5hK)
_Le cercle orange indique le score de notre passage._

### Deux problèmes clés

Pour vous donner une idée de pourquoi ce passage est si difficile, je vais me concentrer sur deux problèmes clés.

Le premier problème est la longueur des phrases. Plus la phrase est longue, plus vous ajoutez de complexité à la phrase. Les phrases complexes peuvent avoir plusieurs sujets, verbes, objets, sans compter les clauses et phrases intégrées, et des temps qui peuvent changer. Lorsque le lecteur a du mal avec l'analyse des mots et les compétences en vocabulaire, les structures de phrases compliquées causent de la frustration au lecteur, ce qui peut le forcer à arrêter de lire.

À un niveau de lecture de 7e ou 8e année, un nombre confortable de mots par phrase serait de 13–16, mais la moyenne de notre passage était entre 20–22 (voir diagramme).

![Image](https://cdn-media-1.freecodecamp.org/images/v0052YuH8JATK5Ij4HsDk3zQZAYLmECVMVBi)

Les mots polysyllabiques sont des mots qui ont 3 syllabes ou plus. Ces mots sollicitent le lecteur pour décoder (ou prononcer) le mot ainsi que pour en comprendre le sens en même temps. Comprendre les bases/racines et les préfixes/suffixes est une compétence avancée, mais plus un mot a de syllabes, plus ces composants sont inclus.

Prenons, par exemple, un mot clé de notre passage « underbanked » — un mot de 4 syllabes avec trois parties significatives : « under » (2 syllabes), « bank », et la terminaison « ed ». Pire encore, c'est aussi un mot à la mode. Il n'a aucun contexte pour le lecteur.

Le pourcentage moyen de mots de 3 syllabes pour les lecteurs du secondaire et adultes aux États-Unis est entre 12–14 %. Le pourcentage de mots de 3 syllabes dans ce texte est entre 26–29 %. Cela est extrêmement élevé (voir diagramme).

![Image](https://cdn-media-1.freecodecamp.org/images/7-duAyMUtL3FSY2w0Wa7J1uSaouDVTIA6AxW)

### Révisions

Heureusement, il est facile de déterminer le niveau de lecture d'un passage et d'analyser pourquoi il est difficile. Il est plus difficile de réviser un passage pour abaisser le niveau de lecture plutôt que de commencer en prêtant attention à la longueur des phrases, aux mots polysyllabiques et même aux mots à la mode.

Heureusement, Bank on Atlanta s'engage à créer un site web où tous leurs lecteurs peuvent comprendre les informations nécessaires avec facilité.

En écrivant simplement des phrases plus courtes mais plus nombreuses, en éliminant les mots polysyllabiques et en limitant les mots à la mode, leur deuxième version a été beaucoup plus réussie :

![Image](https://cdn-media-1.freecodecamp.org/images/kbU3MxqMGq7TFAB1ZC4Y2wTZ3icDyr1QD94k)
_Description révisée_

La première version sur le site de Bank on Atlanta a obtenu un score de 30,7 sur le score de facilité de lecture de Flesch, ce qui est difficile à lire. Sur le niveau scolaire de Flesch-Kincaid, la première version a obtenu un niveau de 14,2, ce qui signifie niveau universitaire.

Cette deuxième version a obtenu un score de 64,5, considéré comme moyen, sur l'échelle de facilité de lecture de Flesch, et un niveau scolaire de 8,4 sur le niveau scolaire de Flesch-Kincaid. Cette révision a été un énorme succès !

Étant donné que notre public cible est composed de lecteurs en difficulté, nous avons encore des révisions à faire. Au mieux, nos passages devraient être à un niveau de lecture de 5e année. Mais l'important est que l'équipe a fait de la lisibilité une priorité et nous progressons.

Pour déterminer la lisibilité des passages sur vos sites web, utilisez cet [outil gratuit](https://www.online-utility.org/english/readability_test_and_improve.jsp). Il vous fournira des scores pour le score de facilité de lecture de Flesch et le niveau scolaire de Flesch-Kincaid, et espérons que vous ferez des révisions basées sur vos scores.