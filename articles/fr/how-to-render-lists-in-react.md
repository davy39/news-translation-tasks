---
title: Comment rendre des listes dans React en utilisant array.map()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-10T21:39:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-render-lists-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Lists-in-React.png
tags:
- name: React
  slug: react
seo_title: Comment rendre des listes dans React en utilisant array.map()
seo_desc: 'By Mwendwa Bundi Emma

  When you''re working with React, you will often times need to render lists of items.
  With the map() method, you can create new results from your current lists or even
  showcase all the items in your lists.

  In this tutorial, you wi...'
---

Par Mwendwa Bundi Emma

Lorsque vous travaillez avec React, vous devrez souvent rendre des listes d'éléments. Avec la méthode `map()`, vous pouvez créer de nouveaux résultats à partir de vos listes actuelles ou même présenter tous les éléments de vos listes.

Dans ce tutoriel, vous apprendrez à utiliser cette méthode pour accéder au contenu des tableaux dans React. Nous explorerons également comment passer une liste d'éléments à plusieurs composants React en utilisant les `props` de React.

## Qu'est-ce que array.prototype.map() ?

La méthode JavaScript `map()` fonctionne en créant un nouveau tableau qui contient les résultats de l'appel d'une fonction sur les éléments de votre tableau.

Voici le tableau avec lequel vous allez travailler. Il contient des informations sur les candidats à un atelier de mentorat. Le tableau est stocké dans la variable `applicants`.

```js
const applicants = [ {
  name: 'Joe', work: 'freelance-developer', 
  blogs: '54', websites: '32', 
  hackathons: 'none', location: 'Morocco', id: '0',
    
},
 {
  name: 'Janet', work: 'fullstack-developer', 
  blogs: '34', websites: '12', 
  hackathons: '6', location: 'Mozambique', id: '1',
    
},

];
```

## Comment `array.prototype.map()` fonctionne dans React

Maintenant, vous devez retourner du JSX qui rend chaque nom de candidat tel que présenté dans le tableau.

Pour obtenir les noms des candidats, vous pouvez facilement le faire avec la méthode `array.map` de JavaScript. Voici comment vous pouvez mapper chaque nom de candidat :



```react
import React from 'react';


  const applicants = [ {
    name: 'Joe', work: 'freelance-developer',
    blogs: '54', websites: '32',
    hackathons: '6', location: 'morocco', id: '0',
  },
  {
    name: 'janet', work: 'fullstack-developer', 
    blogs: '34', websites: '12', 
    hackathons: '8', location: 'Mozambique', id: '1',
  },

];

function App() {
  return (
    <>
    {applicants.map(function(data) {
      return (
        <div>
          Nom du candidat :  {data.name}
        </div>
      )
    })}
    </>

  )
}
export default App;
```

Voici le résultat attendu du code :

```react
Nom du candidat : Joe
Nom du candidat : janet
```

Malheureusement, une inspection rapide de notre page web actuelle génère cette erreur concernant les clés :

> react-jsx-dev-runtime.development.js:87 Avertissement : Chaque enfant dans une liste doit avoir un prop "key" unique.  
>   
> Vérifiez la méthode de rendu de `App`. Voir [https://reactjs.org/link/warning-keys](https://reactjs.org/link/warning-keys) pour plus d'informations.  
> at div  
> at App  
> printWarning @ react-jsx-dev-runtime.development.js:87

## Pourquoi vous avez besoin de clés dans les listes

Bien que le code ci-dessus fonctionne parfaitement, un attribut clé lors de la gestion des listes dans React est essentiel. L'attribut clé est très important pour identifier de manière unique chaque élément particulier dans le tableau. 

React attribue à chaque élément un attribut clé unique et peut ainsi les suivre malgré les changements. Cela aide à garantir que vous ne finissez pas par désorganiser votre code lorsque des changements se produisent dans vos listes.

Avec l'attribut clé, tout changement tel que le réordonnancement, l'ajout ou la suppression d'éléments du tableau peut être suivi. C'est une bonne pratique.

Voici une démonstration de code montrant l'attribut clé en action :

```react
import React from 'react';


  const applicants = [ {
    name: 'Joe', work: 'freelance-developer',
    blogs: '54', websites: '32',
    hackathons: '6', location: 'morocco', id: '0',
  },
  {
    name: 'janet', work: 'fullstack-developer', 
    blogs: '34', websites: '12', 
    hackathons: '8', location: 'Mozambique', id: '1',
  },

];

function App() {
  return (
    <>
    {applicants.map(function(applicant) {
      return (
        <div key={applicant.id}>
          <p>Nom du candidat : {applicant.name}</p>
          <p>Localisation du candidat : {applicant.location}</p>
          <p>Hackathons participés : {applicant.hackathons}</p>

        </div>
      )
    })}
    </>
  );
};


        
  
export default App;
```

Comme vous pouvez le voir, un grand ensemble de candidats est mappé et affiché en douceur en utilisant quelques lignes de code.

En même temps, si vous deviez supprimer des candidats qui ne répondent pas à certaines qualifications, l'attribut clé aiderait à suivre les candidats restants en utilisant la clé unique attribuée.

Voici le résultat attendu du code :

```react
Nom du candidat : Joe

Localisation du candidat : Maroc

Hackathons participés : aucun

Nom du candidat : Janet

Localisation du candidat : Mozambique

Hackathons participés : 6
```

Dans les exemples ci-dessus, vous ne traitez que d'une seule variable.

Maintenant, il y aura des cas dans votre travail où vous aurez différents fichiers et plus d'une variable dans différents composants React.

C'est là que les `props` de React interviennent.

## Qu'est-ce que les Props dans React ?

Le mot 'props' signifie propriétés et elles sont utilisées pour passer des données d'un composant à un autre. Les props sont utiles pour passer des données et vous aident à écrire un code propre et léger.

Le tableau que nous utilisons a une variable nommée `applicants`. Vous avez un nouveau composant qui présente les noms des candidats, le nombre de sites web construits et leurs localisations respectives.

Comment passez-vous alors la liste à ce nouveau composant ?

`<ShowcaseApplicants applicants={applicants} />`

Vous pouvez facilement obtenir les données des candidats à partir de l'objet `props` comme montré ci-dessous :

```react
import React from 'react';

const App = () => {
  const applicants = [ {
    name: 'Joe', work: 'freelance-developer',
    blogs: '54', websites: '32',
    hackathons: '6', location: 'morocco', id: '0',
  },
  {
    name: 'janet', work: 'fullstack-developer', 
    blogs: '34', websites: '12', 
    hackathons: '8', location: 'Mozambique', id: '1',
  },

]


return (
  <div>
    <h1>Oh ! Bonjour le monde</h1>

    <ShowcaseApplicants applicants={applicants} />

  </div>
)

function ShowcaseApplicants(props) {
  const applicants = props.applicants

  return (

    <div>
    {applicants.map((applicant) => (

      <div key={applicant.id}>
        <p>
          Nom du candidat : <span>{applicant.name}</span>
        </p>
        <p>
          Sites web construits : <span>{applicant.websites}</span>
        </p>
        <p>Localisation du candidat : <span>{applicant.location}</span>
        </p>
      </div>  

    ))}
    </div>
  );
}
}

        
  
export default App;
```

À l'intérieur du composant `App`, nous avons inclus `applicants` en tant que variable locale. Ainsi, nous ne polluons pas la portée globale. Nous avons ensuite retourné une `div` avec une balise `h1`.

Ensuite, nous voulons passer les données du tableau à un nouveau composant qui présente des données supplémentaires sur chaque candidat. Avec l'instanciation de `ShowcaseApplicants`, le composant accède au tableau en utilisant les `props` `applicants`.

Après cela, nous avons utilisé `array.map()` pour mapper le nom des candidats, le nombre de sites web construits et la localisation, qui a été rendu en JSX. Et nous n'avons pas oublié l'attribut clé important.

Voici le résultat attendu du code :

```react
Oh ! Bonjour le monde
Nom du candidat : Joe

Sites web construits : 32

Localisation du candidat : Maroc

Nom du candidat : Janet

Sites web construits : 12

Localisation du candidat : Mozambique
```

## Conclusion

Dans cet article, vous avez appris à utiliser la méthode JavaScript `map()` pour rendre une liste d'éléments dans React. Vous avez également appris à utiliser les `props` de React pour passer les données des listes à d'autres composants également.