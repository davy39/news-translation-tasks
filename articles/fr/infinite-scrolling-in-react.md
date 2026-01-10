---
title: Comment créer un défilement infini dans React en utilisant l'API Intersection
  Observer
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-07-01T09:24:18.000Z'
originalURL: https://freecodecamp.org/news/infinite-scrolling-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/photo-1563986768494-4dee2763ff3f.jpeg
tags:
- name: React
  slug: react
seo_title: Comment créer un défilement infini dans React en utilisant l'API Intersection
  Observer
seo_desc: 'Hi fellow developers! Have you ever wondered how social media apps like
  Facebook and Instagram keep you scrolling endlessly through your feed?

  This user experience, designed to load new content on demand, uses a technique called
  infinite scrolling. T...'
---

Bonjour à tous les développeurs ! Vous êtes-vous déjà demandé comment les applications de réseaux sociaux comme Facebook et Instagram vous font défiler sans fin votre fil d'actualité ?

Cette expérience utilisateur, conçue pour charger du nouveau contenu à la demande, utilise une technique appelée défilement infini. Cela aide à vous maintenir accroché à ces applications pendant des heures.

Traditionnellement, ces fonctionnalités vous feraient cliquer sur "Page suivante" pour afficher du nouveau contenu. Cependant, le défilement infini réduit la charge sur le serveur en récupérant moins de données à la fois et offre ainsi une expérience utilisateur beaucoup plus engageante.

Dans cet article, nous allons implémenter la même fonctionnalité en JavaScript. Nous utiliserons l'API Intersection Observer pour charger des données à la demande, au fur et à mesure que l'utilisateur fait défiler. Nous créerons une application React simple qui affiche des posts similaires à un fil d'actualité de réseau social.

## Comment configurer l'application React

Exécutez `create-react-app` dans votre terminal ou utilisez un [outil de construction moderne comme Vite](https://www.freecodecamp.org/news/get-started-with-vite/) pour créer votre application React. Supprimez le code boilerplate existant. Il n'est pas nécessaire d'installer des dépendances supplémentaires. Exécutez la commande `npm start` pour démarrer le projet.

Vous pouvez trouver le code complet de ce tutoriel sur [GitHub](https://github.com/KunalN25/my-tutorials/tree/main/javascript-and-react/infinite-scroll-js). Commençons.

## Comment créer la fonction de récupération de données

Créez un fichier séparé appelé `services.js` et écrivez la fonction de récupération de données suivante.

Nous utiliserons l'API `/posts` de [JSONPlaceholder](https://jsonplaceholder.typicode.com) pour obtenir nos données.

```js
export const fetchPosts = async (page, limit) => {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/posts?_page=${page}&_limit=${limit}`
  );
  const data = await response.json();
  return data;
};
```

Ici, nous avons passé deux paramètres à l'API :

* `page` indique la partie des données qui est appelée. Cela augmente chaque fois que l'utilisateur fait défiler et charge de nouvelles données.

* `limit` indique la quantité de données qui est appelée à la fois. Pour le défilement infini, nous appelons juste assez de données pour pouvoir être affichées sur une seule page.

## Comment construire le composant de défilement infini

Créons un composant `PostsList` pour afficher une liste de posts avec défilement infini.

Créons nos variables d'état, récupérons les données et affichons-les :

```js
const PostsList = () => {
  const [posts, setPosts] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);

  return (
    <div>
      <h1>Votre Fil</h1>
      <ul>
        {posts.map((post, index) => (
          <li
            key={post.id}
          >
            <h2>{post.title}</h2>
            <p>{post.body}</p>
          </li>
        ))}
      </ul>
      {loading && <p>Chargement...</p>}

    </div>
  );
};
```

Ici, nous avons défini les variables d'état pour les posts, le numéro de page et l'état de chargement. Notez que le numéro de page ne signifie pas que nous ajoutons une pagination. Ce n'est qu'un paramètre pour charger le prochain ensemble de données.

Maintenant, appelons notre API avec le numéro de page actuel et définissons les états de chargement :

```js
const loadMorePosts = async () => {
    setLoading(true);
    const newPosts = await fetchPosts(page, 10);
    setPosts((prevPosts) => [...prevPosts, ...newPosts]);
    setLoading(false);
  };

  useEffect(() => {
    loadMorePosts();
  }, [page]);
```

Jusqu'à présent, nous avons récupéré les 10 premiers posts au premier chargement de la page. Nous voulons charger plus de données au fur et à mesure que l'utilisateur fait défiler vers le bas de la page.

Ensuite, nous utiliserons l'API Intersection Observer pour détecter quand des données supplémentaires doivent être chargées.

Avant de l'utiliser, comprenons d'abord ce qu'est cette API.

## Qu'est-ce que l'API Intersection Observer ?

L'API Intersection Observer est une API web qui vous permet d'observer de manière asynchrone les changements dans l'intersection d'un élément cible avec un élément ancêtre ou la fenêtre d'affichage.

En termes plus simples, elle vous permet de détecter quand un élément entre ou sort d'une zone d'un autre élément DOM ou de la fenêtre d'affichage. L'utilisation de l'Intersection Observer nous offre les avantages suivants :

* Réduit le besoin d'attacher des écouteurs d'événements à chaque événement de défilement.

* Supprime le besoin de calculs manuels de la position de l'élément et de leurs écouteurs d'événements, simplifiant ainsi votre code.

* Efficace pour observer plusieurs événements par rapport aux écouteurs d'événements de défilement ou de redimensionnement.

Consultez la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) pour en savoir plus sur l'Intersection Observer.

## Comment utiliser l'API Intersection Observer

Pour utiliser cette API, nous devons créer un objet observateur.

Voici comment créer un objet observateur :

```python
const observer = new IntersectionObserver(callback, options);
```

* `callback` est une fonction appelée lorsque la visibilité de l'élément observé change. Cette fonction prend deux arguments : `entries` et l'objet `observer` lui-même. Chaque objet dans le tableau `entries` est un objet `IntersectionObserverEntry` qui contient des informations sur l'état d'intersection de l'élément observé.

* `options` est un argument optionnel pour configurer davantage l'Observer.

Comment utilisons-nous cela dans notre application ? Nous définirons l'objet observateur comme une ref :

```js
  const observer = useRef();
```

Maintenant, pour définir cet objet observateur sur un élément et pour détecter si cet élément intersecte avec la fenêtre d'affichage, nous utilisons la fonction suivante, qui est une ref de rappel :

```python
const lastPostElementRef = useCallback(
    (node) => {
      if (loading) return;
      if (observer.current) observer.current.disconnect();

      observer.current = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          setPage((prevPage) => prevPage + 1); // déclencher le chargement de nouveaux posts en changeant le numéro de page
        }
      });

      if (node) observer.current.observe(node);
    },
    [loading]
  );
```

Comprenons comment cette fonction fonctionne :

* Nous vérifions si les données sont encore en cours de chargement. Si c'est le cas, nous n'exécutons pas la logique.

* Pour faire référence à l'objet `observer`, nous utilisons la propriété `current` de la ref.

* Si un élément est déjà observé, alors nous le déconnectons et créons un nouvel Observer qui change le numéro de page, déclenchant ainsi l'appel API si l'élément observé intersecte avec la fenêtre d'affichage.

* Puisque nous n'observons qu'un seul élément à la fois (comme le dernier élément de la page), la taille de `entries` est de un.

* Ce nouvel Observer va maintenant surveiller l'élément actuel auquel la ref est attachée, qui est le dernier élément de la page.

Puisque nous voulons seulement observer le dernier élément de la page, nous ajoutons cette ref selon la condition suivante :

```python
{posts.map((post, index) => (
          <li
            key={post.id}
            ref={posts.length === index + 1 ? lastPostElementRef : null}
          >
            ...
          </li>
        ))}
```

Maintenant, pourquoi utilisons-nous des refs de rappel au lieu de la ref `observer` elle-même ?

Une ref nous donne une référence directe à l'élément et définit la valeur de l'objet ref directement. Cela fonctionne bien pour les éléments qui n'ont pas besoin de changer de référence dynamiquement.

Une ref de rappel offre plus de contrôle sur la ref et peut gérer les changements dynamiques de référence plus efficacement. C'est une fonction appelée avec l'instance de l'élément, ou son nœud DOM lorsque le composant est monté et avec null s'il est démonté.

Dans notre cas, notre référence change dynamiquement puisque notre dernier élément est mis à jour lorsque plus de données sont chargées. Nous sommes également en mesure d'écrire une logique pour observer et nous déconnecter d'un nœud, tout en définissant notre objet ref.

Nous envelopperons également la fonction `lastPostElementRef` dans un hook `useCallback` pour éviter qu'elle ne soit recréée à chaque ré-rendu. Nous ne créerons cette fonction que si l'état de chargement change lorsqu'il est temps d'exécuter la fonction.

Exécutez votre application avec `npm start`, allez sur `http://localhost:3000`, et ouvrez l'onglet Réseau. Au fur et à mesure que vous faites défiler vers le bas, vous verrez de nouvelles requêtes API être effectuées.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-101.png align="left")

*Requêtes API pour chaque nouvelle page*

Vous pouvez trouver le code complet sur [GitHub](https://github.com/KunalN25/my-tutorials/tree/main/javascript-and-react/infinite-scroll-js) et des tutoriels similaires en JavaScript et React.

## Conclusion

Lorsque vous implémentez le défilement infini dans votre application, cela offre une expérience utilisateur fluide et engageante similaire à ce que vous voyez sur les applications de réseaux sociaux populaires. Au lieu de cliquer à travers les pages, les utilisateurs peuvent faire défiler sans effort le contenu qui se charge dynamiquement.

Dans notre exemple, nous avons créé un fil d'actualité de réseau social fictif qui charge plus de contenu au fur et à mesure que l'utilisateur fait défiler vers le bas. Nous avons utilisé l'API Intersection Observer pour détecter la position du dernier élément en fonction de laquelle nous avons chargé plus de données. Cela a simplifié notre code et supprimé le besoin d'attacher plusieurs écouteurs d'événements.

J'espère que cela vous aidera à créer des fonctionnalités similaires dans votre prochain projet web et vous permettra de fournir une expérience utilisateur engageante. N'hésitez pas à partager vos pensées et retours. Merci !