---
title: Comment créer des composants réutilisables avec des props dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-13T17:14:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-reusable-components-with-props-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/reusable-components-image.png
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: Comment créer des composants réutilisables avec des props dans React
seo_desc: 'By Alvin Okoro

  Props are one of the most important building blocks of React.js. When you need to
  pass data down from a parent component to a child component, props make this possible.

  In this article we''ll learn how to work with props and build reusa...'
---

Par Alvin Okoro

Les props sont l'un des éléments de construction les plus importants de React.js. Lorsque vous devez passer des données d'un composant parent à un composant enfant, les props rendent cela possible.

Dans cet article, nous allons apprendre comment travailler avec les props et créer des composants réutilisables dans React.

## Qu'est-ce que les Props dans React ?

Props est l'abréviation de properties (propriétés). Ils représentent les informations que vous souhaitez transmettre à un composant spécifique afin que ce composant puisse réutiliser ces informations.

Les informations que vous pouvez transmettre en tant que props vont de className à height, width, et bien plus encore. Cela rend très facile la création d'éléments réutilisables tels que des boutons, des cartes, des éléments d'entrée, etc.

## Comment travailler avec les Props dans React

Maintenant que vous savez ce que sont les props et le travail principal qu'ils effectuent dans les composants, il est temps de démontrer comment travailler avec les props lorsque vous créez un composant réutilisable dans React.

Supposons que vous avez une nouvelle application React ou existante, créez deux nouveaux fichiers. Nous appellerons le premier fichier **Author.jsx** et le second fichier **AuthorProfile.jsx**.

Ouvrez maintenant votre fichier "Author.jsx" et ajoutez le code suivant :

```javascript
export default function Author({name, imageUrl}){
	return (
    	<div className="author">
          <h2>{name}</h2>
          <img src={imageUrl} alt={name}/>
        </div>
    )
}
```

Que avons-nous dans le code ci-dessus ?

Nous avons notre composant fonctionnel régulier dans React et ensuite nous avons les props – `name` et `imageUrl`. Ils sont déstructurés et passés directement dans notre fonction afin que nous puissions vraiment réutiliser ce composant Author dans n'importe quelle section de notre application.

Maintenant, pour réutiliser le composant Author.jsx dans notre AuthorProfile.jsx, nous pouvons faire ceci :

```javascript
import Author from "./Author"

export default function AuthorProfile(){
	return (
      <div className="author-profile">
      	<Author name="Alvin"  
        imageUrl="https://avatars.githubusercontent.com/u/43749581?v=4" />
      </div>
    )
}
```

Tout d'abord, nous devons importer le composant là où nous voulons le réutiliser, comme vous pouvez le voir dans la première ligne du code ci-dessus où nous avons notre instruction d'importation.

Deuxièmement, parce que nous avons passé `name` et `imageUrl` en tant que props dans le composant author précédemment, le composant author s'attend à ce que les mêmes données lui soient passées au départ.

Nous pouvons rendre de nombreux composants réutilisables de cette manière dans une grande base de code avec l'aide des props. Et cela nous aide à structurer correctement notre code.

Génial !

## Exemple de Props

Démontrons comment les props sont utiles avec un dernier exemple – mais cette fois-ci, nous allons créer un bouton réutilisable avec l'aide des props.

Créez un nouveau fichier appelé PrimaryButton.jsx. Dans le fichier PrimaryButton, faisons ceci :

```javascript
export default function PrimaryButton({width,
  height,
  backgroundColor,
  color,
  border,
  borderColor,
  fontSize,
  buttonText,}) {
	return (
    	<button style={{width, height, backgroundColor, color, border, borderColor, fontSize}}>
           {buttonText}
        </button>
    )
}
```

Super, maintenant nous avons un bouton que nous pouvons utiliser n'importe où dans notre application. Au lieu de répéter ou de créer des boutons encore et encore, nous pouvons simplement importer le bouton réutilisable, passer les données requises, et nous sommes prêts à partir.

## Conclusion

Maintenant que vous avez appris comment créer des composants réutilisables dans React avec l'aide des props. Essayez d'autres exemples par vous-même et bon codage !