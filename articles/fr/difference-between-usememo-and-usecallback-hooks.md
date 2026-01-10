---
title: Quelle est la différence entre les hooks useMemo et useCallback ?
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-07-15T19:14:59.000Z'
originalURL: https://freecodecamp.org/news/difference-between-usememo-and-usecallback-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/photo-1619410283995-43d9134e7656.jpeg
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Quelle est la différence entre les hooks useMemo et useCallback ?
seo_desc: React provides various hooks that make it easier to manage application state
  and other React features in functional components. Hooks provide class component
  features to functional components, and they don't need a lot of code compared to
  class compo...
---

React fournit divers hooks qui facilitent la gestion de l'état de l'application et d'autres fonctionnalités React dans les composants fonctionnels. Les hooks fournissent des fonctionnalités de composant de classe aux composants fonctionnels, et ils ne nécessitent pas beaucoup de code par rapport aux composants de classe.

Les hooks facilitent également votre vie en fournissant certaines fonctionnalités pratiques. Parmi ces hooks, nous avons `useMemo` et `useCallback` qui aident à améliorer les performances de votre site web.

Dans le tutoriel d'aujourd'hui, nous allons discuter des hooks `useMemo` et `useCallback`. Vous apprendrez la différence entre eux et quand utiliser chaque hook.

## Le hook `useMemo`

Le hook `useMemo` *mémoïse* la valeur de retour d'un calcul coûteux entre les rendus. La mémoïsation signifie stocker la valeur comme une valeur mise en cache afin que la valeur n'ait pas besoin d'être recalculée (sauf si nécessaire).

`useMemo` est un hook utilisé pour optimiser les performances de vos rendus. Normalement, lorsque vous déclarez une variable à l'intérieur d'un composant, elle est recréée à chaque rendu. Si elle stocke la valeur de retour d'une fonction, alors la fonction est appelée chaque fois que votre composant est rendu.

Normalement, cela ne poserait pas de problème. Mais, que se passe-t-il si la fonction est coûteuse ? Que se passe-t-il si elle prend plus de temps à s'exécuter ? Prenons l'exemple suivant :

```js
function calculate() {
  let result = 0;
  for (let i = 0; i < 1000000000; i++) {
    result += i;
  }
  return result;
}

function App1() {
  const [count, setCount] = useState(0);

  const value = calculate();

  return (
    <div className="App">
      <button onClick={() => setCount(count + 1)}>Incrémenter le compte</button>
      <p>Compte : {count}</p>
    </div>
  );
}
```

Lorsque vous cliquez sur 'Incrémenter le compte', cela prend quelques secondes pour mettre à jour l'état du compte. Cela est dû au fait que la fonction `calculate` s'exécute chaque fois qu'un composant est réaffiché après un changement d'état.

Maintenant, imaginez s'il y avait plusieurs variables d'état dans le composant, chacune servant son propre but. Chaque mise à jour d'état provoquerait un nouveau rendu et exécuterait cette fonction coûteuse.

Ces variables d'état pourraient être complètement indépendantes du calcul coûteux effectué, ce qui provoquerait des retards inutiles. Cela affecterait les performances de votre site web et pourrait conduire à une mauvaise expérience utilisateur.

`useMemo` peut vous aider à résoudre ce problème. Commençons par comprendre sa syntaxe :

```python
const value = useMemo(expensiveFunction, [...dependencyArray])
```

Le hook `useMemo` doit être déclaré au niveau supérieur de votre composant. Il prend les arguments suivants :

* `expensiveFunction` contient le calcul coûteux que vous souhaitez effectuer. Si vous avez déclaré la fonction à l'extérieur, passez uniquement la référence de la fonction, sans les parenthèses. Vous pouvez également passer des fonctions fléchées directement.
    
* `dependencyArray` contient la liste des dépendances pour le hook. La fonction coûteuse ne sera appelée que lorsqu'une de ces dépendances est mise à jour. Vous pouvez passer des variables d'état ou des props qui dépendent de ce calcul. Toute autre mise à jour d'état ne déclenchera pas la fonction.
    

Lors du premier rendu, `useMemo` retourne le résultat de `expensiveFunction` et met en cache le résultat. Lors des rendus suivants, il retournera la valeur mise en cache si aucune dépendance n'a changé. Si elles changent, alors il appellera à nouveau la fonction.

Utilisons cela dans notre cas :

```js
const [dependentCount, setDependentCount] = useState(10);

const value = useMemo(calculate, [dependentCount]);

return (
  <div className="App">
    
    // ...

    <button onClick={() => setDependentCount(dependentCount + 1)}>
      Incrémenter le compte dépendant
    </button>
    <p>Compte dépendant : {dependentCount}</p>
  </div>
);
```

Nous avons créé un autre état `dependentCount` que nous supposons dépendant du calcul coûteux. Lorsque cet état est mis à jour et rend le composant, la fonction `calculate` s'exécutera.

Mais si un autre état change, alors `useMemo` retournera la valeur mise en cache au lieu d'exécuter à nouveau la fonction.

Testons cela en ajoutant un `console.log` à l'intérieur de la fonction :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-28.png align="left")

*Sortie avec useMemo*

Maintenant, lorsque vous cliquez sur "Incrémenter le compte", le rendu est plus rapide, car la fonction `calculate` n'est pas appelée à chaque rendu. Il en va de même pour chaque autre mise à jour d'état non listée dans le tableau de dépendances de useMemo.

Mais lorsque vous cliquez sur "Incrémenter le compte dépendant", cela prend du temps pour rendre la valeur mise à jour. Cela est dû au fait que `dependentCount` est une dépendance de `useMemo` et que sa modification appelle la fonction coûteuse, donc le composant prend du temps à se réafficher.

De cette manière, avec `useMemo`, vous pouvez contrôler l'exécution d'une fonction coûteuse en l'appelant uniquement pour les mises à jour d'état qui ont réellement besoin de la valeur retournée. Cela peut considérablement améliorer les performances de votre application.

### Quand utiliser `useMemo` :

* Lorsque vous avez un état dépendant d'un calcul coûteux, mais que vous ne souhaitez pas exécuter le calcul à chaque rendu.
    
* Lorsque vous déclarez un tableau ou un objet à l'intérieur d'un composant, sa référence change à chaque rendu, même si la valeur reste la même. En enveloppant les valeurs à l'intérieur de `useMemo`, vous maintenez l'égalité référentielle et évitez les rendus inutiles. Cela est essentiel lorsqu'il y a un `useEffect` dépendant du tableau ou de l'objet.
    
* Lorsque vous rendez des listes en utilisant `Array.map` qui n'ont pas besoin de changer sauf si une certaine valeur d'état change.
    

## Le hook `useCallback`

Similaire à `useMemo`, vous pouvez également utiliser ce hook pour optimiser les performances. Le hook `useCallback` mémoïse une fonction de rappel et la retourne.

Notez que le hook `useCallback` mémoïse la fonction elle-même, et non sa valeur de retour. `useMemo` met en cache la valeur de retour des fonctions afin que la fonction n'ait pas besoin de s'exécuter à nouveau. `useCallback` met en cache la définition de la fonction ou la référence de la fonction.

Une fonction déclarée à l'intérieur d'un composant est recréée à chaque rendu du composant, similaire à une variable. La différence est qu'elle est rendue avec une référence différente à chaque fois. Ainsi, un `useEffect` dépendant de cette fonction s'exécutera à nouveau à chaque rendu. Une chose similaire se produit avec les composants enfants.

Prenons un exemple :

```python
const App = () => {
  const [count, setCount] = useState(0);
  const [value, setValue] = useState("");

  const handleClick = () => {
    setValue("Kunal");
  };
  return (
    <div className="App">
      <button onClick={() => setCount(count + 1)}>Incrémenter le compte</button>
      <p>Compte : {count}</p>
      <p>Valeur : {value}</p>
      <SlowComponent handleClick={handleClick} />
    </div>
  );
};

const SlowComponent = React.memo(({ handleClick, value }) => {
  
  // Intentionnellement rendre le composant lent
  for (let i = 0; i < 1000000000; i++) {}

  return (
    <div>
      <h1>Composant lent</h1>
      <button onClick={handleClick}>Cliquez-moi</button>
      
    </div>
  );
});
```

Ici, nous avons un `SlowComponent` comme enfant du composant `App`. Lorsque le composant parent est rendu, tous ses composants enfants sont rendus, indépendamment du fait que quelque chose ait changé à l'intérieur.

Pour éviter les rendus inutiles des composants enfants, nous utilisons généralement la fonction `React.memo`. Cela met essentiellement en cache le composant et ne le réaffiche que si ses props ont changé.

Maintenant, lorsque vous cliquez sur 'Incrémenter le compte', cela prend toujours beaucoup de temps pour rendre, car `SlowComponent` est réaffiché lors du changement d'état. Mais pourquoi ? Nous ne changeons aucune de ses props.

En surface, nous ne semblons pas changer la valeur de la prop `handleClick`. Mais, puisque les fonctions sont recréées avec une référence différente, à chaque rendu du composant App, son enfant (c'est-à-dire `SlowComponent`) est rendu.

Pour maintenir l'égalité référentielle, nous enveloppons la définition de cette fonction à l'intérieur d'un `useCallback`.

Comprenons sa syntaxe :

```python
const cachedFn = useCallback(fn, [...dependencyArray])
```

`useCallback` prend les arguments suivants :

* `fn` est la fonction que vous souhaitez mettre en cache. C'est la définition de la fonction que vous souhaitez créer, et elle peut prendre n'importe quels arguments et retourner n'importe quelle valeur.
    
* `dependencyArray` est une liste de dépendances, dont les changements déclenchent la recréation de la fonction. Vous pouvez passer des valeurs d'état ou des props qui dépendent de cette fonction.
    

Lors du premier rendu, React crée la fonction (ne l'appelle pas) et la met en cache. Lors des rendus suivants, la fonction mise en cache vous est retournée. N'oubliez pas que ce hook retourne et met en cache la *fonction* et non sa valeur de retour.

Utilisons ce hook dans notre exemple :

```python
import { useCallback } from "react";

const App = () => {
  
  // ...

  const handleClick = useCallback(() => {
    setValue("Kunal");
  }, [value, setValue]);
  
  // ...
};
```

Ici, nous avons enveloppé la fonction à l'intérieur d'un `useCallback` et passé deux dépendances qui sont impliquées avec cette fonction.

Maintenant, lorsque vous cliquez sur 'Incrémenter le compte', le rendu est beaucoup plus rapide. Cela est dû au fait que la référence `handleClick` est mise en cache entre les rendus et donc, `SlowComponent` ne se réaffiche pas.

Mais lorsque vous cliquez sur le bouton à l'intérieur de `SlowComponent`, il se réaffichera. Cela est dû au fait que lorsque l'état `value` change, la méthode `handleClick` est créée à nouveau et donc les props du composant lent ont changé.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-33.png align="left")

*La valeur prend du temps à s'afficher*

Vous pouvez ajouter beaucoup plus d'états au composant `App` et les mettre à jour sans nuire aux performances tant que vous ne mettez pas à jour l'état de `value`.

### Quand utiliser `useCallback`

* Lorsque vous avez des gestionnaires d'événements définis pour un élément à l'intérieur de votre composant, enveloppez-les à l'intérieur d'un `useCallback` pour éviter les recréations inutiles de gestionnaires d'événements.
    
* Lorsque vous appelez une fonction à l'intérieur d'un `useEffect`, vous passez généralement la fonction comme une dépendance. Pour éviter d'utiliser `useEffect` inutilement à chaque rendu, enveloppez la définition de la fonction à l'intérieur d'un `useCallback`.
    
* Si vous écrivez un hook personnalisé, et qu'il retourne une fonction, il est recommandé de l'envelopper à l'intérieur d'un `useCallback`. Ainsi, les utilisateurs n'ont pas besoin de se soucier de l'optimisation du hook – plutôt, ils peuvent se concentrer sur leur propre code.
    

## Différences entre `useMemo` et `useCallback`

Récapitulons les différences entre les deux hooks :

* `useMemo` met en cache la valeur de retour d'une fonction. `useCallback` met en cache la définition de la fonction elle-même.
    
* `useMemo` est utilisé lorsque vous avez un calcul coûteux que vous souhaitez éviter à chaque rendu.
    
* `useCallback` est utilisé pour mettre en cache une fonction afin d'éviter de la recréer à chaque nouveau rendu.
    
* `useMemo` s'assure qu'une fonction coûteuse ne doit être appelée que pour les valeurs d'état dépendantes.
    
* `useCallback` crée des fonctions stables qui maintiennent la même référence entre les rendus. Cela évite le rendu inutile des composants enfants.
    

Et voici quelques autres choses à retenir. Utilisez ces hooks uniquement si vous souhaitez mémoïser des calculs coûteux ou prévenir des rendus inutiles. N'utilisez pas `useMemo` et `useCallback` partout.

Pour les fonctions régulières, ces hooks ne font pas une grande différence. Les surutiliser rendra votre code illisible. Au lieu de cela, vous pouvez trouver d'autres moyens d'améliorer les performances de l'application.

## Conclusion

`useMemo` et `useCallback` sont des hooks utiles dans React qui peuvent vous aider à optimiser les performances de votre application web. Il est important de comprendre la différence entre les deux et leurs usages.

Dans cet article, nous avons discuté du fonctionnement des deux hooks. `useMemo` met en cache le résultat d'un calcul coûteux, tandis que `useCallback` met en cache la référence de la fonction. Nous avons également listé des scénarios où vous devriez utiliser chaque hook. Ensemble, ces deux hooks peuvent rendre votre site web plus rapide.

J'espère que cet article aide à clarifier toute confusion. Si vous avez d'autres questions ou commentaires concernant l'article, contactez-moi sur Twitter. J'adorerais recevoir des suggestions. Jusqu'à la prochaine fois, au revoir !