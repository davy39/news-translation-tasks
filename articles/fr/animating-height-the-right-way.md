---
title: Animer la hauteur - la bonne façon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-18T13:56:16.000Z'
originalURL: https://freecodecamp.org/news/animating-height-the-right-way
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/boards-2040575_1920.jpg
tags: []
seo_title: Animer la hauteur - la bonne façon
seo_desc: 'By Fredrik Strand Oseberg

  Let’s be honest. Animating height can be a huge pain. For me, it’s been a constant
  battle between wanting to have nice animations, and not being willing to pay the
  enormous performance cost associated with animating height. ...'
---

Par Fredrik Strand Oseberg

Soyons honnêtes. Animer la hauteur peut être un vrai casse-tête. Pour moi, cela a toujours été un combat constant entre le désir d'avoir de belles animations et le refus de payer le coût énorme en performance associé à l'animation de la hauteur. Maintenant—c'est terminé.

Tout a commencé lorsque je travaillais sur mon projet parallèle—un générateur de CV où vous pouvez partager des liens vers votre CV qui ne sont actifs que pendant une certaine période.

Je voulais avoir une belle animation pour toutes les sections du CV, et j'ai construit un composant React qui effectuait l'animation. Cependant, j'ai rapidement découvert que ce composant détruisait complètement les performances sur les appareils bas de gamme et dans certains navigateurs. Même mon MacBook Pro haut de gamme avait du mal à maintenir un nombre d'images par seconde fluide pour l'animation.

La raison en est bien sûr que l'animation de la propriété de hauteur en CSS oblige le navigateur à effectuer des opérations de mise en page et de peinture coûteuses à chaque image. Il y a une section fantastique sur les performances de rendu sur [Google Web Fundamentals, je vous suggère de la consulter](https://developers.google.com/web/fundamentals/performance/rendering/).

En bref, chaque fois que vous modifiez une propriété géométrique en CSS, le navigateur doit ajuster et effectuer des calculs sur la manière dont ce changement impacte la mise en page de la page, puis il devra réafficher la page dans une étape appelée peinture.

### Pourquoi devrions-nous nous soucier des performances ?

Il peut être tentant d'ignorer les performances. Ce n'est pas sage, mais cela peut être tentant. D'un point de vue commercial, vous gagnez beaucoup de temps qui peut être consacré à la construction de nouvelles fonctionnalités.

Cependant, les performances peuvent influencer directement votre résultat net. À quoi bon construire beaucoup de fonctionnalités si personne ne les utilise ? Plusieurs études réalisées par Amazon et Google montrent que cela est vrai. Les performances sont directement liées à l'utilisation de l'application et aux revenus.

L'autre aspect des performances est tout aussi important. Nous, en tant que développeurs, avons la responsabilité de nous assurer que le web reste accessible à tous—nous le faisons parce que c'est juste. Parce que l'internet n'est pas seulement pour vous et moi, il est pour tout le monde.

Comme le montre l'excellent article d'Addy Osmani [The Cost of JavaScript in 2018](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4), les appareils bas de gamme prennent significativement plus de temps pour analyser et exécuter JavaScript par rapport à leurs homologues haut de gamme.

Pour éviter de créer une division de classe sur l'internet, nous devons être implacables dans notre quête de performance. Pour moi, cela signifiait être créatif et trouver un autre moyen d'atteindre mes animations sans sacrifier les performances.

### Animer la hauteur de la bonne façon

Si vous ne vous souciez pas du comment et que vous voulez simplement voir un exemple en direct, veuillez consulter les liens ci-dessous pour le site de démonstration, les exemples et un package npm pour React :

* [Site de démonstration utilisant la technique](https://resummy.no)
* [Exemple en direct en vanilla JS](https://codesandbox.io/s/3x2zjl0l7m)
* [Exemple simple en React](https://codesandbox.io/s/983z7n92rw)
* [Package NPM et documentation pour React](https://fredrikoseberg.github.io/react-anim-kit-docs/#/)

La question que je me suis posée était de savoir comment éviter le coût de performance encouru par l'animation de la hauteur. Réponse simple—vous ne pouvez pas.

Au lieu de cela, j'ai dû être créatif avec d'autres [propriétés CSS qui n'entraînent pas ces coûts](https://csstriggers.com/). Notamment les transformations.

Puisque les transformations n'ont aucun moyen d'influencer la hauteur, nous ne pouvons pas simplement appliquer une propriété simple à un élément et en avoir terminé. Nous devons être plus malins que cela.

La méthode que nous utiliserons pour obtenir une animation performante de la hauteur consiste en fait à la simuler avec transform: scaleY. L'animation se fait en plusieurs étapes :

Voici un exemple :

```html
<div class="ah-outercontainer">  
<div class="ah-background" style="${this.getBackgroundStyle()}"></div>
<div class="ah-innercontainer">${this.markup}</div></div>
```

* Tout d'abord, nous devons obtenir la hauteur initiale du conteneur de l'élément. Ensuite, nous définissons la hauteur du conteneur extérieur pour qu'elle soit explicite à cette hauteur. Cela provoquera le débordement de tout contenu changeant au lieu d'étendre son parent.
* À l'intérieur du conteneur extérieur, nous avons une autre div qui est positionnée de manière absolue pour couvrir toute la largeur et la hauteur de la div. C'est notre arrière-plan, et il sera mis à l'échelle une fois que nous aurons basculé la transformation.
* Nous avons également un conteneur intérieur. Le conteneur intérieur contient le balisage et changera sa hauteur en fonction du contenu qu'il contient.
* **Voici l'astuce :** Une fois que nous basculons un événement qui change le balisage, nous prenons la nouvelle hauteur du conteneur intérieur et calculons la quantité dont l'arrière-plan doit être mis à l'échelle pour accommoder la nouvelle hauteur. Ensuite, nous définissons l'arrière-plan pour qu'il soit mis à l'échelle par la nouvelle quantité.
* En JavaScript vanilla, cela signifie quelques astuces avec des rendus doubles. Une fois pour obtenir la hauteur du conteneur intérieur afin de calculer l'échelle. Ensuite, pour appliquer l'échelle à la div d'arrière-plan afin qu'elle effectue la transformation.

[Vous pouvez voir un exemple en direct ici en vanilla JS.](https://codesandbox.io/s/3x2zjl0l7m)

À ce stade, notre arrière-plan a été correctement mis à l'échelle pour créer l'illusion de hauteur. Mais qu'en est-il du contenu environnant ? Puisque nous n'ajustons plus la mise en page, le contenu environnant n'est pas affecté par les changements.

Pour faire bouger le contenu environnant, nous devons ajuster le contenu en utilisant transformY. L'astuce est de prendre la quantité dont le contenu s'est étendu et d'utiliser cela pour déplacer le contenu environnant avec des transformations. Voir l'exemple ci-dessus.

### Animer la hauteur dans React

Comme je l'ai mentionné précédemment, j'ai développé cette méthode en travaillant sur un projet personnel en React. Ce site de démonstration utilise cette méthode exclusivement dans toutes ses animations de "hauteur". [Consultez le site de démonstration ici.](https://resummy.no/)

Après avoir implémenté cela avec succès, j'ai pris le temps d'ajouter ce composant et quelques composants de support à une petite bibliothèque d'animation que j'ai créée en React. Si vous êtes intéressé, vous pouvez trouver les informations pertinentes ici :

* [voir la bibliothèque sur NPM ici](https://www.npmjs.com/package/react-anim-kit)
* [La documentation peut être trouvée ici.](https://fredrikoseberg.github.io/react-anim-kit-docs/#/docs/animateheight)

Les composants les plus importants de cette bibliothèque sont AnimateHeight et AnimateHeightContainer. Examinons-les :

```javascript
// À l'intérieur d'un composant React
// handleAnimateHeight est appelé à l'intérieur de AnimateHeight et reçoit le
// transitionAmount et éventuellement selectedId si vous passez cela comme une prop à // AnimateHeight. Cela signifie que vous pouvez utiliser le transitionAmount pour
// transitionner votre contenu environnant

const handleAnimateHeight = (transitionAmount, selectedId) => {     this.setState({ transitionAmount, selectedId });
};

// Prend une prop style, une prop shouldchange et un callback. shouldChange 
// détermine quand le composant AnimateHeight doit se déclencher, ce qui est 
// chaque fois que la prop change. La même prop est utilisée pour contrôler quel 
// contenu afficher.

<AnimateHeight 
  style={{ backgroundColor: "#f2f2f2" }} 
  shouldChange={this.state.open}   
  callback={this.handleAnimateHeight}
>
  {this.state.open && <Component />}
  {!this.state.open && <AnotherComponent />}
</AnimateHeight>
```

* [Exemple avec déplacement du contenu environnant](https://codesandbox.io/s/jn5rp5jvzy)

Les exemples ci-dessus vous montrent comment utiliser AnimateHeight et déclencher manuellement l'ajustement de votre contenu environnant. Mais que faire si vous avez beaucoup de contenu et ne voulez pas faire ce processus manuellement ? Dans ce cas, vous pouvez utiliser AnimateHeight en conjonction avec AnimateHeightContainer.

Pour utiliser AnimateHeightContainer, vous devez fournir à tous les enfants de niveau supérieur une prop appelée animateHeightId, qui doit également être passée à vos composants AnimateHeight :

```js
// À l'intérieur du composant React
const handleAnimateHeight = (transitionAmount, selectedId) => {     
this.setState({ transitionAmount, selectedId });
};

// AnimateHeight reçoit le transitionAmount et l'id actif de l'AnimateHeight qui a été déclenché. 
<AnimateHeightContainer
  transitionAmount={this.state.transitionAmount}
  selectedId={this.state.selectedId}
>
  <div animateHeightId={1}>
    <AnimateHeight 
      style={{ backgroundColor: "#f2f2f2" }}
      shouldChange={this.state.open}
      callback={this.handleAnimateHeight}
      animateHeightId={1}
    > 
    {this.state.open && <Component />
    {!this.state.open && <AnotherComponent />}
    <AnimateHeight />
          
    // Lorsque AnimateHeight est déclenché par un changement d'état
    // ce contenu bougera parce que l'animateHeightId
    // est supérieur à l'id du composant AnimateHeight ci-dessus
    <div animateHeightId={2}>Je bougerai</div>
    <div animateHeightId={3}>Je bougerai aussi</div>
<AnimateHeightContainer />
```

Comme vous pouvez le voir dans cet exemple, AnimateHeight reçoit les informations dont il a besoin pour ajuster le contenu lorsque le composant AnimateHeight est déclenché par un changement d'état.

Une fois que cela se produit, le composant AnimateHeight déclenchera le callback et définira les propriétés dans l'état. À l'intérieur de AnimateHeight, cela ressemble à quelque chose comme ceci (simplifié) :

```js
// À l'intérieur de AnimateHeight
componentDidUpdate() {
  if (update) {
    doUpdate() 
    callback(transitionAmount, this.props.animateHeightId)
   } 
}

// Équivalent à l'appel de cette fonction : 
const handleAnimateHeight = (transitionAmount, selectedId) => {     
this.setState({ transitionAmount, selectedId });
};

handleAnimateHeight(transitionAmount, this.props.animateHeight)
```

Maintenant, vous avez la quantité en pixels dont le contenu a été transitionné, et l'id du composant AnimateHeight qui a été déclenché. Une fois que vous passez ces valeurs à AnimateHeightContainer, il les prendra et transitionnera les autres composants à l'intérieur de lui-même, à condition que vous ayez configuré des animateHeightIds incrémentiels sur les enfants de niveau supérieur.

Exemples plus avancés :

* [Déplacement du contenu environnant avec AnimateHeightContainer](https://codesandbox.io/s/6zz62yp65w)
* [Exemple d'accordéon](https://codesandbox.io/s/202w3n81q0)

REMARQUE : Si vous utilisez cette méthode pour animer la hauteur et déplacer le contenu environnant, vous devez ajouter la quantité de transition à la hauteur de votre page.

### Conclusion

Vous avez peut-être remarqué dans cet article que nous n'animons pas réellement la hauteur—et l'appeler ainsi est incorrect. Vous avez, bien sûr, absolument raison. Cependant, je crois fermement que ce que nous l'appelons n'a pas d'importance. Ce qui compte, c'est que nous obtenons l'effet souhaité avec le coût le plus faible possible pour les performances.

Bien que je pense avoir trouvé un moyen meilleur que d'animer directement la propriété de hauteur, je ne prétends pas avoir inventé ou autrement pensé à quelque chose qui n'a pas été découvert auparavant. Je ne juge pas non plus. Peut-être que l'animation de la hauteur fonctionne pour vous dans votre scénario—aucun problème.

Tout ce que je veux, c'est permettre et simplifier les effets que nous devons tous faire, mais qui parfois entraînent des coûts difficiles à supporter. À tout le moins, je veux susciter une discussion qui vaut la peine d'être menée. Comment pouvons-nous améliorer l'internet pour tout le monde ?