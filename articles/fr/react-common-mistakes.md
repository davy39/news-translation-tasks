---
title: Erreurs courantes à éviter avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-08-06T22:19:05.000Z'
originalURL: https://freecodecamp.org/news/react-common-mistakes
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/react-mistakes.png
tags:
- name: React
  slug: react
seo_title: Erreurs courantes à éviter avec React
seo_desc: 'By Scott Gary

  React is a highly popular and powerful JavaScript library for user interface development.
  Its component-based architecture, combined with its declarative nature, is one of
  the primary reasons it works well for both small and large-scale...'
---

Par Scott Gary

React est une bibliothèque JavaScript très populaire et puissante pour le développement d'interfaces utilisateur. Son architecture basée sur les composants, combinée à sa nature déclarative, est l'une des principales raisons pour lesquelles elle fonctionne bien pour les applications petites et grandes.

Mais comme avec toute technologie, il y a des pièges dans lesquels vous pouvez tomber lorsque vous écrivez du code React si vous n'êtes pas prudent.

Dans cet article, nous allons discuter de ces erreurs courantes et je vous fournirai les meilleures pratiques pour les éviter. Cela vous aidera à garder vos projets React efficaces, maintenables et évolutifs.

## 1. Erreurs dans l'utilisation des props Key

L'une des erreurs les plus courantes lors de l'utilisation de React concerne la prop key. Il existe plusieurs scénarios où les props key sont utilisées, les listes étant les plus courantes.

La prop key est cruciale car elle aide React à suivre les éléments qui ont changé, été ajoutés ou supprimés. Si elles ne sont pas correctement définies, l'algorithme de diffing de React peut devenir inefficace, entraînant des problèmes de performance et des bugs.

**Meilleure pratique :** Toujours passer une clé stable et unique pour les éléments d'une liste. Si possible, utilisez des identifiants uniques de vos données au lieu des indices de tableau comme clés.

```
const ItemList = ({ items }) => (
  <ul>
    {items.map(item => (
      <li key={item.id}>{item.name}</li>
    ))}
  </ul>
);

```

Dans l'extrait de code ci-dessus, chaque élément de la liste a une clé avec `item.id`. Cela garantit que chaque élément de la liste est identifiable de manière unique, aidant React à rendre plus efficacement et à réduire les rendus inutiles.

Pour plus de conseils sur l'optimisation des performances, consultez cet article sur [la mise en cache dans React](https://www.freecodecamp.org/news/caching-in-react/).

## 2. Ignorer le Virtual DOM

Certains développeurs pensent à tort que le rôle du Virtual DOM signifie qu'ils doivent mettre à jour le DOM eux-mêmes. Cela va à l'encontre du fonctionnement de React et peut entraîner des comportements imprévisibles et des bugs.

### Qu'est-ce que le Virtual DOM ?

Pour ceux qui découvrent React, le Virtual DOM est une représentation en mémoire du vrai DOM. Il permet à React de mettre à jour l'interface utilisateur efficacement en minimisant les manipulations directes du DOM réel. React compare le nouveau Virtual DOM avec le précédent et met à jour uniquement les parties nécessaires du vrai DOM.

Les développeurs peuvent supposer qu'ils doivent synchroniser le Virtual DOM avec le vrai DOM en raison de leurs expériences avec d'autres bibliothèques ou frameworks.

**Meilleure pratique :** Laissez toujours React gérer le DOM. Si vous devez interagir directement avec le DOM, utilisez des refs.

```
const ItemList = ({ items }) => (
  <ul>
    {items.map(item => (
      <li key={item.id}>{item.name}</li>
    ))}
  </ul>
);

```

**Explication :**

L'utilisation d'un identifiant unique provenant des données, tel que `item.id`, garantit que chaque clé est unique et stable. Cela permet à React de déterminer efficacement quels éléments ont changé, été ajoutés ou supprimés. Cela aide l'algorithme de réconciliation de React à mettre à jour l'interface utilisateur efficacement et empêche les bugs liés au réordonnancement ou à la suppression d'éléments.

## 3. Surutilisation de l'état

La gestion de l'état est cruciale dans React, mais une utilisation excessive de l'état peut rendre un composant complexe et difficile à maintenir. Tout changement d'état déclenche un nouveau rendu, ce qui peut être coûteux si ce n'est pas géré correctement.

**Meilleure pratique :** Minimisez l'utilisation de l'état et remontez l'état uniquement lorsque cela est nécessaire. Pour l'état global, utilisez des contextes ou des bibliothèques de gestion d'état comme Redux.

```
import React, { useState } from 'react';

const MyComponent = () => {
  const [count, setCount] = useState(0);
  const [name, setName] = useState(''); // État supplémentaire

  const handleIncrement = () => setCount(count + 1);
  const handleNameChange = (e) => setName(e.target.value);

  return (
    <div>
      <p>Compte : {count}</p>
      <button onClick={handleIncrement}>Incrémenter</button>
      <input
        type="text"
        value={name}
        onChange={handleNameChange}
        placeholder="Entrez le nom"
      />
    </div>
  );
};

```

Dans l'exemple ci-dessus, le hook `useState` est utilisé pour maintenir un état de compte simple. Lorsque le bouton est pressé, il affiche et incrémente le compte, démontrant une utilisation très basique de l'état.

## 4. Oublier de nettoyer les effets

Lorsque vous utilisez le hook useEffect, il est essentiel de nettoyer les effets secondaires pour éviter les fuites de mémoire et autres comportements indésirables. Les effets secondaires peuvent inclure la configuration d'abonnements, de minuteries ou d'écouteurs d'événements qui doivent être effacés lorsque le composant est démonté ou lorsque les dépendances de l'effet changent.

**Meilleure pratique :** Toujours retourner une fonction de nettoyage depuis votre effet lorsque vous configurez des effets secondaires qui doivent être effacés.

Exemple sans nettoyage :

```
const Timer = () => {
  const [time, setTime] = React.useState(0);

  React.useEffect(() => {
    const intervalId = setInterval(() => {
      setTime(prevTime => prevTime + 1);
    }, 1000);
    // Aucune fonction de nettoyage fournie ici
  }, []);

  return <div>Temps : {time}s</div>;
};

```

Dans l'exemple ci-dessus, une minuterie est configurée avec `setInterval`, mais aucune fonction de nettoyage n'est fournie pour effacer l'intervalle lorsque le composant est démonté. Cela peut entraîner des fuites de mémoire.

**Correct :** Nettoyage avec `useEffect` :

```
const Timer = () => {
  const [time, setTime] = React.useState(0);

  React.useEffect(() => {
    const intervalId = setInterval(() => {
      setTime(prevTime => prevTime + 1);
    }, 1000);

    // Fonction de nettoyage pour effacer l'intervalle
    return () => clearInterval(intervalId);
  }, []);

  return <div>Temps : {time}s</div>;
};

```

Dans cet exemple corrigé, une fonction de nettoyage est fournie pour effacer l'intervalle lorsque le composant est démonté, empêchant les fuites de mémoire potentielles.

## 5. Ignorer la performance

Une application React peut rencontrer de sérieux problèmes de performance, tels que des re-rendus excessifs et des calculs lourds pendant le rendu.

**Meilleure pratique :** Mémoïsez les composants et les valeurs en utilisant `React.memo`, `useMemo` et `useCallback` pour améliorer les performances.

```
const MemoizedComponent = React.memo(({ data }) => {
  return <div>{data}</div>;
});

```

Cet exemple utilise `React.memo` pour mémoïser un composant fonctionnel, l'empêchant de se re-rendre inutilement lorsque la prop `data` n'a pas changé.

## 6. Surutilisation de l'API Context

L'API Context est très pratique pour passer des données à travers votre arbre de composants sans prop drilling. Mais elle est souvent surutilisée, entraînant des problèmes de performance.

**Meilleure pratique :** Évitez d'utiliser le contexte pour des valeurs changeant fréquemment. Utilisez-le principalement pour des valeurs statiques ou des mises à jour rares.

```
const ThemeContext = React.createContext('light');

const ThemedComponent = () => {
  const theme = useContext(ThemeContext);
  return <div className={theme}>Composant thématique</div>;
};

```

Dans l'exemple ci-dessus, `ThemeContext` est initialisé avec la valeur par défaut `'light'`. Le `ThemedComponent` utilise le hook `useContext` pour obtenir la valeur réelle du thème.

## 7. Ne pas gérer les erreurs correctement

Une fonctionnalité importante de React est les limites d'erreur. Elles attrapent et gèrent les erreurs dans l'arbre de composants. Sans elles, les erreurs non gérées peuvent éventuellement faire planter toute l'application.

**Meilleure pratique :** Implémentez des limites d'erreur en utilisant `componentDidCatch` ou des composants `ErrorBoundary`.

```
const UserProfile = ({ userId }) => {
  const [user, setUser] = React.useState(null);
  const [error, setError] = React.useState(null);

  React.useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('La réponse du réseau n\'était pas correcte');
        }
        return response.json();
      })
      .then(data => setUser(data))
      .catch(err => setError(err.message));
  }, [userId]);

  if (error) {
    return <div>Erreur : {error}</div>;
  }

  if (!user) {
    return <div>Chargement...</div>;
  }

  return <div>{user.name}</div>;
};

```

En ajoutant la gestion des erreurs, nous attrapons tout problème avec la requête API et affichons un message d'erreur approprié.

Cette approche améliore la robustesse du composant, fournissant aux utilisateurs un retour en cas d'erreur et garantissant que l'application reste fonctionnelle même lorsque des problèmes inattendus surviennent.

## 8. Échec à garder les composants purs

Les composants React doivent toujours être des fonctions pures de leurs props. Les composants impurs dépendent d'états externes et d'effets secondaires, rendant le système imprévisible.

**Meilleure pratique :** Assurez-vous que vos composants sont purs et que leur sortie dépend entièrement de leurs props.

```
const MyComponent = ({ name }) => {
  return <div>{name}</div>;
};

```

Ce composant fonctionnel est pur car il ne dépend que de la prop `name` pour rendre sa sortie.

## 9. Ne pas utiliser les outils de développement React

Les outils de développement React sont une extension simple mais essentielle pour le débogage et l'optimisation des performances d'une application React. Le développement peut devenir plus compliqué si vous n'utilisez pas cet ensemble d'outils utile.

**Meilleure pratique :** Installez et utilisez régulièrement les outils de développement React pour inspecter les hiérarchies de composants, l'état et les props.

## 10. Ignorer les meilleures pratiques SEO

Le SEO est un aspect important de toute application web, et cela est également vrai pour les applications React. De nombreux développeurs négligent le SEO, ce qui conduit à un mauvais classement dans les moteurs de recherche et à une visibilité réduite.

Voici quelques-unes des erreurs SEO les plus courantes avec React :

%[https://www.youtube.com/watch?v=tIQv8oIn3g4]

Vous vous demandez comment implémenter les meilleures pratiques SEO pour React ? Bonne nouvelle, j'ai fait une vidéo de suivi :

%[https://www.youtube.com/watch?v=xAFzD1ckPXs&themeRefresh=1]

**Meilleures pratiques :** Si la vidéo n'est pas votre truc, voici les points clés à retenir :

* Toujours [rendre votre contenu côté serveur](https://www.freecodecamp.org/news/server-side-rendering-javascript/) : Google a publiquement déclaré éviter le rendu côté client (CSR).
* Assurez-vous d'avoir des URLs uniques pour différentes pages : Puisque React est une application monopage (SPA), assurez-vous toujours de rendre différentes URLs pour différentes pages. Par exemple, si vous avez 5 pages de destination, assurez-vous de rendre 5 URLs uniques.
* Assurez-vous d'avoir des métadonnées uniques pour chaque page : En bonus, utilisez [React Helmet](https://www.freecodecamp.org/news/react-helmet-examples/) pour vous assurer que chaque page a des métadonnées uniques.
* Liez interne votre site web : Étonnamment, de nombreux développeurs ignorent complètement cela. Assurez-vous d'ajouter des liens internes pour améliorer la navigation et le SEO.

## Conclusion

En conclusion, éviter ces erreurs courantes avec React peut grandement améliorer les performances et la maintenabilité de vos applications.

Si vous êtes intéressé à en apprendre davantage sur mon travail ou avez besoin d'aide avec le développement React ou Next.js, consultez [hirenext.dev](https://www.hirenext.dev/). Alternativement, vous pouvez suivre mon blog [OhMyCrawl](https://www.ohmycrawl.com/).