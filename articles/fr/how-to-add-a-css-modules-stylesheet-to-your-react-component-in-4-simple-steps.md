---
title: Comment ajouter une feuille de style CSS Modules à votre composant React en
  4 étapes simples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-28T13:03:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-css-modules-stylesheet-to-your-react-component-in-4-simple-steps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca135740569d1a4ca4d4a.jpg
tags:
- name: CSS
  slug: css
- name: CSS Modules
  slug: css-modules
- name: React
  slug: react
seo_title: Comment ajouter une feuille de style CSS Modules à votre composant React
  en 4 étapes simples
seo_desc: 'By Holly Atkinson

  Let’s say you’d like to add a CSS Modules Stylesheet to your project. You can find
  Create React App’s guidance here, but essentially — and as the guidance states — CSS
  Modules let you use the same CSS selector in different files wit...'
---

Par Holly Atkinson

Disons que vous souhaitez ajouter une feuille de style CSS Modules à votre projet. Vous pouvez trouver les [conseils](https://facebook.github.io/create-react-app/docs/adding-a-css-modules-stylesheet) de Create React App ici, mais essentiellement — et comme le mentionnent les conseils — les CSS Modules vous permettent d'utiliser le _même_ sélecteur CSS dans différents fichiers sans vous soucier des conflits de noms. Cela fonctionne parce que chaque élément HTML dans votre fichier que vous souhaitez styliser reçoit automatiquement un nom de classe _unique_.

Cela peut sembler assez confus au début, mais en réalité, le processus pour implémenter les CSS Modules peut être simplifié en seulement 4 étapes, comme démontré dans l'exemple ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_lmno_4nmNyohGa-gM_GaEw.jpeg)
_Oui, vraiment !_

### Ajout de CSS modulaire à un simple composant <Link />

1. Une caractéristique de React est que les CSS Modules sont "activés" pour les fichiers se terminant par l'extension `.module.css`. Créez le fichier CSS avec un nom de fichier spécifique au format suivant :

```bash
Link.module.css
```

2. Importez le style dans votre composant :

```jsx
import styles from '../styling/components/Link.module.css'
```

3. Les styles dans votre fichier CSS peuvent suivre votre convention de nommage préférée, par exemple :

```css
.bold {  font-weight: bold;}
```

4. Le style est appliqué à l'élément HTML comme suit :

```jsx
className={styles.bold}
```

Et c'est tout !

_Crédit photo :_ [_Adrian Swancar_](https://unsplash.com/photos/72El6N0cmj4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) _sur_ [_Unsplash_](https://unsplash.com/search/photos/confused?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)