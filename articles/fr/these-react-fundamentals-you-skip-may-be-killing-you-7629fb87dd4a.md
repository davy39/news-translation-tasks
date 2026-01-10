---
title: Ces fondamentaux de React que vous ignorez pourraient vous nuire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-05T19:03:56.000Z'
originalURL: https://freecodecamp.org/news/these-react-fundamentals-you-skip-may-be-killing-you-7629fb87dd4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sVjlf2VlXRhi6zglSUyVoQ.png
tags:
- name: Apps
  slug: apps-tag
- name: development
  slug: development
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Ces fondamentaux de React que vous ignorez pourraient vous nuire
seo_desc: 'By Emmanuel Ohans

  Often times, the inability to debug a certain error stems from not understanding
  some foundational concept.

  You can say the same thing if you don’t understand some more advanced concepts because
  you lack the knowledge of certain fun...'
---

Par Emmanuel Ohans

Souvent, l'incapacité à déboguer une certaine erreur provient du fait de ne pas comprendre certains concepts fondamentaux.

On peut dire la même chose si vous ne comprenez pas certains concepts plus avancés parce qu'il vous manque la connaissance de certains fondamentaux.

Dans cet article, je souhaite expliquer ce que je considère comme certains des concepts fondamentaux les plus importants de React que vous devez comprendre.

Ces concepts ne sont pas particulièrement techniques. Il existe de nombreux autres articles qui couvrent ces sujets — des choses comme `props`, `state`, `context`, `setState`, et ainsi de suite.

Cependant, dans cet article, je me concentrerai sur certaines connaissances plus conceptuelles qui forment la base de la plupart des choses techniques que vous ferez dans React.

Prêt ?

### Comment React fonctionne sous le capot

L'une des premières choses que tout le monde apprend dans React est comment construire des composants. Je suis presque sûr que vous l'avez appris aussi.

Par exemple :

```
// composant fonctionnel
function MyComponent() {
  return <div> Mon Composant Fonctionnel </div>
}

// composant basé sur une classe
class MyComponent extends React.Component {
  render() {
    return <div> Mon Composant de Classe </div>
  }
}
```

La plupart des composants que vous écrivez retourneront certains éléments :

```
function MyComponent() {
  return <span> Mon Composant Fonctionnel </span> // élément span
}

class MyComponent extends React.Component {
  render() {
    return <div> Mon Composant de Classe </div> // élément div
  }
}
```

Sous le capot, la plupart des composants retournent un arbre d'éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/tQn1uuZsujd4JU-cIxVrjn8-3Giy1CRAqjCD)
_Les composants, lorsqu'ils sont évalués en interne, retournent souvent un arbre d'éléments._

Maintenant, vous devez également vous souvenir que les composants sont comme des fonctions qui retournent des valeurs basées sur leurs valeurs `props` et `state`.

![Image](https://cdn-media-1.freecodecamp.org/images/7NCegDIGXAs8OGYEP733SK7L-uOpMI4vZwSR)
_Les composants sont comme des fonctions avec des paramètres "props" et "state"._

Par conséquent, chaque fois que les valeurs `props` ou `state` d'un composant changent, un nouvel arbre d'éléments est rendu.

![Image](https://cdn-media-1.freecodecamp.org/images/jqur2fLzWkWzsXgcm0bDIVRRJWSfnN0v6DSN)
_Si les valeurs des props ou du state changent, l'arbre d'éléments est ré-rendu. Cela entraîne un nouvel arbre._

Si le composant est un composant basé sur une classe, la fonction `render` est invoquée pour retourner l'arbre d'éléments.

```
class MyComponent extends React.Component {
  render() {
    // cette fonction est invoquée pour retourner l'arbre d'éléments
  }
}
```

Si le composant est un composant fonctionnel, sa valeur de retour produit l'arbre d'éléments.

```
function MyComponent() {
  // la valeur de retour produit l'arbre d'éléments
  return <div>
```

```
  </div>
}
```

Pourquoi est-ce important ?

Considérons un composant, `<MyComponent />` qui prend une prop `name` comme montré ci-dessous :

```
<MyComponent name='Ohans'/>
```

Lorsque ce composant est rendu, un arbre d'éléments est retourné.

![Image](https://cdn-media-1.freecodecamp.org/images/3DsSWux3GMF8nLy8KyWXqaciojsvhKaIcts8)
_Un arbre d'éléments retourné à partir du rendu de &lt;MyComponent /&gt;_

Que se passe-t-il lorsque la valeur de `name` change ?

```
<MyComponent name='Quincy'/>
```

Eh bien, un nouvel arbre d'éléments est retourné !

![Image](https://cdn-media-1.freecodecamp.org/images/OQ1FFA7FNaRpmkrMH43CpbHJCV2opTEBNMqe)
_UN NOUVEL arbre d'éléments retourné à partir du rendu de &lt;MyComponent /&gt; avec des props différentes_

D'accord.

Maintenant, React a en sa possession deux arbres différents — l'ancien et l'arbre d'éléments actuel.

À ce stade, React compare les deux arbres pour trouver ce qui a exactement changé.

![Image](https://cdn-media-1.freecodecamp.org/images/cO44K8IzUSeTPwvnGm5nJwYhfn0AvC5lnyGX)
_Deux arbres différents. Qu'est-ce qui a vraiment changé dans les deux arbres ?_

La plupart du temps, l'arbre entier n'a pas changé. Juste quelques mises à jour ici et là.

Après avoir comparé ces deux arbres d'éléments, le DOM réel est ensuite mis à jour avec le changement dans le nouvel arbre d'éléments.

Facile, non ?

Ce processus de comparaison de deux arbres pour détecter les changements est appelé "réconciliation". C'est un [processus technique](https://reactjs.org/docs/reconciliation.html#motivation), mais cet aperçu conceptuel est idéal pour comprendre ce qui se passe sous le capot.

### React ne met à jour que ce qui est nécessaire. Vrai ?

Lorsque vous commencez avec React, tout le monde vous dit à quel point React est génial — en particulier comment il met à jour uniquement la partie essentielle du DOM qui est mise à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/o83thhmBUVqoiatZw56dEY6yGNMJn5jxemhw)
_D'après la [documentation React](https://reactjs.org/docs/rendering-elements.html#react-only-updates-whats-necessary" rel="noopener" target="_blank" title="): Inspecteur DOM montrant des mises à jour granulaires._

Est-ce complètement vrai ?

Oui, c'est vrai.

Cependant, avant que React ne mette à jour le DOM, rappelez-vous que sous le capot — il a d'abord construit l'arbre d'éléments pour les différents composants et a fait le "diffing" essentiel avant de mettre à jour le DOM. En d'autres termes, il a comparé les changements entre les arbres d'éléments précédents et actuels.

La raison pour laquelle je réitère cela est que, si vous êtes nouveau dans React, vous pourriez être aveugle aux problèmes de performance creusés dans votre application parce que vous pensez que React met simplement à jour le DOM avec ce qui est nécessaire.

Bien que ce soit vrai, les préoccupations de performance dans la plupart des applications React commencent avec le processus avant que le DOM ne soit mis à jour !

### Rendus inutiles vs. Mises à jour visuelles

Quelle que soit leur taille, le rendu d'un arbre d'éléments de composant prend un certain temps (aussi minime soit-il). Le temps de rendu augmente à mesure que l'arbre d'éléments du composant grandit.

L'implication de cela est que dans votre application, vous ne voulez pas que React ré-rende l'arbre d'éléments de votre composant si ce n'est PAS important.

Permettez-moi de vous montrer un exemple rapide.

Considérons une application avec une structure de composants comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/sN9IozHOb0YjHvIPzCleBcjPZsTR8nPNZn3y)
_Une application avec un composant parent A et des composants enfants B, C et D._

Le composant conteneur global, `A`, reçoit une certaine prop. Cependant, la seule raison de cela est de transmettre les props au composant `D`.

![Image](https://cdn-media-1.freecodecamp.org/images/5xX0JPX-o-Gej4yKA3iJ8mv4EQpLEaWkvQgH)
_Le composant parent `A` reçoit certaines props et les transmet au composant enfant D._

Maintenant, chaque fois que la valeur de la prop dans `A` change, tous les éléments enfants de `A` sont ré-rendus pour calculer un nouvel arbre d'éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/74D67kRq4cnFHlKfw86OUkdCO1nMYgT9E-rN)

![Image](https://cdn-media-1.freecodecamp.org/images/iAEokbsFD2IW1AOG7DSnhfRFTp0VztjXf5YA)
_Lorsque le composant parent reçoit de nouvelles Props, chaque élément enfant est ré-rendu et un nouvel arbre est retourné._

Par implication, les composants `B` et `C` sont également ré-rendus même s'ils n'ont pas changé du tout ! Ils n'ont pas reçu de nouvelles props !

Ce ré-rendu inutile est ce que l'on appelle un rendu "inutile".

Dans cet exemple, `B` et `C` n'ont pas besoin d'être ré-rendus, mais React ne le sait pas.

Il existe de nombreuses façons de traiter ce problème, et j'en parle dans mon récent article, [Comment Éliminer les Problèmes de Performance de React](https://medium.com/@ohansemmanuel/how-to-eliminate-react-performance-issues-a16a250c0f27).

En continuant, considérons l'application ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/eSvpbb0SILVtzIf8G7peS9DfJOK2gS1bIc1s)
_Cardey en Action :)_

J'appelle cette application [Cardey](http://cardie-performace.surge.sh/).

Lorsque je clique sur le bouton pour changer la profession de l'utilisateur, je peux choisir de mettre en évidence les mises à jour du DOM comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/QnX-5eQrP7GkCVyxl5Xkfu78uhxN-9JhJMMJ)
_Activer les mises à jour visuelles (Paint Flashing) via Chrome Devtools_

Et maintenant je vois ce qui a été mis à jour dans le DOM.

Ceci est une représentation des mises à jour visuelles du DOM. Notez le flash vert autour du texte "Je suis bibliothécaire".

C'est bien, mais je suis préoccupé par le rendu initial des composants de React.

Donc, je pourrais choisir de vérifier cela aussi.

![Image](https://cdn-media-1.freecodecamp.org/images/xDeyGJE6fL42FrSmU15nm5she0xfO6mtC42G)
_Activer le basculement de mise en évidence des mises à jour dans React Devtools_

En faisant cela, je vois quels composants sont réellement ré-rendus lorsque je clique sur ce bouton.

![Image](https://cdn-media-1.freecodecamp.org/images/zduYcMxUoMrKLzHbLABBf3d2zkVa0gkv9Stc)
_Notez le flash vert autour de la carte utilisateur._

Voyez-vous comment les mises à jour visuelles du DOM et les mises à jour de rendu de React sont différentes ?

La grande carte utilisateur a été ré-rendue mais seule la petite région de texte a été mise à jour.

C'est important.

### Conclusion

Je crois que vous avez maintenant une compréhension plus intuitive de ce qui se passe sous le capot dans vos composants React.

En fait, beaucoup plus de choses se passent que ce que j'ai discuté ici. Cependant, c'est un bon début.

Allez construire de grandes applications !

Apprenez-vous React/Redux en ce moment ? Si oui, j'ai une série de livres vraiment excellente sur [Redux](https://thereduxjsbooks.com). Certains disent que c'est [l'un des meilleurs](https://twitter.com/Kaafu4u/status/1041495744803491840) livres techniques qu'ils [aient jamais lus](https://twitter.com/LedZeck/status/1044888661664378880) !