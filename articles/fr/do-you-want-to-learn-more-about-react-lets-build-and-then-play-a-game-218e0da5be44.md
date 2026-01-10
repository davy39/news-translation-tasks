---
title: Voulez-vous en savoir plus sur React ? Construisons — puis jouons — à un jeu.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-17T13:27:48.000Z'
originalURL: https://freecodecamp.org/news/do-you-want-to-learn-more-about-react-lets-build-and-then-play-a-game-218e0da5be44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jju0KT50kJI1xX6c6EJVsw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Voulez-vous en savoir plus sur React ? Construisons — puis jouons — à un
  jeu.
seo_desc: 'By Samer Buna


  Update: This article is now part of my book “React.js Beyond The Basics”.

  Read the updated version of this content and more about React at jscomplete.com/react-beyond-basics.


  When I teach React to beginners, I start by introducing the...'
---

Par Samer Buna

> **Mise à jour :** Cet article fait maintenant partie de mon livre « React.js Beyond The Basics ».

> Lisez la version mise à jour de ce contenu et plus sur React sur [**_jscomplete.com/react-beyond-basics_**](https://jscomplete.com/g/target-sum)_._

Lorsque j'enseigne React aux débutants, je commence par leur présenter l'API React. Ensuite, je leur fais construire un simple jeu de navigateur. Je pense que c'est une bonne stratégie d'introduction, car un jeu simple a généralement un état réduit et, dans la plupart des cas, aucune dépendance de données. Les apprenants peuvent se concentrer entièrement sur l'API React elle-même. Le tutoriel officiel React est un simple [jeu de Tic-Tac-Toe](https://reactjs.org/tutorial/tutorial.html#getting-started), qui est un excellent choix.

Construire des applications de jeux simples est bien mieux que construire des applications abstraites (et des applications de liste de tâches) à tant de niveaux. J'ai toujours été contre l'utilisation d'exemples de types abstraits foo-bar, car ils manquent de contexte et d'engagement.

Les apprenants doivent aimer ce qu'ils construisent. Ils doivent accomplir quelque chose à la fin de chaque phase de leur parcours d'apprentissage. Ils doivent prendre des décisions de conception et voir des progrès sur des fonctionnalitésqu'ils peuvent comprendre.

**Veuillez noter** que cet article n'est pas un tutoriel pour débutants. Je vais supposer que vous connaissez les bases de React. Si vous êtes absolument nouveau dans React, commencez par [écrire votre premier composant React](https://medium.freecodecamp.org/how-to-write-your-first-react-js-component-d728d759cabc) et ensuite [apprendre les concepts fondamentaux de React](https://medium.freecodecamp.org/all-the-fundamental-react-js-concepts-jammed-into-this-single-medium-article-c83f9b53eac2).

![Image](https://cdn-media-1.freecodecamp.org/images/1*jju0KT50kJI1xX6c6EJVsw.png)
_Le jeu Target Sum : Choisissez l'ensemble de nombres défis qui s'additionnent à la cible 42 en 10 secondes_

J'ai nommé le jeu que nous allons construire dans cet article **The Target Sum**. C'est un jeu simple : vous commencez avec un nombre aléatoire dans l'en-tête, **la cible** (42 dans la capture d'écran ci-dessus), et une liste de nombres aléatoires **challenge numbers** en dessous de cette cible (les six nombres dans la capture d'écran ci-dessus).

Quatre des six nombres aléatoires utilisés ci-dessus (8, 5, 13, 16) s'additionnent exactement à la somme cible de 42. Choisir le sous-ensemble correct de nombres est la façon de gagner le jeu.

Vous voulez jouer quelques rounds ? Cliquez sur le bouton **Start** ci-dessous :

Avez-vous réussi à gagner ? Je suis tellement mauvais à ce jeu.

Maintenant que vous savez ce que nous allons construire, plongeons directement. Ne vous inquiétez pas — nous allons construire ce jeu par petites étapes, une à la fois.

#### Étape #1 : balisage initial et styles

Il est bon de commencer par tout balisage et styles connus pour les mettre de côté. Avec des jeux simples comme celui-ci, c'est généralement une tâche facile. Il suffit de mettre du contenu statique fictif là où le contenu dynamique sera éventuellement.

Pour garder cet article aussi court que possible et axé sur React, je vais commencer avec un balisage et un CSS prêts à l'emploi. Voici une session de code jsComplete que vous pouvez utiliser pour commencer : [jsdrops.com/rg-0](https://jsdrops.com/rg-0)

Si vous souhaitez suivre avec un environnement de développement différent, voici tout le CSS que j'ai utilisé pour styliser le balisage ci-dessus :

```
.game {  display: inline-flex; flex-direction: column;  align-items: center; width: 100%;}.target {  border: thin solid #999; width: 40%; height: 75px;  font-size: 45px; text-align: center; display: inline-block;  background-color: #ccc;}.challenge-numbers {  width: 85%; margin: 1rem auto;}.number {  border: thin solid lightgray; background-color: #eee;  width: 40%; text-align: center; font-size: 36px;  border-radius: 5px; margin: 1rem 5%; display: inline-block;}.footer {  display: flex; width: 90%; justify-content: space-between;  }.timer-value { color: darkgreen; font-size: 2rem; }
```

Je ne suis pas très bon avec CSS, et certains de mes choix ci-dessus sont probablement discutables. Ne vous laissez pas distraire par cela. Nous avons un jeu à construire.

#### Étape #2 : extraction des composants

Une fois que nous avons atteint un bon état pour le balisage initial et les styles, il est naturel de penser aux composants comme prochaine étape. Il y a de nombreuses raisons d'extraire une partie du code dans un composant. Pour cet exemple, je voudrais me concentrer sur une seule raison : **Comportement partagé**.

Un bon indicateur que vous avez besoin d'un nouveau composant est lorsque plusieurs éléments vont partager exactement le même comportement. Dans notre exemple, vous pouvez cliquer sur l'un des six nombres aléatoires de défi pour les additionner vers le nombre cible. Ces clics déclencheront des changements d'UI. Ce comportement partagé signifie que nous devons créer un composant pour représenter un seul nombre. Je vais simplement l'appeler `Number`.

Les nouveaux changements introduits dans chaque extrait de code ci-dessous sont mis en évidence en **gras**.

```
// Étape #2
```

```
class Number extends React.Component {  render() {    return <div className="number">{this.props.value}</div>;  }}
```

```
class Game extends React.Component {  render() {    return (      <div className="game">        <div className="target">42</div>        <div className="challenge-numbers">          <Number value={8} />          <Number value={5} />          <Number value={12} />          <Number value={13} />          <Number value={5} />          <Number value={16} />        </div>        <div className="footer">          <div className="timer-value">10</div>          <button>Start</button>        </div>      </div>    );  }}
```

```
ReactDOM.render(<Game />, document.getElementById('mountNode'));
```

Vous pourriez vouloir extraire plus de composants comme un composant `Target` ou `Timer`. Bien que l'ajout de composants comme ceux-ci pourrait améliorer la lisibilité du code, je vais garder l'exemple simple et utiliser seulement deux composants : `Game` et `Number`.

#### Étape #3 : rendre les choses dynamiques

Chaque fois que nous rendons un nouveau jeu, nous devons créer un nouveau nombre cible aléatoire. C'est facile. Nous pouvons utiliser `Math.random()` pour obtenir un nombre aléatoire dans la plage `min...max` en utilisant cette fonction :

```
// Fonction de niveau supérieur
```

```
const randomNumberBetween = (min, max) =>  Math.floor(Math.random() * (max - min + 1)) + min;
```

Si nous avons besoin d'un nombre cible entre `30` et `50`, nous pouvons simplement utiliser `randomNumberBetween(30, 50)`.

Ensuite, nous devons générer les six nombres aléatoires de défi. Je vais exclure le nombre `1` de ces nombres et probablement ne pas aller au-dessus de `9` pour le premier niveau. Cela nous permet de simplement utiliser `randomNumberBetween(2, 9)` dans une boucle pour générer tous les nombres de défi. Facile, non ? NON ?

Cet ensemble de nombres aléatoires de défi doit avoir un sous-ensemble qui s'additionne réellement au nombre cible aléatoire que nous avons généré. Nous ne pouvons pas simplement choisir n'importe quel nombre aléatoire. Nous devons désigner les **facteurs** du nombre cible (avec certains de leurs résultats de factorisation), et ensuite quelques autres nombres aléatoires distracteurs. C'est difficile !

Si vous faisiez ce défi dans un entretien de codage, ce que vous faites ensuite pourrait faire ou défaire l'offre d'emploi. Ce que vous devez faire est simplement vous demander : y a-t-il une manière plus facile ?

Prenez une minute et réfléchissez à ce problème particulier. Pour rendre les choses intéressantes, faisons en sorte que la taille de la liste des nombres de défi soit dynamique. Le composant `Game` recevra deux nouvelles propriétés :

```
<Game challengeSize={6} challengeRange={[2, 9]} />
```

L'alternative simple au problème de factorisation ci-dessus est de choisir les nombres de défi aléatoires **en premier**, puis de calculer la cible à partir d'un sous-ensemble aléatoire de ces nombres de défi.

C'est plus facile. Nous pouvons utiliser `Array.from` pour créer un tableau de nombres aléatoires avec l'aide de la fonction `randomNumberBetween`. Nous pouvons ensuite utiliser la méthode `sampleSize` de lodash pour choisir un sous-ensemble aléatoire, puis simplement additionner ce sous-ensemble et l'appeler une cible.

Puisque aucun de ces nombres ne va changer pendant une seule session de jeu, nous pouvons les définir en toute sécurité comme propriétés d'instance.

Voici les modifications dont nous avons besoin pour l'instant :

```
// Dans la classe Game
```

```
  challengeNumbers = Array    .from({ length: this.props.challengeSize })    .map(() => randomNumberBetween(...this.props.challengeRange));
```

```
  target = _.sampleSize(    this.challengeNumbers,    this.props.challengeSize - 2  ).reduce((acc, curr) => acc + curr, 0);
```

```
  render() {    return (      <div className="game">        <div className="target">{this.target}</div>                <div className="challenge-numbers">         {this.challengeNumbers.map((value, index) =>           <Number key={index} value={value} />          )}        </div>        <div className="footer">          <div className="timer-value">10</div>          <button>Start</button>        </div>      </div>    )  }
```

Remarquez comment j'ai utilisé la valeur `index` de l'appel `map` comme `key` pour chaque composant `Number`. Souvenez-vous que cela est acceptable tant que nous ne supprimons pas, n'éditons pas ou ne réorganisons pas la liste de nombres (ce que nous ne ferons pas ici).

Vous pouvez voir le code complet que nous avons pour l'instant [ici](https://jscomplete.com/repl/?j=S10iws71M).

#### Étape #4 : décider ce qui va sur le state

Lorsque le bouton **Start** est cliqué, le jeu passera à un état différent et le compte à rebours du timer de `10` secondes commencera. Puisque ce sont des changements d'UI, un statut de jeu et la valeur actuelle de ce timer à tout moment doivent être placés sur le state.

Lorsque le jeu est en mode `playing`, le joueur peut commencer à cliquer sur les nombres de défi. Chaque clic déclenchera un changement d'UI. Lorsqu'un nombre est sélectionné, nous avons besoin que l'UI le représente différemment. Cela signifie que nous devons également placer les nombres sélectionnés sur le state. Nous pouvons simplement utiliser un tableau pour ceux-ci.

Cependant, nous ne pouvons pas utiliser les **valeurs** des nombres dans ce nouveau tableau, car la liste des nombres de défi aléatoires peut contenir des valeurs répétées. Nous devons désigner les **IDs** uniques de ces nombres comme sélectionnés. Nous avons utilisé un **index** positionnel de nombre comme son ID, donc nous pouvons utiliser cela pour sélectionner de manière unique un nombre.

Tous ces éléments d'état identifiés peuvent être définis sur le state du composant `Game`. Le composant `Number` n'a pas besoin de state.

Voici ce que nous devons placer sur le state du composant `Game` pour l'instant :

```
// Dans le composant Game
```

```
state = {  gameStatus: 'new' // new, playing, won, lost  remainingSeconds: this.props.initialSeconds,  selectedIds: [],};
```

Remarquez comment j'ai rendu la valeur initiale pour le nombre de `remainingSeconds` personnalisable également. J'ai utilisé une nouvelle propriété de niveau de jeu (`initialSeconds`) pour cela :

```
<Game   challengeSize={6}   challengeRange={[2, 9]}   initialSeconds={10} />
```

Pour être honnête, nous n'avons pas besoin que le `gameStatus` soit sur le state du tout. Il est principalement calculable. Cependant, je fais intentionnellement une exception en le plaçant sur le state comme une forme simplifiée de **mise en cache** de ce calcul.

Idéalement, il est préférable de mettre en cache ce calcul comme une propriété d'instance, mais je vais le garder sur le state pour garder les choses simples.

Et les couleurs de fond utilisées pour le nombre cible lorsque le joueur gagne ou perd un jeu ? Doivent-elles aller sur le state ?

Pas vraiment. Puisque nous avons un élément `gameStatus`, nous pouvons l'utiliser pour rechercher la bonne couleur de fond. Le dictionnaire des couleurs de fond peut être une simple propriété statique `Game` (ou vous pouvez le transmettre si vous voulez le rendre personnalisable) :

```
// Dans le composant Game
```

```
  static bgColors = {    playing: '#ccc',    won: 'green',    lost: 'red',  };
```

Vous pouvez voir le code complet que nous avons pour l'instant [ici](https://jscomplete.com/repl/?j=rkh2YjEJf).

#### Étape #5 : concevoir les vues comme des fonctions de données et de state

C'est vraiment le cœur de React. Maintenant que nous avons identifié toutes les données et le state dont ce jeu a besoin, nous pouvons concevoir toute l'UI en fonction de ceux-ci.

Puisque le state commence généralement avec des valeurs vides (comme le tableau vide `selectedIds`), il est difficile de concevoir l'UI sans tester des valeurs réelles. Cependant, des valeurs fictives peuvent être utilisées pour faciliter les tests :

```
// Mock states:
```

```
state = {  gameStatus: 'playing',  remainingSeconds: 7,  selectedIds: [0, 3, 4],};
```

```
// Testez également avec  gameStatus: 'lost'
```

```
// Et  gameStatus: 'won'
```

En utilisant cette stratégie, nous n'avons pas à nous soucier du comportement et des interactions utilisateur (pour l'instant). Nous pouvons nous concentrer uniquement sur la conception de l'UI en fonction des données et du state (fictif).

La clé pour exécuter cette étape correctement est **de s'assurer que les composants enfants reçoivent uniquement les données minimales dont ils ont réellement besoin pour se re-rendre dans les différents states**. C'est probablement l'énoncé le plus important de tout l'article.

Nous n'avons qu'un seul composant enfant, alors réfléchissons à ce dont il a besoin pour se rendre. Nous transmettons déjà sa valeur depuis l'appel de map, alors qu'a-t-il besoin d'autre ? Par exemple, réfléchissez à ces questions :

* Le composant `Number` doit-il être conscient du tableau `selectedIds` pour déterminer s'il est un nombre sélectionné ?
* Le composant `Number` doit-il être conscient de la valeur actuelle de `gameStatus` ?

Je dois admettre que répondre à ces questions n'est pas aussi facile que vous pourriez le penser. Bien que vous pourriez être tenté de répondre oui aux deux, le composant `Number` n'a pas besoin d'être conscient à la fois de `selectedIds` et de `gameStatus`. Il doit seulement être conscient s'il peut être cliqué ou non. S'il ne peut pas être cliqué, il devra se rendre différemment.

Transmettre autre chose au composant `Number` le fera se re-rendre inutilement, ce que nous devons éviter.

Nous pouvons utiliser une opacité plus faible pour représenter un nombre non cliquable. Faisons en sorte que le composant `Number` reçoive une propriété `clickable`.

Le calcul de cette propriété booléenne `clickable` doit se faire dans le composant `Game` afin d'éviter d'avoir à transmettre plus de données au composant `Number`. Laissez-moi donner des exemples sur l'importance de s'assurer qu'un composant enfant reçoive uniquement les données minimales dont il a besoin :

* Si nous transmettons la valeur `gameStatus` au composant `Number`, alors chaque fois que le `gameStatus` change (par exemple, de `playing` à `won`), React va re-rendre tous les six nombres de défi. Mais dans ce cas, il n'avait pas vraiment besoin de re-rendre aucun d'entre eux.
* Un composant Number doit se re-rendre lorsque le `gameStatus` change de `new` à `playing` à cause de la fonctionnalité des points d'interrogation de masquage au début. Pour éviter de transmettre le `gameStatus` à `Number`, nous pouvons calculer la valeur affichée dans un composant `Number` à l'intérieur de la fonction de rappel `map` dans le composant `Game`.
* Si nous transmettons le tableau `selectedIds` au composant `Number`, alors à chaque clic React va re-rendre tous les six nombres de défi alors qu'il n'avait besoin de re-rendre qu'un seul nombre. C'est pourquoi un indicateur booléen `clickable` est un bien meilleur choix ici.

Avec chaque propriété que vous transmettez à un composant enfant React vient une grande responsabilité.

C'est plus important que vous ne le pensez. Cependant, React n'optimisera pas le re-rendu d'un composant automatiquement. Nous devrons décider si nous voulons qu'il le fasse. Cela est discuté dans l'étape #8 ci-dessous.

Outre la propriété `clickable`, qu'a-t-il besoin d'autre le composant `Number` ? Puisqu'il va être cliqué, et que nous devons placer l'ID du nombre cliqué sur le state de `Game`, le gestionnaire de clic de chaque composant `Number` doit être conscient de son propre ID. Et nous ne pouvons pas utiliser la valeur de la propriété `key` de React dans ce cas. Faisons en sorte que le composant `Number` reçoive également une propriété `id`.

```
// Dans le composant Number
```

```
render() {    return (      <div         className="number"         style={{ opacity: this.props.clickable ? 1 : 0.3 }}        onClick={() => console.log(this.props.id)}      >        {this.props.value}      </div>    );  }
```

Pour calculer si un nombre est disponible et cliquable, vous pouvez utiliser un simple appel `indexOf` sur le tableau `selecetdIds`. Créons une fonction pour cela :

```
// Dans la classe GameisNumberAvailable = (numberIndex) =>    this.state.selectedIds.indexOf(numberIndex) === -1;
```

Un comportement que vous avez probablement remarqué en jouant au jeu ci-dessus est que les carrés de nombres commencent par afficher un point d'interrogation jusqu'à ce que le bouton Start soit cliqué. Nous pouvons utiliser un opérateur ternaire pour contrôler la valeur de chaque composant `Number` en fonction de la valeur `gameStatus`. Voici ce que nous devons changer pour rendre un composant `Number` à l'intérieur de l'appel `map` :

```
<Number  key={index}  id={index}  value={this.state.gameStatus === 'new' ? '?' : value}  clickable={this.isNumberAvailable(index)}/>
```

Nous pouvons utiliser une expression ternaire similaire pour la valeur du nombre cible. Nous pouvons également contrôler sa couleur de fond en utilisant un appel de recherche à l'objet statique `bgColors` :

```
<div  className="target"  style={{ backgroundColor: Game.bgColors[gameStatus] }}&gt;  {this.state.gameStatus === 'new' ? '?' : this.target}</div>
```

Enfin, nous devrions montrer le bouton **Start** uniquement lorsque le `gameStatus` est `new`. Sinon, nous devrions simplement montrer le compteur `remainingSeconds`. Lorsque le jeu est `won` ou `lost`, montrons un bouton **Play Again**. Voici les modifications dont nous avons besoin pour tout cela :

```
<div className="footer">  {this.state.gameStatus === 'new' ? (    <button>Start</button>  ) : (    <div className="timer-value">{this.state.remainingSeconds}</div>  )}  {['won', 'lost'].includes(this.state.gameStatus) && (    <;button>Play Again</button>  )}</div>
```

Vous pouvez voir le code complet que nous avons pour l'instant [ici](https://jscomplete.com/repl/?j=HkIlnsEJG).

#### Étape #6 : concevoir des comportements pour changer le state

Le premier comportement que nous devons comprendre est comment démarrer le jeu. Nous avons besoin de deux actions principales ici : 1) changer le `gameStatus` en `playing` et 2) démarrer un timer pour décrémenter la valeur `remainingSeconds`.

Si `remainingSeconds` est décrémenté jusqu'à zéro, nous devons forcer le jeu à passer à l'état `lost` et arrêter le timer également. Sinon, il décrémentera au-delà de zéro.

Voici une fonction que nous pouvons utiliser pour faire tout cela :

```
// Dans la classe Game
```

```
startGame = () => {  this.setState({ gameStatus: 'playing' }, () => {    this.intervalId = setInterval(() => {      this.setState((prevState) => {        const newRemainingSeconds = prevState.remainingSeconds - 1;        if (newRemainingSeconds === 0) {          clearInterval(this.intervalId);          return { gameStatus: 'lost', remainingSeconds: 0 };        }        return { remainingSeconds: newRemainingSeconds };      });    }, 1000);  });};
```

Remarquez comment je démarre le timer uniquement après que l'appel `setState` est terminé. Cela est possible en utilisant la **fonction de rappel du deuxième argument** de `setState`.

Ensuite, déterminons ce qui devrait se passer lorsqu'un nombre est cliqué pendant une session de jeu. Créons une fonction `selectNumber` pour cela. Cette fonction devrait recevoir l'ID du nombre cliqué et ne devrait fonctionner que lorsque le `gameStatus` est `playing`. Chaque fois qu'un nombre est cliqué, nous devons ajouter son ID au tableau `selectedIds`.

Nous devons également calculer le nouveau `gameStatus` car chaque clic peut entraîner un statut `won`/`lost`. Créons une fonction `calcGameStatus` pour cela.

Voici une façon d'implémenter ces deux nouvelles fonctions :

```
// Dans la classe Game
```

```
selectNumber = (numberIndex) => {  if (this.state.gameStatus !== 'playing') {    return;  }  this.setState(    (prevState) => ({      selectedIds: [...prevState.selectedIds, numberIndex],      gameStatus: this.calcGameStatus([        ...prevState.selectedIds,        numberIndex,      ]),    }),    () => {      if (this.state.gameStatus !== 'playing') {        clearInterval(this.intervalId);      }    }  );};
```

```
calcGameStatus = (selectedIds) => {  const sumSelected = selectedIds.reduce(    (acc, curr) => acc + this.challengeNumbers[curr],    0  );  if (sumSelected < this.target) {    return 'playing';  }  return sumSelected === this.target ? 'won' : 'lost';};
```

Remarquez quelques choses sur les fonctions ci-dessus :

* Nous avons utilisé l'**opérateur de propagation** de tableau pour ajouter `numberIndex` à `selectedIds`. C'est une astuce pratique pour éviter de muté le tableau original.
* Puisque le nouveau `gameStatus` doit être calculé **pendant** que nous mettons à jour le state, j'ai passé la nouvelle valeur `selectedIds` à la fonction `calcGameStatus` plutôt que d'utiliser la valeur actuelle de `selectedIds`. Elle n'a pas encore été mise à jour pour inclure le nouveau `numberIndex` à ce stade.
* Dans `calcGameStatus`, j'ai utilisé un appel `reduce`. Cela calcule la somme actuelle après un clic en utilisant une combinaison de ce qui est sélectionné et du tableau original `challengeNumbers`, qui contient les valeurs réelles des nombres. Ensuite, quelques conditionnelles peuvent faire le tour de déterminer le statut actuel du jeu.
* Puisque le timer doit être arrêté si le nouveau `gameStatus` n'est pas `playing`, j'ai utilisé l'argument de rappel secondaire pour `setState` pour implémenter cette logique. Cela garantit qu'il utilisera le nouveau `gameStatus` après que l'appel asynchrone `setState` soit terminé.

Le jeu est actuellement complètement fonctionnel à l'exception du bouton **Play Again**. Vous pouvez voir le code complet que nous avons pour l'instant [ici](https://jscomplete.com/repl/?j=SJoO0nVJf).

Maintenant, comment allons-nous implémenter exactement cette action **Play Again** ? Pouvez-nous simplement réinitialiser le state du composant `Game` ?

Non. Réfléchissez à pourquoi.

#### Étape #7 : réinitialiser un composant React

L'action **Play Again** a besoin de plus qu'une simple réinitialisation du state du composant `Game`. Nous devons générer un nouvel ensemble de `challengeNumbers` ainsi qu'un nouveau nombre `target`. De plus, nous devons effacer tous les timers en cours d'exécution et démarrer automatiquement le jeu.

Nous pouvons certainement améliorer la fonction `startGame` pour faire tout cela. Mais React offre une manière plus facile de réinitialiser un composant : démonter ce composant et le remonter simplement. Cela déclenchera tout le code d'initialisation et prendra également en charge tous les timers.

Nous n'avons pas vraiment à nous soucier de la partie timer du state, car cette partie est contrôlée par le comportement. Cependant, en général, le démontage d'un composant doit également effacer tous les timers définis dans ce composant. Faites toujours cela :

```
// Dans la classe Game
```

```
  componentWillUnmount() {    clearInterval(this.intervalId);  }
```

Maintenant, si le composant `Game` est démonté et remonté, il démarrera une instance complètement nouvelle avec de nouveaux nombres aléatoires et un state vide. Cependant, pour remonter un composant en fonction d'un comportement, nous devrons introduire un nouveau composant parent pour `Game`. Nous l'appellerons `App`. Ensuite, nous mettrons quelque chose sur le state de ce nouveau composant parent qui déclenchera un changement d'UI.

React a une autre astuce utile que nous pouvons utiliser pour accomplir cette tâche. Si un composant React est rendu avec une certaine `key` et ensuite re-rendu avec une `key` différente, React voit une instance complètement nouvelle. Il démonte et remonte alors automatiquement ce composant !

Tout ce que nous devons faire est d'avoir un ID de jeu unique comme partie du state du composant `App`, utiliser cela comme `key` pour le composant `Game`, et le changer lorsque nous devons réinitialiser un jeu.

Nous voulons également que le jeu se lance automatiquement lorsque le joueur clique sur **Play Again**, au lieu de lui faire cliquer sur **Start** après **Play Again**. Alors faisons en sorte que le composant App transmette également une propriété **autoPlay** à **Game** et calculons cela en fonction du nouvel attribut **gameId**. Seule la première partie ne doit pas être jouée automatiquement.

Voici les modifications dont nous avons besoin :

```
// Créer un nouveau composant App
```

```
class App extends React.Component {  state = {    gameId: 1,  };
```

```
resetGame = () =>    this.setState((prevState) => ({      gameId: prevState.gameId + 1,    }));
```

```
  render() {    return (      <Game        key={this.state.gameId}        autoPlay={this.state.gameId > 1}        challengeSize={6}        challengeRange={[2, 9]}        initialSeconds={10}        onPlayAgain={this.resetGame}      />    );  }}
```

```
// Dans la classe Game : respecter la valeur de la nouvelle propriété autoPlay  componentDidMount() {    if (this.props.autoPlay) {      this.startGame();    }  }
```

```
// Dans l'appel de rendu de Game// Connecter l'action Play Again en utilisant la propriété parent<button onClick={this.props.onPlayAgain}>  Play Again</button>
```

```
// Rendre le nouveau composant App au lieu de GameReactDOM.render(<App />, document.getElementById('mountNode'));
```

Vous pouvez voir le code complet que nous avons maintenant [ici](https://jscomplete.com/repl/?j=HJrVXJrJG).

#### Étape #8 : optimiser si vous pouvez mesurer

L'un des aspects difficiles d'une application React est d'éviter le rendu inutile des composants qui n'ont pas besoin d'être re-rendus. Nous avons fait de grands efforts dans l'étape #5 pour ne pas transmettre de propriété qui causerait un re-rendu inutile d'un composant `Number`.

Cependant, le code tel qu'il est maintenant continue de re-rendre inutilement la plupart des composants `Number`. Pour voir cela en action, utilisez une méthode `componentWillUpdate` dans le composant `Number` et faites simplement un `console.log` là :

```
// Dans le composant NumbercomponentWillUpdate() {  console.log('Number Updated');}
```

Ensuite, allez-y et jouez. À chaque changement de state dans le composant `Game`, vous verrez que nous re-rendons les 6 composants `Number`. Cela se produit lorsque nous cliquons sur le bouton **Start** et chaque seconde après cela !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gun2dDDh21wbMyBmPkJIIQ.png)
_Le composant Number a été re-rendu 66 fois. Combien de ces re-rendus étaient nécessaires ?_

Le fait est qu'un composant `Number` ne devrait pas se re-rendre lui-même à moins que le joueur ne clique dessus. Les `60` re-rendus qui ont été déclenchés par le changement de timer étaient inutiles. De plus, lorsque le joueur clique sur un nombre, seul ce nombre a besoin d'être re-rendu. Actuellement, React re-rend également les six nombres lorsque le joueur sélectionne un nombre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JB4ahRqp1hWKGr1LvbjsoQ.png)
_36 mises à jour du composant Number se sont produites alors que seulement 9 mises à jour auraient dû se produire_

Heureusement, nous avons été suffisamment prudents pour ne transmettre au composant `Number` que les propriétés exactes dont il a besoin pour se re-rendre. Seul le nombre de défi qui doit être re-rendu recevra des valeurs différentes dans ces propriétés.

Cela signifie que nous pouvons utiliser une conditionnelle dans `shouldComponentUpdate` de React pour court-circuiter l'opération de rendu si tous les `nextProps` d'un composant `Number` correspondent aux propriétés actuelles.

La classe `PureComponent` de React fera exactement cela. Allez-y et changez le composant `Number` pour qu'il étende `React.PureComponent` au lieu de `React.Component` et voyez comment le problème disparaît magiquement.

```
class Number extends React.PureComponent
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*zz5qM2QVa_7ZrRmuXC2a9A.png)
_Exactement dix composants Number ont été mis à jour (six initiaux + les quatre sélectionnés)_

Cependant, cette optimisation en vaut-elle la peine ? Nous ne pouvons pas répondre à cette question sans mesurer. Basiquement, vous devez mesurer quel code utilise le moins de ressources : un appel de rendu de composant ou l'instruction `if` dans `React.PureComponent` qui compare l'état/les propriétés précédents et suivants. Cela dépend complètement des tailles des arbres d'état/propriétés et de la complexité de ce qui est re-rendu. Ne supposez pas simplement qu'une manière est meilleure que l'autre.

Vous pouvez voir le code final [ici](https://jscomplete.com/repl/?j=rJj8poQyM). MVP complet. Maintenant, par amour du CSS, quelqu'un peut-il styliser ce jeu pour le rendre attrayant pour les enfants ? :)

Ne vous arrêtez pas ici si vous aimez cela. Ajoutez plus de fonctionnalités au jeu. Par exemple, gardez un score pour les victoires et augmentez-le chaque fois que le joueur gagne une manche. Peut-être faites en sorte que la valeur du score dépende de la rapidité avec laquelle le joueur gagne la manche.

Vous pouvez également rendre les manches futures plus difficiles en changeant `challengeSize`, `challengeRange`, et `initialSeconds` lors du démarrage d'un nouveau jeu.

Le jeu Target Sum a été présenté dans mon **cours React Native Essential Training**, qui est disponible sur [Lynda](https://www.lynda.com/React-Native-tutorials/React-Native-Essential-Training/560343-2.html) et [LinkedIn Learning](https://www.linkedin.com/learning/react-native-essential-training).

Merci d'avoir lu.

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)