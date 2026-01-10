---
title: Comment optimiser la recherche en JavaScript avec le Debouncing
subtitle: ''
author: Ajay Yadav
co_authors: []
series: null
date: '2025-09-23T17:17:46.880Z'
originalURL: https://freecodecamp.org/news/optimize-search-in-javascript-with-debouncing
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758647563748/4f1c792d-5912-4bbb-9144-fcdda83d78ec.png
tags:
- name: JavaScript
  slug: javascript
- name: optimization
  slug: optimization
seo_title: Comment optimiser la recherche en JavaScript avec le Debouncing
seo_desc: 'A few months ago, my manager assigned me a task: implement a search functionality
  across an entire page. The tricky part was that the displayed text was shown in
  the form of prompts, and each prompt could be truncated after two lines.

  If the text exc...'
---

Il y a quelques mois, mon manager m'a confié une tâche : implémenter une fonctionnalité de recherche sur l'ensemble d'une page. Le point délicat était que le texte affiché se présentait sous forme de prompts, et chaque prompt pouvait être tronqué après deux lignes.

Si le texte dépassait la limite, un bouton de fractionnement apparaissait, permettant aux utilisateurs d'ouvrir le prompt complet dans une section de vue fractionnée séparée (voir l'illustration ci-dessous pour mieux comprendre).

![Une interface noire avec une barre de recherche en haut à gauche, une note de 5/10 et des flèches de navigation. En dessous se trouvent quatre zones de texte avec des extraits de texte factice. À droite se trouve une explication détaillée de \"Lorem Ipsum\", abordant son histoire dans l'industrie de l'imprimerie et de la mise en page. Le numéro de page est 1 sur 7 sur 12.](https://cdn.hashnode.com/res/hashnode/image/upload/v1757771259264/66158a97-07d1-4b4f-ad24-c57c62a498ae.png align="center")

Maintenant, si l'exigence n'avait été que du texte brut, j'aurais pu résoudre le problème avec une simple recherche basée sur les regex. En fait, à l'intérieur de la vue fractionnée elle-même, j'ai initialement utilisé une approche regex pour la recherche ainsi que la navigation vers les correspondances. Cela fonctionnait parfaitement.

Puisque j'avais déjà une fonction d'aide à la recherche opérationnelle, j'ai pensé : \"Pourquoi ne pas la réutiliser également pour la recherche globale ?\"

Eh bien, j'ai essayé. Mais cette fois, l'interface utilisateur a commencé à ralentir chaque fois que je cliquais sur les boutons suivant/précédent dans la barre de recherche. Même les contrôles de pagination en haut à droite ralentissaient pendant la navigation. Pour trouver une meilleure approche, je me suis tourné vers des outils d'IA pour faire du brainstorming et je suis tombé sur plusieurs idées et concepts.

En tant que développeurs, nous utilisons Google quotidiennement, et naturellement, je suis devenu curieux de savoir comment fonctionne la recherche de Google sous le capot. J'ai ouvert les Chrome DevTools, j'ai commencé à taper dans la barre de recherche de Google, et j'ai remarqué quelque chose d'intéressant.

Alors que Google Search met à jour les résultats en temps réel à chaque frappe, nous n'avons pas la puissance des serveurs de Google. Dans nos applications, le debouncing est un moyen pratique d'éviter les appels API inutiles et d'améliorer les performances. Cette idée correspondait exactement à ce que ChatGPT m'avait suggéré plus tôt.

J'ai donc appliqué une approche similaire à mon projet et j'ai finalement livré la fonctionnalité en utilisant le debouncing, ainsi que des hooks React comme `useTransition` et `useDeferredValue`. C'est ainsi qu'est née l'idée de cet article.

Dans cet article, je vais vous montrer comment optimiser les performances de votre application en implémentant la technique du debounce.

## Table des matières

* [Le problème sans Debouncing](#heading-le-probleme-sans-debouncing)
    
* [Qu'est-ce que le Debouncing](#heading-qu-est-ce-que-le-debouncing) ?
    
* [Comment implémenter le Debouncing en JavaScript](#heading-comment-implementer-le-debouncing-en-javascript)
    
* [Avantages de l'utilisation du Debouncing dans la recherche](#heading-avantages-de-l-utilisation-du-debouncing-dans-la-recherche)
    
* [Erreurs courantes à éviter](#heading-erreurs-courantes-a-eviter)
    
* [Conclusion](#heading-conclusion)
    
* [Avant de terminer](#heading-avant-de-terminer)
    

Entrons dans le vif du sujet.

## Le problème sans Debouncing

Imaginez que vous construisez une barre de recherche qui récupère des résultats à partir d'une API. Chaque fois que l'utilisateur tape une lettre, la barre de recherche effectue immédiatement une nouvelle requête.

Si quelqu'un tape le mot \"JavaScript\", cela signifie que 10 appels API distincts seront lancés — un pour chaque caractère.

![la page de recherche Google avec \"javascript\" dans la zone de saisie](https://cdn.hashnode.com/res/hashnode/image/upload/v1758013146153/204187ef-1757-490b-8b29-7d11951c88b3.png align="center")

Maintenant, dans Google Search, les résultats se mettent à jour en temps réel à chaque frappe. Mais contrairement à Google, nous ne disposons pas d'une infrastructure massive pour gérer cette charge. Dans la plupart des applications, lancer une requête pour chaque caractère devient rapidement inefficace.

Au début, cela peut ne pas sembler grave, mais en pratique, cela mène à des problèmes sérieux. Le navigateur doit gérer un flux de requêtes inutiles, le serveur est surchargé par des appels répétés, et l'utilisateur se retrouve avec une expérience lente ou incohérente. Toute l'interface semble lourde et peu réactive.

C'est exactement la situation dans laquelle je me suis trouvé lorsque j'ai réutilisé ma simple fonction de recherche basée sur les regex pour la recherche globale. Elle fonctionnait bien pour un petit prompt à l'intérieur de la vue fractionnée, mais appliquée à plus grande échelle avec des boutons de navigation et une pagination, l'interface utilisateur a commencé à se figer et à ralentir.

## Qu'est-ce que le Debouncing ?

Le debouncing est une technique, pas une fonctionnalité du langage de programmation. C'est simplement un moyen de contrôler la fréquence d'appel d'une fonction. Au lieu d'exécuter la fonction à chaque fois qu'un événement se produit, vous retardez son exécution.

Si l'événement continue de se déclencher pendant ce délai, le minuteur est réinitialisé. La fonction ne s'exécute que lorsque l'utilisateur fait enfin une pause.

Pensez à la saisie dans une barre de recherche. Sans debouncing, l'application ferait une requête pour chaque frappe. Avec le debouncing, l'application attend que l'utilisateur arrête de taper pendant un court instant — disons 300 millisecondes — puis effectue une seule requête avec la saisie finale.

En coulisses, cela est généralement implémenté avec `setTimeout` et `clearTimeout`. Un minuteur démarre lorsque l'événement se produit, et si un autre événement survient avant la fin du minuteur, celui-ci est effacé et redémarré. La fonction ne s'exécute que lorsque l'utilisateur cesse de taper pendant le délai spécifié.

## Comment implémenter le Debouncing en JavaScript

Comme je l'ai mentionné plus tôt, le debouncing n'est lié à aucun langage de programmation spécifique. C'est simplement un concept qui peut être implémenté à l'aide de minuteurs. En JavaScript, nous utilisons généralement `setTimeout` et `clearTimeout` pour y parvenir.

Voici un exemple simple d'une fonction de debounce en JavaScript :

```javascript
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}
```

Nous commençons par une fonction `debounce` qui prend deux arguments :

* `fn` est la fonction que nous voulons contrôler, comme l'appel API.
    
* `delay` est le temps que nous voulons attendre avant d'exécuter réellement `fn`.
    

À l'intérieur, nous déclarons une variable `timer`. Celle-ci contiendra la référence au `setTimeout`.

La fonction `debounce` renvoie ensuite une autre fonction. Cette fonction renvoyée est celle qui s'exécutera réellement chaque fois qu'un événement (comme la saisie dans l'input ou un appel API) se produit.

Chaque fois que l'utilisateur tape, la première chose que vous faites est `clearTimeout(timer)`. Cela annule tout appel de fonction précédemment programmé. Ensuite, vous créez un nouveau délai avec `setTimeout`.

Si l'utilisateur continue de taper avant la fin du délai, l'ancien minuteur est effacé et redémarré. Ce n'est que lorsqu'il fait une pause assez longue que le délai se termine et que `fn` est exécuté.

Avez-vous remarqué comment j'ai utilisé `fn.apply(this, args)` ? C'est juste une manière sûre d'appeler la fonction d'origine avec le bon contexte `this` et de transmettre tous les arguments.

Voici comment l'utiliser en pratique :

```javascript
function fetchResults(query) {
  console.log("Récupération des résultats pour :", query);
  // Ici, vous pourriez appeler votre API
}

// Envelopper avec debounce
const debouncedSearch = debounce(fetchResults, 300);

// Attacher à l'événement input
const input = document.getElementById("search");
input.addEventListener("input", (e) => {
  debouncedSearch(e.target.value);
});
```

1. `fetchResults` est notre fonction de recherche réelle. Normalement, elle s'exécuterait à chaque frappe.
    
2. Nous l'enveloppons avec `debounce` et définissons un délai de 300 ms. Cela signifie qu'elle ne s'exécutera pas tant que l'utilisateur ne s'arrête pas de taper pendant 300 ms.
    
3. À chaque événement `input`, au lieu d'appeler directement `fetchResults`, nous appelons `debouncedSearch`. Cela garantit que seule la version debouncée de la fonction s'exécute.
    

Ainsi, si un utilisateur tape \"hello\", au lieu de cinq appels API, un seul ou deux seront lancés une fois qu'il aura fait une pause.

## Avantages de l'utilisation du Debouncing dans la recherche

L'utilisation du debouncing dans une fonctionnalité de recherche peut sembler être une petite optimisation, mais elle a un impact majeur. L'avantage le plus évident est la performance.

Au lieu de faire une requête pour chaque frappe, votre application attend que l'utilisateur fasse une pause, ce qui économise les ressources du navigateur et du serveur. L'interface utilisateur semble beaucoup plus fluide car elle n'est pas constamment interrompue par des appels inutiles.

Le debouncing améliore également la scalabilité. Si des centaines ou des milliers d'utilisateurs tapent en même temps, vous réduisez considérablement le nombre d'appels API gaspillés. Cela signifie que votre backend peut gérer plus d'utilisateurs sans être surchargé.

Il y a aussi un avantage indirect pour le SEO et l'analytique. Lorsque votre application est performante et réactive, les utilisateurs restent plus longtemps, interagissent davantage et le taux de rebond diminue. Ce type de réactivité peut faire une grande différence dans la façon dont les gens perçoivent la qualité de votre produit.

## Erreurs courantes à éviter

Bien que le debouncing soit puissant, les développeurs commettent souvent quelques erreurs. Un problème courant est de définir un délai trop élevé. Si vous faites attendre les utilisateurs une ou deux secondes avant de voir les résultats, la recherche semblera peu réactive.

D'un autre côté, un délai trop court peut ne pas réduire suffisamment les appels pour être utile. Le juste milieu se situe généralement entre 300 et 500 millisecondes, mais cela dépend de votre cas d'utilisation.

Une autre erreur consiste à oublier d'effacer les anciens minuteurs. Sans effacement, votre application pourrait encore exécuter des appels plus anciens et obsolètes, ce qui peut entraîner des bugs ou des fuites de mémoire. C'est pourquoi `clearTimeout` est tout aussi important que `setTimeout` dans toute fonction de debounce.

Il est également important de penser aux cas limites. Que se passe-t-il si la saisie est effacée rapidement ? Ou si quelqu'un colle une longue chaîne de caractères au lieu de taper ? Tester ces cas garantit que votre fonction de debounce fonctionne correctement dans des scénarios réels.

## Conclusion

Lorsque j'ai été confronté pour la première fois au défi de construire une recherche globale, je pensais pouvoir simplement réutiliser ma solution de base basée sur les regex. Cependant, l'interface utilisateur a vite commencé à ramer et l'expérience utilisateur s'est dégradée. Il est surprenant de voir comment un si petit concept peut avoir un impact significatif sur les performances.

Le debouncing garantit que vos fonctions s'exécutent au bon moment, et non à chaque fois. Que vous construisiez une simple application JavaScript ou que vous travailliez avec React et Next.js, cette technique aide à réduire les appels inutiles, améliore les performances et maintient la scalabilité de votre application.

Ainsi, la prochaine fois que vous construirez une barre de recherche, rappelez-vous : ne vous contentez pas de la faire fonctionner, rendez-la efficace.

## Avant de terminer

J'espère que vous avez trouvé cet article instructif. Je suis Ajay Yadav, développeur logiciel et créateur de contenu.

Vous pouvez me suivre sur :

* [Twitter/X](https://x.com/atechajay) et [LinkedIn](https://www.linkedin.com/in/atechajay/), où je partage des conseils pour vous aider à vous améliorer de 0,01 % chaque jour.
    
* Consultez mon [GitHub](https://github.com/ATechAjay) pour plus de projets.
    
* Je gère également une [chaîne YouTube](http://youtube.com/@atechajay) en hindi où je partage du contenu sur les carrières, l'ingénierie logicielle et la rédaction technique.
    

On se retrouve dans le prochain article — d'ici là, continuez d'apprendre !