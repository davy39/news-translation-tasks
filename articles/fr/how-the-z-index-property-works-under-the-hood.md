---
title: Comment la propriété z-index fonctionne en coulisses
subtitle: ''
author: Mahesh Patidar
co_authors: []
series: null
date: '2022-01-14T11:06:00.000Z'
originalURL: https://freecodecamp.org/news/how-the-z-index-property-works-under-the-hood
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/freecodecamp.png
tags:
- name: Web Development
  slug: web-development
seo_title: Comment la propriété z-index fonctionne en coulisses
seo_desc: 'The z-index property might seem simple, but it''s not just about using
  a positive or negative integer.

  There''s a lot more going on under the hood, and some quirks can cause problems
  when you''re working with it.

  In this article, we''re going to dive dee...'
---

La propriété z-index peut sembler simple, mais ce n'est pas seulement une question d'utilisation d'un entier positif ou négatif.

Il se passe beaucoup plus de choses en coulisses, et certains comportements peuvent poser problème lorsque vous travaillez avec elle.

Dans cet article, nous allons plonger profondément dans la propriété z-index et apprendre comment elle fonctionne vraiment.

Alors, prenez une tasse de café ou de thé, et soyez prêt avec un stylo et du papier 😉

z-index contrôle l'ordre de superposition et crée le contexte de superposition. Commençons donc par comprendre ce que signifient ces termes.

## Ordre de superposition

Lorsque le navigateur rend les éléments de votre page web le long de l'axe z, il doit choisir quel élément dessiner en premier sur le canevas.

Et l'ordre de ces éléments est appelé ordre de superposition.

Avant d'aller plus loin et de parler de l'ordre de superposition avec la propriété z-index, comprenons à quoi ressemble la superposition par défaut :

1. les arrière-plans et les bordures de l'élément racine.

2. les éléments de bloc non positionnés (dans l'ordre d'apparition)

3. les éléments flottants non positionnés (dans l'ordre d'apparition)

4. les éléments en ligne (dans l'ordre d'apparition)

5. les éléments positionnés (dans l'ordre d'apparition)

L'arrière-plan et les bordures de l'élément racine représentent le niveau le plus bas de la pile. Les éléments positionnés représentent le niveau le plus élevé de la pile.

> Remarque : un élément positionné est un élément qui est soit relatif, fixe, absolu ou collant – tout sauf statique.

<iframe height="487" style="width:100%" src="https://codepen.io/ali6nx404/embed/gOGdJEY?default-tab=result&theme-id=dark">
  See the Pen <a href="https://codepen.io/ali6nx404/pen/gOGdJEY">
  Untitled</a> by Mahesh Patidar (<a href="https://codepen.io/ali6nx404">@ali6nx404</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Un élément non positionné est en dessous de l'élément en ligne et de l'élément positionné. Si nous modifions le code et ajoutons une position relative dans la deuxième div, elle masquera alors l'élément en ligne.

## Comment fonctionne la propriété z-index

La propriété z-index est utilisée pour modifier l'ordre de superposition par défaut des éléments.

Le z-index peut prendre l'une des 3 valeurs suivantes :

1. **auto** : L'ordre de superposition de l'élément est le même que celui de son élément parent. Il s'agit de la valeur par défaut.

2. **integer** : il peut s'agir d'un nombre positif ou négatif.

3. **inherit** : définit la valeur identique à celle de l'élément parent.

> z-index ne fonctionne qu'avec un élément positionné. (Eh bien, ce n'est pas complètement vrai car il existe également quelques cas particuliers – mais nous en discuterons ci-dessous.)

La valeur z-index positive la plus élevée signifie celle la plus proche de l'utilisateur, et la valeur z-index négative la plus basse signifie celle la plus éloignée de l'utilisateur.

<iframe height="497" style="width:100%" src="https://codepen.io/ali6nx404/embed/GRMXVwd?default-tab=result&theme-id=dark">
  See the Pen <a href="https://codepen.io/ali6nx404/pen/GRMXVwd">
  Negative z-index</a> by Mahesh Patidar (<a href="https://codepen.io/ali6nx404">@ali6nx404</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

L'exemple CodePen ci-dessus a le même code que l'exemple d'ordre de superposition par défaut, mais j'ai simplement modifié une seule ligne dans le code du 3ème élément.

`z-index: -1;`

J'ai ajouté un z-index négatif, donc il masque les éléments positionnés sous l'élément non positionné.

Lorsque nous spécifions le z-index sur l'élément positionné, il crée un contexte de superposition.

La propriété z-index simple devient un peu compliquée avec l'introduction du contexte de superposition.

## Contexte de superposition

Les groupes d'éléments avec un parent commun qui avancent ou reculent ensemble dans l'ordre de superposition constituent ce qu'on appelle un contexte de superposition. (Définition officielle de [w3.org](https://drafts.csswg.org/css2/#propdef-z-index).)

> L'élément racine (HTML) forme le contexte de superposition racine. D'autres contextes de superposition sont générés par tout élément positionné (y compris les éléments positionnés de manière relative) ayant une valeur calculée de 'z-index' autre que 'auto'. Les contextes de superposition ne sont pas nécessairement liés aux blocs conteneurs.

J'espère que cette définition est claire.

La balise HTML forme le contexte de superposition racine et par défaut, tous les éléments appartiennent à ce contexte de superposition.

Mais en utilisant des éléments positionnés et un z-index autre que la valeur "auto", nous pouvons créer un contexte de superposition local. Cet élément est connu comme l'élément racine dans le contexte de superposition local.

Les enfants de l'élément parent appartiennent à ce contexte de superposition local et ils se déplacent ensemble vers l'arrière et vers l'avant dans l'ordre de superposition.

### Pourquoi devons-nous connaître le contexte de superposition

Alors pourquoi devriez-vous apprendre toutes ces choses si vous pouvez simplement utiliser le z-index en donnant des valeurs positives ou négatives ?

Permettez-moi de vous donner un simple problème :

<iframe height="424" style="width:100%" src="https://codepen.io/ali6nx404/embed/gOGBovo?default-tab=result&theme-id=dark">
  See the Pen <a href="https://codepen.io/ali6nx404/pen/gOGBovo">
  stacking context example</a> by Mahesh Patidar (<a href="https://codepen.io/ali6nx404">@ali6nx404</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Nous avons 3 divs avec des valeurs de z-index de 1, 999 et 2. Mais la partie déroutante est la deuxième div qui a une valeur de z-index de 999 (la valeur la plus élevée) – et elle n'est toujours pas capable de venir devant la troisième div.

C'est là que notre compréhension est utile : tout cela arrive à cause du contexte de superposition.

Découvrons pourquoi.

Jetez un coup d'œil au HTML :

```html
   <main>
      <div class="first">1</div>
      <div class="second">999</div>
   </main>
   <div class="third">2</div>
```

Nous avons trois divs avec des noms de classe first, second et third. Les première et deuxième divs sont enveloppées dans la balise main.

Voici le CSS :

```css
.first {
  z-index: 1;
}

.second {
  z-index: 999;
}

.third {
  z-index: 2;
}
```

Vous pouvez voir que la deuxième div a la valeur de z-index la plus élevée. Pourtant, elle n'est pas capable de venir devant la troisième div.

Tout cela se passe à cause de cette ligne de code 👇

```css
main {
  position: relative;
  z-index: 1;
}
```

L'élément main crée un contexte de superposition local et les première et deuxième divs appartiennent au même contexte de superposition local – mais pas la troisième div.

C'est pourquoi la deuxième div est capable de venir devant la première : parce qu'elle a une valeur de z-index de 999 (plus élevée que la première div).

La balise main et la troisième div sont les enfants de l'élément racine, tous deux ayant des valeurs de z-index.

L'élément main a une valeur de z-index de 1 et la troisième a une valeur de z-index de 2. La troisième a la valeur de z-index la plus élevée, c'est pourquoi la troisième div est capable de venir devant la balise main.

J'espère que vous comprenez maintenant comment fonctionne le contexte de superposition et pourquoi vous devez le connaître.

## Comment créer des contextes de superposition

Nous avons vu comment nous pouvons combiner le positionnement (en particulier relatif et absolu) avec le z-index pour créer un contexte de superposition – mais ce n'est pas la seule façon ! En voici quelques autres :

1. utiliser position fixed ou sticky (pas besoin de z-index pour ces valeurs !)

2. Ajouter une valeur de z-index à un enfant dans un conteneur display: flex ou display: grid

3. ajouter une valeur d'opacité inférieure à 1

Ce sont quelques-unes des façons courantes de faire cela, mais vous pouvez consulter la liste complète [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).

Je vous ai dit plus tôt que le z-index ne fonctionne pas seulement avec les éléments positionnés – il existe quelques cas particuliers.

La propriété z-index fonctionne bien avec les enfants des conteneurs grid et flex sans spécifier de positionnement.

Consultez l'exemple et le code ci-dessous :

<iframe height="453" style="width:100%" src="https://codepen.io/ali6nx404/embed/JjrmvNd?default-tab=result&theme-id=dark">
  See the Pen <a href="https://codepen.io/ali6nx404/pen/JjrmvNd">
  z-index with grid</a> by Mahesh Patidar (<a href="https://codepen.io/ali6nx404">@ali6nx404</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Cela fonctionne parce que l'ajout d'une valeur de z-index à un enfant dans un conteneur grid ou flex forme un contexte de superposition.

## Conclusion

Je sais que ces choses sont déroutantes et un peu complexes.

J'espère qu'après avoir lu cet article et pratiqué avec la propriété z-index, vous avez compris comment les choses fonctionnent en coulisses.

Mais si vous êtes toujours confus, vous pouvez me contacter [ici](https://twitter.com/Ali6nX404).