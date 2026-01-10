---
title: Comment lier un paragraphe spécifique dans votre article Medium (méthode de
  la Table des matières)
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2018-02-22T20:47:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UCdiE5IGAlQt8YJ-vKWv1A.png
tags: []
seo_title: Comment lier un paragraphe spécifique dans votre article Medium (méthode
  de la Table des matières)
seo_desc: 'Update Feb 26, 2018: a member of the freeCodeCamp community just built
  a tool that makes this process extremely convenient. Instead of using the method
  I describe in this article, I recommend you just use his website.


  A screenshot from mediumtoc.com...'
---

**Mise à jour du 26 févr. 2018** : un membre de la communauté freeCodeCamp a créé un outil qui rend ce processus extrêmement pratique. Au lieu d'utiliser la méthode que je décris dans cet article, je vous recommande d'utiliser simplement [son site web](https://www.mediumtoc.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/gIWQ-TirKtcVt91mqai-UHzE0aBbNBiUYZkM align="left")

*Une capture d'écran de* [*mediumtoc.com*](https://www.mediumtoc.com/)

Je vais vous montrer comment créer une belle Table des matières avec des liens hypertextes pour vos articles Medium. Voici à quoi cela ressemblera dans votre article Medium :

![Image](https://cdn-media-1.freecodecamp.org/images/2eyEr6YvptG9w1PAfp1jNJfq1OCrN68dKnqO align="left")

Chacun de ces liens vous amènera à une partie spécifique de l'article. C'est une amélioration majeure de l'ergonomie pour vos lecteurs. Surtout si votre article est assez long pour nécessiter plusieurs sessions de lecture pour être terminé.

Sur la [publication Medium de freeCodeCamp](https://medium.freecodecamp.org), nous publions fréquemment des articles qui nécessitent 20 minutes, 40 minutes, voire 60 minutes de lecture. Et nous trouvons ces Tables des matières super utiles.

Notez que la technique que je partage ici dans cet article donne des résultats mitigés sur les appareils mobiles. Alors espérons que Medium ajoutera officiellement cette fonctionnalité à l'avenir.

### Preuve que cela fonctionne

En cliquant sur [ce lien](https://medium.com/p/e66595fea549#ddca), vous serez transporté directement à cette partie exacte de cet article.

### Voici comment faire cela.

Chaque titre sur Medium est son propre élément HTML, avec son propre `id`.

Pour obtenir l'`id` du titre, vous devez faire un clic droit dessus, puis cliquer sur "inspecter".

Cela ouvrira les outils de développement de votre navigateur. Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/wjuRelJMIPs2ShBj8LjFTv8Jzrfy2XRe64BE align="left")

Maintenant, vous devez simplement obtenir le code hexadécimal à 4 chiffres associé à cet élément HTML. Dans ce cas, l'`id` du titre "Hello, World!" est `48f5`.

Vous pouvez maintenant utiliser ce code pour créer un lien spécial qui pointera directement vers ce titre. Ces liens suivent cette structure :

`https://medium.com/p/[ID de l'article]#[code hexadécimal à 4 chiffres]`

* L'**ID de l'article** est le code hexadécimal à 12 chiffres pour l'article Medium. L'un de ces codes est présent dans chaque URL Medium. Par exemple, l'ID de l'article que vous lisez est `e66595fea549`. Allez-y — vérifiez la barre d'adresse de votre navigateur et vous devriez voir ce code dans l'URL. Ce code est l'identifiant universel de votre article et il ne changera jamais — même si vous changez le titre de votre article ou le publiez dans une publication Medium.

* Le **code hexadécimal à 4 chiffres** est le code que vous avez obtenu à partir des outils de développement (dans ce cas, `48f5`).

Voici l'URL que j'ai utilisée précédemment pour lier à ma section "preuve que cela fonctionne" :

```javascript
https://medium.com/p/e66595fea549#ddca
```

### Construisons une table des matières !

Voici cette table des matières que je vous ai montrée précédemment. Chacun de ces liens pointera vers une section différente du même article :

#### Table des matières

* [Avertissements](https://medium.com/p/1c96572a1401#0239)

* [Les sept ponts de Königsberg](https://medium.com/p/1c96572a1401#48f5)

* [Introduction à la représentation des graphes et aux arbres binaires (exemple Airbnb)](https://medium.com/p/1c96572a1401#0374)

* [Représentation des graphes : conclusion](https://medium.com/p/1c96572a1401#fb0c)

* [Exemple Twitter : problème de livraison de tweets](https://medium.com/p/1c96572a1401#0cd4)

* [Algorithmes de graphes : introduction](https://medium.com/p/1c96572a1401#fb0c)

* [Netflix et Amazon : exemple d'index inversé](https://medium.com/p/1c96572a1401#cdde)

* [Parcours : DFS et BFS](https://medium.com/p/1c96572a1401#45f6)

* [Uber et le problème du plus court chemin (algorithme de Dijkstra)](https://medium.com/p/1c96572a1401#aa4d)

### Une extension Chrome pour faciliter ce processus

En réponse à cet article, [Cadu de Castro Alves](https://www.freecodecamp.org/news/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549/undefined) [a créé une extension Chrome](https://github.com/castroalves/medium-anchor-url-generator) qui rend l'extraction des ID des différents paragraphes plus simple.

### C'est tout. Amusez-vous bien et bon écriture !

Si vous avez trouvé cet article utile, vous devriez [me suivre sur Twitter](https://www.twitter.com/ossia). Je ne tweete que sur la programmation et la technologie, et je ne perdrai pas votre temps :)