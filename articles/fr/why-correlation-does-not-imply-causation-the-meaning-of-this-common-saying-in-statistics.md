---
title: Pourquoi la corrélation n'implique pas la causalité - La signification de ce
  dicton courant en statistiques
subtitle: ''
author: Abigail Rennemeyer
co_authors: []
series: null
date: '2019-11-12T17:50:00.000Z'
originalURL: https://freecodecamp.org/news/why-correlation-does-not-imply-causation-the-meaning-of-this-common-saying-in-statistics
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f61740569d1a4ca4250.jpg
tags:
- name: statistics
  slug: statistics
seo_title: Pourquoi la corrélation n'implique pas la causalité - La signification
  de ce dicton courant en statistiques
seo_desc: 'You might remember this simple mantra from your statistics class:


  "Correlation does not imply causation."


  So maybe you think you know what this phrase means.

  Like, if you studied really hard in statistics, got a good grade, and then got into
  colleg...'
---

Vous vous souvenez peut-être de ce simple mantra de votre cours de statistiques :

> "La corrélation n'implique pas la causalité."

Alors peut-être pensez-vous savoir ce que signifie cette phrase.

Par exemple, si vous avez étudié très dur en statistiques, obtenu une bonne note, puis été admis à l'université, cela doit signifier que vous avez été admis à l'université parce que vous avez réussi votre cours de statistiques.

Bien que cette note, ainsi que les compétences que vous avez acquises, ont probablement aidé, vous ne pouvez pas ignorer les autres facteurs en jeu - et il est peu probable que vous puissiez affirmer que votre note en statistiques était la cause de votre admission à l'université.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/correlation.png)
_[Source de l'image : XKCD](https://imgs.xkcd.com/comics/correlation.png)_

## D'abord, pourquoi confondons-nous corrélation et causalité ?

Il est facile de penser que simplement parce que deux choses semblent liées, l'une doit être la cause de l'autre. Mais cela peut être une supposition stupide et parfois dangereuse.

Par exemple, supposons que vous essayez de déterminer ce qui rend les gens moins grincheux. Vous réalisez une étude qui montre que, lorsque les gens dorment au moins x heures par nuit, ils sont moins grincheux.

Mais avez-vous pris en compte tous les facteurs ici ? Peut-être ont-ils également commencé à faire plus de sport en conséquence d'être bien reposés, et c'est cela qui a modifié leur humeur.

Tous les exemples ne sont pas aussi bénins - et certains sont carrément nonsensiques.

Pour illustrer à quel point il peut être trompeur de supposer que la corrélation implique la causalité, regardez le graphique suivant de Tyler Vigen sur les [Corrélations fallacieuses](http://www.tylervigen.com/spurious-correlations) :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Ridiculous-correlation.png)
_Alors, si vous jouez plus aux jeux vidéo... vous obtiendrez un doctorat en informatique ??_

Bien qu'il y ait une forte corrélation entre ces deux facteurs, je doute que vous puissiez argumenter efficacement que l'un a causé l'autre. Peut-être sera-ce un défi pour les gens d'essayer de le prouver.

En voici une autre perle de la [collection de Tyler](http://tylervigen.com/spurious-correlations) :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screen-Shot-2019-09-21-at-2.26.01-PM.png)
_Si vous mangez plus de fromage... vous serez étranglé par vos draps ??_

Regardez cette belle corrélation. Mais vous auriez du mal à argumenter que, simplement parce que quelqu'un a mangé plus de fromage, il serait plus susceptible de s'emmêler mortellement dans ses draps.

### Qu'est-ce que la corrélation en statistiques ?

Selon le [dictionnaire](https://www.merriam-webster.com/dictionary/correlation), une **corrélation** est une relation ou une connexion mutuelle entre deux choses ou plus (ou variables) - surtout une qui n'est pas attendue sur la base du hasard seul.

Utilisons-la dans une phrase : La taille énorme de mes tomates cultivées à la maison semble être corrélée avec la pluie supplémentaire que nous avons eue cet été.

Maintenant, j'assume ici que, parce qu'il a plu un peu plus que d'habitude, mes plants de tomates ont produit des tomates monstres.

Mais est-ce le seul facteur ? Qu'en est-il du compost riche en nutriments que j'ai utilisé dans mes plates-bandes surélevées ? Qu'en est-il de la qualité des plants que j'ai achetés à la pépinière ? Qu'en est-il de ma taille soigneuse et de mon entretien ?

Comme vous pouvez le voir, bien qu'il y ait une corrélation entre mes grosses tomates et notre été pluvieux, cela n'implique pas nécessairement une causalité.

### Qu'est-ce que la causalité en statistiques ?

Il est temps pour une autre définition. **Causalité**, selon le dictionnaire, est l'acte ou l'agent qui produit un effet.

Soyons un peu plus spécifiques. La causalité signifie qu'il existe une relation entre deux événements où un événement affecte l'autre. En statistiques, lorsque la valeur d'un événement - ou variable - augmente ou diminue à cause d'un autre événement ou variable, nous pouvons dire qu'il y a eu causalité. A a **causé** B à se produire.

Et un exemple pour celui-ci ? Peut-être travaillez-vous en freelance pour un magazine qui paie au mot. Plus l'histoire est longue (et plus elle contient de mots), plus vous êtes payé.

Il y a donc une corrélation directe entre le nombre de mots que vous écrivez et le montant que vous êtes payé. Mais il y a aussi causalité (parce que vous avez écrit plus, vous avez été payé plus).

## Pourquoi est-il si facile de se tromper ?

Pourquoi est-il si facile de penser que la corrélation **implique** la causalité ? Eh bien, si deux choses semblent liées, nous avons tendance à les associer et à supposer qu'elles s'impactent mutuellement. Lorsque le temps est froid, les gens passent plus de temps à l'intérieur. Pendant les vacances, les centres commerciaux sont bondés. Lorsque vous prenez de l'ibuprofène, votre mal de tête disparaît.

Bien que ces circonstances soient certainement liées - et certaines pourraient même impliquer une causalité - elles ne résistent pas nécessairement à une analyse scientifique.

Il y a quelques raisons pour lesquelles nous pourrions à tort déduire la causalité de la corrélation.

### Qu'est-ce qu'une variable confondante ?

Tout d'abord, vous pourriez avoir une **variable confondante** dans le mélange. Il s'agit d'une variable qui affecte à la fois les variables indépendantes et dépendantes dans votre relation - et confond ainsi votre capacité à déterminer la nature de cette relation.

Par exemple, si une nouvelle famille emménage dans un quartier et que la criminalité augmente, les résidents de cette zone pourraient supposer que c'est à cause de cette nouvelle famille. Mais que se passe-t-il si, en même temps, un centre de détention a ouvert à proximité ? C'est la cause la plus probable de l'augmentation de la criminalité.

### Qu'est-ce que la causalité inverse ?

Deuxièmement, vous pourriez avoir affaire à une **causalité inverse**. Cela se produit lorsque, au lieu de supposer correctement que A cause B, vous les mélangez et supposez que B cause A.

Il peut être difficile d'imaginer comment cela se produit, mais pensez au fonctionnement des panneaux solaires. Ils produisent plus d'énergie lorsque le soleil est dans le ciel plus longtemps.

Mais le soleil n'est pas dans le ciel plus longtemps parce que les panneaux produisent plus d'énergie. Les panneaux produisent plus d'énergie parce que le soleil brille pendant de plus longues périodes.

### Qu'est-ce qu'une coïncidence ?

Troisièmement, nous ne devons pas oublier le pouvoir de la **coïncidence**. Lorsque deux choses se produisent en même temps, il est tentant de voir une causalité. Mais comme ce graphique stupide ci-dessus, avec les arcades et les diplômes en informatique, beaucoup ne sont que des coïncidences.

### En fin de compte - pourquoi nous en soucions-nous ?

Peut-être essayez-vous de déterminer si un certain nouveau médicament fait sentir les patients mieux. Ou vous aimeriez savoir ce qui pousse les gens à acheter un certain produit.

Quelle que soit votre motivation, il est souvent très utile de déterminer si A cause B, ainsi que comment et pourquoi.

Mais comme nous l'avons vu, ce n'est pas si facile. Vous devez contrôler autant de facteurs que possible, réduire la probabilité de variables confondantes et de coïncidences, et réduire les données à ce qui est pertinent.

Nous n'aborderons pas la question philosophique plus profonde de savoir comment nous pouvons vraiment établir la causalité sans aucun doute. Cela sera pour une autre fois.

Au moins maintenant vous savez que - même si deux événements ou variables peuvent sembler liés - cela ne signifie pas que l'un a un effet causal direct sur l'autre.