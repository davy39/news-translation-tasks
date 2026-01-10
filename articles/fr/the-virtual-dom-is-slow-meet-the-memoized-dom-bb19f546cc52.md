---
title: Le Virtual DOM est lent. Voici le Memoized DOM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-18T13:01:37.000Z'
originalURL: https://freecodecamp.org/news/the-virtual-dom-is-slow-meet-the-memoized-dom-bb19f546cc52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pwD6vakbORJiYCsD0NppHw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: vue
  slug: vue
seo_title: Le Virtual DOM est lent. Voici le Memoized DOM
seo_desc: 'By Sindre Osen Aarsaether

  Moving beyond the Virtual DOM and State Management


  The virtual DOM was a fantastic innovation. It brought about a much more productive
  way of writing web applications by allowing us to write our views in a declarative
  manne...'
---

Par Sindre Osen Aarsaether

#### Aller au-delà du Virtual DOM et de la gestion d'état

![Image](https://cdn-media-1.freecodecamp.org/images/hAPVXQJeNHcW4WTZqiRiAHQvAcyLP9HjEIDC)

Le Virtual DOM était une innovation fantastique. Il a apporté une manière beaucoup plus productive d'écrire des applications web en nous permettant d'écrire nos vues de manière déclarative.

Ce grand avantage a peu à voir avec la performance du rendu initial. Au lieu de cela, c'est le processus de mise à jour du DOM pour refléter les changements dans votre état qui est devenu beaucoup plus rapide.

Ce processus de synchronisation du DOM avec l'état est souvent appelé [réconciliation DOM](https://reactjs.org/docs/reconciliation.html).

Si nous avions un réconciliateur infiniment rapide, nous pourrions simplifier considérablement nos applications en **rendant tout à chaque frame**. La couche d'état n'aurait jamais besoin de connaître les vues, et encore moins d'envoyer des événements et de suivre quelles vues doivent réagir lorsque certaines parties de l'état changent. La vue serait toujours synchronisée avec les données, peu importe ce que vous lui lanciez.

Malheureusement, les implémentations du Virtual DOM ne sont _pas_ infiniment rapides. Elles sont, en fait, surprenamment lentes. Heureusement, beaucoup ont adopté l'immutabilité™, auquel cas le Virtual DOM vous remercie ! D'autres enveloppent tout l'état dans des observables (par exemple, mobx), et gardent une trace de quelle vue dépend de quel état. Cela vous permet de ne réconcilié que des parties de votre vue, mais cela vient avec son propre ensemble d'inconvénients.

Le plus gros problème est que nous avons tendance à décider comment gérer l'état de notre application en fonction de notre couche de vue. Et si nous pouvions obtenir des **meilleures** performances dans un monde où la couche de données et la couche de vue ne se connaissent pas ou ne se soucient pas vraiment l'une de l'autre ?

### Voici le Memoized DOM

[Imba](https://github.com/somebee/imba) est un langage de programmation pour le web. Il alimente la plateforme interactive de screencasting [scrimba.com](https://scrimba.com), dont je suis le développeur principal. Imba est né pour rendre le développement d'applications web amusant à nouveau. Il présente une syntaxe propre et lisible inspirée par Ruby. Il compile en JavaScript lisible et performant, et fonctionne dans l'écosystème existant.

![Image](https://cdn-media-1.freecodecamp.org/images/2SSQxsAdonLBrSsgBWEtRsC-CTjqS4VI9g8c)
_Toute la pile de scrimba.com est écrite en [Imba](http://imba.io/guides" rel="noopener" target="_blank" title="), mais le langage peut facilement être utilisé uniquement pour la couche de vue._

Outre une syntaxe propre et lisible, le plus grand avantage d'Imba est qu'il traite vraiment les éléments DOM comme des citoyens de première classe, à un niveau beaucoup plus profond que JSX. Il vous permet d'écrire des vues de manière déclarative, mais il **n'utilise pas de Virtual DOM**. Au lieu de cela, Imba compile les vues en un **Memoized DOM**, qui s'avère être **d'un ordre de grandeur plus rapide**.

#### Comment ça marche

L'idée générale est que nous créons des wrappers légers autour des éléments DOM, et compilons des vues déclaratives en chaînes de setters, chacun modifiant directement le DOM sous-jacent.

```jsx
tag AppView
    def render
        <self>
            <h1.title> "Welcome"
            <p.desc .red=(Math.random > 0.5)> "Roulette"
```

La vue Imba ci-dessus se compilera approximativement en le JavaScript suivant :

```jsx
class AppView extends Imba.Tag {
  render() {
    var $ = this.$; // cache en ligne pour la balise
    return this.setChildren($.$ = $.$ || [
      Imba.tag('h1',$).flag('title').setText("Welcome"),
      Imba.tag('p',$).flag('desc').setText("Roulette")
    ]).synced(
      $[1].flagIf('red',Math.random() > 0.5)
    );
  }
}
```

Ceci est un exemple _très_ simple pour illustrer le concept de base. Pendant la compilation, nous divisons la création et les mises à jour en branches séparées. La première fois que render est appelé pour un `<AppView>`, les enfants seront créés et les attributs statiques seront définis. Lors de tous les appels suivants, le seul travail réel que nous faisons est de basculer le className de notre <p>. Bien que beaucoup plus complexe, le même concept est utilisé pour les conditionnelles, les boucles, et tout le reste à l'intérieur des arbres de balises.

Si vous êtes intéressé par la manière dont cela fonctionne vraiment, je vous recommande de lire [cette introduction](http://imba.io/guides/advanced/performance#performance).

### Benchmark

> React est rapide, ont-ils dit. React est assez rapide, ont-ils dit. React Fiber sera assez rapide, ont-ils dit.

La plupart des benchmarks testent des choses comme "insérer/mélanger/supprimer 1000 lignes". Cela donne peu d'indication sur les performances dans le monde réel. Lorsqu'il y a des centaines de changements, la plupart des différences sont absorbées par les mutations DOM réelles, le repeint, etc. Cela ne mesure pas la métrique la plus importante.

Si vous voulez vraiment tester les performances de la réconciliation DOM, vous devez regarder à quelle vitesse l'implémentation synchronise le DOM avec l'état, **_surtout_ lorsqu'il y a peu ou pas de changements**.

Ainsi, pour capturer une vue réaliste des performances du réconciliateur, nous pourrions changer une petite partie de l'état de l'application à chaque itération, puis mesurer le temps qu'il faut pour forcer la synchronisation de la vue avec cet état modifié. La vue ne doit pas écouter aucune partie de l'état, et l'état ne doit pas avoir besoin de notifier qui que ce soit s'il a changé.

![Image](https://cdn-media-1.freecodecamp.org/images/TVVy8hfU5Sda4vHDAJRtYAWOUZxWC9X6FMzw)
_Capture d'écran de [dom-reconciler-bench](https://somebee.github.io/dom-reconciler-bench/index.html" rel="noopener" target="_blank" title=")_

[Ce benchmark](https://somebee.github.io/dom-reconciler-bench/index.html) parcourt une séquence déterministe d'altérations d'état, faisant au plus **un changement par itération**. Nous mesurons le temps qu'il faut pour réconcilié _toute la vue de l'application_ après :

1. Basculer l'achèvement d'une tâche
2. Supprimer une tâche
3. Insérer une tâche
4. Renommer une tâche
5. Ne rien faire

### Résultats

L'exécution du benchmark sur un iMac (4GHz i7) donne les résultats suivants :

#### Safari 11

* Imba 1.3 : **360458** ops / sec
* React 16.2 : **9752** ops / sec — **36.96x plus lent**
* Vue 2.5 : **8719** ops / sec — **41.34x plus lent**

#### Chrome 65

* Imba 1.3 : **282484** ops / sec
* React 16.2 : **8882** ops / sec — **31.81x plus lent**
* Vue 2.5 : **8103** ops / sec — **34.86x plus lent**

#### Firefox 58

* Imba 1.3 : **234334** ops / sec
* React 16.2 : **5075** ops / sec — **46.17x plus lent**
* Vue 2.5 : **3119** ops / sec — **75.13x plus lent**

Cela semble outrageant, n'est-ce pas ? Surement, cela ne peut pas être correct.

* Toutes les implémentations sont _vraiment_ en train de réconcilié à chaque étape.
* Toutes les implémentations sont bloquantes, synchrones et déterministes.
* Toutes les implémentations effectuent le même nombre de mutations DOM.
* Oui, nous utilisons la version de production minifiée de React. La version de développement est **200x plus lente** qu'Imba sur le même test.
* Le Memoized DOM ne crée pratiquement aucun déchet pendant une itération, utilise moins de mémoire en général, et est conceptuellement très simple.

Toutes les implémentations peuvent probablement être optimisées davantage. Je serais très heureux d'accepter des pull-requests sur [GitHub](https://github.com/somebee/dom-reconciler-bench). Pour être clair, j'ai un énorme respect pour ce que React a accompli, et j'aime vraiment Vue. Imba a tiré beaucoup d'inspiration de cela. Je soupçonne qu'il devrait être possible de compiler les templates Vue en utilisant une approche similaire, et j'aimerais que quelqu'un essaie !

### Profiling

Testons les performances brutes du réconciliateur lorsqu'il n'y a même aucun changement. Cela élimine le temps passé à faire des mutations DOM réelles de l'équation, et nous donne une bonne image de la quantité de travail qui se fait pendant la réconciliation. Le profil CPU graphique de Chrome donne une indication visuelle de la quantité de travail réduite avec la technique du Memoized DOM.

#### Imba 1.3

![Image](https://cdn-media-1.freecodecamp.org/images/nlYhyzt27JL8sd3ayEyVJiWTg1F0eTVMauLr)
_Imba complète 100000 itérations en 99.7ms — 5.1ms passés en GC_

#### React 16.2

![Image](https://cdn-media-1.freecodecamp.org/images/zUVYDsdcUzXcgRZ5ZdjlWMJtH5QN5wSWkIPw)
_React complète 100000 itérations en 8312.7ms (83.4x plus lent) — 100.4ms passés en GC_

#### Vue 2.5

![Image](https://cdn-media-1.freecodecamp.org/images/JU5nkcDdF25gJGK18rtJIwj0emDqdV7v0egC)
_Vue complète 100000 itérations en 8514.7ms (85.4x plus lent) — 308.4ms passés en GC_

### Est-ce que cela scale ?

> "Il y a BEAUCOUP, et je veux dire, BEAUCOUP de petits projets qui prétendent plus de vitesse, un développement plus facile, mais à y regarder de plus près, ils manquent généralement de fonctionnalités très importantes (comme les hooks de cycle de vie des modules) et, bien sûr, sans eux, la performance est plus élevée, mais la flexibilité d'utiliser ces bibliothèques au-delà d'une application de liste de tâches est limitée."

Ceci est une citation de quelqu'un qui a lu une ébauche précoce de cet article, et je voudrais le traiter de front. La différence de performance n'est pas limitée à un simple test, bien au contraire. [Imba](http://imba.io) a été utilisé en production pendant plusieurs années sur [scrimba.com](https://scrimba.com), mais il n'est toujours pas pour les timides. Pour la plupart des développeurs, les écosystèmes massifs pour Vue et React seront difficiles (et probablement imprudents) à laisser derrière. La [documentation Imba](http://imba.io/guides/essentials/introduction) laisse encore beaucoup à désirer, mais nous l'améliorons chaque jour.

### Est-ce que cela compte ?

Je suis sûr que vous avez entendu dire que React est assez rapide. Mais assez rapide pour quoi ? Cela n'a pas vraiment d'importance si React était 15 % plus rapide, mais avec une amélioration d'un ordre de grandeur, nous pouvons commencer à explorer des moyens plus simples de construire des applications.

![Image](https://cdn-media-1.freecodecamp.org/images/fLiP6wWOXcRKJ4ULiU-Cc6dqBoO2ePluCgSb)

Ce n'est pas une question de vitesse _perçue_, mais de ce que cela vous permet de faire. Sur [scrimba.com](https://scrimba.com), nous ne nous inquiétons pas de garder la vue synchronisée avec l'état. Nous ne nous inquiétons pas de suivre quand l'état a changé. Nos modèles de données ne sont pas observables. Nous rendons simplement. Quand nous voulons. **Et c'est libérateur.**