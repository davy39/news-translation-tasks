---
title: Que sont les Bookmarklets ? Comment utiliser JavaScript pour créer un Bookmarklet
  dans Chromium et Firefox
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-06-17T00:53:04.000Z'
originalURL: https://freecodecamp.org/news/what-are-bookmarklets
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/cover-defectivefox-o-1.png
tags:
- name: automation
  slug: automation
- name: Google Chrome
  slug: chrome
- name: Firefox
  slug: firefox
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
seo_title: Que sont les Bookmarklets ? Comment utiliser JavaScript pour créer un Bookmarklet
  dans Chromium et Firefox
seo_desc: 'Bookmarklets are browser bookmarks that execute JavaScript instead of opening
  a webpage. They''re also known as bookmark applets, favlets, or JavaScript bookmarks.

  Bookmarklets are natively available in all major browsers, including Mozilla Firefox
  an...'
---

[Bookmarklets](https://en.wikipedia.org/wiki/Bookmarklet) sont des favoris de navigateur qui exécutent du JavaScript au lieu d'ouvrir une page web. Ils sont également connus sous le nom d'applets de favoris, de favlets ou de favoris JavaScript.

Les bookmarklets sont disponibles nativement dans tous les principaux navigateurs, y compris Mozilla Firefox et les navigateurs basés sur Chromium comme Chrome ou Brave.

## Scripting avec JavaScript

Apprendre à écrire des scripts offre de nombreux avantages, notamment des économies de temps considérables grâce à l'automatisation des tâches répétitives ou fastidieuses.

Si vous n'êtes pas développeur, l'idée d'apprendre à coder peut être intimidante, cependant le scripting ne nécessite pas de connaissances en ingénierie logicielle ou en modèles de conception. Le but n'est pas de créer un logiciel scalable, mais plutôt d'automatiser des tâches spécialisées ou triviales.

Quelle que soit votre profession, même si vous n'avez jamais écrit de code auparavant, réfléchissez à ce que vous faites dans votre navigateur. Si vous pensez que ce que vous faites est répétitif ou robotique, envisagez la possibilité de déléguer la tâche à un vrai robot.

## Cas d'utilisation des Bookmarklets

Avec les bookmarklets, vous pouvez manipuler la page actuelle car la fonction aura le contexte de l'onglet actuel. Cela signifie que vous pouvez :

* Cliquer sur des boutons virtuellement

* Modifier le contenu

* Utiliser le contenu de la page pour ouvrir une nouvelle page

* Supprimer des éléments de la page

Vous pouvez également créer des favoris qui n'utilisent pas du tout le contexte, comme l'ouverture conditionnelle d'une URL, ou la génération de HTML pour un nouvel onglet.

Vous trouverez quelques bookmarklets que j'ai créés pour cet article dans [Exemples de Bookmarklets](#heading-exemples-de-bookmarklets). Ils ne sont là qu'à titre de démonstration, mais devraient rendre les capacités et les implémentations apparentes.

## Comment créer des Bookmarklets

Créer un bookmarklet est presque identique à la création d'un favori ordinaire. La seule différence est que vous écrirez du JavaScript dans le champ URL au lieu d'une URL HTTP/HTTPS.

### Accéder au menu des favoris

#### Mozilla Firefox

Soit dans votre barre de favoris, soit dans la barre latérale des favoris (`CTRL` + `B`), vous pouvez faire un clic droit, puis cliquer sur "Ajouter un favori..." :

![La modale "Ajouter un favori" lors de la création d'un nouveau favori dans Firefox.](https://www.freecodecamp.org/news/content/images/2021/06/firefox-1.png align="left")

#### Chromium

Vous pouvez faire un clic droit sur votre barre de favoris, puis cliquer sur "Ajouter la page...". Alternativement, vous pouvez aller dans votre gestionnaire de favoris, puis faire un clic droit et cliquer sur "Ajouter un nouveau favori" :

![La modale "Modifier le favori" lors de la création d'un nouveau favori dans Chromium.](https://www.freecodecamp.org/news/content/images/2021/06/chromium.png align="left")

## Comment écrire un Bookmarklet

Dans le champ URL de la modale de favori, écrivez une fonction JavaScript dans le format suivant.

```js
javascript: (() => {
  // Votre code ici !
})();
```

`javascript:` est le protocole de l'URL. Cela indique que le navigateur doit exécuter le favori en tant que JavaScript.

`(() => { })` définit une fonction anonyme (lambda). Vous devez écrire le code que vous souhaitez exécuter entre les accolades.

`();` exécutera la fonction anonyme que vous venez de créer.

```js
javascript: (() => {
  alert('Bonjour, le monde !');
})();
```

![Une alerte de navigateur avec le message : "Bonjour, le monde !"](https://www.freecodecamp.org/news/content/images/2021/06/image-147-1.png align="left")

Vous pouvez également faire en sorte qu'il génère du HTML et l'ouvre en tant que document HTML :

```js
javascript: (() => {
  return '<h1 style="color: white; background-color: black;">Bonjour, le monde !</h1>';
})();
```

### Espacement pour les Bookmarklets

La plupart des navigateurs ne permettent pas un champ de saisie multiline dans l'URL du favori, vous devrez donc généralement faire un usage strict des accolades (`{` et `}`) et des points-virgules (`;`) lors de l'écriture de bookmarklets. Cela est particulièrement important lors de la portée des constructions conditionnelles (`if`/`for`/`while`).

Autre que cela, l'espacement n'a pas d'importance. N'ayez pas peur d'avoir beaucoup de code sur une seule ligne car c'est tout ce que vous avez :

```js
javascript: (() => {   const documentHTML = document.documentElement.outerHTML;   const matches = documentHTML.matchAll(/[\w.+=~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*/g);   const flatMatches = Array.from(matches).map((item) => item[0]);   const uniqueMatches = Array.from(new Set(flatMatches));      if (uniqueMatches.length > 0) {     const result = uniqueMatches.join('\n');     alert(result);   } else {     alert('Aucun email trouvé !');   } })();
```

Si votre script est complexe, il sera plus facile de maintenir votre bookmarklet dans un éditeur de code comme [Visual Studio Code](https://code.visualstudio.com/). Vous pouvez le copier et le coller dans votre navigateur lorsqu'il est prêt.

### Comment interagir avec les sites web

La chose la plus courante que vous feriez avec les bookmarklets est de manipuler ou d'interagir avec les sites web que vous avez ouverts.

#### L'objet Document global

Comme le bookmarklet a le contexte de la page sur laquelle vous vous trouvez, vous avez accès à l'objet `[document](https://developer.mozilla.org/en-US/docs/Web/API/Document)`.

Les fonctions idéales pour sélectionner des éléments pour notre cas d'utilisation sont :

* [`querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) pour sélectionner un seul élément par sélecteur CSS.

* [`querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) pour sélectionner tous les éléments correspondants par sélecteur CSS.

* `[evaluate](https://developer.mozilla.org/en-US/docs/Web/API/Document/evaluate)` pour sélectionner tous les éléments correspondants par XPath.

Il existe d'autres fonctions comme `[getElementById](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)` et `[getElementsByClassName](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName)`, mais nous voulons éviter les faux positifs, donc nous ferons toujours une sélection stricte en utilisant plusieurs attributs d'élément.

#### Sélecteurs CSS et XPath

Si vous ne sélectionnez des éléments que sur la base de noms d'éléments, d'IDs, de classes et d'autres attributs, l'utilisation d'un sélecteur CSS sera simple et efficace.

Les sélecteurs CSS sont utilisés pour sélectionner des éléments dans des documents HTML afin d'appliquer des styles. Si vous êtes familier avec le développement web ou le CSS en général, alors vous savez déjà comment utiliser les sélecteurs CSS. (Plus d'informations : [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors), [freeCodeCamp](https://www.freecodecamp.org/news/css-selectors-cheat-sheet/))

Si vous devez également faire correspondre le contenu textuel d'un élément, alors vous devrez utiliser XPath à la place.

XPath est utilisé pour parcourir des documents XML, il fournit toutes les capacités des sélecteurs CSS et plus encore, y compris la comparaison du contenu des éléments ou l'utilisation d'une expression régulière pour le faire correspondre. (Plus d'informations : [MDN](https://developer.mozilla.org/en-US/docs/Web/XPath), [Wikipedia](https://en.wikipedia.org/wiki/XPath))

#### Comment sélectionner des éléments de la page web

L'une des utilisations les plus courantes des bookmarklets est la manipulation des pages web. Pour interagir avec, manipuler ou supprimer des éléments de la page, vous devrez toujours sélectionner les éléments en premier.

1. Tout d'abord, ouvrez les outils de développement du navigateur en appuyant sur `F12`, ou `CTRL` + `SHIFT` + `I`.

2. Cliquez sur l'onglet [Inspector](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector)/[Elements](https://developer.chrome.com/docs/devtools/dom/), qui affiche le document HTML complet de la page que vous avez ouverte.

3. Utilisez l'outil de sélection d'élément (`CTRL` + `SHIFT` + `C`) et cliquez sur l'élément avec lequel vous souhaitez interagir. Le visualisateur de document fera défiler jusqu'à l'élément sur lequel vous avez cliqué dans le document HTML. Vous verrez l'ID de l'élément, les classes et les attributs.

4. Vérifiez si vous êtes sur le bon élément. Les éléments peuvent être imbriqués où il est plus facile de naviguer manuellement dans le HTML. Par exemple, vous avez peut-être cliqué sur un élément `svg`, mais vous aviez en fait besoin du `button` ou du `div` dans lequel il se trouvait.

5. Définissez un sélecteur CSS ou XPath qui correspond à tout ce que vous voulez, vous pourriez vouloir le rendre plus strict que nécessaire pour éviter les potentiels faux positifs.

Par exemple, supposons que je veux ignorer toutes les suggestions de sujets sur Twitter parce qu'elles sont ennuyeuses. Voici à quoi ressemble un élément cliquable pour ignorer un sujet.

![Suggestions de sujets Twitter, avec un bouton X pour le marquer comme "Pas intéressé".](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-16-at-04.19.17.png align="left")

*Suggestions de sujets Twitter, avec un bouton X pour le marquer comme "Pas intéressé".*

```html
<div aria-label="Dismiss" role="button" tabindex="0" class="...">
  <!-- Le div parent a l'écouteur de clic. -->
  <div class="...">
    <svg viewBox="0 0 24 24" aria-hidden="true" class="...">
      <!-- L'icône X réelle. -->
    </svg>
  </div>
</div>
```

Un sélecteur approprié est `div[aria-label=Dismiss][role=button]`.

Nous devons utiliser la fonction `querySelectorAll` de [L'objet Document global](#heading-lobjet-document-global), puis appeler la méthode `[click](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)` pour simuler un clic.

Un bookmarklet peut être implémenté pour sélectionner chaque bouton de rejet et déclencher un événement de clic pour tous avec un intervalle de 250 ms.

```js
javascript: (() => {
  const selector = 'div[aria-label=Dismiss][role=button]';
  const topics = document.querySelectorAll(selector);
    
  for (let i = 0; i < topics.length; i++) {
    let topic = topics[i];
    setTimeout(() => topic.click(), i * 250);
  }
})();
```

## Comment redistribuer des Bookmarklets

Pour "installer" un bookmarklet, les utilisateurs créent un favori sur leur navigateur et copient et collent le code dedans.

Cela peut être inconvénient, donc il est courant de lier les bookmarklets lors du partage. Cela est aussi simple que de le mettre dans l'attribut `href` de votre ancre de lien.

```html
<a href="javascript: (() => {   alert('Bonjour, le monde !'); })();">
  Bonjour, le monde !
</a>
```

Maintenant, les utilisateurs peuvent faire un clic droit et "Ajouter un favori", ou le glisser vers la barre de favoris pour un accès facile.

Cliquer sur le lien dans la page web exécutera le script immédiatement. Assurez-vous qu'il ne va pas obstruer ce qu'un utilisateur essaie de faire sur votre site s'il clique dessus par accident.

Par exemple, le lien suivant affichera une alerte avec "Bonjour, le monde !".

### Contenu utilisateur et contournement de la politique de sécurité du contenu

Si vous exécutez un service qui permet au contenu généré par les utilisateurs de contenir du HTML personnalisé, il est important de nettoyer les ancres de lien (`a`).

Le bookmarklet s'exécute comme du code dans la console des outils de développement et contourne la [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (CSP) configurée.

Le lien "Bonjour, le monde !" peut tout aussi facilement envoyer des données à un autre serveur, y compris l'entrée des champs de formulaire ou des cookies.

En tant que fournisseur de services, il est important de se méfier que les utilisateurs peuvent exploiter cela pour partager du code malveillant sur votre plateforme. Si leur ancre de lien s'exécute sur une page sous votre domaine, elle peut accéder à des informations sensibles sur la page et à `[document.cookies](https://developer.mozilla.org/en-US/docs/web/api/document/cookie)`.

Vous pouvez l'essayer vous-même dans un environnement sandbox :

```html
<a href="javascript: (() => {   alert(document.cookie); })();">
  EvilScript
</a>
```

### N'exécutez que le code en lequel vous avez confiance

En tant qu'utilisateur, il est important de noter que tout code peut être malveillant, ne cliquez ou n'ajoutez des bookmarklets que si au moins l'une des conditions suivantes est vraie :

* Il provient d'une source fiable.

* Vous connaissez JavaScript et vous avez examiné ce qu'il fait.

* Quelqu'un en qui vous avez confiance connaît JavaScript et l'a examiné pour vous.

## Vie privée et sécurité

Les bookmarklets peuvent être pratiques, mais nous avons également des [extensions web](https://en.wikipedia.org/wiki/Browser_extension) et des [scripts utilisateur](https://en.wikipedia.org/wiki/Userscript). Qu'est-ce qui les rend différents ?

Les extensions web sont incroyablement conviviales et flexibles. Les bookmarklets ne peuvent pas bloquer les requêtes réseau, mettre à jour le contenu lorsque la page change ou gérer les onglets.

Cependant, il y a certains avantages à utiliser des bookmarklets plutôt que autre chose, notamment pour la vie privée et la sécurité.

Une extension qui modifie la police sur toutes les pages doit obtenir la permission d'accéder à toutes les données sur toutes les pages web. Sur Firefox et Chrome, cela inclut tous les champs de saisie et de mot de passe. (Plus d'informations : [Mozilla](https://support.mozilla.org/kb/permission-request-messages-firefox-extensions#w_access-your-data-for-all-websites), [Google](https://developer.chrome.com/docs/extensions/mv3/permission_warnings/#permissions_with_warnings))

En revanche, un bookmarklet n'a accès à la page que pour le très court moment où il s'exécute, et seulement lorsqu'il est déclenché manuellement par l'utilisateur.

Cela entraîne moins de risques de logiciels malveillants, un employé malveillant ne peut pas pousser une mise à jour malveillante, et les données ne seront pas envoyées silencieusement à d'autres serveurs.

Le Chrome Web Store a précédemment eu plusieurs extensions malveillantes qui ont dû être retirées. Certaines d'entre elles avaient des millions d'installations avant d'être supprimées. ([Plus d'informations](https://en.wikipedia.org/wiki/Chrome_Web_Store#Malware))

## Exemples de Bookmarklets

Voici une liste d'idées de bookmarklets, ainsi que le code qui les implémente. Vous pouvez les copier et les coller dans de nouveaux favoris pour les essayer.

```js
javascript: (() => {
  const documentHTML = document.documentElement.outerHTML;
  const matches = documentHTML.matchAll(/[\w.+=~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*/g);
  const flatMatches = Array.from(matches).map((item) => item[0]);
  const uniqueMatches = Array.from(new Set(flatMatches));
  
  if (uniqueMatches.length > 0) {
    const result = uniqueMatches.join('\n');
    alert(result);
  } else {
    alert('Aucun email trouvé !');
  }
})();
```

```js
javascript: (() => {
  const xpath = "//a [contains(., 'Jobs') or contains(., 'Careers') or contains(., 'Hiring')]";
  const elements = document.evaluate(xpath, document);
  const element = elements.iterateNext();
    
  if (element) {
    element.click();
  } else {
    alert('Aucun lien pour les emplois trouvé !');
  }
})();
```

```js
javascript: (() => {
  const allElements = document.querySelectorAll('*');

  for (let element of allElements) {
    element.style.fontFamily = 'Comic Sans MS';
  }
})();
```

```js
javascript: (() => {
  const destination = "https://www.freecodecamp.org/";
  const alternate = "https://tenor.com/Y6jj.gif";
  
  const date = new Date();
  const hours = date.getHours();
    
  if (hours < 3 || hours >= 6) {
    window.open(destination);
  } else {
    window.open(alternate);
  }
})();
```

Merci d'avoir lu ! Maintenant, allez de l'avant et créez vos propres bookmarklets.