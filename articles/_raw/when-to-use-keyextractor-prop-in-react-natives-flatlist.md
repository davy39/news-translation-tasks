---
title: When to Use the keyExtractor Prop in React Native's FlatList
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
seo_title: null
seo_desc: 'By Aman Mittal

  In React Native, you can use the FlatList component to render a long list of data.
  It renders only the items shown on the screen in a scrolling list and not all the
  data at once.

  To render a scrollable list of items using FlatList, you...'
---

By Aman Mittal

In React Native, you can use the [FlatList component](https://reactnative.dev/docs/flatlist) to render a long list of data. It renders only the items shown on the screen in a scrolling list and not all the data at once.

To render a scrollable list of items using `FlatList`, you need to pass the required `data` prop to the component. The `data` prop accepts an array of items. Each item in the array represents a single item in the list. 

Another required prop is `renderItem`, which takes an item from the `data` and renders it on the list. This prop accepts a function that returns the JSX to be rendered.

To display an item in the scrollable list, the `FlatList` component requires that each item has a unique key such as an `id`. This key is what allows the `FlatList` component (since it uses [VirtualizedList](https://reactnative.dev/docs/virtualizedlist) under the hood) to track the order of items in the list. 

The key from the data array is extracted using the `keyExtractor` prop on the `FlatList` component.

In this post, let's talk about where you might need to use `keyExtractor` and in what scenarios it's not required.

## How to Display a List of Items Using FlatList

Consider the following structure of data. There are ten items in the array, and each item has two properties, `id` and `title`. The `id` is the unique key for each item.

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

Using the `FlatList` component, you want to render the `title` of each item as shown below:

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

The result of the above component will display a list of items without any errors or warnings. In addition, the `FlatList` component doesn't require a unique key to identify each item since the original data structure already contains a key called `id`.

Here is the output on a device's screen from the above snippet:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/ss2.png)

## How to Use the keyExtractor Prop

By default, the `keyExtractor` prop checks for properties like `key` and `id` (in that order). If either of the two is present in the original data structure, it will be considered a unique key by the `FlatList` component. 

In this case (as in the previous example), you do not have to explicitly use the `keyExtractor` prop.

If neither of them are provided, the `FlatList` component will throw a warning "VirtualizedList: missing keys for items ...":

![Image](https://www.freecodecamp.org/news/content/images/2022/03/ss1-1.png)

Now, let's consider a scenario where an array of data contains a unique key with each list item but the name of the unique key is neither `key` nor `id`. It contains a unique key property with the name of `userId`.

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

When rendering the list, you will see the warning in this case because the `FlatList` component doesn't recognize the `userId` as the `key` or `id` name in the original data structure.

For custom key names such as `userId` in the example above, you'll use the `keyExtractor` prop. It extracts the unique key name and its value and tells the `FlatList` component to track the items based on that value.

For the above array of data, modify the `FlatList` component and use the `keyExtractor` prop to extract the key:

```javascript
<FlatList
  data={DATA_WITH_ID}
  renderItem={renderList}
  keyExtractor={item => item.userId}
/>
```

The warning will then disappear after this step.

## Conclusion

When using a `FlatList` component, if the data array has a unique `id` or a `key` property, you do not need to use the `keyExtractor` prop explicitly. But for custom id names, use the `keyExtractor` prop to explicitly tell the component which unique key to extract.

If you'd like to learn more about React Native, check out the [React Native category](https://amanhimself.dev/tags/react-native/) and [Expo category](https://amanhimself.dev/tags/expo/) pages on my blog. You can also subscribe my [newsletter](https://www.getrevue.co/profile/amanhimself) or follow me on [Twitter](https://twitter.com/amanhimself) to get updates on whenever I publish a new article or tutorial.

