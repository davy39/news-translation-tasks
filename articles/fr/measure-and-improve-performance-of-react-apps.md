---
title: Comment mesurer et améliorer la performance d'une application React
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-03-27T17:18:19.000Z'
originalURL: https://freecodecamp.org/news/measure-and-improve-performance-of-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/nicolas-hoizey-poa-Ycw1W8U-unsplash.jpg
tags:
- name: performance
  slug: performance
- name: React
  slug: react
- name: web performance
  slug: web-performance
seo_title: Comment mesurer et améliorer la performance d'une application React
seo_desc: 'Hi everyone!

  React is a popular JavaScript library for building user interfaces. As applications
  built with React become more complex, their performance can start to degrade.

  Poor performance can lead to a frustrating user experience and a negative i...'
---

Salut à tous !

React est une bibliothèque JavaScript populaire pour créer des interfaces utilisateur. À mesure que les applications construites avec React deviennent plus complexes, leur performance peut commencer à se dégrader.

Une mauvaise performance peut mener à une expérience utilisateur frustrante et un impact négatif sur l'engagement des utilisateurs. Dans cet article, nous allons donc discuter de la manière de mesurer et d'améliorer la performance d'une application React.

# Table des matières

* [Comment définir la performance](#heading-comment-definir-la-performance)
    
* [Comment mesurer la performance](#heading-comment-mesurer-la-performance)
    
    * [React dev tools](#heading-react-dev-tools)
        
* [Comment améliorer la performance](#heading-comment-ameliorer-la-performance)
    
    * [Optimiser les images](#heading-optimiser-les-images)
        
    * [Code splitting et Lazy Loading](#heading-code-splitting-et-lazy-loading)
        
    * [Optimiser le DOM](#heading-optimiser-le-dom)
        
    * [Éviter les re-renders inutiles de composants](#heading-eviter-les-re-renders-inutiles-de-composants)
        
    * [Rendering patterns](#heading-rendering-patterns)
        
    * [CDNs](#heading-content-delivery-network-cdn)
        
* [Conclusion](#heading-conclusion)
    

# Comment définir la performance

En développement web, la "performance" se réfère généralement à la vitesse et à l'efficacité d'un site web ou d'une application web. Elle englobe plusieurs facteurs différents, notamment :

1. **Temps de chargement de la page :** Cela correspond au temps nécessaire pour qu'une page se charge complètement et affiche tout son contenu. Des temps de chargement plus rapides mènent généralement à une meilleure expérience utilisateur.
    
2. **Réactivité :** Cela se réfère à la vitesse à laquelle un site web répond aux interactions de l'utilisateur, comme cliquer sur un bouton ou scroller. Un site réactif semble fluide et rapide, ce qui peut également améliorer l'expérience utilisateur.
    
3. **Utilisation des ressources :** Il s'agit de la quantité de ressources serveur (telles que le CPU et la mémoire) qu'un site web utilise pour servir des pages et répondre aux requêtes. Un site bien optimisé utilisera les ressources efficacement, permettant au serveur de gérer plus de trafic tout en réduisant les coûts.
    
4. **Scalabilité :** Cela désigne la capacité d'un site web à gérer une augmentation du trafic et de la charge sans sacrifier la performance. Un site scalable peut gérer des pics soudains de trafic sans ralentir ni planter.
    

L'optimisation de la performance d'un site web est importante car elle peut impacter directement l'expérience utilisateur, le classement dans les moteurs de recherche et même les revenus de l'entreprise.

# Comment mesurer la performance

La première étape pour améliorer la performance d'une application React est de mesurer sa performance actuelle. Il existe plusieurs outils disponibles pour cela, notamment :

1. **Lighthouse** – [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=es) est un outil open-source de Google qui audite les pages web pour la performance, l'accessibilité, et plus encore. Lighthouse génère un rapport incluant des suggestions pour améliorer la performance de l'application.
    
2. **WebPageTest** – [WebPageTest](https://gercocca.vercel.app/) est un outil gratuit qui vous permet de tester la vitesse de votre site depuis plusieurs endroits dans le monde. WebPageTest fournit des rapports détaillés sur la performance de votre site, incluant des suggestions d'amélioration.
    
3. **Google PageSpeed Insights –** [Google PageSpeed Insights](https://pagespeed.web.dev/) analyse le contenu d'une page web et génère un rapport identifiant les opportunités d'amélioration de la performance de la page.
    

Ces trois outils fonctionnent fondamentalement de la même manière. Vous fournissez l'URL du site que vous souhaitez analyser, et les outils le parcourent pour vous fournir un rapport détaillé couvrant les opportunités d'amélioration en performance, mais aussi en accessibilité, SEO et bonnes pratiques générales.

Ces outils sont excellents pour obtenir une mesure objective de nos applications. Certains d'entre eux peuvent même être intégrés dans des pipelines CI/CD afin de surveiller l'impact des changements sur la performance au fil du temps.

## React dev tools

Un autre outil utile pour mesurer la performance dans une application React est le profiler de [React DevTools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi). React DevTools est une extension de navigateur qui vous permet d'inspecter et de déboguer des applications React dans les navigateurs Chrome, Firefox ou Edge.

Le "profiler" est un outil qui vous permet d'enregistrer l'activité de votre application et de générer ensuite un rapport montrant quels composants ont été rendus, combien de fois et quand chaque composant a été rendu, ainsi que la durée de chaque rendu.

C'est très utile pour détecter les re-renders inutiles de composants et les rendus qui prennent trop de temps, générant ainsi des goulots d'étranglement de performance.

Si vous souhaitez approfondir le fonctionnement du profiler, je recommande [cette vidéo](https://www.youtube.com/watch?v=00RoZflFE34&t=452s).

# Comment améliorer la performance

Maintenant que nous avons une idée de la façon d'identifier les problèmes de performance dans notre application, passons en revue certaines techniques d'optimisation que nous pouvons utiliser pour l'améliorer.

## Optimiser les images

Les images sont l'un des principaux coupables des sites web lents à charger. Vous pouvez optimiser les images en les compressant sans compromettre leur qualité. Des outils comme [tinyPng](https://tinypng.com/) peuvent compresser vos images et vous aider à réduire la taille de votre site web, et donc son temps de chargement.

Les meta-frameworks tels que Next viennent avec une optimisation d'image intégrée.

## Code splitting et Lazy Loading

Le Lazy Loading consiste à charger le contenu uniquement lorsqu'il est nécessaire, au lieu de tout charger d'un coup. Cela se fait grâce à ce qu'on appelle le **"code splitting"**. C'est une technique de bundling qui vous permet de diviser le code en plus petits chunks qui ne sont téléchargés qu'en cas de besoin, au lieu de télécharger l'intégralité du code lors du premier rendu.

Un exemple classique où cette technique s'avère utile est la navigation entre différentes routes. Disons que notre site web possède deux routes principales, "Accueil" (Home) et "Contact".

Nous ne voudrions télécharger le code lié à la page "Accueil" que lorsque nous sommes sur cette route, et le code "Contact" uniquement lorsque nous sommes sur l'autre route. Le code splitting nous permet de faire cela, aidant ainsi à réduire le temps de chargement initial de l'application et à améliorer l'expérience utilisateur.

Vous pouvez utiliser des outils tels que **React.lazy()** et **Suspense** pour implémenter le Lazy Loading dans votre application. Si vous voulez en savoir plus sur le fonctionnement de ces outils, [consultez cette vidéo](https://www.youtube.com/watch?v=JU6sl_yyZqs).

## Optimiser le DOM

La taille du Document Object Model (DOM) peut impacter la performance de l'application. Plus il est grand et complexe, plus il faudra de temps pour le charger et le modifier.

Vous pouvez optimiser le DOM en réduisant le nombre d'éléments, en supprimant les éléments inutiles et en minimisant l'utilisation des animations CSS.

### Éviter les re-renders inutiles de composants

Comme vous le savez peut-être, React est une bibliothèque qui nous permet de construire des interfaces utilisateur. Dans React, chaque partie de l'UI est représentée dans le code par un composant. Lorsqu'une partie de l'UI doit être modifiée, React re-rend le composant avec les informations mises à jour.

Deux choses déclenchent un re-render de composant : un changement d'état (state) ou un changement de props. Mais parfois, les composants peuvent se re-rendre inutilement, ce qui signifie qu'il n'y a aucun changement réel dans l'information à afficher.

Pour prévenir les re-renders inutiles, nous pouvons implémenter certaines des techniques suivantes :

* **Mémoïsation :** Dans React, la mémoïsation permet à un composant de "se souvenir" de la valeur de l'état et/ou des props qu'il reçoit. Avant de se re-rendre, il peut vérifier si la valeur a réellement changé. Si ce n'est pas le cas, il ne se re-rend pas. Cette technique peut être mise en œuvre via des hooks comme `useMemo` et `useCallback`. Si vous voulez approfondir ce point, [consultez cet article que j'ai écrit](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/).
    
* **Utiliser la prop key pour les listes :** Lors du rendu d'une liste d'éléments dans React, il est important de fournir une prop key unique pour chaque élément. Cela aide React à identifier quels éléments ont changé et doivent être re-rendus. Si vous ne fournissez pas de prop key, React utilisera l'index de l'élément dans le tableau, ce qui peut mener à des re-renders inutiles si l'ordre des éléments change.
    
* **Garder l'état aussi local que possible :** Par garder l'état local, j'entends que l'état qu'un composant utilise devrait être (quand c'est possible) au sein du composant lui-même ou aussi proche que possible dans l'arbre des composants. C'est parce que lorsqu'un composant se re-rend, tous ses composants enfants se re-rendent également. Ce n'est pas nécessairement une mauvaise chose, mais si nous pouvons l'éviter, nous devrions probablement le faire. Il n'est donc pas conseillé de centraliser tout l'état dans un seul composant parent, à moins que cet état ne doive être utilisé par plusieurs parties de l'application plus bas dans l'arbre. Voici [un excellent article à ce sujet](https://kentcdodds.com/blog/state-colocation-will-make-your-react-app-faster) si vous souhaitez en apprendre davantage.
    

## Rendering patterns

Une autre chose qui peut avoir un impact sur la performance de votre application est le rendering pattern (modèle de rendu) qu'elle utilise. Un rendering pattern se réfère à la manière dont le code HTML, CSS et JavaScript est traité et rendu dans une application ou un site web.

Différents modèles de rendu sont utilisés pour atteindre différents objectifs de performance et d'expérience utilisateur. Les modèles les plus courants en développement web sont :

1. **Client-side rendering (CSR)** : Dans le CSR, le navigateur du client génère le contenu HTML d'une page web côté client à l'aide de JavaScript. Cette approche peut fournir une expérience utilisateur rapide et interactive, mais peut être plus lente pour les temps de chargement initiaux et moins efficace pour le SEO.
    
2. **Server-side rendering (SSR)** : Dans le SSR, le serveur web génère le contenu HTML d'une page web côté serveur et l'envoie au navigateur du client. Cette approche peut améliorer les temps de chargement initiaux et le SEO (optimisation pour les moteurs de recherche), mais peut être plus lente pour le contenu dynamique.
    

Le Server-Side Rendering (SSR) peut aider à améliorer le temps de chargement initial de l'application en effectuant le rendu de la page initiale côté serveur. Cela peut aider à améliorer les métriques Time-to-Interactive (TTI) et First Contentful Paint (FCP). Vous pouvez utiliser des outils tels que Next.js ou Gatsby pour implémenter le SSR dans votre application.

Le choix du modèle de rendu dépend des besoins spécifiques et des exigences d'un projet, tels que la performance, le SEO, l'expérience utilisateur et la flexibilité. Si votre priorité est de fournir aux utilisateurs une expérience fluide et proche du natif, le CSR est probablement un bon choix. Si vous avez besoin de temps de chargement de page ultra-rapides, le SSR ou le SSG peut être une meilleure option.

Pour approfondir les modèles de rendu, consultez [cet article que j'ai récemment écrit](https://www.freecodecamp.org/news/rendering-patterns/).

## Content Delivery Network (CDN)

Un CDN, ou Content Delivery Network, est un système de serveurs ou de nœuds distribués qui travaillent ensemble pour livrer du contenu web, tel que des images, des vidéos et d'autres fichiers, aux utilisateurs en fonction de leur emplacement géographique.

Lorsqu'un utilisateur demande du contenu à un site web, le CDN servira le contenu depuis le serveur le plus proche de l'utilisateur, ce qui aide à réduire la latence et à améliorer la performance du site. Les CDNs peuvent également aider à réduire la charge sur le serveur d'origine d'un site web en mettant en cache le contenu fréquemment accédé et en le livrant depuis les serveurs du CDN au lieu du serveur d'origine.

Les CDNs sont normalement utilisés pour héberger du contenu statique (c'est-à-dire du contenu qui ne change pas fréquemment), comme des images, des vidéos, des articles de blog, etc. De plus, si vous utilisez la Static Site Generation (SSG) comme modèle de rendu, vous pourriez héberger vos sites rendus sur un CDN pour une livraison encore plus rapide.

Quelques exemples de CDNs populaires sont Cloudflare et Amazon CloudFront.

Pour plus de détails sur le fonctionnement des CDNs, consultez [cette superbe vidéo](https://www.youtube.com/watch?v=RI9np1LWzqw).

# **Conclusion**

Eh bien tout le monde, dans cet article, nous avons discuté de la manière de mesurer et d'améliorer la performance d'une application React.

Nous avons défini le concept de performance de site web, incluant le temps de chargement de la page, la réactivité, l'utilisation des ressources et la scalabilité, et nous avons esquissé comment mesurer la performance en utilisant des outils tels que Lighthouse, WebPageTest, Google PageSpeed Insights et les React dev tools.

Enfin, nous avons vu quelques techniques d'optimisation telles que l'optimisation des images, le code splitting et le lazy loading, l'optimisation du DOM, et l'évitement des re-renders inutiles de composants.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/03/AbsoluteAnnualKoi-size_restricted.gif align="left")