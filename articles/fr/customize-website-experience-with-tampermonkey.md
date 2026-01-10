---
title: Comment utiliser Tampermonkey pour améliorer l'UI d'un site web – Exemple avec
  freeCodeCamp
subtitle: ''
author: Tasnim Ferdous
co_authors: []
series: null
date: '2023-08-22T22:32:35.000Z'
originalURL: https://freecodecamp.org/news/customize-website-experience-with-tampermonkey
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/cover_image.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Scripting
  slug: scripting
- name: user experience
  slug: user-experience
seo_title: Comment utiliser Tampermonkey pour améliorer l'UI d'un site web – Exemple
  avec freeCodeCamp
seo_desc: "What is Tampermonkey?\nTampermonkey is a browser extension that lets you\
  \ add custom scripts to websites, making them work or look the way you want. It's\
  \ like giving websites a makeover or adding new features. \nThese scripts are called\
  \ userscripts and ..."
---

## Qu'est-ce que Tampermonkey ?

Tampermonkey est une extension de navigateur qui vous permet d'ajouter des scripts personnalisés aux sites web, les faisant fonctionner ou apparaître comme vous le souhaitez. C'est comme donner un relooking aux sites web ou ajouter de nouvelles fonctionnalités. 

Ces scripts sont appelés userscripts et vous pouvez faire en sorte que Tampermonkey exécute ces scripts lorsque vous visitez un site particulier.


## Comment utiliser Tampermonkey pour personnaliser l'expérience utilisateur d'un site web

Il existe de nombreux cas d'utilisation pour Tampermonkey. Le plus évident est d'ajouter votre propre style personnalisé. Vous pouvez ajouter du CSS personnalisé pour un site spécifique et modifier l'apparence comme vous le souhaitez. Mais comme vous pouvez exécuter un script, vous pouvez également manipuler les éléments du DOM. 

Je vais lister les choses que j'ai faites pour vous donner quelques idées de ce qui est possible.

1. Augmenter la lisibilité en modifiant les propriétés de la police.
2. Supprimer les publicités sur les sites qui n'autorisent pas un bloqueur de publicités.
3. Désencombrer un site pour que vous puissiez vous concentrer sur la partie qui vous intéresse.
4. Ajouter des raccourcis clavier pour les tâches répétitives.
5. Ajouter des boutons pour des actions personnalisées.
6. Remplir automatiquement les données de formulaire.

Aujourd'hui, vous aurez un aperçu de ce que vous pouvez faire avec Tampermonkey en écrivant des scripts qui fonctionneront sur le site freeCodeCamp /news. 

Tout d'abord, nous verrons comment désencombrer pour une expérience de lecture plus ciblée. Ensuite, nous attacherons des boutons de copie aux extraits de code. Et enfin, nous générerons automatiquement une table des matières à laquelle vous pourrez accéder avec un bouton bascule. 

Le code source est disponible sur <a href="https://github.com/renzhamin/freecodecamp-enhancer" target="_blank">GitHub</a>.

Il est important de noter que toutes les modifications apportées par votre script ne seront disponibles que dans votre navigateur. Donc, tant que vous ne traitez pas de données sensibles sur ce site, vous pouvez vous lâcher autant que vous le souhaitez. 

Mais soyez conscient que certains sites peuvent avoir des politiques concernant l'utilisation de JavaScript tiers et prendre des mesures disciplinaires si vous violez cette politique.


## Prérequis

Comme nous allons modifier un site web, des connaissances de base en HTML, CSS et JavaScript sont nécessaires pour suivre ce tutoriel. Une expérience avec la manipulation du DOM serait également idéale. 

Si vous pouvez manipuler efficacement les éléments DOM existants, cela vous permettra d'écrire des scripts Tampermonkey pour vous rendre plus productif sur n'importe quel site web. 


## Table des matières

  * [Comment installer Tampermonkey](#comment-installer-tampermonkey)
  * [Comment créer un nouveau Userscript](#comment-creer-un-nouveau-userscript)
  * [Comment modifier le comportement d'un bouton](#comment-modifier-le-comportement-dun-bouton)
  * [Comment implémenter la vue lecteur pour les articles freeCodeCamp /news](#comment-implementer-la-vue-lecteur-pour-les-articles-freecodecamp-news)
  * [Comment ajouter des boutons de copie aux extraits de code](#comment-ajouter-des-boutons-de-copie-aux-extraits-de-code)
  * [Comment générer automatiquement une table des matières](#comment-generer-automatiquement-une-table-des-matieres)
  * [Points clés à retenir](#points-cles-a-retenir)


<!-- TOC --><a name="comment-installer-tampermonkey"></a>
## Comment installer Tampermonkey

Pour Chrome, l'extension est disponible sur le <a href="https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo" target="_blank">chrome web store.</a>

Elle est également disponible pour Firefox, que vous pouvez installer depuis <a href="https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/" target="_blank">Firefox Add-Ons.</a>

Pour les autres navigateurs, vous pouvez visiter la <a href="https://www.tampermonkey.net/index.php" target="_blank">page d'accueil de Tampermonkey</a>. Actuellement, Chrome, Firefox, Edge, Safari et Opera sont officiellement supportés. Mais celui du Chrome web store fonctionne bien sur les navigateurs basés sur Chromium comme Brave.

<!-- TOC --><a name="comment-creer-un-nouveau-userscript"></a>
## Comment créer un nouveau Userscript

La manière la plus simple de commencer est d'utiliser l'option `create new script` depuis la barre d'outils.

<img src="https://www.freecodecamp.org/news/content/images/2023/08/create-new-script.jpeg" alt="create new script" width="200px" />

Vous verrez quelque chose comme ceci :

```
// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.freecodecamp.org/news/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=freecodecamp.org
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
})();
```

L'en-tête du userscript contient des informations sur le script ainsi que d'autres paramètres importants. 

Pour l'instant, la partie pertinente est `@match`. Cela indique à Tampermonkey pour quels sites exécuter le script. J'ai modifié pour correspondre à n'importe quel article sur le site d'actualités de freeCodeCamp en utilisant le caractère générique "\*" .

Testez-le en mettant quelque chose de simple comme `alert("HI")` dans la fonction. Ensuite, naviguez vers n'importe quel article sur freecodecamp.org/news. 

Faisons quelque chose d'intéressant ensuite. Ce sera une brève introduction à la manipulation du DOM. 

Avant d'écrire du code dans le userscript, il est préférable d'écrire votre code dans la console de développement d'abord. Ensuite, lorsque vous avez un code fonctionnel, vous pouvez simplement le coller dans le script Tampermonkey. C'est ainsi que nous écrirons tous les scripts de cet article également.

<!-- TOC --><a name="comment-modifier-le-comportement-dun-bouton"></a>
## Comment modifier le comportement d'un bouton

À la fin de chaque article freeCodeCamp, il y a un bouton qui dit "Tweet a thanks". Vous pouvez voir la fonction onclick du bouton en utilisant le sélecteur d'élément depuis les outils de développement et en cliquant sur ce bouton.

<img src="https://www.freecodecamp.org/news/content/images/2023/08/tweet-btn.jpeg" width="600px">

En cliquant sur ce bouton, une nouvelle fenêtre s'ouvrira sur Twitter avec un texte par défaut pour un tweet comme suit :

```
Thank you @twitter-username-of-author for writing this helpful article.

Title of Article
https://www.freecodecamp.org/news/slug-of-article
```

Disons que vous voulez changer le texte par défaut en quelque chose comme ceci :

```
This article is quite fascinating.

Title of Article by @twitter-username-of-author
https://www.freecodecamp.org/news/slug-of-article
```

Le nouveau texte est statique car vous le choisissez, mais il y a quelques variables ici. Vous devez extraire ces 3 choses :

1. Le lien de l'article.
2. Le nom d'utilisateur Twitter de l'auteur.
3. Le titre de l'article.

L'extraction du lien se fait avec `location.href`.

Maintenant, comment extraire le nom d'utilisateur Twitter ?

À première vue, vous pourriez penser que le nom après l'image de l'auteur est la réponse. Mais il s'agit en réalité du nom de l'auteur (qui n'est pas nécessairement unique) – ce n'est pas leur nom d'utilisateur Twitter. Alors, où commencer à le chercher ?

Puisque vous pouvez simplement cliquer sur le bouton ou l'inspecter, vous connaissez déjà les valeurs de toutes ces variables. Donc, une bonne façon de trouver le nom d'utilisateur Twitter serait de le rechercher dans l'ensemble du document HTML. Comme il est unique, il n'y aura pas beaucoup d'occurrences. 

Ouvrez les outils de développement et recherchez le nom d'utilisateur Twitter. Vous trouverez cette balise :

```html
<meta name="twitter:creator" content="@username" />
```


<img src="https://www.freecodecamp.org/news/content/images/2023/08/twitter-username-search.jpeg" width="500px" >

Ce qui n'est pas surprenant, car la plupart des sites de publication mettent des informations telles que le titre de l'article, les tags, la description et les informations sur l'auteur dans les balises meta à des fins de SEO. Mais la plupart du temps, vous pouvez simplement trouver ce que vous cherchez en utilisant l'outil d'inspection.

Alors, comment extraire la propriété "content" de cette balise meta ? Considérant qu'un article est écrit par un seul auteur, il y aura toujours une seule balise meta avec le nom "twitter:creator". Donc, vous pouvez simplement utiliser querySelector.

```js
const username = document.querySelector('meta[name="twitter:creator"]').content
```

Passons maintenant à l'extraction du titre. Si vous avez cherché le nom d'utilisateur Twitter, vous trouverez qu'il y a aussi une balise meta avec le nom "twitter:title". Mais cette fois, le titre est quelque chose que vous pouvez voir visuellement et inspecter. Dans la plupart des cas, c'est la manière la plus simple de procéder.

<img src="https://www.freecodecamp.org/news/content/images/2023/08/article-title.png" width="700px">

Si vous inspectez le titre de l'article au-dessus de l'image de couverture, vous verrez qu'il est à l'intérieur d'un h1 avec la classe "post-full-title". Vous pouvez le sélectionner avec ce qui suit :

```js
const title = document.querySelector("h1.post-full-title").textContent
```

Maintenant, nous avons toutes les pièces nécessaires pour faire le changement. Inspectez le bouton cible et vous verrez qu'il vient avec un id de "tweet-btn". Maintenant, définissons notre texte.

```js
const text = `This article is quite fascinating.

${title} by ${username}
${location.href}
`
```

En mettant tout ensemble en changeant l'onclick du bouton, voici ce que vous devriez avoir :

```js
function change_tweet_text() {
    document.getElementById("tweet-btn").onclick = () => {
        const username = document.querySelector(
            'meta[name="twitter:creator"]'
        ).content
        const title = document.querySelector("h1.post-full-title").textContent

        const text = `This article is quite fascinating.

${title} by ${username}
${location.href}
`

        const share_link = encodeURI(
            `https://twitter.com/intent/tweet?text=${text}`
        )

        window.open(share_link, "share-twitter", "width=550, height=235")

        return false
    }
}
```

Parce que le texte contient des caractères de nouvelle ligne, nous devons le convertir en format encodé URL.

Collez la fonction à l'intérieur du userscript et appelez-la.

```js
;(function () {
    change_tweet_text()
})()
```

Maintenant, rechargez la page de l'article et cliquez sur le bouton pour voir si cela fonctionne comme prévu.

Il est possible que cela ne fonctionne pas comme prévu. Surtout si la page met beaucoup de temps à charger. 

Avec ce script, nous modifions un bouton qui est un élément DOM. Mais que se passe-t-il si l'élément n'est pas encore chargé ? Alors vous rencontrerez des résultats inattendus. 

Tampermonkey fournit l'en-tête "// @run-at" que vous pouvez spécifier comme "document-end", mais j'ai trouvé que cela produit encore parfois des résultats inattendus. 

La bonne façon de l'atténuer est d'utiliser l'événement "load" qui est émis lorsque toute la page est chargée. Donc, nous pouvons refactoriser notre fonction principale de la manière suivante :

```js
addEventListener("load", main)

function main() {
    change_tweet_text()
}
```

Vous pouvez être extra prudent et ajouter un délai également :

```js
addEventListener("load", setTimeout(main, 2000))
```

À partir de maintenant, nous appellerons toutes les fonctions dans cette fonction principale qui s'exécutera après que l'événement load soit déclenché.

Notez que vous auriez pu obtenir le même résultat en utilisant une expression régulière. Dans ce cas, vous auriez pu extraire les variables de l'onclick du bouton qui contient l'URL avec le texte complet. 

Mais extraire les informations des balises est meilleur car si un jour le texte du tweet par défaut change, vous devrez également changer le regex.

<!-- TOC --><a name="comment-implementer-la-vue-lecteur-pour-les-articles-freecodecamp-news"></a>
## Comment implémenter la vue lecteur pour les articles freeCodeCamp /news

Si vous mettez votre navigateur en plein écran, la barre de navigation supérieure reste en haut – ce qui n'est pas la meilleure expérience de lecture. Donc, nous voulons masquer tout sauf le corps principal de l'article. 

Commençons à inspecter. Vous verrez que, près de la balise "main", il y a une balise "article" avec la classe "post". Elle contient tout le texte de l'article, y compris l'en-tête et l'image de couverture.

Cette fois, nous allons modifier en direct le CSS de la page. Dans Firefox, vous pouvez utiliser l'onglet "Style Editor" dans les outils de développement. Cliquez sur l'icône "+" et commencez à tester votre CSS.

Pour l'instant, il n'y a pas de moyen intégré pour masquer tous les éléments sauf un (dans notre cas article.post) en utilisant CSS. Vous pourriez être tenté d'utiliser `:not(article.post)` mais cela ne fonctionnera pas car si un ancêtre de l'élément est masqué, alors tous les descendants seront également masqués. 

Nous pouvons accomplir notre objectif en utilisant le sélecteur ":has". `:has(article.post)` sélectionnera tous les ancêtres de article.post afin que nous puissions sélectionner l'inverse avec `:not(:has(article.post))`. 

Mais il y a encore un problème : le descendant de article.post est également ignoré par ce sélecteur. Nous pouvons les ramener en enchaînant un autre not – `:not(article.post, article.post *)`. Cela sélectionnera tout ce qui n'est pas un article.post ou un descendant de celui-ci.

Voici le CSS final :

```css
:not(:has(article.post)):not(article.post, article.post *) {
    display: none;
}
```

<img src="https://www.freecodecamp.org/news/content/images/2023/08/style-editor.png" width="700px" >

Au moment de l'écriture, le sélecteur ":has" est expérimental dans Firefox. Mais vous pouvez aller dans `about:config` et l'activer en changeant la valeur de `layout.css.has-selector.enabled` à true.

Et si vous voulez utiliser la barre de navigation ? Ce serait dommage d'écrire manuellement le CSS et de le supprimer lorsque vous ne le voulez pas, n'est-ce pas ? Surtout maintenant que vous pouvez faire du scripting.

Nous allons ajouter un raccourci clavier au site qui mettra le navigateur en plein écran. Nous appliquerons également ce CSS et, lors de la sortie du plein écran, le CSS sera supprimé.

L'une des API exposées de tampermonkey est `GM_addStyle(css)` pour ajouter du CSS. Pour que cette API fonctionne, vous devez inclure `// @grant           GM_addStyle` dans l'en-tête du userscript et également supprimer `// @grant none` si vous l'avez.

Pour créer le raccourci, vous utiliserez un écouteur d'événement "keydown".

```js
function add_declutter_toggle(key) {
    const css = `
        .declutter :not(:has(article.post)):not(article.post, article.post *) {
            display: none;
        }`

    GM_addStyle(css)

    document.addEventListener("keydown", (event) => {
        if (event.key === key) {
            if (document.fullscreen) {
                document.exitFullscreen()
                document.body.classList.remove("declutter")
            } else {
                document.body.classList.add("declutter")
                document.documentElement.requestFullscreen()
            }
        }
    })
}
```

Nous appliquons le CSS aux éléments avec la classe "declutter". En basculant le "declutter" sur le body, nous basculons essentiellement le CSS sur toute la page.

Maintenant, nous devons simplement ajouter l'appel de fonction dans notre fonction principale.

```js
function main() {
    change_tweet_text()
    add_declutter_toggle("F")
}
```

Rechargez la page et vous verrez qu'appuyer sur "F" basculera le plein écran et supprimera également tout sauf le corps de l'article lorsque vous êtes en mode plein écran.

<img src="https://www.freecodecamp.org/news/content/images/2023/08/declutter_demo.gif" width="600px" alt="declutter demo">

<!-- TOC --><a name="comment-ajouter-des-boutons-de-copie-aux-extraits-de-code"></a>
## Comment ajouter des boutons de copie aux extraits de code

La première étape consiste toujours à identifier le bon sélecteur. Si vous inspectez n'importe quel extrait de code, vous verrez qu'ils sont contenus dans des blocs `<code>` et ont un `<pre>` comme parent. Donc, pour sélectionner tous les extraits de code, le sélecteur peut être `pre > code`. 

Maintenant, la question est où placer le bouton ? Pour un accès facile, nous voulons que le bouton soit en haut de l'extrait de code et aligné à droite. Vous pourriez penser que le placer entre la balise `<pre>` et la balise `<code>` pourrait fonctionner – mais cela interférerait avec le contenu de l'extrait de code, ce qui n'est pas idéal.

La solution idéale consiste à envelopper la balise `<pre>` avec une div et à créer la structure comme `div > button > pre > code`.

La copie est effectuée par l'API clipboard en utilisant la méthode `navigator.clipboard.writeText`. Nous appliquerons également un peu de style et informerons le lecteur que leur copie a réussi en changeant le texte du bouton de "copy" à "copied" pendant une courte durée.

```js
function attach_code_copy_btn() {
    const css = `
        .copy-btn {
            float: right;
            margin-bottom: 5px;
            border-radius: 1rem;
            font-size: 0.8em;
            width: 7rem;
        }

        .pre-wrapper {
            width: 100%;
        }
    `
    GM_addStyle(css)

    const codes = document.querySelectorAll("pre > code")
    codes.forEach((code) => {
        const pre = code.parentElement
        const btn = document.createElement("button")
        btn.textContent = "copy"
        btn.classList.add("copy-btn")
        btn.addEventListener("click", () =>
            navigator.clipboard.writeText(code.textContent).then(() => {
                btn.textContent = "copied"
                setTimeout(() => (btn.textContent = "copy"), 2500)
            })
        )
        const div = document.createElement("div")
        div.classList.add("pre-wrapper")
        div.appendChild(btn)
        wrap(pre, div)
    })
}

function wrap(elem, wrapper) {
    elem.parentNode.insertBefore(wrapper, elem)
    wrapper.appendChild(elem)
}
```

La fonction `attach_code_copy_btn` trouve tous les extraits de code et les enveloppe autour d'une div, ajoute des classes à ceux-ci, et attache un bouton qui copiera le contenu du code au clic.

Appelez la fonction comme avant :

```js
function main() {
    change_tweet_text()
    add_declutter_toggle("F")
    attach_code_copy_btn()
}
```


<img src="https://www.freecodecamp.org/news/content/images/2023/08/copy_demo.gif" alt="copy demo" width="700px">


<!-- TOC --><a name="comment-generer-automatiquement-une-table-des-matieres"></a>

Voici un peu de pratique, essayez d'ajouter des écouteurs d'événements de clic à toutes les balises `<code>` qui ne sont pas à l'intérieur d'une balise `<pre>`. Sur un clic de souris sur le bloc `<code>`, le contenu du bloc sera copié.


## Comment générer automatiquement une table des matières

freeCodeCamp est un excellent endroit pour lire des articles approfondis. Les articles sont également bien organisés. La plupart des auteurs utilisent des en-têtes appropriés et fournissent une table des matières. Mais la ToC n'est pas accessible sur toutes les parties de la page. 

Si vous voulez sauter quelque part, vous devrez revenir à la ToC puis cliquer sur votre section d'intérêt. Et puis il y a des articles plus courts qui ne fournissent pas de ToC du tout.

C'est là que nous pouvons introduire un userscript qui générera automatiquement une table des matières accessible n'importe où sur la page. Cela améliore l'expérience utilisateur lors de la lecture d'articles plus longs. 

La première chose que vous devez savoir est comment fonctionne une ToC. Une section dans la ToC est simplement une balise d'ancrage avec une valeur href de `#some-section`. Ici, "some-section" peut être la propriété name d'une balise d'ancrage de l'emplacement cible (par exemple, `<a name="some-section">`) ou si elle est utilisée comme id sur n'importe quel élément (par exemple, `<h2 id="some-section">`).

Si vous inspectez n'importe quelle balise d'en-tête, vous verrez que l'attribut id est présent. Cela est automatiquement inséré lorsque la page de l'article est construite. Donc, nous pouvons l'utiliser pour notre ToC.

Voici une fonction de générateur de ToC modifiée à partir d'une <a href="https://stackoverflow.com/questions/187619/is-there-a-javascript-solution-to-generating-a-table-of-contents-for-a-page" target="_blank">réponse StackOverflow</a>.

```js
function generate_toc() {
    let toc = ""
    let level = 1

    let container = document.querySelector(".post-content")
    const regex = /<h([2-5])\s+id="([^"]+)">([^<]+)<\/h([2-5])>/gi
    const matches = [...container.innerHTML.matchAll(regex)]
    matches.forEach((match) => {
        if (match.length != 5) return
        const [_, openLevel, id, titleText, closeLevel] = match

        if (openLevel !== closeLevel) {
            return
        }

        if (openLevel > level) {
            toc += new Array(openLevel - level + 1).join("<ol>")
        } else if (openLevel < level) {
            toc += new Array(level - openLevel + 1).join("</li></ol>")
        } else {
            toc += new Array(level + 1).join("</li>")
        }

        level = parseInt(openLevel)

        if (!id) {
            id = titleText.replace(/ /g, "_")
        }
        toc += '<li><a href="#' + id + '">' + titleText + "</a></li>"
    })

    if (level) {
        toc += new Array(level + 1).join("</ol>")
    }

    return toc
}
```

Nous utilisons une regex pour correspondre aux balises h2, h3, h4 et h5 et créons une liste ordonnée pour afficher le contenu de la ToC et retournons le HTML de toute la ToC.

Maintenant, nous allons ajouter ce HTML à une div qui contiendra la ToC. Cette div sera enveloppée à l'intérieur d'un composant de dialogue afin que nous puissions utiliser une modale pour afficher/masquer facilement la ToC. Nous ajouterons également un bouton qui servira de bascule.

```js
function show_toc() {
    document.documentElement.style.overflow = "hidden"
    document.getElementById("toc-dialog").showModal()
}

function add_toc_toggle() {
    const dialog = document.createElement("dialog")
    dialog.setAttribute("id", "toc-dialog")
    const toc_div = document.createElement("div")
    toc_div.classList.add("toc-content")
    toc_div.innerHTML = "<h2>Table des matières</h2>"
    dialog.appendChild(toc_div)

    const show_toc_btn = document.createElement("button")
    show_toc_btn.setAttribute("id", "toc-toggle")
    show_toc_btn.innerHTML =
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M.361 256C.361 397 114 511 255 511C397 511 511 397 511 256C511 116 397 2.05 255 2.05C114 2.05 .361 116 .361 256zM192 150V363H149V150H192zM234 150H362V193H234V150zM362 235V278H234V235H362zM234 320H362V363H234V320z"></path></svg>'

    show_toc_btn.addEventListener("click", () => {
        show_toc()
    })

    // Cliquez n'importe où pour fermer
    dialog.addEventListener("click", (event) => {
        document.documentElement.style.overflow = "auto"
        event.currentTarget.close()
    })

    dialog.addEventListener("close", (event) => {
        document.documentElement.style.overflow = "auto"
        event.currentTarget.close()
    })

    document.querySelector(".post-content").appendChild(dialog)
    document.querySelector(".post-content").appendChild(show_toc_btn)
}
```

Enfin, nous fournirons une fonction de pilotage qui effectuera toutes les tâches nécessaires liées à la génération de la ToC. Nous ajouterons également un raccourci clavier pour basculer la ToC.

```js
function add_toc(toc_toggle_key) {
    const css = `
        .toc-content {
            margin: 0;
            padding: 0;
            max-width: 65vw;
        }

        @media (width <= 800px) {
            .toc-content {
                max-width: 100vw;
            }
        }

        .toc-content h2 {
            padding: 20px 30px;
        }

        .toc-content ol {
            counter-reset: item;
        }

        .toc-content li {
            display: flex;
            white-space: nowrap;
            gap: 5px;
        }

        .toc-content li:before {
            content: counters(item, ".") " ";
            counter-increment: item;
        }

        .toc-content a {
            text-decoration: none;
            white-space: normal;
            flex-grow: 1;
        }

        .toc-content li:hover {
            background: rgba(82, 142, 227, 0.3);
            cursor: pointer;
        }

#toc-toggle {
            background: transparent;
            position: fixed;
            bottom: 5%;
            right: 5%;
            width: 5rem;
        }

#toc-toggle svg {
            fill: rgb(82, 142, 227);
            scale: 1;
        }

#toc-toggle svg:hover {
            scale: 1.15;
        }

#toc-dialog {
            padding: 0;
            border: 0;
        }
`
    GM_addStyle(css)

    add_toc_toggle()
    document.querySelector(".toc-content").innerHTML += generate_toc()

    if (toc_toggle_key) {
        document.addEventListener("keydown", (event) => {
            if (event.key === toc_toggle_key) {
                show_toc()
            }
        })
    }
}
```

Maintenant, appelez simplement la fonction de pilotage dans main.

```js
function main() {
    change_tweet_text()
    add_declutter_toggle("F")
    attach_code_copy_btn()
    add_toc(";")
}
```


<img src="https://www.freecodecamp.org/news/content/images/2023/08/toc_demo-1.gif" width="800px" alt="toc demo">

Maintenant, chaque fois que vous lisez un article sur freeCodeCamp, vous pouvez utiliser le bouton bascule ou un raccourci pour afficher la ToC.

Pour vous entraîner, essayez de rendre la ToC collante sur le côté (gauche/droite). Si vous êtes sur un écran plus large, avoir la ToC sur le côté rendra l'expérience de lecture encore meilleure. 

<!-- TOC --><a name="points-cles-a-retenir"></a>
## Points clés à retenir

Vous ne devriez jamais exécuter de JavaScript arbitraire en aucune occasion. Cela s'applique également aux scripts Tampermonkey. 

Je recommande de passer en revue chaque ligne de code avant d'utiliser un userscript. Comme vous pouvez déjà l'imaginer, un userscript peut radicalement modifier l'apparence d'un site web. Si vous n'êtes pas assez prudent, vous pourriez cliquer sur un bouton que vous attendez pour faire une chose mais qui en fait une complètement différente, alors soyez toujours prudent.

Lors de l'écriture de userscripts, gardez ces choses à l'esprit :

1. Testez toujours votre code dans la console de développement d'abord et prenez soin de tous les cas limites.
2. Préférez créer/manipuler des éléments DOM en utilisant des fonctions intégrées plutôt que de modifier le innerHTML.
3. Si vous trouvez un comportement inattendu, essayez d'ajouter un long délai et vérifiez si cela résout le problème.

Vous pouvez lire mes autres articles sur mon <a href="https://blog.renzhamin.com" target="_blank">blog</a>. Retrouvez-moi sur <a href="https://twitter.com/renzhamin" target="_blank">Twitter</a> <a href="https://www.linkedin.com/in/renzhamin/" target="_blank">LinkedIn</a>.