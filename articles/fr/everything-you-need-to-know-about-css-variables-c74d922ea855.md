---
title: Tout ce que vous devez savoir sur les variables CSS [Guide Complet]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T14:42:34.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-css-variables-c74d922ea855
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Im5WsB6Y7CubjWRx9hH7Gg.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: handbook
  slug: handbook
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Tout ce que vous devez savoir sur les variables CSS [Guide Complet]
seo_desc: 'By Emmanuel Ohans

  Most programming languages have support for variables. But sadly, CSS has lacked
  support for native variables from the very beginning.

  You write CSS? Then no variables for you. Well, except if you were using a preprocessor
  like Sass...'
---

Par Emmanuel Ohans

La plupart des langages de programmation supportent les variables. Mais malheureusement, CSS a toujours manqué de support pour les variables natives dès le début.

Vous écrivez du CSS ? Alors pas de variables pour vous. À moins que vous n'utilisiez un préprocesseur comme Sass.

Les préprocesseurs comme Sass vendent l'utilisation des variables comme un gros avantage. Une raison de les essayer. Et vous savez quoi ? C'est une raison vraiment très bonne.

Le web évolue rapidement. Et je suis heureux de vous annoncer que **CSS supporte enfin les variables**.

Bien que les préprocesseurs supportent beaucoup plus de fonctionnalités, l'ajout des variables CSS est une bonne chose. Cela rapproche le web encore plus de l'avenir.

Dans ce guide, je vais vous montrer comment les variables fonctionnent nativement en CSS, et comment vous pouvez les utiliser pour vous faciliter la vie.

### Ce que vous allez apprendre

Je vais d'abord vous guider à travers les bases des variables CSS. Je crois que toute tentative décente de comprendre les variables CSS doit commencer ici.

Apprendre les fondamentaux, c'est bien. Ce qui est encore mieux, c'est d'appliquer ces fondamentaux pour construire des applications réelles.

Je vais donc conclure en vous montrant comment construire 3 projets qui mettent en avant les variables CSS et leur facilité d'utilisation. Voici un aperçu rapide de ces 3 projets.

#### Projet 1 : Créer des variations de composants en utilisant les variables CSS

Vous construisez peut-être déjà des variations de composants aujourd'hui. Que vous utilisiez React, Angular ou Vue, les variables CSS rendront ce processus plus simple.

![Image](https://cdn-media-1.freecodecamp.org/images/r-nxpw6nKfFcP2qKc1kazVf-I73jUwFtSEBW)
_Création de variations de composants en utilisant les variables CSS_

Consultez le projet sur [Codepen](https://codepen.io/ohansemmanuel/full/PQYzvv/).

#### Projet 2 : Styles de thème avec les variables CSS

Vous avez probablement déjà vu cela quelque part. Je vais montrer à quel point les variables CSS facilitent la création de styles de thème pour l'ensemble du site.

![Image](https://cdn-media-1.freecodecamp.org/images/bgLNFnk5dAvvsgFM1nOQgu0Atr2zBGHEDwl7)
_Styles de thème pour l'ensemble du site en utilisant les variables CSS_

Consultez le projet sur [Codepen](https://codepen.io/ohansemmanuel/full/xYKgwE/).

#### Projet 3 : Construire le CSS Variable Booth ?

C'est le projet final. Ne vous souciez pas du nom. Je n'ai pas pu trouver un meilleur nom.

![Image](https://cdn-media-1.freecodecamp.org/images/wgeg31Oo2VNWSckH5knbYZHR3TwMk2xGbTLU)
_La couleur des boîtes est mise à jour dynamiquement_

Remarquez comment les couleurs des boîtes sont mises à jour dynamiquement, et comment le conteneur de boîtes est tourné dans l'espace 3D lorsque la valeur de l'entrée de type range est modifiée.

![Image](https://cdn-media-1.freecodecamp.org/images/tZSo5HlypOi0UxMK-T4Rp0QbuKpBs4nTCZqR)

Ce projet montre la facilité de mise à jour des variables CSS avec JavaScript, et les avantages réactifs que vous obtenez avec.

#### Cela va être amusant !

Passez du temps à vous amuser avec sur [Codepen](https://codepen.io/ohansemmanuel/full/EoBLgd/).

Note : L'article suppose que vous avez une bonne maîtrise de CSS. Si vous ne connaissez pas bien CSS, ou si vous souhaitez apprendre à créer des interfaces utilisateur époustouflantes, je vous recommande de suivre mon [Cours Avancé de CSS](https://bit.ly/learn_css) (cours payant incluant 85 leçons). Cet article est un extrait du cours. </Shameless plug> ?

### Pourquoi les variables sont si importantes

Si vous êtes nouveau dans l'utilisation des variables dans les préprocesseurs ou dans CSS natif, voici quelques raisons pour lesquelles les variables sont importantes.

#### **Raison #1 : Un code plus lisible**

Sans en dire beaucoup, vous pouvez rapidement voir à quel point les variables rendent le code plus lisible et plus maintenable.

#### **Raison #2 : Facilité de modification dans de grands documents**

Si vous avez toutes vos constantes enregistrées dans un fichier séparé, vous n'avez pas à parcourir des milliers de lignes de code lorsque vous souhaitez modifier une variable.

Cela devient super facile. Il suffit de le changer à un seul endroit, et voilà.

#### **Raison #3 : Vous pouvez repérer les fautes de frappe plus rapidement**

C'est une corvée de parcourir des lignes de code pour essayer de repérer une erreur. C'est encore plus ennuyeux si l'erreur était due à une simple faute de frappe. Elles sont difficiles à repérer. L'utilisation judicieuse des variables élimine ces tracas.

En fin de compte, la lisibilité et la maintenabilité sont les grands gagnants.

Grâce aux variables CSS, nous pouvons maintenant avoir cela avec CSS natif aussi.

### Définir les variables CSS

Je vais commencer par quelque chose que vous connaissez peut-être déjà : les variables en JavaScript.

Une simple variable JavaScript peut être déclarée comme suit :

```
var amAwesome;
```

et ensuite vous pouvez lui assigner une valeur comme suit :

```
amAwesome = "awesome string"
```

En CSS, une variable CSS est toute « propriété » dont le nom commence par deux tirets.

```
/* pouvez-vous repérer la variable ici ? */.block { color: #8cacea;--color: blue}
```

![Image](https://cdn-media-1.freecodecamp.org/images/FCjHzPCqE-7rA9iKu5aGF7rojUNRx-s0Tzm1)
_Les variables CSS sont également appelées « Propriétés Personnalisées »_

### Portée des variables CSS

Il y a une autre chose à laquelle je dois attirer votre attention.

Souvenez-vous qu'en JavaScript, les variables ont une portée. Elles peuvent avoir une portée `globale` ou `locale`.

Il en va de même pour les variables CSS.

Considérez l'exemple suivant :

```
:root {  --main-color: red}
```

Le sélecteur `:root` vous permet de cibler l'élément de plus haut niveau dans le DOM, ou l'arborescence du document.

Ainsi, les variables déclarées de cette manière sont en quelque sorte dans la portée globale.

Vous avez compris ?

![Image](https://cdn-media-1.freecodecamp.org/images/XjRjOOsd5x9tj7-HtCx5CxhWQqfS-Ih9brdo)
_Variables à portée locale et globale_

### Exemple 1

Supposons que vous souhaitiez créer une variable CSS qui stocke la couleur principale d'un site thématique.

Comment procéderiez-vous ?

1. Vous créez le sélecteur de portée. Utilisez `:root` pour une variable 'globale'

```
:root { }
```

2. Définissez la variable

```
:root { --primary-color: red}
```

Souvenez-vous, une variable CSS est toute « propriété » dont le nom commence par deux tirets, par exemple `--color`

C'était simple.

### Utilisation des variables CSS

Une fois qu'une variable a été définie et qu'une valeur lui a été assignée, vous pouvez l'utiliser dans une valeur de propriété.

Il y a un petit piège cependant.

Si vous venez du monde des préprocesseurs, vous devez être habitué à utiliser une variable en référençant simplement son nom. Par exemple :

```
$font-size: 20px.test {  font-size: $font-size}
```

Avec les variables CSS natives, les choses sont un peu différentes. Vous référencez une variable en utilisant la fonction `var()`.

Avec l'exemple ci-dessus, l'utilisation des variables CSS donnera ceci :

```
:root {  --font-size: 20px}.test {  font-size: var(--font-size)}
```

Assez différent.

![Image](https://cdn-media-1.freecodecamp.org/images/1AMhf-NdKdLdzxW45VtU6uwfaZjWfWcXF3wl)
_N'oubliez pas d'utiliser la fonction var_

Une fois que vous avez compris cela, vous allez commencer à aimer les variables CSS - beaucoup !

Une autre note importante est que, contrairement aux variables dans Sass (ou d'autres préprocesseurs) - où vous pouvez utiliser les variables dans de nombreux endroits, et faire des calculs comme vous le souhaitez - vous devez être prudent avec les variables CSS. Vous les aurez principalement définies comme valeurs de propriétés.

```
/* ceci est incorrect */.margin {--side: margin-top;var(--side): 20px;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/bBkez6wqzvxDXUGNyyyLdHbN4ebWs9qcCPDB)
_La déclaration est rejetée comme une erreur de syntaxe pour avoir un nom de propriété invalide_

Vous ne pouvez pas non plus faire de calculs. Vous avez besoin de la fonction CSS `calc()` pour cela. Je discuterai des exemples au fur et à mesure.

```
/* ceci est incorrect */.margin {--space: 20px * 2;font-size:  var(--space);  // pas 40px}
```

Si vous devez faire des calculs, utilisez alors la fonction calc() comme suit :

```
.margin {--space: calc(20px * 2);font-size:  var(--space);  /* égal à 40px */}
```

### Propriétés dignes de mention

Voici quelques comportements qui méritent d'être mentionnés.

#### 1. Les propriétés personnalisées sont des propriétés ordinaires, donc elles peuvent être déclarées sur n'importe quel élément.

Déclarez-les sur un élément de paragraphe, une section, un aside, la racine, ou même des pseudo-éléments. Ils fonctionneront comme prévu.

![Image](https://cdn-media-1.freecodecamp.org/images/EOJ56i9qnkGPl1-I19u3TILcrJq8Ma-5R99s)
_Ils se comportent comme des propriétés normales_

#### 2. Les variables CSS sont résolues avec les règles normales d'héritage et de cascade

Considérez le bloc de code suivant :

```
div {  --color: red;}div.test {  color: var(--color)}div.ew {  color: var(--color)}
```

Comme pour les variables normales, la valeur `--color` sera héritée par les divs.

![Image](https://cdn-media-1.freecodecamp.org/images/g-kAkNulNHQGkMd9vst3XuTG5kvoJJ2IfVff)

#### 3. Les variables CSS peuvent être rendues conditionnelles avec `@media` et d'autres règles conditionnelles

Comme pour les autres propriétés, vous pouvez changer la valeur d'une variable CSS dans un bloc `@media` ou d'autres règles conditionnelles.

Par exemple, le code suivant change la valeur de la variable, gutter sur les appareils plus grands.

```
:root { --gutter: 10px }@media screen and (min-width: 768px) {    --gutter: 30px}
```

![Image](https://cdn-media-1.freecodecamp.org/images/IFwkEmf33YCyC19hjtMZwPgwA3VnwKR6bgvG)
_Bit utile pour le design réactif_

#### 4. Les variables CSS peuvent être utilisées dans l'attribut style du HTML.

Vous pouvez choisir de définir la valeur de vos variables en ligne, et elles fonctionneront toujours comme prévu.

```
<!--HTML--><html style="--color: red"><!--CSS-->;body {  color: var(--color)}
```

![Image](https://cdn-media-1.freecodecamp.org/images/bZgNRz8ZoSoLMcWPcmPnivMx8p7035cx6p5E)
_Définir les variables en ligne_

Les variables CSS sont sensibles à la casse. Faites attention à cela. Je m'épargne le stress et j'écris les variables en minuscules. Votre expérience peut différer.

```
/* ceci sont deux variables différentes */:root { --color: blue;--COLOR: red;}
```

### Résolution des déclarations multiples

Comme pour les autres propriétés, les déclarations multiples sont résolues avec la cascade standard.

Voyons un exemple :

```
/* définir les variables */:root { --color: blue; }div { --color: green; }#alert { --color: red; }/* utiliser la variable */* { color: var(--color); }
```

Avec les déclarations de variables ci-dessus, quelle sera la couleur des éléments suivants ?

```
<;p>Quelle est ma couleur ?</p><div>et moi ?</div><div id='alert'>  Quelle est ma couleur aussi ?  <p>couleur ?</p></div>
```

Pouvez-vous le déterminer ?

Le premier paragraphe sera `blue`. Il n'y a pas de définition directe de `--color` sur un sélecteur `p`, donc il hérite de la valeur de `:root`

```
:root { --color: blue; }
```

Le premier `div` sera `green`. C'est assez clair. Il y a une définition directe de la variable sur le `div`

```
div { --color: green; }
```

Le `div` avec l'ID `alert` ne sera PAS vert. Il sera `red`

```
#alert { --color: red; }
```

L'ID a une portée de variable directe. Ainsi, la valeur dans la définition remplacera les autres. Le sélecteur `#alert` est plus spécifique.

Enfin, le `p` dans le `#alert` sera... `red`

Il n'y a pas de déclaration de variable sur l'élément de paragraphe. Vous auriez pu vous attendre à ce que la couleur soit `blue` en raison de la déclaration sur l'élément `:root`.

```
:root { --color: blue; }
```

Comme pour les autres propriétés, les variables CSS sont héritées. La valeur est héritée du parent, `#alert`

```
#alert { --color: red; }
```

![Image](https://cdn-media-1.freecodecamp.org/images/65xpwkEjRm90CKZEWAbaX66cCHdl46xWr32C)
_La solution au Quiz_

### Résolution des dépendances cycliques

Une dépendance cyclique se produit de la manière suivante :

1. Lorsqu'une variable dépend d'elle-même. C'est-à-dire qu'elle utilise un `var()` qui se réfère à elle-même.

```
:root {  --m: var(--m)}body {  margin: var(--m)}
```

2. Lorsque deux variables ou plus se réfèrent l'une à l'autre.

```
:root {  --one: calc(var(--two) + 10px);  --two: calc(var(--one) - 10px);}
```

Faites attention à ne pas créer de dépendances cycliques dans votre code.

### Que se passe-t-il avec les variables invalides ?

Les erreurs de syntaxe sont ignorées, mais les substitutions `var()` invalides reviennent par défaut à la valeur initiale ou héritée de la propriété en question.

Considérez ce qui suit :

```
:root { --color: 20px; }p { background-color: red; }p { background-color: var(--color); }
```

![Image](https://cdn-media-1.freecodecamp.org/images/ExHNombXi1ObmK5sc8WtbTSttIJ7MNGujbZP)

Comme prévu, `--color` est substitué dans `var()` mais la valeur de la propriété, `background-color: 20px` est invalide après la substitution. Puisque `background-color` n'est pas une propriété héritable, la valeur reviendra à sa valeur `initiale` de `transparent`.

![Image](https://cdn-media-1.freecodecamp.org/images/tdeD7sLFRUvKCdXP2Y6SXuQCakTcv-hV5PNR)

Notez que si vous aviez écrit `background-color: 20px` sans aucune substitution de variable, la déclaration de fond particulière aurait été invalide. La déclaration précédente aurait alors été utilisée.

![Image](https://cdn-media-1.freecodecamp.org/images/24FLLWAoCML1VC4G95GQ1IGLQnPuwoJ2AoGA)
_Le cas est différent lorsque vous écrivez la déclaration vous-même_

### Soyez prudent lors de la création de jetons uniques

Lorsque vous définissez la valeur d'une propriété comme indiqué ci-dessous, le `20px` est interprété comme un seul jeton.

```
font-size: 20px
```

Une façon simple de le dire est que la valeur `20px` est considérée comme une seule « entité ».

Vous devez être prudent lorsque vous créez des jetons uniques avec des variables CSS.

Par exemple, considérons le bloc de code suivant :

```
:root { --size: 20}div {  font-size: var(--size)px /*INCORRECT*/}
```

Vous auriez pu vous attendre à ce que la valeur de `font-size` donne `20px`, mais c'est incorrect.

Le navigateur interprète cela comme `20 px`

Notez l'espace après le `20`

Ainsi, si vous devez créer des jetons uniques, faites en sorte qu'une variable représente le jeton entier. Par exemple, `--size: 20px`, ou utilisez la fonction `calc` par exemple `calc(var(--size) * 1px)` où `--size` est égal à `20`

Ne vous inquiétez pas si vous ne comprenez pas encore cela. Je l'expliquerai plus en détail dans un exemple à venir.

### Construisons des choses !

Maintenant, voici la partie de l'article que nous attendions.

Je vais vous guider à travers des applications pratiques des concepts discutés en construisant quelques projets utiles.

Commençons.

### Projet 1 : Créer des variations de composants en utilisant les variables CSS

Considérez le cas où vous devez construire deux boutons différents. Même style de base, juste une petite différence.

![Image](https://cdn-media-1.freecodecamp.org/images/Em6yJKVwIi9tjgjAw6vbF1Ci5H4ARS0A9acL)

Dans ce cas, les propriétés qui diffèrent sont la `background-color` et la `border-color` de la variante.

Alors, comment feriez-vous cela ?

Voici la solution typique.

Créez une classe de base, disons `.btn` et ajoutez les classes de variante. Voici un exemple de balisage :

```
<button class="btn">Bonjour</button><button class="btn red">Bonjour</button>
```

`.btn` contiendrait les styles de base du bouton. Par exemple :

```
.btn {  padding: 2rem 4rem;  border: 2px solid black;  background: transparent;  font-size: 0.6em;  border-radius: 2px;}
```

```
/* au survol */.btn:hover {  cursor: pointer;  background: black;  color: white;}
```

Alors, où intervient la variante ?

Ici :

```
/* variations */.btn.red {  border-color: red}.btn.red:hover {  background: red}
```

Vous voyez comment nous dupliquons le code ici et là ? C'est bien, mais nous pourrions l'améliorer avec les variables CSS.

Quelle est la première étape ?

Substituez les couleurs variables avec des variables CSS, et n'oubliez pas d'ajouter des valeurs par défaut pour les variables !

```
.btn {   padding: 2rem 4rem;   border: 2px solid var(--color, black);   background: transparent;   font-size: 0.6em;   border-radius: 2px; }
```

```
 /* au survol */  .btn:hover {  cursor: pointer;   background: var(--color, black);   color: white; }
```

Lorsque vous faites cela : `background: **var(--color, black)**` vous dites, définissez l'arrière-plan sur la valeur de la variable `--color`. Cependant, si la variable n'existe pas, utilisez la valeur par défaut de `**black**`

C'est ainsi que vous définissez les valeurs de variable par défaut. Tout comme vous le faites en JavaScript ou dans tout autre langage de programmation.

Voici la bonne partie.

Avec les variantes, vous fournissez simplement la nouvelle valeur de la variable CSS comme suit :

```
.btn.red {   --color: red }
```

C'est tout. Maintenant, lorsque la classe `.red` est utilisée, le navigateur note la valeur différente de la variable `--color`, et met immédiatement à jour l'apparence du bouton.

C'est vraiment bien si vous passez beaucoup de temps à construire des composants réutilisables.

Voici une comparaison côte à côte :

![Image](https://cdn-media-1.freecodecamp.org/images/gmEzlvRN7KiaDVWEy2ZUE7kI5a5PpAAJs3gU)
_Sans variables CSS VS avec variables CSS_

Oh, et si vous aviez plus de variantes, vous venez de vous épargner beaucoup de frappe supplémentaire.

![Image](https://cdn-media-1.freecodecamp.org/images/OUyVLhYwkveuuaSbIAG8QHoo0cgNtqPrqWhi)
_Voyez la différence ??_

### Projet 2 : Sites à thème avec les variables CSS

Je suis sûr que vous en avez déjà rencontré. Les sites à thème donnent à l'utilisateur l'impression de personnalisation. Comme s'ils étaient en contrôle.

Voici l'exemple de base que nous allons construire.

![Image](https://cdn-media-1.freecodecamp.org/images/LsBPxBoN-bc9PZorRq39kklAE5yTiSmkgm6I)

Alors, à quel point les variables CSS facilitent-elles cela ?

Nous allons y jeter un coup d'œil.

Juste avant cela, je voulais mentionner que cet exemple est assez important. Avec cet exemple, je vais introduire le concept de mise à jour des variables CSS avec JavaScript.

C'est amusant !

Vous allez adorer ça.

### Ce que nous voulons vraiment faire.

La beauté des variables CSS est leur nature réactive. Dès qu'elles sont mises à jour, toute propriété ayant la valeur de la variable CSS est également mise à jour.

Conceptuellement, voici une image qui explique le processus concernant l'exemple en question.

![Image](https://cdn-media-1.freecodecamp.org/images/OmRYAlINfOHcYWrLDzBJfjJkI6ejbsg5Tstc)
_Le processus_

Nous avons donc besoin de JavaScript pour l'écouteur de clic.

Pour cet exemple simple, l'arrière-plan et la couleur du texte de toute la page sont basés sur des variables CSS.

Lorsque vous cliquez sur l'un des boutons ci-dessus, ils définissent la variable CSS sur une autre couleur. En conséquence, l'arrière-plan de la page est mis à jour.

Hé, c'est tout ce qu'il y a à faire.

Euh, une dernière chose.

Lorsque je dis que la variable CSS est définie sur une autre valeur, comment cela se fait-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/UIQ3ij9Cy-iU3rO5OXkQc1uyPhMPGuHD1zXb)
_Définir la variable en ligne_

Les variables CSS prendront effet même si elles sont définies en ligne. Avec JavaScript, nous obtenons le document racine, et nous définissons la nouvelle valeur pour la variable CSS en ligne.

Vous avez compris ?

C'est beaucoup de paroles — faisons la vraie chose.

### Le balisage initial

Le balisage initial nécessaire est le suivant :

```
<div class="theme">  <button value="dark">dark</button>  <button value="calm">calm</button>  <button value="light">light</button></div><article>...</article>
```

Le balisage se compose de trois boutons dans un élément parent `.theme`. Pour garder les choses courtes, j'ai tronqué le contenu de l'élément `article`. Dans cet élément `article` se trouve le contenu de la page.

### Styliser la page

Le succès de ce projet commence par le style de la page. L'astuce est simple.

Au lieu de simplement définir la `background-color` et la `color` de la page de manière fixe, nous allons les définir en fonction de variables.

Voici ce que je veux dire.

```
body {  background-color: var(--bg, white);  color: var(--bg-text, black)}
```

La raison en est assez évidente. Chaque fois qu'un bouton est cliqué, nous allons changer la valeur des deux variables dans le document.

Lors de ce changement, le style global de la page sera mis à jour. Facile comme bonjour.

![Image](https://cdn-media-1.freecodecamp.org/images/lbU62-myh4lQakl9DoOYEaetbRLhPt4NZP01)

Alors, allons-y et gérons la mise à jour depuis JavaScript.

#### Entrer dans le JavaScript

Je vais vous donner tout le JavaScript nécessaire pour ce projet.

```
const root = document.documentElement const themeBtns = document.querySelectorAll('.theme > button')themeBtns.forEach((btn) => {  btn.addEventListener('click', handleThemeUpdate)})function handleThemeUpdate(e) {  switch(e.target.value) {    case 'dark':       root.style.setProperty('--bg', 'black')      root.style.setProperty('--bg-text', 'white')      break    case 'calm':        root.style.setProperty('--bg', '#B3E5FC')       root.style.setProperty('--bg-text', '#37474F')      break    case 'light':      root.style.setProperty('--bg', 'white')      root.style.setProperty('--bg-text', 'black')      break  }}
```

Ne vous laissez pas effrayer par cela. C'est beaucoup plus facile que vous ne le pensez probablement.

Tout d'abord, gardez une référence à l'élément racine, `const root = document.documentElement`

L'élément racine ici est l'élément `HTML`. Vous verrez pourquoi c'est important dans un instant. Si vous êtes curieux, il est nécessaire de définir les nouvelles valeurs des variables CSS.

Gardez également une référence aux boutons, `const themeBtns = document.querySelectorAll('.theme > button')

`querySelectorAll` produit une structure de données de type tableau sur laquelle nous pouvons boucler. Itérez sur chacun des boutons et ajoutez un écouteur d'événement à chacun, au clic.

Voici comment :

```
themeBtns.forEach((btn) => {  btn.addEventListener('click', handleThemeUpdate)})
```

Où est la fonction `handleThemeUpdate` ? Je vais en discuter ensuite.

Chaque bouton cliqué aura la fonction `handleThemeUpdate` comme fonction de rappel. Il devient important de noter quel bouton a été cliqué et ensuite d'effectuer la bonne opération.

À cet effet, un opérateur `switch` est utilisé, et certaines opérations sont effectuées en fonction de la valeur du bouton cliqué.

Allez-y et jetez un deuxième coup d'œil au bloc de code JavaScript. Vous le comprendrez beaucoup mieux maintenant.

### Projet 3 : Construire le CSS Variable Booth ?

Au cas où vous l'auriez manqué, voici ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/IgKvTxKSenWIErNZ4Im96FCV65MJPaf4qfad)

Souvenez-vous que la couleur des boîtes est mise à jour dynamiquement, et que le conteneur de boîtes est tourné dans l'espace 3D lorsque la valeur de l'entrée de type range est modifiée.

![Image](https://cdn-media-1.freecodecamp.org/images/UZNu2ymN0vI2VH4en9NLaJ4T22l8UEWnPi2i)

Vous pouvez aller de l'avant et jouer avec sur [Codepen](https://codepen.io/ohansemmanuel/full/EoBLgd/).

C'est un exemple superbe de mise à jour des variables CSS avec JavaScript et de la réactivité qui en découle.

Voyons comment construire cela.

#### Le balisage

Voici les composants nécessaires.

1. Une entrée de type range
2. Un conteneur pour contenir les instructions
3. Une section pour contenir une liste d'autres boîtes, chacune contenant des champs de saisie

![Image](https://cdn-media-1.freecodecamp.org/images/FHA6xhsFiPCoGpBB5VLcKzoggivesElFAkWQ)

Le balisage se révèle simple.

Le voici :

```
<main class="booth">  <aside class="slider">    <label>Déplacez ceci ? </label>    <input class="booth-slider" type="range" min="-50" max="50" value="-50" step="5"/>  </aside>    <section class="color-boxes">    <div class="color-box" id="1"><input value="red"/></div>    <div class="color-box" id="2"><input/></div>    <div class="color-box" id="3"><input/></div>    <div class="color-box" id="4"><input/></div>    <div class="color-box" id="5"><input/></div>    <div class="color-box" id="6"><input/></div>  </section>  <footer class="instructions">    ?? Déplacez le curseur<br/>    ?? Écrivez n'importe quelle couleur dans les boîtes rouges   </footer></main>  
```

Voici quelques points à noter.

1. L'entrée de type range représente des valeurs de `-50` à `50` avec une valeur de pas de `5`. De plus, la valeur de l'entrée de type range est la valeur minimale, `-50`.
2. Si vous n'êtes pas sûr du fonctionnement de l'entrée de type range, consultez-la sur [w3schools](https://www.w3schools.com/jsref/dom_obj_range.asp).
3. Notez comment la section avec la classe `.color-boxes` contient d'autres conteneurs `.color-box`. Dans ces conteneurs se trouvent des champs de saisie.
4. Il est peut-être utile de mentionner que la première entrée a une valeur par défaut de rouge.

Ayant compris la structure du document, allez-y et stylisez-le comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/pY28lnZFx4xvar807GegIg4HIn4DNcBAG5rE)

1. Sortez les conteneurs `.slider` et `.instructions` du flux du document. Positionnez-les de manière absolue.
2. Donnez à l'élément `body` une couleur de fond de lever de soleil et garnissez l'arrière-plan avec une fleur dans le coin inférieur gauche.
3. Positionnez le conteneur `color-boxes` au centre.
4. Stylisez le conteneur `color-boxes`.

Occupons-nous de ces tâches.

Ce qui suit réglera la première tâche.

```
/* Slider */.slider,.instructions {  position: absolute;  background: rgba(0,0,0,0.4);  padding: 1rem 2rem;  border-radius: 5px}.slider {  right: 10px;  top: 10px;}.slider > * {  display: block;}/* Instructions */.instructions {  text-align: center;  bottom: 0;  background: initial;  color: black;}
```

L'extrait de code n'est pas aussi complexe que vous le pensez. J'espère que vous pouvez le lire et le comprendre. Sinon, laissez un commentaire ou tweetez.

Styliser le `body` est un peu plus impliqué. Espérons que vous comprenez bien le CSS.

Puisque nous aspirons à styliser l'élément avec une couleur de fond et une image de fond, il est peut-être préférable d'utiliser la propriété raccourcie `background` pour définir plusieurs fonds.

Le voici :

```
body {  margin: 0;  color: rgba(255,255,255,0.9);  background: url('http://bit.ly/2FiPrRA') 0 100%/340px no-repeat, var(--primary-color);  font-family: 'Shadows Into Light Two', cursive;}
```

La partie `url` est le lien vers la fleur de lever de soleil.

La série de propriétés suivante `0 100%` représente la position de fond de l'image.

Voici une illustration de la façon dont le positionnement de fond CSS fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/4rZugtEKFeay00FsfDXFuXyiHA1Amf1iG2Jd)
_De : [le guide avancé de CSS](http://bit.ly/learn_css" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/zFcuuEu5RnrGWiG5Doqg7jS4OS-PyOh7H93v)
_De : [le guide avancé de CSS](http://bit.ly/learn_css" rel="noopener" target="_blank" title=")_

La partie suivante après la barre oblique représente la `background-size`. Celle-ci a été définie à `340px`. Si vous la rendiez plus petite, l'image serait également plus petite.

`no-repeat`, vous pouvez deviner ce que cela fait. Cela empêche le fond de se répéter.

Enfin, tout ce qui vient après la virgule est une deuxième déclaration de fond. Cette fois, nous avons seulement défini la `background-color` à `var(primary-color)`

Oups, c'est une variable.

L'implication de cela est que vous devez définir la variable. Voici comment :

```
:root {  --primary-color: rgba(241,196,15 ,1)}
```

La couleur primaire là est la couleur jaune du lever de soleil. Pas de gros problème. Nous allons définir quelques variables supplémentaires là bientôt.

Maintenant, centrons le `color-boxes`

```
main.booth {  min-height: 100vh;    display: flex;  justify-content: center;  align-items: center;}
```

Le conteneur principal agit comme un conteneur flex et positionne correctement l'enfant direct au centre de la page. Cela se trouve être notre conteneur `color-box` bien-aimé.

Rendons le conteneur `color-boxes` et ses éléments enfants jolis.

Tout d'abord, les éléments enfants :

```
.color-box {  padding: 1rem 3.5rem;  margin-bottom: 0.5rem;  border: 1px solid rgba(255,255,255,0.2);  border-radius: 0.3rem;  box-shadow: 10px 10px 30px rgba(0,0,0,0.4); }
```

Cela fera l'affaire. Il y a une belle ombre ajoutée aussi. Cela nous donnera quelques effets sympas.

Ce n'est pas tout. Stylisons le conteneur global `color-boxes` :

```
/* Color Boxes */.color-boxes {  background: var(--secondary-color);  box-shadow: 10px 10px 30px rgba(0,0,0,0.4);  border-radius: 0.3rem;    transform: perspective(500px) rotateY( calc(var(--slider) * 1deg));  transition: transform 0.3s}
```

Oh mon Dieu !

Il y a beaucoup de choses là-dedans.

Permettez-moi de le décomposer.

Voici la partie simple :

```
.color-boxes {   background: var(--secondary-color);   box-shadow: 10px 10px 30px rgba(0,0,0,0.4);   border-radius: 0.3rem;}
```

Vous savez ce que cela fait, n'est-ce pas ?

Il y a une nouvelle variable là-dedans. Cela devrait être pris en charge en l'ajoutant au sélecteur root.

```
:root {  --primary-color: rgba(241,196,15 ,1);  --secondary-color: red;}
```

La couleur secondaire est rouge. Cela donnera au conteneur un fond rouge.

Maintenant, la partie qui vous a probablement confus :

```
/* Color Boxes */.color-boxes {  transform: perspective(500px) rotateY( calc(var(--slider) * 1deg));  transition: transform 0.3s}
```

Pour un moment, nous pourrions simplifier la valeur de la propriété transform ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/JzclULDPJ-fDazCDnHaBt2Jw72HQAY3k0AjK)

Par exemple :

```
transform: perspective(500px) rotateY( 30deg);
```

La propriété transform raccourcie applique deux fonctions différentes. L'une, la perspective, et l'autre, la rotation le long de l'axe Y.

Hmmm, alors quel est le problème avec les fonctions `perspective` et `rotateY` ?

La fonction perspective() est appliquée à un élément qui est transformé dans l'espace 3D. Elle active l'espace tridimensionnel et donne de la profondeur à l'élément le long de l'axe z.

Vous pouvez en lire plus sur la fonction perspective sur [codrops](https://tympanus.net/codrops/css_reference/transform/#section_perspective).

La fonction `rotateY`, quel est le problème avec celle-ci ?

Après l'activation de l'espace 3D, l'élément a les plans x, y, z. La fonction `rotateY` fait tourner l'élément le long du plan `Y`.

Le diagramme suivant de [codrops](https://tympanus.net/codrops/css_reference/transform/#section_rotate3d) est vraiment utile pour visualiser cela.

![Image](https://cdn-media-1.freecodecamp.org/images/nlm073Uq9QmQYLaA2A78IbeDQqMuT9qvq00n)
_[Codrops](https://tympanus.net/codrops/css_reference/transform/#section_rotate3d" rel="noopener" target="_blank" title=")_

J'espère que cela a dissipé une partie de la confusion.

Retour à notre point de départ.

![Image](https://cdn-media-1.freecodecamp.org/images/PnEnAMTI0LRrJ2ZKbF3cs70AkNdIcSEuAYDP)

Lorsque vous déplacez le curseur, savez-vous quelle fonction affecte la rotation du `.container-box` ?

C'est la fonction rotateY qui est invoquée. La boîte est tournée le long de l'axe Y.

Puisque la valeur passée dans la fonction rotateY sera mise à jour via JavaScript, la valeur est représentée avec une variable.

![Image](https://cdn-media-1.freecodecamp.org/images/UAI2w26oH2IgBTljbP6GgDjQEzljccawUiz4)

Alors, pourquoi multiplier la variable par 1deg ?

En règle générale, et pour une liberté explicite, il est conseillé, lors de la création de jetons uniques, de stocker des valeurs dans vos variables sans unités.

Vous pouvez les convertir en n'importe quelle unité que vous souhaitez en effectuant une multiplication via la fonction `calc`.

![Image](https://cdn-media-1.freecodecamp.org/images/YmWMuiiZ8yvGpy6WHWlmquGbDGGBez4muwSN)

Cela vous permet de faire « ce que vous voulez » avec ces valeurs lorsque vous les avez. Vous voulez les convertir en `deg` ou en ratio de la vue de l'utilisateur `vw`, vous pouvez faire ce que vous voulez.

Dans ce cas, nous convertissons le nombre pour avoir un degré en multipliant la valeur « nombre » par 1deg

![Image](https://cdn-media-1.freecodecamp.org/images/gXw20rbptib1kLg0FpxSEsrIKOZGlECgESrn)

Puisque CSS ne comprend pas les mathématiques, vous devez passer cette arithmétique dans la fonction calc pour qu'elle soit correctement évaluée par CSS.

Une fois cela fait, nous sommes prêts à partir. La valeur de cette variable peut être mise à jour en JavaScript autant que nous le souhaitons.

Maintenant, il ne reste qu'un peu de CSS.

Le voici :

```
/* Gérer les couleurs pour chaque boîte de couleur */.color-box:nth-child(1) {  background: var(--bg-1)}.color-box:nth-child(2) {  background: var(--bg-2)}.color-box:nth-child(3) {  background: var(--bg-3)}.color-box:nth-child(4) {  background: var(--bg-4)}.color-box:nth-child(5) {  background: var(--bg-5)}.color-box:nth-child(6) {  background: var(--bg-6)}
```

Alors, qu'est-ce que ce vaudou ?

Tout d'abord, le sélecteur nth-child sélectionne chacune des boîtes enfants.

![Image](https://cdn-media-1.freecodecamp.org/images/WWzkEOGXTgxkDGkCJSYbgkPEtyHEEezhesXT)

Un peu de prévoyance est nécessaire ici. Nous savons que nous allons mettre à jour la couleur de fond de chaque boîte. Nous savons également que cette couleur de fond doit être représentée par une variable pour qu'elle soit accessible via JavaScript. N'est-ce pas ?

Nous pourrions aller de l'avant et faire ceci :

```
.color-box:nth-child(1) {  background: var(--bg-1)}
```

Facile.

Il y a un problème cependant. Si cette variable n'est pas présente, que se passe-t-il ?

Nous avons besoin d'un fallback.

Cela fonctionne :

```
.color-box:nth-child(1) {  background: var(--bg-1, red)}
```

Dans ce cas particulier, j'ai choisi de NE PAS fournir de fallbacks.

Si une variable utilisée dans une valeur de propriété est invalide, la propriété prendra sa valeur initiale.

Par conséquent, lorsque `--bg-1` est invalide ou NON disponible, le fond reviendra à sa valeur initiale de transparent.

Les valeurs initiales font référence aux valeurs d'une propriété lorsqu'elles ne sont pas explicitement définies. Par exemple, si vous ne définissez pas la `background-color` d'un élément, elle reviendra par défaut à `transparent`

Les valeurs initiales sont en quelque sorte des valeurs de propriété par défaut.

### Écrivons un peu de JavaScript

Il y a très peu de choses à faire du côté JavaScript.

Tout d'abord, occupons-nous du curseur.

Nous avons juste besoin de 5 lignes pour cela !

```
const root = document.documentElementconst range = document.querySelector('.booth-slider')// lorsque la valeur de la plage du curseur change, faites quelque chose range.addEventListener('input', handleSlider)function handleSlider (e) {  let value = e.target.value   root.style.setProperty('--slider', value)}
```

C'était facile, n'est-ce pas ?

Permettez-moi de l'expliquer au cas où je vous aurais perdu.

Tout d'abord, gardez une référence à l'élément curseur, `const range = document.querySelector('.booth-slider')`

Mettez en place un écouteur d'événement pour lorsque la valeur de l'entrée de type range change, `range.addEventListener('input', handleSlider)`

Écrivez le rappel, `handleSlider`

```
function handleSlider (e) {  let value = e.target.value   root.style.setProperty('--slider', value)}
```

![Image](https://cdn-media-1.freecodecamp.org/images/0PtXkLeMkuwE0mJxuJX3T0emkunPARGxRN8T)

`root.style.setProperty('--slider', value)` dit, obtenez l'élément `root` (HTML), prenez son style, et définissez une propriété dessus.

### Gestion des changements de couleur

C'est aussi facile que de gérer le changement de valeur du curseur.

Voici comment :

```
const inputs = document.querySelectorAll('.color-box > input')
```

```
// lorsque la valeur dans l'entrée change, faites quelque chose.inputs.forEach(input => {  input.addEventListener('input', handleInputChange)})function handleInputChange (e) {  let value = e.target.value  let inputId = e.target.parentNode.id   let inputBg = `--bg-${inputId}`   root.style.setProperty(inputBg, value)}
```

Gardez une référence à toutes les entrées de texte, `const inputs = document.querySelectorAll('.color-box > input')

Mettez en place un écouteur d'événement sur toutes les entrées :

```
inputs.forEach(input => {   input.addEventListener('input', handleInputChange)})
```

Écrivez la fonction `handleInputChange` :

```
function handleInputChange (e) {  let value = e.target.value  let inputId = e.target.parentNode.id   let inputBg = `--bg-${inputId}`   root.style.setProperty(inputBg, value)}
```

![Image](https://cdn-media-1.freecodecamp.org/images/HX4X1oDSyXAJGMEeV2oIKX8PBbunS4i0sngB)

Ouf...

C'est tout !

Le projet est terminé.

### Comment ai-je pu manquer cela ?

J'avais terminé et édité le premier jet de cet article lorsque j'ai remarqué que je n'avais mentionné nulle part la compatibilité des navigateurs. Alors, laissez-moi corriger mon erreur.

La compatibilité des navigateurs pour les variables CSS (alias propriétés personnalisées) n'est pas mauvaise du tout. Elle est assez bonne, avec un support décent sur tous les navigateurs modernes (plus de 87 % au moment de la rédaction de cet article).

![Image](https://cdn-media-1.freecodecamp.org/images/4ycpka14Kg2tCJLF6y3b0Zc-XHWCvbwOayAB)
_[caniuse](https://caniuse.com/#search=css%20var" rel="noopener" target="_blank" title=")_

Alors, pouvez-vous utiliser les variables CSS en production aujourd'hui ? Je dirais oui ! Assurez-vous de vérifier vous-même le taux d'adoption, cependant.

Du bon côté, vous pouvez utiliser un préprocesseur comme [Myth](http://www.myth.io). Il pré-traiter votre CSS « futur » en quelque chose que vous utilisez aujourd'hui. Plutôt cool, non ?

Si vous avez de l'expérience avec [postCSS](http://postcss.org), c'est également un excellent moyen d'utiliser le CSS futur aujourd'hui. Voici un [module postCSS pour les variables CSS](https://www.npmjs.com/package/postcss-css-variables).

C'est tout. J'ai terminé ici.

### Oups, mais j'ai des questions !

![Image](https://cdn-media-1.freecodecamp.org/images/ofZP6Nh0aCZOu6yWtDYs9HROStLDrUOgH97D)

[Obtenez l'Ebook](https://gum.co/lwaUh) pour une lecture hors ligne, et obtenez également une invitation **privée** sur Slack où vous pouvez me poser n'importe quelle question.

C'est un bon marché, non ?

À plus tard ! ?