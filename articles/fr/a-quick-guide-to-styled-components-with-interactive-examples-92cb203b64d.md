---
title: Un guide rapide sur les Styled Components avec des exemples interactifs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-27T00:54:43.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-styled-components-with-interactive-examples-92cb203b64d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Iqjo47QeVFf2kb9-SAxh8Q.jpeg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un guide rapide sur les Styled Components avec des exemples interactifs
seo_desc: 'By Maciej Nowakowski

  “That’s interesting…” I thought when I first read about styled-components. And then
  I went right back to my tried-and-tested React components.

  But then Max Stoiber, the co-creator of styled-components, showed us his new library
  a...'
---

Par Maciej Nowakowski

« C'est intéressant… » me suis-je dit lorsque j'ai lu pour la première fois à propos de styled-components. Et puis je suis retourné à mes composants React éprouvés.

Mais ensuite, [Max Stoiber](https://twitter.com/mxstbr), le co-créateur de styled-components, nous a présenté sa nouvelle bibliothèque lors du [React in Flip Flops coding bootcamp](https://www.codecamps.com/riff1/). « C'est intéressant » s'est transformé en « C'est incroyable ! »

Je pouvais à peine contenir mon excitation. J'avais enfin compris le concept derrière styled-components. Cela a ouvert tant de nouvelles possibilités pour styliser les composants. Cela a simplifié la façon de structurer les applications web. Et cela a renforcé la cohérence dans le style des applications React.

### Tout a commencé avec les littéraux de gabarit étiquetés

Vous pourriez penser que je suis un peu vieux jeu, mais je crois que si vous voulez vraiment comprendre une idée, vous devez vous familiariser avec les concepts sous-jacents. Nous pourrions plonger directement dans les styled components. Mais d'abord, découvrons ce qui a suscité la curiosité de Max et [Glen](https://twitter.com/glenmaddern) avant qu'ils ne commencent le projet et ne construisent réellement styled-components.

Les littéraux de gabarit d'ES6 simplifient la façon dont vous pouvez mélanger des variables et du texte. Si vous prenez deux variables : `name` et `mood`, avec les valeurs assignées « Alice » et « happy » respectivement, le littéral de gabarit :

```
const sentence = `${name} is ${mood}.`;
```

produira une phrase : « Alice is happy. »

Les littéraux de gabarit étiquetés vont plus loin dans la syntaxe.

Les étiquettes sont des fonctions JavaScript. Mais il y a deux différences essentielles par rapport aux fonctions régulières :

* les fonctions d'étiquette sont appelées en utilisant la notation des backticks au lieu des parenthèses. Dans l'exemple ci-dessous, nous appelons la fonction `greetingTag` en enveloppant les arguments dans des backticks :

```
greetingTag`${name} is ${mood}.`;
```

* JavaScript traite le littéral de gabarit — tout ce qui se trouve entre les backticks — comme des arguments de fonction. Dans la première étape, JavaScript transforme le littéral de gabarit en un tableau de chaînes. Les chaînes sont suivies par les variables extraites. Si nous prenons l'exemple ci-dessus, les arguments transformés passés à la fonction `greetingTag` ressembleront à ceci :

```
["", " is ", "."], name, mood
```

Le premier argument, un tableau, contient toutes les chaînes que nous avons placées avant, entre et après les variables `name` et `mood`. Dans notre exemple, la première chaîne est vide car il n'y a rien avant `name`. Les deux arguments suivants, `name` et `mood`, ont été extraits du littéral de gabarit en tant que variables.

Maintenant, la fonction `greetingTag` peut appliquer n'importe quelle logique au tableau de textes et aux variables `name` et `mood` et retourner le résultat souhaité.

Créons une fonction d'étiquette, `greetingTag`, qui prendra trois arguments : un tableau `texts`, une variable `name` et une variable `mood`. Et voici la logique qu'elle utilisera : si la valeur de `mood` est « happy », elle retournera une phrase de salutation régulière. Dans tous les autres cas, elle retournera la version encourageante de la salutation :

```
const greetingTag = (texts, name, mood) => {   if (mood === 'happy') {     return `Hi ${name}!`;   } else {     return `Hi ${name}, you are awesome!`;   } } const greeting = greetingTag`${name} is ${mood}.`;
```

Maintenant, si nous assignons « Alice » à `name` et « happy » à `mood`, la fonction `greetingTag` retournera : « Hi Alice! ». Si nous changeons la valeur de `mood` en un autre mot que « happy » — disons « excited » ou « cat » — `greetingTag` retournera : « Hi Alice, you are awesome! ».

Mais comment pouvez-vous utiliser cette connaissance pour styliser les composants React ?

### Styled components

Cette question exacte a intrigué Max et Glenn alors qu'ils cherchaient une meilleure et plus cohérente façon de styliser les composants React. Le moment Aha! est venu lorsqu'ils ont réalisé que les littéraux de gabarit étiquetés acceptent non seulement des variables mais aussi des fonctions. Comme dans l'exemple ci-dessous :

```
const greeting = greetingTag`${ name => `Hi ${name}!` }`;
```

Ici, `greetingTag` reçoit un littéral de gabarit avec une fonction. Une fois la fonction exécutée par `greetingTag`, `greetingTag` peut appliquer une logique supplémentaire à la valeur retournée et retourner un résultat.

Les styled components sont également des fonctions d'étiquette. Mais au lieu d'accepter des motifs de salutation, ils acceptent des littéraux de gabarit qui contiennent des styles CSS. Et au lieu de phrases de salutation, ils retournent des composants React.

Permettez-moi de vous montrer comment cela fonctionne.

**Note de bas de page :** Les exemples de code ci-dessous sont interactifs. Vous pouvez jouer avec eux, ajouter des styles et changer les valeurs assignées. Vous pouvez inspecter différents fichiers en cliquant sur leurs onglets. Ou appuyez sur le bouton orange, bleu-orange ou bleu en haut pour basculer entre différentes vues.

Si vous voulez utiliser des styled components dans votre application, vous devez d'abord installer `styled-components` :

```
npm install --save styled-components
```

Ci-dessous, j'ai créé un styled component `Title` :

Le `styled.h1` est une fonction d'étiquette. Elle retourne un composant React qui est identique à celui ci-dessous :

```
import React from 'react'; const Title = ({children}) => <h1>{children}</h1>
```

La beauté de cette solution est que styled-components font le travail difficile pour vous — votre composant `Title` aura la `color` de `royalblue`.

Je sais ce que vous pensez : si nous devions écrire les styles de chaque composant de cette manière, cela ne serait pas très différent de l'écriture de classes CSS. Heureusement, les styled components sont beaucoup plus intelligents !

Imaginez que vous souhaitez garder vos en-têtes noirs la plupart du temps et ne les mettre en évidence qu'occasionnellement avec une couleur différente. Avec les styled components, nous pouvons créer un `Title` conscient de la couleur qui sera `black` par défaut et changera pour `royalblue` chaque fois que nous lui passerons une prop `primary` :

Vous pouvez passer des props au `Title` comme à n'importe quel autre composant React. Ici, le deuxième `Title` reçoit la prop `primary`. Nous pouvons accéder aux props à l'intérieur de la déclaration d'un styled component. Cela ouvre un tout nouveau monde de possibilités.

Ci-dessus, j'ai défini le styled component `Title`. Parce que les `props` sont accessibles à l'intérieur de la déclaration du styled component, nous pouvons décider de la couleur de notre composant. La fonction utilise l'opérateur ternaire et retourne `royalblue` lorsque la propriété `primary` est `true` et `black` sinon.

Vous n'avez pas à l'écrire explicitement comme dans :

```
<Title primary={true}>Hi Bob, you are awesome!&lt;/Title>
```

Passer la prop `primary` sans assignation est comme passer `primary={true}`.

Maintenant que la porte est grande ouverte, rendons notre `Title` plus universel. Parfois, vous pourriez avoir besoin que votre `Title` utilise des polices plus petites et parfois plus grandes. Parfois, vous pourriez vouloir qu'il ait un poids normal et parfois vous pourriez vouloir qu'il se distingue et lui donner un poids de police gras. Et parfois, vous pourriez vouloir le mettre en majuscules ou en lettres capitales.

Les styled components vous permettent de créer un seul composant universel. Ensuite, vous pouvez l'utiliser partout sans avoir à penser aux styles :

Dans l'exemple ci-dessus, la `font-size` est assignée à des valeurs explicites : `48px` ou `32px`. Un tel code est difficile à maintenir lorsque la base de code grandit.

### Thèmes

Lorsque vous créez un ensemble de styled components pour une utilisation ultérieure, vous voulez imposer un style cohérent dans toute l'application. Il est toujours utile de définir les règles de style. De préférence, dans un fichier séparé. Plus tard, lorsque vous devez changer les styles, au lieu de revisiter tous vos composants, vous pouvez modifier le style en un seul endroit.

Les styled components vous donnent un outil pour faire exactement cela — les thèmes.

Un `theme` est un objet JavaScript où vous pouvez définir des paramètres de style :

```
const theme = {   colors: {     primary: "royalblue",     secondary: "teal",     text: "black"   },   fontSize: {     xl: "2.4rem",     lg: "1.8rem",     md: "1.3rem",     nm: "1rem",     sm: "0.75rem"   } }
```

Le `theme` ci-dessus définit les propriétés `colors` et `fontSize`. Vous pourrez y accéder dans tous les styled components de l'application.

Mais d'abord, vous devez rendre l'application consciente du `theme`. Vous devez le passer en tant que prop au `ThemeProvider` — un composant wrapper fourni par les styled components :

```
import { ThemeProvider } from "styled-components"; import theme from "./theme.js";
```

```
const App = () => (   <ThemeProvider theme={theme}>     <div>       <Title>Hi, Alice!</Title>     &lt;/div>   </ThemeProvider> )
```

Prenons l'exemple précédent pour apprendre comment utiliser un `theme` et comment accéder à ses propriétés à l'intérieur des styled components.

Dans le `Title`, vous pouvez accéder à l'objet `theme` via `props.theme`. Par exemple, pour sélectionner la couleur du `Title`, vous vérifiez d'abord si un attribut donné a été passé au `Title` (`primary` ou `secondary`). Ensuite, vous retournez la valeur de `color` correspondante déclarée dans le `theme`. Si aucun n'a été passé, vous retournez une couleur de `text` standard.

Le `Title` peut maintenant décider également de ses tailles de police. Il vérifie d'abord si une prop `xl`, `lg`, `md` ou `sm` a été passée et — en fonction de cela — assigne une valeur appropriée à la propriété `font-size`. Si aucune prop n'a été passée, il assignera la valeur de `fontSize.nm` définie dans le `theme`.

Nous venons de créer un composant `Title` flexible. Maintenant, vous pouvez l'utiliser sans avoir à vous soucier du CSS. Vous pouvez décider de son apparence exclusivement en passant un ensemble spécifique de `props`.

### Étendre les styled-components

Créer un seul composant `Title` n'est pas suffisant. Par exemple, sur une page de blog, vous aurez besoin d'une balise `h1` pour le titre d'un article et d'une balise `h2` pour les sous-titres. Vous avez également besoin de paragraphes pour afficher du texte.

Les styled components sont facilement extensibles. Vous pouvez créer un nouveau composant `Subtitle` avec une balise `h2` et copier-coller toutes les règles de style du `Title`. Ou vous pouvez étendre le composant `Title` avec la méthode d'assistance `withComponent`. Le `Subtitle` aura toutes les propriétés d'un `Title` mais utilisera une balise `h2` :

```
const Subtitle = Title.withComponent("h2");
```

Vous pouvez étendre le `Title` pour créer le composant `Text` avec une balise `p` et — en même temps — fixer sa `color` comme `theme.text` et définir la `line-height` à `1.65`? Ici aussi, les styled-components brillent :

```
const Paragraph = Title.withComponent("p");const Text = Paragraph.extend`   color: ${props => props.theme.colors.text};   line-height: 1.65;
```

Tout d'abord, nous avons créé un composant intermédiaire `Paragraph` qui aura toutes les règles de style du `Title`. Cependant, nous utiliserons la balise `p` et ensuite le composant `Text` qui étend le `Paragraph` et définit ses propriétés `color` et `line-height`. Ci-dessous, vous pouvez inspecter le code pour les composants `Title`, `Subtitle` et `Text` :

Les styled components vous permettent d'écrire du CSS régulier en JavaScript. De plus, vous pouvez imbriquer les styles CSS et les pseudo-classes. Vous pouvez ajouter des media-queries et des attributs. Enfin, en utilisant la méthode d'assistance `injectGlobal`, vous pouvez injecter des règles de style globales et importer des polices.

### Pseudo-classes

Pour apprendre à utiliser les pseudo-classes, créons un composant `Button` qui changera de couleur lorsque nous survolerons la souris dessus.

Ci-dessus, j'ai imbriqué la pseudo-classe `&:hover` pour changer la `color` chaque fois que vous survolez la souris sur le bouton. Vous pouvez utiliser n'importe quelle pseudo-classe disponible en CSS de la même manière.

### Injection de styles globaux avec styled-components

Au lieu d'importer le fichier de styles globaux, vous pouvez utiliser l'assistant `injectGlobal` pour ajouter des styles globaux à votre application. Tout d'abord, vous devez importer l'assistant `injectGlobal` :

```
import styled, { ThemeProvider, injectGlobal } from "styled-components";
```

Dans l'exemple ci-dessous, j'utilise `injectGlobal` pour :

* importer des polices et définir la `font-family` pour tous les éléments en « Montserrat ».
* réinitialiser les marges, les remplissages et les bordures.
* changer la taille de la police de l'élément racine en utilisant la media-query pour la taille d'écran inférieure à `screen.medium` et `screen.mobile`. Les deux sont définis dans le `theme`.

Les thèmes des styled components imposent la cohérence. Pour en savoir plus, explorez l'une des meilleures documentations que j'aie jamais vues : [Styled Components Docs](https://www.styled-components.com/docs).

Grâce à la curiosité de Max et Glen, les styled components vous offrent un ensemble incroyable d'outils pour styliser les applications React. L'écosystème des styled components est en plein essor. Visitez la page [Ecosystem](https://www.styled-components.com/ecosystem) pour explorer les composants prêts à l'emploi et les systèmes de grille. Examinez les nombreux autres outils construits avec les styled components.

### Conclusion

Dans ce tutoriel, vous avez appris comment fonctionnent les littéraux de gabarit étiquetés. Vous avez également appris comment utiliser les styled components pour construire des composants React universels. Vous comprenez maintenant comment utiliser un thème pour implémenter les styles cohérents de votre prochaine application.

Les styled components sont une nouvelle façon de styliser les applications React. Dès la sortie de la boîte, les styled components :

* vous permettent de construire des composants réutilisables et universels
* imposent la cohérence du style
* vous permettent d'imbriquer les styles
* ajoutent des préfixes de fournisseur lorsque nécessaire
* sont simplement incroyables !

Si vous avez aimé cet article, ? même 50 fois — je l'apprécierais vraiment et cela fait une énorme différence pour moi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u5zyRKX71tdYC430kIpnmA.jpeg)

J'ai récemment publié un tutoriel React gratuit pour débutants. Si vous voulez apprendre à construire une application web à partir de zéro, c'est un excellent point de départ. Vous apprendrez à construire une application pour vous aider à trouver le meilleur film à regarder ? S[weet Pumpkins](https://sweetpumpkins.codecamps.com/)