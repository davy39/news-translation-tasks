---
title: Comment utiliser le répertoire App dans Next.js
subtitle: ''
author: Quincy Oghenetejiri Ukumakube
co_authors: []
series: null
date: '2024-02-15T00:52:55.000Z'
originalURL: https://freecodecamp.org/news/app-directory-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Freecodecamp-Banner-2.png
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
seo_title: Comment utiliser le répertoire App dans Next.js
seo_desc: 'When you''re building a project using the latest version of Next.js, you''ll
  be prompted to select between using the app/ directory or the pages/ directory.
  The app/ directory is now the recommended way of building apps in Next.js.

  In this article, you...'
---

Lorsque vous construisez un projet en utilisant la dernière version de Next.js, vous serez invité à choisir entre l'utilisation du répertoire `app/` ou du répertoire `pages/`. Le répertoire `app/` est désormais la méthode recommandée pour construire des applications dans Next.js.

Dans cet article, vous apprendrez à maximiser le potentiel du répertoire `app` dans Next.js en découvrant ses fonctionnalités disponibles.

## Table des matières

* [Le dossier `app/`](#heading-le-dossier-app)
* [Layout](#heading-layout) 
* [Routing](#heading-routing) 
* [Utilisation des polices](#heading-utilisation-des-polices)
* [Composant Loading](#heading-le-fichier-loadingjsx) 
* [Composant Error](#heading-le-fichier-errorjsx) 
* [Composant Not-Found](https://www.freecodecamp.org/news/p/eef6be7d-0a78-4259-8106-3994bb8268c1/the-not-found-jsx-file)
* [Composant Template](#heading-le-fichier-templatejsx)
* [Composant Serveur](#heading-composants-serveur)

## Le dossier `app/` 

Le répertoire `app/` dans Next.js offre de nombreuses fonctionnalités, contrairement au répertoire `pages/`. Certaines de ces fonctionnalités incluent :  

* Layout
* Routing 
* Utilisation des polices
* Composant Loading
* Composant Error 
* Composant Not Found
* Composant Template
* Composant Serveur

### Layout 

L'utilisation de `Layout` dans le répertoire `app/` simplifie la création d'interfaces complexes qui permettent des modèles de routage avancés, évitent les re-rendus coûteux et maintiennent l'état à travers les navigations.

Dans le répertoire `app/`, vous pouvez utiliser la fonction `Layout` en créant un fichier `layout.jsx` à la racine du répertoire `app/`. Cela définit une interface utilisateur (UI) qui est partagée à travers plusieurs emplacements. 

Un layout peut rendre un autre layout ou une page à l'intérieur. Chaque fois qu'une route change vers un composant dans le layout, son état est préservé car le composant layout ne se démonte pas.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Layout-Screenshot-.png)
_Une image montrant un layout imbriqué dans le répertoire app_

#### Comment ajouter des balises meta aux Layouts

Les balises meta sont de petites pièces d'information qui fournissent des détails sur une page web aux navigateurs et aux moteurs de recherche. 

Pour ajouter des balises meta à votre application lorsque vous utilisez le répertoire `app/` dans Next.js, vous pouvez utiliser les métadonnées dans le fichier `layout.js`. Les métadonnées sont exportées depuis le fichier, comme dans l'extrait de code suivant :

```javascript
export const metadata = {
  title: 'Titre Mot-clé',
  description: 'N'importe quel Mot-clé,Un autre Mot-clé, Plus de Mots-clés ',
};
```

Remplacer la balise meta du layout principal est crucial lorsque vous souhaitez avoir des balises meta différentes pour chaque route. Pour les remplacer, vous devez exporter la variable `metadata` depuis le fichier de route où vous souhaitez que la balise meta prenne effet.

#### Il n'y a pas de fichier `_app.js`

Le fichier `_app.jsx` a disparu du répertoire `app/`. Comme vous l'avez peut-être anticipé, nous allons stocker tout sous le fichier `layout.jsx`, qui est le layout de base lors de l'utilisation du répertoire `app/` dans Next.js.

Si, par exemple, vous souhaitez utiliser Chakra UI, vous devrez placer le fournisseur dans le fichier `layout.jsx`. Voici un extrait de code de la documentation Chakra montrant comment lier le fournisseur au fichier de layout :

```javascript 
// app/providers.tsx
'use client'

import { ChakraProvider } from '@chakra-ui/react'

export function Providers({ children }: { children: React.ReactNode }) {
  return <ChakraProvider>{children}</ChakraProvider>
}
```

```javascript
// app/layout.tsx
import { Providers } from './providers'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode,
}) {
  return (
    <html lang='en'>
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
```

### Routing 

Le routage dans le répertoire `app/` implique l'utilisation d'un routage strictement basé sur les dossiers. Cela diffère du répertoire `pages/`, qui permet l'utilisation d'un routage basé sur les fichiers ou les dossiers.

Le routage basé sur les dossiers implique la création d'un dossier où le nom de la route doit correspondre au nom du dossier, puis la création d'un fichier `page.js` qui référence l'URL `/` de ce dossier. 

Par exemple, si vous créez un dossier appelé `about`, et qu'un `page.js` est créé dans ce dossier, en supposant que vous utilisez toujours un serveur de développement, l'URL sera `localhost:3000/about`. De même, tout dossier créé n'importe où dans le répertoire `app/` suivra ce modèle.

#### Routage imbriqué 

Les routes imbriquées dans le répertoire `app/` impliquent la création ou l'imbrication de dossiers dans d'autres. Puisque chaque dossier dans le répertoire `app/` correspond à une route, avec le fichier `page.js` dans le dossier respectif pointant vers l'URL `/` de ce dossier, vous pouvez créer des routes imbriquées en plaçant des dossiers dans d'autres dossiers.

Par exemple, le chemin d'URL `/dashboard/analytics` correspondrait à une structure de dossiers comme `app/dashboard/analytics`, avec un fichier `page.js` présent dans le dossier `analytics` pour rendre la route publiquement accessible.

#### Groupe de routes 

En raison de l'approche basée sur les dossiers du répertoire app, chaque dossier contenant un fichier `page.js` est automatiquement considéré comme une route pour cette application. 

Pour éviter d'utiliser le nom du dossier directement dans la route, vous pouvez enfermer le nom du dossier entre parenthèses, comme `(nom_du_dossier)`, ce qui regroupe efficacement les routes sous ce nom. Vous pouvez voir cela représenté visuellement dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Pictures-Showing-the-routing-done-in-next-14.png)
_Image illustrant le groupe de routes_

### Utilisation des polices 

Dans Next.js 12, l'installation des polices dans le répertoire `page/` implique de copier le lien de la feuille de style de la police dans le fichier CSS. 

Mais dans Next.js 13, le processus dans le répertoire `app/` implique l'utilisation du mot-clé `import` pour importer n'importe quelle police de votre choix depuis `next/font/google`. Après l'importation, le sous-ensemble de la police est initialisé et stocké dans une variable qui est ensuite ajoutée à la balise body en tant que classe. 

```javascript
//importation des polices 
import { Inter } from 'next/font/google';

//initialisation d'une variable 
const inter = Inter({ subsets: ['latin'] });



export default function RootLayout({ children }) {


  return (
    <>
      <html lang="en">
        //Ajout de la variable en tant que classe à la balise body
        <body className={inter.className}>
            {children}
        </body>
      </html>
    </>
  );
}

```

#### Comment créer un favicon

De même, la manière dont nous importons les polices dans Next.js a évolué depuis son introduction, et il en va de même pour la méthode de création d'un favicon. 

Dans le répertoire `app/`, la création d'un favicon dans Next.js implique soit la création, soit le remplacement du fichier `favicon.ico` situé dans le dossier racine du répertoire app par l'image que vous souhaitez utiliser. Notez que si votre image est dans un autre format, tel que JPG, PNG ou SVG, vous devez la convertir au format ICO.

### Le fichier `loading.jsx`.  

L'utilisation d'un composant de chargement est une fonctionnalité utile dans Next.js, où vous pouvez obtenir la fonction de chargement simplement en créant un fichier nommé `loading.jsx` dans le dossier désigné. Cela est particulièrement utile lorsque vous récupérez des données depuis une API et que vous devez afficher un état de chargement en attendant la réponse. 

Vous pouvez créer un fichier `loading.jsx` qui définit son état à 'loading' en attendant la réponse de l'API.

Voici un exemple de ce à quoi un fichier `loading.jsx` pourrait ressembler :

```javascript 
// app/loading.jsx 
const loadingPage = ()=>{
    return (
        <div className="loader">
            <div id="loader-wrapper">
                <div id="loader">
                <img src="/img/Spinner-1s-120px.gif"/>
                </div>
                <div className="loader-section section-left">
                
                </div>
                <div className="loader-section section-right"></div>
        
    
      </div>
        </div>

    )
}

export default loadingPage
```

### Le fichier `error.jsx`.

Le fichier `error.jsx` est un fichier spécial utilisé pour gérer les erreurs côté serveur. Il fait partie des nouvelles fonctionnalités de gestion des erreurs introduites dans la version 13.4 de Next.js. 

Ce fichier est destiné à remplacer les traditionnels fichiers `pages/error.js` ou `pages/_error.js` pour gérer les erreurs de manière plus centralisée. 

Un avantage principal est que ce fichier peut gérer à la fois les erreurs côté client et côté serveur. Il peut recevoir une prop `statusCode` pour déterminer le type d'erreur qui s'est produit et afficher le message ou le style approprié.

Voici un exemple de ce à quoi un fichier `error.jsx` pourrait ressembler :

```javascript
// app/error.jsx
function Error({ statusCode }) {
  return (
    <div>
      <h1>Erreur</h1>
      <p>Une erreur {statusCode} s'est produite sur le serveur</p>
    </div>
  );
}

Error.getInitialProps = ({ res, err }) => {
  const statusCode = res ? res.statusCode : err ? err.statusCode :  404;
  return { statusCode };
};

export default Error;

```

Dans l'exemple ci-dessus, le composant `Error` reçoit une prop `statusCode`, qui est déterminée dans la méthode `getInitialProps`. Cette méthode vérifie s'il y a un objet de réponse (`res`), un objet d'erreur (`err`), ou par défaut `404` si aucun n'est présent. Le code d'état est ensuite affiché dans la page d'erreur.

### **Le fichier `not-found.jsx`**

Le fichier `not-found.jsx` est une convention de fichier spéciale utilisée pour gérer les cas où un utilisateur navigue vers une route qui n'existe pas dans cette application. Il est généralement utilisé pour rendre une page "Non trouvée" personnalisée lorsqu'une ressource demandée ne peut pas être trouvée.

Voici un exemple de ce à quoi un `not-found.jsx` pourrait ressembler :

```javascript
// app/not-found.jsx
import Link from 'next/link';

export default function NotFound() {
  return (
    <div>
      <h2>Non trouvé</h2>
      <p>La page que vous cherchiez n'existe pas.</p>
      <Link href="/">Retour à l'accueil</Link>
    </div>
  );
}

```

### Le fichier `template.jsx`. 

Imaginez que vous avez une boîte de blocs LEGO, et que vous voulez construire différents types de voitures. Un fichier `template.jsx` dans Next.js est comme un plan spécial qui vous aide à construire ces voitures. Chaque voiture a un design différent, mais elles suivent toutes les mêmes règles de base de construction.

Le fichier `template.jsx` indique à Next.js comment assembler les pièces pour chaque page de votre site web. Tout comme vous pourriez utiliser un plan simple pour construire de nombreuses voitures, le fichier `template.jsx` donne des instructions pour construire de nombreuses pages web.

Chaque fois que vous voulez créer une nouvelle page, vous suivriez le plan. Mais contrairement à un plan normal, celui-ci est effacé après avoir terminé la page, donc vous commencez frais avec une nouvelle page. C'est pourquoi il est appelé un "template" - c'est quelque chose que vous utilisez comme point de départ pour construire autre chose.

Parfois, vous pourriez vouloir ajouter une fonctionnalité spéciale à une seule voiture, comme un pare-chocs phosphorescent. Dans Next.js, vous pourriez faire cela avec un fichier `template.jsx` en ajoutant un morceau de code spécial juste pour cette page. Après avoir terminé, vous oublierez la fonctionnalité spéciale car le plan est effacé.

Donc, en résumé, un fichier `template.jsx` est comme un livre de règles spécial qui vous aide à créer différentes pages sur votre site web, et il commence frais pour chaque nouvelle page que vous créez.

#### En quoi est-il différent du fichier layout.jsx ?

Dans Next.js, `template.jsx` et `layout.jsx` sont tous deux utilisés pour envelopper les pages et fournir une structure commune, mais ils se comportent différemment en matière de navigation et de préservation de l'état.

**Layouts (`layout.jsx`)**: Ceux-ci sont persistants et maintiennent leur état à travers différentes routes. Ils sont idéaux pour les éléments qui doivent rester les mêmes et cohérents tout au long de la navigation, tels que les en-têtes, les pieds de page et les barres latérales. 

Les layouts minimisent les re-rendus et aident à améliorer les performances puisqu'ils ne se remontent pas et ne se re-rendent pas lors de la navigation.

**Templates (`template.jsx`)**: Ceux-ci ne sont pas persistants et créent une nouvelle instance pour chacun de leurs enfants lors de la navigation. Cela signifie que lorsque l'utilisateur navigue entre des routes qui partagent un template, une nouvelle instance du composant est montée, les éléments DOM sont recréés et l'état n'est pas préservé. 

Les templates sont utiles lorsque vous devez isoler les composants du partage d'état ou de comportements, ou lorsque vous devez déclencher certains effets ou changements d'état chaque fois qu'un utilisateur navigue vers un composant. 

Par exemple, ils sont adaptés pour collecter des commentaires avec un formulaire géré par `useState` unique à chaque page ou pour suivre les vues de page avec `useEffect`.

En essence, les layouts sont pour les éléments cohérents et étatiques, tandis que les templates sont pour les composants distincts et indépendants de l'état qui nécessitent un état frais à chaque navigation. Vous choisirez les layouts pour l'efficacité et la cohérence, et les templates pour les composants isolés et indépendants de l'état qui nécessitent un état frais lors de la navigation.

### Composants Serveur 

Les composants serveur sont désormais l'état par défaut du répertoire app dans Next.js. Ils vous permettent d'effectuer un rendu côté serveur dans votre application front-end, ce qui réduit la quantité de code JavaScript envoyé au client.

Certains des avantages de l'utilisation des composants serveur incluent :

* Récupération de données
* Sécurité
* Mise en cache
* Tailles de bundle
* Optimisation pour les moteurs de recherche et partage sur les réseaux sociaux

#### Rendu côté serveur (SSR) vs composants serveur dans Next.js

Les différences clés entre ces deux méthodes résident dans leur utilisation (pages vs. app), leur impact sur la taille du bundle côté client, et le niveau de contrôle qu'elles offrent sur le rendu. 

Les composants serveur offrent un moyen de tirer parti de la logique côté serveur sans le surcoût du SSR traditionnel, ce qui peut conduire à de meilleures performances et maintenabilité pour les applications web modernes.

De plus, bien que le SSR et les composants serveur rendent côté serveur, ces derniers ne supportent pas l'interactivité—un processus connu sous le nom d'hydratation—avec JS, et par conséquent, les gestionnaires d'événements et les fonctionnalités React telles que useState, useEffect, et autres opérations DOM ne fonctionnent pas avec eux. 

Vous pouvez accéder à ces fonctionnalités en convertissant le composant serveur par défaut en un composant client en plaçant la directive `useClient` en haut du code.

## Conclusion

Le répertoire `app/` dans Next.js offre un ensemble robuste de fonctionnalités conçues pour améliorer l'expérience du développeur et optimiser les performances des applications. 

En tirant parti du répertoire `app/`, vous pouvez profiter pleinement des dernières avancées dans Next.js, telles que le composant `Layout` pour gérer la cohérence de l'UI et la préservation de l'état, le routage basé sur les dossiers pour une navigation rationalisée, et la capacité d'importer des polices et de créer des favicons avec facilité.

L'introduction de fichiers spéciaux comme `loading.jsx`, `error.jsx`, et `not-found.jsx` fournit une approche centralisée pour gérer les états de chargement, les erreurs, et les routes inexistantes, respectivement. 

De plus, le fichier `template.jsx` agit comme un plan pour la construction de pages web, offrant de la flexibilité pour des designs de pages uniques tout en assurant une structure cohérente. 

Les composants serveur, désormais par défaut dans le répertoire `app/`, offrent également des avantages significatifs.

À ce stade, vous êtes suffisamment confiant pour utiliser ces fonctionnalités dans la construction d'applications puissantes, évolutives et maintenables avec Next.js.



###