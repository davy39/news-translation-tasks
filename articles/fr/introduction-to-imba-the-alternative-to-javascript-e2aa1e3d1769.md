---
title: 'Introduction à Imba : le langage compatible JavaScript pour des mises à jour
  DOM ultra-rapides'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T07:56:49.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-imba-the-alternative-to-javascript-e2aa1e3d1769
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Clq_Sxied7OsDJPgH-n1yw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: vue
  slug: vue
- name: Web Development
  slug: web-development
seo_title: 'Introduction à Imba : le langage compatible JavaScript pour des mises
  à jour DOM ultra-rapides'
seo_desc: 'By Per Harald Borgen

  Imba is an open-source programming language we created specifically for building
  web apps. It compiles to JavaScript and works inside the existing JS ecosystem,
  meaning you can use it with Node, npm, and Webpack.

  The big benefit ...'
---

Par Per Harald Borgen

Imba est un langage de programmation open-source que nous avons créé spécifiquement pour construire des applications web. Il compile en JavaScript et fonctionne dans l'écosystème JS existant, ce qui signifie que vous pouvez l'utiliser avec Node, npm et Webpack.

Le grand avantage d'Imba est qu'il permet de créer des applications beaucoup plus rapides que si vous utilisiez des bibliothèques basées sur le DOM virtuel comme React et Vue. L'augmentation de la vitesse est due à la manière dont Imba gère les mises à jour du DOM, que mon cofondateur et créateur d'Imba [Sindre Osen Aarsaether](https://www.freecodecamp.org/news/introduction-to-imba-the-alternative-to-javascript-e2aa1e3d1769/undefined) [explique ici](https://medium.freecodecamp.org/the-virtual-dom-is-slow-meet-the-memoized-dom-bb19f546cc52).

J'utilise Imba moi-même depuis quelques années, et c'est effectivement un langage agréable à utiliser, car la syntaxe est plus propre que celle de JavaScript, ce qui améliore la lisibilité du code.

Tout au long de cet article, je vais vous apprendre à commencer à développer des applications Imba simples par vous-même. Nous commencerons par un peu de syntaxe avant de passer à la création d'interfaces utilisateur. Enfin, je vous aiderai à vous installer sur votre machine afin que vous puissiez continuer à coder par vous-même.

### Projets utilisant Imba

Mais avant de plonger dans le code, je veux souligner que ce n'est pas seulement un langage obscur utilisé dans des projets de loisir. Imba alimente également des applications critiques pour de grandes entreprises.

Un exemple est le [marché aux enchères de poisson](https://rsf.is/) en Islande. Comme le poisson est une grande affaire en Islande, ce marché représente 1,6 % de l'économie du pays, soit environ 390 millions de dollars US.

> Donc Imba gère en fait 1,6 % du PIB de l'Islande !

![Image](https://cdn-media-1.freecodecamp.org/images/1*hx-omKWeIS8rDU5vfKOC4A.png)

Deuxièmement, l'ensemble de la plateforme d'apprentissage [Scrimba.com](https://scrimba.com/) est construite avec Imba, à la fois le front-end et le back-end. C'est une application complexe qui dépend fortement de la réconciliation DOM rapide d'Imba.

![Image](https://cdn-media-1.freecodecamp.org/images/1*th9zBq40K-4HkByEKbILhg.png)

Ainsi, le langage que vous apprendrez aujourd'hui peut vous aider à construire des applications de production à grande échelle ainsi que des projets secondaires plus petits.

Commençons !

### La syntaxe

La syntaxe d'Imba présente de nombreuses similitudes avec JavaScript, mais elle est également influencée par Ruby et Python. Elle est facile à apprendre en cours de route, alors commençons par un exemple. Ci-dessous, vous verrez une fonction JavaScript simple qui retourne le plus grand de deux nombres, ou false s'ils sont égaux :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vCJGm1ZHEkc5BYaAsbgNuw.png)
_findGreatest en JavaScript_

Maintenant, traduisons cela en Imba :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FIY4FhDdPoFmHy5I0FxuQA.png)
_findGreatest en Imba_

En regardant simplement les deux exemples, vous pouvez probablement déduire quelques différences fondamentales entre Imba et JavaScript :

1. **function → def.** Tout d'abord, le mot-clé `function` a été renommé en `def`.
2. **Pas de parenthèses.** De plus, les paramètres de la fonction ne sont pas enveloppés dans des parenthèses. Vous aurez en fait rarement besoin de parenthèses dans Imba, mais vous pouvez les utiliser si vous le souhaitez.
3. **Indentations.** Imba est basé sur l'indentation. Cela signifie que nous n'avons pas besoin d'utiliser des accolades, ce qui économise de l'espace.
4. **Pas de return.** Dans Imba, les retours sont implicites, ce qui signifie que nous n'avons pas besoin d'écrire `return`. Imba retourne automatiquement la dernière expression de la fonction.

Aucune de ces différences n'est l'aspect le plus important d'Imba, mais ensemble, elles rendent le code moins verbeux que JavaScript. Cet avantage deviendra plus clair à mesure que nous progresserons dans cet article.

### Construction d'interfaces utilisateur

Passons à la création d'interfaces utilisateur. C'est en fait ce pour quoi Imba est conçu. Cela signifie que les nœuds DOM sont intégrés dans le langage en tant que citoyens de première classe.

> Si vous venez du monde React, vous pouvez le voir comme si Imba avait sa propre version de JSX intégrée dans le langage.

Considérez le code suivant en React, qui rend simplement un bouton et enregistre quelque chose dans la console lorsqu'il est cliqué :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7-oYsP6nqhipaw-sgsYfTA.png)

Si nous réécrivons cet exemple en Imba, nous obtenons ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NI4x41wXBq9OAFbhoKM6BA.png)

Prenez un moment pour comparer les deux. Il y a trois choses que je veux que vous remarquiez :

1. **Les balises sont natives.** Le `class App extends React.Component` a été traduit en `tag App` beaucoup plus simple. Cela est dû au fait que `tag` est une partie native du langage Imba. Cela est vrai pour les balises DOM et les balises personnalisées.
2. **Pas de balises de fermeture.** Comme nous utilisons l'indentation, nous n'avons pas besoin de fermer nos balises (par exemple, `</button>`). Cela nous fait économiser beaucoup de frappe et d'espace.
3. **Syntaxe de classe simple.** L'ajout de classes est simple dans Imba. Au lieu de l'encombrant `className="container"`, nous ajoutons simplement un `.container` à la balise elle-même.

Vous avez peut-être également remarqué que le gestionnaire d'événements est différent. Nous faisons `:tap.logOut` au lieu de `onClick={this.logOut}`. Ce n'est qu'une des plusieurs façons de gérer les entrées utilisateur dans Imba, que vous pouvez lire plus en détail [dans la documentation](http://imba.io/guides/essentials/event-handling#event-handling) si vous êtes intéressé.

### Gestion des données

Maintenant, examinons comment Imba gère les données. Dans l'exemple ci-dessous, j'ai modifié notre application pour inclure une variable `count` dans l'état du composant `App`. Cette variable sera augmentée ou diminuée en fonction du bouton sur lequel l'utilisateur clique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CHovwPSo9VYJD5bES9KyTw.png)

Voici à quoi ressemble la réécriture en Imba :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JtfkPX_D10cQMTdlYOmEVQ.png)

La différence la plus frappante est la quantité de code.

> L'exemple Imba est environ deux fois plus petit, à la fois en lignes de code et en nombre de caractères.

Bien que le nombre de lignes de code soit certainement une comparaison superficielle, la lisibilité d'une base de code est importante. Moins de lignes, moins de caractères et moins de symboles rendent l'exemple Imba plus facile à lire que React.

#### Self implicite

Une chose que vous avez peut-être également remarquée est que nous avons accédé à notre variable d'instance directement via `count`, contrairement à React, où nous utilisons `this.state.count` pour récupérer la valeur.

Dans Imba, nous aurions pu faire `self.count`. Cependant, le `self` est implicite, donc nous n'avons pas besoin de l'écrire. Imba vérifie s'il y a une variable `count` dans la portée, ou si `count` existe en tant que variable d'instance sur `App` lui-même.

#### Mutabilité

Une autre grande différence entre les deux exemples ci-dessus est la manière dont ils traitent les changements d'état. Dans l'exemple Imba, l'état est mutable, car nous le changeons simplement directement, la variable `count`.

Cela suit un modèle opposé à React, où `this.state` doit être traité comme immutable, et la seule façon de le changer est via `this.setState`.

Vous pouvez utiliser une bibliothèque immutable avec Imba si vous préférez. Il est en fait agnostique à cet égard. Chez Scrimba, nous utilisons la mutabilité, car nous ne pensons pas que les coûts de l'immutabilité en valent la peine.

### Installation d'Imba en local

Maintenant que vous avez appris les bases, il est temps de commencer à coder par vous-même, alors installons Imba sur votre machine locale. Suivez simplement ces quatre étapes, et vous serez prêt à partir :

```
git clone https://github.com/somebee/hello-world-imba.git
```

```
cd hello-world-imba
```

```
npm install
```

```
npm run dev
```

Accédez à [http://localhost:8080/](http://localhost:8080/) et vous verrez votre projet. Ouvrez _src/client.imba_ pour commencer à modifier l'application.

Alternativement, si vous souhaitez commencer sans l'installer localement, vous pouvez utiliser [ce terrain de jeu interactif Scrimba](https://scrimba.com/c/cyW2esn?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=imba_intro_article).

### La vitesse d'Imba

Avant de conclure, examinons également la vitesse d'Imba. La raison pour laquelle il est si incroyablement rapide est en fait qu'il ne suit pas l'implémentation du DOM virtuel que React a popularisée. Il utilise quelque chose qu'il appelle le Memoized DOM, qui est une méthode plus simple et plus directe de le faire.

Dans le [benchmark](https://somebee.github.io/dom-reconciler-bench/index.html) ci-dessous, nous comptons combien d'opérations DOM nous sommes capables de faire par seconde en effectuant un _test en direct_ aux côtés de Vue et React. Les trois bibliothèques font exactement la même chose, qui est de modifier une liste de tâches des milliers de fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EXQcYGJWR06_EDyRc0MRSA.png)
_Benchmarking Imba contre React et Vue. Résultat : 20 à 30 fois plus rapide pour la réconciliation DOM._

> Comme vous pouvez le voir, Imba gère en fait 20 à 30 fois plus d'opérations que React et Vue.

Donc Imba est rapide. Vraiment rapide.

#### Conclusion

Il y a beaucoup d'autres choses à apprendre sur Imba, donc je vous recommande de visiter [la documentation](http://imba.io/). Par exemple, ses concepts de getters/setters et d'invocations implicites sont importants à comprendre. La courbe d'apprentissage peut être un peu raide au début, mais c'est comme ça. Tout ce qui vaut la peine dans la vie nécessite un peu de douleur et d'effort ;)

Dans le prochain article, je couvrirai certaines des fonctionnalités plus avancées. [Suivez-moi sur Twitter](http://bit.ly/perborgen) pour être averti lorsque ce moment arrivera.

Bonne chance et bon codage !

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com) – la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=imba_intro_article) si vous souhaitez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=imba_intro_article)_