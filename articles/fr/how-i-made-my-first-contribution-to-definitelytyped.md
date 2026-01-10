---
title: Comment j'ai fait ma première contribution à DefinitelyTyped, un dépôt TypeScript
  open source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T17:37:07.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-my-first-contribution-to-definitelytyped
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/definitelytyped.png
tags:
- name: open source
  slug: open-source
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Comment j'ai fait ma première contribution à DefinitelyTyped, un dépôt
  TypeScript open source
seo_desc: "By Iva Kop\nTypeScript is awesome. It instantly makes our code safer, easier\
  \ to debug, and better documented. \nFor some time now, I have been using TypeScript\
  \ exclusively in all my projects. And here is the thing – I had never come across\
  \ a package th..."
---

Par Iva Kop

TypeScript est génial. Il rend notre code instantanément plus sûr, plus facile à déboguer et mieux documenté. 

Depuis un certain temps, j'utilise TypeScript exclusivement dans tous mes projets. Et voici la chose – je n'avais jamais rencontré de package auquel il manquait des définitions de types. Jusqu'à maintenant...

J'admets avoir été un peu gâtée à cet égard. Mais j'ai été surprise de découvrir qu'un petit mais utile plugin [Gatsby](https://www.gatsbyjs.com/) que nous utilisions – [gatsby-plugin-breakpoints](https://www.gatsbyjs.com/plugins/gatsby-plugin-breakpoints/) – n'avait pas encore de définitions de types. Cela m'a fait réfléchir.

# Comment j'ai résolu le problème

Ma première réaction a été de supprimer complètement le plugin du projet. Il fournissait une fonctionnalité simple que je pouvais facilement reproduire moi-même. Et en règle générale, moins nous avons de dépendances externes, mieux c'est, n'est-ce pas ?

Mais le plugin était déjà utilisé de manière assez extensive dans le projet. Donc, si je voulais éviter de refactoriser, je devais reproduire exactement son API. Cela signifierait que je devrais réécrire le code déjà existant (et fonctionnel) juste pour le plaisir de supprimer une dépendance. Cela ne semblait pas être une bonne approche.

Au lieu de cela, j'ai décidé d'ajouter simplement les types nécessaires à mon projet. Cela a été assez simple. Avant que je ne m'en rende compte, tout était fait et prêt à partir.

Mais ensuite, j'ai réalisé quelque chose. C'était la première fois que je devais faire cela pour l'une des dizaines de bibliothèques et de plugins que j'utilise quotidiennement dans mes projets React. Cela présentait une opportunité unique pour moi de sauter dans le bain et de faire une petite contribution à la communauté qui m'avait tant gâtée en premier lieu.

Alors je l'ai fait. 

# Comment contribuer à DefinitelyTyped

[DefinitelyTyped](https://definitelytyped.org/) est un dépôt open-source dirigé par la communauté pour les définitions de types TypeScript. C'est l'endroit idéal pour le type de contribution que je cherchais à faire. 

Bien que ce que je décris ci-dessous soit un peu centré sur React, j'espère qu'il peut encore servir de guide plus général. 

## Configuration pour contribuer

Commencer est simple. La première étape consiste à fork le dépôt [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) et à générer l'échafaudage en utilisant ce qui suit :

```
npx dts-gen --dt --name gatsby-plugin-breakpoints --template module

```

Cela créera un dossier dans le projet DefinitelyTyped avec 4 fichiers :

```
gatsby-plugin-breakpoints-test.ts
index.d.ts
tsconfig.json
tslint.json
```

Toutes nos définitions de types vivront dans `index.d.ts` et le fichier `gatsby-plugin-breakpoints-test.ts` nous aidera à nous assurer que tout fonctionne comme prévu.

Avant de commencer, puisque nous travaillons avec React, un petit ajustement est nécessaire dans le fichier `tsconfig.json`. Nous devons ajouter `"jsx": "react"` aux options du compilateur et changer le nom du fichier de test en `gatsby-plugin-breakpoints-tests.tsx`. N'oublions pas non plus de renommer le fichier de tests réel.

Le fichier `tsconfig.json` final devrait ressembler à ceci :

```
{
    "compilerOptions": {
        "module": "commonjs",
        "lib": [
            "es6",
            "DOM"
        ],
        "noImplicitAny": true,
        "noImplicitThis": true,
        "strictFunctionTypes": true,
        "strictNullChecks": true,
        "baseUrl": "../",
        "typeRoots": [
            "../"
        ],
        "types": [],
        "noEmit": true,
        "forceConsistentCasingInFileNames": true,
        "jsx": "react",
        "esModuleInterop": true
    },
    "files": [
        "index.d.ts",
        "gatsby-plugin-breakpoints-tests.tsx"
    ]
}

```

Jusqu'à présent, tout va bien !

## Comment créer les types et les tester

En regardant la documentation et le code source de `gatsby-plugin-breakpoints`, nous pouvons identifier les types que nous devons créer. Faisons une liste rapide :

* Configuration du plugin
* Hook React useBreakpoint
* HOC (higher order component) React withBreakpoints
* BreakpointProvider
* BreakpointContext

### Configuration du plugin

Commençons par la configuration.

```
// index.d.ts

// Définitions de types pour gatsby-plugin-breakpoints 1.3
// Projet : https://github.com/JimmyBeldone/gatsby-plugin-breakpoints
// Définitions par : Iva Kop <https://github.com/IvaKop>
// Définitions : https://github.com/DefinitelyTyped/DefinitelyTyped

/**
 * @see https://www.gatsbyjs.com/plugins/gatsby-plugin-breakpoints/
 */


export type QueriesObject = Record<string, string>;

export interface BreakpointOptions {
    queries?: QueriesObject;
}

export interface BreakpointConfig {
    resolve: 'gatsby-plugin-breakpoints';
    options?: BreakpointOptions;
}
```

Super ! Maintenant, allons dans le fichier de test et assurons-nous que nous avons tout fait correctement :

```
// gatsby-plugin-breakpoints-tests.tsx

import React from 'react';
import {
    BreakpointConfig,
} from 'gatsby-plugin-breakpoints';

const defaultQueries = {
    xs: '(max-width: 320px)',
    sm: '(max-width: 720px)',
    md: '(max-width: 1024px)',
    l: '(max-width: 1536px)',
};

const plugins: BreakpointConfig = {
    resolve: `gatsby-plugin-breakpoints`,
    options: {
        queries: defaultQueries,
    },
};

```

### useBreakpoints

Ensuite, typons le hook useBreakpoints.

```
// index.d.ts
// ...

export type BreakpointsObject = Record<string, boolean>;

export function useBreakpoint(): BreakpointsObject;
```

Et testons-le.

```
// gatsby-plugin-breakpoints-tests.tsx

import React from 'react';
import {
    // ...
    useBreakpoint
} from 'gatsby-plugin-breakpoints';

function HookComponent() {
    const breakpoints = useBreakpoint();
    return <div>{breakpoints.xs ? <div /> : null}</div>;
}



```

### withBreakpoints

Le plugin fournit également un HOC (higher order component) que nous pouvons utiliser. Typons-le :

```
// index.d.ts
// ...

export interface BreakpointProps {
    breakpoints: BreakpointsObject;
}

export function withBreakpoints<P extends BreakpointProps>(Component: React.ComponentType<P>): React.ComponentType<P>;

```

... et testons-le :

```
// gatsby-plugin-breakpoints-tests.tsx

import React from 'react';
import {
    // ...
    withBreakpoints,
    BreakpointProps,
} from 'gatsby-plugin-breakpoints';

const EnhancedFunctionalComponent = withBreakpoints(function Component({ breakpoints }) {
    return breakpoints.xs ? <div /> : <div>Content hidden only on mobile</div>;
});

class Component extends React.Component<BreakpointProps> {
    render() {
        const { breakpoints } = this.props;
        return breakpoints.xs ? <div /> : <div>Content hidden only on mobile</div>;
    }
}

const EnhancedClassComponent = withBreakpoints(Component);

```

### BreakpointContext et BreakpointProvider

Enfin, il reste deux choses à prendre en charge : `BreakpointContext` et `BreakpointProvider` :

```
// index.d.ts
// ...

export type QueriesObject = Record<string, string>;

export const BreakpointContext: React.Context<QueriesObject>;

export const BreakpointProvider: React.Provider<QueriesObject>;
```

Derniers tests :

```
// gatsby-plugin-breakpoints-tests.tsx

import React from 'react';
import {
    // ...
    BreakpointProvider,
    BreakpointContext,
} from 'gatsby-plugin-breakpoints';

// BreakpointContext
function useContext() {
    const context = React.useContext(BreakpointContext);
    return context;
}

// BreakpointProvider
const ProviderComponent: React.FC = ({ children }) => {
    return <BreakpointProvider value={defaultQueries}>{children}</BreakpointProvider>;
};

```

## Étapes finales

La partie difficile est maintenant terminée. Il ne reste plus qu'à exécuter les scripts de lint et de test de DefinitelyTyped avant de créer une pull request.

```
npm run lint gatsby-plugin-breakpoints
```

Tout semble bon !

```
npm run test gatsby-plugin-breakpoints
```

Oh, non ! Il semble y avoir une erreur :

```
Cannot find module 'csstype' or its corresponding type declarations.
```

Heureusement, nous ne sommes pas les premiers à rencontrer ce problème. Il y a déjà un [problème ouvert](https://github.com/DefinitelyTyped/DefinitelyTyped/issues/24788) dans le dépôt DefinitelyTyped et la solution semble assez simple – nous devons installer les modules node dans `types/react`. Allons-y !

```
cd types/react && npm install && cd ../../ && npm run test gatsby-plugin-breakpoints
```

Ouf, ça a marché ! 

À ce stade, nous sommes prêts à ouvrir une PR, à nous assurer que toutes les vérifications CI passent et à attendre l'approbation. D'après mon expérience limitée, le processus semble être assez rapide. Cette PR particulière a été approuvée, fusionnée et publiée en un peu plus d'une journée.

Voici le [lien](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/50868) si vous voulez le consulter.

# Conclusion

Ce que j'ai décrit ici est une petite contribution. Et elle peut probablement être améliorée (comme c'est le cas pour tout le code que nous écrivons). Mais les petites contributions s'accumulent lorsqu'elles sont partagées avec la communauté.

Le fait que j'ai utilisé TypeScript exclusivement pendant plus d'un an et que c'est la première fois que je rencontre un projet que je peux typer moi-même est un témoignage de l'excellence de l'open source. Je suis heureuse d'avoir rendu les choses juste un peu plus faciles pour la prochaine personne qui utilisera TypeScript dans son projet.

Alors, la prochaine fois que vous trouvez un projet qui cherche encore ses types (ou autre chose), n'hésitez pas à contribuer, si vous le pouvez. Cela fait toute la différence !

*Si vous avez trouvé cela utile, [connectons-nous](https://twitter.com/iva_kop). Pour plus d'articles approfondis sur React, consultez [mon blog](https://blog.whereisthemouse.com/).*