---
title: Comment créer un composant Table des matières pour votre blog
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-03T14:54:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-table-of-contents-component
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/toc.jpg
tags:
- name: blog
  slug: blog
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer un composant Table des matières pour votre blog
seo_desc: 'By Caleb Olojo

  When you visit documentation sites, you''ll notice that many of them have a common
  component: the <TableOfContent /> component.

  The idea behind it is to give the reader a "heads-up" about the information they''re
  trying to consume.

  This ...'
---

Par Caleb Olojo

Lorsque vous visitez des sites de documentation, vous remarquerez que beaucoup d'entre eux ont un composant commun : le composant `<TableDesMatieres />`.

L'idée derrière celui-ci est de donner au lecteur un "aperçu" des informations qu'il essaie de consulter.

Cette fonctionnalité permet au lecteur d'aller directement à la section qui contient une solution à tout bug ou problème auquel il est confronté, sans avoir à lire l'article entier. Cela contribue à une bonne expérience utilisateur car vous finissez par épargner à votre audience le tracas de faire défiler et rechercher davantage.

J'ai un blog personnel [blog](https://meje.dev/blog) auquel je consacre beaucoup de mon temps. Et pendant longtemps, j'ai pensé à ajouter cette fonctionnalité. Cela aidera toute personne visitant mon site à profiter de son temps et à trouver ce dont elle a besoin.

Cet article est un résumé de mon processus, afin que vous n'ayez pas à traverser les problèmes que j'ai rencontrés. Si vous essayez d'ajouter une fonctionnalité de Table des matières à votre blog, vous pouvez le faire avec moi.

J'ai partagé une vidéo de ce à quoi ressemblait le composant après l'avoir terminé. Vous pouvez y jeter un coup d'œil [ici](https://twitter.com/calebolojo/status/1629113931066142720).

## **Comment obtenir le texte des titres à partir du frontmatter**

Pour créer une fonctionnalité de table des matières, je savais ce que je devais faire. Puisque les articles de mon blog sont écrits en markdown, j'utilise simplement un sur-ensemble de markdown – MDX – qui me permet d'utiliser des composants React dans des fichiers markdown.

La première chose sur ma liste était de trouver un moyen de rendre le texte des titres dans un composant. Ainsi, lorsque les gens cliquaient sur les titres, le navigateur faisait défiler jusqu'à ce point dans l'article.

Avec HTML, vous pouvez y parvenir en utilisant la balise d'ancrage et en passant la valeur à un attribut `href`.

Pour avoir un texte lié pointant vers une section, la manière idéale de faire cela ressemblerait à ce qui est dans l'extrait ci-dessous :

```html
<a href="#section-un">Aller à la section un</a>
<a href="#section-deux">Aller à la section deux</a>
<a href="#section-trois">Aller à la section trois</a>

<section id="section-un">un certain contenu</section>
<section id="section-deux">encore un contenu qui semble bizarre</section>
<section id="section-trois">un certain contenu, encore</section>

```

Dans l'extrait ci-dessus, les balises d'ancrage sont liées aux sections en fonction de leur attribut `id` dans le DOM. Lorsque vous cliquez sur un texte, il vous emmène à la section respective.

Avec ce modèle mental, j'ai pensé à remplir le frontmatter de chaque article avec les titres de tous les articles que j'ai écrits. Je savais que cela allait être stressant, mais je l'ai fait quand même.

Pour contexte, voici à quoi ressemble un frontmatter dans un fichier markdown. Le frontmatter contient les métadonnées de tous les articles de mon blog. Des détails comme le titre, la date de publication, les tags ou la catégorie dans laquelle l'article se classe, la description, une URL canonique, et toute autre chose que vous pourriez vouloir ajouter pour améliorer le SEO de votre article.

Ce modèle est courant lorsque vous construisez des blogs avec Next.js et MDX (markdown en général). Il a aussi une syntaxe de type YAML.

```bash
---
id: 20
title: Construction d'un composant Table des matières
publishedAt: '2023-02-28'
excerpt: description de l'article
tags:
  - ux
  - nextjs
headings:
  - heading-un
  - heading-deux
  - heading-trois
cover_image: /img/covers/toc.jpg
---

```

L'extrait ci-dessus montre à quoi ressemble le frontmatter de cet article, mais avec l'entrée `headings`. Je vais utiliser cela pour expliquer mon approche initiale. Si je continue et parcours le frontmatter, je pourrai récupérer le contenu du tableau des titres.

C'est génial car je pourrai utiliser les éléments du tableau `headings` dans le composant TableDesMatieres. Cela semblait irréel, et j'étais ravi pendant une minute. Le composant ressemblait à ceci :

```jsx
import React from 'react'
import { HeadingContainer } from './style/toc.styled'

export default function TableDesMatieres({ headings }) {
  return (
    <HeadingContainer>
      <p>Dans cet article</p>
      <ul>
        {headings.map((item, index) => (
          <li key={index}>
            <a href={`#${item}`}>{item}</a>
          </li>
        ))}
      </ul>
    </HeadingContainer>
  )
}

```

Le composant ci-dessus reçoit une seule propriété `headings`, qui à son tour reçoit une valeur du frontmatter via la méthode `getStaticProps()` de Next.js.

```jsx
export default function Blog({
  post: {
    frontmatter: { title, headings },
  },
}) {
  return (
    <>
      <Head>
        <title>{title}</title>
      </Head>
      <TableDesMatieres headings={headings} />
    </>
  )
}

// déstructuration des params pour obtenir les slugs uniques
export async function getStaticProps({ params }) {
  const { slug } = params
  const { frontmatter } = await getArticleFromSlug(slug)

  return {
    props: {
      post: {
        frontmatter,
      },
    },
  }
}

```

Si tout ce qui est dans les extraits ci-dessus semble un peu confus, vous pouvez consulter cet article où j'ai écrit sur le [processus de configuration d'un blog Next.js](https://meje.dev/blog/how-i-built-this-blog).

Cela étant dit, le composant a rendu la liste des éléments du frontmatter, et cela semblait bien.

Mais, au moment où j'ai cliqué sur un élément, espérant faire défiler jusqu'à cette section, cela n'a pas fonctionné comme prévu. J'ai rencontré une erreur, que vous verrez dans la section suivante.

## **Comment utiliser extract-md-headings**

J'ai réalisé que lorsque je cliquais sur un élément dans le composant, le navigateur encodait l'URL du slug actuel avec un paramètre d'encodage pour les espaces – `%20%` – ce qui a conduit au problème.

Bien que j'aie réalisé que cela pouvait aussi être la manière dont je référençais les éléments de titre dans le `frontmatter`. Mais cela n'a pas fini par importer, car j'ai trouvé une alternative et cela a bien fonctionné.

Après m'être assuré que cela fonctionnait parfaitement, j'ai publié cette alternative en tant que [package](https://npmjs.com/package/extract-md-headings) sur le registre npm.

Le package étend une fonction, `extractHeadings()`, qui accepte une chaîne, en tant que chemin, vers l'endroit où se trouve le fichier markdown et extrait tout texte qui correspond à la manière dont les textes de titre sont écrits dans les fichiers markdown. Vous pouvez consulter le code source [ici](https://github.com/kaf-lamed-beyt/extract-md-headings/blob/834ad610c80db6a367260b3ec6927c9cd2099a5c/src/index.ts#L15-L36) si vous voulez voir comment cela fonctionne sous le capot.

Avec cet outil dans mon arsenal, j'ai modifié la méthode `getStaticProps` pour utiliser la fonction. Pourquoi ? vous pourriez me demander. Eh bien, parce que le package dépend uniquement du module `fs` de Node, ce qui équivaut à une approche de script côté serveur.

Avec Next.js, nous pouvons effectuer des opérations côté serveur dans le répertoire des pages avec l'une des méthodes de récupération de données, `getStaticProps`, `getStaticPaths`, et `getServerSideProps` :

```jsx
import React from 'react'
import { extractHeadings } from 'extract-md-headings'

export default function Blog({
  post: {
    fileContent,
    frontmatter: { title },
  },
}) {
  return (
    <>
      <Head>
        <title>{title}</title>
      </Head>
      <TableDesMatieres headings={fileContent} />
    </>
  )
}

export async function getStaticProps({ params }) {
  const { slug } = params
  const { frontmatter } = await getArticleFromSlug(slug)
  const mdxContent = extractHeadings(`/path/to/where/${slug}.mdx`)

  return {
    props: {
      post: {
        frontmatter,
        fileContent: mdxContent,
      },
    },
  }
}

```

La page `[slug].js` est maintenant consciente du `fileContent` via la propriété `heading` du composant `TOC`. Je dois donc la modifier pour qu'elle accommodate les propriétés que la fonction retourne.

```jsx
import React from 'react'
import { HeadingContainer } from './style/toc.styled'

export default function TableDesMatieres({ headings }) {
  return (
    <HeadingContainer>
      <p>Dans cet article</p>
      <ul>
        {headings.map(({ slug, title, id }) => (
          <li key={id}>
            <a href={`#${slug}`}>{title}</a>
          </li>
        ))}
      </ul>
    </HeadingContainer>
  )
}

```

Pour l'instant, le composant se contente de rendre la liste des éléments du tableau qui est retourné par la fonction, sans interactivité, sans moyen de suivre quel élément est actif, et bien d'autres choses que je n'ai pas encore pu ajouter.

## **Comment ajouter des états basés sur les clics et le défilement**

S'il y a une chose que j'aime dans React, c'est sa capacité à suivre l'état. J'ai vu comment cela fonctionne sur d'autres plateformes de documentation – lorsque vous cliquez sur un élément, il devient actif, lorsque vous faites défiler jusqu'à la section où il y a une balise de titre, il devient actif.

Beaucoup de gens ont différentes approches pour surveiller ces états. J'ai choisi de prendre la plus simple – changer la couleur – parce que, comme d'habitude, "je n'aime pas le stress". La couleur de texte par défaut dans l'UI de mon composant est un peu "grisâtre", donc lorsqu'il est actif, il devient blanc.

Je vais commencer par les extraits de la modification que j'ai apportée au composant avec le hook `useState`, quelques API DOM, et l'API web `getBoundingClientRect`. C'est beaucoup – je sais 😩. Mais, s'il vous plaît, restez avec moi, j'essaierai de le décomposer simplement.

Il est courant d'avoir une valeur par défaut – un booléen, une chaîne ou un nombre – lorsque nous utilisons le hook `useState`. Dans l'extrait ci-dessous, le composant utilise la propriété `headings` pour vérifier si la longueur du tableau n'est pas vide, est supérieure à zéro, et définit l'état par défaut du composant à celui du premier élément.

```js
const [active, setActive] = React.useState(
  headings.length > 0 ? headings[0].slug : ''
)

```

Si le tableau est vide, aucun élément n'aura le style d'état actif. Pour l'instant, si vous placez un attribut `onClick` dans l'élément de liste – comme je l'ai fait – et passez le `slug` comme argument, il basculera le style que vous avez écrit dans l'attribut `style`.

```jsx
<li
  key={index}
  onClick={() => setActive(slug)}
  style={{
    color: active === slug ? '#fff' : '',
  }}
>
  <a href={`#${slug}`}>{title}</a>
</li>

```

La gestion de l'état de défilement nécessiterait l'utilisation du hook `useEffect` de React car il contient toutes les méthodes de cycle de vie – `componentDidMount()`, `componentDidMount()`, et `componentWillUnmount()`. Ici, j'ai décidé de suivre l'état de défilement en écoutant l'événement de défilement natif avec l'interface `EventTarget` du DOM.

La fonction `handleScroll` ci-dessous mappe le résultat que nous obtenons de la fonction `extractHeadings()` en déstructurant la propriété `slug` de l'objet. Elle procède ensuite à retourner tous les éléments contenant un attribut `id` approprié avec `getElementById` et attribue la valeur à `headingElements`.

```js
const handleScroll = () => {
  const headingElements = headings.map(({ slug }) =>
    document.getElementById(slug)
  )
  const visibleHeadings = headingElements.filter((el) =>
    isElementInViewport(el)
  )
  if (visibleHeadings.length > 0) {
    setActive(visibleHeadings[0].id)
  }
}

```

Toujours dans cette fonction, les `visibleElements` sont filtrés à partir du tableau des `headingElements`, et la fonction `isElementInViewport` est utilisée pour vérifier quel élément de titre est actuellement dans le viewport – cela est possible avec `getBoundingClientRect`, j'y viendrai bientôt.

La fonction se termine par une condition pour définir un élément actif si la longueur des titres visibles est supérieure à zéro.

Maintenant, je peux aller de l'avant pour envelopper cette fonction dans l'Effect, initier le nettoyage de l'événement de défilement, et passer la propriété `headings` à l'intérieur du tableau de dépendances. Ensuite, l'Effect n'est déclenché que lorsque la propriété `headings` change.

```js
React.useEffect(() => {
  const handleScroll = () => {
    const headingElements = headings.map(({ slug }) =>
      document.getElementById(slug)
    )
    const visibleHeadings = headingElements.filter((el) =>
      isElementInViewport(el)
    )
    if (visibleHeadings.length > 0) {
      setActive(visibleHeadings[0].id)
    }
  }

  document.addEventListener('scroll', handleScroll)

  // nettoyer l'effet en supprimant l'écouteur d'événement
  return () => {
    document.removeEventListener('scroll', handleScroll)
  }
}, [headings])

```

`isElementInViewport` est la cerise sur le gâteau de cette fonctionnalité. La fonction accepte un élément, `el` comme argument, et vérifie si son rectangle de délimitation (ce qui prouve à nouveau que le principe de la boîte sur le web est correct) est à l'intérieur du viewport du navigateur.

```js
const isElementInViewport = (el) => {
  const rect = el.getBoundingClientRect()
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <=
      (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  )
}

```

Cela est possible grâce à l'API web `getBoundingClientRect`. La méthode retourne un objet contenant les coordonnées des bords supérieur, gauche, inférieur et droit de l'élément par rapport au viewport.

Lorsque `getBoundingClientRect` est appelé, il retourne un objet contenant les coordonnées des bords supérieur, gauche, inférieur et droit d'un élément de titre particulier par rapport au viewport.

Dans le contexte de cette fonctionnalité, l'élément qui est relatif au viewport est l'élément de titre qui est récupéré en utilisant la méthode `getElementById`.

La fonction retourne vrai si les coordonnées supérieure et gauche sont supérieures ou égales à zéro, et les coordonnées inférieure et droite sont inférieures ou égales à la hauteur et à la largeur du viewport, respectivement.

Pour que la fonction retourne `true`, nous devons obtenir la valeur de la hauteur et de la largeur du viewport. C'est pourquoi il est pratique de comparer ces valeurs avec `window.innerHeight` et `window.innerWidth` ou `documentElement.clientHeight` et `documentElement.clientWidth`.

## **Pourquoi le stress ? IntersectionObserver résout ce problème**

Je sais que prendre la route `intersectionObserver` m'aurait épargné beaucoup de stress. Mais, j'ai choisi cette approche néanmoins, parce que je voulais comprendre le fonctionnement interne de la manière dont cette fonctionnalité est construite par d'autres personnes.

Je pense qu'il existe un package d'observateur d'intersection que vous pouvez utiliser pour surveiller les événements de défilement dans les applications React, aussi. Vous n'aurez donc peut-être même pas besoin de prendre cette route. Mais je veux partager certaines des raisons pour lesquelles j'ai décidé d'utiliser cette API, au lieu de `IntersectionObserver`.

En termes de précision, `getBoundingClientRect` retourne une position plus précise de l'élément par rapport au viewport, tandis que `IntersectionObserver` utilise une approximation basée sur la boîte de délimitation de l'élément.

Cela signifie que `getBoundingClientRect` peut être plus précis pour certains cas d'utilisation, comme lorsque vous devez déclencher une action dès que l'élément entre dans le viewport – tout comme nous changeons l'état actif de l'élément de liste dans le composant.

En termes de compatibilité des navigateurs, `IntersectionObserver` est une API relativement nouvelle, et son support par d'autres navigateurs peut ne pas être disponible. Mais, `getBoundingClientRect` d'autre part est largement supporté par les navigateurs modernes.

Un avantage que `IntersectionObserver` a sur `getBoundingClientRect` est en termes de performance. Cela est dû au fait que l'API utilise un algorithme optimisé qui minimise la quantité de travail nécessaire pour détecter les changements dans l'état d'intersection lorsque vous suivez tant d'éléments.

L'API `getBoundingClientRect` ne peut pas gérer autant d'éléments.

## **Conclusion**

Je sais que beaucoup de gens préféreraient encore utiliser `intersectionObserver`. Mais, j'ai décidé de prendre cette autre approche car elle m'a ouvert les yeux sur le fonctionnement interne de `intersectionObserver` lui-même, et surtout, elle convenait à mon cas d'utilisation.

Voici à quoi ressemble la logique du composant TOC – sans le balisage. Copiez-le et utilisez-le si vous le souhaitez.

```jsx
import React from 'react'
import { HeadingContainer } from './style/toc.styled'

const TableDesMatieres = ({ headings }) => {
  const [active, setActive] = React.useState(
    headings.length > 0 ? headings[0].slug : ''
  )

  React.useEffect(() => {
    const handleScroll = () => {
      const headingElements = headings.map(({ slug }) =>
        document.getElementById(slug)
      )
      const visibleHeadings = headingElements.filter((el) =>
        isElementInViewport(el)
      )
      if (visibleHeadings.length > 0) {
        setActive(visibleHeadings[0].id)
      }
    }

    document.addEventListener('scroll', handleScroll)
    return () => {
      document.removeEventListener('scroll', handleScroll)
    }
  }, [headings])

  const isElementInViewport = (el) => {
    const rect = el.getBoundingClientRect()
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <=
        (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    )
  }

  return // component markup
}

export default TableDesMatieres

```

Si vous avez lu jusqu'à ce point, veuillez partager cet article. Merci de le faire. Vous pouvez également lire sur l'[API web getBoundingClientRect()](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) si vous voulez obtenir une compréhension approfondie.