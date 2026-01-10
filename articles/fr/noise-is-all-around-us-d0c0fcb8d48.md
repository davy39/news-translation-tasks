---
title: Le bruit est partout autour de nous.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-17T17:07:03.000Z'
originalURL: https://freecodecamp.org/news/noise-is-all-around-us-d0c0fcb8d48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*K8x5vECRP6b6_Dc1y8PiqA.jpeg
tags:
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Le bruit est partout autour de nous.
seo_desc: 'By Donavon West

  Noise! Noise! Noise! It’s all around us. That person on the train playing a video
  game on their phone with the sound on with no headphones. The guy who think’s it’s
  perfectly within their right to hold a speakerphone call while in lin...'
---

Par Donavon West

Du bruit ! Du bruit ! Encore du bruit ! Il est partout autour de nous. Cette personne dans le train qui joue à un jeu vidéo sur son téléphone avec le son activé et sans casque. Le gars qui pense qu'il est tout à fait dans son droit de passer un appel en haut-parleur en faisant la queue chez Starbucks. Les sirènes des véhicules de secours et les voitures qui klaxonnent dans les embouteillages (comme si cela allait résoudre quoi que ce soit).

Le bruit peut sembler aussi anodin que quelqu'un qui ne coupe pas le son de son ordinateur portable pendant une réunion — jusqu'à ce que, enfin, tout le monde soit forcé d'entendre les notifications Slack qui arrivent toutes les 3–4 minutes. Voulez-vous être cette personne qui leur demande de mettre leur ordinateur en sourdine ? Ou préférez-vous mordre votre langue et essayer d'ignorer les « cla-clunks » tout en essayant de vous concentrer sur la présentation ?

> bruit /bʁɥi/  
> un son, particulièrement celui qui est fort ou désagréable, ou qui cause un dérangement

Le bruit est un tel problème qu'il a même sa propre journée — la [Journée internationale de sensibilisation au bruit](https://euracoustics.org/INAD2017/AboutNoise.html).

### Le bruit visuel

Mais le bruit ne se limite pas au son. Nos yeux peuvent également être inondés de bruit. Les panneaux d'affichage, la publicité sur les bancs publics et les enseignes de magasin au néon clignotantes contribuent tous au bruit visuel.

De nombreuses villes ont des arrêtés limitant la publicité extérieure et les conceptions architecturales distrayantes. À Scottsdale, en Arizona par exemple, de nombreux bâtiments sont d'une couleur beige clair qui se fond dans l'environnement naturel. Comparez cela avec Times Square à New York. Passez-moi l'aspirine s'il vous plaît !

![Image](https://cdn-media-1.freecodecamp.org/images/nSZrzE16aOvUs0gapJBHWGJRiqgTHUgEEmAo)
_Image : [Wikipedia](https://creativecommons.org/licenses/by-sa/3.0" rel="noopener" target="_blank" title="">CC BY-SA 3.0</a> de <a href="https://en.wikipedia.org/wiki/Times_Square#/media/File:New_york_times_square-terabass.jpg" rel="noopener" target="_blank" title=")_

### Le bruit dans le code

Je sais ce que vous pensez : « Donavon. J'ai commencé à te suivre pour ta vision aiguisée des questions techniques. Y a-t-il un but à tout cela ? » Tout d'abord, « Merci ». Et oui, je suis ravi que vous ayez posé la question !

Le fait est que… Coder peut être assez complexe sans ajouter de bruit superflu, ou ce que j'aime appeler « l'encombrement visuel ».

Regardons quelques exemples.

#### Sections de code répétées

Le code qui est inutilement répété peut être considéré comme de l'encombrement visuel. [Ne vous répétez pas (DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Non seulement l'écriture d'un code DRY réduit les risques d'erreurs, mais c'est aussi plus agréable pour l'œil.

Prenons l'exemple suivant. Regardez tout ce code répété.

```
const Foo = () => (  <div>    <Bar className="fruit medium">      <span>Apple</span>    </Bar>    <Bar className="fruit medium">      <span>Orange</span>    </Bar>    <Bar className="fruit large">      <span>Watermelon</span>    </Bar>    <Bar className="fruit large">      <span>Jack Fruit</span>    </Bar>    </div>);
```

Mais nous pouvons rendre cela DRY proprement en plaçant le code répété dans son propre composant et en le sortant de la vue en le plaçant dans son propre fichier.

```
const Fruit = ({ size, type }) => (  <Bar className={`fruit ${size}`}>    <span>{type}</span>  </Bar>);Fruit.defaultProps = {  size: 'medium',};
```

Maintenant, `Foo` est parfaitement DRY.

```
const Foo = () => (  <div>    <Fruit type="Apple" />    <Fruit type="Orange" />    <Fruit type="Watermelon" size="large" />    <Fruit type="Jack Fruit" size="large" />  </div>);
```

#### Composants fonctionnels sans état React vs composants de classe ES6

Ici, nous avons un composant React traditionnel écrit à l'aide d'une classe ES6.

```
Hello class extends Component {  render() {    return (      <div>Hello {this.name}</div>    );  }}
```

Remarquez qu'il ne conserve aucun état et n'utilise aucun événement de cycle de vie. Pourquoi n'utilisons-nous pas alors un composant fonctionnel sans état (SFC) ?

Voici le même composant écrit sous forme de SFC.

```
const Hello = ({ name }) => (  <div>Hello {name}</div>);
```

Remarquez qu'un SFC n'est au fond que la méthode `render` d'un composant de classe ES6 traditionnel. Comme il ne s'agit pas d'une instance de classe, les `props` référencées n'ont pas besoin d'utiliser `this`. Et comme tout ce que nous faisons est de renvoyer une valeur, nous pouvons utiliser la forme « instruction unique » de la fonction fléchée ES6, ce qui signifie que nous pouvons également éliminer l'instruction `return`.

L'utilisation d'un SFC nous permet de supprimer près de la moitié du code. Mais ne pensez pas qu'il s'agisse d'un concours pour écrire le moins de lignes possible (rendre votre code trop concis peut aussi le rendre trop difficile à comprendre). Il s'agit d'éliminer l'inutile, le code passe-partout (boilerplate), et cela nous permet de nous concentrer simplement sur le problème à résoudre.

> Les SFC aident à réduire le rapport signal sur bruit.

#### Code auto-commenté

Commenter votre code _semble_ être une bonne idée, n'est-ce pas ? Mais beaucoup diraient que les commentaires ne devraient être ajoutés que lorsque vous avez besoin d'expliquer quelque chose qui n'est peut-être pas évident ou pour expliquer le problème. Le code lui-même devrait être écrit de manière à ce qu'il soit auto-commenté.

> Les commentaires devraient être utilisés pour énoncer le problème. Votre code montre la solution.

Prenons l'exemple suivant.

```
// afficher un message si le risque est élevé et que le conducteur a trop d'accidents
if (driver.age < 25 || driver.age > 85 && driver.accidents > 2) {  doSomething();}
```

Pas mal. Nous avons tous l'habitude de lire du code qui ressemble à ça. Mais c'est complexe. Considérons maintenant cet exemple.

```
const { age, accidents } = driver;const isHighRiskAge = age < 25 || age > 85;const hasManyAccidents = accidents > 2;
```

```
if (isHighRiskAge && hasManyAccidents) {  doSomething();}
```

Remarquez que nous n'avons pas éliminé de lignes de code — en fait, la taille du code a **augmenté** — mais la logique est répartie en morceaux digestes que votre cerveau peut évaluer et mettre de côté. Et en utilisant des noms de variables descriptifs (c'est-à-dire `isHighRiskAge` et `hasManyAccidents`), l'instruction `if` est désormais explicite, éliminant ainsi le besoin de commentaire.

Un autre grand avantage de l'élimination des commentaires est d'éviter la confusion. Aujourd'hui, vous écrivez et commentez votre code comme suit.

```
if (age > 75) { // faire quelque chose si plus de 75
```

Demain, vous trouvez un bug et modifiez le code.

```
if (age > 85) { // faire quelque chose si plus de 75
```

Mais avez-vous pensé à mettre à jour le commentaire en conséquence ? Peut-être ? Peut-être pas ? Un autre programmeur lisant ce code dans quelques mois pourrait lire les commentaires et être induit en erreur. Les ordinateurs n'exécutent pas les commentaires.

> Ne commentez pas l'évidence.

#### Petits composants réutilisables

La création de composants plus petits et réutilisables peut également réduire l'encombrement visuel. Prenons l'exemple suivant.

```
const Foo = () => (  <div>    <div      style={{        color: 'red',        width: '200px',        height: '200px'      }}    >Hello World</div>  </div>);
```

Pas mal, mais nous pouvons faire mieux. Et si nous créions un composant `RedBox` qui encapsule le style ?

```
const Foo = () => (  <div>    <RedBox>Hello World</RedBox>  </div>);
```

Les détails sont désormais cachés à la vue. Vous n'avez besoin de regarder son implémentation qu'en cas de problème. Sinon, vous devriez supposer que `RedBox` fait son travail correctement.

Ci-dessous se trouve une implémentation de `RedBox` qui utilise [Styled Components](https://www.styled-components.com/), ce qui permet de réduire encore plus l'encombrement visuel. Si vous ne l'avez jamais utilisé, jetez-y un œil !

```
const RedBox = styled.div`  color: red;  width: 200px;  height: 200px;`;
```

### Conclusion

Éliminer toutes les formes de bruit de votre vie peut faire des merveilles pour votre santé mentale. Promenez-vous dans un parc tranquille, loin du chaos des rues de la ville. Profitez du chant agréable des oiseaux et de la beauté naturelle des arbres. Évitez simplement l'aire de jeux ! 🛝

![Image](https://cdn-media-1.freecodecamp.org/images/kvcMTFHg-XZALxBYFPznzJzu2FlHvuNiHrwy)
_Image : [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:%C3%87ocuk_park%C4%B1.JPG" rel="noopener" target="_blank" title=")_

_J'écris également pour le blog d'ingénierie d'American Express. Découvrez mes autres travaux et ceux de mes talentueux collègues sur [AmericanExpress.io](http://americanexpress.io/). Vous pouvez également me [suivre sur Twitter](https://twitter.com/donavon)._