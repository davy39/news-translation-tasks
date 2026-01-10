---
title: Qu'est-ce que le théming de site web ? Comment utiliser les propriétés personnalisées
  CSS et Gatsby.js pour personnaliser votre site
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-07-01T18:19:21.000Z'
originalURL: https://freecodecamp.org/news/website-theming-with-css-custom-properties-and-gatsbyjs
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/theming-website-preview-1-1.jpg
tags:
- name: CSS
  slug: css
- name: css properties
  slug: css-properties
- name: Gatsby
  slug: gatsby
- name: themes
  slug: themes
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le théming de site web ? Comment utiliser les propriétés
  personnalisées CSS et Gatsby.js pour personnaliser votre site
seo_desc: 'In this article, I''m going to show you how to theme your website so users
  can customize certain elements to their tastes.

  We''ll talk about website themes, how theming works, and we''ll end with a demo
  so you can see it in action. Let''s dive in.

  Table ...'
---

Dans cet article, je vais vous montrer comment thématiser votre site web afin que les utilisateurs puissent personnaliser certains éléments selon leurs goûts.

Nous parlerons des thèmes de sites web, du fonctionnement du théming, et nous terminerons par une démonstration pour que vous puissiez voir cela en action. Plongeons-nous dans le sujet.

## Table des matières :

* [Qu'est-ce qu'un thème de site web ?](#heading-qu-est-ce-qu-un-theme)  
    Qu'est-ce que le théming ?
    
* [Pourquoi devriez-vous vous soucier du théming ?](#heading-pourquoi-devriez-vous-vous-soucier-du-theming)  
    « C'est leur écran, machine et logiciel »  
    Le théming améliore la lisibilité  
    Tous les cool cats l'utilisent - le théming dans la nature
    
* [Comment utiliser les propriétés de thème](#heading-comment-utiliser-les-proprietes-de-theme)  
    Qu'est-ce que les propriétés de thème ?  
    Qu'est-ce que les propriétés personnalisées CSS ?  
    Comment configurer les propriétés de thème dans Gatsby.js  
    Comment stocker les propriétés de thème  
    Comment transformer les propriétés de thème en propriétés personnalisées CSS
    
* [Comment utiliser le composant de commutateur de thème](#heading-comment-utiliser-le-composant-de-commutateur-de-theme)  
    Le balisage  
    Comment configurer l'état  
    Comment mettre à jour l'état  
    Comment persister l'état dans `LocalStorage`
    
* [Conclusion](#heading-conclusion)
    

## À qui s'adresse cet article ?

Cet article s'adresse aux développeurs qui ont déjà une connaissance de base de CSS, React et Gatsby et qui souhaitent apprendre à créer une application Gatsby ou React thématisable par l'utilisateur.

À la fin de cet article, vous devriez comprendre comment fonctionne le théming et comment l'implémenter sur vos sites Gatsby.

## Qu'est-ce qu'un thème ?

Pour comprendre ce qu'est le théming de site web, regardons d'abord ce qu'est un **thème de site web** et ce qui constitue un thème.

Un thème dans le contexte d'un site web est l'apparence générale, la sensation et le style de votre **site web**. Un thème peut inclure :

* les polices
    
* la taille de la police
    
* les schémas de couleurs
    
* les mises en page
    
* l'esthétique
    

Un thème contrôle la conception de votre site web. Il détermine à quoi ressemble votre site web en surface, et c'est la partie de votre site web qui a un impact direct sur vos utilisateurs.

Un thème est également un ensemble de styles portés par un site web.

## Qu'est-ce que le théming ?

Le théming est pour un site web ce que les vêtements sont pour nos corps. Imaginez porter les mêmes vêtements à une réunion, un mariage et une ferme - cela semble drôle, n'est-ce pas ? Bien sûr, vous ne feriez probablement pas cela si vous aviez le choix.

Pour chaque occasion, vous porteriez le type ou le style de vêtement approprié. C'est ce qu'est le théming de site web - il permet à nos utilisateurs de choisir l'apparence et la sensation de notre site web avec un ensemble de styles basés sur différentes occasions.

Le théming consiste simplement à donner aux utilisateurs la possibilité de faire des personnalisations sur nos sites web et applications. Vous pouvez également considérer le théming comme un ensemble de personnalisations que les utilisateurs peuvent apporter à nos sites web ou applications en fonction de leurs choix.

Le théming se produit lorsque l'utilisateur peut indiquer à votre site web ce qu'il préfère voir, par exemple :

* Cliquer sur un bouton pour changer l'arrière-plan d'un site web en rouge ou noir
    
* Augmenter ou diminuer la taille de la police d'un site web/application
    
* Cliquer sur un bouton pour supprimer le contenu non pertinent pour l'utilisateur.
    

Voici un conseil : laisser ou demander à vos utilisateurs de déterminer le thème de votre site web à partir de zéro est une mauvaise idée. Vous ou votre équipe devriez fournir aux utilisateurs un thème par défaut accessible et utilisable, car dans la plupart des cas, de nombreux utilisateurs ne personnaliseront jamais « leur vue » sur votre site web, peu importe la facilité.

## Pourquoi devriez-vous vous soucier du théming de site web ?

Outre le fait de montrer aux utilisateurs que vous vous souciez de leurs préférences personnelles, il existe d'autres raisons de laisser vos utilisateurs thématiser votre site web. Certaines d'entre elles incluent :

### « C'est leur écran, machine et logiciel »

C'est une citation de l'article de Jakob Nielsen de 2002 : [Let users control font size](https://www.nngroup.com/articles/let-users-control-font-size/).

Le fait que votre site web fonctionne sur l'écran, la machine et le logiciel de l'utilisateur (et probablement draine également leurs batteries) est une raison suffisante pour qu'ils puissent personnaliser leur expérience sur votre site.

### Le théming améliore la lisibilité du site web

En citant D. Bnonn de l'article : [16 Pixels Font Size: For Body Copy. Anything Less Is A Costly Mistake](https://www.smashingmagazine.com/2011/10/16-pixels-body-copy-anything-less-costly-mistake/)

> Fait : La plupart des utilisateurs web détestent la taille de police « normale ».

Avec ce fait à l'esprit, le théming peut aider les lecteurs en leur permettant de choisir la taille de police qui convient le mieux à leurs yeux.

Oh, et voici une autre citation du même article.

> Lectorat = Revenus.

### Tous les cool cats l'utilisent - le théming dans la nature

Beaucoup de développeurs ont utilisé l'idée du théming pour créer des versions en mode sombre de leurs sites web. D'autres ont poussé cette idée plus loin pour permettre aux utilisateurs de changer la taille de la police, les couleurs et l'arrière-plan en fonction de leurs préférences individuelles.

Voici un exemple de ce type de personnalisation dans l'application web Twitter :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/twitter.com_home.png align="left")

*Interface utilisateur de personnalisation de thème Twitter*

Toujours pas motivé ? Si vous avez encore besoin de plus de preuves que le théming est une bonne idée, [voici une liste complète de sites web, applications et logiciels](https://darkmodelist.com/) qui utilisent le théming pour fournir des modes sombre et clair à leurs utilisateurs.

## Comment utiliser les propriétés de thème

Maintenant que vous savez ce qu'est le théming et que vous avez vu des sites qui utilisent cette idée de théming dans leurs sites web et applications, apprenons ce que sont les propriétés de thème.

### Qu'est-ce que les propriétés de thème ?

Les propriétés de thème sont un ensemble de propriétés personnalisées CSS qui constituent un thème. Rappelez-vous qu'« un thème est un ensemble de styles portés par un site web » - donc les propriétés de thème sont toutes les propriétés qui constituent les styles qu'un site porte. Par exemple :

```css
[data-theme="default"] {
  --font-size: 20px;
  --background: red;
}
```

Dans l'exemple ci-dessus, `[data-theme="default"]` est notre thème, tandis que toutes les propriétés personnalisées CSS à l'intérieur sont les propriétés de thème. Vous comprenez l'idée, n'est-ce pas ?

Voici un conseil : vos propriétés de thème n'ont pas à être uniquement des propriétés personnalisées CSS. Elles peuvent également être n'importe quelle propriété CSS valide que vous souhaitez appliquer à un thème spécifique.

Avant de continuer, comprenons d'abord ce que sont les propriétés personnalisées CSS.

### Qu'est-ce que les propriétés personnalisées CSS (également connues sous le nom de variables CSS) ?

Les propriétés personnalisées CSS sont des entités qui contiennent des valeurs que vous pouvez réutiliser dans l'ensemble d'un site ou d'un document.

Pour les besoins de ce tutoriel, nous n'allons pas couvrir en profondeur les propriétés personnalisées CSS. Vous pouvez [en lire plus sur les propriétés personnalisées ici](https://www.freecodecamp.org/news/css-customs-properties-cheatsheet-c86778541f7d/).

Il existe également de nombreux excellents tutoriels qui couvrent les propriétés personnalisées CSS et comment les utiliser pour le théming, donc nous laisserons la théorie à ces autres articles.

Pour un guide stratégique sur la façon d'utiliser les propriétés personnalisées CSS pour le théming, consultez cet article génial : [A Strategy Guide To CSS Custom Properties](https://www.smashingmagazine.com/2018/05/css-custom-properties-strategy-guide/).

Bien que nous ne couvions pas en profondeur les propriétés personnalisées CSS, je veux souligner quelques raisons pour lesquelles les propriétés personnalisées CSS sont idéales pour le théming de site web :

* Elles sont réutilisables - vous pouvez les utiliser dans l'ensemble de votre CSS
    
* Elles réduisent la complexité de notre code, puisque vous n'avez plus besoin de créer différentes feuilles de style pour obtenir un site web thématisable
    
* Elles sont disponibles à l'exécution, ce qui signifie que vous pouvez mettre à jour leur valeur dans le navigateur, via JavaScript, avec des résultats immédiats.
    

## Comment configurer les propriétés de thème dans Gatsby.js

Bien sûr, vous pouvez coder en dur les propriétés de thème directement dans votre fichier CSS comme n'importe quelle autre propriété CSS. Mais devoir faire défiler quelques lignes de votre code CSS chaque fois que vous voulez apporter quelques modifications à vos thèmes semble fastidieux, n'est-ce pas ?

[Max Böck](https://mxb.dev/about/) dans son article ["Color Theme Switcher"](https://mxb.dev/blog/color-theme-switcher/) conseille de définir nos thèmes dans un emplacement central.

Avoir un emplacement central (fichier) où vous pouvez facilement accéder et gérer vos thèmes semble être une idée intéressante. Et c'est le genre de chose pour lequel Gatsby a été conçu.

En citant la documentation de Gatsby :

> "Une fonctionnalité principale de Gatsby.js est sa capacité à charger des données de n'importe où."

Cela signifie que vous pouvez sourcer des données à partir d'un fichier JSON qui sera disponible au moment de la construction. Lorsque vous importez ces données, vous pouvez ensuite itérer sur elles avec la méthode `Array.map` et les rendre dans un composant React.

### Comment stocker les propriétés de thème

Dans votre dossier de projet Gatsby, créez un répertoire appelé content s'il n'existe pas déjà. Ensuite, ajoutez un nouveau fichier appelé `themes.json` avec le contenu suivant :

```json
[
  {
    "id": "default",
    "colors": {
      "primary-color": "#0250bb",
      "text": "#20123a",
      "text-alt": "#42425a",
      "border": "#ededf0",
      "background": "#ffffff",
      "background-alt": "#f9f9fa",
      "color-scheme": "light"
    }
  },
  {
    "id": "dark",
    "colors": {
      "primary-color": "#7f5af0",
      "text": "#fffffe",
      "text-alt": "#94a1b2",
      "border": "#010101",
      "background": "#16161a",
      "background-alt": "#242629",
      "color-scheme": "dark"
    }
  },
  {
    "id": "warm",
    "colors": {
      "primary-color": "#ff8e3c",
      "text": "#0d0d0d",
      "text-alt": "#2a2a2a",
      "background": "#eff0f3",
      "background-alt": "#fff",
      "border": "rgba(0,0,0,.1)",
      "color-scheme": "light"
    }
  },
// Ajoutez d'autres thèmes ici
]
```

Chaque thème obtient un `id`, un ensemble de propriétés de thème et une propriété CSS `color-scheme`.

Voici un conseil - nous utilisons la propriété CSS `color-scheme` pour indiquer quel schéma de couleurs (clair/sombre) notre page web doit être rendue. Pour une meilleure compréhension de `color-scheme`, veuillez vous référer à ce [guide de schéma de couleurs](https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme).

### Comment transformer les propriétés de thème en propriétés personnalisées CSS

Actuellement, les thèmes de couleurs stockés dans nos fichiers `content/themes.json` sont simplement des **données**. Ils doivent être transformés en propriétés personnalisées CSS avant de pouvoir faire quoi que ce soit de significatif.

> **Données** est une collection de faits, tels que des nombres, des **mots**, des mesures, des observations ou simplement des descriptions de choses.

Nous allons avoir besoin que nos propriétés personnalisées CSS soient générées dynamiquement et ajoutées en tant que `<style>` en ligne dans le `<head>` de toutes les pages de notre site.

Vous devez installer deux plugins importants pour ce tutoriel : react-helmet, un gestionnaire de tête de document pour React, et gatsby-plugin-react-helmet pour permettre le rendu côté serveur des données ajoutées avec React Helmet.

Installez ces plugins avec cette commande :

```plaintext
npm installl gatsby-plugin-react-helmet react-helmet
```

Pour utiliser ces plugins, vous devez les ajouter au tableau des plugins dans votre fichier gatsby-config.js situé à la racine du répertoire du projet :

```plaintext
plugins: [gatsby-plugin-react-helmet]
```

Puisque vous allez utiliser React helmet sur toutes vos pages, il est logique de l'utiliser dans votre fichier `Layout.js`. Dans votre fichier `layout.js`, ajoutez le code suivant :

```js
import React from "react"
import { Helmet } from "react-helmet"
import themes from "../../content/themes.json"
// autres imports

export default function Layout({ children }) {
  function colors(theme) {
    return `
          --primary-color: ${theme.colors["primary-color"]};
          --text: ${theme.colors["text"]};
          --text-alt: ${theme.colors["text-alt"]};
          --background: ${theme.colors["background"]};
          --background-alt: ${theme.colors["background-alt"]};
          --border: ${theme.colors["border"]};
          --shadow: ${theme.colors["shadow"]};
          color-scheme: ${theme.colors["color-scheme"]};
    `
  }
  
  return (
    <>
      <Helmet>
        // autres balises méta head

        <style type="text/css">{`
    ${themes
      .map(theme => {
        if (theme.id === "default") {
          return `
          :root {
            ${colors(theme)}
          }
        `
        } else if (theme.id === "dark") {
          return `
          @media (prefers-color-scheme: dark) {
            ${colors(theme)}
          }
        `
        }
      })
      .join("")}
    ${themes
      .map(theme => {
        return `
        [data-theme="${theme.id}"] {
          ${colors(theme)}
        }
      `
      })
      .join("")}
  `}
        </style>
      </Helmet>
      <Header />
      <main id="main">{children}</main>
      <Footer />
    </>
  )
}
```

Décomposons cela un peu.

Tout d'abord, les thèmes et react-helmet sont importés depuis `content/themes.json` et React respectivement :

```js
import React from "react"
import { Helmet } from "react-helmet"
import themes from "../../content/themes.json"
// autres imports

export default function Layout({ children }) {
  return (
    
  )
}
```

Il crée une fonction qui transformera nos thèmes en propriétés personnalisées CSS :

```js
function colors(theme) {
    return `
          --primary-color: ${theme.colors["primary-color"]};
          --text: ${theme.colors["text"]};
          --text-alt: ${theme.colors["text-alt"]};
          --background: ${theme.colors["background"]};
          --background-alt: ${theme.colors["background-alt"]};
          --border: ${theme.colors["border"]};
          --shadow: ${theme.colors["shadow"]};
          color-scheme: ${theme.colors["color-scheme"]};
    `
  }
```

À l'intérieur de notre `<Helmet>`, nous ajoutons une balise `<style>` à la tête de notre document.

Voici un conseil - si vous devez ajouter un style à la tête du document, vous devez rendre le style sous forme de chaîne à l'intérieur d'accolades.

Dans la première méthode `Array.map`, nous vérifions s'il existe un thème avec un `id` égal à `default`. Si c'est le cas, nous le définissons comme notre schéma de couleurs par défaut dans le `:root{}`. Nous vérifions également s'il existe un thème avec un `id` égal à `dark`. Si c'est le cas, nous l'utilisons lorsque le `prefers-color-scheme` de l'utilisateur est sombre :

```js
${themes
      .map(theme => {
        if (theme.id === "default") {
          return `
          :root {
            ${colors(theme)}
          }
        `
        } else if (theme.id === "dark") {
          return `
          @media (prefers-color-scheme: dark) {
            ${colors(theme)}
          }
        `
        }
      })
      .join("")}
```

Dans la dernière méthode `Array.map`, nous itérons sur nos thèmes et chaque thème obtient un sélecteur d'attribut `[data-theme=""]` :

```js
 ${themes
      .map(theme => {
        return `
        [data-theme="${theme.id}"] {
          ${colors(theme)}
        }
      `
      })
      .join("")}
```

Maintenant, si vous inspectez la tête de votre site, vous devriez voir toutes les propriétés de thème dans votre fichier `content/themes.json` bien générées en tant que propriétés personnalisées CSS. En fait, si vous ajoutez l'attribut `data-theme="nom de votre thème"` à votre balise `html` via les outils de développement, votre thème devrait fonctionner parfaitement bien.

## Comment utiliser le composant de commutateur de thème

Eh bien, nous ne pouvons pas avoir des utilisateurs modifiant manuellement notre site via les outils de développement chaque fois qu'ils veulent utiliser un thème différent sur notre site. Donc, tout ce qui reste dans ce tutoriel est de créer une interface utilisateur pour que les utilisateurs puissent facilement **thématiser** notre site web.

### Le balisage

Créez un nouveau fichier appelé `themes.js` dans votre répertoire de composants et ajoutez le code suivant :

```js
import React from "react"
import themes from "../../content/theme.json"

const Theme = () => {

  return (
    <div className="theme">
      <div className="theme-close text-right">
        <button>x</button>
      </div>
      <div className="theme-wrapper__inner">
        <div className="theme-header text-center">
          <strong className="theme-title">Sélectionner le thème</strong>
          <p>
            Veuillez noter que les modifications apportées ici affecteront les autres pages du
            site entier.
          </p>
        </div>
        <div className="theme-content">
          <ul className="schemes">
            {theme.map(data => {
              return (
                <li className="scheme">
                  <button
                    className="scheme-btn js-scheme-btn"
                    aria-label={`${data.id}`}
                    name="scheme"
                    value={`${data.id}`}
                    style={{ backgroundColor: `${data.colors["background"]}` }}
                  ></button>
                </li>
              )
            })}
          </ul>
        </div>
        <div className="theme-content">
          <div className="theme-range">
            <label htmlFor="font" title={state.font}>
              <span className="text-xsmall">Aa</span>
              <input
                type="range"
                name="font"
                min="10"
                max="20"
                step="2"
                className="theme-range__slider"
              />
              <span className="text-large">Aa</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  )
}
export default Theme
```

Décomposons un peu ce code pour savoir ce qui se passe.

Tout d'abord, nous importons nos thèmes depuis content/themes.js et itérons dessus avec une méthode `Array.map`. Pour chaque thème, j'ai créé un bouton avec une couleur d'arrière-plan égale à sa `background-color` avec une valeur égale à son `id`.

```html
<ul className="schemes">
            {theme.map(data => {
              return (
                <li className="scheme">
                  <button
                    className="scheme-btn js-scheme-btn"
                    aria-label={`${data.id}`}
                    name="scheme"
                    value={`${data.id}`}
                    style={{ backgroundColor: `${data.colors["background"]}` }}
                  ></button>
                </li>
              )
            })}
</ul>
```

Pour changer la taille de la police de notre texte, j'ai également ajouté un champ `input` de type `range` avec une valeur `min` de `10px` et une valeur `max` de `20px`.

```html
<input
  type="range"
  name="font"
  min="10"
  max="20"
  step="2"
  className="theme-range__slider"
  />
```

Avec un peu de CSS ajouté (que nous ne couvrirons pas dans ce tutoriel), nous avons maintenant une interface utilisateur qui ressemble à celle ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/localhost_8000_--13-.png align="left")

*Interface utilisateur de personnalisation de thème iamspruce.dev*

### Comment configurer l'état

Nous allons commencer par importer le hook `useState()` de React :

```js
import React, { useState} from "react"

const Theme = () => {
  
  return (
  )
}
```

Nous utilisons l'initialisation paresseuse de React, qui nous permet de passer une fonction à `useState()` que nous utiliserons lors du rendu initial.

En citant la documentation de React :

> "Si l'état initial est le résultat d'un calcul coûteux, vous pouvez fournir une fonction à la place, qui ne sera exécutée que lors du rendu initial."

```js
import React, { useState} from "react"
import themes from "../../content/theme.json"

const Theme = () => {
 const [state, setState] = useState(() => {
     const localVal =
       typeof window !== "undefined" && window.localStorage.getItem("theme")
     let obj = {
       font: 15,
       scheme: "default",
     }
     return localVal !== null ? JSON.parse(localVal) : obj
   })
  return (
  
  )
}

export default Theme
```

Dans notre cas, nous l'utilisons pour vérifier la valeur dans `localStorage()`. Si la valeur existe, nous l'utiliserons comme notre valeur initiale. Sinon, nous utiliserons l'`obj` par défaut.

Nous vérifions si l'objet window existe `(typeof window !== "undefined")` car au moment de la construction, l'objet window n'existe pas. Si vous exécutez `gatsby build` sans vérifier si l'objet window existe ou non, vous obtiendrez une erreur qui ressemble à ceci :

`WebpackError: ReferenceError: localStorage is not defined`

### Comment mettre à jour l'état

L'étape suivante consiste à avoir un écouteur d'événements `onClick` et `onChange` pour mettre à jour notre état. Pour cela, nous allons créer une fonction :

```js
import React, { useState} from "react"
import themes from "../../content/theme.json"

const Theme = () => {
 const [state, setState] = useState(() => {
     const localVal =
       typeof window !== "undefined" && window.localStorage.getItem("theme")
     let obj = {
       font: 15,
       scheme: "default",
     }
     return localVal !== null ? JSON.parse(localVal) : obj
   })
// la fonction de mise à jour
  const update = e => {
    const { name, value } = e.target
    setState(prevState => ({
      ...prevState,
      [name]: value,
    }))
  }

  return (
  
  )
}
```

Nous avons passé un objet comme valeur initiale pour notre `useState` car nous pouvons mettre à jour plusieurs états avec un seul hook `useState`. Nous devons maintenant définir la fonction de mise à jour sur notre interface utilisateur :

```js
...
{theme.map(data => {
  return (
    <li className="scheme">
       <button
       onClick={update} // définir la fonction de mise à jour sur un événement Onclick 
       className="scheme-btn js-scheme-btn"
       aria-label={`${data.id}`}
       name="scheme"
       value={`${data.id}`}
       style={{ backgroundColor: `${data.colors["background"]}` }}
       ></button>
    </li>
   )
})}

<input
  type="range"
  name="font"
  min="10"
  max="20"
  step="2"
  className="theme-range__slider"
  onChange={update} // définir la fonction de mise à jour sur un événement Onchange
  value={state.font}
/>
```

### Comment persister nos changements dans LocalStorage

L'étape finale consiste à s'assurer que nous mettons à jour `localStorage` et notre site web avec les valeurs actuelles de notre état chaque fois que la valeur de l'état change. Pour cela, nous utiliserons le hook `useEffect`, qui nous permet **d'exécuter du code après que React a mis à jour le DOM.**

```js
import React, { useState} from "react"
import themes from "../../content/theme.json"

const Theme = () => {
 const [state, setState] = useState(() => {
     const localVal =
       typeof window !== "undefined" && window.localStorage.getItem("theme")
     let obj = {
       font: 15,
       scheme: "default",
     }
     return localVal !== null ? JSON.parse(localVal) : obj
   })

  const update = e => {
    const { name, value } = e.target
    setState(prevState => ({
      ...prevState,
      [name]: value,
    }))
  }

// persistance de l'état dans localStorage
  useEffect(() => {
    window.localStorage.setItem("theme", JSON.stringify(state))
    let root = document.documentElement
    root.setAttribute("data-theme", state.scheme)
    root.style.setProperty("--font-size", `${state.font}px`)
  }, [state])

  return (
  
  )
}
```

Félicitations ! Si vous êtes arrivé jusqu'ici, vous avez maintenant un site web entièrement thématisable par l'utilisateur. La conception globale de notre **interface utilisateur de commutateur de thème** ressemble maintenant à ceci :

%[https://youtu.be/cMboQU-qwyE] 

Pour un aperçu en direct du site, visitez [https://www.iamspruce.dev/](https://www.iamspruce.dev/).

## Conclusion

Il n'y a vraiment aucune limite à ce que vous pouvez faire avec le **théming**. Bien que ce tutoriel utilise Gatsby.js, vous pouvez facilement appliquer ces concepts à d'autres générateurs de sites statiques basés sur React.

Si vous avez trouvé ce tutoriel utile, suivez-moi sur Twitter [@sprucekhalifa](https://twitter.com/sprucekhalifa).

Bon codage !