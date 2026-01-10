---
title: Comment convertir des nombres arabes en chiffres romains avec SolidJS
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2023-03-08T20:52:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-arabic-numbers-to-roman-numerals-with-solidjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Arabic_to_Roman_Converter_-_Mihail_Gaberov.gif
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment convertir des nombres arabes en chiffres romains avec SolidJS
seo_desc: 'Have you heard about the Romans? Who hasn’t, right 🙂

  They used their own numeric system, which was a bit of a mouthful, especially when
  it came to writing. It looks like this: I, II, III, IV, V, VI and so on.

  Maybe that’s one of the reasons that peo...'
---

Avez-vous entendu parler des Romains ? Qui n'en a pas entendu parler, n'est-ce pas 642

Ils utilisaient leur propre système numérique, qui était un peu compliqué, surtout lorsqu'il s'agissait d'écrire. Cela ressemble à ceci : **I, II, III, IV**, **V**, **VI** et ainsi de suite.

Peut-être que c'est l'une des raisons pour lesquelles les gens ont adopté et commencé à utiliser le système numérique arabe. C'est celui que nous connaissons tous et utilisons au quotidien. Oui, oui, le même – 1, 2, 3… et ainsi de suite.

## **Que construisons-nous ?**

Dans ce tutoriel, nous verrons comment construire une petite application qui donne à l'utilisateur une entrée pour saisir des nombres arabes et affiche leur équivalent en chiffres romains avec une belle animation élégante.

Nous utiliserons [SolidJS](https://www.solidjs.com/) pour construire l'interface utilisateur et le bon vieux [JavaScript](https://developer.mozilla.org/en-US/docs/Web/javascript) pour implémenter l'algorithme de conversion proprement dit. Plus d'informations à ce sujet plus tard dans l'article.

Nous profiterons également de [CSS Modules](https://css-tricks.com/css-modules-part-1-need/) et de [SASS](https://sass-lang.com/) pour rendre notre application un peu plus agréable à l'œil.

## Dépôt GitHub et projet de démonstration

4caSi vous souhaitez sauter la lecture, [ici](https://github.com/mihailgaberov/arabic-roman-visualized/) 481 se trouve le dépôt GitHub, et ici vous pouvez voir la démonstration en direct [demo](https://arabic-roman-visualized.vercel.app/) 4fa.

## Qu'est-ce que SolidJS ?

![Image](https://www.freecodecamp.org/news/content/images/2023/03/logo.png align="left")

SolidJS est une bibliothèque front-end pour créer des interfaces utilisateur réactives. Elle est encore relativement nouvelle. Elle ressemble beaucoup à [React](https://beta.reactjs.org/), mais on dit qu'elle est [plus simple et plus rapide](https://www.webtips.dev/solidjs-vs-react).

Elle a récemment attiré mon attention, alors j'ai décidé de l'examiner plus en détail et de me former. Et, bien sûr, de partager mon expérience avec vous ici.

## Le projet

Notre application est vraiment simple. Elle a seulement quelques dépendances et ne contient que plusieurs composants. Permettez-moi de vous les présenter brièvement.

### Dépendances

```json
{
  "devDependencies": {
    "vite": "^4.1.1",
    "vite-plugin-solid": "^2.5.0"
  },
  "dependencies": {
    "@motionone/solid": "^10.15.5",
    "@solid-primitives/keyed": "^1.1.8",
    "sass": "^1.58.3",
    "solid-js": "^1.6.10"
  }
}
```

Outre la dépendance évidente – `solid-js` – j'ai seulement installé les bibliothèques `sass`, `@motionone/solid` et `@solid-primitives/keyed`. Nous les utiliserons pour le style et les animations. Les packages liés à [Vite](https://vitejs.dev/) viennent avec l'installation de l'application SolidJS, ce qui signifie que lorsque vous exécutez ceci :

`npx degit solidjs/templates/js my-app`

Cela installera tout ce dont vous avez besoin pour exécuter initialement votre nouvelle application SolidJS.

### Structure du projet

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Untitled.png align="left")

*Structure du projet*

Peut-être que les personnes ayant une expérience avec React verront immédiatement à quel point cela ressemble à une application React régulière. Nous avons la même organisation de fichiers/dossiers. Et oui, nous pouvons utiliser JSX avec Solid également.

Après avoir vu la structure de la nouvelle application Solid, plongeons dans les composants de base qui proviennent de la bibliothèque et dont nous avons besoin pour construire l'interface utilisateur.

### Composants

Les composants dans Solid sont, surprise surprise 632, des fonctions JavaScript régulières. Une application Solid est composée de ces fonctions. Et, de la même manière que dans React, elles supportent [JSX](https://beta.reactjs.org/learn/writing-markup-with-jsx). Cela signifie que nous pouvons écrire des fonctions qui produisent des éléments DOM.

Par exemple, voici à quoi ressemble notre composant [Logo](https://github.com/mihailgaberov/arabic-roman-visualized/tree/main/src/components/Logo) :

```jsx
import styles from './Logo.module.scss';
import gameLogo from '../../../assets/logo.png';

export function Logo() {
  return (
      <div className={styles.logo}>
          <img src={gameLogo} alt="logo" />
      </div>
  );
}
```

Oui, vous avez deviné juste. Cela produira un code HTML comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-1.png align="left")

*Composant Logo (HTML)*

Peut-être que certains d'entre vous se demandent déjà « Allez, Mihail, tu plaisantes ? Quelle est la différence entre Solid et React ? » et je suis d'accord. Jusqu'à présent, tout semble à peu près identique. Parlons maintenant des Signaux.

### Signaux SolidJS

![Image](https://www.freecodecamp.org/news/content/images/2023/03/SolidJS-Create-Signal-Component-2-1270x762.jpeg align="left")

*Signal SolidJS*

Les signaux sont la base de la réactivité dans Solid. Ils contiennent des valeurs qui changent avec le temps et mettent à jour tout ce qui utilise ces valeurs. Ce qui signifie que si vous changez la valeur d'un signal, ce changement sera propagé partout ailleurs dans votre application où il est utilisé.

C'est quelque chose qui manque dans le monde React. Au moins en nom.

Lorsqu'un signal est créé, il vous donne deux fonctions, un getter et un setter. Vous utilisez la première pour obtenir la valeur actuelle contenue dans le signal. Et la fonction setter est utilisée pour changer cette valeur. La syntaxe est la suivante :

```jsx
const [count, setCount] = createSignal(0)
```

La valeur que vous passez en argument à `createSignal` est la valeur initiale qui sera détenue par le signal, 0 dans ce cas. Cela signifie que si vous appelez `count()` sans avoir appelé `setCount` avec une valeur différente avant cela, le résultat que vous obtiendrez sera ce zéro.

Maintenant que vous avez vu comment l'utiliser et quel est son but, vous pensez peut-être à son équivalent dans React, `useState`. Dans mon cas, c'était l'association initiale qui m'est venue à l'esprit. Les soi-disant signaux sont des moyens de gérer l'état dans une application Solid. Comme il vous donne un moyen facile d'y accéder et de le changer.

## L'algorithme

Il existe plusieurs implémentations de cet algorithme. Et dans de nombreux langages de programmation différents. Seul un moteur de recherche Google peut dire combien 913.

Nous allons l'implémenter en JavaScript. Je garde le fichier contenant l'algorithme séparé, dans un répertoire appelé [lib](https://github.com/mihailgaberov/arabic-roman-visualized/tree/main/lib). Cette approche nous permet de changer facilement l'interface utilisateur, par exemple, avec une bibliothèque d'interface utilisateur différente. Ou peut-être l'utiliser dans un contexte complètement différent. C'est-à-dire que le `frontend` et le `backend` de notre application sont totalement découplés.

Commençons par examiner l'algorithme lui-même, puis nous pourrons discuter des améliorations possibles.

### Étapes de l'algorithme

Tout d'abord, laissez-moi présenter le code ici pour que ce soit plus facile à suivre :

```javascript
export const convertArabicToRoman = function (num) {
	const rules = {
		"M": 1000,
		"CM": 900,
		"D": 500,
		"CD": 400,
		"C": 100,
		"XC": 90,
		"L": 50,
		"XL": 40,
		"XXX": 30,
		"XX": 20,
		"X": 10,
		"IX": 9,
		"V": 5,
		"IV": 4,
		"I": 1
	}
	
	let res = "";
	const romans = Object.keys(rules);

	for (let i = 0; i < romans.length; ++i) {
		const val = rules[romans[i]];
		
		while (num >= val) {
			num -= val;
			res += romans[i];
		}
	}
	return res;
};
```

Ensuite, examinons les règles qui définissent comment les chiffres romains sont créés.

Ces règles vous permettent d'écrire n'importe quel nombre :

* Si un chiffre plus petit vient après un chiffre plus grand, ajoutez le chiffre plus petit au chiffre plus grand.

* Si un chiffre plus petit vient avant un chiffre plus grand, soustrayez le chiffre plus petit du chiffre plus grand.

* N'utilisez pas le même symbole plus de trois fois de suite.

* L'usage moderne emploie sept symboles, chacun avec une valeur entière fixe :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-57.png align="left")

En gardant à l'esprit ces règles, voici quelques exemples :

* 399 en chiffres romains est **CCCXCIX**

* 151 en chiffres romains est **CLI**

* 185 en chiffres romains est **CLXXXV**

* 3070 en chiffres romains est **MMMLXX**

* 570 en chiffres romains est **DLXX**

* 7 en chiffres romains est **VII**

* 290 en chiffres romains est **CCXC**

* 1880 en chiffres romains est **MDCCCLXXX**

* 47 en chiffres romains est **XLVII**

**Passons maintenant en revue notre solution étape par étape :** 3a2.

1. Créez une structure de données qui contiendra les représentations des nombres connus à partir des règles. Dans notre cas, il s'agit d'un simple objet JavaScript.

2. Ajoutez quelques nombres connus supplémentaires qui nous aideront dans les calculs ultérieurs, c'est-à-dire 4, 9, 20, 30, 40, 90, 400 et 900.

3. Créez une chaîne vide qui contiendra le résultat.

4. Utilisez ensuite la méthode Object.keys() pour obtenir tous les chiffres romains de notre structure.

5. Parcourez-les via une boucle for.

6. Pour chaque lettre de chiffre romain, obtenez son équivalent arabe et vérifiez s'il est inférieur ou égal au nombre que nous convertissons.

7. Si c'est le cas, soustrayez-le d'abord du nombre que nous convertissons, puis stockez la représentation romaine actuelle dans la chaîne `res` en la concaténant avec ce qui s'y trouve déjà.

8. Après que les deux boucles se terminent, retournez le résultat final dans notre variable de chaîne.

Après avoir défini les étapes de l'algorithme, prenons un exemple spécifique et passons-le à travers elles pour que ce soit plus clair.

### Exemple

D'accord, prenons un nombre aléatoire et passons-le à notre algorithme. Disons le nombre **1293**. Nous sauterons les étapes de **préparation** et irons directement là où la vraie magie se produit. Ce qui signifie que nous commençons par obtenir les chiffres romains qui sont les clés de notre structure de données clé-valeur :

```python
	const romans = Object.keys(rules); // ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "XXX", "XX", "X", "IX", "V", "IV", "I"]
```

Cela résulte en un tableau contenant les représentations des chiffres romains que nous avons là. Cela nous permet de les parcourir via la boucle **for** et d'accéder à chacun d'eux à chaque cycle.

Ensuite, ayant accès à chaque chiffre romain de ce tableau, nous obtenons sa valeur :

```javascript
const val = rules[romans[i]]; // Premier cycle cela donnera 1000, 900 dans le second, et ainsi de suite
```

Nous avons donc le nombre 1293 comme notre entrée, que nous avons nommé `num`. Dans la boucle interne **while**, nous comparons l'entrée avec la valeur actuellement sélectionnée (de la structure de données `rules`) et si elle est plus grande ou égale, nous la soustrayons de notre valeur d'entrée. Ensuite, nous concaténons la lettre du chiffre romain à notre résultat de chaîne.

Dans notre exemple, cela signifierait ce qui suit :

```python
Est-ce que 1293 >= 1000 > oui => num = 1293 - 1000 = 293 et res = 'M'
```

Ensuite, nous continuons à itérer avec la valeur de résultat de l'itération précédente.

```python
Est-ce que 293 >= 1000 => non => 293 >= 900 => non => 293 >= 500 => non
=> 293 >= 400 => non => 293 >= 100 => oui => 293 - 100 = 193
et res = 'MC'
```

```python
Est-ce que 193 >= 100 => oui => 193 - 100 = 93 et res = 'MCC'
```

```python
Est-ce que 93 >= 100 => non => 93 >= 90 => oui => 93 - 90 = 3 et res = 'MCCXC'
```

```python
Est-ce que 3 >= 90 => non => 3 >= 50 => non => 3 >= 40 => non => 3 >= 30 => non => 3 >= 20
=> non => 3 >= 10 => non => 3 >= 9 => non => 3 >= 5 => non => 3 >= 4 => non => 3 >= 1
=> oui => 3 - 1 = 2 et res = 'MCCXCI'
```

```python
Est-ce que 2 >= 1 => oui => 2 - 1 = 1 et res = 'MCCXCII'
```

et enfin

```python
Est-ce que 1 >= 1 => oui => 1 - 1 = 0 et res = 'MCCXCIII' est le résultat final ! 389389389
```

### Comment améliorer le processus

Une chose importante à mentionner ici. Si nous utilisons l'algorithme directement tel quel, il pourrait consommer n'importe quel nombre que nous lui passons. Mais, en gardant à l'esprit les règles mentionnées ci-dessus, la chaîne de résultat pourrait devenir très longue. Cela pourrait casser l'interface utilisateur ou, au minimum, la rendre laide et inutilisable pour l'écriture.

C'est pourquoi certaines implémentations parlent d'ajouter plus de lettres aux règles. Comme le montre le tableau ci-dessous, nous pourrions avoir des lettres signifiant des nombres plus grands. L'ajout de cela à l'algorithme réduirait considérablement la longueur de la chaîne de résultat lorsqu'un nombre plus grand est ajouté.

Par exemple, avec notre implémentation actuelle, si nous entrons 1 000 000, le résultat serait 1000 fois la lettre M. Vous pouvez l'imaginer, c'est une longue chaîne de M, comme MMMMMMMM_…_ Mais, si nous introduisons des lettres supplémentaires pour des nombres plus grands, cela deviendra simplement la lettre M avec une ligne au-dessus, comme le montre le tableau ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Untitled-2.png align="left")

*Amélioration possible en utilisant plus de lettres. Source : par* [*https://www.calculateme.com/roman-numerals/to-roman*](https://www.calculateme.com/roman-numerals/to-roman)

## Conclusion

Une autre session d'apprentissage par le partage se termine ici 389.

Nous avons atteint deux objectifs principaux dans ce tutoriel. Tout d'abord, nous avons abordé un acteur relativement nouveau sur le marché des bibliothèques front-end, SolidJS. Nous nous sommes familiarisés avec ses éléments de base. Nous avons compris comment les utiliser pour construire rapidement une interface utilisateur décente. Et nous avons réussi à utiliser cette interface utilisateur pour montrer le fonctionnement de notre algorithme.

Et deuxièmement, nous avons abordé l'algorithme lui-même. Nous avons vu comment nous pouvons l'implémenter en JavaScript. Nous comprenons également les limitations de cette approche et les améliorations possibles. Par exemple, vous pouvez ajouter plus de lettres pour signifier les nombres plus grands. Cela pourrait facilement supprimer notre limite supérieure. Et au lieu de 4999, nous pourrions aller sans limite.

La dernière chose que je voudrais dire ici est, comme toujours, merci pour la lecture 64f3ffb, j'espère que cela a été amusant et intéressant pour vous !

### Références :

* [Documentation SolidJS](https://www.solidjs.com/)