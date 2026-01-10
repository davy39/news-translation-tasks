---
title: Comment créer des listes déroulantes dépendantes dans React
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2025-01-30T14:52:54.172Z'
originalURL: https://freecodecamp.org/news/how-to-build-dependent-dropdowns-in-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738246583123/caa07859-2ce8-44b1-9fd2-44b414babe52.png
tags:
- name: React
  slug: reactjs
seo_title: Comment créer des listes déroulantes dépendantes dans React
seo_desc: In many web applications, we often encounter forms where selecting an option
  in one dropdown unlocks a new set of options in another. These interconnected dropdowns,
  commonly known as dependent or cascading dropdowns, play a crucial role in creating
  ...
---

Dans de nombreuses applications web, nous rencontrons souvent des formulaires où la sélection d'une option dans une liste déroulante déverrouille un nouvel ensemble d'options dans une autre. Ces listes déroulantes interconnectées, communément appelées listes déroulantes dépendantes ou en cascade, jouent un rôle crucial dans la création d'une expérience de remplissage de formulaire fluide et intuitive.

Qu'il s'agisse de sélectionner un pays pour révéler les états correspondants ou de choisir une catégorie de produit pour afficher des articles spécifiques, ces listes déroulantes simplifient les choix complexes pour tout le monde. Pour les développeurs, la mise en œuvre de listes déroulantes dépendantes est un défi pratique qui combine logique, utilisabilité et gestion dynamique des données.

Dans ce tutoriel, vous apprendrez à implémenter ce type de liste déroulante dans votre application React.

## Table des matières

* [Qu'est-ce qu'une liste déroulante dépendante ?](#heading-quest-ce-quune-liste-deroulante-dependante)
    
* [Comment fonctionne une liste déroulante dépendante ?](#heading-comment-fonctionne-une-liste-deroulante-dependante)
    
* [Étapes pour créer des listes déroulantes dépendantes dans React](#heading-etapes-pour-creer-des-listes-deroulantes-dependantes-dans-react)
    
    * [Étape 1 : Installer votre projet React](#heading-etape-1-installer-votre-projet-react)
        
    * [Étape 2 : Structurer le composant](#heading-etape-2-structurer-le-composant)
        
    * [Étape 3 : Utiliser le composant](#heading-etape-3-utiliser-le-composant)
        
* [Gestion des données dynamiques (requêtes API)](#heading-gestion-des-donnees-dynamiques-requetes-api)
    
* [Conclusion](#heading-conclusion)
    

## **Qu'est-ce qu'une liste déroulante dépendante ?**

Une liste déroulante dépendante est un élément d'interface utilisateur dans lequel les options disponibles dans une liste déroulante sont déterminées par la sélection effectuée dans une autre liste déroulante. Par exemple, considérons un scénario où vous avez deux listes déroulantes :

1. Liste déroulante Pays : L'utilisateur sélectionne un pays.
    
2. Liste déroulante Ville : En fonction du pays sélectionné, la liste des villes disponibles dans la deuxième liste déroulante sera filtrée en conséquence.
    

Ce type d'interaction est crucial pour les formulaires qui nécessitent des entrées de données complexes et sensibles au contexte.

## **Comment fonctionne une liste déroulante dépendante ?**

Les listes déroulantes dépendantes fonctionnent en mettant à jour dynamiquement les options de la deuxième liste déroulante en fonction de la valeur sélectionnée dans la première liste déroulante. Ce changement dynamique est généralement réalisé par :

1. **Écoute de l'entrée utilisateur :** Lorsque l'utilisateur sélectionne une option dans la première liste déroulante, un événement (généralement onChange) déclenche une fonction pour mettre à jour l'état.
    
2. **Récupération de nouvelles données :** Cet état mis à jour peut être utilisé pour filtrer les données existantes ou effectuer un appel API pour récupérer la nouvelle liste d'options.
    
3. **Rendu des nouvelles données :** La deuxième liste déroulante est ensuite mise à jour avec les nouvelles options, offrant à l'utilisateur des choix pertinents.
    

## **Étapes pour créer des listes déroulantes dépendantes dans React**

### **Étape 1 : Installer votre projet React**

Si vous êtes nouveau dans React et souhaitez suivre ce tutoriel, [consultez la documentation de Vite](https://vite.dev/guide/) et suivez les étapes pour créer votre projet React. Une fois terminé, revenez ici et continuons à construire.

Si vous avez déjà un projet React que vous souhaitez utiliser, c'est également parfait.

### **Étape 2 : Structurer le composant**

Pour simplifier, supposons que nous construisons une liste déroulante dépendante à deux niveaux où la première liste déroulante vous permet de choisir un pays, et la deuxième liste déroulante affiche des villes en fonction du pays sélectionné.

De plus, dans la liste déroulante des pays, nous aurons une autre option pour entrer un nom de pays qui n'est pas inclus dans les options de pays. L'utilisateur peut ensuite procéder à la saisie de son pays dans une entrée de texte.

Tout d'abord, créez un nouveau fichier nommé `DependentDropdown.js` ou `DependentDropdown.jsx`. À l'intérieur de ce fichier, définissez un composant fonctionnel appelé `DependentDropdown`.

Nous allons maintenant passer par les étapes suivantes pour construire notre liste déroulante dépendante :

**Déclarer des variables pour stocker les données**

Nous devons créer des données statiques pour les valeurs de nos pays et villes :

```javascript
  // Données statiques des pays
  const countries = [
    { id: 1, name: 'USA' },
    { id: 2, name: 'Canada' },
    { id: 3, name: 'Autre' },
  ];

  // Données statiques des villes correspondant aux pays
  const cities = {
    USA: ['New York', 'Los Angeles', 'Chicago'],
    Canada: ['Toronto', 'Vancouver', 'Montreal'],
  };
```

* `countries` est un tableau d'objets. Chaque objet ayant des propriétés `id` et `name`.
    
* `cities` est un objet avec des noms de pays comme clés et les valeurs comme tableau de villes.
    

**Déclarer des variables d'état**

Pour chaque sélection de pays ou de villes, nous voulons pouvoir suivre les valeurs sélectionnées. Nous voulons également pouvoir remplir les options de villes après qu'une sélection de pays a été faite. Pour cela, nous devons déclarer quelques états.

Si le concept d'état vous est nouveau, vous pouvez lire mon article sur l'état [ici](https://www.freecodecamp.org/news/react-state-management/).

```javascript
  const [selectedCountry, setSelectedCountry] = useState('');
  const [availableCities, setAvailableCities] = useState([]);
  const [selectedCity, setSelectedCity] = useState('');
  const [otherCountry, setOtherCountry] = useState('');
```

* L'état `selectedCountry` est déclaré et sa valeur initiale est définie comme une chaîne vide.
    
* L'état `availableCities` est déclaré et sa valeur initiale est définie comme un tableau vide.
    
* L'état `selectedCity` est déclaré et sa valeur initiale est définie comme une chaîne vide.
    
* L'état `otherCountry` est déclaré et sa valeur initiale est définie comme une chaîne vide.
    

**Gestion des événements**

Dans le processus de sélection dans la liste déroulante, nous voulons que certaines actions soient effectuées. Les gestionnaires d'événements nous permettent de le faire en cas d'événement, qui dans ce cas est l'événement `onChange`.

```javascript
  const handleCountryChange = (e) => {
    const country = e.target.value;
    setSelectedCountry(country);
    setAvailableCities(cities[country] || []);
    setSelectedCity(''); 
     if (country !== 'Autre') {
      setOtherCountry('');
    }
  };
```

Voici ce qui se passe dans la fonction `handleCountryChange` :

* Récupère la valeur de l'option sélectionnée dans la liste déroulante (le pays qui a été sélectionné).
    
* Le `setSelectedCountry` met à jour la variable d'état (selectedCountry) avec le nouveau pays sélectionné.
    
* `cities[country]` recherche la liste des villes pour le pays sélectionné à partir de l'objet `cities`.
    
    * Si `cities[country]` est trouvé, il définit cette liste de villes comme les villes disponibles.
        
    * Si aucune ville n'est trouvée pour le pays sélectionné (`cities[country]` est indéfini), le `|| []` garantit qu'un tableau vide (`[]`) est utilisé comme solution de repli, empêchant les erreurs lors de l'affichage des villes.
        
* Lorsque l'utilisateur change la sélection du pays, la fonction `setSelectedCity` réinitialise la `selectedCity` à une chaîne vide.
    
* Si le pays sélectionné n'est pas 'Autre', l'état `otherCountry` est réinitialisé à une chaîne vide. Cela garantit que si l'utilisateur avait précédemment tapé quelque chose dans l'entrée "Autre", ce texte est effacé une fois qu'il sélectionne un autre pays (par exemple, "USA" ou "Canada").
    

Pour la sélection du pays 'Autre', nous devons simplement suivre la valeur entrée dans l'entrée. La fonction `setOtherCountry` met à jour la valeur entrée. Et voici comment cela se fait :

```javascript
  const handleOtherCountryChange = (e) => {
    setOtherCountry(e.target.value);
  };
```

Pour le changement de villes, nous n'avons pas besoin de faire grand-chose car le pays sélectionné détermine quelles villes sont affichées. Tout ce que nous avons à faire est de mettre à jour la `selectedCity` à la valeur de l'option sélectionnée dans la liste déroulante, qui est la ville qui est sélectionnée.

Dans React, la fonction de mise à jour effectue la mise à jour des variables d'état, donc le `setSelectedCity` gère cela dans ce cas.

La fonction `handleCityChange` sera :

```javascript
  const handleCityChange = (e) => {
    setSelectedCity(e.target.value);
  };
```

**Retourner JSX**

Le composant `DependentDropdown` rend trois éléments principaux : la liste déroulante Pays, la liste déroulante Ville et l'entrée de texte Pays.

Une liste déroulante en HTML est une combinaison des éléments `<select>` et `<option>`. Pour suivre la valeur des éléments, nous allons attacher des variables d'état à ceux-ci afin de pouvoir les contrôler. Faire cela s'appelle 'Contrôler les éléments', tandis que les éléments eux-mêmes sont appelés 'Éléments contrôlés' dans React.

Pour contrôler l'élément `<select>` du pays, nous allons lui donner un attribut `value` de `selectedCountry` et également attacher la fonction `handleCountryChange` à celui-ci.

```javascript
     <label htmlFor="country" className='font-bold'>Sélectionner le pays : </label>
      <select id="country" value={selectedCountry} onChange={handleCountryChange}>
        <option value="">Sélectionner un pays</option>
        {countries.map((country) => (
          <option key={country.id} value={country.name}>
            {country.name}
          </option>
        ))}
      </select>
```

De plus,

* À l'intérieur de `<option>`, nous parcourons le tableau `countries` et créons dynamiquement une `<option>` pour chaque objet pays dans le tableau.
    
* Le `name` de chaque pays est affiché comme texte de l'option.
    
* La `key` de chaque option est définie sur l'`id` du pays et la `value` est définie sur le `name` du pays.
    
* La `key` aide React à gérer la liste efficacement lors du re-rendu.
    

La liste déroulante des villes est rendue conditionnellement en fonction du pays sélectionné. Si l'option de pays 'Autre' est choisie, un champ de saisie de texte est affiché pour que l'utilisateur spécifie le pays. Sinon, si un pays valide est sélectionné, une liste déroulante des villes avec des options pertinentes est affichée.

```javascript
{selectedCountry === 'Autre' ? (
        <>
          <label htmlFor="other-country" className='font-bold'>Veuillez spécifier le pays : </label>
          <input
            id="other-country"
            type="text"
            value={otherCountry}
            onChange={handleOtherCountryChange}
            placeholder="Entrez le nom du pays"
          />
        </>
      ) : (
        selectedCountry && (
          <>
            <label htmlFor="city" className='font-bold'>Sélectionner la ville : </label>
            <select id="city" value={selectedCity} onChange={handleCityChange}>
              <option value="">Sélectionner une ville</option>
              {availableCities.map((city, index) => (
                <option key={index} value={city}>
                  {city}
                </option>
              ))}
            </select>
          </>
        )
      )
}
```

De plus :

* Nous vérifions si `selectedCountry` est l'option 'Autre' et affichons une entrée de texte.
    
* L'entrée de texte a un état `otherCountry` et la fonction de gestionnaire `handleOtherCountryChange` attachée à celle-ci.
    
* Nous contrôlons l'élément `<select>` de la ville en utilisant l'attribut `value`, en le définissant sur la variable d'état `selectedCity`. Le gestionnaire d'événements, `handleCityChange`, est également attaché pour gérer les événements `onChange`.
    
* Nous parcourons le tableau `availableCities` et créons dynamiquement une `<option>` pour chaque ville dans le tableau.
    
* La `key` de chaque option est définie sur un `index` et la `value` est définie sur la `city`.
    
* Chaque ville est affichée comme texte de l'option.
    

C'est tout ce que nous avons à faire pour avoir une liste déroulante dépendante fonctionnelle en utilisant nos données statiques.

Voici tout le code mis ensemble :

```javascript
import React, { useState } from 'react';

const DependentDropdown = () => {
  // Données statiques des pays
  const countries = [
    { id: 1, name: 'USA' },
    { id: 2, name: 'Canada' },
    { id: 3, name: 'Autre' },
  ];

  // Données statiques des villes correspondant aux pays
  const cities = {
    USA: ['New York', 'Los Angeles', 'Chicago'],
    Canada: ['Toronto', 'Vancouver', 'Montreal'],
  };

  // État pour contenir le pays sélectionné, la ville et le texte du pays autre
  const [selectedCountry, setSelectedCountry] = useState('');
  const [availableCities, setAvailableCities] = useState([]);
  const [selectedCity, setSelectedCity] = useState('');
  const [otherCountry, setOtherCountry] = useState(''); 

  // Gérer le changement de pays
  const handleCountryChange = (e) => {
    const country = e.target.value;
    setSelectedCountry(country);
    setAvailableCities(cities[country] || []);
    setSelectedCity(''); 
    if (country !== 'Autre') {
      setOtherCountry('');
    }
  };

  // Gérer le changement de ville
  const handleCityChange = (e) => {
    setSelectedCity(e.target.value);
  };

  // Gérer le changement de l'entrée du pays autre
  const handleOtherCountryChange = (e) => {
    setOtherCountry(e.target.value);
  };

  return (
    <div className='text-center text-3xl'>
      <h1 className='font-extrabold text-5xl p-10'>Exemple de liste déroulante dépendante</h1>

      {/* Liste déroulante Pays */}
      <label htmlFor="country" className='font-bold'>Sélectionner le pays : </label>
      <select id="country" value={selectedCountry} onChange={handleCountryChange}>
        <option value="">Sélectionner un pays</option>
        {countries.map((country) => (
          <option key={country.id} value={country.name}>
            {country.name}
          </option>
        ))}
      </select>

      {/* Ville ou entrée du pays autre */}
      {selectedCountry === 'Autre' ? (
        <>
          <label htmlFor="other-country" className='font-bold'>Veuillez spécifier le pays : </label>
          <input
            id="other-country"
            type="text"
            value={otherCountry}
            onChange={handleOtherCountryChange}
            placeholder="Entrez le nom du pays"
          />
        </>
      ) : (
        selectedCountry && (
          <>
            <label htmlFor="city" className='font-bold'>Sélectionner la ville : </label>
            <select id="city" value={selectedCity} onChange={handleCityChange}>
              <option value="">Sélectionner une ville</option>
              {availableCities.map((city, index) => (
                <option key={index} value={city}>
                  {city}
                </option>
              ))}
            </select>
          </>
        )
      )}
    </div>
  );
};

export default DependentDropdown;
```

### Étape 3 : Utiliser le composant

Pour obtenir vos résultats finaux, vous devez importer le composant `DependentDropdown` dans votre `App.js` ou `App.jsx` et le placer à l'intérieur de la section de retour du composant App.

```javascript
import DependentDropdown from './DependentDropdown'

function App() {

  return (
    <DependentDropdown/>
  )
}

export default App
```

N'oubliez pas d'exécuter l'application en entrant l'une de ces commandes :

```javascript
npm start //pour create react app
npm run dev //pour react vite app
```

Enfin, voici ce qui devrait être rendu dans votre navigateur :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737899898480/38ff328c-09bd-4f74-b458-423ff1216e48.gif align="center")

## Gestion des données dynamiques (requêtes API)

Dans les applications réelles, les listes pour les listes déroulantes peuvent ne pas être statiques. Au lieu de cela, elles peuvent être récupérées à partir d'une API ou d'un fichier JSON agissant comme une API.

Dans cet exemple, nous allons lire les données d'un fichier JSON pour remplir notre liste déroulante dépendante. Cette pratique présente certains avantages qui sont :

* **Charge de la base de données réduite :** En utilisant un fichier JSON statique (ou un fichier préchargé), vous réduisez le nombre de requêtes de base de données qui seraient autrement nécessaires pour remplir les listes déroulantes. Cela est particulièrement utile si les options de la liste déroulante sont assez statiques et ne changent pas souvent.
    
* **Rendu de l'interface utilisateur plus rapide :** Puisque les données sont déjà du côté client, il n'est pas nécessaire d'effectuer une requête aller-retour vers le serveur chaque fois que l'utilisateur interagit avec la liste déroulante. Cela peut rendre l'interface plus réactive.
    

Notre fichier JSON contient des états et des LGAs (Zones de gouvernement local), qui sont les équivalents des pays et des villes.

Les données dans le fichier JSON sont représentées sous forme de tableau d'objets, chaque objet ayant des clés pour **state**, **alias** et **lgas**. La clé 'lgas' contient un tableau.

Voici comment cela est représenté :

```json
[
  {
    "state": "Adamawa",
    "alias": "adamawa",
    "lgas": [
      "Demsa",
      "Fufure",
      "Toungo",
      "Yola North",
      "Yola South"
    ]
  },
  {
    "state": "Akwa Ibom",
    "alias": "akwa_ibom",
    "lgas": [
      "Abak",
      "Uruan",
      "Urue-Offong/Oruko",
      "Uyo"
    ]
  },
//le reste des objets
]
```

Cette méthode de création d'une liste déroulante dépendante dynamique à partir d'une API n'est pas très différente de l'exemple précédent, à l'exception de quelques modifications mineures.

Voici comment nous avons récupéré et utilisé les données d'un fichier JSON :

```javascript
import React, { useEffect, useState } from "react";

function DependentDropdown() {
//déclaration des variables d'état globales
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  
//récupération des données en utilisant le hook useEffect
  useEffect(() => {
    fetch("nigeria-state-and-lgas.json") //Fichier JSON défini comme URL
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des données :", error);
        setLoading(false);
      });
  }, []);
  return loading ? <div>Chargement...</div> : <Form data={data} />;
  
}
//formulaire recevant les données en tant que props
function Form({ data }) {

//déclaration des variables d'état locales
  const [selectedState, setSelectedState] = useState("");
  const [selectedLga, setSelectedLga] = useState("");
  const [showList, setShowList] = useState(false);
  let sortedData = data.slice().sort((a, b) => a.state.localeCompare(b.state));
  const selectedData = sortedData.find((item) => item.state === selectedState);

//fonction de gestion pour l'état
  function handleClickState(e) {
    setSelectedState(e.target.value);
    setShowList(true);
  }
//fonction de gestion pour Lga
  function handleClickLga(e) {
    setSelectedLga(e.target.value);
  }

  return (
    <div>
  <form onSubmit={handleFormSubmit}>
    <div>
      {/* Prénom */}
      <div>
        <label htmlFor="firstName">Prénom</label>
        <input type="text"
          id="firstName"
          name="firstName"
          placeholder="Entrez votre prénom"/>
      </div>

      {/* Nom de famille */}
      <div>
        <label htmlFor="lastName">
          Nom de famille
        </label>
        <input
          type="text"
          id="lastName"
          name="lastName"
          placeholder="Entrez votre nom de famille"/>
      </div>
    </div>

    <div>
      <div>
        <select value={selectedState} onChange={handleClickState} name="state">
          <option value="" disabled>Choisissez votre état</option>
          {sortedData.map((data) => (
            <option key={data.alias} value={data.state}>
              {data.state}
            </option>
          ))}
        </select>
      </div>
      {selectedData && showList && (
        <select value={selectedLga} onChange={handleClickLga} name="lga">
          <option value="" disabled>{`Choisissez votre LGA dans ${selectedState}`}</option>
          {selectedData.lgas.map((lgass) => (
            <option key={lgass} value={lgass}>
              {lgass}
            </option>
          ))}
        </select>
      )}
      
    </div>
    <div>
        <button type="submit">
          Soumettre
        </button>
      </div>
  </form>
</div>
  );
}

export default DependentDropdown;
```

La modification clé ici est la récupération des données en utilisant le hook `useEffect`, qui récupère les données des états et des LGAs uniquement lors du rendu initial.

Voici comment cela est rendu dans le navigateur :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737856956995/ada964c4-a2a4-4012-869f-c0bbf53761a7.gif align="center")

## Conclusion

Dans ce tutoriel, vous avez appris à créer des listes déroulantes dépendantes dans React en utilisant des données statiques et dynamiques. Vous pouvez maintenant utiliser ce type de liste déroulante dans vos applications React.

Si vous avez trouvé cet article utile, vous pouvez vous connecter avec moi sur [LinkedIn](https://linkedin.com/in/timothy-olanrewaju750) pour plus d'articles et de publications liés à la programmation.

À la prochaine !