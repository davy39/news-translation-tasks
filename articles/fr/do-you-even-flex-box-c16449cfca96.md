---
title: Un guide visuel de CSS Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T07:27:53.000Z'
originalURL: https://freecodecamp.org/news/do-you-even-flex-box-c16449cfca96
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qucqUWwkbRPaVF0muyhN-g.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un guide visuel de CSS Flexbox
seo_desc: 'By Zeeshaan Maudarbocus

  What is CSS Flexbox?

  As per the MDN web docs:


  “CSS Flexible Box Layout is a module of CSS that defines a CSS box model optimized
  for user interface design, and the layout of items in one dimension. In the flex
  layout model, t...'
---

Par Zeeshaan Maudarbocus

### **Qu'est-ce que CSS Flexbox ?**

Selon les documents web MDN :

> « *CSS Flexible Box Layout est un module de CSS qui définit un modèle de boîte CSS optimisé pour la conception d'interfaces utilisateur et la disposition des éléments dans une dimension. Dans le modèle de disposition flex, les enfants d'un conteneur flex peuvent être disposés dans n'importe quelle direction et peuvent « flex » leurs tailles, soit en grandissant pour remplir l'espace inutilisé, soit en rétrécissant pour éviter de déborder du parent. L'alignement horizontal et vertical des enfants peut être facilement manipulé.* »

Donc, pour résumer, il s'agit d'un module de disposition qui facilite l'alignement et la distribution de l'espace entre les éléments dans un conteneur.

Jetons un rapide coup d'œil à quelques exemples de ce qui peut être fait avec seulement 1 à 2 lignes de code en utilisant CSS flexbox :

Disposition d'alignement horizontal :

![Image](https://cdn-media-1.freecodecamp.org/images/fNTVn8WpbfBeMCThuUM9WWA55Nclr6T-pWaI)
_display: flex_

Disposition d'alignement vertical :

![Image](https://cdn-media-1.freecodecamp.org/images/1Loex4JPiVH4TjVuSmY7vk4BTZKGv5qu5A4o)
_flex-direction: column_

C'est assez impressionnant étant donné qu'une ou deux lignes de CSS ont suffi pour manipuler la disposition à l'intérieur de chaque conteneur.

### **Les bases**

Les propriétés Flexbox peuvent être catégorisées en 2 types principaux :

1. **Propriétés du conteneur** (flex-direction, flex-wrap, justify-content, align-items, align-content)
2. **Propriétés des éléments flex** (order, flex, flex-grow, flex-shrink, align-self)

#### **Display: flex**

La première propriété n'est pas spécifique à flexbox. Cette propriété est `display` que nous définissons à la valeur : `flex`. Cela est défini sur le conteneur qui contient les éléments que nous voulons manipuler.

Ajoutons quelques visuels pour comprendre comment cela fonctionne :

Si nous avons initialement un conteneur, avec 3 boîtes ( `div` ) à l'intérieur. Voici à quoi elles ressembleront :

![Image](https://cdn-media-1.freecodecamp.org/images/499sbxU5hRDoKXof2IuvBZ86G27WiEKN9O4s)
_Conteneur avec 3 boîtes_

Maintenant, ajoutons `flex` au conteneur :

![Image](https://cdn-media-1.freecodecamp.org/images/drIav4nUAz0hGxqndfN-HJMeVNYN5UUG18Zl)
_`display: flex;`_

Une seule ligne de CSS a changé la disposition d'une direction verticale à une direction horizontale.

#### **Terminologies importantes autour de Flexbox**

![Image](https://cdn-media-1.freecodecamp.org/images/CrFtHTSVIdR7Dqq-03ryhZIlqbX5r86JIJlF)
_terminologies liées à flexbox_

Ces terminologies seront utilisées tout au long de ce guide.

1. **Flex Container** : Cela fait référence au conteneur qui a `display: flex;` défini.
2. **Flex Item** : Ce sont les enfants individuels à l'intérieur du Flex Container.
3. **Axe principal** : Par défaut, il est défini de gauche à droite.
4. **Axe transversal** : Par défaut, il est défini de haut en bas.

Dès que `display: flex` est défini sur un conteneur, ces axes imaginaires vont travailler ensemble pour déterminer comment les éléments flex à l'intérieur du conteneur flex doivent se déplacer et se comporter. Ces deux axes changent de direction chaque fois que nous modifions certaines propriétés de flexbox qui sont discutées ci-dessous.

#### **Flex-direction**

Cette propriété détermine la direction des axes imaginaires. Les axes, à leur tour, déterminent comment les éléments dans le conteneur flex doivent être placés. Elle prend les 4 valeurs suivantes :

1. `row` est la valeur par défaut de l'axe principal qui pointe de gauche à droite. L'axe transversal reste de haut en bas.
2. `row-reverse` inverse la direction de la ligne de droite à gauche. Encore une fois, l'axe transversal reste inchangé.

![Image](https://cdn-media-1.freecodecamp.org/images/FoiNopDUSzaDfmBRdfkipXzknXluXnsHtZyD)
_flex-direction: row-reverse;_

3. `column` change l'axe principal de l'axe horizontal à l'axe vertical. Cela signifie que l'axe principal coule maintenant de haut en bas tandis que l'axe transversal coule de gauche à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/qLRCI9W8q8TpC20lLXOXrCIKROWYsRvV8vMs)
_flex-direction: column;_

4. `column-reverse` est similaire à la valeur column avec la seule différence que l'axe principal coule maintenant de bas en haut.

![Image](https://cdn-media-1.freecodecamp.org/images/TjDPAkqDmogY31pMG-ZCaWEZhYK67ZAP3op0)
_flex-direction: column-reverse;_

#### **Flex-wrap**

Le conteneur flex ne permet pas par défaut aux éléments de prendre plusieurs lignes. Au lieu de cela, tous les éléments seront compressés pour tenir sur une seule ligne, c'est-à-dire qu'il ne permet pas le retour à la ligne sur plusieurs lignes.

1. `flex-wrap: no-wrap` est la valeur par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/uroUYXVBrpQiZipR5c4JVvm5RB9DmdSv4PIg)
_no-wrap. Chaque bloc fait 200px dans un conteneur de 500px_

2. `flex-wrap: wrap`. En changeant cette propriété en `wrap`, nous pouvons maintenant nous assurer que chaque élément flex conservera ses tailles respectives. S'ils ne peuvent pas tenir sur une seule ligne, ils passeront à la ligne suivante ou à la colonne suivante en fonction de la flex-direction.

![Image](https://cdn-media-1.freecodecamp.org/images/JnYxdDQn1qESWUWgfBXbPafTpFNejiNwFp5Y)
_flex-wrap défini sur wrap pour le même cas que ci-dessus_

Si la flex-direction a été définie sur row-reverse, alors les éléments iront sur la ligne suivante en commençant de droite à gauche.

3. `wrap-reverse` d'autre part, enveloppera la ligne suivante des éléments flex au-dessus de la ligne initiale, toujours de gauche à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/Dp-NP6eMN4-xK987GAPEtdsHAOdoMCdIA7Fs)
_Flex-wrap maintenant défini sur wrap-reverse_

#### **Justify-content**

Cette propriété est très souvent utilisée. Son but est de distribuer l'espace entre les éléments flex dans un conteneur flex le long de l'**axe principal**. Sa valeur par défaut est définie sur `flex-start`.

![Image](https://cdn-media-1.freecodecamp.org/images/WQ1EGCmhvH1ectG2APn6G762jmKRJDZGJtOU)
_1. justify-content: flex-start;_

![Image](https://cdn-media-1.freecodecamp.org/images/DH9LFgtyTqM4OfL7AZXzDC8ELiorA0GTKxwl)
_2. justify-content: center;_

![Image](https://cdn-media-1.freecodecamp.org/images/GM1B4g6eE7oIhDjYoFYbhJOQjSNSGKoDZqRH)
_3. justify-content: flex-end;_

![Image](https://cdn-media-1.freecodecamp.org/images/s7dHJo8qtbeNAXJXjIbb9woBGFiMRvqnGw-j)
_4. justify-content: space-between;_

![Image](https://cdn-media-1.freecodecamp.org/images/f9F4uWOsXXq3hj6A5qO2wdL-L6PQUj3NcrCu)
_5. justify-content: space-around;_

**À noter :** Si flex-direction a été défini sur column, alors l'axe principal coulera de haut en bas. Cela signifie que justify-content distribuera maintenant les éléments de manière verticale.

#### **Align-items**

Cette propriété est tout aussi populaire que `justify-content` et est utilisée régulièrement avec flexbox. Elle fait la même chose que `justify-content` avec la seule différence qu'elle fonctionne le long de l'**axe transversal**. La valeur par défaut pour `align-items` est `stretch`.

![Image](https://cdn-media-1.freecodecamp.org/images/D3nBOOnF6moyki-v6PcKY4Cp8IdKTpdUjCh8)
_1. align-items: flex-start;_

![Image](https://cdn-media-1.freecodecamp.org/images/PMNLD87bTT83lTpGQouFZsQEgfor7UAmdNKY)
_2. align-items: center;_

![Image](https://cdn-media-1.freecodecamp.org/images/7KFkc53rzNF86KW9qfGtxAwKyF6EqNN6QCfl)
_3. align-items: flex-end;_

![Image](https://cdn-media-1.freecodecamp.org/images/mUbWmyiritrypgTTExjDjXn34oUrrhmzpt5o)
_4. align-items: baseline;_

![Image](https://cdn-media-1.freecodecamp.org/images/SpErFyFcyHdOHNEpRBLrpuvpwpD81TLWyVxQ)
_5. align-items: stretch;_

**À noter :** Si flex-direction a été défini sur column, alors l'axe transversal coulera de gauche à droite. Cela signifie que align-items distribuera maintenant les éléments de manière horizontale.

#### **Align-content**

Cette propriété est similaire à et peut être facilement confondue avec `align-items`. Le but de cette propriété est de déterminer comment l'espace entre les **lignes** dans un conteneur flex doit être distribué le long de l'**axe transversal**.

Alors que `align-items` cible l'espace entre les éléments flex, `align-content` cible les lignes entre les éléments. La valeur par défaut pour `align-content` est `stretch`.

![Image](https://cdn-media-1.freecodecamp.org/images/pZQxtxQPOFGOo3nPI0PP30dtSV2Kh1JWTvPq)
_1. align-content: stretch;_

![Image](https://cdn-media-1.freecodecamp.org/images/AXH1xvGBA0saPyjQlkhPB2o1SY7aKfZLMm9W)
_2. align-content: flex-start;_

![Image](https://cdn-media-1.freecodecamp.org/images/YVJtoXcCmR-mdR-uwSOhxzeiLEa2n1NH2Nme)
_3. align-content: center;_

![Image](https://cdn-media-1.freecodecamp.org/images/2jTX6X2VKk4hfSDlompfbhWgztGhR6DqKj55)
_4. align-content: flex-end;_

![Image](https://cdn-media-1.freecodecamp.org/images/dw1WSjk4n8X4jzjFdvA1arNDP4QFMuH06RJ3)
_5. align-content: space-between;_

![Image](https://cdn-media-1.freecodecamp.org/images/mjZp6dQV9Oj5SgdEEL1GMVnTbGHwmr7HuOTq)
_6. align-content: space-around;_

#### **Propriétés des éléments Flex**

Il est temps de passer au deuxième type de propriétés flexbox qui nous permet de cibler les éléments individuels à l'intérieur d'un conteneur flex.

#### **Align-self**

Cette propriété vous permet d'aligner un élément flex individuel le long de l'**axe transversal**. Elle remplace l'alignement défini pour le conteneur via `align-items`.

Elle prend également les mêmes propriétés que `align-items` (voir ci-dessus).

![Image](https://cdn-media-1.freecodecamp.org/images/lKmArHZGlbeWX8q3SWuUZeUuZjRRYUEizomC)
_align-items défini sur flex-start sur le conteneur parent_

![Image](https://cdn-media-1.freecodecamp.org/images/31G-EGLQX5w5cl4Xlg1s-iEEr72aVEYDuNLw)
_align-self défini sur flex-end sur la boîte orange_

#### **Order**

Cette propriété nous permet de réorganiser les positions des éléments flex individuels à l'intérieur de leur conteneur flex. Par défaut, tous les éléments ont une valeur de 0 qui leur est assignée.

En assignant une valeur inférieure (-ve) ou supérieure (+ve) via `order` sur les éléments individuels, cet élément spécifique se déplacera pour être positionné selon leurs valeurs.

L'ordre suivra la convention la plus logique, c'est-à-dire -ve, 0, +ve. Le nombre le plus bas ira à l'extrême gauche et le nombre le plus élevé à l'extrême droite, en supposant que tout le reste est défini par défaut. Si certains éléments n'ont pas été assignés de nouvelle valeur, ils restent à 0.

![Image](https://cdn-media-1.freecodecamp.org/images/p5hJHrSBtqC3d5d3-t2auhtwh37l35V0YQoe)
_par défaut — tout a une valeur de 0_

![Image](https://cdn-media-1.freecodecamp.org/images/WlPCp0vPzXCHcLcjgaRXctU1iQT7nC0WT9fd)
_définir order: -1 sur la boîte 4_

![Image](https://cdn-media-1.freecodecamp.org/images/rtghkbKFnM3NgK0pCXXwKrpe9LW7qnTr0YYP)
_définir order: 1 sur la boîte 3_

**Note :** Les boîtes 1, 2, 5 et 6 dans l'exemple ci-dessus sont toutes encore à la valeur par défaut de 0. Pour clarifier, les six boîtes ci-dessus ont les valeurs suivantes : -1, 0, 0, 0, 0, 1.

Si vous voulez placer une boîte devant la boîte numéro 4, alors vous devez définir votre boîte ciblée à un ordre de -2 ou inférieur.

#### **Flex-basis, Flex-grow et Flex-shrink**

Jusqu'à présent, tous les éléments flex étaient de taille égale. Regardons maintenant comment nous pouvons faire en sorte qu'un élément flex spécifique prenne plus d'espace à l'intérieur d'un conteneur flex par rapport aux autres éléments à l'intérieur du même conteneur.

#### **Flex-basis**

Cette propriété spécifie la taille **idéale** d'un élément flex **avant** qu'il ne soit placé dans un conteneur flex. Elle fonctionne de manière similaire à la largeur lors du travail avec des lignes. Elle fonctionne comme la hauteur lors du travail avec des colonnes. Donc, si nous travaillons avec des colonnes et qu'un élément a reçu à la fois une hauteur et un flex-basis, le flex-basis aura la priorité car il s'agit de la hauteur **idéale** qu'un élément flex prendra s'il y a suffisamment d'espace disponible.

Cela dit, s'il n'y a pas assez d'espace et qu'aucune hauteur ou largeur n'est assignée aux éléments, les éléments prendront la hauteur maximale ou la largeur maximale disponible dans le conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/jhEltaPaYIgLk5dDIzeaVAWkZUWyW71l7jQx)
_largeur de 200px et aucun flex-basis défini_

![Image](https://cdn-media-1.freecodecamp.org/images/79Y4saDm3ADVxjuZy7RmUACikbrAbVPPdmId)
_largeur de 200px et flex-basis de 300px. Flex-basis gagne_

![Image](https://cdn-media-1.freecodecamp.org/images/fr6HCB5oC0BCaxf1GZUG638mp-6H4NudU4kZ)
_flex-basis défini à 500px. Les éléments sont plus petits que 500px de large mais prennent tout l'espace du conteneur_

![Image](https://cdn-media-1.freecodecamp.org/images/TC0UiVqY16oOjATjUiDoZAauk3ZBtXFLnzov)
_colonnes, hauteur définie à 50px chacune, aucun flex-basis_

![Image](https://cdn-media-1.freecodecamp.org/images/Kju4X3NJxGMnfKBUAV9tMmZwzufsOjyHX-j4)
_colonnes, hauteur définie à 50px et flex-basis défini à 100px. Flex-basis gagne._

#### **Flex-grow**

Cette propriété détermine comment les éléments flex peuvent grandir afin de remplir l'espace inutilisé dans un conteneur flex.

Si nous assignons un `flex-grow: 1` à toutes les boîtes, elles prendront toutes l'espace restant de manière égale, ce qui est également sa valeur par défaut. Le nombre peut être n'importe quoi, tant qu'ils sont tous le même nombre.

Si nous donnons `flex-grow: 1` à un élément et `flex-grow: 2` à un deuxième, alors le deuxième élément prendra deux fois plus d'espace inutilisé que le premier.

Cela s'applique à la fois aux lignes et aux colonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/nW-U0oAU8JJRaniQ7fAI7X8RlvsIjHxmjFh1)
_largeur définie à 200px, aucun flex-grow_

![Image](https://cdn-media-1.freecodecamp.org/images/arjSqUCpl4KspxFj7ZOYkMliIdniKFuDtocZ)
_flex-grow défini à 1 sur la boîte rouge uniquement_

![Image](https://cdn-media-1.freecodecamp.org/images/M07dCm22-YEm5EpIuPlxnAEXmv9qyGhweEIw)
_flex-grow défini à 1 sur les deux boîtes_

![Image](https://cdn-media-1.freecodecamp.org/images/0FlgJ8zigEsdOUvE-BEEFdyJuQUfjFki6FIt)
_flex-grow défini à 1 sur la boîte rouge et 6 sur la boîte orange._

#### **Flex-shrink**

Cette propriété détermine comment les éléments flex peuvent rétrécir lorsqu'il n'y a **pas** assez d'espace dans un conteneur flex.

La valeur `flex-shrink: 1` est la valeur par défaut, ce qui signifie que tous les éléments rétréciront au même rythme par défaut.

**Note : `flex-shrink: 0;`** signifie que cet élément spécifique ne doit jamais rétrécir.

`flex-shrink: 2;` signifie que cet élément spécifique doit rétrécir plus rapidement que les autres à `flex-shrink: 1;`

![Image](https://cdn-media-1.freecodecamp.org/images/RI3cY04kjXpppx76-Ay8VqRjrtmp-pgxnHGN)
_aucun flex-shrink. largeur des éléments plus grande que le conteneur_

![Image](https://cdn-media-1.freecodecamp.org/images/XB8ZKK8OgUZxvG0XrxjclymxPbQiizei8k4u)
_flex-shrink:2 sur la boîte rouge_

![Image](https://cdn-media-1.freecodecamp.org/images/7yqbRNkF8bidJxgFfkqxPyv5U66aLw8ImY1-)
_flex-shrink: 4 sur la boîte rouge_

#### **Flex**

Il s'agit de la version abrégée de flex-grow, flex-shrink et flex-basis dans cet ordre particulier.

Si vous devez utiliser les trois propriétés ci-dessus, vous pourriez simplement utiliser quelque chose comme ceci :

`flex: 0 2 200px;` où 0 fait référence à flex-grow, 2 fait référence à flex-shrink et 200px fait référence à flex-basis respectivement.

### **Félicitations !**

C'est tout ! Ce sont les ingrédients clés pour devenir un maître de flex. Et comme pour toute autre chose dans la vie et dans le code, la pratique rend parfait. Je recommande vivement de mettre ce guide en pratique pour obtenir une compréhension pratique. Un exemple pourrait être de commencer par quelque chose de petit comme une simple barre de navigation.

Vous pouvez également consulter [le lien vers ma collection Codepen sur flex-box](https://codepen.io/collection/DrwYRr/) que j'ai utilisée pour créer ces flexboxes dans les images ci-dessus et les modifier pour voir comment elles changent.

Merci d'avoir lu ce guide sur flexbox. J'espère qu'il a été utile et informatif. Si vous avez des questions ou si vous souhaitez partager vos réflexions sur ce sujet, n'hésitez pas à me contacter via la section des commentaires ou par email à _maudarbocus.zeeshaan@gmail.com_.

Si vous avez trouvé cette lecture utile, montrez un peu d'amour à cet article en laissant quelques applaudissements, afin que d'autres développeurs puissent également le trouver.

[**ZeeshaanMaudar - Aperçu**](https://github.com/ZeeshaanMaudar)  
[_Code for fun Code for a change Code for social good - ZeeshaanMaudar_github.com](https://github.com/ZeeshaanMaudar)