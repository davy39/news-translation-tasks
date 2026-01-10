---
title: Comment commencer avec TailwindCSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-03T17:46:38.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-tailwindcss
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c996e740569d1a4ca1fa8.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: tailwind
  slug: tailwind
- name: Web Design
  slug: web-design
seo_title: Comment commencer avec TailwindCSS
seo_desc: 'By Dillion Megida

  TailwindCSS is an awesome utility-first CSS library for creating beautiful layouts
  with less customized CSS.

  There''s a good chance you''ve heard about Tailwind. But, have you tried using it?

  In this article, I''ll share the things tha...'
---

Par Dillion Megida

TailwindCSS est une bibliothèque CSS utilitaire incroyable pour créer de belles mises en page avec moins de CSS personnalisé.

Il y a de fortes chances que vous ayez entendu parler de Tailwind. Mais l'avez-vous déjà utilisé ?

Dans cet article, je vais partager les choses qui rendent Tailwind différent des autres bibliothèques de composants que je connais. Et je vais discuter de pourquoi vous devriez commencer à l'utiliser.

**Notez que** tout ceci est mon opinion. Je ne dis pas que j'ai utilisé toutes les bibliothèques de composants du monde, lol.

## Avant TailwindCSS

...il y avait des bibliothèques de composants comme Bootstrap et Material UI, pour n'en nommer que quelques-unes. Ces bibliothèques viennent avec un ensemble de composants prédéfinis. Par exemple, le plus courant (ou entendu) est probablement `PrimaryButton`.

Ces bibliothèques réduisent la difficulté de concevoir des éléments à partir de zéro avec CSS. La plupart de ces bibliothèques font également un travail incroyable pour rendre les composants personnalisables par l'utilisateur, afin qu'ils n'aient pas à se conformer aux décisions du créateur.

Cependant, cette personnalisation implique souvent de remplacer les styles existants. Par exemple, créer de nouvelles classes pour remplacer les styles existants fournis par la bibliothèque.

Ce n'est pas un gros problème en soi (selon l'utilisateur, pour moi, c'en est un), mais vous devez toujours suivre le flux du type "Est-ce que j'aime la façon dont ceci est stylisé ? Non. Laissez-moi le remplacer".

Certains développeurs peuvent voir ces composants déjà prêts comme exactement ce dont ils ont besoin. Mais les créateurs ne peuvent pas toujours faire quelque chose de parfait pour chaque utilisateur. Heureusement, comme mentionné précédemment, ils font un excellent travail pour rendre les composants personnalisables.

## Puis vint TailwindCSS

Tailwind est une bibliothèque CSS utilitaire. Cela signifie qu'ils sont axés sur les utilitaires. Ils fournissent des classes utilitaires comme les bordures, les couleurs, les couleurs de fond, et ainsi de suite. Ils ne définissent pas nécessairement l'apparence de votre composant. Vous décidez de cela en utilisant différentes classes qu'ils fournissent.

C'est pourquoi j'aime Tailwind. Bien sûr, il est toujours possible de remplacer les styles ici, mais c'est très rare. L'équipe formidable derrière le produit a créé de nombreuses classes pour différents besoins. Sans avoir besoin de remplacer, vous pouvez configurer les styles par défaut que vous souhaitez que la bibliothèque utilise dans le fichier de configuration. Plutôt génial, non ?

Si certains de ces termes ne vous sont pas clairs pour l'instant, ne vous inquiétez pas. Nous entrerons dans plus de détails au fur et à mesure que nous avancerons dans l'article.

## Exemples de classes utilitaires

Avant de commencer à utiliser TailWindCSS, laissez-moi vous montrer quelques classes qui rendent l'outil incroyable.

- `rounded`: ajoute un `border-radius` de 0.25rem à un élément.
- `text-gray-400`: ajoute une couleur gris clair (`#cbd5e0`). 300 ajoute quelque chose de plus clair et 500, quelque chose de plus foncé.
- `bg-gray-100`: ajoute une couleur de fond gris clair (`#f7fafc`).
- `md:text-gray-100`: ajoute une requête média pour un élément de sorte que les largeurs d'écran supérieures ou égales à l'écran moyen (768px par défaut) appliquent un gris très clair (`#f7fafc`) à l'élément. Sympa, non ?
- `hover:underline`: ajoute un soulignement à un texte lorsqu'on le survole.
- `xs:text-lg`: similaire à `md..`, cela applique une requête média pour un élément de sorte qu'une taille de police de 1.125rem (par défaut) est utilisée pour un élément lorsque la largeur de l'écran est supérieure ou égale à l'écran extra petit (640px par défaut).
- `mt-20`: applique un `margin-top` de 5rem à un élément.
- `awesome-responsive`: ok, cela n'existe pas ?

Toutes ces options sont également personnalisables, bien sûr. Nous verrons cela plus tard dans cet article.

Comme vu dans les classes, elles ne déterminent pas (par elles-mêmes) l'apparence finale d'un élément ou la mise en page d'une page. C'est leur combinaison par vous, le développeur, qui détermine cela. Cela vous donne un contrôle total sans avoir à remplacer.

À ce stade, je veux croire que vous trouvez TailWindCSS incroyable, alors commençons à l'utiliser.

## Installation et configuration

[Leur documentation d'installation](https://tailwindcss.com/docs/installation/) explique le processus d'installation en détail. Pour des raisons de complétude, je vais partager les étapes d'installation ici.

### 1. Installer le package avec npm

```shell
npm install tailwindcss
```

### 2. Ajouter Tailwind à votre CSS

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
h1 {
  color: purple;
}
```

`@tailwind` n'est pas une syntaxe CSS valide. Mais, tailwind utilise ces directives (comme elles sont appelées) pour générer le CSS construit. `h1` sera également ajouté à la feuille de style tel quel.

`h1` n'est pas obligatoire. J'essayais de vous montrer que d'autres choses peuvent être ajoutées.

### 3. Créer votre fichier de configuration

Cette étape est **optionnelle**, mais elle vous permet de spécifier certaines valeurs par défaut. Avec cette configuration, tailwind générera le bon CSS. *Rappelez-vous que j'ai dit plus tôt que le remplacement serait minimal car Tailwind vous permet de configurer vos styles par défaut*.

Pour créer votre fichier de configuration, faites ceci :

```shell
npx tailwindcss init
```

`npx` car tailwind n'a pas été installé globalement. De cette façon, le package installé localement est utilisé.

Le code ci-dessus créera un fichier de configuration modèle similaire à ceci :

```js
module.exports = {
  purge: [],
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}
```

[Cette documentation](https://tailwindcss.com/docs/configuration/) explique comment configurer le fichier.

### 4. Utiliser Tailwind avec PostCSS

[PostCSS](https://github.com/postcss/postcss) aide le processus de construction de la feuille de style tailwind à produire le code CSS correct. Dans votre fichier `postcss.config.js`, ajoutez ceci :

```js
module.exports = {
  plugins: [
    // ...
    require('tailwindcss'),
    require('autoprefixer'),
    // ...
  ]
}
```

`autoprefixer` est également ajouté (un plugin de PostCSS) pour ajouter des [préfixes de fournisseurs](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix) aux propriétés.

Pour construire votre CSS, exécutez ce qui suit :

```shell
npx postcss tailwind.css -o public/style.css
```

Cela prend le fichier tailwind.css (avec les directives), et produit le contenu traité dans la feuille de style publique fournie.

Maintenant, vous êtes prêt à utiliser Tailwind.

## Comment utiliser Tailwind dans votre projet

Avec la feuille de style publique remplie, toutes les pages liées à la feuille de style peuvent utiliser les styles. Un exemple est :

```html
<div
  className='flex justify-center mt-10 items-center'
>
  <h1 className='text-xl md:text-4xl'>
    Bonjour
  </h1>
  <button
    className='bg-red-300 p-2 rounded mx-20 hover:bg-red-600 hover:text-white'
  >
    Cliquez-moi !
  </button>
  <a
    href='https://google.com'
    className='underline font-bold'
  >
    Google
  </a>
</div>
```

Voici ce que les classes font pour les éléments :

- `flex` - `display: flex`.
- `justify-center` - `justify-content: center`.
- `mt-10` - `margin-top: 2.5rem`
- `items-center` - `align-items: center`
- `text-xl` - `font-size: 1.25rem`
- `md:text-xl` - md signifie taille moyenne. La valeur par défaut est 768px mais vous pouvez la changer dans le fichier de configuration.

Voici ce que la classe fait pour vous :

  ```css
    @media only screen and (min-width:768px) {
      element {
        font-size: 1.25rem;
      }
    }
  ```

- `bg-red-300` - `background-color: #feb2b2`
- `rounded` - `border-radius: 0.25rem`
- `mx-20` - `margin-left: 5rem` et `margin-right: 5rem`
- `hover:bg-red-600` - applique une couleur de fond de `#e53e3e` sur l'état pseudo de survol.
- `hover:text-white` - applique une couleur blanche sur l'état pseudo de survol.
- `underline`: `text-decoration: underline`
- `font-bold`: `font-weight: bold`

Voici le résultat pour un écran supérieur à 768px :

![Résultat du code d'exemple pour une taille d'écran supérieure à 768px](https://www.freecodecamp.org/news/content/images/2020/08/tailwind1.png)

et pour un écran inférieur à 768px :
![Résultat du code d'exemple pour une taille d'écran inférieure à 768px](https://www.freecodecamp.org/news/content/images/2020/08/tailwind2.png)

Remarquez la différence dans l'élément `h1` ?

Cet article ne peut pas contenir toutes (ou même les plus spéciales) les fonctionnalités de Tailwind. Vous pouvez [commencer par ici](https://tailwindcss.com/docs/utility-first/) pour en apprendre plus.

## Conclusion

Voici une introduction à la belle bibliothèque Tailwind !

En résumé, TailwindCSS ne définit pas l'apparence de votre composant. Vous définissez cela en combinant plusieurs classes ensemble.

Personnellement, j'adore TailwindCSS car il me donne cette sensation de CSS vanilla (j'adore mon CSS vanilla ?) tout en simplifiant les choses pour moi.

Bien qu'il abstraie les styles pour moi, je ne suis pas entièrement ignorant de ce qui se passe. Par exemple, avec `PrimaryButton`, je ne connais pas les espacements et les couleurs qui composent ce composant. Mais avec `mt-10`, je comprends que c'est simplement `margin-top:2.5rem`.

Si vous avez des questions ou des contributions à cet article, vous pouvez me trouver sur [l'application de l'oiseau ?](https://twitter.com/iamdillion)