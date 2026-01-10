---
title: Comment implémenter le défilement infini dans Next.js avec Intersection Observer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-05T15:38:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-infinite-scroll-in-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-ahmed-aqtai-63572.jpg
tags:
- name: Next.js
  slug: nextjs
- name: Web Development
  slug: web-development
seo_title: Comment implémenter le défilement infini dans Next.js avec Intersection
  Observer
seo_desc: "By Divine Orji\nCreators and developers continually come up with new ways\
  \ to enhance apps and provide value to users. \nOne feature that's useful for social\
  \ media and ecommerce apps in particular is infinite scroll. It provides a seamless\
  \ and intuitive..."
---

Par Divine Orji

Les créateurs et les développeurs ne cessent de trouver de nouvelles façons d'améliorer les applications et d'apporter de la valeur aux utilisateurs. 

Une fonctionnalité particulièrement utile pour les applications de réseaux sociaux et de commerce électronique est le défilement infini. Il offre une expérience de navigation fluide et intuitive en réduisant le temps nécessaire pour voir du nouveau contenu.

Cet article vous apprendra à implémenter le défilement infini dans une application Next.js en utilisant l'API Intersection Observer de JavaScript.

## Qu'est-ce que le défilement infini ?

Le défilement infini est une technique de conception web qui permet à votre site web ou à votre application de charger plus de contenu à mesure que l'utilisateur fait défiler vers le bas. 

Par exemple, supposons que votre site web ait de nombreux éléments à afficher (comme un fil d'actualités ou une liste de produits). Cette technique élimine le besoin de cliquer à travers de nombreuses pages, permettant aux utilisateurs d'explorer et de découvrir facilement du nouveau contenu.

Cela aide également à améliorer l'expérience utilisateur en réduisant le temps nécessaire pour charger de nouvelles pages, puisque le contenu se charge dynamiquement à mesure que l'utilisateur fait défiler.

![Pagination vs Défilement Infini - Smashing Magazine](https://www.freecodecamp.org/news/content/images/2022/12/pagination_vs_infinite.png)
_Pagination vs Défilement Infini - [Smashing Magazine](https://www.smashingmagazine.com/2013/05/infinite-scrolling-lets-get-to-the-bottom-of-this/" rel="noopener noreferrer)_

Vous pouvez l'implémenter dans votre projet en utilisant l'API Intersection Observer de JavaScript.

## Qu'est-ce que l'API Intersection Observer ?

Cette API basée sur le navigateur vous permet d'observer les changements dans la fenêtre d'affichage de votre application ou une intersection spécifique entre des éléments.

Elle fonctionne pour des cas d'utilisation comme le chargement paresseux, la transition d'animation fluide et le défilement infini. Vous pouvez utiliser cette API pour détecter lorsque certains éléments apparaissent à l'écran et déclencher une fonction pour apporter des modifications à l'application.

## CodeSandbox et Dépôt GitHub

La démonstration complète de cet article est disponible sur [CodeSandbox](https://codesandbox.io/p/github/dpkreativ/infinitea/draft/infinitea?file=%2Fpages%2Findex.js). Vous pouvez également consulter son code source sur [GitHub](https://github.com/dpkreativ/infinitea).

## Prérequis

Pour suivre cet article sans difficulté, vous aurez besoin des éléments suivants :

* Connaissance de JavaScript et React.
* Un [compte GitHub](https://github.com/) pour générer le code de démarrage et stocker votre code à distance. Vous avez également besoin de [Git](https://git-scm.com/) pour suivre les changements de votre base de code.
* [Yarn](https://classic.yarnpkg.com/lang/en/) installé sur votre ordinateur. Vous devez avoir [Node.js](https://nodejs.org/en/) installé sur votre ordinateur, qui vient avec [NPM](https://www.npmjs.com/) pour installer Yarn.
* Une expérience avec [Next.js](https://nextjs.org/), bien que non requise, vous donnera un avantage et vous aidera à mieux comprendre cet article.
* Une familiarité avec [Tailwind](https://tailwindcss.com/), le framework CSS utilisé dans ce projet. Ce n'est pas strictement requis.

## Comment configurer le projet

Cliquez [ici](https://github.com/dpkreativ/infinitea-starter/generate) pour générer les fichiers de démarrage de ce projet dans votre navigateur préféré :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/generate_repo.png)

Après avoir généré le dépôt, copiez son URL Git afin de pouvoir le cloner sur votre PC :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/project_repo.png)

Dans le terminal de votre PC, exécutez la commande suivante pour cloner votre dépôt :

```bash
git clone theGitUrlOfYourRepo

```

Après avoir cloné le projet avec succès, installez les dépendances en exécutant la commande suivante dans le terminal de votre projet :

```bash
yarn

# ou npm install. Mais pour cette démonstration, yarn est préféré

```

Une fois terminé, exécutez `yarn dev` dans le terminal de votre projet, et naviguez vers `localhost:3000` sur votre navigateur pour voir l'interface utilisateur de démarrage :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/starter_ui.png)

## Comment gérer le contenu

Pour ce projet, vous obtiendrez des images de thé depuis Unsplash via son API publique. Alors, naviguez vers [https://unsplash.com/developers](https://unsplash.com/developers) et cliquez sur "Register as a developer" ou "Login" si vous avez un compte Unsplash :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/unsplash_login.png)

Après une connexion réussie, cliquez sur "Your apps" et "New Application". Acceptez les termes de l'accord, puis remplissez le nom et la description de votre application :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/app_info.png)

Après avoir créé votre application sur Unsplash, faites défiler vers le bas pour copier votre Access Key.

Ouvrez votre projet dans votre éditeur de code préféré et créez un fichier `.env.local` dans son dossier racine pour stocker votre Access Key :

```
NEXT_PUBLIC_UNSPLASH=votreClefDAccesAPIUnsplash

```

Dans votre éditeur de code, naviguez vers `pages/index.js` et mettez à jour la fonction `fetchImages` avec le code suivant :

```jsx
const fetchImages = async () => {
  const response = await fetch(`${BASE_URL}?query=tea&page=${page}`, {
    headers: {
      Authorization: `Client-ID ${process.env.NEXT_PUBLIC_UNSPLASH}`,
    },
  });
  const { results } = await response.json();
  setImages((prev) => [...prev, ...results]);
}; 

```

Ici, vous avez fait ce qui suit :

* Implémenté la fonction `fetch` de JavaScript pour faire une requête HTTP vers le point de terminaison de l'API d'Unsplash. Le point de terminaison contient le `BASE_URL`, votre `query`, et la `page` actuelle.
* Dans votre fonction `fetch`, l'objet options inclut une propriété `headers` qui spécifie un en-tête `Authorization` avec une valeur de `Client-ID ${process.env.NEXT_PUBLIC_UNSPLASH}`, qui est votre clé d'accès API.
* Vous avez ensuite analysé votre `response` en JSON et déstructuré la propriété `results`.
* Enfin, vous avez mis à jour votre état `images` en concaténant la valeur précédente de `images` avec le tableau `results`.

Dans votre fichier `pages/index.js`, remplacez `// useEffect here` par le code suivant :

```jsx
useEffect(() => {
  fetchImages();
}, [page]);

```

Ici, vous avez configuré useEffect pour déclencher la fonction `fetchImages` chaque fois que `page` est mis à jour.

## Comment implémenter l'API Intersection Observer

Naviguez vers `components/ui/Card.js` et mettez à jour `useEffect` avec le code suivant :

```jsx
useEffect(() => {
  if (!cardRef?.current) return;

  const observer = new IntersectionObserver(([entry]) => {
    if (isLast && entry.isIntersecting) {
      newLimit();
      observer.unobserve(entry.target);
    }
  });

  observer.observe(cardRef.current);
}, [isLast]);

```

Ici, vous avez configuré un Intersection Observer avec le hook `useEffect`. Il détecte lorsque chaque composant Card devient visible dans la fenêtre d'affichage.

Lorsque le composant Card contient le dernier élément de votre tableau d'images et est visible (`entry.isIntersecting`), l'API Intersection Observer déclenche la fonction `newLimit` et arrête d'observer l'élément cible.

Le hook `useEffect` s'exécutera chaque fois que la variable `isLast` changera.

Mettez à jour les props dans votre composant card pour inclure `newLimit` et `isLast` :

```jsx
export default function Card({
  creditUrl,
  imgAlt = 'placeholder',
  imgSrc = '/placeholder.jpg',
  shotBy,
  newLimit,
  isLast,
}) {
// contenu du code
}

```

Dans votre `pages/index.js`, mettez à jour `<HomeLayout>` avec le code suivant :

```jsx
<HomeLayout>
  {images.map((image, index) => (
    <Card
      key={image.id}
      imgSrc={image.urls.regular}
      imgAlt={image.alt_description}
      shotBy={image.user.name}
      creditUrl={image.links.html}
      isLast={index === images.length - 1}
      newLimit={() => setPage(page + 1)}
    />
  ))}
</HomeLayout>;

```

Ici, vous avez parcouru votre tableau `images`, en rendant une liste de composants `Card` qui affichent chacun l'image, le photographe et le lien vers le post original sur Unsplash.

La prop `isLast` vérifie si le composant de carte actuel est le dernier dans le tableau `images`. Elle déclenche ensuite la fonction `newLimit` de votre API Intersection Observer pour mettre à jour le compteur de pages.

Voici le résultat final ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/infinitea_demo.gif)

## Conclusion

Dans cet article, vous avez appris à implémenter le défilement infini dans une application Next.js. Les capacités de l'API Intersection Observer ne se limitent pas au défilement infini et au chargement paresseux. Vous découvrirez davantage en pratiquant. Les ressources ci-dessous sont un bon point de départ.