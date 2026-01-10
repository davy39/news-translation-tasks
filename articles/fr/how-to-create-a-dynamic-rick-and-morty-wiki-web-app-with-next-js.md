---
title: Comment créer une application Web Wiki dynamique Rick and Morty avec Next.js
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-07-09T05:49:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-dynamic-rick-and-morty-wiki-web-app-with-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/nextjs.jpg
tags:
- name: Next.js
  slug: nextjs
- name: progressive web app
  slug: progressive-web-app
- name: Web Applications
  slug: web-applications
seo_title: Comment créer une application Web Wiki dynamique Rick and Morty avec Next.js
seo_desc: 'Building web apps with dynamic APIs and server side rendering are a way
  to give people a great experience both with content and speed. How can we use Next.js
  to easily build those apps?


  What are we going to build?

  What is Next.js?

  Step 0: Setting up...'
---

La création d'applications Web avec des API dynamiques et le rendu côté serveur est un moyen de offrir aux gens une excellente expérience à la fois en termes de contenu et de vitesse. Comment pouvons-nous utiliser Next.js pour construire facilement ces applications ?

* [Qu'allons-nous construire ?](#heading-quallons-nous-construire)
* [Qu'est-ce que Next.js ?](#heading-quest-ce-que-nextjs)
* [Étape 0 : Configuration d'une nouvelle application Next.js](#heading-etape-0-installation-dune-nouvelle-application-nextjs)
* [Étape 1 : Récupération des personnages de Rick and Morty avec une API dans Next.js](#heading-etape-1-recuperation-des-personnages-de-rick-and-morty-avec-une-api-dans-nextjs)
* [Étape 2 : Affichage des personnages de Rick and Morty sur la page](#heading-etape-2-affichage-des-personnages-de-rick-and-morty-sur-la-page)
* [Étape 3 : Chargement de plus de personnages de Rick and Morty](#heading-etape-3-chargement-de-plus-de-personnages-de-rick-and-morty)
* [Étape 4 : Ajout de la possibilité de rechercher des personnages de Rick and Morty](#heading-etape-4-ajout-de-la-possibilite-de-rechercher-des-personnages-de-rick-and-morty)
* [Étape 5 : Utilisation de routes dynamiques pour lier aux pages des personnages de Rick and Morty](#heading-etape-5-utilisation-de-routes-dynamiques-pour-lier-aux-pages-des-personnages-de-rick-and-morty)
* [Étape Bonus : Déployez votre wiki Rick and Morty sur Vercel !](#heading-etape-bonus-deployez-votre-wiki-rick-and-morty-sur-vercel)

%[https://www.youtube.com/watch?v=iW39Merz0zE]

## Qu'allons-nous construire ?

Nous allons nous amuser et construire une application Web qui sert de wiki de base pour les personnages de Rick and Morty.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-morty-wiki-nextjs-demo-1.jpg)
_Démo du Wiki Rick and Morty_

Notre application va consister en quelques éléments :

* Une liste de personnages sur la page d'accueil
* Un bouton qui peut charger plus de personnages, car l'API est paginée
* Une boîte de recherche pour chercher des personnages
* Une page de personnage avec des détails de base

Nous allons apprendre quelques concepts comme :

* Comment lancer une application Web avec [Next.js](https://nextjs.org/)
* Comment récupérer et utiliser des données [à partir d'une API](https://rickandmortyapi.com/api/character/)
* Comment [pré-rendre des données à partir d'une API](https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering)
* Comment configurer le [routage dynamique](https://nextjs.org/docs/routing/dynamic-routes)

## Qu'est-ce que Next.js ?

[Next.js](https://nextjs.org/) est un framework React de [Vercel](https://vercel.com/). Il vous permet de construire facilement des applications Web dynamiques légères avec une tonne de fonctionnalités modernes que vous attendez dès la sortie de la boîte.

Vercel, l'entreprise qui soutient Next.js, est un service qui vous permet d'automatiser les pipelines de développement continu pour déployer facilement des applications Web dans le monde. Nous allons également utiliser l'outil de ligne de commande de Vercel pour déployer optionnellement notre nouvelle démo de wiki.

## Étape 0 : Configuration d'une nouvelle application Next.js

Pour commencer, lançons notre projet Next.js. Nous allons utiliser npm ou yarn pour commencer :

```shell
yarn create next-app
# ou
npx create-next-app

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/yarn-create-next-app.jpg)
_Création d'une nouvelle application Next.js_

Une fois que vous avez exécuté cette commande, elle vous posera quelques questions. Je vais appeler mon projet `my-rick-and-morty-wiki`, mais vous pouvez le nommer comme vous le souhaitez.

Elle vous demandera ensuite quel modèle choisir — allez-y et sélectionnez le modèle par défaut.

Enfin, elle installera toutes les dépendances.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/successfully-created-next-app-terminal.jpg)
_Création réussie d'une nouvelle application Next.js_

Lorsque c'est terminé, vous pouvez naviguer vers ce nouveau répertoire et exécuter :

```shell
yarn dev
# ou
npm run dev

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/develop-next-app.jpg)
_Démarrage du serveur de développement Next.js_

Vous devriez maintenant avoir un serveur local en cours d'exécution à l'adresse [http://localhost:3000](http://localhost:3000) !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/default-template-next-app.jpg)
_Modèle par défaut de Next.js_

## Étape 1 : Récupération des personnages de Rick and Morty avec une API dans Next.js

Maintenant que nous avons notre application configurée, la première chose dont nous avons besoin pour construire notre wiki est une liste de personnages.

Pour ce faire, nous allons commencer par notre page d'accueil dans `pages/index.js`.

Next.js échafaudage cette page pour nous automatiquement. C'est la première page que quelqu'un verra sur notre site Web et elle a quelques fonctionnalités de base dans le modèle par défaut comme un titre, une grille simple et quelques styles.

Actuellement, cette page ne demande aucune donnée. Pour obtenir nos personnages, nous allons sauter directement dans la demande côté serveur.

Pour ce faire, Next.js nous permet d'exporter une fonction asynchrone `getServerSideProps` juste à côté de notre page, qu'il utilisera pour injecter notre page avec toutes les données que nous récupérons.

Commençons par ajouter le snippet suivant au-dessus de notre fonction composant `Home` :

```js
const defaultEndpoint = `https://rickandmortyapi.com/api/character/`;

export async function getServerSideProps() {
  const res = await fetch(defaultEndpoint)
  const data = await res.json();
  return {
    props: {
      data
    }
  }
}

```

Voici ce que nous faisons :

* Nous définissons une variable appelée `defaultEndpoint` qui définit simplement notre point de terminaison d'API par défaut
* Nous définissons notre fonction `getServerSideProps` que nous utiliserons pour récupérer nos données
* Dans cette fonction, nous utilisons d'abord l'API `fetch` pour faire une requête à notre point de terminaison
* Avec sa réponse, nous exécutons la méthode `json` afin que nous puissions récupérer la sortie au format JSON
* Enfin, nous retournons un objet où nous rendons nos `data` disponibles en tant que prop dans la propriété `props`

Maintenant que nous faisons cette requête, nous devons la rendre disponible à l'utilisation.

Nos `data` sont mises à disposition en tant que prop, alors créons un argument dans notre fonction composant `Home` pour les récupérer :

```
export default function Home({ data }) {

```

Pour tester cela, nous pouvons utiliser `console.log` pour voir les résultats :

```js
export default function Home({ data }) {
  console.log('data', data);

```

Et une fois que nous avons sauvegardé et rechargé la page, nous pouvons maintenant voir nos résultats !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/nextjs-app-logging-server-rendered-data.jpg)
_Journalisation des données des personnages de Rick and Morty dans l'application Next.js_

[Suivez le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/3850e08e47654053d33f8440557e882e3579b335)

## Étape 2 : Affichage des personnages de Rick and Morty sur la page

Maintenant que nous avons nos données de personnages, affichons-les réellement sur notre page.

Pour commencer, je vais faire quelques ajustements. Je vais mettre à jour :

* Le titre `<h1>` en "Wubba Lubba Dub Dub !"
* La description `<p>` en "Wiki des personnages de Rick and Morty"

Je vais également mettre à jour le contenu de `<div className="grid">` en :

```jsx
<ul className="grid">
  <li className="card">
    <a href="https://nextjs.org/docs">
      <h3>Mon Personnage</h3>
    </a>
  </li>
</ul>

```

Ce que je fais ici :

* Je transforme le `<div>` en une liste car cela sera meilleur pour l'accessibilité
* Je fais du `<li>` de la `<ul>` la `card`
* Et je change simplement le `<h3>` en "Mon Personnage" temporairement

Pour nous assurer que notre nouvelle `<ul>` ne perturbe pas la mise en page avec ses styles par défaut, ajoutons également ce qui suit à la fin des règles CSS `.grid` :

```css
list-style: none;
margin-left: 0;
padding-left: 0;

```

Et maintenant, si nous regardons la page, nous devrions voir nos changements de base.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/basic-wiki-page-with-title.jpg)
_Titre mis à jour dans le Wiki Rick and Morty_

Ensuite, faisons en sorte que notre grille charge nos personnages.

En haut de notre fonction composant `Home`, ajoutons :

```js
const { results = [] } = data;

```

Cela va déstructurer notre tableau de résultats à partir de notre objet de données.

Ensuite, mettons à jour notre code de grille :

```jsx
<ul className="grid">
  {results.map(result => {
    const { id, name } = result;
    return (
      <li key={id} className="card">
        <a href="#">
          <h3>{ name }</h3>
        </a>
      </li>
    )
  })}
</ul>

```

Voici ce que nous faisons :

* Nous utilisons la méthode `map` pour créer un nouvel élément de liste pour chacun de nos résultats (ou personnages)
* À l'intérieur de cela, nous récupérons l'`id` et le `name` de chaque résultat de personnage
* Nous utilisons l'ID comme `key` pour notre élément de liste pour rendre React heureux
* Nous mettons à jour notre en-tête avec le `name`

Et une fois que vous avez sauvegardé et rechargé la page, nous devrions maintenant voir une nouvelle liste de nos personnages de l'API !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-with-character-names.jpg)
_Liste dynamique des noms de personnages de Rick and Morty_

Nous pouvons également ajouter une image pour chaque personnage.

Tout d'abord, à l'intérieur de notre grille, mettons à jour notre instruction de déstructuration pour récupérer l'URL de l'image :

```js
const { id, name, image } = result;

```

Ensuite, ajoutons l'image au-dessus de notre en-tête :

```jsx
<img src={image} alt={`${name} Thumbnail`} />

```

Et maintenant, chacun de nos personnages montre également leur photo !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-with-character-names-and-pictures.jpg)
_Ajout d'images de personnages sur le Wiki Rick and Morty_

[Suivez le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/fd959ac66a51900d2fcff9130925d8979ab8db32)

## Étape 3 : Chargement de plus de personnages de Rick and Morty

Maintenant, si vous remarquez, lorsque nous chargeons la page, nous n'obtenons qu'un certain nombre de résultats. Par défaut, l'API ne renverra pas la liste complète des personnages, ce qui est logique, car elle est vraiment longue !

Au lieu de cela, elle utilise la pagination et nous fournit le point de terminaison "next", ou la page suivante de résultats, qui nous permettra de charger plus de résultats.

Pour commencer, nous allons utiliser le hook `useState` de React pour stocker nos résultats dans l'état. Nous aurons alors la possibilité de mettre à jour cet état avec plus de résultats.

Tout d'abord, importons `useState` de React :

```
import { useState } from 'react';

```

Ensuite, créons notre état en renommant d'abord notre variable `results` originale et en configurant notre instance `useState` :

```js
const { results: defaultResults = [] } = data;
const [results, updateResults] = useState(defaultResults);

```

Si vous sauvegardez cela et rechargez la page, vous ne devriez pas encore remarquer de différence.

Ensuite, nous voulons pouvoir comprendre dans notre application quel est notre point de terminaison actuel auquel nous avons fait une requête, quel est le point de terminaison suivant, quel est le point de terminaison précédent, et comment nous pouvons tout mettre à jour.

Pour ce faire, nous allons créer plus d'états. Tout d'abord, nous voulons mettre à jour notre instruction de déstructuration avec nos `data` pour obtenir la valeur `info` :

```js
const { info, results: defaultResults = [] } = data;

```

Ensuite, configurons un état en utilisant cela :

```js
const [page, updatePage] = useState({
  ...info,
  current: defaultEndpoint
});

```

Ici, nous :

* Créons un nouvel état `page` que nous pouvons utiliser pour obtenir nos valeurs `prev` et `next`
* Nous créons également une nouvelle valeur appelée `current` que nous allons commencer par utiliser notre `defaultEndpoint`, qui était la requête faite sur le serveur

L'idée ici est que lorsque nous voulons charger plus de résultats, nous allons configurer du code pour surveiller la valeur de `current` et mettre à jour cette valeur avec `next`, donc lorsque cela change, nous ferons une nouvelle requête.

Pour ce faire, ajoutons un hook `useEffect` pour faire cette requête :

```js
const { current } = page;

useEffect(() => {
  if ( current === defaultEndpoint ) return;

  async function request() {
    const res = await fetch(current)
    const nextData = await res.json();

    updatePage({
      current,
      ...nextData.info
    });

    if ( !nextData.info?.prev ) {
      updateResults(nextData.results);
      return;
    }

    updateResults(prev => {
      return [
        ...prev,
        ...nextData.results
      ]
    });
  }

  request();
}, [current]);

```

Voici ce qui se passe :

* Tout d'abord, nous déstructurons la valeur `current` de `page`
* Nous créons un hook `useEffect` qui utilise `current` comme dépendance. Si la valeur change, le hook s'exécutera
* Si notre valeur `current` est la même que `defaultEndpoint`, nous n'exécutons pas le code, car nous avons déjà nos données de requête. Cela évite une requête supplémentaire au chargement
* Nous créons une fonction asynchrone que nous pouvons exécuter. Cela nous permet d'utiliser `async/await` à l'intérieur de notre hook `useEffect`
* Nous faisons la requête au point de terminaison `current`. Avec cette requête réussie, nous mettons à jour l'état `page` avec les nouvelles `info` comme les nouvelles valeurs `prev` et `next`
* Si notre requête n'a pas de valeur précédente, cela signifie qu'il s'agit du premier ensemble de résultats pour la requête donnée, donc nous devrions remplacer complètement nos résultats pour commencer à partir de zéro
* Si nous avons une valeur précédente, nous concaténons nos nouveaux résultats aux anciens, car cela signifie que nous venons de demander la page suivante de résultats

Encore une fois, si vous sauvegardez et rechargez la page, cela ne devrait toujours rien faire et votre page devrait être là où elle était avant.

Enfin, nous allons créer un bouton "Load More" et l'utiliser pour mettre à jour la valeur `current` afin de déclencher une nouvelle requête lorsque nous voulons une nouvelle page.

Pour ce faire, ajoutons d'abord un nouveau bouton sous notre grille :

```jsx
<p>
  <button>Load More</button>
</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-load-more-button.jpg)
_Bouton "Load More" ajouté à la liste des personnages du Wiki Rick and Morty_

Maintenant, nous voulons que quelque chose se passe lorsque nous cliquons sur ce bouton, alors ajoutons d'abord un gestionnaire d'événements :

```jsx
<button onClick={handleLoadMore}>Load More</button>

```

Ensuite, au-dessus de l'instruction de retour du composant, ajoutons cette fonction :

```js
function handleLoadMore() {
  updatePage(prev => {
    return {
      ...prev,
      current: page?.next
    }
  });
}

```

Lorsque cette fonction est déclenchée par notre clic sur le bouton, elle mettra à jour notre état `page` avec une nouvelle valeur `current`, spécifiquement avec la valeur `next` qui est le point de terminaison pour récupérer notre page suivante de résultats.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-load-more-characters.gif)
_Chargement de plus de résultats dans le Wiki Rick and Morty_

Et lorsque nous sauvegardons et rechargeons la page, c'est exactement ce qu'elle fait !

[Suivez le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/157eda9c3a93eb79e6e063eaa60f7abe82246fc5)

## Étape 4 : Ajout de la possibilité de rechercher des personnages de Rick and Morty

L'une des fonctionnalités que notre API Rick and Morty fournit est la possibilité de filtrer les résultats — donc essentiellement la possibilité de rechercher. Alors ajoutons cela comme une fonctionnalité.

Tout d'abord, nous avons besoin d'un formulaire de recherche. Ajoutons le snippet suivant sous le paragraphe de description :

```jsx
<form className="search">
  <input name="query" type="search" />
  <button>Search</button>
</form>

```

Ensuite, ajoutons ces styles à la fin du premier bloc `<style jsx>` :

```css
.search input {
  margin-right: .5em;
}

@media (max-width: 600px) {
  .search input {
    margin-right: 0;
    margin-bottom: .5em;
  }

  .search input,
  .search button {
    width: 100%;
  }
}

```

Cela va donner un peu d'espace à notre champ de recherche et au bouton ainsi que le rendre compatible avec les mobiles. N'hésitez pas à ajouter plus de styles si vous le souhaitez.

Et si nous sauvegardons et actualisons notre page, nous avons un formulaire simple.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-character-wiki-search-form.jpg)
_Formulaire de recherche ajouté au Wiki Rick and Morty_

Il ne fait encore rien, alors faisons en sorte qu'il recherche lorsque nous soumettons le formulaire.

Pour commencer, ajoutons un attribut `onSubmit` à notre formulaire :

```jsx
<form className="search" onSubmit={handleOnSubmitSearch}>

```

Et pour aller avec cela, définissons notre fonction de soumission au-dessus de notre instruction return :

```js
function handleOnSubmitSearch(e) {
  e.preventDefault();

  const { currentTarget = {} } = e;
  const fields = Array.from(currentTarget?.elements);
  const fieldQuery = fields.find(field => field.name === 'query');

  const value = fieldQuery.value || '';
  const endpoint = `https://rickandmortyapi.com/api/character/?name=${value}`;

  updatePage({
    current: endpoint
  });
}

```

Voici ce que nous faisons :

* Tout d'abord, nous empêchons le comportement par défaut de la soumission du formulaire pour empêcher la page de se recharger
* Ensuite, nous récupérons la cible actuelle, qui est notre formulaire
* Nous récupérons les champs du formulaire en utilisant la propriété elements. Nous transformons également cela en un tableau pour qu'il soit facile à utiliser
* Nous recherchons dans ces champs notre champ de requête
* Nous récupérons la valeur de ce champ
* Nous créons un nouveau point de terminaison où nous filtrons par nom en utilisant cette valeur de requête
* Enfin, nous mettons à jour notre propriété `current` dans notre état de page pour déclencher une nouvelle requête à ce point de terminaison

Et une fois que vous avez sauvegardé cela et rechargé la page, vous pouvez maintenant essayer la recherche. Vous devriez pouvoir taper un nom comme "rick", appuyer sur entrée ou cliquer sur le bouton de recherche, et vous devriez maintenant voir des résultats filtrés avec les différents ricks à travers l'univers !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-search-rick.jpg)
_Recherche de Rick sur le Wiki Rick and Morty_

[Suivez le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/f365d2bc7fc3ca48c2ad693d457a6b6984ea67c3)

## Étape 5 : Utilisation de routes dynamiques pour lier aux pages des personnages de Rick and Morty

Maintenant que nous avons tous nos personnages, nous voulons pouvoir cliquer sur ces personnages et afficher quelques détails supplémentaires. Pour ce faire, nous allons utiliser les routes dynamiques de Next.js.

La première chose que nous devons faire est de configurer correctement notre structure de répertoires pour que Next.js reconnaisse le chemin dynamique. Afin de configurer une route dynamique, nous devons créer notre dossier exactement comme suit :

```
- pages
-- character
--- [id]
-- index.js

```

Oui, cela signifie que vous créez littéralement un dossier avec le nom de `[id]`, ce qui n'est pas censé être remplacé. Next.js reconnaît ce motif et nous permettra de l'utiliser pour créer une route dynamique.

Pour faciliter la création de la page, nous allons simplement dupliquer notre page d'accueil en copiant notre fichier `pages/index.js` dans notre répertoire suivant.

Ainsi, nous devrions maintenant avoir une nouvelle page à `pages/character/[id]/index.js`.

Ensuite, supprimons un tas de choses pour que nous puissions obtenir un bon point de départ :

* Supprimez tout ce qui se trouve au-dessus de l'instruction `return` dans le composant de fonction de notre page
* Renommez le composant de fonction Character
* Supprimez les imports `useState` et `useEffect`
* Supprimez la description, le formulaire de recherche, la grille et le bouton de chargement
* Optionnel : supprimez le pied de page

Une fois que vous avez terminé, le haut de notre composant de fonction de page devrait ressembler à ceci :

```jsx
export default function Character({ data }) {
  return (
    <div className="container">
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className="title">
          Wubba Lubba Dub Dub!
        </h1>
      </main>

```

Bien qu'il y ait du CSS dont nous n'avons pas besoin, nous allons tout laisser là pour cette démo. N'hésitez pas à nettoyer une partie de cela plus tard.

Si vous naviguez manuellement vers /character/1, vous devriez maintenant voir une page simple avec juste un titre :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/new-character-page-basic-title.jpg)
_Page de personnage simple_

Ensuite, mettons à jour les données que nous récupérons. Nous pouvons réutiliser la plupart du code dans notre fonction `getServerSideProps`.

Nous allons ajouter un nouvel argument à cette fonction `getServerSideProps` :

```js
export async function getServerSideProps({ query }) {

```

Lorsque notre page est rendue, Next.js injecte des données dans notre page et la fonction `getServerSideProps` concernant l'environnement. Ici, nous déstructurons ces données pour récupérer l'objet `query` qui inclura tous les attributs de routage dynamique, tels que le `[id]` que nous définissons dans la route.

Ensuite, en haut de la fonction `getServerSideProps`, déstructurons l'ID :

```js
const { id } = query;

```

Et enfin, utilisons cet ID pour créer dynamiquement un point de terminaison que nous utiliserons pour récupérer les données de notre personnage :

```js
const res = await fetch(`${defaultEndpoint}${id}`);

```

Ici, nous utilisons notre point de terminaison de personnage et nous ajoutons l'ID dynamique de notre URL à la fin de l'URL.

Pour tester cela, ajoutons un `console.log` en haut de la fonction `Character` :

```jsx
export default function Character({ data }) {
  console.log('data', data);

```

Et si nous cliquons sur sauvegarder et rechargeons notre page, nous devrions maintenant voir les détails de l'utilisateur sur le personnage numéro 1 enregistrés, qui est Rick Sanchez !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-character-page-console-log-data.jpg)
_Journalisation des données individuelles des personnages de Rick and Morty_

Alors nous avons les données, ajoutons-les à notre page.

En haut de la fonction de personnage, ajoutons cette instruction de déstructuration :

```js
const { name, image, gender, location, origin, species, status } = data;

```

Cela nous donne un tas d'attributs que nous obtenons directement de cet objet de données que nous avons vu journalisé.

Pour l'utiliser, nous pouvons commencer par mettre à jour le titre avec ce nom :

```jsx
<title>{ name }</title>

```

Aussi le `<h1>` :

```jsx
<h1 className="title">{ name }</h1>

```

À ce stade, nous devrions maintenant voir dynamiquement le nom de Rick.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-character-page-dynamic-title.jpg)
_Titre de page de personnage dynamique de Rick and Morty_

Ensuite, ajoutons ce bloc sous notre `<h1>` pour inclure plus de détails sur notre personnage :

```jsx
<div className="profile">
  <div className="profile-image">
    <img src={image} alt={name} />
  </div>
  <div className="profile-details">
    <h2>Character Details</h2>
    <ul>
      <li>
        <strong>Name:</strong> { name }
      </li>
      <li>
        <strong>Status:</strong> { status }
      </li>
      <li>
        <strong>Gender:</strong> { gender }
      </li>
      <li>
        <strong>Species:</strong> { species }
      </li>
      <li>
        <strong>Location:</strong> { location?.name }
      </li>
      <li>
        <strong>Originally From:</strong> { origin?.name }
      </li>
    </ul>
  </div>
</div>

```

Ici, nous utilisons l'`image` de nos personnages pour afficher une photo de notre personnage et d'autres métadonnées variées pour ajouter des détails sur le personnage.

Nous pouvons suivre cela en ajoutant ce snippet de CSS à nos styles :

```css
.profile {
  display: flex;
  margin-top: 2em;
}

@media (max-width: 600px) {
  .profile {
    flex-direction: column;
  }
}

.profile-image {
  margin-right: 2em;
}

@media (max-width: 600px) {
  .profile-image {
    max-width: 100%;
    margin: 0 auto;
  }
}

```

Et maintenant nous avons notre bio de personnage !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-character-page-rick-sanchez.jpg)
_Page de personnage dynamique de Rick Sanchez_

Alors un rapide récapitulatif, nous avons notre nouvelle page dynamique. Nous pouvons aller à `/character/1` ou n'importe quel ID pour voir un personnage spécifique. Mettons maintenant à jour notre page d'accueil pour lier à ces pages.

De retour sur `pages/index.js`, notre page d'accueil, importons d'abord le composant `Link` de Next.js :

```js
import Link from 'next/link'

```

Ensuite, à l'intérieur de notre grille où nous parcourons notre liste de résultats, utilisons notre composant `<Link>` et mettons à jour notre code :

```jsx
<li key={id} className="card">
  <Link href="/character/[id]" as={`/character/${id}`}>
    <a>
      <img src={image} alt={`${name} Thumbnail`} />
      <h3>{ name }</h3>
    </a>
  </Link>
</li>

```

Voici ce que nous faisons :

* Tout d'abord, nous enveloppons notre élément `<a>` avec un composant `<Link>`
* Nous ajoutons un `href` et les propriétés `as` pour décrire à Next.js quelle page nous voulons lier. Nous devons utiliser la propriété `as` car il s'agit d'un lien dynamique
* Nous supprimons le `href` de notre élément `<a>` car il est maintenant appliqué à l'élément `<Link>`

Si nous sauvegardons et rechargeons notre page d'accueil, nous remarquerons que rien n'a changé, mais lorsque nous cliquons sur l'un de nos personnages, nous allons maintenant sur leur page de bio !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-navigate-to-jerry-smith.gif)
_Navigation vers la page de personnage de Jerry Smith sur le Wiki Rick and Morty_

Enfin, ajoutons également un bouton à notre page de bio de personnage qui renvoie à notre page d'accueil pour faciliter la navigation.

Tout d'abord, importons le composant `Link` :

```
import Link from 'next/link';

```

À la fin de notre balise `<main>` sous notre div `.profile`, ajoutons ce code :

```
<p className="back">
  <Link href="/">
    <a>
      Back to All Characters
    </a>
  </Link>
</p>

```

Et nous pouvons ajouter les styles de base suivants pour qu'il ressemble simplement à un lien :

```css
.back a {
  color: blue;
  text-decoration: underline;
}

```

Et si nous rechargeons la page, nous avons maintenant un lien sur lequel nous pouvons cliquer pour revenir à la page principale avec tous nos personnages !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-back-to-all-characters.gif)
_Lien "Retour à tous les personnages" sur la page de personnage de Rick and Morty_

[Suivez le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/61ec2f5b2092278dc3983c339fa4e556a5c7862c)

## Étape Bonus : Déployez votre wiki Rick and Morty sur Vercel !

Parce que nous utilisons Next.js, Vercel rend le déploiement de notre application super simple.

Pour ce faire, nous devons [installer le CLI Vercel](https://vercel.com/download). Nous pouvons le faire en l'installant en tant que module npm globalement :

```shell
yarn global add vercel
# ou 
npm i -g vercel

```

Maintenant, vous pouvez exécuter la commande `vercel` dans votre terminal.

La première fois que vous exécutez cela, vous serez invité à vous connecter. Vous devrez utiliser votre compte Vercel pour ce faire. Si vous n'en avez pas, vous devrez [vous inscrire pour un compte gratuit](https://vercel.com/signup).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/vercel-cli-login.jpg)
_Connexion au CLI Vercel_

Avec le CLI Vercel installé, nous pouvons simplement exécuter `vercel` dans notre répertoire de projet, remplir quelques questions, et il se déployera automatiquement !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/vercel-cli-deploy.jpg)
_Déploiement de l'application avec le CLI Vercel_

Vous pouvez utiliser presque toutes les valeurs par défaut, bien que vous devrez probablement utiliser un nom de projet différent de celui que j'utilise.

Mais une fois terminé, nous avons maintenant déployé avec succès notre nouvelle application sur Vercel !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-deployed-to-vercel.jpg)
_Application Wiki Rick and Morty terminée_

## Que pouvons-nous faire d'autre ?

### Plus de pages dynamiques

Chaque fois que vous faites une requête à un personnage, l'API renvoie d'autres points de terminaison que vous pouvez utiliser tels que les lieux et les épisodes. Nous pouvons utiliser ces points de terminaison et créer de nouvelles pages dynamiques, tout comme nos pages de profil de personnage dynamiques, pour permettre aux gens de voir plus d'informations sur un lieu ou un épisode spécifique.

### Ajoutez des styles

Nous avons gardé certains des styles de base que Next.js a inclus et ajouté quelques styles de base juste à des fins de démonstration. Mais maintenant que vous avez terminé, vous pouvez vous amuser et le personnaliser !

### Ajoutez des filtres de personnages

En plus de filtrer par nom, [l'API prend également en charge le filtrage par statut](https://rickandmortyapi.com/documentation/#filter-characters). En ajoutant un paramètre `status` à l'URL du point de terminaison, tout comme notre paramètre `name`, vous pouvez ajouter un nouveau filtre pour faciliter la recherche de personnages encore en vie ou non.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>