---
title: Navigation dynamique dans Next.js – Comment rendre les éléments de navigation
  dynamiques dans une application Next
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-16T17:32:33.000Z'
originalURL: https://freecodecamp.org/news/dynamic-navigation-in-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/dynamic-nav-cover.jpg
tags:
- name: Next.js
  slug: nextjs
- name: Web Applications
  slug: web-applications
- name: Web Development
  slug: web-development
seo_title: Navigation dynamique dans Next.js – Comment rendre les éléments de navigation
  dynamiques dans une application Next
seo_desc: 'By Caleb Olojo

  I''ve lately been noticing a pattern in React applications: developers protect certain
  routes on a web app from unauthorized users.

  In such cases, the navigation item (nav-item) on the navigation bar/Header of the
  web won''t be visible t...'
---

Par Caleb Olojo

J'ai récemment remarqué un schéma dans les applications React : les développeurs protègent certaines routes d'une application web contre les utilisateurs non autorisés.

Dans de tels cas, l'élément de navigation (nav-item) sur la barre de navigation/En-tête du web ne sera pas visible pour un utilisateur non autorisé.

Dans ce court guide, nous allons voir comment faire cela dans NextJS. Nous allons rendre un nav-item dynamiquement sur la barre de navigation d'une simple page web que nous allons construire ici.

### Prérequis

Avant de lire cet article plus avant, vous devriez avoir quelques connaissances de base sur :

* Comment React fonctionne
* NextJS, un framework prêt pour la production de React.
* Le rendu conditionnel dans React.
* La vérification des PropTypes dans React
* Les instructions d'import et d'export en JavaScript. Vous pouvez consulter cet [article](https://seven.hashnode.dev/understanding-import-and-export-statements-in-javascript) pour vous familiariser avec cela.

## Getting Started

Puisque cet article se concentre sur Next.js, nous allons commencer par créer un projet Next.js. Tapez la commande suivante dans votre terminal pour l'installer :

```bash
npx create-next-app [nom-de-votre-webapp/site-web]
```

La commande ci-dessus obtient toutes les dépendances dont nous avons besoin pour faire fonctionner notre application Next en un rien de temps.

Gardez à l'esprit que la structure de fichiers d'une application Next est assez différente de l'architecture ubiquitaire create-react-app.

Jetons un coup d'œil aux fichiers importants avec lesquels nous allons interagir dans cet article :

```md
|--pages
|   |-- _app.js
|   |-- index.js
|   |-- about.js
|   |-- blog.js
|   |__ services.js
|--src
|   |-- components
|   |      |-- Header.js
|   |      |__ NavItem.js 
|   |-- data.js
|__
```

La structure de fichiers ci-dessus est un extrait des fichiers dans l'architecture de l'application Next.js. Voyons maintenant ce qui se passe ici.

## Les composants dans notre application Next.js

Nous allons examiner tous les composants que vous voyez ci-dessus et leurs rôles. Nous allons commencer par décomposer les fichiers dans le dossier `pages`.

* `_app.js` : c'est le fichier racine de la base de code. Il est assez similaire au fichier `index.js` dans `create-react-app`. Ici, vous pouvez appliquer n'importe quel style global, ajouter de nouveaux thèmes, fournir un contexte à l'ensemble de l'application, et ainsi de suite.

```js
import Head from "next/head";
import React from "react";

function MyApp({ Component, pageProps }) {
  return (
    <React.Fragment>
      <Head>
        <meta name="theme-color" content="#3c1742" />
      </Head>
      <Component {...pageProps} />
    </React.Fragment>
  );
}

export default MyApp;

```

L'extrait ci-dessus montre le contenu de `_app.js`. Le composant `Head` qui est importé de `"next/head"` nous permet d'ajouter des titres de document aux pages uniques et de nombreuses balises `meta` pour le référencement.

* `index.js` : Nextjs abstrait le besoin de commencer à utiliser `BrowserRouter` de la bibliothèque `react-router-dom` pour configurer les routes dans vos applications. Au lieu de cela, tout fichier qui se trouve dans le dossier `pages` devient une route. `index.js` devient accessible à `https://localhost:3000/` une fois que nous démarrons le serveur de développement avec `npm run dev`.

Vous pourriez remarquer que nous avons déjà importé le composant `Header` du dossier `src/component`. Ne vous inquiétez pas. Nous arriverons à cette section bientôt.

```js
import Head from "next/head";
import Header from "../src/components/Header";

export default function Home() {
  return (
    <>
      <Head>
        <title>Exemples d'articles de Caleb</title>
        <link rel="icon" type="image/ico" href="/img/goals.ico" />
      </Head>
      <Header />
      <section>
        <h1>Page d'accueil</h1>
        <section id="contact">
          <h3 className="section-title">Contactez-nous</h3>
          <p className="section-body">
            Vous pouvez nous contacter via nos différents comptes de réseaux sociaux
          </p>
        </section>
      </HomeWrapper>
    </>
  );
}

```

* Les composants de page restants : `about.js`, `blog.js` et `services.js` peuvent être accessibles à `http://localhost:3000/about`, `http://localhost:3000/blog` et `http://localhost:3000/about` respectivement

## Comment mapper les éléments de tableau sur le composant Header

Au lieu de coder en dur l'interface utilisateur de la barre de navigation, nous pouvons utiliser la fonction `map()` de JavaScript pour rendre une liste d'éléments sur le composant Header.

Pour ce faire, nous devons nous rendre dans le fichier `data.js` dans le dossier `src: source`. Nous allons créer un tableau d'objets qui contiendra les informations ou éléments que nous souhaitons rendre.

L'extrait ci-dessous montre la liste des éléments que nous voulons rendre. Remarquez que le dernier objet a une propriété `path` qui est assez différente des autres. Au lieu d'une valeur `"/contact"`, il a une valeur `"#contact"`. Cela est dû au fait que la section de contact est sur la page d'accueil.

```js
export const navLinks = [
  { name: "Accueil", 
   path: "/" 
  },
  {
    name: "À propos",
    path: "/about",
  },
  {
    name: "Services",
    path: "/services",
  },
  {
    name: "Blog",
    path: "/blog",
  },
  {
    name: "Contactez-nous",
    path: "#contact",
  },
];
```

Continuons pour créer le composant Header en mappant le tableau d'objets que nous avons dans `data.js`. Pour ce faire, nous devons importer le tableau de ce fichier afin de pouvoir accéder à ses propriétés.

```js
import React from "react";
import { navLinks } from "../utils/data";
import Link from "next/link";

export default function Header() {
  return (
    <header>
      <div className="brand">
        <h3>Exemple</h3>
      </div>
      <nav>
        {navLinks.map((link, index) => {
          return (
            <ul>
              <Link href={link.path}>
                <li key={index}>{link.name}</li>
              </Link>
            </ul>
          );
        })}
      </nav>
    </header>
  );
}

```

Avec ce que nous avons dans l'extrait ci-dessus, si nous cliquons sur le nav-item **"Contactez-nous"**, la route actuelle sera : `https://localhost:3000/#contact`.

Le navigateur fait défiler jusqu'à l'élément HTML qui a un id de "contact". Si une telle section n'existe pas, rien n'est défilé dans la fenêtre d'affichage.

C'est pourquoi nous devons rendre ce nav-item particulier uniquement sur les pages qui ont la section correspondante. Voyons comment y parvenir dans la section suivante.

## Comment rendre conditionnellement le Nav-Item avec le hook `useRouter` de Next.js

Nous devons savoir quand une autre page/route est actuellement active ou "en vue" dans un onglet du navigateur afin que nous puissions définir une condition pour rendre le nav-item dans la page appropriée.

Heureusement pour nous, le hook `useRouter` de Next nous permet de le faire. Voyons comment :

```js
import React from "react";
import { useRouter } from "next/router";
import propTypes from "prop-types";

const NavItem = ({ item }) => {
  const router = useRouter();
  return <>{router.pathname === "/" ? item : ""}</>;
};

export default NavItem;

// vérification des proptypes
NavItem.propTypes = {
  item: propTypes.string,
};
```

L'extrait ci-dessus est assez simple. Nous passons `item` en tant que props au composant `NavItem` afin qu'il soit dynamique à utiliser dans n'importe quel cas, pas seulement pour le nav-item de contact.

Voyez comment nous avons assigné le hook `useRouter()` à la variable `router` ? Avec cela, nous pouvons accéder aux propriétés du hook lui-même. Vous pouvez lire à propos des propriétés du hook [ici](https://nextjs.org/docs/api-reference/next/router#router-object).

```js
router.pathname === "/" ? item : ""
```

L'opération ternaire ci-dessus vérifie si le `pathname` de la page est égal à la page d'accueil, c'est-à-dire `"/"`.

Si le résultat est vrai, il assigne la valeur en tant que props au composant (qui sera toujours une chaîne de caractères, en raison de la vérification de validation des props). Sinon, il assigne une chaîne vide au composant, ce qui se traduit par rien dans le composant Header.

## Dernières retouches

Maintenant, modifions le dernier élément du tableau `navLinks` pour qu'il ressemble à ce qui suit :

```js
import NavLink from "./NavLink";

export const navLinks = [
  { name: "Accueil", 
   path: "/" 
  },
  {
    name: "À propos",
    path: "/about",
  },
  {
    name: "Services",
    path: "/services",
  },
  {
    name: "Blog",
    path: "/blog",
  },
  {
    name: <NavLink item="Contactez-nous" />,
    path: "#contact",
  },
];
```

## Conclusion

Voici le résultat final de ce que nous avons construit. Vous verrez que j'ai ajouté du contenu pour illustrer le comportement de défilement fluide vers la section de contact.

Au clic sur les autres routes, le nav-item de contact n'est plus sur l'en-tête.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/fixed.gif)

Merci d'avoir lu cet article ! J'espère qu'il vous a aidé à comprendre comment rendre l'UI dynamiquement, en fonction de certaines conditions. N'hésitez pas à partager cet article avec vos pairs.