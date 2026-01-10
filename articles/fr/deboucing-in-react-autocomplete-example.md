---
title: Debouncing en JavaScript – Expliqué en construisant une fonctionnalité d'auto-complétion
  dans React
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-02-12T23:23:30.000Z'
originalURL: https://freecodecamp.org/news/deboucing-in-react-autocomplete-example
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/photo-1550063873-ab792950096b.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Debouncing en JavaScript – Expliqué en construisant une fonctionnalité
  d'auto-complétion dans React
seo_desc: 'Hi readers, I hope you are doing great! I am back with another tutorial
  on web development. If you are someone who enjoys developing web apps with JavaScript
  and React, then this post is for you.

  When you roll out a new app into production, you want ...'
---

Bonjour les lecteurs, j'espère que vous allez bien ! Je suis de retour avec un autre tutoriel sur le développement web. Si vous êtes quelqu'un qui aime développer des applications web avec JavaScript et React, alors cet article est pour vous.

Lorsque vous déployez une nouvelle application en production, vous voulez vous assurer qu'elle est conviviale. La performance d'un site web est une partie clé de l'expérience utilisateur. Chaque utilisateur veut que le site web et son contenu se chargent rapidement. Chaque seconde est précieuse et pourrait entraîner un utilisateur à ne plus jamais visiter votre site web.

Dans ce guide, nous allons comprendre une technique très importante en JavaScript connue sous le nom de debouncing. Ensuite, je vais vous montrer comment implémenter la fonctionnalité d'auto-complétion dans React avec le debouncing.

Maintenant, afin de tirer le meilleur parti de ce tutoriel, je suppose que vous avez une connaissance de base de JavaScript. Si vous devez commencer ou réviser, voici quelques ressources pour vous :

* Apprendre les bases de JavaScript – [manuel pour débutants](https://www.freecodecamp.org/news/learn-javascript-for-beginners/)

* La certification [JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/news/learn-javascript-with-new-data-structures-and-algorithms-certification-projects/) de freeCodeCamp

## **Table des matières :**

* [Qu'est-ce que le Debouncing ?](#heading-quest-ce-que-le-debouncing)

* [Comment implémenter le Debouncing en JavaScript](#heading-comment-implementer-le-debouncing-en-javascript)

* [Cas d'utilisation du Debouncing](#heading-cas-dutilisation-du-debouncing)

* [Conclusion](#heading-conclusion)

## Qu'est-ce que le Debouncing ?

Le debouncing est une stratégie utilisée pour améliorer les performances d'une fonctionnalité en contrôlant le moment où une fonction doit être exécutée.

Le debouncing accepte une fonction et la transforme en une fonction mise à jour (debounced) de sorte que le code à l'intérieur de la fonction originale soit exécuté après une certaine période de temps.

Si la fonction debounced est appelée à nouveau dans cette période, le minuteur précédent est réinitialisé et un nouveau minuteur est démarré pour cet appel de fonction. Le processus se répète pour chaque appel de fonction.

Un exemple vous aidera à mieux comprendre. Prenons une fonction `fun()`. Nous voulons que cette fonction s'exécute après 500ms.

```javascript
function fun() {
    console.log('This is a function')
}
```

Après le debouncing, une nouvelle fonction `debouncedFun()` est retournée. Maintenant, chaque fois que vous appelez `debouncedFun()`, elle sera appelée après 500ms.

Si vous l'appelez à nouveau dans les 500ms suivant le premier appel, le minuteur précédent est réinitialisé et un nouveau minuteur est démarré pour le deuxième appel de fonction. Le processus se répète si vous continuez à appeler la fonction dans les 500ms.

## Comment implémenter le Debouncing en JavaScript

Comprenons comment implémenter le debouncing en JavaScript. Tout d'abord, nous allons passer en revue nos exigences. Quel comportement voulons-nous de la fonction debounced ?

* Retarder l'exécution de la fonction d'un certain temps, `delay`.

* Réinitialiser le minuteur si la fonction est appelée à nouveau.

Pour debouncer une fonction, nous aurons une fonction séparée qui accepte la référence de la fonction et le délai comme paramètres, et retourne une fonction debounced.

```python
function debounce(func, delay) {
      return () => {}   // retourne une fonction debounced
}
```

Cette fonction ne sera appelée qu'une seule fois pour retourner une fonction debounced et celle-ci, à son tour, sera utilisée dans le code suivant.

Pour retarder une fonction de quelques millisecondes, nous pouvons simplement utiliser la fonction `setTimeout` en JavaScript.

```python
function debounce(func, delay) {
    return () => {
        setTimeout(() => {
        	func()
        }, delay)
    }
}
```

Cela retarde l'appel de la fonction de `delay` millisecondes. Mais cela est incomplet car il ne satisfait que la première exigence. Comment obtenir le deuxième comportement ?

Créons une variable `timeout` et assignons-lui la valeur de retour de la méthode `setTimeout`. La méthode `setTimeout` retourne un identifiant unique pour le timeout, qui est conservé par la variable `timeout`.

```python
function debounce(func, delay) {
    let timeout=null
    return () => {
        timeout=setTimeout(() => {
            func()
        }, delay)
    }
}
```

Chaque fois que vous invoquez `setTimeout`, l'ID est différent. Nous allons utiliser cette variable `timeout` pour réinitialiser le minuteur.

Mais comment accéder à `timeout` depuis l'extérieur de la méthode `debounce()` ? Comme mentionné précédemment, `debounce()` n'est utilisée qu'une seule fois pour retourner une fonction debounced. Celle-ci, à son tour, effectue la logique de debouncing.

Alors, comment la fonction debounced a-t-elle accès à `timeout` même si elle est utilisée en dehors de la fonction `debounce()` ? Eh bien, elle utilise un concept appelé closure.

### Qu'est-ce qu'une closure en JavaScript ?

En JavaScript, une fonction interne a toujours accès aux variables locales de la fonction externe. Dans notre cas, la fonction interne a accès à `timeout` qui a une portée au niveau de la fonction dans la méthode `debounce()`.

Mais lorsque la fonction externe retourne cette fonction interne, la fonction interne conserve toujours une référence aux variables locales de la fonction externe longtemps après que la fonction externe a terminé son exécution. C'est le concept de closure.

Comprenons les closures avec un exemple.

```python
function outerFunction() {
  const x = 5;

  return () => {
    console.log(x);
  }
}

const inner = outerFunction();

inner(); // imprime 5

// console.log(x)   Lance une erreur de référence
```

Ici, si nous appelons `inner()`, le code s'exécute sans aucune erreur et imprime 5. Mais, si nous essayons d'accéder à `x` directement, JavaScript lance une erreur de référence.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-09-141749.png align="left")

*Erreur de référence JavaScript*

Ici, `inner()` ferme sur `x` et seule cette fonction peut utiliser la variable et aucune autre. Nous ne pouvons pas accéder à la variable explicitement.

Vous pouvez consulter [ce tutoriel pour débutants](https://www.freecodecamp.org/news/closures-in-javascript/) pour en savoir plus sur les closures.

### Retour au Debouncing

Revenons à l'endroit où nous nous étions arrêtés :

```python
function debounce(func, delay) {
    let timeout=null
    return () => {
        timeout=setTimeout(() => {
            func()
        }, delay)
    }
}
```

Ici, JavaScript utilise une closure pour conserver l'accès à `timeout` chaque fois que nous utilisons la fonction debounced.

Utilisons cela à notre avantage. Puisque `debouncedFun()` a accès à la même variable `timeout` à chaque appel de fonction, nous pouvons ajouter une condition pour vérifier si un timeout précédent existe. Nous pouvons simplement faire cela avec une vérification de nullité, `if(timeout !== null)` ou `if(timeout)`.

Ensuite, nous utilisons la méthode `clearTimeout()` pour annuler le timeout précédent, réinitialisant ainsi le minuteur.

Ajoutez l'instruction suivante avant de démarrer un nouveau timeout :

```python
if(timeout) 
	clearTimeout(timeout)
```

Une fois le timeout réinitialisé, un nouveau timeout est démarré pour l'appel de fonction actuel, dont l'ID est ensuite assigné à `timeout`. Le processus est répété pour les appels de fonction suivants qui ont accès au même `timeout` grâce aux closures.

```python
function debounce(func, delay) {
    let timeout=null
    return () => {
        if(timeout) clearTimeout(timeout)

        timeout=setTimeout(() => {
            func()
        }, delay)
    }
}
```

Avec cela, nous avons satisfait notre deuxième exigence – c'est-à-dire, réinitialiser le minuteur et en démarrer un nouveau. Il est temps d'utiliser cette fonction debounced.

Passons `fun()` à la méthode `debounce()` avec un délai de 500ms.

```python
const debouncedFun = debounce(fun, 500)
```

`debouncedFun()` est essentiellement `fun()` avec un comportement de debouncing. Appelons cette fonction à différents intervalles de temps pour tester notre fonctionnalité.

```python
debouncedFun()

setTimeout(debouncedFun, 300)

setTimeout(debouncedFun, 900)
```

Le premier appel de fonction est fait instantanément. Les deux autres sont faits après 300ms et 900ms respectivement. Pouvez-vous deviner le résultat ?

Le code imprime `This is a function` deux fois. Comprenons pourquoi. Ici, après le premier appel, `fun()` est programmé pour s'exécuter après 500ms. Mais le deuxième appel est fait en 300ms, ce qui réinitialise le minuteur et en démarre un nouveau.

500ms se sont écoulés et la méthode `fun()` s'exécute. Ensuite, à 900ms, un autre appel de fonction est fait. Cela exécute à nouveau `fun()` après 500ms.

Il y a encore une petite amélioration que nous devrions apporter. Notre logique ne prend pas en compte les arguments de fonction. Remplaçons `fun()` par `fun(a, b)`.

```python
function fun(a, b) {
    console.log(`This is a function with arguments ${a} and ${b}`)
}
```

Pour incorporer les arguments lors du debouncing, retournez une fonction debounced qui accepte les arguments.

```python
function debounce(func, delay) {
    let timeout=null
    return (...args) => {
        if(timeout) clearTimeout(timeout)

        timeout=setTimeout(() => {
            func(...args)
            timeout=null
        }, delay)
    }
}
```

En utilisant l'opérateur de décomposition, tous les arguments passés à la fonction debounced seront stockés sous forme de tableau dans la variable `args`. Ensuite, décomposez le même tableau `args` pour appeler la fonction réelle avec les arguments passés.

```python
const debouncedFun=debounce(fun, 500)
debouncedFun(2,3)
```

Le code ci-dessus imprime `This is a function with arguments 2 and 3` après 500ms.

## Cas d'utilisation du Debouncing

Voyons comment le debouncing est utilisé dans les applications pratiques. Le cas d'utilisation le plus courant du debouncing est la fonctionnalité d'auto-complétion. Vous devez avoir vu de nombreux sites web où vous tapez dans un champ de saisie et il affiche une liste de résultats au fur et à mesure que vous les tapez.

Voici un exemple de Google Search :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-09-163240.png align="left")

*Auto-complétion de Google Search après avoir tapé "Top 10"*

Google Search affiche les termes les plus récents et les plus recherchés. Les informations sont principalement récupérées depuis le cache du navigateur. Mais, plusieurs sites web font des appels API au serveur backend pour récupérer les données depuis une base de données.

Cela peut facilement être implémenté en ajoutant un événement `onchange` à l'élément `input` et en implémentant la logique de récupération dans le gestionnaire d'événements. Mais il y a un léger problème avec cela.

Considérez l'exemple suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-09-163930.png align="left")

*Requête API faite pour chaque valeur de saisie*

Lorsque je tape le mot *absolute*, une requête API est faite chaque fois que la valeur du champ de saisie change. Nous faisons 8 requêtes API en très peu de millisecondes, ce qui met une charge importante sur le serveur backend et pourrait causer des problèmes de performance.

Idéalement, nous voulons afficher les résultats d'auto-complétion un certain temps après que l'utilisateur a fini de taper. Ici, l'utilisateur a tapé *absolute* d'un seul coup, donc au lieu d'afficher des résultats chaque fois que la saisie change, nous pourrions les afficher une fois que l'utilisateur a fini de taper – c'est-à-dire, nous pourrions ajouter un certain délai entre le changement de saisie et l'affichage des résultats.

Ainsi, nous ne faisons les appels API que lorsque l'utilisateur a fini de taper son mot et non à chaque changement de saisie. Cela réduit le nombre d'appels API et améliore les performances. Nous pouvons obtenir ce comportement avec le debouncing.

Comprenons comment implémenter la fonctionnalité d'auto-complétion dans React.

### Exemple d'auto-complétion

Utilisez `create-react-app` (ou un outil de build moderne comme Vite) pour créer le projet. Supprimez le code boilerplate existant. Il n'est pas nécessaire d'installer des dépendances supplémentaires. Exécutez la commande `npm start` pour démarrer le projet. Vous pouvez trouver le code complet sur [GitHub](https://github.com/KunalN25/react-debouncing).

J'ai configuré un serveur Node pour récupérer les données pour l'application. Vous pouvez le trouver dans le dépôt Git. Exécutez la commande `node server` pour le démarrer. Je ne vais pas montrer le code Node.js car il est hors du cadre de ce tutoriel.

Commençons avec l'implémentation. Nous allons écrire une fonctionnalité d'auto-complétion simple. L'application doit afficher une liste de villes qui contiennent une chaîne de caractères saisie par l'utilisateur.

#### Composant App

Nous aurons d'abord besoin d'un élément `input` pour accepter la saisie de l'utilisateur et d'un *conteneur de résultats* pour les résultats de recherche. Attachez un gestionnaire d'événements à l'élément `input` qui est une fonction `async` puisqu'elle inclura la logique de récupération.

```python
function App() {
    const [data, setData] = useState(null)

    const loadData = async (event) => {
        
    }
    return (
        <div className="App">
            <input type="text" onChange={(e) => loadData(e)}/>
            {data && data.length !== 0 &&
            <div className="results-container">
                {data.map(item => (
                    <div key={item.id} className="result-item">
                        <p> {item.city} </p>
                    </div>
                ))}
            </div>}
        </div>
    );
}
```

Les données seront stockées sous forme d'état et les résultats ne seront affichés que si les données ne sont pas vides. Je vais sauter le CSS pour ce tutoriel, vous pouvez le trouver dans le [Dépôt Git](https://github.com/KunalN25/react-debouncing).

#### Gestionnaire d'événements

La fonction `loadData()` récupère nos données et stocke la réponse sous forme d'état.

```python
const loadData = async (event) => {
	const value=event.target.value
    if(value === '') {
        setData(null)
        return
    }
    const response=await fetch(`http://localhost:8000/data/${value}`)
    const res=await response.json()
    setData(res)
}
```

Si aucune valeur n'est saisie, quittez simplement la fonction. Sinon, faites la requête au point de terminaison du serveur node. Cette fonction est appelée chaque fois que la saisie change, nous allons donc debouncer cette fonction.

#### Implémentation du Debounce utilisant un Hook personnalisé

Nous allons écrire la logique de debouncing à l'intérieur d'un hook personnalisé. L'avantage des hooks personnalisés est que vous pouvez réutiliser la même logique dans toute votre application. Il est fortement conseillé de le faire.

Créez un nouveau dossier `custom-hooks` et à l'intérieur, créez un fichier `useDebounce.js`. Comme expliqué précédemment, la méthode `useDebounce()` doit prendre une fonction et un délai comme paramètres et retourner la fonction debounced.

```python
const useDebounce = (func, delay) => {
    let timeout=null

    return (...args) => {
        if(timeout) clearTimeout(timeout)

        timeout=setTimeout(() => {
            func(...args)
        }, delay)
    }
}

export default useDebounce
```

Maintenant, à l'intérieur du composant app, appelez cette méthode une fois pour obtenir `loadDataDebounced()`.

```python
const loadDataDebounced = useDebounce(loadData, 400)
```

Nous allons utiliser cette nouvelle méthode comme gestionnaire d'événements pour l'élément `input`.

```python
<input type="text" onChange={(e) => loadDataDebounced(e)}/>
```

#### Résultat

Saisissez une chaîne de recherche à l'intérieur de l'élément `input` pour tester notre code.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-09-190240.png align="left")

*Sortie à l'écran*

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-09-191234.png align="left")

Comme vous pouvez le voir dans l'onglet Réseau, une seule requête est envoyée au lieu de trois. Cela rend les performances de recherche beaucoup meilleures.

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est le debouncing et comment il est implémenté. Le debouncing retarde l'exécution de la fonction d'un certain temps et réinitialise le minuteur précédent si la fonction est appelée à nouveau.

Le debouncing utilise le concept important des closures. J'ai fait un léger détour de l'implémentation pour expliquer ce qu'est une closure. Cela peut être un concept déroutant pour les débutants, alors prenez votre temps pour le comprendre. Les closures vous permettent de travailler avec des variables locales même après qu'une fonction a terminé son exécution.

Ensuite, je vous ai montré un cas d'utilisation populaire du debouncing, la fonctionnalité d'auto-complétion. Les performances de la fonctionnalité peuvent être améliorées avec le debouncing. Je vous ai également montré comment implémenter l'auto-complétion dans React et utiliser le debouncing avec des hooks personnalisés. J'espère que cela vous aidera dans vos futurs projets.

Si vous n'arrivez pas à comprendre le contenu ou trouvez l'explication insatisfaisante, faites-le moi savoir. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. En attendant, au revoir !