---
title: Comment remplacer des liens dans un texte par des balises d'ancrage avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-28T10:26:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-replace-links-in-a-text-with-anchor-tags-using-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/23.-modify-links-in-strings.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment remplacer des liens dans un texte par des balises d'ancrage avec
  JavaScript
seo_desc: 'By Dillion Megida

  When you make a post on social media, and that post contains links, you would see
  the links styled differently from other text. How can you achieve this?

  For example, here''s a tweet I made on Twitter


  The text for my tweet is:


  hi g...'
---

Par Dillion Megida

Lorsque vous publiez sur les réseaux sociaux et que votre publication contient des liens, vous remarquez que ces liens sont stylisés différemment du reste du texte. Comment pouvez-vous obtenir ce résultat ?

Par exemple, voici un tweet que j'ai publié sur Twitter :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-199.png)

Le texte de mon tweet est :
> hi good morning
> 
> my website is dillionmegida.com and you can also find me on youtube here youtube.com/@deeecode
> 
> thank youuu

Il y a deux liens ici : **dillionmegida.com** et **youtube.com/@deeecode**. Et comme vous pouvez le voir dans le tweet, ces liens sont stylisés différemment (en bleu) par rapport aux autres textes (en blanc). De plus, lorsque vous cliquez sur l'un de ces liens, le navigateur se dirige vers la bonne destination.

Que se passe-t-il ici ?

Ces liens sont remplacés par des éléments d'ancrage qui sont également stylisés, ce qui rend leur apparence et leur comportement différents des autres textes.

Alors, comment pouvez-vous réaliser cela avec JavaScript ? Une façon de faire est de remplacer les liens dans une chaîne de caractères par des éléments d'ancrage et d'intégrer la chaîne modifiée dans le DOM.

Commençons par apprendre comment remplacer des liens dans une chaîne de caractères.

J'ai une [version vidéo de ce sujet](https://youtu.be/ADQ_UvfiYLk) que vous pouvez également consulter.

## La méthode String.replace()

La méthode `replace` des chaînes de caractères vous permet de remplacer des sous-chaînes par de nouveaux caractères. Cette méthode renvoie la nouvelle chaîne contenant le remplacement. Voici un exemple d'utilisation de cette méthode :

```js
const str = "J'aime JavaScript"
const updatedStr = str.replace("JavaScript", "Python")

console.log(updatedStr)
// "J'aime Python"
```

Dans cet exemple, nous avons remplacé "JavaScript" par "Python".

Pour la sous-chaîne à remplacer, vous pouvez utiliser un motif de chaîne littérale (comme nous l'avons vu ci-dessus) ou une expression régulière.

Voici un exemple avec une expression régulière :

```js
const str = "Ses mots de passe sont 345543, 995533 et 884499"
const regex = /\d+/g

const updatedStr = str.replace(regex, "******")

console.log(updatedStr)
// "Ses mots de passe sont ******, ****** et ******"
```

Ici, nous spécifions une expression régulière qui correspond à un ou plusieurs chiffres.

## La méthode String.replace() avec une fonction de rappel

Pour l'argument de remplacement, vous pouvez spécifier soit une chaîne (comme nous l'avons vu dans les exemples précédents), soit une fonction de rappel. L'intérêt d'une fonction de rappel est que vous pouvez récupérer la sous-chaîne correspondante et l'utiliser dans votre remplacement.

Utilisons l'exemple précédent :

```js
const str = "Ses mots de passe sont 345543, 995533 et 884499"
const regex = /\d+/g

const updatedStr = str.replace(regex, function(matched) {
  const firstChar = matched[0]
  const lastChar = matched.at(-1)
  
  return firstChar + "****" + lastChar
})

console.log(updatedStr)
// "Ses mots de passe sont 3****3, 9****3 et 8****9"
```

Comme vous pouvez le voir ici, en utilisant une fonction de rappel comme argument, je suis capable de capturer la sous-chaîne correspondante et d'utiliser le premier et le dernier caractère de cette sous-chaîne dans mon remplacement.

Vous pouvez en apprendre davantage sur ce concept [dans cet article](https://www.freecodecamp.org/news/how-to-pass-callback-functions-to-string-replace-javascript/)

## Remplacer des liens dans une chaîne de caractères

Pour remplacer un lien dans une chaîne, vous spécifiez une expression régulière qui correspond à un lien, puis vous remplacez cette sous-chaîne par un élément d'ancrage `a`. L'élément d'ancrage aura l'attribut `href` et le contenu textuel correspondant à la sous-chaîne. De plus, l'élément d'ancrage peut avoir une classe que vous pourriez utiliser dans votre feuille de style pour changer son apparence.

Regardons un exemple. Disons que nous avons la chaîne de caractères de l'exemple Twitter :

```js
const str = `hi good morning

my website is dillionmegida.com and you can also find me on youtube here youtube.com/@deeecode

thank youuu`
```

J'utilise des accents graves (backticks) pour pouvoir écrire la chaîne sur plusieurs lignes.

Ensuite, notre expression régulière pour correspondre à la chaîne :

```js
const linkRegex = /(https?\:\/\/)?(www\.)?[^\s]+\.[^\s]+/g
```

C'est une expression régulière de base pour les liens.

Expliquer en détail le fonctionnement de cette expression régulière dépasse le cadre de cet article, mais pour faire simple : cette expression régulière correspond aux sous-chaînes qui commencent (ou non) par "https://", suivies (ou non) par "www", suivies de certains caractères, suivies d'un point, puis de nouveau suivies de certains caractères. Ainsi, ce motif correspondra à "https://google.com", "http://www.google.com", "google.io", et ainsi de suite.

Vous pouvez améliorer cette expression de plusieurs façons, par exemple en ne spécifiant que les domaines acceptés, car ce motif correspondra également à "google.wrong". Ce n'est pas le sujet de cet article, alors continuons avec le motif de base que nous avons.

Maintenant, définissons la fonction de rappel :

```js
function replacer(matched) {
  let withProtocol = matched
  
  if(!withProtocol.startsWith("http")) {
    withProtocol = "http://" + matched
  }
 
  const newStr = `<a
    class="text-link"
    href="${withProtocol}"
  >
    ${matched}
  </a>`
  
  return newStr
}
```

Cette méthode `replacer` prendra chaque sous-chaîne correspondante comme argument. Tout d'abord, nous vérifions si la sous-chaîne commence par "http", et si ce n'est pas le cas, nous ajoutons le protocole au début de la chaîne et l'assignons à la variable `withProtocol`.

Ensuite, nous avons une variable `newStr`, à laquelle nous assignons une chaîne. Cette chaîne contient un élément d'ancrage HTML avec une classe `text-link`, un `href` avec la valeur de `withProtocol` et le contenu textuel est `matched`.

Maintenant, récupérons la chaîne modifiée :

```js
const modifiedStr = str.replace(linkRegex, replacer)

console.log(modifiedStr)
// "hi good morning

// my website is <a
//   class='text-link'
//   href='http://dillionmegida.com'
// >
//   dillionmegida.com
// </a> and you can also find me on youtube here <a
//   class='text-link'
//   href='http://youtube.com/@deeecode'
// >
//   youtube.com/@deeecode
// </a>

// thank youuu"
```

Comme vous le voyez dans cette chaîne modifiée, les liens ont été remplacés par des balises d'ancrage. Maintenant, ajoutons cela au DOM. Supposons que nous ayons le HTML suivant :

```html
<div id='text-target'>
</div>
```

Nous pouvons maintenant utiliser du code dans notre fichier JavaScript pour intégrer `modifiedStr` dans cet élément :

```js
const textTarget = document.getElementById('text-target')

textTarget.innerHTML = modifiedStr
```

Ajoutons également quelques styles dans notre fichier CSS :

```css
#text-target {
  font-size: 20px;
  padding: 20px;
}

.text-link {
  color: orange;
  font-weight: bold;
  margin-right: 2px;
}
```

Voici le résultat que nous obtenons sur notre navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-200.png)

Comme vous pouvez le voir, les liens dans la chaîne sont remplacés par l'élément d'ancrage et stylisés exactement comme nous le souhaitions. De plus, lorsque vous cliquez sur le lien, vous êtes dirigé vers l'URL.

Vous pouvez vérifier cela en direct [sur ce projet Codepen](https://codepen.io/Dillion/pen/gOddxPG).

## Conclusion

De nombreuses plateformes de réseaux sociaux utilisent ce concept où les liens dans une chaîne ont une apparence et un comportement différents du reste du texte. Ces différences indiquent qu'il s'agit d'un lien.

Comme nous l'avons vu dans cet article, nous avons réalisé cela avec la méthode `replace`, une fonction de rappel `replacer`, et en l'intégrant dans le DOM.

Vous pouvez utiliser cette approche de différentes manières pour modifier l'apparence de vos chaînes de caractères.

Si vous avez apprécié cet article, n'hésitez pas à le partager :)