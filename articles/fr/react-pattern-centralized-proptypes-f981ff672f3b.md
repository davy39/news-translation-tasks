---
title: 'Modèle React : Centralisation des PropTypes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-14T16:39:43.000Z'
originalURL: https://freecodecamp.org/news/react-pattern-centralized-proptypes-f981ff672f3b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fjBw8m5BiLqjW9BHfmySfg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Modèle React : Centralisation des PropTypes'
seo_desc: 'By Cory House

  Avoid repeating yourself by centralizing PropTypes

  There are three popular ways to handle types in React: PropTypes, TypeScript and
  Flow. This post is about PropTypes, which are currently the most popular.

  https://twitter.com/housecor/s...'
---

Par Cory House

#### Évitez de vous répéter en centralisant les PropTypes

Il existe trois méthodes populaires pour gérer les types dans React : [PropTypes](https://reactjs.org/docs/typechecking-with-proptypes.html), [TypeScript](http://typescriptlang.org) et [Flow](http://flowtype.org/). Cet article traite des PropTypes, qui sont actuellement les plus populaires.

%[https://twitter.com/housecor/status/911673327240073216?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fhousecor%2Fstatus%2F911673327240073216%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F650743198348808192%25252FLT6SeOJr_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Puisque les PropTypes fournissent des avertissements de type à l'exécution, il est utile d'être aussi spécifique que possible.

* Le composant accepte un objet ? Déclarez la forme de l'objet.
* La prop n'accepte qu'une liste spécifique de valeurs ? Utilisez oneOf.
* Le tableau doit contenir des nombres ? Utilisez arrayOf.
* Vous pouvez même déclarer vos propres types. [AirBnB offre de nombreux PropTypes supplémentaires](https://github.com/airbnb/prop-types).

Voici un exemple de PropType :

```js
UserDetails.propTypes = {
 user: PropTypes.shape({
   id: PropTypes.number.isRequired,
   firstName: PropTypes.string.isRequired,
   lastName: PropTypes.string.isRequired,
   role: PropTypes.oneOf(['user','admin'])
};
```

Dans les vraies applications avec de grands objets, cela conduit rapidement à beaucoup de code. C'est un problème, car **dans React, vous passerez souvent le même objet à plusieurs composants**. Répéter ces détails dans plusieurs fichiers de composants brise le [principe DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (ne vous répétez pas). Se répéter crée un problème de maintenance.

La solution ? **Centralisez vos PropTypes**.

#### Voici comment centraliser les PropTypes

Je préfère centraliser les PropTypes dans /types/index.js.

J'utilise des imports nommés à la ligne 2 pour raccourcir les déclarations. ?

Et voici comment j'utilise le PropType que j'ai déclaré ci-dessus :

```js
// types/index.js
import { shape, number, string, oneOf } from 'prop-types';

export const userType = shape({
  id: number,
  firstName: string.isRequired,
  lastName: string.isRequired,
  company: string,
  role: oneOf(['user', 'author']),
  address: shape({
    id: number.isRequired,
    street: string.isRequired,
    street2: string,
    city: string.isRequired,
    state: string.isRequired,
    postal: number.isRequired
  });
});
```

J'utilise un import nommé pour obtenir une référence à la déclaration PropType exportée à la ligne 2. Et je l'utilise à la ligne 13.

**Avantages** :

1. Le PropType centralisé simplifie radicalement la déclaration PropType du composant. La ligne 13 fait simplement référence au PropType centralisé, ce qui le rend facile à lire.
2. Le type centralisé ne déclare que la forme, vous pouvez donc toujours marquer la prop comme requise si nécessaire.
3. Plus de copier/coller. Si la forme de l'objet change plus tard, vous avez un seul endroit à mettre à jour. ?

Voici un [exemple fonctionnel sur CodeSandbox](https://codesandbox.io/s/3vw24xnlqm).

%[https://codesandbox.io/s/3vw24xnlqm]

#### Bonus : Générez vos PropTypes

Enfin, envisagez d'écrire du code personnalisé pour générer vos déclarations PropType à partir de votre code côté serveur. Par exemple, si votre API est écrite dans un langage fortement typé comme C# ou Java, envisagez de générer vos déclarations PropType dans le cadre de votre processus de construction de l'API côté serveur en lisant la forme de vos classes côté serveur. Ainsi, vous n'aurez pas à vous soucier de maintenir vos PropTypes côté client et votre code API côté serveur synchronisés. ?

**Note** : Si vous connaissez un projet qui fait cela pour un langage côté serveur, veuillez répondre dans les commentaires et j'ajouterai un lien ici.

**Édition** : Vous pouvez convertir du JSON en PropTypes en utilisant [transform.now.sh](https://transform.now.sh/). ?

### Résumé

1. Déclarez vos PropTypes aussi explicitement que possible, afin de savoir quand vous avez fait une erreur.
2. Centralisez vos PropTypes pour éviter de vous répéter.
3. Si vous travaillez dans un langage fortement typé côté serveur, envisagez de générer vos PropTypes en lisant votre code côté serveur. Cela assure que vos PropTypes correspondent à vos types côté serveur.

### Vous cherchez plus d'informations sur React ? 

J'ai écrit [plusieurs cours sur React et JavaScript](http://bit.ly/psauthorpageimmutablepost) sur Pluralsight ([essai gratuit](http://bit.ly/pstrialimmutablepost)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel chez VinSolutions, MVP Microsoft, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).