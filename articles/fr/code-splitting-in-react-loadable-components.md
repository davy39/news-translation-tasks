---
title: Division de code dans React – Les composants chargeables à la rescousse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-07T20:41:40.000Z'
originalURL: https://freecodecamp.org/news/code-splitting-in-react-loadable-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/david-lezcano-zwCE12DucBo-unsplash-4.jpg
tags:
- name: components
  slug: components
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Division de code dans React – Les composants chargeables à la rescousse
seo_desc: "By Lusan Das\nCode splitting is a way to split up your code from a large\
  \ file into smaller code bundles. These can then be requested on demand or in parallel.\
  \ \nNow, it isn't a new concept, but it can be tricky to understand.\nWhen you're\
  \ doing code spl..."
---

Par Lusan Das

La division de code est une méthode pour diviser votre code d'un gros fichier en petits bundles de code. Ceux-ci peuvent ensuite être demandés à la demande ou en parallèle. 

Ce n'est pas un nouveau concept, mais il peut être difficile à comprendre.

Lorsque vous faites de la division de code, il est important de garder les tailles des bundles HTML, CSS et JavaScript aussi petites que possible. Mais souvent, à mesure que les applications grandissent, des bundles plus gros sont inévitables. Et cela peut affecter négativement les [web vitals](https://web.dev/vitals/) de votre site web.

Alors dans cet article, nous verrons comment fonctionne la division de code et comment vous pouvez bien la faire.

## Division de code dans une base de code React

Voici quelques méthodes courantes pour faire de la division de code :

### Division de code en utilisant la syntaxe d'import dynamique de Webpack

Consultez l'exemple ci-dessous :

```import("module_name").then({ default } => // faire quelque chose)```

Cette syntaxe permettra au fichier Webpack qui doit être divisé et bundlé d'être généré en conséquence. Il existe également d'autres méthodes dans Webpack comme l'utilisation de **points d'entrée manuels** et **SplitChunksPlugin**. Vous pouvez trouver plus d'informations dans la [documentation](https://webpack.js.org/guides/code-splitting/).

### Division de code en utilisant React.Lazy et Suspense

Il s'agit d'une fonctionnalité fournie directement par React. Plongeons dans l'exemple ci-dessous issu de la documentation officielle :

```js
import React, { Suspense } from 'react';

const OtherComponent = React.lazy(() => import('./OtherComponent'));

function MyComponent() {
  return (
    <div>
      <Suspense fallback={<div>Chargement...</div>}>
        <OtherComponent />
      </Suspense>
    </div>
  );
}
```

Cela ressemble beaucoup à la syntaxe d'import dynamique de Webpack, où le composant Suspense peut être utilisé pour offrir un état de chargement jusqu'à ce que le composant soit chargé de manière paresseuse.

J'ai exploré cela dans un autre article où j'ai parlé de [L'avenir de React, se déroulant avec Suspense](https://blog.logrocket.com/the-future-of-react-unfolding-with-suspense/).

## Quand utiliser la division de code dans React

Le seul inconvénient de la division de code est que vous ne pouvez l'utiliser que pour le rendu côté client.

Les deux techniques ci-dessus ne fonctionneront pas lors du rendu côté serveur lorsqu'il s'agit de React 🤯. C'est la raison pour laquelle l'équipe React recommande d'utiliser des composants chargeables pour la division de code sur le serveur.

## Mais pourquoi utiliser des composants chargeables ?

Je vous entends et je vous comprends. Cela m'a également pris un certain temps pour le comprendre.

Plongeons dans un exemple.

Revenons à notre problème initial : nous aimerions faire de la division de code lors du rendu côté serveur (SSR). Le meilleur outil que nous avons dans notre arsenal jusqu'à présent est la syntaxe d'import dynamique de Webpack, dont nous avons brièvement parlé dans la section ci-dessus. 

Nous allons donc construire un composant appelé **AsyncComponent** dont la responsabilité est d'accepter des modules et d'utiliser des imports dynamiques. 

Il aura trois états :

* isLoading _// car l'import dynamique retourne une promesse_
* Component _// module réel dérivé de la division de code_
* Error _// pour le journal en cas d'échec de l'import_

### Comportement attendu

Notre AsyncComponent acceptera tout module d'import et le résoudra. En cas de succès, nous définirons l'état isLoading sur false et rendrons le composant résolu.

Parcourons rapidement le code ci-dessous tel que décrit ci-dessus :

```js
import React from 'react';


class AsyncComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoading: true,
            component: null,
            error: null
        }
    }

    componentWillMount() {
        const { importModule } = this.props;
        importModule()
            .then((module) => {
                const component = module.default;
                console.log(component)
                this.setState(({
                    component,
                    isLoading: false
                }))
            })
            .catch(err => {
                console.log(error)
                this.setState({
                    isLoading: false,
                    error
                })
            })
    }

    render() {
        const { isLoading, component, error } = this.state;

        if(isLoading) {
            return <div>Chargement</div>
        }
        if(error) {
            return <div>{error}</div>
        }
        return <div>{component}</div>
    }
}

const A = () => {
    return (
        <div>
            <AsyncComponent importModule={() => import('./F')} />
        </div>
    )
}

// Nous gardons une référence pour empêcher uglify de supprimer

export default A
```

### Comportement réel

Mais cela ne fonctionnera pas. Puisque nous essayons de le faire côté serveur, le cycle de vie de rendu de React n'attendra pas que l'import dynamique se résolve, ce qui est une promesse. Nous resterons donc bloqués sur l'écran de chargement, ce qui est évident d'après la capture d'écran ci-dessous de l'expérience que j'ai réalisée.

![Image](https://lh5.googleusercontent.com/dC4gCS9bG_07BiEbljwNtEWu_ODXXizy8geQ45XqmNJLEcl_KlliePS3niWZnrNSnpSR1qwFNNuw4h91iyN-_xRgTIZ8WWrDlTR5ruUm1pu2SuRl_v6xlbiuWb6zJepfoxYi_UnT)

C'est pourquoi la division de code dans React n'est pas simple lorsque nous essayons de le faire simplement avec nos outils disponibles.

## Entrée des composants chargeables dans React

Pour résoudre ce problème, nous avons [loadable components](https://loadable-components.com/docs/server-side-rendering/), une bibliothèque recommandée par la documentation officielle de React. 

Je ne vais pas entrer dans la partie configuration, car la documentation officielle contient suffisamment d'exemples et d'étapes qui couvrent ce que vous devez savoir. Regardons cela d'un point de vue code.

```js
import React from 'react';
import loadable from '@loadable/component';

const F = loadable(() => import('./F'))

const A = () => {
    return (
        <div>
            {/* <AsyncComponent importModule={() => import('./F')} /> */}
            <F />
        </div>
    )
}

// Nous gardons une référence pour empêcher uglify de supprimer

export default A
```

Dans notre exemple actuel, nous avons remplacé **AsyncComponent** par un **composant chargeable.**

**Violà – ça marche !** 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/viola.png)

C'est effectivement un problème complexe à résoudre, mais les composants chargeables le rendent facile. Et la documentation est tout aussi facile à suivre !

Le plugin babel loadable transpile la syntaxe loadable dans les composants et prépare la chaîne finale pour le HTML lors du rendu côté serveur et la syntaxe d'import dynamique lors du rendu côté client. 

Notez que les composants chargeables peuvent être utilisés pour la division de code à la fois côté client et serveur avec l'aide d'un drapeau SSR qui peut être activé/désactivé.

## Conclusion

J'ai écrit cet article pour parler de l'importance des composants chargeables et des problèmes qu'ils résolvent. Je voulais également expliquer pourquoi la division de code est compliquée lors du rendu côté serveur. J'espère vraiment que cela vous a aidé à comprendre le problème.

> _Mention spéciale à [Kashyap](https://twitter.com/kgrz) qui m'a aidé à comprendre le concept._

Suivez-moi sur [Twitter](https://twitter.com/daslusan) pour obtenir plus de mises à jour concernant les nouveaux articles et pour rester à jour dans le dernier développement frontend. De plus, partagez cet article sur Twitter pour aider les autres à le connaître. Partager, c'est prendre soin ^_^.

### Ressources

* [https://loadable-components.com/docs/server-side-rendering/](https://loadable-components.com/docs/server-side-rendering/)
* [https://webpack.js.org/guides/lazy-loading/](https://webpack.js.org/guides/lazy-loading/)
* [https://webpack.js.org/guides/code-splitting/](https://webpack.js.org/guides/code-splitting/)
* [https://reactjs.org/docs/code-splitting.html](https://reactjs.org/docs/code-splitting.html)

Voici quelques autres articles que j'ai écrits et que vous pourriez trouver intéressants :

1. [L'avenir de React, se déroulant avec Suspense](https://blog.logrocket.com/the-future-of-react-unfolding-with-suspense/)
2. [L'histoire de la demande deux fois – CORS](https://www.freecodecamp.org/news/the-story-of-requesting-twice-cors/)
3. [Comment utiliser Redux Persist lors de la migration de vos états](https://www.freecodecamp.org/news/how-to-use-redux-persist-when-migrating-your-states-a5dee16b5ead/)
4. [Redux Observable à la rescousse](https://codeburst.io/redux-observable-to-the-rescue-b27f07406cf2)
5. [Construction d'une application web pour l'avenir](https://codeburst.io/building-webapp-for-the-future-68d69054cbbd)