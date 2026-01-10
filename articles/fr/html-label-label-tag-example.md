---
title: HTML Label – Exemple de balise Label
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-03T16:37:47.000Z'
originalURL: https://freecodecamp.org/news/html-label-label-tag-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/label.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: HTML Label – Exemple de balise Label
seo_desc: 'You use the HTML <label> tag to caption form controls. <label> is an inline
  element – meaning it doesn''t take up an entire line unless you put a break tag
  before it.

  By definition, form controls refer to the elements inside a form element.

  Examples o...'
---

Vous utilisez la balise HTML `<label>` pour légender les contrôles de formulaire. `<label>` est un élément en ligne – ce qui signifie qu'il n'occupe pas une ligne entière sauf si vous placez une balise de saut avant.

Par définition, les contrôles de formulaire font référence aux éléments à l'intérieur d'un élément de formulaire.

Les exemples de contrôles de formulaire incluent `<input type="text"/>`, `<input type="number"/>`, `<input type="radio"/>`, `<input type="checkbox"/>`, `<textarea></textarea>`, `<button></button>` et ainsi de suite.

L'avantage ultime de l'étiquetage d'un contrôle de formulaire est que le contrôle de formulaire est lié à l'étiquette. Cela signifie que l'utilisateur n'a pas à cliquer uniquement sur l'entrée avant qu'elle ne devienne active.

Lier une étiquette à un contrôle de formulaire aide également les utilisateurs malvoyants car un lecteur d'écran lira toujours l'étiquette lorsque l'entrée est focalisée.

Dans cet article, je vais vous montrer comment utiliser la balise `<label>` pour que vous puissiez améliorer vos projets de manière unique.

## Comment utiliser la balise `<label>`

Il existe 2 façons d'utiliser la balise `<label>` :

- en tant qu'élément autonome en liant un contrôle de formulaire à celui-ci avec l'attribut for
- en l'enveloppant autour du contrôle de formulaire

Si vous l'utilisez en tant qu'élément autonome, vous devez le connecter au contrôle de formulaire en attribuant la même valeur à l'attribut `for` du label et à l'attribut `id` du contrôle de formulaire.

De plus, l'utilisateur n'aura pas à focaliser le contrôle de formulaire uniquement en cliquant dessus. S'ils cliquent sur l'étiquette, le contrôle devient également focalisé. C'est un plus pour l'expérience utilisateur.

Voici comment cela fonctionne :
```html
<form>
      <label for="name"> Nom : </label>
      <input type="text" id="name" />
</form>
```
![label](https://www.freecodecamp.org/news/content/images/2022/02/label.gif)

Ce CSS rend la page un peu meilleure :

```css
body {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      height: 100vh;
      background-color: #cacaca;
    }
```

Si vous l'enveloppez autour d'un contrôle de formulaire, vous n'avez pas besoin des attributs `for` et `id`. Dans ce cas, l'entrée et l'étiquette sont associées implicitement.

Cela fonctionne comme suit :
```html
<form>
      <label>
        Nom :
        <input type="text" />
      </label>
</form>
```
![label](https://www.freecodecamp.org/news/content/images/2022/02/label.gif)

**P.S. :** Si les valeurs de l'attribut `for` du label et de l'attribut `id` du contrôle de formulaire ne sont pas les mêmes, le contrôle de formulaire ne sera pas focalisé lorsque le label est cliqué.

## Conclusion

Dans cet article, vous avez appris à utiliser la balise `label` de la bonne manière car c'est une partie essentielle de l'expérience utilisateur et de l'accessibilité.

Avec un étiquetage correct, vous pouvez toujours créer un formulaire que vos utilisateurs seront heureux de remplir.

Merci d'avoir lu.