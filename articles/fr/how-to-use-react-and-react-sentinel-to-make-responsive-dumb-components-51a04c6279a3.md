---
title: Comment utiliser React et React-Sentinel pour créer des composants réactifs
  et simples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T20:34:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-and-react-sentinel-to-make-responsive-dumb-components-51a04c6279a3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-M7kIz-f-VmOfAy6.
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment utiliser React et React-Sentinel pour créer des composants réactifs
  et simples
seo_desc: 'By Ryan Yurkanin

  tldr; Media Queries aren’t always enough. Element Queries are amazing, and you can
  black box them with a combination of render props, and something observing your
  element!

  Dealing with Media Queries

  If you’ve had to recreate a Respon...'
---

Par Ryan Yurkanin

**tldr; Les Media Queries ne suffisent pas toujours. Les Element Queries sont incroyables, et vous pouvez les encapsuler avec une combinaison de render props et quelque chose qui observe votre élément !**

#### Gérer les Media Queries

Si vous avez dû recréer un Responsive Design, alors vous savez à quel point les [Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries) sont géniales — mais problématiques.

Les Media Queries permettent d'appliquer du CSS uniquement lorsque la taille change par rapport à la fenêtre d'affichage.

Malheureusement, si vous souhaitez créer un composant de carte réutilisable et réactif, les Media Queries sont moins qu'idéal :

1. Vous devez déterminer la relation entre la hauteur et la largeur de la carte réactive et la hauteur et la largeur de la fenêtre d'affichage.
2. Si votre carte se trouve dans une mise en page plus complexe (comme une mise en page flex), vous devez déterminer comment la taille de la fenêtre modifiera la mise en page flex, puis comment cela affectera la carte. ?
3. Il pourrait y avoir du JavaScript qui bascule une condition qui modifie programmatiquement la taille de la carte, vous devriez donc également en tenir compte et le communiquer aux feuilles de style.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vIDJ7ghnI_MUu0kfVUD9DA.gif)
_20
6 et maintenant nous sommes dans l'enfer de CSS calc(). ?_

À ce stade, je me suis demandé pourquoi je m'étais lancé dans le développement en premier lieu.

Tout ce que je voulais, c'était un moyen de styliser la carte en fonction de la hauteur et de la largeur de cet élément. [Beaucoup de gens veulent avoir cette capacité](https://discourse.wicg.io/t/element-queries/26/33). Une proposition est les Element Queries, et [il existe quelques moyens de les avoir en CSS dès maintenant !](https://elementqueries.com/) ?

Si vous êtes comme moi, vous voulez pouvoir l'intégrer non seulement dans l'écosystème JavaScript, mais aussi dans l'écosystème React. Peut-on créer un conteneur réactif intelligent et encapsulé, et un composant visuel simple ?

**Oui**, nous le pouvons.

#### La solution

La beauté de ce composant est qu'il ne sait pas pourquoi il a la taille qu'il a. C'est à celui qui l'utilise de décider, ce qui signifie que ce composant peut être réutilisé dans plusieurs mises en page. Notre objectif est de **le garder ainsi**, tout en le rendant génial.

Voyons comment nous pouvons faire cela en intégrant `react-sentinel` et en créant un conteneur réactif intelligent avec lui ! ?

Alors, que se passe-t-il **réellement** ici ?

`react-sentinel` fonctionne en prenant une fonction, la prop `observe`, et en l'appelant de manière répétée dans une boucle performante `requestAnimationFrame` ou `requestIdleCallback`.

`requestAnimationFrame` boucle à une vitesse déterminée par le navigateur. Si quelqu'un navigue sur un ancien téléphone, la boucle se produira moins souvent. Cela donne au navigateur un contrôle plus fin et conduit à une expérience plus fluide !

Si vous souhaitez en savoir plus sur `requestAnimationFrame`, je vous suggère de lire [**Gain Motion Superpowers with requestAnimationFrame**](https://medium.com/@bdc/gain-motion-superpowers-with-requestanimationframe-ecc6d5b0d9a4) par Benjamin De Cock ! ?

`Sentinel` prend la valeur de retour de ces fonctions, et si elle est différente de la valeur de retour précédente, la définit comme état local du composant `Sentinel`. Si elle n'est pas différente, alors nous nous arrêtons là et ne mettons pas à jour pour éviter de rerendre constamment ! ?

#### Utilisation des Render Props

Maintenant, à ce stade, vous pourriez vous demander à quoi bon définir l'état local de `Sentinel` ? Comment allons-nous obtenir cela ? ?

Ma méthode préférée pour faire cela est d'utiliser les Render Props.

La plupart savent que vous pouvez passer des enfants à un composant et y accéder en utilisant `this.props.children`, mais vous pouvez aussi passer une fonction !

```
<MightHaveSecrets>  {() => <WantsSecrets />}</MightHaveSecrets>
```

D'accord, c'est une chose. Pourquoi quelqu'un voudrait-il faire cela ? ?

Parce que maintenant, **a des secrets** peut passer ses secrets internes comme argument à cette fonction ! Il n'a aucune idée de la manière dont vous allez réellement utiliser ces secrets, ce qui le rend super encapsulé.

```
<MightHaveSecrets>  {secret => <WantsSecrets emoji={ secret ? ? : ? } />}</MightHaveSecrets>  
```

Tout ce que le composant `<Sentinel` /> se soucie, c'est de sonder infiniment pour se mettre à jour. Les Render Props permettent à n'importe quel morceau d'UI d'interpréter ces mises à jour comme ils le voient. De plus, c'est beaucoup plus évident de savoir d'où viennent ces valeurs. ?

Si vous souhaitez en savoir plus sur les Render Props, je vous suggère de consulter la documentation React ou de lire cet article de la personne [qui m'a d'abord fait découvrir cela !](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce)

Maintenant, nous avons un composant intelligent qui traduit la taille de l'élément en props simples que `<DumbCard` /> peut digérer. Il est super facile de refactoriser et d'échanger des valeurs, et vous n'avez pas à vous soucier de la mise en page dans laquelle il se trouve, ou de ce qui se passe en dehors de sa portée.

#### Conclusion

Imaginez à quel point il aurait été difficile d'écrire du CSS pour une carte que l'utilisateur pourrait redimensionner. Maintenant, nous réagissons à tout ce qui change la taille des éléments.

Le truc cool avec `react-sentinel` est qu'il ne résout pas seulement le problème des element queries. Je l'ai également utilisé pour créer un composant Smart Animation, puisqu'il utilise `requestAnimationframe` sous le capot ?

[Ici](https://github.com/YurkaninRyan/react-sentinel) est l'endroit où vous pouvez consulter le code pour `react-sentinel`, ainsi que quelques solutions alternatives !

Si vous avez des questions, ou des sujets que vous aimeriez voir abordés plus en profondeur, n'hésitez pas à me contacter ! Merci pour la lecture et bon codage ! ?