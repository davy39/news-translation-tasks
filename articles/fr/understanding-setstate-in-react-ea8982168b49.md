---
title: Une introduction rapide à setState dans React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T04:04:07.000Z'
originalURL: https://freecodecamp.org/news/understanding-setstate-in-react-ea8982168b49
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OhUk2Ct_kQ78DO1M.
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction rapide à setState dans React.js
seo_desc: 'By Rajesh Pillai

  How to use setState effectively and what pitfalls to avoid


  State management shouldn’t be like solving Rubik Cube :)

  TL;DR — In case you are a visual learner, head over to the video I made: ReactJS
  — How setState works

  Or watch it he...'
---

Par Rajesh Pillai

#### Comment utiliser setState efficacement et quels pièges éviter

![Image](https://cdn-media-1.freecodecamp.org/images/0*OhUk2Ct_kQ78DO1M.)
_La gestion d'état ne devrait pas être comme résoudre un Rubik's Cube :)_

**TL;DR** — Si vous êtes un apprenant visuel, regardez la vidéo que j'ai faite : [ReactJS — Comment setState fonctionne](https://www.youtube.com/watch?v=hwvnCnQ1mRg)

Ou regardez-la ici :

### Une introduction à setState

La première chose à savoir est que la fonction setState dans React fonctionne de manière asynchrone. Cela peut surprendre certains développeurs, car les valeurs d'état ne sont pas immédiatement disponibles après la mise à jour.

Il existe deux variations de l'utilisation de setState : l'approche basée sur les objets et l'approche fonctionnelle.

Voyons les deux en action. Nous comprendrons le problème avec setState basé sur les objets dans le processus.

Créons une application simple.

```
class App extends React.Component {   constructor() {     super();     this.state = {       value: 0,       message: 'état de clic par défaut'     }   }     onClick = () => {     this.setState({       value: this.state.value + 1     });          this.setState({       message: `état-de-clic ${this.state.value}`     });   }         render(){     return(        <div>         <div>render->state={this.state.value} -              {this.state.message}         </div>         <button onClick={this.onClick}>Click-setState</button>               </div>     );   }}
```

Maintenant, nous allons monter cette application sur notre nœud DOM racine.

```
ReactDOM.render(  <App />,   document.getElementById("root"));
```

Le code ci-dessus, lorsqu'il est exécuté, rend la valeur et le message de l'objet d'état et rend également un bouton.

Si vous regardez le gestionnaire de clic, nous avons deux fonctions setState consécutives qui accèdent à la valeur this.state.

Le comportement que nous attendons est que, lorsque le bouton est cliqué, la valeur d'état correcte doit être rendue dans la div ci-dessous (extraite pour référence) :

```
<div>render->state={this.state.value} -      {this.state.message}</div>
```

Le `this.state.message` contient des valeurs de `this.state.value`

Nous nous attendons à ce que les deux valeurs d'état soient les mêmes lorsque le bouton est cliqué.

Voyons le résultat de cela.

La sortie initiale est montrée ci-dessous, car la valeur est 0 au départ.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XJSgTpbY1uJmdKJDWYxHKQ.png)

Après le premier clic, nous attendons la sortie suivante :

```
render->state=1 -état-de-clic 1
```

mais nous obtenons cela à la place :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gwTie8l4onwKgloeOCXItA.png)
_inadéquation dans la valeur de l'état_

Au deuxième clic, la sortie est toujours inadéquate comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WPzoGxDaOgd91EEnNwPH-Q.png)

À ce stade, vous pourriez être en train de somnoler ou de vous gratter la tête :)

![Image](https://cdn-media-1.freecodecamp.org/images/0*finEoFAqAty_kvoo.)
_Photo par [Unsplash](https://unsplash.com/@jackmanchiu?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jackman Chiu</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### La fonction onClick()

Alors, examinons la fonction onClick() pour comprendre le problème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GHPR2qbIGr-EoWoxg5Jo4w.png)

Puisque l'appel à setState est asynchrone avant que la première exécution de setState ne soit terminée, la référence au deuxième setState peut pointer vers la valeur précédente et non vers la première valeur mise à jour.

Nous allons corriger cela en utilisant l'aspect fonctionnel de setState.

Pour démontrer la correction, créons un autre bouton :

```
<button onClick={this.onClickfn}>Click-setState fn</button>
```

Et ajoutons un nouveau gestionnaire de clic onClickfn() comme montré ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/1*crfPkk3iZn0LWjQ48cyaMA.png)
_setState(fn)_

La méthode ci-dessus utilise le paramètre fonctionnel dans setState.

Cela peut être une fonction fléchée comme montré ci-dessus ou la fonction ES5 normale.

Cette fonction prend deux paramètres comme arguments : le premier est le prevState, et le second est les props (au cas où vous auriez besoin des props, qui sont passés depuis le composant parent). Ici, nous ne regardons que le prevState.

Le prevState ci-dessus se rapporte à la fonction setState car c'est le dernier état mis à jour. Cela pointera toujours vers la valeur correcte.

Voyons la sortie après quelques clics. Vous trouverez que les valeurs sont toujours synchronisées lorsque vous cliquez sur le deuxième bouton.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JJxtwtGrlULXMplQVL643A.png)

Dans l'exemple ci-dessus, vous pouvez voir que l'utilisation du paramètre fonctionnel setState regroupe correctement l'état précédent, et vous obtenez des valeurs d'état prévisibles.

Un autre piège dont nous devons être conscients : setState() prend une autre fonction de rappel, qui est exécutée une fois que les valeurs d'état sont mises à jour avec succès.

Cela est très pratique dans une situation où vous devez effectuer une opération une fois que setState a mis à jour avec succès.

Voyons un dernier exemple.

Supposons que nous voulons journaliser la valeur de l'état après la mise à jour, et nous écrivons le code comme ci-dessous. J'utiliserai le gestionnaire onClickfn() pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UyMTLi70kI2pMzpQKq8qAQ.png)

Mais regardons le `console.log` et vérifions si la valeur est correcte ou non. Après trois clics, vous obtenez ce statut :

![Image](https://cdn-media-1.freecodecamp.org/images/1*91u86QfsxY6Kx5HmNWbf2A.png)

Vous observerez que la valeur journalisée n'est pas la dernière valeur mise à jour. Corrigons cela et voyons la sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-RUif3etCRJuK6oeoCj3JA.png)

Dans l'exemple ci-dessus, nous utilisons le deuxième paramètre de rappel de setState(). Ce rappel sera exécuté une fois que setState() aura terminé son opération.

Voyons la sortie finale avec le code modifié ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P48JwStPYtR_fZiOxSF0Dg.png)

### Conclusion

J'espère que cet article clarifie certaines idées fausses sur setState.

Le code source complet est disponible sur [jsbin](http://jsbin.com/mekiwog/1/edit).

Bon codage !

Apprenez avec moi @Learner + Fullstack Coach (@rajeshpillai) : [https://twitter.com/rajeshpillai](https://twitter.com/rajeshpillai)

Promotion : Coupon spécial de 10 $ pour les lecteurs de medium pour mon prochain cours en direct [ReactJS-Beyond the basics](https://www.udemy.com/reactjs-beyond-the-basics/?couponCode=MEDIUM_500) sur udemy au cas où vous souhaiteriez soutenir notre programme open source [Mastering frontend engineering in 12 to 20 weeks](https://codeburst.io/mastering-front-end-engineering-in-12-to-20-weeks-for-beginners-and-experienced-alike-6dc5172e3295)