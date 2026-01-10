---
title: La balise HTML <a> – Exemple de code de la balise d'ancrage
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-12-17T17:47:31.000Z'
originalURL: https://freecodecamp.org/news/the-html-a-tag-anchor-tag-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/freeCodeCamp-Cover.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: La balise HTML <a> – Exemple de code de la balise d'ancrage
seo_desc: 'HTML(Hyper Text Markup Language) is one of the languages we use to create
  web applications. It adds structure to your web pages.

  HTML has various tags we use to create elements. And multiple elements come together
  to create meaningful web pages and a...'
---

`HTML` (**H**yper **T**ext **M**arkup **L**anguage) est l'un des langages que nous utilisons pour créer des applications web. Il ajoute de la structure à vos pages web.

HTML dispose de diverses balises que nous utilisons pour créer des éléments. Et plusieurs éléments se combinent pour créer des pages et des applications web significatives.

La balise `anchor` (ancrage) est l'une des balises les plus utilisées et les plus connues en HTML. Dans cet article, nous allons apprendre à connaître la balise d'ancrage (<a>) et ses principales utilisations avec de nombreux exemples.

Mais pourquoi parler de la balise d'ancrage si elle est déjà bien connue ? Il y a quelques détails essentiels de cette balise que beaucoup de développeurs ne connaissent pas - mais ils devraient. Alors apprenons-les.

J'ai créé une application pour démontrer différents comportements de la balise d'ancrage. Vous pouvez la consulter et l'utiliser tout en lisant cet article.

%[https://anchors.vercel.app/]

Si vous aimez aussi apprendre à partir de contenu vidéo, cet article est également disponible sous forme de tutoriel vidéo ici : 👨‍💻

%[https://www.youtube.com/watch?v=neWThioR5hw&list=PLIJrr73KDmRzBs_I3rfndvH_GPrF_byYD]

# Qu'est-ce que la balise d'ancrage en HTML ?

Le but principal d'une balise `anchor` est de lier une page à une autre page ou à une section de la même page. La balise d'ancrage est également connue sous le nom de `HyperLien`. Comme pour les autres balises HTML, vous utilisez la construction suivante pour créer une balise d'ancrage :

```html
<a>Mon Site Web</a>
```

La balise d'ancrage ci-dessus est une balise HTML valide, mais elle ne fait pas grand-chose d'autre que de servir de placeholder. Utilisons cette balise d'ancrage pour lier à une page web. Vous devez utiliser l'attribut `href` pour lier à une autre page.

```html
<a href="https://tapasadhikary.com">Mon Site Web</a>
```

La valeur de l'attribut `href` est généralement une URL pointant vers une page web (comme celle ci-dessus). Vous pouvez également lier un autre élément HTML ou un protocole (par exemple, envoyer un email), et vous pouvez exécuter du JavaScript en utilisant l'attribut href. Nous verrons des exemples de comment faire tout cela ci-dessous.

# Utilisations de la balise d'ancrage avec des exemples

En plus de `href`, il existe d'autres attributs vitaux qui rendent la balise d'ancrage utile. Apprenons à les connaître avec des exemples.

### Comment lier à une section de la page

Nous avons vu comment lier à une page web externe (site web). Mais vous pouvez également lier à une section de la même page en liant à un élément en utilisant son id. Supposons que notre page a une section `div` avec l'id `news`.

```html
<div id="news">
	<h2>News</h2>
	<p>
		Lorem ipsum dolor sit amet, consectetur adipiscing elit.
		Sed non risus. Suspendisse lectus tortor, dignissim sit amet,
		adipiscing nec, ultricies sed, dolor. Lorem ipsum dolor sit amet, 
        consectetur adipiscing elit.
	</p>
</div>
```

Vous pouvez maintenant lier à cette section (div) en utilisant la balise d'ancrage. Pour ce faire, utilisez simplement l'id de la section avec un `#` comme préfixe pour la valeur `href`.

```html
<a href="#news">Aller</a>
```

Ainsi, lorsque vous cliquez sur le lien `Aller`, vous ferez défiler jusqu'à la section des nouvelles de la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/link-page.gif)
_Démonstration du lien dans la page. Vous pouvez l'essayer en utilisant l'application Anchors._

### Comment lier à un client de messagerie

Vous pouvez avoir besoin d'ouvrir le client de messagerie par défaut avec l'adresse email lorsque les utilisateurs cliquent sur un lien. Vous pouvez faire cela en utilisant le protocole `mailto` comme valeur de l'attribut `href`. La syntaxe de la valeur doit être sous la forme `mailto:<adresse email>`.

```html
<a href="mailto:me@example.com">Envoyer un email</a>
```

Maintenant, en cliquant sur le lien `Envoyer un email`, vous ouvrirez le client de messagerie par défaut sur votre système d'exploitation avec l'adresse email (me@example.com) spécifiée dans le champ `À`.

De même, vous pouvez utiliser la construction `tel:<Numéro de téléphone>` pour ouvrir l'application téléphone par défaut avec le numéro de téléphone lorsque quelqu'un clique sur le lien.

```html
<a href="tel:+914123456765">Appeler +914123456765</a>
```

### Comment lier à un script et l'exécuter

Vous pouvez lier à du code JavaScript et l'exécuter lorsque quelqu'un clique sur le lien. Vous ne devriez pas faire cela souvent, car il est toujours préférable de s'appuyer sur des gestionnaires d'événements pour exécuter des actions plutôt que de les lier. Mais apprenons aussi cette méthode.

```html
<a href="javascript:alert('Hello World!')">Cliquez ici</a>
```

Maintenant, si vous cliquez sur le lien `Cliquez ici`, vous verrez une alerte du navigateur avec le texte `Hello World!` dedans.

### Comment télécharger un fichier

La balise d'ancrage a l'attribut `download` qui transforme un lien régulier en un lien de téléchargement. Vous pouvez télécharger un fichier en cliquant sur le lien. Cela ouvre la fenêtre contextuelle de téléchargement pour enregistrer le fichier sur l'appareil.

```html
<a href="./images/rajni.jpg" download="Thalaiva">Télécharger</a>
```

Vous pouvez éventuellement spécifier un nom de fichier personnalisé en attribuant le nom à l'attribut `download`. Il n'est pas nécessaire de spécifier l'extension du fichier lors de la spécification du nom personnalisé. Elle sera ajoutée automatiquement en fonction de l'extension du fichier que vous essayez de télécharger.

Notez que cette fonctionnalité ne fonctionne que si le fichier est de la `même origine`. Le fichier que vous téléchargez doit être situé sous le même site où le lien est ajouté.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Download.gif)
_Démonstration du lien de téléchargement. Veuillez l'essayer en utilisant l'application Anchors._

Consultez ce tweet,

%[https://twitter.com/tapasadhikary/status/1470260903257858058]

### Comment ouvrir une page dans une nouvelle fenêtre/onglet

Vous ne voulez peut-être pas que vos utilisateurs soient trop distraits de ce qu'ils font lorsqu'ils cliquent sur un lien. Vous voulez peut-être ouvrir la page dans une nouvelle fenêtre/onglet du navigateur lorsque l'utilisateur clique sur le lien sur une page actuelle. Nous pouvons utiliser l'attribut `target` à cette fin.

```html
<a href="https://example.com" target="_blank">Cliquez ici</a>
```

L'attribut target peut avoir les valeurs suivantes,

* `_blank` : c'est l'option la plus utilisée. Vous pouvez ouvrir la page liée dans une nouvelle fenêtre/onglet en définissant la valeur de l'attribut target sur _blank.
* `_self` : c'est la valeur par défaut. Elle permet d'ouvrir la page liée dans le même cadre de fenêtre.
* `_top` : cela ouvre la page liée dans la fenêtre supérieure.
* `_parent` : cela ouvre la page liée dans le cadre parent.

Nous verrons comment utiliser les deux dernières valeurs lorsque nous discuterons du lien avec les cadres dans un instant.

### Lien d'ancrage et Tabnabbing

Le `Tabnabbing` est un type d'attaque de cybersécurité où l'attaquant profite du fait que l'utilisateur s'éloigne de la page actuelle et introduit une attaque de `Phishing`.

Supposons que vous naviguez sur un site web et cliquez sur un lien pour ouvrir la page dans un nouvel onglet/fenêtre (rappellez-vous `target=_blank` ?). Maintenant, l'attaquant prend le contrôle de l'objet `window` du navigateur et manipule (redirige) la page source vers un site web similaire avec quelques changements pour vous piéger.

Ces quelques changements pourraient être un formulaire de `connexion` où vous fournissez accidentellement vos identifiants, et l'attaquant gagne. Cela s'appelle le `Tabnabbing`.

Pour protéger les utilisateurs d'une attaque comme le `Tabnabbing`, vous devez passer quelques valeurs à l'attribut `rel` d'une balise d'ancrage :

* `noopener` : rend le contexte du navigateur d'ouverture inconnu en définissant l'objet `window.opener` comme `null`. Cela signifie que l'attaquant n'a aucun moyen de rediriger la page source.
* `noreferrer` : cela garantit que l'en-tête `referrer` ne sera pas inclus lorsque le lien est cliqué. Vous devez définir cette valeur pour les anciens navigateurs.

Ainsi, la manière plus sécurisée d'utiliser la valeur `target=_blank` est avec l'attribut `rel`, comme ceci :

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
```

### Comment lier avec des cadres et des pages enfants

Vous pouvez inclure un autre document HTML sur la page actuelle en utilisant la balise `<iframe>`.

```html
<iframe src="./child-frame.html" frameborder="0"></iframe>
```

Ensuite, le `chlid-frame.html` peut avoir un autre iframe pour inclure un autre document HTML.

```html
<div class="child-frame">
  Je suis le cadre enfant.
  <iframe src="./grand-child-frame.html" frameborder="0"></iframe>
</div>
```

Maintenant, comment lier au cadre parent depuis la page grand-child.html ? De plus, comment lier au cadre de fenêtre le plus haut ?

```html
<li>
    <a href="https://example.com" target="_parent">Ouvre dans le cadre parent (target: _parent)</a>
    <a href="https://example.com" target="_top">Ouvre dans le corps complet de la fenêtre (target: _top)</a>
</li>

```

Comme le montre le code ci-dessus, nous utilisons la cible `_parent` pour lier au cadre parent. La valeur de cible `_top` lie au cadre de la fenêtre.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/context.gif)
_Vérifiez les différences entre les deux clics de lien. Essayez-le en utilisant l'application Anchors._

### Comment ping en arrière-plan

Vous pouvez vouloir `suivre` combien de clics un lien particulier reçoit sur votre site web. Pour ce faire, vous pouvez utiliser l'attribut `ping` de la balise d'ancrage.

Un attribut `ping` accepte une ou plusieurs `URL` comme valeurs. Lorsque quelqu'un clique sur le lien, il effectue une petite `requête POST` sur ces URL. S'il y a plusieurs URL, elles doivent être séparées par des virgules.

```html
<a href="https://example.com" ping="https://example.com/tracking">Avec un Ping</a>
```

# Comment styliser une balise d'ancrage

La balise d'ancrage a des états. L'état par défaut est appelé `link`. Les trois autres états sont :

* `hover` : Une ancre a cet état lorsque l'utilisateur passe la souris dessus.
* `active` : Une ancre a cet état lorsque l'utilisateur clique sur le lien.
* `visited` : Un état visité signifie qu'un utilisateur a déjà cliqué sur le lien d'ancrage.

Vous pouvez être confus avec les différences entre les états `active` et `visited` à certains moments. L'état `active` est bref. Il s'active juste lorsque l'utilisateur clique sur un lien, puis l'état change en état `visited`.

CSS dispose de pseudo-classes pour appliquer des styles à un état spécifique. Les pseudo-classes sont précédées d'un symbole deux-points (:) et ajoutées après un sélecteur. Ainsi, pour la balise d'ancrage (), nous pouvons la styliser pour tous les états que nous avons vus ci-dessus.

* `a:link` : identique à l'application de styles à la balise `a` directement.
* `a:hover` : applique des styles lorsque l'utilisateur passe la souris sur l'ancre.
* `a:active` : applique des styles lorsque l'utilisateur active le lien en cliquant dessus.
* `a:visited` : applique des styles lorsque l'état change en `visited`.

Voici un exemple d'application de différentes couleurs pour chaque état de la balise d'ancrage :

```html
a:link {
    color: #ff3e00;
}

a:hover {
    color: #ffee00;
}

a:active {
    color: #d900ff;
}

a:visited {
    color: #51ff00;
}


```

Vous pouvez appliquer n'importe quel style de votre choix en fonction de ces changements d'état.

# Ne confondez pas la balise d'ancrage avec la balise de lien

Vous pouvez parfois confondre la balise `anchor` avec la balise `link` (<link>). Nous utilisons la balise `link` pour lier des ressources externes comme des feuilles de style, des favicons, des polices, etc.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500&display=swap" rel="stylesheet">

<link rel="stylesheet" href="main.css">

<link rel="icon" href="./images/fav.ico">
```

Nous avons déjà appris que le but principal de la balise d'ancrage (<a>) est de lier une page HTML à une autre. De plus, il s'agit d'un `hyperlien` sur lequel vous pouvez cliquer pour accéder au document cible.

# Avant de partir

C'est tout pour l'instant. J'espère que vous avez trouvé l'article perspicace et informatif. Mes DM sont ouverts sur `Twitter` si vous souhaitez discuter davantage.

Restons en contact. Je partage mes apprentissages sur JavaScript, le développement web et le blogging sur ces plateformes également :

* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary)
* [Abonnez-vous à ma chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1)
* [Projets secondaires sur GitHub](https://github.com/atapas)

Avant de terminer, voici le lien du projet GitHub de l'application `Anchors` que nous avons utilisée dans cet article. N'hésitez pas à l'utiliser, à la fork ou à l'améliorer.

%[https://github.com/atapas/anchors]

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.