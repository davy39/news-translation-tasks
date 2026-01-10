---
title: Comment configurer le suivi des performances et des utilisateurs dans React
  avec Google Analytics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-31T18:37:30.000Z'
originalURL: https://freecodecamp.org/news/performance-and-user-tracking-in-react-with-google-analytics
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/guillaume-fischer--JPCZcxeqzM-unsplash.jpg
tags:
- name: Google Analytics
  slug: google-analytics
- name: React
  slug: react
- name: web performance
  slug: web-performance
seo_title: Comment configurer le suivi des performances et des utilisateurs dans React
  avec Google Analytics
seo_desc: 'By Mohammad Iqbal

  Keeping track of your users and your app performance is a very crucial part of modern
  web development. You may have seen reports of companies increasing revenues by simply
  decreasing the load time of their app by a few hundred milli...'
---

Par Mohammad Iqbal

Suivre vos utilisateurs et les performances de votre application est une partie très cruciale du développement web moderne. Vous avez peut-être vu des rapports de sociétés augmentant leurs revenus simplement en réduisant le temps de chargement de leur application de quelques centaines de millisecondes. 

Suivre le comportement de vos utilisateurs est également crucial. Cela vous permettra de modifier et de construire votre application selon la manière préférée de vos utilisateurs d'interagir avec votre application, ce qui entraînera des utilisateurs plus heureux et plus de trafic sur votre site.  

Voici le projet terminé : 

[https://github.com/iqbal125/react-hooks-google-analytics](https://github.com/iqbal125/react-hooks-google-analytics)

Dans ce guide, je vous donnerai un guide fondamental complet pour suivre à la fois les performances et le comportement des utilisateurs. À la fin du tutoriel, vous aurez tout ce dont vous avez besoin pour construire des configurations complexes de suivi des utilisateurs et des performances. 

> Suivez-moi sur Twitter pour plus de tutoriels à l'avenir : [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)

## Table des matières

1. Introduction
2. Google Analytics
3. Suivi des vues de pages
4. Suivi des performances de chargement
5. Suivi des performances de rendu
6. Suivi de la peinture
7. Suivi du défilement
8. Suivi des événements
9. Conseils rapides sur les performances et heuristiques

## Introduction

Je vais vous montrer les métriques de performance pour la version de développement de React pour garder ce tutoriel concis. Mais dans une situation réelle, ne testez pas la version de développement, car elle contient beaucoup de code de gestion des erreurs et un manque d'optimisations qui vous donneront des résultats très biaisés. 

Pour cette raison, il est préférable de tester sur la version de production pour établir certaines métriques de base. 

De plus, pour des raisons de brièveté, je vais simplement me référer à Google Analytics comme GA. 

GA ne fonctionne pas non plus avec l'hôte local. Pour obtenir une simulation de ce que vous pourriez envoyer à GA sans l'envoyer réellement et fausser vos analyses, vous pouvez simplement substituer une console.log partout où vous prévoyez de mettre votre hit GA. 

`ReactGA` est la fonction globale et est connue sous le nom de file d'attente de commandes car elle n'exécute pas les commandes immédiatement mais ajoute des commandes à une file d'attente et les envoie ensuite de manière asynchrone. Cela ne bloque pas le thread principal et n'entraîne pas que votre code de suivi nuise aux performances de votre application. 

Un hit est lorsqu'un tracker GA envoie des données à Google Analytics. 

Nous nous concentrerons principalement sur le code React dans ce tutoriel, il existe de bien meilleurs tutoriels pour apprendre à utiliser GA.  

Il y a 3 fonctions principales que nous utiliserons lors de l'envoi de hits à GA. Vous devez savoir qu'il y en a plus mais nous nous concentrerons uniquement sur ces 3 pour les besoins de ce tutoriel. 

`GAReact.pageview()` : transmettra une chaîne contenant la route. 

`GAReact.timing()` : prendra un objet comme paramètre. Contiendra des informations liées à nos métriques de performance que nous verrons ci-dessous. Les champs seront `category`, `variable`, `value` et `label`. Remarquez que seule la propriété value proviendra de notre application, le reste des propriétés est défini par l'utilisateur.

`GAReact.event()` : prendra un objet comme paramètre. Contiendra des données sur les événements qui se produisent dans l'application (soumission de formulaire, clic sur un bouton, etc.)  Aura des champs de `category`, `action`, `label` et `value`. Notez que seule la valeur proviendra de l'application, le reste des propriétés est défini par l'utilisateur.

**Test synthétique vs RUM**  
Vous vous demandez peut-être pourquoi passer par tout ce tracas de configuration des métriques Performance Observer si vous pouvez simplement utiliser un outil comme Lighthouse ou Webpage speed test et obtenir ces métriques simplement en entrant l'URL. 

Les outils comme ceux-ci sont importants mais ils sont ce qu'on appelle des tests synthétiques puisque le test sera effectué sur votre appareil et le test ne reflétera pas réellement ce que vos utilisateurs vivent. Vous pouvez limiter le CPU ou le réseau lors de la réalisation de ces tests mais ils restent des simulations. 

L'utilisation de GA avec les métriques Performance Observer nous donnera des chiffres réels provenant de nos utilisateurs finaux, appareils et réseaux réels. Cela est connu sous le nom de RUM ou Real User Monitoring. 

Outils de test synthétique. Il suffit d'entrer l'URL de votre application pour exécuter les tests synthétiques. 

* [https://www.webpagetest.org/](https://www.webpagetest.org/)
* [https://www.thinkwithgoogle.com/feature/testmysite](https://www.thinkwithgoogle.com/feature/testmysite)
* [https://developers.google.com/speed/pagespeed/insights/](https://developers.google.com/speed/pagespeed/insights/)
* [https://www.uptrends.com/tools/website-speed-test](https://www.uptrends.com/tools/website-speed-test)
* [https://tools.pingdom.com/](https://tools.pingdom.com/)

  


## Google Analytics  


**Installation**  
Si vous avez déjà configuré Google Analytics sur votre application, n'hésitez pas à sauter cette section, il n'y a rien de nouveau ici. 

Pour configurer GA, allez sur le tableau de bord et cliquez sur l'onglet admin dans le tiroir latéral. Ensuite, cliquez sur ajouter une propriété. Remplissez les informations requises. 

Si vous lisez ce tutoriel, je vais supposer que vous êtes assez intelligent pour configurer Google Analytics avec ces trois lignes d'instruction. Sinon, voici un guide pratique de Google. 

[https://support.google.com/analytics/answer/1042508?hl=en](https://support.google.com/analytics/answer/1042508?hl=en)

Après avoir terminé la configuration, vous obtiendrez un identifiant de suivi en haut, que nous utiliserons dans notre application React.

  
**Configuration dans React**  
Nous n'avons pas besoin de réinventer la roue ici, nous pouvons utiliser une bibliothèque d'assistance créée par la Mozilla Foundation pour nous aider avec la configuration React. 

Pour installer la bibliothèque, exécutez simplement

`npm install react-ga`

Ensuite, importez simplement l'objet ReactGA où vous voulez l'utiliser

```javascript
import ReactGA from 'react-ga';
```

Vous devrez également l'initialiser dans le composant racine avec l'identifiant de suivi de Google Analytics.  

```javascript
...
ReactGA.initialize('UA-00000-1');
...
```



**Observateurs**  
`ReactGA` ne peut rien faire d'autre que d'envoyer des données au site Web Google Analytics. Pour obtenir des métriques de performance à envoyer, nous utiliserons l'API Performance Observer du navigateur. Cette API Performance Observer n'a rien à voir avec GA ou même React, c'est une API de navigateur disponible dans la plupart des navigateurs modernes 

Comment le PerformanceObserver et les API connexes fonctionnent exactement est un sujet assez vaste et est loin de la portée de ce tutoriel. Voir la section Lecture complémentaire pour plus d'informations et de liens vers des tutoriels. 

L'idée de base de leur fonctionnement est qu'ils "observent" quelque chose puis envoient ces données de manière asynchrone au moment choisi par le navigateur. Cela garde le thread principal libre pour les fonctionnalités critiques de l'application et les tâches connexes, donc le suivi des événements n'affecte pas les performances de votre application. 

Avant les observateurs, vous deviez ajouter un écouteur d'événements et le déclencher de manière synchrone chaque fois que quelque chose se produisait, ce qui entraînait des problèmes de performance notables si trop d'événements étaient déclenchés en même temps. Donc c'est le problème que les observateurs cherchent à résoudre. 



## Suivi des vues de pages  


Le suivi des vues de pages dans une application monopage comme React peut sembler compliqué, mais c'est relativement simple grâce aux bibliothèques react-router et history. 

```javascript
history.listen((location) => {
    ReactGA.set({ page: location.pathname });
    ReactGA.pageview(location.pathname)
  }
);
```

`history.listen()` vous permet de déclencher un rappel lors des changements de route, ce qui dans notre cas se trouve être le hit GA. La route est contenue dans la propriété `pathname` de `location`.  Mais il y a quelques points à noter, tels que : 

**Gestion du chargement initial**  
History écoute les changements de page mais ne provoque pas de hit lors du chargement initial de la page.

Il existe plusieurs façons de gérer le chargement initial. J'ai trouvé une manière simple de le faire qui, je pense, nécessite le moins de code et de complexité, et il suffit d'avoir une variable de chargement initial et de l'enregistrer dans l'état global. Dans la page d'accueil, utilisez simplement une condition pour vérifier si elle est fausse, puis définissez-la sur vraie après le hit. 

Variable de contexte dans le composant parent

```javascript
... 

const [initialLoad, setInitialLoad] = useState(false)

...
      <Context.Provider
            //Chargement initial
            initialLoadProp: initialLoad,
            setInitialLoadProp: () => setInitialLoad(true),
       >
      </Context.Provider>
```

Ensuite, le `useEffect()` dans le composant enfant de la page d'accueil 

```javascript
...   
useEffect(() => {
    if(!context.initialLoadProp) {
      ReactGA.pageview(props.location.pathname);  
      context.setInitialLoadProp(true)
    }
  }, [])
...

```

Il existe d'autres implémentations et discussions que vous pouvez trouver ici :

[https://github.com/react-ga/react-ga/wiki/React-Router-v4-withTracker](https://github.com/react-ga/react-ga/wiki/React-Router-v4-withTracker)  


**Suivi des pages avec des identifiants d'utilisateur**  
Une autre chose que vous pourriez vouloir savoir est combien d'utilisateurs visitent leurs pages de profil privé. L'utilisation des vues de pages vous donnera une URL unique pour chaque hit et ne fonctionnera pas. 

Supposons que vous avez les URL suivantes avec des identifiants d'utilisateur :

user/4543456/messages  
user/4543456/account  
user/3543564/messages  
user/3543564/replytomessage  
user/3543564/account

Celles-ci vous donneront toutes un hit de page unique. Une solution simple consiste simplement à vérifier avec une condition puis à supprimer l'identifiant unique. Vous pouvez également utiliser une condition pour vous assurer de ne pas envoyer ces pages à Google Analytics. 

```javascript
...

 history.listen((location) => {
   if(location.pathname.includes('/user')) {
     let rootURL = location.pathname.split('/')[1]
     let userPage = location.pathname.split('/')[3]

     let pageHit = `/${rootURL}/${userPage}`
     ReactGA.pageview(pageHit)
   } else {
     ReactGA.set({ page: location.pathname });
     ReactGA.pageview(location.pathname)
   }
});

...
```

Nous analysons simplement l'identifiant de l'utilisateur puis concaténons à nouveau la route avant d'envoyer le hit. 

Cela ne serait probablement pas vrai pour les publications de forum puisque avoir une URL unique pour chaque publication serait correct, puisque vous aimeriez savoir combien de personnes ont visité chaque publication. 



## Suivi des performances de chargement

Obtenir les performances de chargement est relativement facile. Toutes les données de performance de chargement se trouvent sous l'entrée `navigation` qui fait partie de l'API [navigation timing API](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_timing_API). 

Le Performance Observer peut être configuré comme suit dans le composant parent racine. 

```javascript
const callback = list => {
    list.getEntries().forEach(entry => {
      ReactGA.timing({
        category: "Performance de chargement",
        variable: "Une métrique",  
	value: "Valeur de la métrique"
      })
  })
}

var observer = new PerformanceObserver(callback);
observer.observe({entryTypes: ['navigation'] })
```

Tout d'abord, nous définissons une fonction à appeler pour chaque entrée. Ensuite, nous passons ce rappel à notre `PerformanceObserver` et enfin nous appelons la méthode `.observe()` sur notre observateur et passons `navigation` comme type d'entrée.  

Cela vous donnera l'entrée suivante :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-76.png)

C'est une très grande quantité d'informations, mais vraiment nous n'avons besoin que de 3 propriétés pour suivre la performance de chargement principale : 

`requestStart` : lorsque le navigateur émet une requête pour obtenir la page web à partir du serveur

`responsesStart` : lorsque le premier octet du site web arrive

`responseEnd` : lorsque le dernier octet du site web arrive

Il y a quelques choses qui se passent avant le requestStart comme la recherche DNS et la poignée de main TLS. Utilisez ces données et voyez si vous pouvez les combiner avec d'autres propriétés pour créer de nouvelles métriques. 

Avec les trois propriétés ci-dessus, nous pouvons créer 3 métriques importantes. Il suffit de substituer les propriétés `variable` et `value` pour la métrique respective. 

```
const callback = list => {
    list.getEntries().forEach(entry => {
      ReactGA.timing({
        category: "Performance de chargement",
        variable: 'Latence du serveur',
        value: entry.responseStart - entry.requestStart 
      })
  })
}
```

Latence du serveur :  
`entry.responseStart - entry.requestStart`

Temps de téléchargement :  
`entry.responseEnd - entry.responseStart`

Temps de chargement total de l'application :  
`entry.responseEnd - entry.requestStart`

  
  
**Temps jusqu'à l'interactivité**  
Cette métrique est essentiellement le temps qu'il faut pour qu'un utilisateur puisse interagir avec votre site.

Jusqu'à ce qu'une métrique TTI native soit disponible via l'API du navigateur, nous pouvons utiliser ce module polyfill npm pratique pour l'instant. Ce module est créé par Google. 

`npm install tti-polyfill`

Ensuite, nous pouvons utiliser le polyfill comme suit. 

```javascript
... 

import ttiPolyfill from 'tti-polyfill';


ttiPolyfill.getFirstConsistentlyInteractive().then((tti) => {
  ReactGA.timing({
    category: "Performance de chargement",
    variable: 'Temps jusquà linteractivité',
    value: tti 
  })
});

...
```

Nous envoyons simplement un hit à l'intérieur de notre fonction avec une instruction `.then()` enchaînée puisque nous récupérerons cette métrique de manière asynchrone. 



## Suivi des performances de rendu

Maintenant, nous pouvons discuter des performances de rendu, qui est le temps qu'il faut à React pour construire l'arbre des nœuds DOM. Nous pouvons suivre les performances de rendu avec les entrées `mark` et `measure`. 

`mark` est utilisé pour "marquer" un point dans le temps que vous souhaitez suivre. Il suffit de passer une chaîne comme nom de la marque sur la ligne exacte où vous souhaitez marquer pour le suivi. 

```javascript
performance.mark("nom de la marque")
```

`measure` est la différence entre les 2 marques. Il suffit de définir le nom de la mesure et de passer les marques de début et de fin, ce qui vous donnera la différence entre les marques en millisecondes. 

```javascript
performance.measure("nom de la marque", startingMark, EndingMark)
```

Heureusement, React est pré-bundlé avec ces marques et mesures, ce qui nous évite d'avoir à ouvrir la source React et de devoir les écrire nous-mêmes. Il suffit de passer `mark` et `measure` pour les types d'entrée et vous avez terminé. 

```javascript
...

var observer = new PerformanceObserver(callback);
observer.observe({entryTypes: ['mark', 'measure'] })

...
```

Cela vous donnera le temps qu'il faut pour que le composant parent racine et tous les composants enfants se rendent en millisecondes. Vous obtiendrez des entrées qui ressembleront à ceci : 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-73.png)

Vous obtiendrez également le temps qu'il faut pour exécuter les méthodes de cycle de vie. Il y a une richesse d'informations ici, il suffit de choisir ce que vous voulez suivre et de l'envoyer à GA en vérifiant le nom dans une instruction conditionnelle. 

```javascript
...
const callback = list => {
    list.getEntries().forEach(entry => {
      if(entry.name.includes('App') ) {
        ReactGA.timing({
          category: "Performance de rendu de l'application",
          variable: entry.name,
          value: entry.duration
        })
      }
  })
}
...
```



## Suivi des performances de peinture

Maintenant, nous pouvons suivre la peinture, qui est le moment où les pixels sont dessinés (ou "peints") à l'écran après le rendu de l'arbre DOM.  

Le suivi des performances de peinture comprend 3 métriques : First Paint, First Contentful Paint et First Meaningful Paint. 

**First Paint** : Première fois où quelque chose d'autre qu'une page blanche est présent. 

**First Contentful Paint** : Lorsque le premier élément DOM est présent. Texte, image, etc. 

First Paint et First Contentful Paint seront donnés automatiquement par l'API. Il suffit de faire ce qui suit :

```
...

const callback = list => {
    list.getEntries().forEach(entry => {
       ReactGA.timing({
          category: "Peinture",
          variable: entry.name,
          value: entry.startTime
     })
  })
}

var observer = new PerformanceObserver(callback);
observer.observe({entryTypes: ['paint'] })
```

Les entrées ressembleront à ceci

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-74.png)

Il est tout à fait possible que ces deux métriques soient exactement les mêmes, jusqu'à la milliseconde. Même si elles ne sont pas les mêmes, il peut y avoir une différence irrélevante entre elles. Pour cette raison, une autre métrique plus flexible est utilisée, appelée : 

**First Meaningful Paint** : Lorsque quelque chose de "significatif" est peint à l'écran. "Significatif" est intentionnellement vague, permettant au développeur de décider lui-même ce qu'il veut tester.  

Selon Google, le First Paint et le First Contentful Paint répondent à la question "Est-ce que cela se produit" et le First Meaningful Paint répond "Est-ce que c'est utile". "Est-ce que c'est utilisable" est répondu par le Time to Interactive. 

Une manière courante d'utiliser le First Meaningful Paint est de tester l'élément héro. Qui est l'élément principal de la page. 

Un exemple pour YouTube serait le lecteur vidéo. Les vidéos suggérées et les commentaires seraient tous des éléments secondaires non héroïques. Le suivi du moment où le lecteur vidéo a fini de peindre serait le First Meaningful Paint dans ce cas. 

Un élément héro courant sur la page d'accueil est une image d'arrière-plan près de l'en-tête qui donne la proposition de valeur ou le thème du site web. Sachant cela, nous pouvons utiliser l'API de timing des ressources pour mesurer quand notre image a fini de charger et en faire notre métrique First Meaningful Paint. 

Si votre élément héro est une image, vous pouvez simplement regarder l'API de timing des ressources puis regarder la propriété `responseEnd` et l'utiliser comme votre FMP. 

```javascript
...
const callback = list => {
    list.getEntries().forEach(entry => {
        ReactGA.timing({
          category: "First Meaningful Paint",
          variable: entry.name,
          value: entry.responseEnd
        })
  })
}

var observer = new PerformanceObserver(callback);
observer.observe({entryTypes: ['resource'] })
...
```

Réponse complète du timing des ressources.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-75.png)

Puisque l'image chargée ne signifie pas techniquement qu'elle est peinte, vous pouvez également essayer de définir les marques manuellement. 

```


//jsx 

{performance.mark('start') 
<img />
{performance.mark('end')
{performance.measure('diff', 'start', 'end')


```

Encore une fois, il y a beaucoup de flexibilité dans cette métrique, réfléchissez vraiment à votre cas d'utilisation et à ce que vous essayez de mesurer.

## **Suivi du défilement**

Le suivi de la position de défilement de votre utilisateur est une partie assez importante de l'analyse. Vous pouvez, par exemple, voir combien d'utilisateurs ont fait défiler une certaine image ou une section de texte. Ayant cette information, vous pouvez ensuite ajuster votre contenu et augmenter votre conversion. 

Vous auriez vu des implémentations plus anciennes utiliser **getBoundingClientRect()** mais cela bloquerait le thread principal et donc le suivi du défilement diminuerait réellement les performances. Vous pouvez exécuter les événements de défilement de manière asynchrone avec `IntersectionObserver`.  

Le `IntersectionObserver` est différent du `PerformanceObserver` avec lequel nous avons travaillé dans les dernières sections. 

Le `IntersectionObserver` prend 2 arguments : un rappel et un objet d'options. L'objet d'options aura 3 propriétés

`root` : L'élément que vous essayez de tester l'intersection contre. Dans la plupart des cas, ce sera le viewport qui sera la valeur de `null`. 

`rootMargin` : Les marges autour de l'élément racine. ex : "10px"

`threshold` : Combien de l'élément est visible avant que `isIntersecting` soit vrai. ex : 0.5 signifie que `isIntersecting` est vrai lorsque 50 % de l'élément est visible. 0 signifie le tout en haut de l'élément et 1.0 signifie l'élément entier. 

L'entrée retournera un objet comme suit : 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-78.png)

  
`isIntersecting` : Essentiellement utilisé pour déterminer si l'élément est visible, ce qui serait vrai lorsque le seuil est atteint.

Et maintenant le code : 

```javascript
//Obtenez l'élément que vous voulez suivre avec useRef
const intersectTarget = useRef(null)

//Utilisez l'observateur à l'intérieur du composant que vous voulez suivre le défilement
  useEffect(() => {
    const opts = {
            root: null,
            rootMargin: '0px',
            threshold: 0
    }
    const callback = list => {
      list.forEach(entry => {
        if(entry.isIntersecting) {
            ReactGA.event({
              category: 'Défilement',
              action: 'Défilé jusquà l en-tête 2',
              value: entry.intersectionRatio
            })
          }
       })
    }
    const observerScroll = new IntersectionObserver(callback, opts)

    observerScroll.observe(intersectTarget.current)
  }, [])

//jsx
  <h1 ref={intersectTarget}
      id="heading2"
		>
     Deuxième en-tête
  </h1>
```

L'idée principale ici est de d'abord initialiser le hook `useRef`. Ensuite, utilisez la référence sur l'élément que vous voulez suivre pour le défilement. Le rappel et l'observateur seront appelés dans le hook `useEffect` et l'élément peut être passé à la méthode `.observe()` avec le nom de la référence et la propriété `.current`. 



**Note** : L'observateur d'intersection se déclenchera lors du chargement initial de la page même si l'élément n'est pas visible. Cela est normal et vous verrez que la propriété `isIntersecting` est fausse. 

**Note également** : Au moment de la rédaction de cet article, il existe également une propriété `isVisible` sur l'entrée, mais elle ne fonctionne pas comme son nom l'indique. Elle reste fausse même lorsque l'élément est visible. Elle n'est documentée nulle part donc je ne peux pas commenter son but, mais je suggérerais d'utiliser la propriété `isIntersecting` à la place.     
  


## Suivi des événements

L'idée de base pour suivre les événements est d'envoyer des hits GA à l'intérieur de l'appel de fonction attaché à un gestionnaire d'événements. Il n'y a vraiment pas grand-chose de plus à cela. 

Une chose à noter est que si votre utilisateur soumet un formulaire, vous pouvez spécifier la propriété `transport: beacon` dans votre hit d'événement, ce qui vous permettra d'envoyer le hit de manière fiable même si la page est rechargée vers une autre page. Ce n'est pas vraiment un problème dans une application monopage comme React, mais si vous vouliez faire cela, sachez simplement que cette option est disponible. 

Voir le [navigator beacon](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon) pour plus d'informations 

Je vais vous montrer comment suivre une soumission de formulaire, mais ce modèle fonctionnera avec pratiquement n'importe quel événement. Encore une fois, vous envoyez simplement le hit dans une fonction attachée au gestionnaire d'événements.

```javascript
  
  ...
  const handleSubmit = (event) => {
    event.preventDefault();
    ReactGA.event({
     category: 'Formulaire',
     action: 'Soumission de formulaire',
     transport: 'beacon'
   });
    apiCall('/apicall', event.target.value)
  };
  
  ...
  
  <form onSubmit={handleSubmit}>
  ...
  </form>
  
  ...
```



  
  
**Conseils rapides sur les performances et heuristiques**  


Le plus grand domaine d'amélioration que je vois pour beaucoup de développeurs est de coder les choses à partir de zéro au lieu d'utiliser une bibliothèque. Le tree shaking réduit un peu le ballonnement, mais il y a encore un ballonnement considérable par rapport au codage de quelque chose soi-même. Ce qui vous permettra d'écrire uniquement le code dont vous avez besoin. Essayez d'utiliser le moins de bibliothèques possible. Au lieu d'utiliser une bibliothèque pour quelques fonctions, essayez simplement de regarder le code source de la bibliothèque et essayez d'implémenter ces fonctions vous-même. Gardez également à l'esprit que la plupart des bibliothèques doivent privilégier la facilité d'utilisation et la personnalisation par rapport aux performances. 

Quelques autres : 

* Pour le déclenchement d'événements comme le défilement, vous aurez définitivement besoin de débogage/limitation. Vous n'avez pas besoin de faire cela pour les observateurs.  
* N'importez que les fonctions et variables dont vous avez besoin et laissez le tree shaking supprimer le code inutilisé. 
* Ne passez pas de fonction anonyme aux événements. 
* Transformez votre application React en une PWA permettant aux utilisateurs de télécharger et d'installer votre application web localement sur leur appareil.
* Réduisez les charges utiles avec le fractionnement de code et le chargement paresseux. 
* Diminuez la taille des fichiers en utilisant gzip ou une compression similaire 
* Servez les images à partir d'un CDN 
* Activez la mise en cache via vos en-têtes http sur les réponses du serveur. 
* Optimisez les images. Voir le guide des fondamentaux de Google pour un guide complet sur la façon de le faire. 
* Utilisez le nouveau CSS Flexbox pour la mise en page. Évitez le [Layout Thrashing](https://developers.google.com/web/fundamentals/performance/rendering/avoid-large-complex-layouts-and-layout-thrashing) 
* N'utilisez que les transformations et l'opacité pour les changements CSS. Donc, au lieu de changer la hauteur et la largeur, utilisez scale X et scaleY 

Heureusement, beaucoup de ces optimisations, comme la minification et gzip, sont faites automatiquement lorsque vous exécutez la commande npm build sur un projet React.

##   
Conclusion

Merci d'avoir lu ! Si vous avez trouvé d'autres métriques créatives ou des moyens astucieux de suivre les utilisateurs, faites-le moi savoir dans les commentaires. 

> Suivez-moi sur Twitter pour plus de tutoriels à l'avenir : [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf) 

  


**Articles de blog :**  
[https://www.searchenginejournal.com/a-technical-seo-guide-to-lighthouse-performance-metrics/292703/#close](https://www.searchenginejournal.com/a-technical-seo-guide-to-lighthouse-performance-metrics/292703/#close)

[https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/)

[https://speedcurve.com/blog/user-timing-and-custom-metrics/](https://speedcurve.com/blog/user-timing-and-custom-metrics/)

[https://designsystem.digital.gov/performance/](https://designsystem.digital.gov/performance/)

[https://hackernoon.com/react-performance-primer-64fe623c4821](https://hackernoon.com/react-performance-primer-64fe623c4821) 

[https://reactjs.org/docs/optimizing-performance.html](https://reactjs.org/docs/optimizing-performance.html)  


**Observateurs :**  
[https://css-tricks.com/paint-timing-api/](https://css-tricks.com/paint-timing-api/)

[https://css-tricks.com/breaking-performance-api/](https://css-tricks.com/breaking-performance-api/)

[https://hackernoon.com/tracking-element-visibility-with-react-and-the-intersection-observer-api-7dfaf3a47218](https://hackernoon.com/tracking-element-visibility-with-react-and-the-intersection-observer-api-7dfaf3a47218)

[https://www.smashingmagazine.com/2018/01/deferring-lazy-loading-intersection-observer-api/](https://www.smashingmagazine.com/2018/01/deferring-lazy-loading-intersection-observer-api/)

[https://www.sitepen.com/blog/improving-performance-with-the-paint-timing-api/](https://www.sitepen.com/blog/improving-performance-with-the-paint-timing-api/)  


**Basé sur Google :**  
[https://developers.google.com/web/fundamentals/performance/user-centric-performance-metrics](https://developers.google.com/web/fundamentals/performance/user-centric-performance-metrics)

[https://developers.google.com/web/fundamentals/performance/navigation-and-resource-timing/](https://developers.google.com/web/fundamentals/performance/navigation-and-resource-timing/)

[https://developers.google.com/web/tools/chrome-devtools/speed/get-started](https://developers.google.com/web/tools/chrome-devtools/speed/get-started)

[https://marketingplatform.google.com/about/optimize/](https://marketingplatform.google.com/about/optimize/)

[https://developers.google.com/analytics/devguides/collection/analyticsjs/user-timings](https://developers.google.com/analytics/devguides/collection/analyticsjs/user-timings)

[https://support.google.com/analytics/answer/1033068#Anatomy](https://support.google.com/analytics/answer/1033068#Anatomy)

[https://developers.google.com/analytics/devguides/collection/analyticsjs/single-page-applications](https://developers.google.com/analytics/devguides/collection/analyticsjs/single-page-applications)

[https://support.google.com/analytics/answer/1033068](https://support.google.com/analytics/answer/1033068)

[https://docs.google.com/document/d/1GGiI9-7KeY3TPqS3YT271upUVimo-XiL5mwWorDUD4c/preview#](https://docs.google.com/document/d/1GGiI9-7KeY3TPqS3YT271upUVimo-XiL5mwWorDUD4c/preview#)

[https://www.doubleclickbygoogle.com/articles/mobile-speed-matters/](https://www.doubleclickbygoogle.com/articles/mobile-speed-matters/)