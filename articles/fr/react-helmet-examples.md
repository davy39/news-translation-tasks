---
title: Comment utiliser React Helmet – Avec un exemple de cas d'utilisation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-05T16:36:10.000Z'
originalURL: https://freecodecamp.org/news/react-helmet-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/react-head-examples.jpg
tags:
- name: React
  slug: react
seo_title: Comment utiliser React Helmet – Avec un exemple de cas d'utilisation
seo_desc: 'By Scott Gary

  Because of the nature of single page applications (SPAs), modifying metadata in
  React apps can be tricky without using a helper library. Lucky for us, that library
  already exists – and it''s called React Helmet.

  Leveraging Helmet for met...'
---

Par Scott Gary

En raison de la nature des applications à page unique (SPA), la modification des métadonnées dans les applications React peut être délicate sans l'utilisation d'une bibliothèque d'aide. Heureusement pour nous, cette bibliothèque existe déjà – et elle s'appelle React Helmet.

L'utilisation de Helmet pour l'inclusion de métadonnées peut considérablement simplifier le processus de création d'une application React optimisée pour le SEO et les réseaux sociaux.

Helmet nous permet d'insérer des métadonnées dans la balise <head> de la même manière que nous le ferions en utilisant la syntaxe HTML standard.

Dans cet article, nous aborderons les étapes suivantes :

1. Comment installer et importer la bibliothèque React Helmet.
2. Utilisation de base pour le rendu côté client et côté serveur (CSR vs SSR).
3. Utilisation plus avancée de Helmet pour configurer un composant SEO.

Afin de comprendre ces sujets, vous devriez avoir une connaissance de base de la bibliothèque React.

## Installation et configuration de React Helmet

Si vous êtes déjà familier avec l'utilisation de React et Node, l'installation de Helmet devrait être un jeu d'enfant.

Cependant, avant de faire une démonstration, il est important de noter que la bibliothèque standard **react-helmet** est désormais considérée comme obsolète. À la place, vous devriez utiliser **react-helmet-async**.

C'est parce que react-helmet entraînait quelques bugs qui provoquaient des fuites de mémoire et une mauvaise intégrité des données. Autant dire que lorsque les développeurs React mentionnent Helmet, ils font presque toujours référence à **react-helmet-async**.

Passons maintenant à l'installation. Naviguez simplement vers le répertoire de votre projet dans le terminal, et installez react-helmet-async avec le gestionnaire de paquets de votre choix. Voici la syntaxe pour yarn et npm :

```
yarn add react-helmet-async
npm i react-helmet-async
```

Une fois l'installation terminée, vous pouvez passer à l'importation et à l'utilisation de la bibliothèque de composants Helmet.

## Concepts de base et utilisation de React Helmet

Les deux composants que nous allons importer de **react-helmet-async** s'appellent **Helmet** et **HelmetProvider**.

1. **HelmetProvider** enveloppera l'ensemble du composant de l'application afin de créer un contexte et d'éviter les fuites de mémoire. Par conséquent, ce composant n'aura besoin d'être importé que dans le composant racine **App**.
2. **Helmet** sera importé dans n'importe quel composant de page où vous souhaitez implémenter des balises méta. Considérez **<Helmet>** comme la balise **<head>** pour la page en question.

Nous allons commencer par une utilisation basique du rendu côté client (CSR) et du rendu côté serveur (SSR). Commençons par voir comment les choses fonctionnent dans une implémentation CSR de base :

```javascript
import React from 'react';
import { HelmetProvider } from 'react-helmet-async';
import NavBar from './NavBar';
import Landing from `./Landing;
export default function App() {
return (
<HelmetProvider>
<NavBar />
<Landing />
</HelmetProvider>
)}
```

Comme vous pouvez le voir, dans le composant **App**, nous avons seulement importé le composant `HelmetProvider` de **react-helmet-async**. C'est assez simple.

L'implémentation SSR est très similaire, avec un petit ajout. Jetons un coup d'œil et voyons si vous pouvez repérer la différence :

```javascript
import React from 'react';
import { HelmetProvider } from 'react-helmet-async';
import NavBar from './NavBar';
import Landing from `./Landing;
export default function App() {
const helmetContext = {};
return (
<HelmetProvider context={helmetContext}>
<NavBar />
<Landing />
</HelmetProvider>
)}
```

Si vous avez remarqué l'ajout de la variable **helmetContext** passée comme prop à notre **HelmetProvider**, vous avez tout juste !

Ce paradigme se retrouve dans la plupart des systèmes de gestion d'état populaires tels que Redux, et aide à garantir que le contexte n'est jamais hors de portée de l'instance actuelle de votre application.

Maintenant, supposons que le composant de page suivant soit la page d'accueil de votre application React :

```javascript
import React from 'react';
import { Helmet } from 'react-helmet-async';
export default function Landing() {
return (
<div>
<Helmet>
<title>Learning React Helmet!</title>
<meta name='description' content='Beginner friendly page for learning React Helmet.' />
</Helmet>
<h1>Cool Landing Page!</h1>
</div>
)
}
```

Un examen rapide du composant de la page Landing montre que nous avons importé le composant **Helmet** et l'avons utilisé pour ajouter les métadonnées _title_ et _description_ à la page.

Nous ajoutons simplement la balise méta équivalente en HTML à l'intérieur du composant Helmet, et le travail d'ajout de celle-ci à la balise HTML **<head>** est géré pour nous.

Génial ! Nous sommes maintenant sur la voie de la création d'une application React optimisée pour le SEO.

## Créer un composant SEO avec React Helmet

Les métadonnées ne concernent pas seulement les résultats de recherche Google. Nous voulons également que les publications sur les réseaux sociaux qui font référence à notre site s'affichent sous forme de jolies cartes d'aperçu.

En ce qui concerne les métadonnées et les balises méta, il existe une multitude de variantes différentes à mémoriser. Facebook utilise les balises **og** (open graph), Twitter utilise sa propre variante **twitter**, et ainsi de suite.

## Comment utiliser les composants pour l'abstraction

Une chose intéressante à propos de la création de composants React avec des props est que vous pouvez réutiliser une prop à l'intérieur du composant comme bon vous semble.

En utilisant cette connaissance, vous pouvez créer un composant appelé SEO qui abstrait l'utilisation des balises de métadonnées couramment utilisées, vous évitant ainsi d'avoir à rechercher chaque variante de balise chaque fois que vous construisez une application optimisée pour le SEO.

Un exemple de composant SEO qui simplifie le processus d'ajout de balises Facebook et Twitter pourrait ressembler à ceci :

```javascript
import React from 'react';
import { Helmet } from 'react-helmet-async';
export default function SEO({title, description, name, type}) {
return (
<Helmet>
{ /* Balises de métadonnées standard */ }
<title>{title}</title>
<meta name='description' content={description} />
{ /* Fin des balises de métadonnées standard */ }
{ /* Balises Facebook */ }
<meta property="og:type" content={type} />
<meta property="og:title" content={title} />
<meta property="og:description" content={description} />
{ /* Fin des balises Facebook */ }
{ /* Balises Twitter */ }
<meta name="twitter:creator" content={name} />}
<meta name="twitter:card" content={type} />
<meta name="twitter:title" content={title} />
<meta name="twitter:description" content={description} />
{ /* Fin des balises Twitter */ }
</Helmet>
)
}
```

Comme indiqué ci-dessus, notre composant accepte quatre props : title, description, name et type. En utilisant ces quatre props, nous avons pu distribuer les valeurs sur neuf types différents de balises méta !

Voici un exemple de la façon dont nous pourrions implémenter ce composant dans notre composant de page **Landing** :

```javascript
import React from 'react';
import { SEO } from './SEO’;
export default function Landing() {
return (
<div>
<SEO
title=’Learning React Helmet!’
description=’Beginner friendly page for learning React Helmet.'
name=’Company name.’
type=’article’ />
<h1>Cool Landing Page!</h1>
</div>
)
}
```

Tout ce que nous avions à faire était de passer nos quatre props, et notre composant SEO personnalisé s'occupe de tout le gros du travail de création des multiples types de balises de métadonnées. Sympa.

Cet exemple est loin d'être une liste exhaustive de balises méta. Il ne faut pas beaucoup d'imagination pour visualiser à quel point ce composant serait utile si vous vouliez inclure toutes les balises méta pertinentes pour votre site.

## Conclusion

Dans cet article, nous avons vu pourquoi React Helmet est un ajout utile à votre application React. Vous avez appris non seulement la configuration et l'utilisation de base, mais aussi une implémentation plus avancée qui aide à abstraire une grande partie du travail répétitif impliqué dans les balises de métadonnées.

Nous espérons que vous vous sentez maintenant suffisamment en confiance pour améliorer votre [React SEO](https://www.ohmycrawl.com/react-seo/) et vos performances sur les réseaux sociaux en implémentant la bibliothèque React Helmet Async. Bonne chance et bon codage !

Pour plus d'informations sur la façon de configurer vos sites Web JavaScript pour le succès dans les moteurs de recherche, consultez [ohmycrawl.com](http://ohmycrawl.com/).