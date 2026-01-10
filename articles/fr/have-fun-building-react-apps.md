---
title: Comment s'amuser en construisant des applications React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-12-19T21:41:26.000Z'
originalURL: https://freecodecamp.org/news/have-fun-building-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/mugshotbot.com_customize_color-teal-discounted_price--image-fa229fca-mode-light-pattern-charlie_brown-price--theme-e_commerce-url-https___gifcoins.io.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment s'amuser en construisant des applications React
seo_desc: "Building React apps can either be a very fun experience or a very difficult\
  \ and tedious one, based off of the tools you choose.  \nReact is a JavaScript library\
  \ that, unlike frameworks like Angular, leave us to making a lot of decisions on\
  \ our own. Yo..."
---

Construire des applications React peut être une expérience très amusante ou très difficile et fastidieuse, selon les outils que vous choisissez. 

React est une bibliothèque JavaScript qui, contrairement à des frameworks comme Angular, nous laisse prendre beaucoup de décisions par nous-mêmes. Vous devez choisir quels outils et bibliothèques vous souhaitez utiliser pour alimenter vos projets React. 

Je souhaite partager avec vous mes cinq meilleurs choix pour construire des applications React. Je crois que ceux-ci vous permettront de vivre une expérience plus amusante en rendant le développement de votre application plus facile, plus rapide et, surtout, plus simple. 

## Vous voulez construire une application web ? Utilisez Next.js

Probablement le choix le plus important que vous puissiez faire dans la construction d'une application React est de décider si vous utilisez un framework React ou non. 

Il existe de nombreux frameworks React différents sur le marché, tels que Gatsby et Redwood.js, pour n'en nommer que quelques-uns. 

Cependant, Next.js continue d'être une option tout aussi excellente pour les applications full-stack et les sites statiques. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-19-at-2.45.12-PM.png)
_nextjs.org, le site officiel de documentation pour Next.js_

Besoin de construire une application full-stack avec un serveur Node ? Next.js vous offre des routes API prêtes à l'emploi, ce qui vous permet simplement de déposer un point de terminaison API dans votre répertoire de pages qui sera exécuté comme une fonction serverless. 

Vous voulez construire un site statique qui récupère des données depuis un CMS ? Pas de problème. Next vous offre la génération de sites statiques pour demander ces données au moment de la construction et exporte votre site en HTML, CSS et JavaScript simples. 

Next.js fait le travail difficile pour toutes sortes de tâches essentielles que vous rencontrerez lors de la construction de votre application. 

Par exemple, Next.js vous offre des outils pour...

* Intégrer facilement TypeScript
* Pré-charger des polices personnalisées (@next/font)
* Gérer le routage simple et dynamique
* Rendre votre contenu côté serveur
* Utiliser des variables d'environnement avec une configuration zéro
* Ajouter des redirections, réécritures et en-têtes personnalisés

Tout cela et bien plus est disponible via la bibliothèque npm `next`. La raison pour laquelle il est judicieux de construire avec Next est qu'il y a beaucoup de choses que Next.js fournit et auxquelles vous n'avez même pas encore pensé. 

Malgré le fait d'être un framework assez complet, Next.js ne sera pas la seule dépendance dont vous aurez besoin. Par exemple, Next.js ne fournit pas d'authentification. Cependant, il existe des outils formidables tels que `next-auth` et Blitz.js qui vous offriront une authentification facile avec Next. 

Si Next.js ne peut pas faire quelque chose pour vous directement, vous pouvez toujours trouver de nombreuses solutions sur le site web de Next.js (plus une excellente documentation) pour presque tout ce dont votre application React aura besoin. 

## Besoin de récupérer des données ? Utilisez React Query

Si vous effectuez une quelconque récupération de données dans votre application, vous devriez utiliser React Query. 

Notez que la bibliothèque est appelée @tanstack/react-query pour la version 4 de React Query. 

React Query est une bibliothèque très puissante qui nous permet de récupérer des données ou de gérer tout type d'opération asynchrone en utilisant un ensemble de hooks personnalisés, notamment `useQuery` et `useMutation`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-19-at-2.43.30-PM.png)
_React Query, également connu sous le nom de TanStack Query_

Le but de React Query est de rendre la récupération de données (appelée _querying_) et la mise à jour des données (_mutating_) une expérience agréable et beaucoup plus facile qu'elle ne l'était dans le passé. 

Auparavant, vous auriez peut-être récupéré des données ou effectué une sorte d'action asynchrone dans le hook useEffect. Le problème de le faire dans la plupart des cas est que cette opération sera toujours effectuée au montage du composant. Cela signifie que si votre composant est chargé dans une page particulière, cette opération sera effectuée chaque fois que la page se charge. 

```js
import { useQuery } from '@tanstack/react-query'

function App() {
  const info = useQuery({ queryKey: ['todos'], queryFn: fetchTodoList })
}
```

L'inconvénient est que vous effectuez probablement cette opération bien plus que nécessaire. Si vous récupérez des données et que les données ne changent pas, quel est l'intérêt de les récupérer à nouveau ? 

C'est là que React Query intervient. En nous donnant un bien meilleur contrôle sur notre récupération de données, nous sommes en mesure de spécifier quand nous voulons récupérer et ré-interroger une requête. 

De plus, si nous récupérons des données et qu'elles ont changé, React Query donnera par défaut les données mises en cache en premier, qui sont ensuite remplacées par les nouvelles données. L'avantage de cela est que nous n'avons pas à voir un indicateur de chargement chaque fois que les données que nous récupérons changent. 

En bref, React Query nous donne un contrôle total sur les données externes au sein de notre application et nous offre un cache pratique avec des valeurs par défaut sensées afin que nous ayons une bien meilleure expérience pour nos utilisateurs avec beaucoup moins d'indicateurs de chargement. 

Il y a une petite courbe d'apprentissage avec React Query, mais une fois que vous vous y êtes habitué, vous vous demanderez comment vous avez pu construire une application React sans lui. 

## Besoin de gérer l'état ? Utilisez Zustand

Gérer l'état dans le passé nécessitait généralement l'installation de la bibliothèque Redux une fois que votre projet avait atteint une certaine taille. 

Redux est toujours une excellente bibliothèque avec l'ajout quelque peu récent de Redux Toolkit. Cependant, dans la plupart des cas, Redux peut être plus sophistiqué que ce dont vous avez besoin. 

Zustand est une bibliothèque qui rend la gestion de l'état global et des applications React extrêmement simple. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-107.png)
_Bibliothèque de gestion d'état Zustand_

Tout ce que vous avez à faire pour gérer une certaine valeur est d'importer le package zustand, créer un store (qui est simplement un appel de fonction qui accepte un objet), placer la propriété que vous souhaitez gérer sur cet objet, et utiliser ce store comme un hook dans toute votre application. C'est tout ! 

```js
import create from 'zustand'

const useCounterStore = create({ count: 0 })
```

Mettre à jour cet état est aussi simple que d'utiliser la fonction interne `set`. Avec elle, nous pouvons créer des méthodes sur cet objet qui nous permettent de mettre à jour n'importe quelle valeur d'état comme nous le souhaitons. C'est vraiment aussi simple que cela. 

```js
import create from 'zustand'

const useCounterStore = create((set, get) => ({ 
  count: 0,
  increaseCount: get().count + 1 // augmente la valeur du compteur de 1
}))
```

Le grand avantage d'utiliser Zustand est qu'il ne nécessite aucun fournisseur – vous n'avez pas besoin d'envelopper quoi que ce soit autour de votre arbre de composants React. De plus, cet état peut être consommé dans n'importe quel composant React, même en dehors de vos composants React entièrement. 

Zustand vous donne également le contrôle sur la manière dont vos composants se mettent à jour en réponse à un changement d'état. Si cela ne vous dérange pas que vos composants se re-rendent à chaque changement d'état, vous pouvez récupérer l'état entier :

```js
const state = useCounterStore()
```

Cependant, si vous souhaitez mettre à jour un composant uniquement lorsqu'une valeur particulière change, vous pouvez sélectionner la partie de l'état que vous souhaitez :

```js
const count = useCounterStore((state) => state.count)
```

Zustand prend ce qui est fondamentalement intimidant – gérer l'état partagé entre de nombreux composants différents – et le transforme en une expérience très simple et même agréable grâce à sa syntaxe facile et ses nombreuses commodités. 

## Vous voulez des animations ? Utilisez Framer Motion

Peut-être la partie la plus amusante de toute application est l'ajout d'effets visuels comme des transitions et des animations. Framer Motion rend le processus de développement de toute sorte de transition et d'animation facile. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-19-at-3.19.40-PM.png)
_Framer Motion (framer.com/docs)_

Framer Motion est un package qui vous permet de faire des animations vraiment impressionnantes de presque n'importe quel type. Qu'il s'agisse de transitions simples, de gestes ou d'animations de mise en page complexes, Framer vous couvre. 

%[https://codesandbox.io/embed/framer-motion-animate-on-state-update-ns67ib?fontsize=14&hidenavigation=1&theme=dark]

L'avantage d'utiliser Framer Motion est qu'il fournit une API déclarative très simple pour la manière dont vous souhaitez que votre animation se déroule. 

Pour utiliser Framer, vous remplacez simplement l'élément JSX que vous souhaitez animer, comme un `div` par `motion.div`. 

Une fois que nous utilisons ce composant motion spécial, nous pouvons lui passer un certain nombre de props qui contrôlent l'animation. La seule prop dont nous avons vraiment besoin, cependant, pour animer nos composants est la prop `animate`. 

```jsx
<motion.div animate={{ x: 100 }} />
```

Cette prop nous permet également de définir quelle sera sa position initiale, comment elle s'animera et, si elle quitte le DOM, à quoi ressemblera l'animation de sortie. 

Framer nous donne les mêmes contrôles que les animations CSS simples, comme la capacité de retarder l'animation ou de choisir sa courbe d'accélération. De plus, il offre beaucoup plus d'options grâce à des hooks et composants personnalisés, ainsi que des valeurs spéciales que nous pouvons définir. 

Avec Framer Motion, nous pouvons :

* Animer lorsque les composants sont réorganisés avec le composant `Reorder`
* Créer des animations liées au défilement avec `useScroll`
* Animer les animations de sortie avec le composant `AnimatePresence`
* Créer des animations de type ressort avec le hook `useSpring`
* Ajouter des contrôles de glisser-déposer avec le hook `useDragControls`
* Animer des éléments dans un espace 3D avec le package `framer-motion-3d`

En un mot, si vous cherchez à rendre facilement votre application React visuellement impressionnante, vous vous devez de vérifier Framer Motion. 

## Vous voulez construire une application native ? Utilisez Capacitor.js

Il est logique d'envisager d'utiliser React Native si vous souhaitez construire une application native en tant que développeur React. React Native est une excellente bibliothèque pour construire des applications iOS et Android avec une syntaxe très similaire à celle de tout projet web React traditionnel. 

Il existe certaines bibliothèques qui peuvent vous permettre de partager du code entre vos projets React et React Native si vous souhaitez construire une application web et native, comme React Native web. 

Cependant, il n'existe vraiment qu'une seule bibliothèque qui vous permettra de construire de vraies applications React multiplateformes avec une seule base de code. Cette bibliothèque est Capacitor.js. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-19-at-3.20.19-PM.png)
_Capacitor.js_

Capacitor.js est une solution clé en main pour que votre application web fonctionne sur des plateformes natives. En d'autres termes, il permet à votre application d'être déployable sur les magasins d'applications pour fonctionner sur des appareils natifs, mais ne nécessite pas que vous modifiiez votre code existant s'il a déjà été conçu pour le web. 

Pour utiliser Capacitor, vous devez simplement installer quelques packages, `@capacitor/core` et `@capacitor/cli`. Capacitor vous donnera de nombreuses API natives pour fournir toutes les fonctionnalités qu'une application native standard aurait, comme les notifications push ou le retour haptique. 

Capacitor vous permet de transformer votre application web en une application native avec toutes les fonctionnalités d'une application native. Capacitor est l'une de ces solutions impressionnantes qui peuvent vraiment changer les limites de votre application pour pouvoir servir un type d'utilisateur complètement différent et exister dans un espace complètement différent si vous le choisissez. 

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même. 

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais souhaité avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*