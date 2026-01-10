---
title: Quand utiliser la prop keyExtractor dans la FlatList de React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-29T18:05:02.000Z'
originalURL: https://freecodecamp.org/news/when-to-use-keyextractor-prop-in-react-natives-flatlist
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/cover_image.png
tags:
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: Quand utiliser la prop keyExtractor dans la FlatList de React Native
seo_desc: 'By Aman Mittal

  In React Native, you can use the FlatList component to render a long list of data.
  It renders only the items shown on the screen in a scrolling list and not all the
  data at once.

  To render a scrollable list of items using FlatList, you...'
---

Par Aman Mittal

Dans React Native, vous pouvez utiliser le composant [FlatList](https://reactnative.dev/docs/flatlist) pour afficher une longue liste de données. Il ne rend que les éléments affichés à l'écran dans une liste déroulante et non toutes les données d'un coup.

Pour afficher une liste d'éléments défilante à l'aide de `FlatList`, vous devez transmettre la prop obligatoire `data` au composant. La prop `data` accepte un tableau d'éléments. Chaque élément du tableau représente un seul élément de la liste.

Une autre prop obligatoire est `renderItem`, qui prend un élément de `data` et le rend dans la liste. Cette prop accepte une fonction qui renvoie le JSX à afficher.

Pour afficher un élément dans la liste défilante, le composant `FlatList` exige que chaque élément possède une clé unique telle qu'un `id`. C'est cette clé qui permet au composant `FlatList` (puisqu'il utilise [VirtualizedList](https://reactnative.dev/docs/virtualizedlist) sous le capot) de suivre l'ordre des éléments dans la liste.

La clé du tableau de données est extraite à l'aide de la prop `keyExtractor` sur le composant `FlatList`.

Dans cet article, nous allons voir quand vous pourriez avoir besoin d'utiliser `keyExtractor` et dans quels scénarios cela n'est pas nécessaire.

## Comment afficher une liste d'éléments avec FlatList

Considérez la structure de données suivante. Il y a dix éléments dans le tableau, et chaque élément possède deux propriétés, `id` et `title`. L' `id` est la clé unique de chaque élément.

```javascript
const DATA_WITH_ID = [
  {
    id: 1,
    title: 'quidem molestiae enim'
  },
  {
    id: 2,
    title: 'sunt qui excepturi placeat culpa'
  },
  {
    id: 3,
    title: 'omnis laborum odio'
  },
  {
    id: 4,
    title: 'non esse culpa molestiae omnis sed optio'
  },
  {
    id: 5,
    title: 'eaque aut omnis a'
  },
  {
    id: 6,
    title: 'natus impedit quibusdam illo est'
  },
  {
    id: 7,
    title: 'quibusdam autem aliquid et et quia'
  },
  {
    id: 8,
    title: 'qui fuga est a eum'
  },
  {
    id: 9,
    title: 'saepe unde necessitatibus rem'
  },
  {
    id: 10,
    title: 'distinctio laborum qui'
  }
];
```

En utilisant le composant `FlatList`, vous souhaitez afficher le `title` de chaque élément comme indiqué ci-dessous :

```javascript
export default function App() {
  const renderList = ({ item }) => {
    return (
      <View style={styles.listItem}>
        <Text style={styles.listItemText}>{item.title}</Text>
      </View>
    );
  };

  return (
    <View style={styles.container}>
      <FlatList data={DATA_WITH_ID} renderItem={renderList} />
    </View>
  );
}
```

Le résultat du composant ci-dessus affichera une liste d'éléments sans aucune erreur ni avertissement. De plus, le composant `FlatList` ne nécessite pas de clé unique pour identifier chaque élément puisque la structure de données originale contient déjà une clé nommée `id`.

Voici le rendu sur l'écran d'un appareil à partir de l'extrait ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/ss2.png)

## Comment utiliser la prop keyExtractor

Par défaut, la prop `keyExtractor` vérifie les propriétés telles que `key` et `id` (dans cet ordre). Si l'une des deux est présente dans la structure de données d'origine, elle sera considérée comme une clé unique par le composant `FlatList`.

Dans ce cas (comme dans l'exemple précédent), vous n'avez pas besoin d'utiliser explicitement la prop `keyExtractor`.

Si aucune d'elles n'est fournie, le composant `FlatList` affichera un avertissement "VirtualizedList: missing keys for items ..." :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/ss1-1.png)

Considérons maintenant un scénario dans lequel un tableau de données contient une clé unique pour chaque élément de la liste, mais le nom de la clé unique n'est ni `key` ni `id`. Il contient une propriété de clé unique nommée `userId`.

```javascript
const DATA_WITH_USER_ID = [
  {
    userId: 1,
    title: 'quidem molestiae enim'
  },
  {
    userId: 2,
    title: 'sunt qui excepturi placeat culpa'
  },
  {
    userId: 3,
    title: 'omnis laborum odio'
  },
  {
    userId: 4,
    title: 'non esse culpa molestiae omnis sed optio'
  },
  {
    userId: 5,
    title: 'eaque aut omnis a'
  },
  {
    userId: 6,
    title: 'natus impedit quibusdam illo est'
  },
  {
    userId: 7,
    title: 'quibusdam autem aliquid et et quia'
  },
  {
    userId: 8,
    title: 'qui fuga est a eum'
  },
  {
    userId: 9,
    title: 'saepe unde necessitatibus rem'
  },
  {
    userId: 10,
    title: 'distinctio laborum qui'
  }
];
```

Lors du rendu de la liste, vous verrez l'avertissement dans ce cas car le composant `FlatList` ne reconnaît pas `userId` comme étant le nom `key` ou `id` dans la structure de données d'origine.

Pour les noms de clés personnalisés tels que `userId` dans l'exemple ci-dessus, vous utiliserez la prop `keyExtractor`. Elle extrait le nom de la clé unique et sa valeur, et indique au composant `FlatList` de suivre les éléments en fonction de cette valeur.

Pour le tableau de données ci-dessus, modifiez le composant `FlatList` et utilisez la prop `keyExtractor` pour extraire la clé :

```javascript
<FlatList
  data={DATA_WITH_ID}
  renderItem={renderList}
  keyExtractor={item => item.userId}
/>
```

L'avertissement disparaîtra alors après cette étape.

## Conclusion

Lors de l'utilisation d'un composant `FlatList`, si le tableau de données possède une propriété unique `id` ou `key`, vous n'avez pas besoin d'utiliser explicitement la prop `keyExtractor`. Mais pour les noms d'identifiants personnalisés, utilisez la prop `keyExtractor` pour indiquer explicitement au composant quelle clé unique extraire.

Si vous souhaitez en savoir plus sur React Native, consultez les pages des catégories [React Native](https://amanhimself.dev/tags/react-native/) et [Expo](https://amanhimself.dev/tags/expo/) sur mon blog. Vous pouvez également vous abonner à ma [newsletter](https://www.getrevue.co/profile/amanhimself) ou me suivre sur [Twitter](https://twitter.com/amanhimself) pour obtenir des mises à jour chaque fois que je publie un nouvel article ou tutoriel.