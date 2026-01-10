---
title: Pourquoi vous ne devriez jamais demander à un développeur de réparer votre
  vélo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-12T15:25:51.000Z'
originalURL: https://freecodecamp.org/news/why-you-shouldnt-ask-a-developer-to-fix-your-bike-336be286fc37
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Pl320OpAF3mO0Ln_KaBqmA.jpeg
tags:
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi vous ne devriez jamais demander à un développeur de réparer votre
  vélo
seo_desc: 'By Andrew Burmistrov

  I used to work as a system administrator. I spent my days repairing PCs, doing backups,
  and restoring deleted emails that had suddenly become very important. But sometimes
  I got really weird requests. Like fixing a microwave. Or ...'
---

Par Andrew Burmistrov

Je travaillais autrefois comme administrateur système. Je passais mes journées à réparer des PC, à faire des sauvegardes et à restaurer des emails supprimés qui étaient soudainement devenus très importants. Mais parfois, je recevais des demandes vraiment étranges. Comme réparer un micro-ondes. Ou changer une ampoule dans les toilettes des femmes. Un jour, quelqu'un m'a même demandé si j'étais bon avec les mixeurs.

C'est ainsi que les gens ont tendance à voir les techniciens. Oui, nous savons des choses : nos choses. Et parfois, nous sommes aussi coupables de nous illusionner en pensant que nous sommes bons dans d'autres domaines liés à la technologie. Mais tous les domaines liés à la technologie ne sont pas nos choses. Prenons les vélos, par exemple.

Si vous voulez réparer un vélo, vous devez savoir comment il fonctionne. Et si vous savez comment il fonctionne, vous pouvez facilement **dessiner** un vélo. La plupart des gens sont convaincus de savoir comment fonctionne un vélo. Et pourtant, si vous leur demandez de dessiner un vélo, leurs dessins peuvent ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/zu9XyJqYcO9ANi4OPaiz5GH8DV3RcoqHYwLz)

Les scientifiques appellent cela une illusion de connaissance. Notre cerveau nous convainc plus facilement que nous savons quelque chose plutôt que de nous laisser admettre que nous ne le savons pas. National Geographic a réalisé un [épisode entier](http://www.dailymotion.com/video/x2aiyo7_what-you-dont-know-brain-games-episode-09_school) sur ce phénomène où **90 % des participants ont dessiné des vélos de manière irréaliste.**

Dans son célèbre projet [Velocipedia](https://www.behance.net/gallery/35437979/Velocipedia), Gianluca Gimini est allé encore plus loin. Il a demandé à différentes personnes de dessiner un vélo, puis a créé des modèles 3D basés sur leurs croquis :

![Image](https://cdn-media-1.freecodecamp.org/images/kLVm4pBnXTst-L7XYBaeKoxF94lpst3KUQDB)

Donc, 90 % des gens ne savent pas comment fonctionne un vélo. Et pourtant...

Dans les deux exemples mentionnés ci-dessus (National Geographic et le projet Velocipedia), les participants étaient des personnes ayant des connaissances générales (beaucoup étaient des étudiants). Aucun critère spécifique. C'est là que j'ai eu de la chance.

Récemment, nous avons entraîné un [réseau neuronal](http://ai.icons8.com/), dont le seul but était de reconnaître des icônes, dessinées par des personnes. Nous avons envoyé un email à notre base de données d'utilisateurs en demandant à nos clients de dessiner toutes sortes de choses : des voitures, des maisons, des poubelles... et des vélos.

Et notre audience se compose de :

![Image](https://cdn-media-1.freecodecamp.org/images/FsAgTMCGQvm2IQ7gYYtIDejlxo2iSSY9md0T)

La moitié des personnes à qui nous avons demandé de dessiner un vélo étaient des développeurs. Maintenant, la question se pose : **est-ce que 90 % des vélos seront toujours irréalistes, ou y aura-t-il une amélioration étant donné que la moitié de l'audience est composée de développeurs ?**

### Aperçu

J'ai demandé à mon ami, un ingénieur et cycliste passionné (je vous ai dit que j'avais de la chance), de m'aider à analyser 200 dessins de vélos que nous avons ensuite classés en 4 catégories différentes :

![Image](https://cdn-media-1.freecodecamp.org/images/Rozq05FmDhAo0AKt31y7DeVRL6xm4hLhC9l8)

**Non roulable** : il s'agit généralement d'un dessin très primitif de deux roues et d'un cadre, attaché de manière à empêcher les roues de rouler du tout.

**Roulable en roulant** : ces vélos peuvent rouler, mais ne peuvent pas tourner. Ou, parfois, ne peuvent pas être assis dessus. Donc ces vélos sont pour des personnes très directes, qui n'ont pas le temps de s'asseoir.

**Roulable (plus ou moins)** : ceux-ci ont de petits problèmes comme l'absence de pédales/chaîne ou des structures redondantes du cadre.

**Totalement roulable** : les gens savaient vraiment ce qu'ils dessinaient là.

Globalement, 76 % des dessins étaient irréalistes, et non 90 %.

> Les développeurs dessinent des vélos qui sont réellement roulables légèrement plus souvent.

Avant de tirer des conclusions, cependant, il y a quelques facteurs importants qui pourraient affecter ce nombre.

### Dessin construit vs. préparé

Avant de demander à mon ami ingénieur de l'aide pour analyser les dessins, je lui ai demandé d'en dessiner un. Sans préparation et sans indices. Voici comment cela s'est passé :

![Image](https://cdn-media-1.freecodecamp.org/images/bnE8WjIspfXmtgZbnYMgS9kwDK4YQVx9LzwT)

Regardez comment il n'utilise pas certains raccourcis mentaux préparés pour les éléments, mais construit le vélo. C'est un **dessin construit**.

Les lignes peuvent être irrégulières et les proportions peuvent être faussées, mais ce n'est pas important. Vous verrez que ces vélos ont également été construits :

![Image](https://cdn-media-1.freecodecamp.org/images/Ee3O9zj8ptZXk08DpeExrQwxyTY4Z0-28yGx)

De l'autre côté, il y a assez peu de designers parmi notre audience (~30 %). Leurs dessins sont très précis.

![Image](https://cdn-media-1.freecodecamp.org/images/9YJdmQetmOu-v3a2exUbLciWQTgTOQJWjzPB)

Ce sont des **dessins préparés**. Heureusement, seulement une très petite portion de tous les dessins semblait être préparée. Donc j'ai pu conclure deux choses :

* Cela n'affecte pas beaucoup les chiffres globaux
* 30 % de notre audience est composée de designers, mais seulement une petite portion des dessins était préparée. Je suppose que peu de designers sont capables de dessiner un vélo de mémoire. D'ailleurs, à en juger par cette [expérience](https://icons8.com/articles/how-good-are-designers-at-following-references-a-fiverr-experiment/), même si vous leur donnez une référence, cela peut ne pas suffire.

### Autres facteurs

Il y a quelques autres facteurs en jeu ici :

#### Il s'agissait d'une expérience non contrôlée

Les dessins n'étaient pas limités dans le temps et il n'y avait pas d'observateurs — les gens pouvaient chercher une référence sur Google. Mais à en juger par le nombre de vélos inhabituels, peu d'entre eux l'ont fait. Même lorsqu'on leur en donne l'occasion, les gens préfèrent encore inventer :

![Image](https://cdn-media-1.freecodecamp.org/images/hNMb7joDVNs7l2CBE9UqJQPvOVVcrawxkvFF)

> « Un seul designer ne pourrait pas inventer autant de nouveaux designs de vélos en 100 vies. Et c'est pourquoi je regarde cette collection avec tant d'admiration. » — **Gianluca Gimini, Velocipedia**

### Pays

![Image](https://cdn-media-1.freecodecamp.org/images/9xc5ZYVYgsLal0v-ZdFWCTTPmrfX1LzUSAdw)

Les vélos sont plus populaires dans certains pays que dans d'autres. Mais seulement l'un de nos cinq principaux pays en termes de trafic (le Japon) figure sur la [liste](http://top10hell.com/top-10-countries-with-most-bicycles-per-capita/). J'adorerais voir à quel point les gens sont bons pour dessiner des vélos aux Pays-Bas, où il y a plus de vélos par habitant que de chevaux dans l'armée mongole.

### Conclusion

Avec tous les facteurs mentionnés — plus les erreurs statistiques — le nombre de personnes qui dessinent des vélos de manière irréaliste est **5 à 10 % inférieur parmi les développeurs** que dans la population générale.

C'est un grand écart, cependant, car il y a tant de facteurs en jeu, comme la croissance générale de la popularité des vélos au cours des dernières années, les spécificités de genre ([92 % des développeurs sont des hommes](http://fusion.net/story/115998/survey-says-92-percent-of-software-developers-are-men/)). Oui, j'aimerais penser que les développeurs sont assez compétents pour dessiner des vélos réalistes, mais les chiffres ne sont pas assez dramatiques pour vraiment tirer cette conclusion.

Je vais donc terminer cet article comme je l'ai commencé. Avec mon propre exemple.

J'ai réparé des centaines de PC, configuré de nombreux appareils réseau. Je n'ai jamais réparé un seul vélo de ma vie.

Donc, après avoir regardé des centaines de dessins de vélos, j'ai décidé d'en dessiner un moi-même. Pas pour le copier, mais pour le construire réellement dans ma tête, à partir de zéro. Sans références ni raccourcis mentaux.

Le voici :

![Image](https://cdn-media-1.freecodecamp.org/images/lq0JiR4FJ7h0pzSwHf7ir4OOla3w1yUjzMUE)

Bien que j'aie possédé une demi-douzaine de vélos, je n'ai jamais eu l'occasion d'en réparer un et je n'en ai jamais eu la motivation. J'ai fait une erreur dans le cadre de la roue. Mon vélo ne peut pas tourner.

Je ne dis pas que les techniciens ne peuvent pas réparer les choses. Je crois que les techniciens sont compétents, et réparer un vélo est plus facile que de migrer d'un framework à un autre, tout en couvrant chaque partie du code avec des tests. Tout est possible, si vous avez la motivation.

Je dis que vous **ne devriez pas vous attendre à ce que les développeurs soient bons pour réparer d'autres choses**. Donc, si vous voulez vraiment que je répare votre vélo, essayez de me donner une motivation. Un cupcake est un bon début.

**À propos de l'auteur**  
[Andrew](https://twitter.com/ABNovels) a commencé chez Icons8 en tant que spécialiste de l'utilisabilité, menant des interviews et des enquêtes d'utilisabilité. Il voulait désespérément partager ses découvertes avec notre communauté professionnelle et a commencé à écrire des histoires perspicaces et drôles (parfois les deux) pour notre blog.

_Suivez Icons8 : [Twitter](https://twitter.com/icons_8) | [Facebook](https://www.facebook.com/Icons8/) | [Dribbble](https://dribbble.com/icons8)_