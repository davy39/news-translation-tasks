---
title: Comment déstructurer les fondamentaux des Hooks React
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-04-17T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-destructure-the-fundamentals-of-react-hooks-d13ff6ea6871
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6g791iHSFVEe6yZqH9IlIA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment déstructurer les fondamentaux des Hooks React
seo_desc: Hooks have become a pretty powerful new feature of React. They can be intimidating
  if you’re not really sure what’s going on behind the scenes. The beauty is now being
  able to manage state in a simple (and reusable) manner within function components....
---

Les Hooks sont devenus une fonctionnalité assez puissante de React. Ils peuvent être intimidants si vous n'êtes pas vraiment sûr de ce qui se passe en coulisses. La beauté réside désormais dans la possibilité de gérer l'état de manière simple (et réutilisable) au sein des composants de fonction.

Mais pourquoi ne pas utiliser une classe ? Sans trop s'éloigner du sujet, les fonctions offrent une manière plus directe d'écrire vos composants, vous guidant vers une écriture plus propre et plus réutilisable. Bonus : cela rend généralement l'écriture de tests plus facile.

Il existe [de nombreux cas d'utilisation pour les hooks](https://github.com/rehooks/awesome-react-hooks), donc je ne vais pas plonger dans des exemples. Ce ne devrait pas être trop difficile de se mettre à niveau avec quelques lignes rapides. Pour les besoins de cet article, supposons que les cookies du navigateur n'existent pas et que ceux-ci sont du type comestible.

### Plonger dans le bocal à cookies

Ici, nous avons `MyCookies`, un composant de fonction, que nous pouvons considérer comme notre bocal à cookies. Disons que nous voulons garder une trace interne du nombre de cookies que nous avons dans le bocal. Avec la nouvelle API des hooks, nous pouvons ajouter une simple ligne utilisant `useState` pour gérer le travail.

```js
const MyCookies = () => {
  const [ cookies, setCookieCount ] = useState(0);
  ...
};
```

### Attendez, comment sortons-nous les cookies de là ?

Si vous pensez que ce qui précède est magique et que vous vous demandez comment les valeurs dans le tableau sont définies, vous devrez comprendre les bases de la déstructuration des tableaux.

Alors que la déstructuration d'un objet utilisera la même clé où que vous essayiez de l'extraire, les tableaux se déstructurent en utilisant l'ordre des éléments dans le tableau.

```js
const [ one, two ] = [ 1, 2 ];
console.log(one); // 1
console.log(two); // 2
```

Alors que ce qui précède semble les nommer dans un ordre particulier, ce n'est pas le cas comme le montre l'exemple ci-dessous :

```js
const [ two, one ] = [ 1, 2 ];
console.log(two); // 1
console.log(one); // 2
```

Sans trop s'enfoncer dans le terrier technique, `useState` est une fonction qui retourne un tableau que nous déstructurons pour l'utiliser dans notre composant.

Et le 0 à l'intérieur de l'invocation de `useState` lui-même ? C'est simplement la valeur initiale que nous définissons pour l'instance de l'état. Dans ce cas, nous commencerons malheureusement avec 0 cookie.

### En fait, utiliser l'état

Une fois que nous avons notre `cookies` déstructuré et la fonction `setCookiesCount`, nous pouvons commencer à interagir avec l'état local du composant comme vous pourriez le faire en utilisant `setState` dans un composant de classe.

Au moment du rendu, notre valeur `cookies` sera celle de l'invocation de la valeur d'état interne de `useState`, similaire à ce que vous pourriez voir avec `this.state`. Pour mettre à jour cette valeur, nous pouvons simplement appeler `setCookiesCount`.

```js
const MyCookies = () => {
  const [ cookies, setCookieCount ] = useState(0);
  return (
    <>
      <h2>Cookies: { cookies }</h2>
      <button onClick={() => setCookieCount(cookies + 1)} >
        Ajouter un cookie
      </button>
    </>
  );
};
```

Si vous êtes plus habitué à la syntaxe de classe, vous pourriez mettre à jour l'état en utilisant `this.setState` comme suit :

```js
const MyCookies = () => {
  const [ cookies, setCookieCount ] = useState(0);
  useEffect(() => {
    getCookieCount().then((count) => {
      setCookieCount(count);
    })
  });
  ...
};
```

### Comment utiliser les effets

Souvent, les composants ont besoin d'un moyen de créer des effets secondaires qui n'interrompront pas nécessairement le flux fonctionnel d'un composant de fonction. Supposons que nous avons le nombre de cookies que nous avons sauvegardé sur un serveur quelque part, nous pourrions vouloir récupérer ce compte lorsque l'application se charge.

```js
const MyCookies = () => {
  const [ cookies, setCookieCount ] = useState(0);
  useEffect(() => {
    getCookieCount().then((count) => {
      setCookieCount(count);
    })
  }, []);
  ...
};
```

Après que le composant soit rendu, tout ce qui se trouve à l'intérieur de `useEffect` sera exécuté. Tout effet secondaire provenant de `useEffect` ne se produira qu'après la fin du rendu. Cela dit, une fois que `useEffect` est exécuté, nous déclenchons `getCookieCount` et utilisons notre fonction précédente `setCookieCount` pour mettre à jour l'état du composant.

### Attendez, il y a un problème...

Il y a un piège dans le code ci-dessus. Cet effet s'exécutera à chaque fois, effaçant essentiellement toutes les nouvelles incrémentations de notre valeur de cookie à partir de notre bouton Ajouter un cookie d'origine.

Pour contourner cela, nous pouvons définir un 2ème argument pour la fonction `useEffect` qui permet à React de savoir quand l'exécuter à nouveau. Dans notre exemple ci-dessus, définir ce 2ème argument à un tableau vide le fera s'exécuter une seule fois.

```js
const MyCookies = ({cookieType = 'chocolate'}) => {
  const [ cookies, setCookieCount ] = useState(0);
  useEffect(() => {
    getCookieCount().then((count) => {
      setCookieCount(count);
    })
  }, [ cookieType ]);
  ...
};
```

Dans la plupart des cas, vous voudrez passer un tableau de dépendances qui, lorsqu'elles changent, feront que `useEffect` se déclenchera à nouveau. Supposons, par exemple, que vous récupérez le compte d'un type de cookie spécifique et que vous souhaitez obtenir le compte à nouveau si ce type change.

```js
import BasketContext from 'context';

const Basket = ({children}) => {
  return (
    <BasketContext.Provider value={basketItems}>
      <h1>Mon Panier</h1>
      { children }
    </BasketContext.Provider>
  );
}

// MyCookies.js
const MyCookies = ({cookieType = 'chocolate'}) => {
  const basketItems = useContext(BasketContext);
  ...
};
```

Dans le code ci-dessus, chaque fois que notre prop `cookieType` change, React sait que nous dépendons de lui pour notre effet et réexécutera cet effet.

### Essayer de faire usage du contexte

Je ne vais pas [entrer dans les détails de l'API de contexte de React](https://reactjs.org/docs/context.html) car cela est un peu hors sujet. Cependant, si vous êtes familier avec cela, le hook `useContext` vous permet de faire facilement usage de votre contexte depuis votre composant de fonction. Dans le code ci-dessus, étant donné notre contexte déjà créé, nous pouvons immédiatement "utiliser" ledit contexte et collecter les valeurs passées dans notre fournisseur de contexte.

```js
import BasketContext from 'context';

const Basket = ({children}) => {
  return (
    <BasketContext.Provider value={basketItems}>
      <h1>Mon Panier</h1>
      { children }
    </BasketContext.Provider>
  );
}

// MyCookies.js
const MyCookies = ({cookieType = 'chocolate'}) => {
  const basketItems = useContext(BasketContext);
  ...
};
```

### Nettoyer vos hooks

Ce qui rend les hooks encore plus puissants, c'est de les combiner et de les abstraire en asséchant votre code de manière plus propre. En tant que dernier exemple rapide, nous pouvons prendre nos exemples de cookies de `useState` et `useEffect` et les abstraire dans leur propre fonction `use[Name]`, créant ainsi [un hook personnalisé](https://reactjs.org/docs/hooks-custom.html).

```js
// useCookies.js
function useCookies(initialCookieCount) {

  const [ cookies, setCookieCount ] = useState(initialCookieCount);

    useEffect(() => {
    getCookieCount().then((count) => {
      setCookieCount(count);
    })
  }, []);

  function addCookie() {
    setCookieCount(cookies + 1);
    console.log('?');
  }

  function removeCookie() {
    setCookieCount(cookies - 1);
    console.log('?');
  }

  return {
    cookies,
    addCookie,
    removeCookie
  }
};

// MyCookies.js
const MyCookies = () => {
  const { cookies, addCookie, removeCookie } = useCookies(0);
  ...
};
```

Nous avons pu abstraire en toute sécurité notre logique d'état et l'utiliser pour gérer nos cookies.

### Beaucoup plus à découvrir

Ce sont les 3 hooks de base que React nous donne, mais [il y en a beaucoup plus qu'ils fournissent out of the box](https://reactjs.org/docs/hooks-reference.html), tous avec les mêmes principes sous-jacents que la documentation React explique bien.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?
 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">
 Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

_Originalement publié à [https://www.colbyfayock.com/2019/04/destructuring-the-fundamentals-of-react-hooks](https://www.colbyfayock.com/2019/04/destructuring-the-fundamentals-of-react-hooks)._