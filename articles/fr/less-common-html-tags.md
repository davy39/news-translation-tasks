---
title: Balises HTML moins courantes que vous devriez connaître – Avec des exemples
  de code
subtitle: ''
author: Murtuzaali Surti
co_authors: []
series: null
date: '2024-01-29T14:00:55.000Z'
originalURL: https://freecodecamp.org/news/less-common-html-tags
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Exotic-HTML-TAGS-1.png
tags:
- name: HTML
  slug: html
seo_title: Balises HTML moins courantes que vous devriez connaître – Avec des exemples
  de code
seo_desc: "There are only so many HTML tags that people typically use when building\
  \ websites. \nBut as there are over 100+ HTML elements, I wondered if there were\
  \ any more beginner-friendly tags that I didn't know about – and that others might\
  \ find useful, too. ..."
---

Il n'existe [qu'un nombre limité de balises HTML](https://css-tricks.com/average-web-page-data-analyzing-8-million-websites/) que les gens utilisent généralement pour construire des sites web.

Mais comme il existe plus de 100 éléments HTML, je me suis demandé s'il existait d'autres balises adaptées aux débutants que je ne connaissais pas – et que d'autres pourraient également trouver utiles.

Après avoir fait quelques recherches, j'ai compilé cette collection de balises HTML moins connues, mais toujours très utiles.

![un bébé lisant un livre intitulé "HTML pour les bébés"](https://www.freecodecamp.org/news/content/images/2023/12/html-for-babies-imgur.png)
_Source : imgur_

## 1. L'élément `<base>`

Lorsque vous définissez l'attribut `href` sur une balise `a` avec une URL relative, l'URL de base par défaut qu'elle considère est l'URL `location.href`.

Vous pouvez remplacer ce comportement en définissant cette balise au-dessus de tous les éléments HTML qui traitent des URL relatives.

Par exemple, si je fais ceci :

```html
<head>
    <base href="https://syntackle.live" />
</head>
<body>
    <a href="/contact/">Contact</a>
</body>
```

alors, l'URL href pour la balise `a` sera `https://syntackle.live/contact/`.

Gardez à l'esprit qu'il ne peut y avoir qu'une seule balise `<base>` par page. Si vous définissez plusieurs balises `<base>`, seule la première sera prise en compte.

Vous n'aurez pas besoin de cet élément la plupart du temps, mais si vous avez l'impression que toutes les URL d'une page pointent vers un autre site, alors le déclarer est bénéfique.

## 2. L'élément `<aside>`

Vous pouvez utiliser cet élément pour tout contenu non directement lié au contenu principal de la page. Il est bien adapté pour afficher des publicités, des articles connexes, du contenu promotionnel, des citations en bloc, des éléments de navigation, etc.

```html
<main>
    <h2>Article</h2>
    <p>Cet article parle d'une race de chiens.</p>
    <aside>
        <p>En savoir plus sur les chats.</p>
    </aside>
</main>
```

Par exemple, dans l'extrait ci-dessus, l'article parle principalement de chiens et de leurs races. Mais si vous avez écrit un article sur les chats et que vous souhaitez y faire référence depuis l'article sur les chiens, vous pourriez utiliser l'élément `aside` pour le mentionner. Le contenu dans l'élément `aside` peut être indirectement lié à la page.

La spécification HTML fournit [de bons exemples sur la façon d'utiliser l'élément `<aside>`](https://html.spec.whatwg.org/multipage/sections.html#the-aside-element).

## 3. L'élément `<search>`

Vous pouvez utiliser l'élément `<search>` comme conteneur pour les éléments traitant de la recherche ou du filtrage. Par exemple, un formulaire envoyant une requête POST pour obtenir des résultats de recherche ou un composant de recherche reposant sur JavaScript pour le filtrage.

```html
// composant de recherche reposant sur JavaScript
<search>
    <input type="text" id="searchInput">
    <div id="results"></div>
</search>
```

Voici un autre exemple :

```html
<search>
    <form action="search.js" method="POST">
        <input type="text" id="searchInput">
        <button type="submit">Rechercher</button>
    </form>
</search>
```

Dans les deux exemples ci-dessus, les éléments enveloppés dans l'élément `search` jouent un rôle dans la fonctionnalité de recherche d'un site.

Vous devriez utiliser cet élément car il fournit une valeur sémantique au navigateur et aux outils d'accessibilité tels que les lecteurs d'écran.

## 4. L'élément `<q>`

La plupart des gens utilisent simplement des guillemets `(")` pour citer quelque chose. Mais il existe une balise HTML dédiée pour cela. En l'utilisant, vous pouvez citer quelque chose d'une autre source et, en définissant son attribut `cite`, vous pouvez également lier à cette source.

```html
<q cite="https://another-source.com">Ceci est une citation d'une autre source.</q>
```

Cependant, selon la spécification HTML :

> L'utilisation des éléments q pour marquer les citations est entièrement facultative ; l'utilisation d'une ponctuation de citation explicite sans éléments q est tout aussi correcte. - [html.spec.whatwg.org](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-q-element)

## 5. L'élément `<var>`

Si vous traitez des mathématiques dans votre page web, expliquez un concept ou résolvez un problème, alors cet élément peut être utile lorsque vous mentionnez des variables tout en décrivant le problème.

```html
<p>Ce sont trois variables, <var>a</var>, <var>b</var> et <var>c</var><sup>2</sup>.</p>
```

![varElement](https://www.freecodecamp.org/news/content/images/2024/01/varElement.PNG)

Vous pouvez utiliser cet élément pour montrer une représentation visuelle de variables connues ou inconnues, comme montré ci-dessus.

## 6. L'élément `<samp>`

Cet élément représente la sortie d'un autre logiciel ou système informatique. Il existe également un élément [`kbd`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-kbd-element) (utilisé pour afficher les entrées utilisateur) qui est visuellement similaire à cet élément.

Vous pouvez utiliser cet élément pour afficher la sortie de la console ou la sortie d'un programme informatique.

```html
<pre>
    <code class="language-javascript">console.log(1 + 2)</code>
    <samp>3<samp>
</pre>
```

## 7. L'élément `<datalist>`

Vous êtes peut-être familier avec l'élément `select` qui vous permet de fournir aux utilisateurs une série d'options parmi lesquelles choisir. Un élément similaire est l'élément `datalist`.

La seule différence entre eux est que l'élément datalist fournit des suggestions au lieu d'un ensemble fini d'options. Les utilisateurs peuvent également saisir leur propre entrée si aucune des suggestions ne correspond à leurs exigences, alors que lors de l'utilisation de l'élément select, les utilisateurs doivent choisir parmi la liste d'options dans le menu déroulant.

Vous pouvez utiliser `<datalist>` avec l'élément `input` afin que l'utilisateur puisse taper ce qu'il veut. Ensuite, si cela correspond aux valeurs dans la datalist, l'utilisateur peut sélectionner cette valeur.

Pour lier l'élément input à la datalist, vous devrez utiliser un attribut `list` sur l'élément input. La valeur de l'attribut list doit être l'`id` de la datalist.

```html
<label>
    Voitures :
    <input name=car list="cars">
    <datalist id=cars>
        <option value="Ferrari">
        <option value="Mercedes">
    </datalist>
</label>
```

Il prend en charge différents types d'entrées, mais il présente une [compatibilité partielle avec les navigateurs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist#browser_compatibility).

## 8. L'élément `<progress>`

L'élément de progression natif en HTML, comme son nom l'indique, est utilisé pour suivre la progression d'une tâche.

Vous pouvez utiliser cet élément de deux manières : de manière déterminée ou indéterminée. Une barre de progression déterminée sait où elle se trouve actuellement, et si la valeur maximale est spécifiée, vous pouvez également déterminer combien il reste.

Pour créer une barre de progression déterminée, vous devez spécifier l'attribut value. La plage par défaut de la valeur est de `0.0` à `1.0`. Mais vous pouvez également spécifier une valeur `max` personnalisée qui doit être un nombre à virgule flottante valide.

```html
<progress value="0">0%</progress>
<!-- ou -->
<progress value="0" max="100">0%</progress>
```

Pour incrémenter/décrémenter la valeur de la barre de progression, définissez l'attribut value sur le nombre souhaité. Voici une implémentation factice de la mise à jour de la progression :

```html
<body>
    <progress value="0" max="100"></progress>
</body>
<script>
    const progressBar = document.querySelector("progress")

    setTimeout(() => {
        setTimeout(() => {
            progressBar.value = 100
        }, 300)
        progressBar.value = 65
    }, 500)

    progressBar.value = 10
</script>
```

Pour afficher une barre de progression indéterminée, vous ne devez pas inclure l'attribut `value` dans l'élément `<progress>`. Les barres de progression indéterminées sont utiles lorsque vous ne pouvez pas préciser combien de temps l'utilisateur devra attendre pour que quelque chose se charge.

```html
<progress id="indeterminate-progress-bar">Indéterminé</progress>
```

![chrome_KPPOfkrwA4](https://www.freecodecamp.org/news/content/images/2024/01/chrome_KPPOfkrwA4.gif)

## 9. L'élément `<dialog>`

Je considère cet élément comme le plus utile de nos jours car il vous évite le tracas de créer votre propre modal avec des solutions de contournement de z-index. Mais cela ne signifie pas que vous devez [en abuser](https://www.scottohara.me/blog/2023/01/26/use-the-dialog-element.html). Vous pouvez l'utiliser pour créer des dialogues interactifs modaux/non-modaux afin d'alerter les utilisateurs ou d'afficher un message ponctuel.

Par exemple, si vous souhaitez afficher un message ponctuel aux utilisateurs visitant votre site, vous pouvez envelopper un élément `form` dans un `dialog` puis mentionner "dialog" comme méthode du formulaire. Cliquer sur le bouton à l'intérieur du formulaire fermera le dialogue.

Il s'agit d'un type de dialogue non-modal et il ne nécessite pas de JavaScript. L'attribut `open` indique que le dialogue sera affiché dès que la page se charge.

```html
<dialog open>
    <p>Ceci est un message ponctuel. Cliquez sur le bouton pour le fermer.</p>
    <form method="dialog">
        <button>Ok</button>
    </form>
</dialog>
```

Pour créer un dialogue modal, vous avez besoin d'un peu de JavaScript pour gérer les événements de clic pour afficher et masquer le modal. Il existe deux méthodes — `showModal()` et `close()` — que vous pouvez utiliser sur l'élément de dialogue après y avoir accédé avec JavaScript.

```html
<dialog>
    <p>Ceci est une boîte de dialogue.</p>
    <button id="close">Fermer</button>
</dialog>
<button id="open">Ouvrir la boîte de dialogue</button>

<script>
    document.querySelector("#open").addEventListener("click", () => {
        document.querySelector("dialog").showModal()
    })
    
    document.querySelector("#close").addEventListener("click", () => {
        document.querySelector("dialog").close()
    })
</script>
```

Il y a [tant de choses que vous pouvez faire](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog#examples) avec l'élément `dialog`, mais il n'est bon que pour certains [cas d'utilisation](https://www.nngroup.com/articles/modal-nonmodal-dialog/) tels que la présentation à l'utilisateur d'un formulaire d'inscription qui peut être fermé, l'affichage d'un avertissement avant que l'utilisateur n'effectue une action critique, et ainsi de suite.

Une situation où vous ne devriez pas les utiliser est pendant le processus de paiement d'une application e-commerce. Cela est dû au fait que l'utilisateur effectue une action critique, et s'il ferme accidentellement le dialogue, cela crée une perturbation dans le flux et l'expérience de l'utilisateur.

## HTML sémantique

Les éléments mentionnés ci-dessus relèvent d'un terme générique : [HTML sémantique](https://www.a11yproject.com/posts/what-is-semantic-html/). Le HTML sémantique donne un sens à votre contenu HTML – non seulement pour les utilisateurs, mais aussi pour les navigateurs, les robots d'indexation et les outils d'accessibilité.

Tout le monde ne peut pas voir l'écran ou utiliser des dispositifs tels qu'une souris pour naviguer sur le web. Au lieu de cela, ils dépendent des technologies d'assistance qui les aident à interpréter le contenu.

De plus, les moteurs de recherche peuvent trouver du contenu pertinent plus facilement en parcourant le HTML sémantique. C'est pourquoi cela devrait être l'une de vos principales priorités lorsque vous construisez un site web.

Vous ne voulez pas non plus que votre site web soit [juste un tas de divs](https://www.scottohara.me/blog/2022/01/20/divisive.html) car un élément `div` ne signifie rien pour un navigateur en termes de contenu — pour un navigateur, ce n'est qu'un élément de division pour séparer le contenu.

![un tas d'éléments div](https://www.freecodecamp.org/news/content/images/2023/12/divs-1.png)
_un tas d'éléments div (Source : imgur)_

## Conclusion

Aujourd'hui, vous avez appris quelques éléments ou balises HTML que vous ne connaissiez probablement pas auparavant.

Chaque élément HTML a un but spécifique et vous devriez envelopper votre contenu dans les éléments appropriés.

Vous avez également appris ce qu'est le HTML sémantique et que c'est la meilleure façon de donner du sens et de la structure à votre contenu.