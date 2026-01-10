---
title: Qu'est-ce que le Throttling en JavaScript ? Expliqué avec un cas d'utilisation
  simple de React
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2024-05-01T15:58:59.000Z'
originalURL: https://freecodecamp.org/news/throttling-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/throttling-image.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que le Throttling en JavaScript ? Expliqué avec un cas d'utilisation
  simple de React
seo_desc: 'Welcome back, fellow developers! Today, we are once again delving into
  JavaScript and Web Development and learning about throttling.

  As a developer, making your website user-friendly is important. This goes a long
  way toward the product''s success, an...'
---

Bienvenue à nouveau, chers développeurs ! Aujourd'hui, nous plongeons à nouveau dans JavaScript et le développement web pour apprendre le throttling.

En tant que développeur, rendre votre site web convivial est important. Cela contribue grandement au succès du produit, et une partie clé de l'expérience utilisateur est la performance du site web.

Dans un [tutoriel précédent](https://www.freecodecamp.org/news/deboucing-in-react-autocomplete-example/), j'ai discuté de la manière d'améliorer les performances de toute fonctionnalité en utilisant une technique appelée debouncing. Et vous pouvez utiliser une technique similaire, appelée throttling, mais dans un scénario légèrement différent. Vous apprendrez comment implémenter le throttling dans cet article.

Pour ce guide, je suppose que vous avez une connaissance de base de JavaScript. Ne vous inquiétez pas si vous êtes débutant – j'ai fourni des explications simples et détaillées pour vous guider. Alors, plongeons directement dans le sujet !

## Table des matières

1. [Qu'est-ce que le Throttling ?](#heading-quest-ce-que-le-throttling)
    
2. [Comment implémenter le Throttling en JavaScript](#heading-comment-implementer-le-throttling-en-javascript)
    
3. [Qu'est-ce qu'une Closure en JavaScript](#heading-quest-ce-quune-closure-en-javascript) ?
    
4. [Cas d'utilisation du Throttling de fonction](#heading-cas-dutilisation-du-throttling-de-fonction)
    

## Qu'est-ce que le Throttling ?

Le throttling est une technique utilisée pour limiter le taux auquel une fonction est appelée. Le throttling transforme une fonction de sorte qu'elle ne puisse être appelée qu'une seule fois dans un intervalle de temps spécifique.

Comprenons cela avec un exemple. Prenons une fonction `fun()` :

```javascript
function fun() {
    console.log('Ceci est une fonction')
}
```

Nous voulons modifier cette fonction pour qu'elle ne puisse être appelée qu'une seule fois toutes les 500 ms. Ainsi, le throttling prendra `fun()` comme entrée et retournera une fonction modifiée (throttled) `throttledFun()` qui ne peut être exécutée que 500 ms après l'exécution de la fonction précédente.

Lorsque vous appelez `throttledFun()` plusieurs fois en 500 ms, `fun()` ne sera exécutée que la première fois. Vous devrez attendre 500 ms avant que `fun()` puisse être exécutée à nouveau. Cela se produit après chaque appel de fonction ultérieur. Ainsi, `fun()` ne peut être appelée qu'une seule fois toutes les 500 ms.

## Comment implémenter le Throttling en JavaScript

Commençons par comprendre ce que nous voulons réaliser avec le throttling :

* Appeler la fonction immédiatement la première fois.
    
* Après chaque appel, empêcher la fonction d'être appelée à nouveau pendant une certaine période.
    
* Une fois cette période écoulée, la fonction peut être appelée à nouveau.
    

Pour faire tout cela, créons d'abord une fonction auxiliaire qui retournera une fonction throttled :

```javascript
function throttle(func, delay) {
      return () => {}   // retourner la fonction throttled
}
```

Pour tout cas d'utilisation, la fonction throttled sera utilisée à la place de la fonction originale `fun()`.

Commençons par simplement appeler la fonction comme ceci :

```javascript
function throttle(func, delay) {
  return () => {
        func()
    }
}
```

Une fois la fonction appelée, nous voulons la bloquer pour qu'elle ne soit pas appelée à nouveau pendant une certaine période `delay`. Une fois le temps écoulé, nous voulons débloquer la fonction. Nous pouvons réaliser ce comportement en utilisant `setTimeout`.

Pour l'instant, gardons le `setTimeout` vide. Vous comprendrez comment il fonctionne dans un instant.

```javascript
setTimeout(() => {}, delay)
```

Ensuite, nous allons déclarer une variable `timeout` qui ne sera initialisée qu'une seule fois dans la fonction externe (c'est-à-dire la fonction `throttle()`). La méthode `setTimeout` retourne un identifiant de timeout unique que nous pouvons utiliser pour identifier un timeout. Nous allons assigner l'identifiant de timeout actuel à `timeout`.

```javascript
function throttle(func, delay) {
    let timeout=null
    return () => {
        func()
        timeout=setTimeout(() => {
            // faire quelque chose
        }, delay)
    }
}
```

Puisque `timeout` contient l'identifiant du timeout actuel, nous ajoutons une condition au début de la fonction throttled pour vérifier si un timeout existe avant d'appeler la fonction originale `func()`.

```javascript
function throttle(func, delay) {
    let timeout=null
    return () => {
        if(!timeout) {
            func()
            timeout=setTimeout(() => {
                // faire quelque chose
            }, delay)
        }
    }
}
```

Initialement, `timeout` est null, donc la fonction est exécutée. La fonction throttled démarre ensuite un nouveau timeout et l'assigne à la variable `timeout`. Dans le prochain appel de fonction, elle vérifie si un timeout existe avant d'appeler `func()`. Si un timeout existe déjà, elle n'exécute pas `func()`.

Mais que se passe-t-il après que la période de temps `delay` se soit écoulée ? À l'intérieur du `setTimeout`, nous devons faire quelque chose qui permet à `func()` d'être appelée à nouveau. Puisque nous utilisons `timeout` pour contrôler les appels de fonction, nous le définissons à null après `delay` millisecondes.

```javascript
timeout=setTimeout(() => {
    timeout=null
}, delay)
```

Maintenant, lorsque vous appelez la fonction, elle est exécutée et le processus se répète en démarrant un nouveau timeout. Nous avons réussi à throttler la fonction.

Mais il y a quelque chose de fondamental que nous négligeons encore. Dans l'appel de fonction actuel, une fois que nous avons assigné `setTimeout` à la variable `timeout`, pour le suivant, nous supposons que `timeout` est toujours valide et contient la valeur que nous voulons – même si la variable est déclarée à l'intérieur de la fonction `throttle()`.

Comment la fonction interne peut-elle encore avoir accès à la variable longtemps après que la fonction `throttle()` ait terminé son exécution ? Elle utilise un concept appelé closure. Faisons un petit détour pour visiter ce concept.

### Qu'est-ce qu'une closure en JavaScript ?

En JavaScript, une fonction interne a toujours accès aux variables locales de la fonction externe. Dans notre cas, la fonction interne a accès à `timeout` qui a une portée au niveau de la fonction dans la méthode `throttle()`.

Mais lorsque la fonction externe retourne cette fonction interne, la fonction interne conserve toujours une référence aux variables locales de la fonction externe longtemps après que la fonction externe ait terminé son exécution. C'est le concept de closure.

Comprenons les closures avec un exemple.

```python
function outerFunction() {
  const x = 5;

  return () => {
    console.log(x);
  }
}

const inner = outerFunction();

inner(); // affiche 5

// console.log(x)   Lance une erreur de référence
```

Ici, si nous appelons `inner()`, le code s'exécute sans aucune erreur et affiche 5. Mais, si nous essayons d'accéder à `x` directement, JavaScript lance une erreur de référence.

![Screenshot-2024-02-09-141749](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-09-141749.png align="left")

*Erreur de référence JavaScript : "x n'est pas défini"*

Ici, `inner()` ferme sur `x` et seule cette fonction peut utiliser la variable et aucune autre. Nous ne pouvons pas accéder à la variable explicitement.

Vous pouvez consulter [ce tutoriel pour débutants](https://www.freecodecamp.org/news/closures-in-javascript/) pour en apprendre davantage sur les closures.

### Retour au throttling

Continuons là où nous nous étions arrêtés.

```javascript
function throttle(func, delay) {
    let timeout=null
    return () => {
        if(!timeout) {
            func()
            timeout=setTimeout(() => {
                timeout=null
            }, delay)
        }
    }
}
```

Nous avons vu que JavaScript utilise les closures pour conserver l'accès à `timeout` chaque fois que nous appelons la fonction throttled.

Avec cela, nous avons une implémentation de base du throttling de fonction.

Testons cela en utilisant la méthode `fun()` ci-dessus et en la throttlant avec un délai de 500 ms. Cette fonction ne devrait pouvoir s'exécuter qu'une fois toutes les 500 ms.

```javascript
const throttledFun = throttle(fun, 500)
```

Appelons `throttledFun()` de différentes manières et voyons comment elle s'exécute.

```javascript
throttledFun(); // Cela s'exécutera immédiatement
throttledFun(); // Cela sera ignoré
setTimeout(() => {
  throttledFun(); // Cela sera également ignoré
}, 300);
setTimeout(() => {
  throttledFun(); // Cela s'exécutera
}, 600);
```

Le premier appel de fonction s'exécutera immédiatement. Pendant les 500 ms suivantes (délai de throttling dans cet exemple), peu importe le nombre de fois où vous appelez `throttledFun()`, rien ne se passera.

Ainsi, le deuxième appel de fonction et le troisième ne s'exécuteront pas, car ils se produisent dans les 500 ms suivant le premier appel. Une fois que 500 ms se sont écoulées, le prochain appel de fonction – c'est-à-dire le dernier – s'exécutera, puisque l'appel est fait après 500 ms.

Ainsi, il affichera la sortie suivante :

```console
Ceci est une fonction
Ceci est une fonction // Affiché après 600 ms
```

La solution n'est pas encore complète. Notre approche ne prend pas en compte les arguments de fonction. Modifions donc `fun()` pour qu'elle ait deux arguments :

```javascript
function fun(a,b) {
    console.log(`Ceci est une fonction avec les arguments ${a} et ${b}`)
}
```

Pour incorporer les arguments, utilisez l'opérateur de décomposition `...` et stockez tous les arguments dans une variable `args` :

```python
function throttle(func, delay) {
    let timeout=null
    return (...args) => {
        if(!timeout) {
            func(...args)
            timeout=setTimeout(() => {
                timeout=null
            }, delay)
        }
    }
}
```

Maintenant, appelez `throttledFun()` à nouveau, avec des arguments comme ceci :

```javascript
throttledFun(2,3);
```

Cela affichera `Ceci est une fonction avec les arguments 2 et 3`.

## Cas d'utilisation du Throttling de fonction

Voyons comment le throttling est utilisé dans des applications pratiques. Nous allons prendre un bouton qui fait un appel au serveur backend lorsque l'utilisateur clique dessus. Un appel API est fait chaque fois que quelqu'un clique sur le bouton.

Mais une requête API peut prendre un certain temps, et si l'utilisateur clique à nouveau sur le bouton, ou plusieurs fois en peu de temps, de plus en plus d'appels API sont faits, ce qui pourrait surcharger le serveur. Pour éviter ce comportement, nous utilisons le throttling de fonction. Implémentons cela avec React.

### Configuration du projet

Exécutez `create-react-app` dans votre terminal ou utilisez un [outil de construction moderne comme Vite](https://www.freecodecamp.org/news/get-started-with-vite/) pour créer votre application React. Supprimez le code boilerplate existant. Il n'est pas nécessaire d'installer des dépendances supplémentaires. Exécutez la commande `npm start` pour démarrer le projet. Vous pouvez trouver le code complet sur [GitHub](https://github.com/KunalN25/react-throttling).

J'ai configuré un serveur Node pour récupérer les données de l'application. Vous pouvez le trouver dans le dépôt Git. Exécutez la commande `node server` pour le démarrer. Je ne vais pas montrer le code Node.js car cela dépasse le cadre de ce tutoriel.

Commençons avec l'implémentation.

### Composant App

Dans le composant App, créons un bouton avec un gestionnaire `onClick` qui fait un appel API au serveur Node.

```javascript
function App() {
  const fetchData = async () => {
    const resp = await fetch("http://localhost:8000/data");
    return resp.json();
  };
  const handleClick = () => {
    fetchData().then((data) => {
      console.log(data);
    });
  };

  return (
    <div className="App">
      <button onClick={handleClick}>Cliquez-moi</button>
    </div>
  );
}

export default App;
```

Maintenant, cliquons plusieurs fois sur ce bouton.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-27.png align="left")

*Appels API multiples*

Ici, un appel API est fait chaque fois que le bouton est cliqué. Donc, si l'utilisateur clique plusieurs fois sur le bouton, de nombreux appels API seront faits en une seconde. Cela peut surcharger le serveur.

Pour résoudre ce problème, nous devons empêcher l'API d'être appelée à chaque clic sur le bouton. Voyons comment y parvenir avec le throttling.

### Implémentation du Throttling en utilisant un Hook personnalisé

Nous allons écrire la logique de throttling à l'intérieur d'un hook personnalisé. Puisque vous pourriez avoir besoin de throttling à plusieurs endroits dans votre application, il est recommandé de mettre la logique à l'intérieur d'un hook personnalisé.

Créez un nouveau dossier appelé `custom-hooks`. À l'intérieur, créez un fichier `useThrottle.js`. À l'intérieur du fichier, créez et exportez une nouvelle fonction `useThrottle()`. La méthode doit prendre une fonction et un délai comme paramètres et retourner la fonction throttled.

```javascript
const useThrottle = (func, delay) => {
  let timeout = null;
  return (...args) => {
    if (timeout) {
      return;
    }
    func(...args);
    timeout = setTimeout(() => {
      timeout = null;
    }, delay);
  };
};

export default useThrottle;
```

Maintenant, à l'intérieur du composant App, appelez cette méthode et passez le gestionnaire de clic `handleClick()` et un délai de 1000 ms.

```javascript
const handleClickThrottled = useThrottle(handleClick, 1000);
```

Nous utiliserons cette fonction comme gestionnaire d'événements pour notre bouton.

```javascript
<button onClick={handleClickThrottled}>Cliquez-moi</button>
```

### Résultat

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-28.png align="left")

*Appels API après Throttling*

Après avoir cliqué plusieurs fois sur le bouton pendant deux secondes, seulement deux appels API sont faits.

En limitant le nombre de fois où vos API sont appelées, le throttling améliore les performances de votre application.

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est le throttling et comment l'implémenter. Le throttling vous permet de contrôler le taux auquel une fonction peut être exécutée dans une période spécifique.

Le throttling utilise un concept important appelé closures. Elles vous permettent de travailler avec des variables locales même après qu'une fonction ait terminé son exécution. Les closures peuvent être assez déroutantes pour les débutants, alors prenez votre temps avec elles.

Ensuite, je vous ai montré un cas d'utilisation courant du throttling, où vous pouvez contrôler le nombre de fois qu'un appel API peut être fait sur plusieurs clics de bouton. J'ai utilisé des hooks personnalisés pour implémenter le throttling dans React. Cela sert à améliorer les performances des applications web. J'espère que cela vous aidera dans vos futurs projets.

Si vous n'êtes pas en mesure de comprendre le contenu ou si vous trouvez l'explication insatisfaisante, faites-le moi savoir. Les nouvelles idées sont toujours appréciées ! N'hésitez pas à me contacter sur Twitter. En attendant, au revoir !