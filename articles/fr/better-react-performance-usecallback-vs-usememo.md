---
title: Meilleures performances React – Quand utiliser les hooks useCallback et useMemo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-05T18:47:25.000Z'
originalURL: https://freecodecamp.org/news/better-react-performance-usecallback-vs-usememo
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/useCallback-vs-useMemo.png
tags:
- name: performance
  slug: performance
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: web performance
  slug: web-performance
seo_title: Meilleures performances React – Quand utiliser les hooks useCallback et
  useMemo
seo_desc: "By Daniel Asta\nWe all want to build powerful applications and avoid unnecessary\
  \ renders. There are some hooks available to help with this, but you might not be\
  \ sure about which one to use and when. \nIn this article you will learn the differences\
  \ betw..."
---

Par Daniel Asta

Nous voulons tous construire des applications puissantes et éviter les rendus inutiles. Il existe certains hooks disponibles pour aider à cela, mais vous ne savez peut-être pas lequel utiliser et quand.

Dans cet article, vous apprendrez les différences entre `useCallback` et `useMemo` ainsi que la manière de mesurer le gain des améliorations que vous obtenez dans la base de code.

Avant de commencer, vous devez noter que les méthodes suivantes pour optimiser React sont vraiment des options de dernier recours. Avant d'appliquer ces utilitaires, votre propre code vous offrira plus d'opportunités d'amélioration que la plupart des gains de performance que vous obtiendrez en utilisant ce que vous allez apprendre ici.

Néanmoins, il est important de connaître ces outils et de savoir quand les utiliser si vous voyez l'opportunité.

## Ressources dont vous aurez besoin pour suivre

- Documentation officielle bêta pour [useCallback](https://beta.reactjs.org/apis/react/useCallback) et [useMemo](https://beta.reactjs.org/apis/react/useMemo)
- [Code source du projet d'exemple](https://github.com/dastasoft/optimizing-react)
- [Démonstration en direct du projet d'exemple](https://react-optimisation.dastasoft.com/)

Comme toujours, j'ai fourni un projet d'exemple afin que vous puissiez tester dans un environnement simplifié tout ce qui est expliqué ici. Pas de quoi fouetter un chat, le projet d'exemple est juste un résumé des principaux points que vous allez apprendre maintenant.

Avant de commencer à comparer ces deux hooks, passons en revue quelques concepts de base nécessaires.

## Qu'est-ce que l'égalité référentielle ?

Lorsque React compare les valeurs utilisées dans un tableau de dépendances tel que `useEffect`, `useCallback`, ou les props passées à un composant enfant, il utilise `Object.is()`.

Vous pouvez trouver l'explication détaillée de [Object.is ici](http://Object.is) mais en résumé :

- Les valeurs primitives sont égales (consultez le lien ci-dessus pour les quelques exceptions).
- Les valeurs non primitives font référence au même objet en mémoire.

Dans un exemple simplifié :

```ts
"string" === "string" // true
0 === 0 // true
true === true // true
{} === {} // false
[] === [] // false

const f = () => 'Hi'
const f1 = f
const f2 = f

f1 === f1 // true
f1 === f2 // false
```

## Comment fonctionne React.memo

Je vais brièvement expliquer comment fonctionne `React.memo` (mais nous en discuterons également plus tard dans l'article). Lorsque cela est approprié, vous pouvez l'utiliser pour améliorer les performances.

Lorsque vous souhaitez éviter les re-rendus inutiles sur un composant enfant (même si le composant parent change), vous pouvez envelopper le composant entier avec `React.memo` – tant que les props ne changent pas. De plus, **notez l'égalité référentielle ici** – le composant enfant ne sera pas re-rendu.

```ts
import { memo } from 'react';

const ChildComponent = (props) => {
  // ...
}

export default memo(ChildComponent)
```

Maintenant que vous savez comment fonctionne `React.memo`, commençons.

## Comment fonctionne le hook useCallback

`useCallback` est l'un des hooks intégrés que nous pouvons utiliser pour optimiser notre code. Mais comme vous le verrez, ce n'est pas vraiment un hook pour des raisons de performance directe.

En bref, `useCallback` vous permettra de sauvegarder la *définition de la fonction* entre les rendus du composant.

```ts
import { useCallback } from "react"

const params = useCallback(() => {
		// ...
    return breed
  }, [breed])
```

L'utilisation est assez simple :

- Importez `useCallback` depuis React car c'est un hook intégré.
- Enveloppez une fonction dont vous souhaitez sauvegarder la définition.
- Comme dans `useEffect`, passez un tableau de dépendances qui indiquera à React quand cette valeur stockée (la définition de la fonction dans ce cas) doit être actualisée.

L'une des premières choses à noter est précisément la partie *définition de la fonction*. Il stocke la définition, pas l'exécution elle-même, pas le résultat – donc la fonction sera exécutée chaque fois qu'elle est appelée. À cause de cela, n'utilisez pas ce hook pour éviter des calculs longs.

Alors, quel est l'avantage de stocker une définition de fonction ?

### Retour à l'égalité référentielle

Si la fonction elle-même est utilisée, et non la valeur retournée, comme dans :

- Dépendance dans `useEffect` ou tout autre hook.
- Prop d'un composant enfant, contexte, etc.

Pour obtenir une véritable égalité entre les rendus, `useCallback` stockera la définition de la fonction avec la **même référence à l'objet en mémoire**. 

Sans ce hook, à chaque rendu, la fonction sera recréée et pointera vers une référence en mémoire différente. Ainsi, React comprendra qu'elle est différente même si vous utilisez `React.memo` dans votre composant enfant.

Vous pouvez tester ce comportement dans le projet d'exemple. Vous verrez que, avec la version non optimisée, chaque fois que vous écrivez, l'effet secondaire d'un composant enfant est déclenché. 

Dans cette démonstration, vous n'obtenez qu'un fetch et un ralentissement fictif. Mais imaginez ce même problème dans un grand projet qui exécute des calculs coûteux sur le client ou dépense beaucoup sur le serveur.

![use-callback-referential-equality](https://www.freecodecamp.org/news/content/images/2022/12/use-callback-referential-equality.png)

## Comment fonctionne le hook `useMemo`

C'est le deuxième hook intégré que vous verrez aujourd'hui. Dans ce cas, vous pouvez considérer ce hook comme une optimisation directe car il stocke le résultat d'une fonction et empêche son exécution jusqu'à ce que les dépendances changent.

Comme il peut stocker le résultat d'une fonction et également empêcher l'exécution entre les rendus d'un composant, vous pouvez utiliser ce hook dans deux situations.

### Égalité référentielle

Comme vous l'avez vu avec `useCallback`, nous pouvons obtenir une égalité référentielle avec ce hook également – mais cette fois pour le résultat lui-même. 

Si une fonction retourne quelque chose qui sera traité différemment à chaque rendu, le plus souvent des objets et des tableaux, vous pouvez utiliser `useMemo` pour obtenir une véritable égalité.

```ts
import { useMemo } from "react"

const params = useMemo(() => {
    // ...
    return { breed }
  }, [breed])
```

Dans l'exemple ci-dessus, vous pouvez voir l'utilisation de `useMemo` :

- Importez `useMemo` depuis React car c'est un hook intégré.
- Enveloppez une fonction dont vous souhaitez sauvegarder le résultat.
- Comme dans `useEffect`, il passe un tableau de dépendances qui indiquera à React quand cette valeur stockée (la valeur retournée par la fonction) doit être actualisée.

Dans ce cas, la fonction retourne un objet. Comme vous le savez, comparer des objets avec [Object.is](http://Object.is) n'est pas la même chose car ils sont stockés à différentes adresses mémoire. Avec useMemo, vous pouvez sauvegarder la même référence.

Dans le projet d'exemple, vous pouvez tester ce comportement comme dans la section précédente, avec les mêmes résultats. Avec la version non optimisée, chaque frappe récupérera les images. Avec `useMemo`, l'égalité est maintenue et le composant enfant ne récupère pas l'image à nouveau.

![use-memo-referential-equality](https://www.freecodecamp.org/news/content/images/2022/12/use-memo-referential-equality.png)

### Calcul coûteux

Parce que vous stockez une valeur et évitez d'exécuter la fonction avec `useMemo`, vous pouvez utiliser cela pour éviter d'exécuter des calculs coûteux inutiles et rendre votre site plus performant.

Voyons cela avec le projet d'exemple :

![use-memo-expensive-calculation](https://www.freecodecamp.org/news/content/images/2022/12/use-memo-expensive-calculation.png)

Il y a un composant qui, étant donné un nombre n, imprime le n-ième nombre de Fibonacci. Mais cette version récursive de l'algorithme fonctionne plutôt mal. 

Vous trouverez également un changement constant au fil du temps pour forcer les rendus. Le jauge de performance changera d'état (ajoutant et supprimant des blocs 60 fois par seconde). Parce que cet état change tout le temps, la fonction qui calcule le nombre de Fibonacci s'exécute constamment encore et encore, même si le nombre donné est toujours le même.

Avec cela, vous verrez comment les performances se dégradent visiblement lorsque vous utilisez des valeurs plus élevées avec la version non optimisée. La version optimisée ne subira des pics de performance que lorsque vous changerez les nombres dans le curseur (lorsque le nombre change) mais le reste des rendus sauteront le calcul et serviront directement le résultat.

Le problème ici est que dans notre travail quotidien, nous ne rencontrerons pas de calculs appelés "calcul coûteux" et la décision d'utiliser `useMemo` ne sera pas nécessairement toujours ou jamais.

## Quand optimiser

Jusqu'à présent, vous avez vu quelques indicateurs sur quand utiliser les différents hooks pour éviter les rendus inutiles et/ou les effets secondaires. Mais définissons quelques règles générales pour décider quand les utiliser dans ces cas pas si clairs :

- Passez d'abord en revue votre code et repensez à la manière dont vous avez structuré les choses. Vous trouverez les plus grandes opportunités d'amélioration des performances dans votre code lui-même. Vous pouvez trouver plus d'informations dans [cet article de Dan Abramov](https://overreacted.io/before-you-memo/).
- Si vous n'avez pas la preuve qu'une optimisation vous donne des résultats bénéfiques, n'optimisez pas – ce n'est pas gratuit.
- Si vous ne voulez pas faire le travail supplémentaire nécessaire pour prouver qu'une optimisation vous donne des résultats bénéfiques, soyons honnêtes : vous ne voulez pas optimiser non plus.

## Comment mesurer l'impact/gain de performance

La règle la plus importante pour l'optimisation (qui vient toujours après avoir passé en revue votre propre code en premier) est de pouvoir mesurer si les changements prennent effet et quel est le % de gain. Et vous ne faites pas cela uniquement pour pouvoir jeter ce % dans votre prochaine revue de performance.

Pour cela, nous allons examiner deux options sur la manière de procéder lorsque vous suspectez un problème de performance ou souhaitez simplement vérifier les principaux domaines d'amélioration.

### Version approximative

J'ajouterai cette option car soyons honnêtes : vous continuez à déboguer votre code avec `console.log` partout, n'est-ce pas ? Ne vous inquiétez pas, nous sommes dans le même bateau.

![crappy-debugger-meme](https://www.freecodecamp.org/news/content/images/2022/12/crappy-debugger-meme.png)

Une approche rapide et furieuse pour essayer de mesurer les problèmes de performance consiste à déterminer combien de temps il faut pour exécuter une certaine action et combien de fois cette action est effectuée. Donc, une façon de faire cela est :

```ts
const t0 = performance.now()
expensiveCalculation(targetNumber)
const t1 = performance.now()
console.log(`Call to expensiveCalculation took ${t1 - t0} milliseconds.`)
console.count('Expensive Calculation')
```

Mais cette information seule détectera très peu de cas évidents où vous suspectiez déjà quelque chose de mal. 

Faites également attention au `StrictMode` qui trompera votre `console.count` en répétant certains rendus pour des raisons de stabilité.

Vérifions maintenant la bonne façon de faire.

### Version Pro

Dans cette version, vous utiliserez les outils officiels [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) pour inspecter les performances de certaines parties de votre code. Une fois que vous avez installé cette extension de navigateur, ouvrez les outils de développement du navigateur et recherchez `Profiler`.

![profiler](https://www.freecodecamp.org/news/content/images/2022/12/profiler.png)

Je donnerai des exemples avec le projet d'exemple, mais vous pouvez le faire avec votre propre projet et vérifier les résultats.

Si vous appuyez sur le bouton `record` et commencez à effectuer les actions que vous pensez pouvoir nécessiter un réglage des performances, le profiler enregistrera et imprimera une explication détaillée de ce qui s'est passé là.

Par exemple, dans le projet d'exemple de calcul coûteux, nous allons comparer côte à côte la version non optimisée versus la version useMemo :

![profiler-graph](https://www.freecodecamp.org/news/content/images/2022/12/profiler-graph.png)

![profiler-graph-detailed](https://www.freecodecamp.org/news/content/images/2022/12/profiler-graph-detailed.png)

J'ai appuyé sur le bouton d'enregistrement, attendu quelques secondes et appuyé à nouveau sur enregistrer pour obtenir ces résultats, avec les deux versions. Comme vous pouvez le voir, comme il s'agit d'un cas extrême préparé, l'énorme amélioration entre les deux est évidente.

Mais examinons de plus près ce qui apparaît dans le profiler :

- Les lignes grises sont des composants qui n'ont pas été re-rendus, donc ce n'est rien à craindre en termes de performance.
- Les lignes vertes et jaunes sont des composants qui ont été re-rendus et vous pouvez voir combien de temps il a fallu pour les rendre.
- Si vous cliquez sur chaque bloc, vous pouvez voir une explication détaillée avec plus de données.

Je ferai un article complet en profondeur sur le profiler, mais pour l'instant, voici quelques conseils rapides :

- Sous l'icône des paramètres, Général, cochez `Highlight updates when components render.`. Cela montrera exactement ce qui est rendu et peut détecter les composants enfants qui ne sont pas censés se rendre sous certaines actions.
- Sous l'icône des paramètres, Profiler, cochez `Record why each component rendered while profiling.`. Cela ajoutera une brève explication de ce qu'un composant rend et cela peut vous donner des indices sur l'endroit où vous devez placer une mise à niveau.

## Conclusion

Comme vous l'avez vu, ces deux hooks souvent mal compris ont des fonctions et des scénarios très différents sur la manière de les utiliser pour un véritable bénéfice. Il est maintenant temps de passer en revue certains de vos projets actuels/passés et de repérer les cas où vous utilisiez cela incorrectement ou d'autres qui pourraient en avoir besoin.

L'optimisation dans React est quelque chose qui, à l'avenir, pourra être fait automatiquement par la bibliothèque. Mais, au moment de la rédaction de cet article, c'est un processus que vous devez faire avec soin et après une analyse approfondie.

J'espère que vous avez trouvé ce tutoriel utile et qu'il vous aidera à construire des applications plus performantes avec React. Merci d'avoir lu !