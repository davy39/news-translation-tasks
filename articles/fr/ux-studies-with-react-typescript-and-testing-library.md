---
title: Comment créer une excellente expérience utilisateur avec React, TypeScript
  et la React Testing Library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-22T09:30:00.000Z'
originalURL: https://freecodecamp.org/news/ux-studies-with-react-typescript-and-testing-library
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/cover-2.jpg
tags:
- name: 'automation testing '
  slug: automation-testing
- name: JavaScript
  slug: javascript
- name: react hooks
  slug: react-hooks
- name: react testing library
  slug: react-testing-library
- name: React
  slug: reactjs
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Comment créer une excellente expérience utilisateur avec React, TypeScript
  et la React Testing Library
seo_desc: 'By TK

  I''m always willing to learn, no matter how much I know. As a software engineer,
  my thirst for knowledge has increased a lot. I know that I have a lot of things
  to learn daily.

  But before I could learn more, I wanted to master the fundamentals. ...'
---

Par TK

Je suis toujours prêt à apprendre, peu importe ce que je sais. En tant qu'ingénieur logiciel, ma soif de connaissances a beaucoup augmenté. Je sais que j'ai beaucoup de choses à apprendre quotidiennement.

Mais avant de pouvoir en apprendre davantage, je voulais maîtriser les fondamentaux. Pour devenir un meilleur développeur, je voulais comprendre davantage comment créer de grandes expériences produit.

Cet article est ma tentative d'illustrer une preuve de concept (PoC) que j'ai construite pour essayer quelques idées.

J'avais quelques sujets en tête pour ce projet. Il devait :

* Utiliser un logiciel de haute qualité
* Offrir une excellente expérience utilisateur

Lorsque je parle de logiciel de haute qualité, cela peut signifier tant de choses différentes. Mais je voulais me concentrer sur trois parties :

* Code propre : Strive pour écrire un code lisible par l'homme qui est facile à lire et simple à maintenir. Séparer la responsabilité des fonctions et des composants.
* Bonne couverture de test : Il ne s'agit pas vraiment de couverture. Il s'agit de tests qui couvrent les parties importantes du comportement des composants sans connaître trop de détails sur l'implémentation.
* Gestion d'état cohérente : Je voulais construire avec un logiciel qui permet à l'application d'avoir des données cohérentes. La prévisibilité est importante.

L'expérience utilisateur était le principal objectif de cette PoC. Le logiciel et les techniques seraient la fondation qui permettrait une bonne expérience pour les utilisateurs.

Pour rendre l'état cohérent, je voulais un système de types. J'ai donc choisi TypeScript. C'était ma première fois à utiliser Typescript avec React. Ce projet m'a également permis de construire des hooks personnalisés et de les tester correctement.

## Installation du projet

Je suis tombé sur cette bibliothèque appelée [tsdx](https://github.com/jaredpalmer/tsdx) qui configure toute la configuration Typescript pour vous. Elle est principalement utilisée pour construire des packages. Comme il s'agissait d'un simple projet parallèle, je n'ai pas hésité à l'essayer.

Après l'avoir installée, j'ai choisi le modèle React et j'étais prêt à coder. Mais avant la partie amusante, je voulais également configurer la configuration des tests. J'ai utilisé la [React Testing Library](https://github.com/testing-library/react-testing-library) comme bibliothèque principale avec [jest-dom](https://github.com/testing-library/jest-dom) pour fournir quelques méthodes personnalisées (j'aime vraiment le `toBeInTheDocument` matcher).

Avec tout cela installé, j'ai écrasé la configuration jest en ajoutant un nouveau `jest.config.js` :

```typescript
module.exports = {
  verbose: true,
  setupFilesAfterEnv: ["./setupTests.ts"],
};
```

Et un `setupTests.ts` pour importer tout ce dont j'avais besoin.

```typescript
import "@testing-library/jest-dom";
```

Dans ce cas, je n'avais que la bibliothèque `jest-dom` à importer. Ainsi, je n'avais pas besoin d'importer ce package dans mes fichiers de test. Maintenant, cela fonctionne directement.

Pour tester cette installation et cette configuration, j'ai construit un simple composant :

```typescript
export const Thing = () => <h1>Je suis TK</h1>;
```

Dans mon test, je voulais le rendre et voir s'il était dans le DOM.

```typescript
import React from 'react';
import { render } from '@testing-library/react';
import { Thing } from '../index';

describe('Thing', () => {
  it('affiche le texte correct dans le document', () => {
    const { getByText } = render(<Thing />);

    expect(getByText("Je suis TK")).toBeInTheDocument();
  });
});
```

Maintenant, nous sommes prêts pour l'étape suivante.

## Configuration des routes

Ici, je voulais avoir seulement deux routes pour l'instant. La page d'accueil et la page de recherche - même si je ne ferai rien pour la page d'accueil.

Pour ce projet, j'utilise la bibliothèque `react-router-dom` pour gérer tout ce qui concerne le routeur. C'est simple, facile et amusant à utiliser.

Après l'avoir installée, j'ai ajouté les composants du routeur dans le `app.typescript`.

```typescript
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

export const App = () => (
  <Router>
    <Switch>
      <Route path="/search">
        <h1>C'est la recherche !</h1>
      </Route>
      <Route path="/">
        <h1>C'est l'accueil</h1>
      </Route>
    </Switch>
  </Router>
);
```

Maintenant, si nous entrons dans `localhost:1234`, nous voyons le titre `C'est l'accueil`. Allez dans `localhost:1234/search`, et nous verrons le texte `C'est la recherche !`.

Avant de continuer à implémenter notre page de recherche, je voulais construire un simple menu pour basculer entre les pages d'accueil et de recherche sans manipuler l'URL. Pour ce projet, j'utilise [Material UI](https://material-ui.com/) pour construire la fondation de l'UI.

Pour l'instant, nous installons simplement `@material-ui/core`.

Pour construire le menu, nous avons le bouton pour ouvrir les options du menu. Dans ce cas, ce sont les options "accueil" et "recherche".

Mais pour construire une meilleure abstraction de composant, je préfère cacher le contenu (lien et libellé) pour les éléments de menu et faire en sorte que le composant `Menu` reçoive ces données en tant que prop. Ainsi, le menu ne connaît pas les éléments, il va simplement itérer à travers la liste des éléments et les rendre.

Cela ressemble à ceci :

```typescript
import React, { Fragment, useState, MouseEvent } from 'react';
import { Link } from 'react-router-dom';
import Button from '@material-ui/core/Button';
import MuiMenu from '@material-ui/core/Menu';
import MuiMenuItem from '@material-ui/core/MenuItem';

import { MenuItem } from '../../types/MenuItem';

type MenuPropsType = { menuItems: MenuItem[] };

export const Menu = ({ menuItems }: MenuPropsType) => {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  const handleClick = (event: MouseEvent<HTMLButtonElement>): void => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = (): void => {
    setAnchorEl(null);
  };

  return (
    <Fragment>
      <Button aria-controls="menu" aria-haspopup="true" onClick={handleClick}>
        Ouvrir le Menu
      </Button>
      <MuiMenu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        {menuItems.map((item: MenuItem) => (
          <Link to={item.linkTo} onClick={handleClose} key={item.key}>
            <MuiMenuItem>{item.label}</MuiMenuItem>
          </Link>
        ))}
      </MuiMenu>
    </Fragment>
  );
};

export default Menu;
```

Ne paniquez pas ! Je sais que c'est un gros bloc de code, mais c'est assez simple. Le `Fragment` enveloppe le `Button` et `MuiMenu` (`Mui` signifie Material UI. J'ai dû renommer le composant car le composant que je construis s'appelle aussi menu).

Il reçoit les `menuItems` en tant que prop et les mappe pour construire l'élément de menu enveloppé par le composant `Link`. Link est un composant de react-router pour lier à une URL donnée.

Le comportement du menu est également simple : nous lions la fonction `handleClick` au `onClick` du bouton. Ainsi, nous pouvons changer `anchorEl` lorsque le bouton est déclenché (ou cliqué si vous préférez). Le `anchorEl` est simplement un état de composant qui représente l'élément de menu Mui pour ouvrir le commutateur de menu. Il ouvrira donc les éléments de menu pour laisser l'utilisateur choisir l'un d'entre eux.

Maintenant, comment utilisons-nous ce composant ?

```typescript
import { Menu } from './components/Menu';
import { MenuItem } from './types/MenuItem';

const menuItems: MenuItem[] = [
  {
    linkTo: '/',
    label: 'Accueil',
    key: 'link-to-home',
  },
  {
    linkTo: '/search',
    label: 'Recherche',
    key: 'link-to-search',
  },
];

<Menu menuItems={menuItems} />
```

Les `menuItems` sont une liste d'objets. L'objet a le contrat correct attendu par le composant `Menu`. Le type `MenuItem` garantit que le contrat est correct. C'est juste un type Typescript :

```typescript
export type MenuItem = {
  linkTo: string;
  label: string;
  key: string;
};
```

## Recherche

Maintenant, nous sommes prêts à construire la page de recherche avec tous les produits et une excellente expérience. Mais avant de construire la liste des produits, je voulais créer une fonction de récupération pour gérer la demande de produits. Comme je n'ai pas encore d'API de produits, je peux simplement simuler la demande de récupération.

Au début, j'ai simplement construit la récupération avec `useEffect` dans le composant `Search`. L'idée serait la suivante :

```typescript
import React, { useState, useEffect } from 'react';
import { getProducts } from 'api';

export const Search = () => {
  const [products, setProducts] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        setIsLoading(true);

        const fetchedProducts = await getProducts();

        setIsLoading(false);
        setProducts(fetchedProducts);
      } catch (error) {
        setIsLoading(false);
        setHasError(true);
      }
    };

    fetchProducts();
  }, []);
};
```

J'ai :

* `products` initialisé comme un tableau vide
* `isLoading` initialisé comme faux
* `hasError` initialisé comme faux
* Le `fetchProducts` est une fonction asynchrone qui appelle `getProducts` depuis le module `api`. Comme nous n'avons pas encore d'API propre pour les produits, ce `getProducts` retournerait des données simulées.
* Lorsque le `fetchProducts` est exécuté, nous définissons le `isLoading` à vrai, récupérons les produits, puis définissons le `isLoading` à faux, car la récupération est terminée, et définissons les produits récupérés dans `products` pour être utilisés dans le composant.
* Si une erreur se produit lors de la récupération, nous les capturons, définissons le `isLoading` à faux, et le `hasError` à vrai. Dans ce contexte, le composant saura que nous avons eu une erreur lors de la récupération et pourra gérer ce cas.
* Tout est encapsulé dans un `useEffect` car nous effectuons un effet secondaire ici.

Pour gérer toute la logique d'état (quand mettre à jour chaque partie pour le contexte spécifique), nous pouvons l'extraire dans un simple réducteur.

```typescript
import { State, FetchActionType, FetchAction } from './types';

export const fetchReducer = (state: State, action: FetchAction): State => {
  switch (action.type) {
    case FetchActionType.FETCH_INIT:
      return {
        ...state,
        isLoading: true,
        hasError: false,
      };
    case FetchActionType.FETCH_SUCCESS:
      return {
        ...state,
        hasError: false,
        isLoading: false,
        data: action.payload,
      };
    case FetchActionType.FETCH_ERROR:
      return {
        ...state,
        hasError: true,
        isLoading: false,
      };
    default:
      return state;
  }
};
```

L'idée ici est de séparer chaque type d'action et de gérer chaque mise à jour d'état. Ainsi, le `fetchReducer` recevra l'état et l'action et retournera un nouvel état. Cette partie est intéressante car elle obtient l'état actuel puis retourne un nouvel état, mais nous conservons le contrat d'état en utilisant le type `State`.

Et pour chaque type d'action, nous mettrons à jour l'état de la bonne manière.

* `FETCH_INIT` : `isLoading` est vrai et `hasError` est faux.
* `FETCH_SUCCESS` : `hasError` est faux, `isLoading` est faux, et les données (produits) sont mises à jour.
* `FETCH_ERROR` : `hasError` est vrai et `isLoading` est faux.

En cas de non-correspondance avec un type d'action, retourne simplement l'état actuel.

Le `FetchActionType` est une simple énumération Typescript :

```typescript
export enum FetchActionType {
  FETCH_INIT = 'FETCH_INIT',
  FETCH_SUCCESS = 'FETCH_SUCCESS',
  FETCH_ERROR = 'FETCH_ERROR',
}
```

Et le `State` est juste un simple type :

```typescript
export type ProductType = {
  name: string;
  price: number;
  imageUrl: string;
  description: string;
  isShippingFree: boolean;
  discount: number;
};

export type Data = ProductType[];

export type State = {
  isLoading: boolean;
  hasError: boolean;
  data: Data;
};
```

Avec ce nouveau réducteur, nous pouvons maintenant utiliser `useReducer` dans notre fetch. Nous lui passons le nouveau réducteur et l'état initial :

```typescript
const initialState: State = {
  isLoading: false,
  hasError: false,
  data: fakeData,
};

const [state, dispatch] = useReducer(fetchReducer, initialState);

useEffect(() => {
  const fetchAPI = async () => {
    dispatch({ type: FetchActionType.FETCH_INIT });

    try {
      const payload = await fetchProducts();

      dispatch({
        type: FetchActionType.FETCH_SUCCESS,
        payload,
      });
    } catch (error) {
      dispatch({ type: FetchActionType.FETCH_ERROR });
    }
  };

  fetchAPI();
}, []);
```

L'`initialState` a le même type de contrat. Et nous le passons à `useReducer` avec le `fetchReducer` que nous venons de construire. Le `useReducer` fournit l'état et une fonction appelée `dispatch` pour appeler des actions afin de mettre à jour notre état.

* État de récupération : dispatch `FETCH_INIT`
* Fin de la récupération : dispatch `FETCH_SUCCESS` avec la charge utile des produits
* Obtenir une erreur lors de la récupération : dispatch `FETCH_ERROR`

Cette abstraction est devenue très grande et peut être très verbeuse dans notre composant. Nous pourrions l'extraire en tant que hook séparé appelé `useProductFetchAPI`.

```typescript
export const useProductFetchAPI = (): State => {
  const initialState: State = {
    isLoading: false,
    hasError: false,
    data: fakeData,
  };

  const [state, dispatch] = useReducer(fetchReducer, initialState);

  useEffect(() => {
    const fetchAPI = async () => {
      dispatch({ type: FetchActionType.FETCH_INIT });

      try {
        const payload = await fetchProducts();

        dispatch({
          type: FetchActionType.FETCH_SUCCESS,
          payload,
        });
      } catch (error) {
        dispatch({ type: FetchActionType.FETCH_ERROR });
      }
    };

    fetchAPI();
  }, []);

  return state;
};
```

Ce n'est qu'une fonction qui enveloppe notre opération de récupération. Maintenant, dans le composant `Search`, nous pouvons l'importer et l'appeler.

```
export const Search = () => {
  const { isLoading, hasError, data }: State = useProductFetchAPI();
};
```

Nous avons toute l'API : `isLoading`, `hasError`, et `data` à utiliser dans notre composant. Avec cette API, nous pouvons rendre un spinner de chargement ou un squelette basé sur les données `isLoading`. Nous pouvons rendre un message d'erreur basé sur la valeur `hasError`. Ou simplement rendre la liste des produits en utilisant les `data`.

Avant de commencer à implémenter notre liste de produits, je veux m'arrêter et ajouter des tests pour notre hook personnalisé. Nous avons deux parties à tester ici : le réducteur et le hook personnalisé.

Le réducteur est plus facile car ce n'est qu'une fonction pure. Il reçoit une valeur, la traite et retourne une nouvelle valeur. Aucun effet secondaire. Tout est déterministe.

Pour couvrir toutes les possibilités de ce réducteur, j'ai créé trois contextes : les actions `FETCH_INIT`, `FETCH_SUCCESS` et `FETCH_ERROR`.

Avant d'implémenter quoi que ce soit, j'ai configuré les données initiales à utiliser.

```typescript
const initialData: Data = [];
const initialState: State = {
  isLoading: false,
  hasError: false,
  data: initialData,
};
```

Maintenant, je peux passer cet état initial au réducteur avec l'action spécifique que je veux couvrir. Pour ce premier test, je voulais couvrir l'action `FETCH_INIT` :

```typescript
describe('quand dispatch FETCH_INIT action', () => {
  it('retourne isLoading à vrai sans aucune erreur', () => {
    const action: FetchAction = {
      type: FetchActionType.FETCH_INIT,
    };

    expect(fetchReducer(initialState, action)).toEqual({
      isLoading: true,
      hasError: false,
      data: initialData,
    });
  });
});
```

C'est assez simple. Il reçoit l'état initial et l'action, et nous attendons la valeur de retour appropriée : le nouvel état avec `isLoading` à `true`.

Le `FETCH_ERROR` est assez similaire :

```typescript
describe('quand dispatch FETCH_ERROR action', () => {
  it('retourne isLoading à vrai sans aucune erreur', () => {
    const action: FetchAction = {
      type: FetchActionType.FETCH_ERROR,
    };

    expect(fetchReducer(initialState, action)).toEqual({
      isLoading: false,
      hasError: true,
      data: [],
    });
  });
});
```

Mais nous passons une action différente et attendons que `hasError` soit `true`.

Le `FETCH_SUCCESS` est un peu plus complexe car nous devons simplement construire un nouvel état et ajouter l'attribut payload dans l'action.

```typescript
describe('quand dispatch FETCH_SUCCESS action', () => {
  it('retourne les données de l\'API', () => {
    const product: ProductType = {
      name: 'iPhone',
      price: 3500,
      imageUrl: 'image-url.png',
      description: 'Téléphone mobile Apple',
      isShippingFree: true,
      discount: 0,
    };

    const action: FetchAction = {
      type: FetchActionType.FETCH_SUCCESS,
      payload: [product],
    };

    expect(fetchReducer(initialState, action)).toEqual({
      isLoading: false,
      hasError: false,
      data: [product],
    });
  });
});
```

Mais rien de trop complexe ici. Les nouvelles données sont là. Une liste de produits. Dans ce cas, un seul, le produit iPhone.

Le deuxième test couvrira le hook personnalisé que nous avons construit. Dans ces tests, j'ai écrit trois contextes : une requête de délai d'attente, une requête réseau échouée et une requête réussie.

Ici, comme j'utilise `axios` pour récupérer des données (quand j'aurai une API pour récupérer les données, je l'utiliserai correctement), j'utilise `axios-mock-adapter` pour simuler chaque contexte pour nos tests.

La configuration d'abord : Initialisation de nos données et configuration d'un mock axios.

```typescript
const mock: MockAdapter = new MockAdapter(axios);
const url: string = '/search';
const initialData: Data = [];
```

Nous commençons à implémenter un test pour la requête de délai d'attente :

```typescript
it('gère l\'erreur sur la requête API en timeout', async () => {
  mock.onGet(url).timeout();

  const { result, waitForNextUpdate } = renderHook(() =>
    useProductFetchAPI(url, initialData)
  );

  await waitForNextUpdate();

  const { isLoading, hasError, data }: State = result.current;

  expect(isLoading).toEqual(false);
  expect(hasError).toEqual(true);
  expect(data).toEqual(initialData);
});
```

Nous configurons le mock pour retourner un timeout. Le test appelle `useProductFetchAPI`, attend une mise à jour, puis nous pouvons obtenir l'état. Le `isLoading` est faux, les `data` sont toujours les mêmes (une liste vide), et le `hasError` est maintenant vrai comme prévu.

La requête réseau est presque la même. La seule différence est que le mock aura une erreur réseau au lieu d'un timeout.

```typescript
it('gère l\'erreur sur la requête API réseau échouée', async () => {
  mock.onGet(url).networkError();

  const { result, waitForNextUpdate } = renderHook(() =>
    useFetchAPI(url, initialData)
  );

  await waitForNextUpdate();

  const { isLoading, hasError, data }: State = result.current;

  expect(isLoading).toEqual(false);
  expect(hasError).toEqual(true);
  expect(data).toEqual(initialData);
});
```

Et pour le cas de succès, nous devons créer un objet produit pour l'utiliser comme données de réponse de requête. Nous attendons également que les `data` soient une liste de cet objet produit. Le `hasError` et le `isLoading` sont faux dans ce cas.

```typescript
it('obtient et met à jour les données de la requête API', async () => {
  const product: ProductType = {
    name: 'iPhone',
    price: 3500,
    imageUrl: 'image-url.png',
    description: 'Téléphone mobile Apple',
    isShippingFree: true,
    discount: 0,
  };

  const mockedResponseData: Data = [product];

  mock.onGet(url).reply(200, mockedResponseData);

  const { result, waitForNextUpdate } = renderHook(() =>
    useFetchAPI(url, initialData)
  );

  await waitForNextUpdate();

  const { isLoading, hasError, data }: State = result.current;

  expect(isLoading).toEqual(false);
  expect(hasError).toEqual(false);
  expect(data).toEqual([product]);
});
```

Super. Nous avons couvert tout ce dont nous avions besoin pour ce hook personnalisé et le réducteur que nous avons créé. Maintenant, nous pouvons nous concentrer sur la construction de la liste des produits.

## Liste des produits

L'idée de la liste des produits est de lister les produits qui ont certaines informations : titre, description, prix, remise et s'il y a une livraison gratuite. La carte produit finale ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-06-at-15.52.17.png)

Pour construire cette carte, j'ai créé la base pour le composant produit :

```typescript
const Product = () => (
  <Box>
    <Image />
    <TitleDescription/>
    <Price />
    <Tag />
  </Box>
);
```

Pour construire le produit, nous devons construire chaque composant qui se trouve à l'intérieur.

Mais avant de commencer à construire le composant produit, je veux montrer les données `JSON` que l'API simulée nous retournera.

```typescript
{
  imageUrl: 'a-url-for-tokyo-tower.png',
  name: 'Tokyo Tower',
  description: 'Some description here',
  price: 45,
  discount: 20,
  isShippingFree: true,
}
```

Ces données sont passées du composant `Search` au composant `ProductList` :

```typescript
export const Search = () => {
  const { isLoading, hasError, data }: State = useProductFetchAPI();

  if (hasError) {
    return <h2>Erreur</h2>;
  }

  return <ProductList products={data} isLoading={isLoading} />;
};
```

Comme j'utilise Typescript, je peux imposer les types statiques pour les props du composant. Dans ce cas, j'ai la prop `products` et `isLoading`.

J'ai construit un type `ProductListPropsType` pour gérer les props de la liste des produits.

```typescript
type ProductListPropsType = {
  products: ProductType[];
  isLoading: boolean;
};
```

Et le `ProductType` est un simple type représentant le produit :

```typescript
export type ProductType = {
  name: string;
  price: number;
  imageUrl: string;
  description: string;
  isShippingFree: boolean;
  discount: number;
};
```

Pour construire le ProductList, j'utiliserai le composant `Grid` de Material UI. D'abord, nous avons un conteneur de grille et ensuite, pour chaque produit, nous rendrons un élément de grille.

```typescript
export const ProductList = ({ products, isLoading }: ProductListPropsType) => (
  <Grid container spacing={3}>
    {products.map(product => (
      <Grid
        item
        xs={6}
        md={3}
        key={`grid-${product.name}-${product.description}-${product.price}`}
      >
        <Product
          key={`product-${product.name}-${product.description}-${product.price}`}
          imageUrl={product.imageUrl}
          name={product.name}
          description={product.description}
          price={product.price}
          discount={product.discount}
          isShippingFree={product.isShippingFree}
          isLoading={isLoading}
        />
      </Grid>
    ))}
  </Grid>
);
```

L'élément `Grid` affichera 2 éléments par ligne pour les mobiles car nous utilisons la valeur `6` pour chaque colonne. Et pour la version desktop, il rendra 4 éléments par ligne.

Nous itérons à travers la liste `products` et rendons le composant `Product` en passant toutes les données dont il aura besoin.

Maintenant, nous pouvons nous concentrer sur la construction du composant `Product`.

Commençons par le plus simple : le `Tag`. Nous passerons trois données à ce composant. `label`, `isVisible`, et `isLoading`. Lorsqu'il n'est pas visible, nous retournons simplement `null` pour ne pas le rendre. S'il est en cours de chargement, nous rendrons un composant `Skeleton` de Material UI. Mais après le chargement, nous rendons les informations de l'étiquette avec le libellé `Free Shipping`.

```typescript
export const Tag = ({ label, isVisible, isLoading }: TagProps) => {
  if (!isVisible) return null;
  if (isLoading) {
    return (
      <Skeleton width="110px" height="40px" data-testid="tag-skeleton-loader" />
    );
  }

  return (
    <Box mt={1} data-testid="tag-label-wrapper">
      <span style={tabStyle}>{label}</span>
    </Box>
  );
};
```

Le `TagProps` est un simple type :

```typescript
type TagProps = {
  label: string;
  isVisible: boolean;
  isLoading: boolean;
};
```

J'utilise également un objet pour styliser le `span` :

```typescript
const tabStyle = {
  padding: '4px 8px',
  backgroundColor: '#f2f3fe',
  color: '#87a7ff',
  borderRadius: '4px',
};
```

Je voulais également construire des tests pour ce composant en essayant de penser à son comportement :

* lorsqu'il n'est pas visible : le tag ne sera pas dans le document.

```typescript
describe('quand il n\'est pas visible', () => {
  it('ne rend rien', () => {
    const { queryByTestId } = render(
      <Tag label="un label" isVisible={false} isLoading={false} />
    );

    expect(queryByTestId('tag-label-wrapper')).not.toBeInTheDocument();
  });
});
```

* lorsqu'il est en cours de chargement : le squelette sera dans le document.

```typescript
describe('quand il est en cours de chargement', () => {
  it('rend le label du tag', () => {
    const { queryByTestId } = render(
      <Tag label="un label" isVisible isLoading />
    );

    expect(queryByTestId('tag-skeleton-loader')).toBeInTheDocument();
  });
});
```

* lorsqu'il est prêt à être rendu : le tag sera dans le document.

```typescript
describe('quand il est visible et non en cours de chargement', () => {
  it('rend le label du tag', () => {
    render(<Tag label="un label" isVisible isLoading={false} />);

    expect(screen.getByText('un label')).toBeInTheDocument();
  });
});
```

* point bonus : accessibilité. J'ai également construit un test automatisé pour couvrir les violations d'accessibilité en utilisant `jest-axe`.

```typescript
it('n\'a pas de violations d\'accessibilité', async () => {
  const { container } = render(
    <Tag label="un label" isVisible isLoading={false} />
  );

  const results = await axe(container);

  expect(results).toHaveNoViolations();
});
```

Nous sommes prêts à implémenter un autre composant : le `TitleDescription`. Il fonctionnera presque de la même manière que le composant `Tag`. Il reçoit certaines props : `name`, `description`, et `isLoading`.

Comme nous avons le type `Product` avec la définition de type pour `name` et `description`, je voulais le réutiliser. J'ai essayé différentes choses - et vous pouvez [regarder ici pour plus de détails](https://leandrotk.github.io/tk/2020/05/typescript-learnings-interesting-types/index.html) - et j'ai trouvé le type `Pick`. Avec cela, j'ai pu obtenir le `name` et le `description` du `ProductType` :

```typescript
type TitleDescriptionType = Pick<ProductType, 'name' | 'description'>;
```

Avec ce nouveau type, j'ai pu créer le `TitleDescriptionPropsType` pour le composant :

```typescript
type TitleDescriptionPropsType = TitleDescriptionType & {
  isLoading: boolean;
};
```

Maintenant, en travaillant à l'intérieur du composant, si `isLoading` est vrai, le composant rend le composant squelette approprié avant de rendre les textes de titre et de description réels.

```typescript
if (isLoading) {
  return (
    <Fragment>
      <Skeleton
        width="60%"
        height="24px"
        data-testid="name-skeleton-loader"
      />
      <Skeleton
        style={descriptionSkeletonStyle}
        height="20px"
        data-testid="description-skeleton-loader"
      />
    </Fragment>
  );
}
```

Si le composant n'est plus en cours de chargement, nous rendons les textes de titre et de description. Ici, nous utilisons le composant `Typography`.

```typescript
return (
  <Fragment>
    <Typography data-testid="product-name">{name}</Typography>
    <Typography
      data-testid="product-description"
      color="textSecondary"
      variant="body2"
      style={descriptionStyle}
    >
      {description}
    </Typography>
  </Fragment>
);
```

Pour les tests, nous voulons trois choses :

* lorsqu'il est en cours de chargement, le composant rend les squelettes
* lorsqu'il n'est plus en cours de chargement, le composant rend les textes
* s'assurer que le composant ne viole pas l'accessibilité

Nous utiliserons la même idée que pour les tests `Tag` : voir s'il est dans le document ou non en fonction de l'état.

Lorsqu'il est en cours de chargement, nous voulons voir si le squelette est dans le document, mais que les textes de titre et de description ne le sont pas.

```typescript
describe('quand il est en cours de chargement', () => {
  it('ne rend rien', () => {
    const { queryByTestId } = render(
      <TitleDescription
        name={product.name}
        description={product.description}
        isLoading
      />
    );

    expect(queryByTestId('name-skeleton-loader')).toBeInTheDocument();
    expect(queryByTestId('description-skeleton-loader')).toBeInTheDocument();
    expect(queryByTestId('product-name')).not.toBeInTheDocument();
    expect(queryByTestId('product-description')).not.toBeInTheDocument();
  });
});
```

Lorsqu'il n'est plus en cours de chargement, il rend les textes dans le DOM :

```typescript
describe('quand le chargement est terminé', () => {
  it('rend le nom et la description du produit', () => {
    render(
      <TitleDescription
        name={product.name}
        description={product.description}
        isLoading={false}
      />
    );

    expect(screen.getByText(product.name)).toBeInTheDocument();
    expect(screen.getByText(product.description)).toBeInTheDocument();
  });
});
```

Et un simple test pour couvrir les problèmes d'accessibilité :

```typescript
it('n\'a pas de violations d\'accessibilité', async () => {
  const { container } = render(
    <TitleDescription
      name={product.name}
      description={product.description}
      isLoading={false}
    />
  );

  const results = await axe(container);

  expect(results).toHaveNoViolations();
});
```

Le composant suivant est le `Price`. Dans ce composant, nous fournirons un squelette lorsqu'il est encore en cours de chargement comme nous l'avons fait dans l'autre composant, et nous ajouterons trois composants différents ici :

* `PriceWithDiscount` : nous appliquons la remise au prix d'origine et le rendons
* `OriginalPrice` : il rend simplement le prix du produit
* `Discount` : il rend le pourcentage de remise lorsque le produit a une remise

Mais avant de commencer à implémenter ces composants, je voulais structurer les données à utiliser. Les valeurs `price` et `discount` sont des nombres. Alors, construisons une fonction appelée `getPriceInfo` qui reçoit le `price` et le `discount` et qui retournera ces données :

```typescript
{
  priceWithDiscount,
  originalPrice,
  discountOff,
  hasDiscount,
};
```

Avec ce contrat de type :

```typescript
type PriceInfoType = {
  priceWithDiscount: string;
  originalPrice: string;
  discountOff: string;
  hasDiscount: boolean;
};
```

Dans cette fonction, elle obtiendra le `discount` et le transformera en un `boolean`, puis appliquera le `discount` pour construire le `priceWithDiscount`, utilisera le `hasDiscount` pour construire le pourcentage de remise, et construira le `originalPrice` avec le signe dollar :

```typescript
export const applyDiscount = (price: number, discount: number): number =>
  price - (price * discount) / 100;

export const getPriceInfo = (
  price: number,
  discount: number
): PriceInfoType => {
  const hasDiscount: boolean = Boolean(discount);
  const priceWithDiscount: string = hasDiscount
    ? `$${applyDiscount(price, discount)}`
    : `$${price}`;

  const originalPrice: string = `$${price}`;
  const discountOff: string = hasDiscount ? `${discount}% OFF` : '';

  return {
    priceWithDiscount,
    originalPrice,
    discountOff,
    hasDiscount,
  };
};
```

Ici, j'ai également construit une fonction `applytDiscount` pour extraire le calcul de la remise.

J'ai ajouté quelques tests pour couvrir ces fonctions. Comme ce sont des fonctions pures, nous devons simplement passer quelques valeurs et attendre de nouvelles données.

Test pour `applyDiscount` :

```typescript
describe('applyDiscount', () => {
  it('applique une remise de 20% sur le prix', () => {
    expect(applyDiscount(100, 20)).toEqual(80);
  });

  it('applique une remise de 95% sur le prix', () => {
    expect(applyDiscount(100, 95)).toEqual(5);
  });
});
```

Test pour `getPriceInfo` :

```typescript
describe('getPriceInfo', () => {
  describe('avec une remise', () => {
    it('retourne les informations de prix correctes', () => {
      expect(getPriceInfo(100, 20)).toMatchObject({
        priceWithDiscount: '$80',
        originalPrice: '$100',
        discountOff: '20% OFF',
        hasDiscount: true,
      });
    });
  });

  describe('sans remise', () => {
    it('retourne les informations de prix correctes', () => {
      expect(getPriceInfo(100, 0)).toMatchObject({
        priceWithDiscount: '$100',
        originalPrice: '$100',
        discountOff: '',
        hasDiscount: false,
      });
    });
  });
});
```

Maintenant, nous pouvons utiliser `getPriceInfo` dans les composants `Price` pour obtenir ces données structurées et les transmettre aux autres composants comme ceci :

```typescript
export const Price = ({ price, discount, isLoading }: PricePropsType) => {
  if (isLoading) {
    return (
      <Skeleton width="80%" height="18px" data-testid="price-skeleton-loader" />
    );
  }

  const {
    priceWithDiscount,
    originalPrice,
    discountOff,
    hasDiscount,
  }: PriceInfoType = getPriceInfo(price, discount);

  return (
    <Fragment>
      <PriceWithDiscount price={priceWithDiscount} />
      <OriginalPrice hasDiscount={hasDiscount} price={originalPrice} />
      <Discount hasDiscount={hasDiscount} discountOff={discountOff} />
    </Fragment>
  );
};
```

Comme nous en avons parlé plus tôt, lorsqu'il est en cours de chargement, nous rendons simplement le composant `Skeleton`. Lorsqu'il termine le chargement, il construira les données structurées et rendra les informations de prix. Construisons chaque composant maintenant !

Commençons par `OriginalPrice`. Nous devons simplement passer le `price` en tant que prop et il le rend avec le composant `Typography`.

```typescript
type OriginalPricePropsType = {
  price: string;
};

export const OriginalPrice = ({ price }: OriginalPricePropsType) => (
  <Typography display="inline" style={originalPriceStyle} color="textSecondary">
    {price}
  </Typography>
);
```

Très simple ! Ajoutons un test maintenant.

Passez simplement un prix et voyez s'il a été rendu dans le DOM :

```typescript
it('affiche le prix', () => {
  const price = '$200';
  render(<OriginalPrice price={price} />);
  expect(screen.getByText(price)).toBeInTheDocument();
});
```

J'ai également ajouté un test pour couvrir les problèmes d'accessibilité :

```typescript
it('n\'a pas de violations d\'accessibilité', async () => {
  const { container } = render(<OriginalPrice price="$200" />);
  const results = await axe(container);

  expect(results).toHaveNoViolations();
});
```

Le composant `PriceWithDiscount` a une implémentation très similaire, mais nous passons le booléen `hasDiscount` pour rendre ce prix ou non. S'il y a une remise, rendre le prix avec la remise. Sinon, il ne rendra rien.

```typescript
type PricePropsType = {
  hasDiscount: boolean;
  price: string;
};
```

Le type de props a le `hasDiscount` et le `price`. Et le composant rend simplement les choses en fonction de la valeur `hasDiscount`.

```typescript
export const PriceWithDiscount = ({ price, hasDiscount }: PricePropsType) => {
  if (!hasDiscount) {
    return null;
  }

  return (
    <Typography display="inline" style={priceWithDiscountStyle}>
      {price}
    </Typography>
  );
};
```

Les tests couvriront cette logique lorsqu'il y a ou non une remise. S'il n'y a pas de remise, les prix ne seront pas rendus.

```typescript
describe('quand le produit n\'a pas de remise', () => {
  it('n\'affiche rien', () => {
    const { queryByTestId } = render(
      <PriceWithDiscount hasDiscount={false} price="" />
    );

    expect(queryByTestId('discount-off-label')).not.toBeInTheDocument();
  });
});
```

S'il y a une remise, elle sera rendue dans le DOM :

```typescript
describe('quand le produit a une remise', () => {
  it('affiche le prix', () => {
    const price = '$200';
    render(<PriceWithDiscount hasDiscount price={price} />);
    expect(screen.getByText(price)).toBeInTheDocument();
  });
});
```

Et comme toujours, un test pour couvrir les violations d'accessibilité :

```typescript
it('n\'a pas de violations d\'accessibilité', async () => {
  const { container } = render(
    <PriceWithDiscount hasDiscount price="$200" />
  );

  const results = await axe(container);

  expect(results).toHaveNoViolations();
});
```

Le composant `Discount` est presque identique au `PriceWithDiscount`. Rendre l'étiquette de remise si le produit a une remise :

```typescript
type DiscountPropsType = {
  hasDiscount: boolean;
  discountOff: string;
};

export const Discount = ({ hasDiscount, discountOff }: DiscountPropsType) => {
  if (!hasDiscount) {
    return null;
  }

  return (
    <Typography
      display="inline"
      color="secondary"
      data-testid="discount-off-label"
    >
      {discountOff}
    </Typography>
  );
};
```

Et tous les tests que nous avons faits pour l'autre composant, nous faisons la même chose pour le composant `Discount` :

```typescript
describe('Discount', () => {
  describe('quand le produit a une remise', () => {
    it('affiche l\'étiquette de remise', () => {
      const discountOff = '20% OFF';
      render(<Discount hasDiscount discountOff={discountOff} />);
      expect(screen.getByText(discountOff)).toBeInTheDocument();
    });
  });

  describe('quand le produit n\'a pas de remise', () => {
    it('n\'affiche rien', () => {
      const { queryByTestId } = render(
        <Discount hasDiscount={false} discountOff="" />
      );

      expect(queryByTestId('discount-off-label')).not.toBeInTheDocument();
    });
  });

  it('n\'a pas de violations d\'accessibilité', async () => {
    const { container } = render(
      <Discount hasDiscount discountOff="20% OFF" />
    );

    const results = await axe(container);

    expect(results).toHaveNoViolations();
  });
});
```

Maintenant, nous allons construire un composant `Image`. Ce composant a le squelette de base comme tout autre composant que nous avons construit. S'il est en cours de chargement, attendez de rendre la source de l'image et rendez le squelette à la place. Lorsqu'il termine le chargement, nous rendrons l'image, mais seulement si le composant est à l'intersection de la fenêtre du navigateur.

Que signifie-t-il ? Lorsque vous êtes sur un site web sur votre appareil mobile, vous verrez probablement les 4 premiers produits. Ils rendront le squelette puis l'image. Mais en dessous de ces 4 produits, comme vous ne voyez aucun d'entre eux, peu importe si nous les rendons ou non. Et nous pouvons choisir de ne pas les rendre. Pas pour l'instant. Mais à la demande. Lorsque vous faites défiler, si l'image du produit est à l'intersection de la fenêtre du navigateur, nous commençons à rendre la source de l'image.

De cette manière, nous gagnons en performance en accélérant le temps de chargement de la page et réduisons le coût en demandant des images à la demande.

Nous utiliserons l'API Intersection Observer pour télécharger des images à la demande. Mais avant d'écrire du code sur cette technologie, commençons par construire notre composant avec l'image et la vue squelette.

Les props de l'image auront cet objet :

```typescript
{
  imageUrl,
  imageAlt,
  width,
  isLoading,
  imageWrapperStyle,
  imageStyle,
}
```

Les props `imageUrl`, `imageAlt`, et `isLoading` sont passées par le composant produit. La `width` est un attribut pour le squelette et la balise image. Les `imageWrapperStyle` et `imageStyle` sont des props qui ont une valeur par défaut dans le composant image. Nous en parlerons plus tard.

Ajoutons un type pour ces props :

```typescript
type ImageUrlType = Pick<ProductType, 'imageUrl'>;
type ImageAttrType = { imageAlt: string; width: string };
type ImageStateType = { isLoading: boolean };
type ImageStyleType = {
  imageWrapperStyle: CSSProperties;
  imageStyle: CSSProperties;
};

export type ImagePropsType = ImageUrlType &
  ImageAttrType &
  ImageStateType &
  ImageStyleType;
```

L'idée ici est de donner un sens aux types puis de tout composer. Nous pouvons obtenir le `imageUrl` du `ProductType`. Le type d'attribut aura le `imageAlt` et le `width`. L'état de l'image a l'état `isLoading`. Et le style de l'image a certaines `CSSProperties`.

Au début, le composant serait comme ceci :

```typescript
export const Image = ({
  imageUrl,
  imageAlt,
  width,
  isLoading,
  imageWrapperStyle,
  imageStyle,
}: ImagePropsType) => {
  if (isLoading) {
    <Skeleton
      variant="rect"
      width={width}
      data-testid="image-skeleton-loader"
    />
  }

  return (
    <img
      src={imageUrl}
      alt={imageAlt}
      width={width}
      style={imageStyle}
    />
  );
};
```

Construisons le code pour faire fonctionner l'observateur d'intersection.

L'idée de l'observateur d'intersection est de recevoir une cible à observer et une fonction de rappel qui est exécutée chaque fois que la cible observée entre ou sort de la fenêtre d'affichage. Ainsi, l'implémentation serait très simple :

```typescript
const observer: IntersectionObserver = new IntersectionObserver(
  onIntersect,
  options
);

observer.observe(target);
```

Instanciez la classe `IntersectionObserver` en passant un objet d'options et la fonction de rappel. L'`observer` observera l'élément `target`.

Comme il s'agit d'un effet dans le DOM, nous pouvons envelopper cela dans un `useEffect`.

```typescript
useEffect(() => {
  const observer: IntersectionObserver = new IntersectionObserver(
    onIntersect,
    options
  );

  observer.observe(target);

  return () => {
    observer.unobserve(target);
  };
}, [target]);
```

En utilisant `useEffect`, nous avons deux choses différentes ici : le tableau de dépendances et la fonction de retour. Nous passons le `target` comme fonction de dépendance pour nous assurer que nous réexécuterons l'effet si le `target` change. Et la fonction de retour est une fonction de nettoyage. React effectue le nettoyage lorsque le composant est démonté, il nettoiera donc l'effet avant d'exécuter un autre effet pour chaque rendu.

Dans cette fonction de nettoyage, nous arrêtons simplement d'observer l'élément `target`.

Lorsque le composant commence à rendre, la référence `target` n'est pas encore définie, nous devons donc avoir une garde pour ne pas observer une `target` indéfinie.

```typescript
useEffect(() => {
  if (!target) {
    return;
  }

  const observer: IntersectionObserver = new IntersectionObserver(
    onIntersect,
    options
  );

  observer.observe(target);

  return () => {
    observer.unobserve(target);
  };
}, [target]);
```

Au lieu d'utiliser cet effet dans notre composant, nous pourrions construire un hook personnalisé pour recevoir la cible, certaines options pour personnaliser la configuration, et il fournirait un booléen indiquant si la cible est à l'intersection de la fenêtre d'affichage ou non.

```typescript
export type TargetType = Element | HTMLDivElement | undefined;
export type IntersectionStatus = {
  isIntersecting: boolean;
};

const defaultOptions: IntersectionObserverInit = {
  rootMargin: '0px',
  threshold: 0.1,
};

export const useIntersectionObserver = (
  target: TargetType,
  options: IntersectionObserverInit = defaultOptions
): IntersectionStatus => {
  const [isIntersecting, setIsIntersecting] = useState(false);

  useEffect(() => {
    if (!target) {
      return;
    }

    const onIntersect = ([entry]: IntersectionObserverEntry[]) => {
      setIsIntersecting(entry.isIntersecting);

			if (entry.isIntersecting) {
        observer.unobserve(target);
      }
    };

    const observer: IntersectionObserver = new IntersectionObserver(
      onIntersect,
      options
    );

    observer.observe(target);

    return () => {
      observer.unobserve(target);
    };
  }, [target]);

  return { isIntersecting };
};
```

Dans notre fonction de rappel, nous définissons simplement si la cible d'entrée intersecte la fenêtre d'affichage ou non. Le `setIsIntersecting` est un setter du hook `useState` que nous définissons en haut de notre hook personnalisé.

Il est initialisé à `false` mais sera mis à jour à `true` s'il intersecte la fenêtre d'affichage.

Avec cette nouvelle information dans le composant, nous pouvons rendre l'image ou non. Si elle intersecte, nous pouvons rendre l'image. Sinon, rendre simplement un squelette jusqu'à ce que l'utilisateur atteigne l'intersection de la fenêtre d'affichage de l'image du produit.

À quoi cela ressemble-t-il en pratique ?

D'abord, nous définissons la référence du wrapper en utilisant `useState` :

```typescript
const [wrapperRef, setWrapperRef] = useState<HTMLDivElement>();
```

Il commence comme `undefined`. Ensuite, construisez un rappel de wrapper pour définir le nœud de l'élément :

```typescript
const wrapperCallback = useCallback(node => {
  setWrapperRef(node);
}, []);
```

Avec cela, nous pouvons l'utiliser pour obtenir la référence du wrapper en utilisant une prop `ref` dans notre `div`.

```typescript
<div ref={wrapperCallback}>
```

Après avoir défini le `wrapperRef`, nous pouvons le passer comme `target` pour notre `useIntersectionObserver` et attendre un statut `isIntersecting` comme résultat :

```typescript
const { isIntersecting }: IntersectionStatus = useIntersectionObserver(wrapperRef);
```

Avec cette nouvelle valeur, nous pouvons construire une valeur booléenne pour savoir si nous rendons le squelette ou l'image du produit.

```typescript
const showImageSkeleton: boolean = isLoading || !isIntersecting;
```

Ainsi, nous pouvons maintenant rendre le nœud approprié au DOM.

```typescript
<div ref={wrapperCallback} style={imageWrapperStyle}>
  {showImageSkeleton ? (
    <Skeleton
      variant="rect"
      width={width}
      height={imageWrapperStyle.height}
      style={skeletonStyle}
      data-testid="image-skeleton-loader"
    />
  ) : (
    <img
      src={imageUrl}
      alt={imageAlt}
      width={width}
    />
  )}
</div>
```

Le composant complet ressemble à ceci :

```typescript
export const Image = ({
  imageUrl,
  imageAlt,
  width,
  isLoading,
  imageWrapperStyle,
}: ImagePropsType) => {
  const [wrapperRef, setWrapperRef] = useState<HTMLDivElement>();
  const wrapperCallback = useCallback(node => {
    setWrapperRef(node);
  }, []);

  const { isIntersecting }: IntersectionStatus = useIntersectionObserver(wrapperRef);
  const showImageSkeleton: boolean = isLoading || !isIntersecting;

  return (
    <div ref={wrapperCallback} style={imageWrapperStyle}>
      {showImageSkeleton ? (
        <Skeleton
          variant="rect"
          width={width}
          height={imageWrapperStyle.height}
          style={skeletonStyle}
          data-testid="image-skeleton-loader"
        />
      ) : (
        <img
          src={imageUrl}
          alt={imageAlt}
          width={width}
        />
      )}
    </div>
  );
};
```

Super, maintenant le chargement à la demande fonctionne bien. Mais je veux construire une expérience légèrement meilleure. L'idée ici est d'avoir deux tailles différentes de la même image. L'image de basse qualité est demandée et nous la rendons visible, mais floue pendant que l'image de haute qualité est demandée en arrière-plan. Lorsque l'image de haute qualité finit enfin de se charger, nous faisons une transition de l'image de basse qualité à l'image de haute qualité avec une transition ease-in/ease-out pour rendre l'expérience fluide.

Construisons cette logique. Nous pourrions construire cela dans le composant, mais nous pourrions également extraire cette logique dans un hook personnalisé.

```typescript
export const useImageOnLoad = (): ImageOnLoadType => {
  const [isLoaded, setIsLoaded] = useState(false);
  const handleImageOnLoad = () => setIsLoaded(true);

  const imageVisibility: CSSProperties = {
    visibility: isLoaded ? 'hidden' : 'visible',
    filter: 'blur(10px)',
    transition: 'visibility 0ms ease-out 500ms',
  };

  const imageOpactity: CSSProperties = {
    opacity: isLoaded ? 1 : 0,
    transition: 'opacity 500ms ease-in 0ms',
  };

  return { handleImageOnLoad, imageVisibility, imageOpactity };
};
```

Ce hook fournit simplement des données et un comportement pour le composant. Le `handleImageOnLoad` dont nous avons parlé plus tôt, le `imageVisibility` pour rendre l'image de basse qualité visible ou non, et le `imageOpactity` pour faire la transition de transparent à opaque, de cette manière nous la rendons visible après l'avoir chargée.

Le `isLoaded` est un simple booléen pour gérer la visibilité des images. Un autre petit détail est le `filter: 'blur(10px)'` pour rendre l'image de basse qualité floue puis lentement mise au point pendant la transition de l'image de basse qualité à l'image de haute qualité.

Avec ce nouveau hook, nous l'importons simplement et l'appelons à l'intérieur du composant :

```typescript
const {
  handleImageOnLoad,
  imageVisibility,
  imageOpactity,
}: ImageOnLoadType = useImageOnLoad();
```

Et commençons à utiliser les données et le comportement que nous avons construits.

```typescript
<Fragment>
  <img
    src={thumbUrl}
    alt={imageAlt}
    width={width}
    style={{ ...imageStyle, ...imageVisibility }}
  />
  <img
    onLoad={handleImageOnLoad}
    src={imageUrl}
    alt={imageAlt}
    width={width}
    style={{ ...imageStyle, ...imageOpactity }}
  />
</Fragment>
```

La première a une image de basse qualité, le `thumbUrl`. La seconde a l'image de haute qualité originale, le `imageUrl`. Lorsque l'image de haute qualité est chargée, elle appelle la fonction `handleImageOnLoad`. Cette fonction fera la transition entre une image et l'autre.

<video width="100%" height="300" controls>
  <source src="https://raw.githubusercontent.com/leandrotk/tk/master/2020/06/ux-studies-with-react-typescript-and-testing-library/assets/loading-japan.mp4" type="video/mp4">
</video>

## Conclusion

Ceci est la première partie de ce projet pour en apprendre davantage sur l'expérience utilisateur, les API natives, le frontend typé et les tests.

Pour la prochaine partie de cette série, nous allons réfléchir de manière plus architecturale pour construire la recherche avec des filtres, tout en gardant à l'esprit d'apporter des solutions techniques pour rendre l'expérience utilisateur aussi fluide que possible.

Vous pouvez trouver d'autres articles comme celui-ci sur [le blog de TK](https://leandrotk.github.io/tk/2020/06/ux-studies-with-react-typescript-and-testing-library/index.html).

## Ressources

* [Lazy Loading Images and Video](https://developers.google.com/web/fundamentals/performance/lazy-loading-guidance/images-and-video)
* [Functional Uses for Intersection Observer](https://css-tricks.com/a-few-functional-uses-for-intersection-observer-to-know-when-an-element-is-in-view/)
* [Tips for rolling your own lazy loading](https://css-tricks.com/tips-for-rolling-your-own-lazy-loading/)
* [Intersection Observer API - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
* [React Typescript Cheatsheet](https://github.com/typescript-cheatsheets/react-typescript-cheatsheet)