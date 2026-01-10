---
title: Qu'est-ce que l'effondrement des marges en CSS ? Et comment l'éviter
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-01-11T18:07:52.000Z'
originalURL: https://freecodecamp.org/news/what-is-margin-collapse-and-how-to-avoid-it
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/domino-g6f10860f9_1280.jpg
tags:
- name: CSS Margins
  slug: css-margins
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que l'effondrement des marges en CSS ? Et comment l'éviter
seo_desc: "What is Margin Collapse?\nMargin collapse occurs when vertically adjacent\
  \ margins of block-level elements collide to share a general margin space. The size\
  \ of this shared space is dictated by the larger number margin. \nYou can visualize\
  \ this as an arm..."
---

## Qu'est-ce que l'effondrement des marges ?

L'effondrement des marges se produit lorsque les marges verticalement adjacentes des éléments de niveau bloc entrent en collision pour partager un espace de marge général. La taille de cet espace partagé est dictée par la marge la plus grande. 

Vous pouvez visualiser cela comme un bras de fer, où la marge la plus grande prendra le dessus et gagnera.

Il est important de clarifier ce que signifie être le plus grand nombre. 

Si une marge de 70px entre en collision avec une marge de 90px, la marge de 90px gagnera. Si une marge de -70px entre en collision avec une marge de -90px, -90px gagnera. 

Bien qu'un nombre négatif soit techniquement une valeur plus petite sur une échelle mathématique qu'un nombre positif, avec l'effondrement des marges, il est utile de se souvenir qu'une valeur numérique plus élevée aura une signification plus élevée. 

L'effondrement est pertinent indépendamment de l'unité de mesure telle que les pixels, rem, em ou les pourcentages. Ces unités peuvent être calculées les unes contre les autres même avec une utilisation mixte.

Dans divers scénarios, cette interaction peut devenir problématique. Par exemple, si vous créez un composant réutilisable qui est censé avoir un espace de marge cohérent autour de lui, indépendamment de son placement. 

Des incohérences peuvent survenir en fonction de l'endroit où ce composant est placé, car la marge peut interagir avec une autre. Heureusement, il existe des précautions que nous pouvons prendre pour éviter cela.

L'effondrement des marges peut causer des comportements inattendus dans votre mise en page. Vous verrez probablement un espacement appliqué qui ne semble pas correspondre à ce que vous attendez. 

Au lieu d'essayer d'augmenter les marges en ajoutant des pixels supplémentaires jusqu'à ce que l'espacement soit correct, vous pouvez apprendre le fonctionnement interne de la propriété de marge afin de reconnaître quand l'effondrement peut se produire. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/margin-collapse-2.png)

### Exemple de code d'effondrement des marges

```html
<div class="one">Élément de niveau bloc Un</div>
<div class="two">Élément de niveau bloc Deux</div>
```

```css
div.one {
    margin-bottom: 30px;
}

div.two {
    margin-top: 100px;
}
```

## Marges négatives

Les valeurs de marge négatives sont également sujettes à l'effondrement des marges. Elles fonctionnent comme les marges positives, où le nombre le plus grand prendra le dessus.   
  
Le résultat d'une marge de -30px et d'une collision de -100px aboutira à un espace de marge de -100px.

### Mélange de marges négatives et positives

Lorsque des marges négatives et positives interagissent, les pixels seront additionnés, s'annulant mutuellement. Voici où quelques calculs entreront en jeu. 

Par exemple, une marge de -30px et une marge de 10px aboutiront à un espace de marge partagé de -20px. Alternativement, une marge de 10px et une marge de -10px aboutiront à aucun espacement de marge (-10 + 10 = 0) ! 

## Comment reconnaître l'effondrement des marges

Il existe différents scénarios où les marges peuvent s'effondrer. Passez en revue les comparaisons ci-dessous pour mieux comprendre quand l'effondrement des marges peut se produire.

### Effondrement des marges

* Les éléments sont de niveau bloc, comme `div` ou `p`
* Les marges verticales s'effondreront
* L'effondrement ne se produira qu'en mode de disposition Flow, qui est le mode de disposition par défaut
* Un élément "invisible" comme un `<br/>` n'arrêtera pas l'effondrement des marges

### Pas d'effondrement des marges

* Les éléments frères horizontaux ne s'effondreront pas
* Pas d'effondrement des marges en Flex, Grid ou en disposition positionnée
* L'effondrement des marges peut s'empiler et créer un effet domino où les frères affectent les uns les autres
* Un élément `<hr/>` entre des frères verticaux peut empêcher l'effondrement

### Comment inspecter vos marges

La fonction Inspecter dans votre navigateur est un excellent outil pour visualiser vos marges, remplissages et autres aspects du modèle de boîte. Cela vous aidera à voir si les marges sont partagées.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/boxmodel.png)
_Le modèle de boîte_

## Comment éviter l'effondrement des marges

Tout d'abord, rappelez-vous que les marges doivent de préférence être utilisées pour augmenter la distance entre les éléments frères, et non pour créer un espacement entre un enfant et un parent. Si vous devez augmenter l'espace dans la disposition Flow, utilisez d'abord le remplissage si possible.

De plus, tenez compte du mode de disposition lors de l'ajout d'une marge. Notez dans quel mode de disposition vous vous trouvez et surveillez l'effondrement des marges chaque fois que vous êtes en mode de disposition Flow normal. 

Pour ajouter de l'espace entre les frères et éviter complètement l'effondrement des marges, envisagez d'utiliser Flexbox ou Grid et d'utiliser leurs fonctionnalités de gap.

Vous pouvez également envisager d'utiliser une bibliothèque de composants alignée sur les directives d'espacement d'un système de conception particulier. Ou vous pouvez utiliser une bibliothèque open-source qui a déjà résolu les problèmes d'effondrement des marges. Vous pouvez également mettre en place un système de conception pour votre équipe où vous pouvez utiliser des marges et des remplissages cohérents dans toute votre interface utilisateur. 

Enfin, essayez de développer un sens pour savoir quand l'effondrement des marges se produit. Maintenant que vous êtes plus conscient de ce comportement, vous commencerez à le remarquer plus fréquemment. 

Utilisez vos outils d'inspection de navigateur fiables lorsque votre radar d'effondrement des marges est activé. Si vous le trouvez, supprimez-le pour éviter une réutilisation répétée du style, car il pourrait être réutilisé et causer des problèmes à l'avenir.

### Ressources sur l'effondrement des marges

Si vous souhaitez approfondir l'effondrement des marges, je vous recommande vivement de lire [The Rules of Margin Collapse](https://www.joshwcomeau.com/css/rules-of-margin-collapse/) par Josh W. Comeau. 

Je recommande également son cours complet [CSS for JavaScript Developers](https://css-for-js.dev/) si vous souhaitez combler les lacunes dans vos connaissances CSS et en apprendre davantage sur des sujets comme celui-ci.

## Résumé

L'effondrement des marges peut être un comportement CSS que vous avez déjà rencontré et pour lequel vous n'aviez pas encore de définition, ou vous n'aviez peut-être pas tous les outils disponibles pour l'éviter. 

Cet aspect délicat de la propriété de marge peut souvent passer inaperçu et causer des ravages à travers des comportements attendus. Comprendre ces effets peut aider à améliorer votre interface utilisateur et à réduire le nombre de bugs dans votre CSS.

Bon codage !