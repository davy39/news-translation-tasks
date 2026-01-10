---
title: Comment créer un bouton intelligent avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-22T08:19:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-smart-button-using-react-1a7628341b4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*J73Qzjq_mkMta6f8QMKiPQ.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer un bouton intelligent avec React
seo_desc: 'By Amber Wilkie

  This is a tale of three buttons and how a web developer who leans away from design
  made her front-end dreams come true.

  You should know ahead of time that most of the styling here is boilerplate Bootstrap.
  It looks good and it’s an in...'
---

Par Amber Wilkie

Ceci est l'histoire de trois boutons et comment une développeuse web qui évite le design a réalisé ses rêves de front-end.

Vous devez savoir à l'avance que la plupart du style ici est du code standard [Bootstrap](https://getbootstrap.com/). C'est joli et c'est un produit interne, donc nous ne réparons pas ce qui n'est pas cassé.

Notre tâche était de créer une interface facile à comprendre pour gérer un enregistrement. Notre enregistrement a un `state` en trois parties — soit `available`, `sick` ou `vab`. Pas beaucoup d'états à communiquer une fois, mais nous avons besoin de cinq semaines de ceux-ci sur une page.

Note de côté : « VAB » est un mot suédois qui fait référence au fait de rester à la maison avec son enfant malade. Il y a une différence entre faire cela et être malade soi-même ici, à la fois en termes de salaire et de temps libre !

### Vérification d'un enregistrement existant

La première étape consistait à montrer si l'utilisateur avait ou non un enregistrement pour le jour en question. Comme dans chaque projet React que je connais, nous prenions une liste d'une API (la nôtre) et nous itérions dessus. Puisque l'API retournera une liste d'enregistrements existants et ignorera les jours sans enregistrements, nous devrons configurer notre propre tableau de jours.

Voici notre code pour obtenir cinq semaines de jours :

```
export const dateArray = (numberOfDays, startDate) => {  const day = moment(startDate);  const days = [];  while (days.length < numberOfDays) {    if (day.day() === 6 || day.day() === 0) {      day.add(1, 'days');    } else {      days.push(day.format('YYYY-MM-DD'));    }    day.add(1, 'days');  }  return days;};
```

J'ai déjà écrit sur [Moment.js](https://momentjs.com/). Si vous ne l'utilisez pas, montez dans le wagon déjà ! Cela rend le travail avec les dates extrêmement facile, comme ici où nous pouvons appeler `day.add(1, 'days')` ou où nous obtenons le jour de la semaine avec `moment(startDate).day()`.

Les objets Moment sont mutables ! Soyez donc prudent en général, mais ici c'est génial car nous devons mettre à jour notre `day` et nous pouvons le faire avec très peu de code.

Note de côté : Les Américains feraient naturellement de samedi le dernier jour de la semaine — 6 — et de dimanche le premier jour — 0. Mais pas les Suédois ou pratiquement le reste du monde. Pour presque tout le monde sauf les Américains, la semaine commence le lundi. La programmation peut être très étrangement centrée sur l'Amérique.

Ici, vous pouvez voir que nous assemblons une liste de dates, en commençant par `startDate`, et nous continuons jusqu'à atteindre `numberOfDays`, en sautant les week-ends. Nous utiliserons ce tableau pour construire notre liste d'enregistrements afin de pouvoir y mettre quelques boutons appétissants.

#### Mappage de notre tableau de jours pour refléter les enregistrements réels

Maintenant que nous avons tous les jours que nous devons afficher (ci-dessous nous appelons `dateArray`), nous devrons parcourir notre ensemble de données de l'API pour déterminer si nous devons afficher un enregistrement ou non. Parce que nous voulons voir les dates qui n'ont pas d'enregistrements, nous devons configurer un tableau avec certains enregistrements remplis et d'autres vides :

```
const userRecords = dateArray(50, startDay).map(date => {  const recordToReturn = data.find(record =>    record.date === date  );  return { date, record: recordToReturn };});
```

Maintenant, nous avons un tableau de dates, certaines avec un enregistrement complet et d'autres avec `record: undefined`.

### Logique du bouton Available

Maintenant que nous pouvons voir s'il y a un enregistrement ce jour-là ou non, nous pouvons conditionner notre bouton pour qu'il soit vert et dise « Available » ou blanc et « Add ». Encore une fois, j'utilise Reactstrap pour le style de base. Le composant `Button` vient avec un bel espacement et des coins arrondis et autres, plus des paramètres « color » pratiques que je peux définir sur des choses comme « info » et « success ».

```
<Button color={setColor(record)} >  {this.state.buttonText}</Button>
```

#### Définition du texte du bouton

Pour définir le `buttonText`, je vérifierai s'il y a un enregistrement :

```
const buttonText = () =>   isEmpty(this.props.data.record) ? 'Add' : 'Available'
```

Rappelez-vous que je passe `{date: 'some date', record: {some: 'record'}}` dans chacun de mes composants de bouton. Si mon `userRecords` n'a pas trouvé d'enregistrement pour ce jour, nous n'aurons rien dans `data.record` et nous pourrons dire « Add ». `isEmpty` provient de l'excellente bibliothèque Javascript [lodash](https://lodash.com). Encore une fois, montez dans le wagon. Lodash rend Javascript beaucoup plus propre et plus facile à utiliser.

#### Définition de la couleur du bouton

Notre fonction `setColor` vérifiera également si l'enregistrement existe, mais elle devra également examiner le `state` de l'enregistrement pour voir quelle couleur nous devons afficher.

```
const setColor = () => {  if (existingRecord && record.status === 'available') {    return 'success';  } else if (existingRecord)) {    return 'gray';  } else {    return 'secondary';  }};
```

Bootstrap a des défauts agréables. Nous avons remplacé ces mots par défaut par nos propres couleurs, mais les options prêtes à l'emploi sont également belles. Ici, nous vérifions si l'enregistrement est `available`. S'il n'est pas disponible mais qu'il y a toujours un enregistrement, il doit être `sick` ou `vab`, mais dans les deux cas, l'utilisateur n'est plus `available` ce jour-là, donc nous devrons griser le bouton.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J73Qzjq_mkMta6f8QMKiPQ.png)
_Les boutons colorés démontrent quatre statuts._

### Les deux autres boutons

Je peux utiliser l'affichage conditionnel super pratique de React pour masquer les boutons « sick » et « vab » lorsqu'il n'y a pas d'enregistrement. Voici le code pour les deux boutons restants :

```
{existingRecord && (  <div>    <Button      color={setSecondaryColor(record, 'sick')}      style={{ marginRight: '5px' }}    >      Sick    </Button>    <Button      color={setSecondaryColor(record, 'vab')}      style={{ marginRight: '5px' }}    >      VAB    </Button>  </div>)}
```

Pour nous assurer que nos boutons ont les bonnes couleurs, nous vérifierons simplement que le `record` a le `status` « sick » ou « vab », respectivement. Si le statut de l'enregistrement ne correspond pas à celui du bouton, nous nous assurerons qu'il n'est pas coloré (notre couleur de bouton « secondary » est blanche).

```
const setSecondaryColor = (record, status) => {  if (record.status !== status) { return 'secondary'}  if (status === 'sick') { return 'danger'}  if (status === 'vab') { return 'yellow'}}
```

### Se faire plaisir avec les survols

À ce stade, les boutons faisaient tout ce dont j'avais besoin (plus toute la logique des requêtes API que j'omets de cet article — nous créons et mettons à jour des enregistrements avec ces boutons).

Mais comment une fille peut-elle être satisfaite de ses boutons s'il n'y a pas d'effets de survol ? Nous devons pouvoir supprimer un enregistrement pour un jour d'une manière ou d'une autre. Au lieu de faire une X et de faire cliquer nos utilisateurs dessus, ne serait-il pas mieux s'ils pouvaient cliquer sur l'un des boutons existants pour supprimer l'enregistrement ? Je le pensais.

J'ai ajouté des événements `onMouseOver` et `onMouseOut` à mon bouton « Available » / « Add » :

```
const mouseOver = () => {  if (existingRecord) {    this.setState({ buttonText: 'Remove' });  }};const mouseOut = () => this.setState({ buttonText: buttonText() });
```

Maintenant, lorsque vous survolez le bouton, il changera pour « Remove » si un enregistrement existe (et restera sinon le même). Lorsque vous sortez, il reviendra à « Available ». Si beau, si fonctionnel !

![Image](https://cdn-media-1.freecodecamp.org/images/1*IB6lPh5Ol4oSQ44X6nioxw.png)
_Démonstration du survol de la fonctionnalité du bouton_

J'ai été surprise par la quantité de réflexion et d'effort qui a dû être mise dans quelque chose de relativement simple. Faire en sorte que les boutons aient la bonne couleur, le bon texte et fassent les bonnes choses est plus complexe qu'il n'y paraît. En fait, j'ai montré ces boutons à des gens comme mon mari, qui haussent simplement les épaules. C'est un fait de la vie : personne n'aimera vos boutons autant que vous.