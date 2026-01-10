---
title: Qu'est-ce que la compatibilité multi-navigateurs ? Comment créer des sites
  web qui fonctionnent partout
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-03-06T18:26:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-cross-browser-compatibility
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Cross-Browser.png
tags:
- name: Browsers
  slug: browsers
- name: Compatibility
  slug: compatibility
seo_title: Qu'est-ce que la compatibilité multi-navigateurs ? Comment créer des sites
  web qui fonctionnent partout
seo_desc: When building for the web, it's easy to develop tunnel vision and only build
  for yourself. You may overlook the diverse needs of your audience and focus solely
  on your preferences and how things look on your preferred browser. This can cause
  you to m...
---

Lors de la création pour le web, il est facile de développer une vision en tunnel et de ne construire que pour soi-même. Vous pouvez négliger les besoins diversifiés de votre audience et vous concentrer uniquement sur vos préférences et sur l'apparence des choses sur votre navigateur préféré. Cela peut vous faire manquer des aspects cruciaux de fonctionnalité et entraîner des problèmes de compatibilité futurs sur d'autres navigateurs. 

Dans cet article, nous allons plonger dans des stratégies pratiques pour atteindre la compatibilité multi-navigateurs, en nous concentrant sur des composants spécifiques de l'interface utilisateur comme les éléments de formulaire, les barres de défilement et les polices. Ensuite, nous discuterons de certaines bonnes pratiques générales que chaque développeur web devrait adopter.

> « Souvenez-vous que vous n'êtes pas vos utilisateurs — simplement parce que votre site fonctionne sur votre MacBook Pro ou votre Galaxy Nexus haut de gamme, cela ne signifie pas qu'il fonctionnera pour tous vos utilisateurs ! » – [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction)

## Table des matières

* [Qu'est-ce que la compatibilité multi-navigateurs ?](#heading-quest-ce-que-la-compatibilite-multi-navigateurs)
* [Problèmes courants de compatibilité multi-navigateurs et solutions](#heading-problemes-courants-de-compatibilite-multi-navigateurs-et-solutions)
* [Bonnes pratiques pour la compatibilité multi-navigateurs](#heading-bonnes-pratiques-pour-la-compatibilite-multi-navigateurs)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que la compatibilité multi-navigateurs ?

En termes simples, la compatibilité multi-navigateurs consiste à garantir que votre site web offre une expérience cohérente et de haute qualité à tous les utilisateurs, quel que soit leur choix de navigateur. 

Les navigateurs utilisent différents moteurs, donc par défaut, ils rendent les sites web différemment. Pour que vos sites web aient la même apparence et fonctionnent de la même manière, quel que soit le navigateur de l'utilisateur, il est nécessaire de comprendre les capacités uniques des navigateurs.

La compatibilité multi-navigateurs signifie qu'idéalement, un site web devrait avoir la même apparence et fonctionner de la même manière, que quelqu'un le consulte sur Chrome, Microsoft Edge et Opera (alimentés par le moteur Blink), Firefox (alimenté par le moteur Gecko) ou même Safari (alimenté par le moteur WebKit). 

### Avantages de la compatibilité multi-navigateurs :

1. Portée plus large – vos sites web sont accessibles à plus d'utilisateurs, quel que soit le navigateur qu'ils utilisent.
2. Expérience utilisateur cohérente – vos sites web ont une apparence et une fonctionnalité uniformes sur toutes les plateformes.
3. Meilleur référencement (SEO) – vos sites web obtiennent des classements plus élevés en étant plus conviviaux.

## Problèmes courants de compatibilité multi-navigateurs et solutions

![Image](https://www.freecodecamp.org/news/content/images/2024/03/browserstack.png)
_Infographie montrant les résultats de test d'une page web sur différents navigateurs. Crédit image Browserstack_

### Éléments de formulaire

L'apparence et le comportement des éléments de formulaire comme `<input>`, `<select>`, `<textarea>`, et `<button>` peuvent varier considérablement selon les navigateurs. Cela affecte à la fois l'aspect visuel et l'utilisabilité des formulaires, y compris la manière dont les utilisateurs interagissent avec eux (par exemple, en cliquant, en se concentrant et en tapant).

Par exemple, le texte de l'espace réservé dans les champs `<input>` peut apparaître plus pâle dans un navigateur et plus prononcé dans un autre, entraînant des problèmes de lisibilité. 

Pour résoudre cela :

* Utilisez CSS pour standardiser l'apparence des éléments de formulaire autant que possible.
* Pour les espaces réservés, assurez le contraste et la lisibilité sur tous les navigateurs :

```css
::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #909090;
  opacity: 1; /* Firefox */
}

input.studentid:-ms-input-placeholder { /* Microsoft Edge */
  color: #909090;
}


```

Le code CSS ci-dessus cible le texte de l'espace réservé dans les champs de saisie sur différents navigateurs, définit leur couleur sur #909090 et assure une opacité complète pour une visibilité cohérente (avec des règles spécifiques pour Microsoft Edge).

### Polices

Les polices et la typographie rencontrent plusieurs problèmes de compatibilité multi-navigateurs, allant des tailles de police par défaut variables aux différences dans les moteurs de rendu de police. Cela peut affecter le poids, l'espacement et l'apparence générale du texte.

Une police peut apparaître plus fine et plus espacée dans Chrome par rapport à Edge, affectant la lisibilité et la cohérence du design. 

Pour résoudre cela :

* Définissez une taille de police de base dans votre CSS et utilisez des unités relatives (comme `em` ou `rem`) pour la taille du texte comme montré dans le code ci-dessous. Cela aide à maintenir la scalabilité et la cohérence.

```css
html {
  font-size: 16px; /* Définir une taille de police de base */
}

body {
  font-family: 'Open Sans', sans-serif;
  line-height: 1.6;
  color: #333;
}

h1, h2, h3, p {
  margin: 2rem;;
  padding: 1.5rem;
}


```

* Lorsque vous utilisez des polices web, assurez-vous qu'elles sont chargées correctement sur tous les navigateurs en utilisant des services comme Google Fonts, qui fournissent un chargement de polices compatible multi-navigateurs :

```html
<link href="<https://fonts.googleapis.com/css?family=Open+Sans&display=swap>" rel="stylesheet">


```

* Le code ci-dessous garantit que la police 'Open Sans' a la même apparence sur notre site web, quel que soit le navigateur. Il le fait d'abord en utilisant une version de la police qui pourrait déjà être sur notre ordinateur pour charger les choses plus rapidement. Sinon, il la récupère depuis Internet mais remplace par une police par défaut en attendant que cette dernière se charge. 

```css
@font-face {
  font-family: 'Open Sans';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: local('Open Sans Regular'), local('OpenSans-Regular'), url(<https://fonts.gstatic.com/s/opensans/v15/mem8YaGs126MiZpBA-UFVZ0b.woff2>) format('woff2');
}
```

### Barres de défilement

Le style des barres de défilement a longtemps été un défi pour les développeurs web en raison du support inconstant sur différents navigateurs. Bien que des navigateurs comme Chrome, Safari et Edge aient fourni des moyens de personnaliser les barres de défilement en utilisant CSS, le niveau de support et les méthodes de mise en œuvre varient.

Les mises à jour récentes ont vu des améliorations dans la standardisation de la personnalisation des barres de défilement, la plupart des navigateurs modernes adoptant des capacités similaires. Mais il existe encore quelques différences dans l'approche :

Pour **Chrome, Edge et Firefox**, vous pouvez utiliser les propriétés CSS `scrollbar-width` et `scrollbar-color` pour personnaliser l'apparence de la barre de défilement. Ces propriétés font partie d'une norme plus récente visant à fournir une méthode plus cohérente pour styliser les barres de défilement sur les navigateurs qui la supportent.

```css
/* Pour Chrome, Firefox et Edge */
scrollbar-width: thin;
scrollbar-color: #c0c0c0 #f0f0f0;
```

**Pour Safari**, qui utilise le moteur de rendu WebKit, vous devrez utiliser le pseudo-élément `::-webkit-scrollbar` pour obtenir un style similaire. Cette méthode est spécifique aux navigateurs basés sur WebKit.

```css
/* Pour Safari */
.mostly-customized-scrollbar::-webkit-scrollbar {
  width: 5px;
  height: 8px;
  background-color: #aaa; /* ou ajoutez-le à la piste */
}

```

Le code CSS ci-dessus personnalise l'apparence des barres de défilement sur ces navigateurs en ajustant leur taille et leurs couleurs.

Mais pour une cohérence sur tous les navigateurs, vous devrez concevoir vos pages web de manière à ce que l'apparence par défaut de la barre de défilement n'affecte pas négativement votre design.

## Bonnes pratiques pour la compatibilité multi-navigateurs

![Image](https://www.freecodecamp.org/news/content/images/2024/03/best-practices.jpeg)
_Infographie montrant des outils de mesure. Crédit image Creative Bloq_

### Définir un Doctype

Commencez votre document HTML avec une déclaration `<!DOCTYPE>` pour vous assurer que le mode standard est activé. 

Cela est important car cela indique au navigateur web quelle version de HTML la page est écrite. Sans cela, les navigateurs pourraient rendre la page en "mode quirks" — où le navigateur suppose que vous avez écrit un ancien code non standard. Cela conduit finalement à des problèmes de style et de mise en page imprévisibles car les normes web modernes ne sont pas pleinement appliquées.

Une déclaration `<!DOCTYPE>` en HTML5 ressemble à ceci au tout début de votre fichier HTML :

```html
<!DOCTYPE html>
```

### Utiliser une réinitialisation CSS

Une réinitialisation CSS consiste essentiellement à ajouter un ensemble de règles qui ciblent des éléments courants pour supprimer leur style par défaut, réduisant ainsi les écarts par défaut des navigateurs. 

Différents navigateurs ont des styles inhérents différents pour les éléments HTML — marges, paddings, tailles de police, etc. Ainsi, la mise en œuvre d'une réinitialisation CSS garantit que seuls les styles que vous écrivez dans votre code prendront effet. Cela conduit à une base cohérente pour le style de votre page web sur divers navigateurs. 

Il y a des développeurs qui aiment écrire les leurs à partir de zéro. Et il y en a d'autres comme moi, qui utilisent [la réinitialisation CSS populaire et gratuite d'Eric Meyer](https://meyerweb.com/eric/tools/css/reset/) comme vous pouvez le voir dans le code ci-dessous :

```css
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
```

Il y a un autre groupe de développeurs qui utilisent [Normalize.css](https://necolas.github.io/normalize.css/), que vous pouvez installer en utilisant un gestionnaire de paquets comme npm, puis l'importer dans votre CSS.

```bash
npm install normalize.css


```

### Vérifier la prise en charge des propriétés CSS

Avant d'utiliser des fonctionnalités CSS avancées, vérifiez leur compatibilité sur des sites comme [Can I Use](https://caniuse.com/). Là, vous pouvez trouver des tableaux de compatibilité détaillés pour les fonctionnalités HTML, CSS et JavaScript sur différents navigateurs et versions. Cela devrait vous aider à prendre des décisions éclairées sur les technologies à utiliser et quand mettre en œuvre des solutions de repli.

Dans la capture d'écran ci-dessous, j'ai recherché CSS Grid et j'ai immédiatement pu voir les différents navigateurs et leurs versions qui le supportent. Ainsi, avant de mettre en œuvre CSS Grid sur ma page web, j'ai une idée des navigateurs avec lesquels il fonctionne.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-05-at-9.06.17-AM.png)
_Compatibilité des navigateurs pour CSS Grid._

### Créer des sites web réactifs 

Le monde multi-appareils dans lequel nous vivons actuellement exige que, en tant que développeurs web, nous fassions de la réactivité une priorité. 

Nous pouvons utiliser des mises en page fluides, des images flexibles et des requêtes média pour garantir que nos sites web s'adaptent à toute taille d'écran. Les effets d'entraînements de la réactivité sont la compatibilité multi-navigateurs, l'accessibilité et l'expérience utilisateur améliorée.

[Voici un article](https://www.freecodecamp.org/news/responsive-design-best-practices/) discutant de certaines bonnes pratiques pour le design réactif et comment les mettre en œuvre.

### Faire des tests multi-navigateurs

Les tests sont devenus un mot à la mode dans la programmation ces derniers temps, mais c'est parce qu'il est très important de s'assurer que le code que vous écrivez fonctionne comme prévu. 

Il ne s'agit pas seulement de vérifier si votre code TypeScript s'exécute sans problème, cependant. Même les projets web les plus simples nécessitent des tests approfondis. 

Les tests multi-navigateurs signifient essayer vos pages web sur divers navigateurs et appareils pour vous assurer qu'elles ont la même apparence et fonctionnent de manière cohérente.

## Conclusion

La compatibilité multi-navigateurs peut être un mot difficile à prononcer. Mais comme nous l'avons vu, il est essentiel de la considérer lors de la création de sites web. Et vous pouvez progressivement rendre vos sites web compatibles en testant et en ajustant votre code et en mettant en œuvre certaines des cinq bonnes pratiques que nous avons discutées ci-dessus. 

Alors, avant de tirer le rideau sur votre prochain site web ou application web, n'oubliez pas de vérifier si vos utilisateurs sur Chrome, Firefox, Safari et autres navigateurs voient et vivent les mêmes choses.

Voici quelques ressources utiles :

* [MDN Web Docs sur la compatibilité multi-navigateurs](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction)
* [Codepaper sur l'importance de la compatibilité multi-navigateurs](https://medium.com/@codepaper_/the-significance-of-cross-browser-compatibility-in-website-development-8ea2cca480dc)
* [Eric Meyer sur la réinitialisation CSS](https://meyerweb.com/eric/tools/css/reset/)