---
title: Comment créer un composant de pagination personnalisé dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-14T22:39:00.000Z'
originalURL: https://freecodecamp.org/news/build-a-custom-pagination-component-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/custom-pagination-image.jpeg
tags:
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer un composant de pagination personnalisé dans React
seo_desc: 'By Shubham Khatri

  We often work with web applications that need to fetch large amounts of data from
  a server through APIs and render it on the screen.

  For example, in a Social media application we fetch and render users'' posts and
  comments. In an HR ...'
---

Par Shubham Khatri

Nous travaillons souvent avec des applications web qui doivent récupérer de grandes quantités de données à partir d'un serveur via des API et les afficher à l'écran.

Par exemple, dans une **application de médias sociaux**, nous récupérons et affichons les publications et les commentaires des utilisateurs. Dans un **tableau de bord RH**, nous affichons des informations sur les candidats qui ont postulé pour un emploi. Et dans un **client de messagerie**, nous montrons les e-mails d'un utilisateur.  
  
Afficher toutes les données à la fois à l'écran peut ralentir considérablement votre page web en raison du grand nombre d'éléments DOM présents dans la page.

Si nous voulons optimiser les performances, nous pouvons adopter diverses techniques pour rendre les données de manière plus efficace. Certaines de ces méthodes incluent le **défilement infini avec virtualisation** et la **pagination**.

La pagination fonctionne bien lorsque vous connaissez la taille des données à l'avance et que vous n'effectuez pas d'ajouts ou de suppressions fréquents dans l'ensemble de données. 

Par exemple, sur un site de médias sociaux où de nouvelles publications sont publiées toutes les quelques millisecondes, la pagination ne serait pas une solution idéale. Mais elle fonctionnerait bien pour un tableau de bord RH où les candidatures des candidats sont affichées et doivent être filtrées ou triées.

Dans cet article, nous nous concentrons sur la pagination et nous allons créer un composant contrôlé personnalisé qui gère les boutons de page en fonction de la page actuelle et du nombre total de données. 

Nous allons également écrire un hook React personnalisé qui nous donne une plage de nombres à afficher par le composant de pagination. Nous pouvons utiliser ce hook indépendamment lorsque nous voulons afficher un composant de pagination avec différents styles ou dans un design différent.

Voici une démonstration de ce que nous allons construire dans ce tutoriel :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/PaginationDemo.gif)

## Comment configurer le projet

Si vous êtes familier avec la configuration d'un projet React, vous pouvez sauter cette section.

Pour configurer notre projet React, nous allons utiliser le paquet de ligne de commande [`create-react-app`](https://github.com/facebook/create-react-app). Vous pouvez installer le paquet globalement en utilisant `npm install -g create-react-app` ou `yarn add global create-react-app`. 

Exécutez `create-react-app` depuis la ligne de commande pour créer un nouveau projet comme suit :

```
npx create-react-app react-pagination
```

Ensuite, nous devons installer nos dépendances. Nous allons simplement utiliser une dépendance supplémentaire appelée `classnames` qui offre de la flexibilité lors de la gestion de plusieurs classNames de manière conditionnelle. 

Pour l'installer, exécutez `npm install classnames` ou `yarn add classnames`.

Maintenant, nous pouvons exécuter notre projet en utilisant la commande suivante :

```
yarn start
```

## Comment définir l'interface  

Maintenant que notre projet est en cours d'exécution, nous allons plonger directement dans notre composant `Pagination`.   
  
Commençons par examiner les valeurs dont nous avons besoin en tant que props pour notre composant `Pagination` :

* **totalCount** : représente le nombre total de données disponibles à partir de la source.
* **currentPage** : représente la page active actuelle. Nous utiliserons un **index basé sur 1** au lieu d'un index traditionnel basé sur 0 pour notre valeur `currentPage`.
* **pageSize** : représente le nombre maximum de données visibles dans une seule page.
* **onPageChange** : fonction de rappel invoquée avec la valeur de page mise à jour lorsque la page est changée. 
* **siblingCount** (optionnel) : représente le nombre minimum de boutons de page à afficher de chaque côté du bouton de page actuelle. Par défaut, 1.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-85.png)
_Illustration des différentes valeurs de siblingCount_



* **className** (optionnel) : className à ajouter au conteneur de niveau supérieur.

À partir du composant de pagination, nous invoquerons le hook `usePagination` qui prendra les paramètres suivants pour calculer les plages de pages : `totalCount`, `currentPage`, `pageSize`, `siblingCount`.

## Comment implémenter le hook usePagination

Voici les quelques points à garder à l'esprit lors de l'implémentation du hook `usePagination` :

* Notre hook de pagination doit retourner la plage de nombres à afficher dans notre composant de pagination sous forme de tableau.
* La logique de calcul doit être réexécutée lorsque l'un des éléments suivants change : `currentPage`, `pageSize`, `siblingCount` ou `totalCount`.
* Le nombre total d'éléments retournés par le hook doit rester constant. Cela évitera de redimensionner notre composant de pagination si la longueur du tableau de plage change pendant que l'utilisateur interagit avec le composant.

En gardant ces points à l'esprit, créons un fichier appelé `usePagination.js` dans notre dossier `src` du projet et commençons l'implémentation.

Notre squelette de code sera le suivant :

```js
export const usePagination = ({
  totalCount,
  pageSize,
  siblingCount = 1,
  currentPage
}) => {
  const paginationRange = useMemo(() => {
     // Notre logique d'implémentation ira ici 
      
  }, [totalCount, pageSize, siblingCount, currentPage]);

  return paginationRange;
};
```

Si nous regardons le code ci-dessus, nous utilisons le hook `useMemo` pour calculer notre logique principale. La fonction de rappel `useMemo` s'exécutera lorsque l'une des valeurs de son tableau de dépendances changera.

Nous définissons également la `defaultValue` de notre prop `siblingCount` à `1` car il s'agit d'une prop optionnelle.

Avant de continuer et d'implémenter la logique du code, comprenons les différents comportements du composant `Pagination`. L'image ci-dessous contient les états possibles d'un composant de pagination :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-80.png)
_Différents états d'un composant de pagination_

Notez qu'il y a quatre états possibles pour un composant de pagination. Nous allons les passer en revue un par un.

* Le nombre total de pages est inférieur aux boutons de page que nous voulons afficher. Dans un tel cas, nous retournons simplement la plage de `1 à totalPageCount`.
* Le nombre total de pages est supérieur aux boutons de page, mais seuls les points de droite (DOTS) sont visibles.
* Le nombre total de pages est supérieur aux boutons de page, mais seuls les points de gauche (DOTS) sont visibles.
* Le nombre total de pages est supérieur aux boutons de page et les points de gauche et de droite (DOTS) sont visibles.

En tant que première étape, nous allons calculer le nombre total de pages à partir de `totalCount` et `pageSize` comme suit :

```js
const totalPageCount = Math.ceil(totalCount / pageSize);
```

Remarquez que nous utilisons `Math.ceil` pour arrondir le nombre à l'entier supérieur suivant. Cela garantit que nous réservons une page supplémentaire pour les données restantes. 

Ensuite, nous allons implémenter une fonction `range` personnalisée qui prend une valeur `start` et `end` et retourne un tableau avec des éléments de start à end :

```js
const range = (start, end) => {
  let length = end - start + 1;
  /*
  	Crée un tableau d'une certaine longueur et définit les éléments à l'intérieur de celui-ci de
    la valeur de départ à la valeur de fin.
  */
  return Array.from({ length }, (_, idx) => idx + start);
};
```

Enfin, nous allons implémenter la logique principale en gardant à l'esprit les cas ci-dessus.

```js
export const usePagination = ({
  totalCount,
  pageSize,
  siblingCount = 1,
  currentPage
}) => {
  const paginationRange = useMemo(() => {
    const totalPageCount = Math.ceil(totalCount / pageSize);

    // Le nombre de pages est déterminé comme siblingCount + firstPage + lastPage + currentPage + 2*DOTS
    const totalPageNumbers = siblingCount + 5;

    /*
      Cas 1 :
      Si le nombre de pages est inférieur au nombre de pages que nous voulons afficher dans notre
      composant de pagination, nous retournons la plage [1..totalPageCount]
    */
    if (totalPageNumbers >= totalPageCount) {
      return range(1, totalPageCount);
    }
	
    /*
    	Calculer les indices des siblings gauche et droite et s'assurer qu'ils sont dans la plage 1 et totalPageCount
    */
    const leftSiblingIndex = Math.max(currentPage - siblingCount, 1);
    const rightSiblingIndex = Math.min(
      currentPage + siblingCount,
      totalPageCount
    );

    /*
      Nous ne montrons pas de points lorsque qu'il y a juste un numéro de page à insérer entre les extrémités du sibling et les limites de page c'est-à-dire 1 et totalPageCount. Par conséquent, nous utilisons leftSiblingIndex > 2 et rightSiblingIndex < totalPageCount - 2
    */
    const shouldShowLeftDots = leftSiblingIndex > 2;
    const shouldShowRightDots = rightSiblingIndex < totalPageCount - 2;

    const firstPageIndex = 1;
    const lastPageIndex = totalPageCount;

    /*
    	Cas 2 : Pas de points à gauche à montrer, mais des points à droite à montrer
    */
    if (!shouldShowLeftDots && shouldShowRightDots) {
      let leftItemCount = 3 + 2 * siblingCount;
      let leftRange = range(1, leftItemCount);

      return [...leftRange, DOTS, totalPageCount];
    }

    /*
    	Cas 3 : Pas de points à droite à montrer, mais des points à gauche à montrer
    */
    if (shouldShowLeftDots && !shouldShowRightDots) {
      
      let rightItemCount = 3 + 2 * siblingCount;
      let rightRange = range(
        totalPageCount - rightItemCount + 1,
        totalPageCount
      );
      return [firstPageIndex, DOTS, ...rightRange];
    }
    
    /*
    	Cas 4 : Les points à gauche et à droite doivent être montrés
    */
    if (shouldShowLeftDots && shouldShowRightDots) {
      let middleRange = range(leftSiblingIndex, rightSiblingIndex);
      return [firstPageIndex, DOTS, ...middleRange, DOTS, lastPageIndex];
    }
  }, [totalCount, pageSize, siblingCount, currentPage]);

  return paginationRange;
};

```

L'idée de l'implémentation est que nous identifions la plage de nombres que nous voulons afficher dans notre composant de pagination, puis nous les joignons avec les séparateurs ou DOTS lorsque nous retournons la plage finale.

Pour le premier scénario où notre `totalPageCount` est inférieur au nombre total de boutons que nous avons calculé en fonction des autres paramètres, nous retournons simplement une plage de nombres `1..totalPageCount`.

Pour les autres scénarios, nous identifions si nous avons besoin de DOTS sur le côté gauche ou droit de la `currentPage` en calculant les indices gauche et droit après avoir inclus les boutons siblings à la `currentPage`, puis nous prenons nos décisions.

Une fois que nous savons où nous voulons afficher les DOTS, le reste des calculs est assez simple.

## Comment implémenter le composant de pagination

Comme je l'ai mentionné précédemment, nous allons utiliser le hook `usePagination` dans notre composant de pagination et nous allons mapper la plage retournée pour les afficher.

Nous créons un fichier `Pagination.js` dans notre dossier `src` et implémentons la logique du code comme suit :

```js
import React from 'react';
import classnames from 'classnames';
import { usePagination, DOTS } from './usePagination';
import './pagination.scss';
const Pagination = props => {
  const {
    onPageChange,
    totalCount,
    siblingCount = 1,
    currentPage,
    pageSize,
    className
  } = props;

  const paginationRange = usePagination({
    currentPage,
    totalCount,
    siblingCount,
    pageSize
  });

  // Si la plage de pagination contient moins de 2 éléments, nous ne rendons pas le composant
  if (currentPage === 0 || paginationRange.length < 2) {
    return null;
  }

  const onNext = () => {
    onPageChange(currentPage + 1);
  };

  const onPrevious = () => {
    onPageChange(currentPage - 1);
  };

  let lastPage = paginationRange[paginationRange.length - 1];
  return (
    <ul
      className={classnames('pagination-container', { [className]: className })}
    >
       {/* Flèche de navigation gauche */}
      <li
        className={classnames('pagination-item', {
          disabled: currentPage === 1
        })}
        onClick={onPrevious}
      >
        <div className="arrow left" />
      </li>
      {paginationRange.map(pageNumber => {
         
        // Si le pageItem est un DOT, rendre le caractère unicode DOTS
        if (pageNumber === DOTS) {
          return <li className="pagination-item dots">&#8230;</li>;
        }
		
        // Rendre nos boutons de page
        return (
          <li
            className={classnames('pagination-item', {
              selected: pageNumber === currentPage
            })}
            onClick={() => onPageChange(pageNumber)}
          >
            {pageNumber}
          </li>
        );
      })}
      {/*  Flèche de navigation droite */}
      <li
        className={classnames('pagination-item', {
          disabled: currentPage === lastPage
        })}
        onClick={onNext}
      >
        <div className="arrow right" />
      </li>
    </ul>
  );
};

export default Pagination;

```

Nous ne rendons pas de composant `Pagination` s'il y a moins de deux pages (et nous retournons alors `null`).

Nous rendons le composant `Pagination` sous forme de liste avec des flèches gauche et droite qui gèrent les actions précédentes et suivantes de l'utilisateur. Entre les flèches, nous mappons la `paginationRange` et rendons les numéros de page en tant que `pagination-items`. Si l'élément de page est un DOT, nous rendons un caractère unicode pour celui-ci.

En tant que gestion spéciale, nous ajoutons une classe `disabled` à la flèche gauche/droite si la `currentPage` est la première ou la dernière page, respectivement. Nous désactivons les `pointer-events` et mettons à jour les styles des icônes de flèche via CSS si l'icône doit être désactivée. 

Nous ajoutons également des gestionnaires d'événements de clic aux boutons de page qui invoqueront la fonction de rappel `onPageChanged` avec la valeur mise à jour de `currentPage`. 

Notre fichier CSS contiendra les styles suivants :

```css
.pagination-container {
  display: flex;
  list-style-type: none;

  .pagination-item {
    padding: 0 12px;
    height: 32px;
    text-align: center;
    margin: auto 4px;
    color: rgba(0, 0, 0, 0.87);
    display: flex;
    box-sizing: border-box;
    align-items: center;
    letter-spacing: 0.01071em;
    border-radius: 16px;
    line-height: 1.43;
    font-size: 13px;
    min-width: 32px;

    &.dots:hover {
      background-color: transparent;
      cursor: default;
    }
    &:hover {
      background-color: rgba(0, 0, 0, 0.04);
      cursor: pointer;
    }

    &.selected {
      background-color: rgba(0, 0, 0, 0.08);
    }

    .arrow {
      &::before {
        position: relative;
        /* top: 3pt; Décommentez ceci pour abaisser les icônes comme demandé dans les commentaires*/
        content: '';
        /* En utilisant une échelle em, les flèches seront dimensionnées avec la police */
        display: inline-block;
        width: 0.4em;
        height: 0.4em;
        border-right: 0.12em solid rgba(0, 0, 0, 0.87);
        border-top: 0.12em solid rgba(0, 0, 0, 0.87);
      }

      &.left {
        transform: rotate(-135deg) translate(-50%);
      }

      &.right {
        transform: rotate(45deg);
      }
    }

    &.disabled {
      pointer-events: none;

      .arrow::before {
        border-right: 0.12em solid rgba(0, 0, 0, 0.43);
        border-top: 0.12em solid rgba(0, 0, 0, 0.43);
      }

      &:hover {
        background-color: transparent;
        cursor: default;
      }
    }
  }
}

```

**Et c'est tout !**  
  
Notre implémentation générique de pagination est prête et nous pouvons l'utiliser n'importe où dans notre base de code. 

## Comment utiliser le composant de pagination personnalisé 

En tant que dernière étape, incorporons ce composant dans un petit exemple.   
  
Pour le cadre de cet article, nous allons afficher des données statiques sous forme de tableau. Alors, allons-y et faisons cela d'abord :

```js
import React from 'react';
import data from './data/mock-data.json';

export default function App() {
  return (
    <>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>PRÉNOM</th>
            <th>NOM</th>
            <th>EMAIL</th>
            <th>TÉLÉPHONE</th>
          </tr>
        </thead>
        <tbody>
          {data.map(item => {
            return (
              <tr>
                <td>{item.id}</td>
                <td>{item.first_name}</td>
                <td>{item.last_name}</td>
                <td>{item.email}</td>
                <td>{item.phone}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </>
  );
}
```

À ce stade, notre interface utilisateur ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/InfiniteTable-1.gif)

Maintenant, pour incorporer le composant `Pagination`, nous avons besoin de deux choses. 

* Premièrement, nous maintenons un état `currentPage`.
* Deuxièmement, nous calculons les données à afficher pour une page donnée et nous les mappons simplement et les affichons. 

Pour les besoins de cette démonstration, nous garderons la `PageSize` constante et définirons sa valeur à `10`. Nous pouvons également fournir un sélecteur pour que l'utilisateur sélectionne la `pageSize` souhaitée.  
  
Une fois que nous avons apporté ces modifications, nous pouvons aller de l'avant et afficher notre composant `Pagination` avec les props appropriées.

Avec ces modifications à l'esprit, notre code final sera le suivant :

```js
import React, { useState, useMemo } from 'react';
import Pagination from '../Pagination';
import data from './data/mock-data.json';
import './style.scss';

let PageSize = 10;

export default function App() {
  const [currentPage, setCurrentPage] = useState(1);

  const currentTableData = useMemo(() => {
    const firstPageIndex = (currentPage - 1) * PageSize;
    const lastPageIndex = firstPageIndex + PageSize;
    return data.slice(firstPageIndex, lastPageIndex);
  }, [currentPage]);

  return (
    <>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>PRÉNOM</th>
            <th>NOM</th>
            <th>EMAIL</th>
            <th>TÉLÉPHONE</th>
          </tr>
        </thead>
        <tbody>
          {currentTableData.map(item => {
            return (
              <tr>
                <td>{item.id}</td>
                <td>{item.first_name}</td>
                <td>{item.last_name}</td>
                <td>{item.email}</td>
                <td>{item.phone}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <Pagination
        className="pagination-bar"
        currentPage={currentPage}
        totalCount={data.length}
        pageSize={PageSize}
        onPageChange={page => setCurrentPage(page)}
      />
    </>
  );
}


```

Voici une démonstration en direct de ce tutoriel :

%[https://stackblitz.com/edit/react-1zaeqk?file=src%2FPagination.js]

## Conclusion

Dans cet article, nous avons créé un hook React personnalisé `usePagination` et l'avons utilisé dans notre composant `Pagination`. Nous avons également implémenté une courte démonstration qui utilisait ce composant.

Vous pouvez consulter le code source complet de ce tutoriel dans [ce dépôt GitHub](https://github.com/mayankshubham/react-pagination).

Si vous avez des questions ou des suggestions concernant cet article, n'hésitez pas à [me contacter sur Twitter](https://twitter.com/mayank_shubham).  
  
Merci d'avoir lu.