---
title: Comment intégrer un site web statique avec WordPress
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2021-10-26T17:09:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-a-static-website-with-wordpress
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/cover.png
tags:
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: Comment intégrer un site web statique avec WordPress
seo_desc: "Lots of people still use static websites, from family-run businesses who\
  \ don't need to update information that often, to large teams who need to release\
  \ something quickly without spending too much time and effort on it. \nYou might\
  \ also want a static ..."
---

Beaucoup de gens utilisent encore des sites web statiques, des entreprises familiales qui n'ont pas besoin de mettre à jour les informations très souvent, aux grandes équipes qui doivent publier quelque chose rapidement sans y consacrer trop de temps et d'efforts. 

Vous pourriez également vouloir un site web statique pour ces raisons :

1. Vitesse : les pages se chargent rapidement
2. Compétences minimales requises : les développeurs web qui n'ont pas beaucoup d'expérience peuvent facilement travailler sur le projet
3. L'hébergement est facile : le marché d'aujourd'hui offre une variété d'options pour héberger votre site web statique (comme AWS S3, Azure Storage, Netlify, et autres)

Jusqu'à présent, nous avons parlé des raisons pour lesquelles vous pourriez choisir un site web statique et de leurs avantages. 

Mais que faire si vous souhaitez ajouter du contenu rapidement à votre site web ou mettre à jour seulement une section de celui-ci ? Que faire si vous souhaitez ajouter un blog à votre site web pour attirer de nouveaux visiteurs ?

C'est un problème que j'ai dû résoudre plusieurs fois dans le passé : des clients m'ont demandé d'ajouter du contenu dynamique à leurs sites web et ils n'avaient ni budget ni temps pour créer un nouveau projet. Heureusement, WordPress m'a aidé à trouver une solution. Voyons comment.

## Comment WordPress m'a aidé

WordPress est la référence dans l'industrie pour le blogging et la publication rapide de contenu. Le tableau de bord est intuitif et facile à utiliser. Les administrateurs peuvent également ajouter de nouveaux utilisateurs et spécifier – en sélectionnant le rôle approprié – leurs permissions.

WordPress expose des API Rest pour aider les développeurs à construire des intégrations avec WordPress lui-même et des services tiers.

J'ai donc décidé d'intégrer un blog WordPress avec le site statique de mon client en appelant le point de terminaison `/wp/v2/posts` fourni par les API WordPress. Dans les étapes suivantes, je vais expliquer comment je l'ai fait et pourquoi.

## Installation du projet

Tout d'abord, je veux partager le site web sur lequel je vais travailler dans cet article. Rien de trop sophistiqué : j'ai choisi ce modèle statique Bootstrap :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/bootstrap_template.png)

Comme vous pouvez le voir, nous pouvons diviser la page en trois sections principales différentes :

1. Présentation de l'entreprise (image + slogan)
2. Une carte d'appel à l'action (la zone grise au milieu)
3. Une rangée avec trois cartes

J'intégrerai notre blog WordPress dans la troisième section.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/bootstrap_template_card.png)

Chaque article sera représenté par une carte, où les utilisateurs pourront lire le titre de l'article, l'extrait, et accéder au contenu de l'article en cliquant sur le bouton bleu "Lire la suite". Le bouton ouvrira une modale où le contenu de l'article sera affiché.

## Voyons comment fonctionne notre instance WordPress

Jetons un coup d'œil à notre instance WordPress et voyons ce que nous avons. Si je me connecte au tableau de bord et que je vais dans la section des articles, je vois que j'ai publié trois articles : Article No. 1, Article No. 2, et Article No. 3. 

Chaque article contient du contenu "Lorem ipsum". Donc, à la fin de cet article, je m'attends à ce que ces articles soient affichés dans trois cartes différentes comme mentionné ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/elenco_post_wp.png)

## Comment travailler avec les API WordPress

Les API WordPress sont bien [documentées](https://developer.wordpress.org/rest-api/) et maintenues par une communauté énorme et enthousiaste. Voyons comment je peux gérer les articles avec les API disponibles. 

Donc, une fois sur la page de documentation, je clique sur "Endpoint Reference" puis sur "posts". Comme je l'ai dit avant, je veux récupérer tous les articles que j'ai publiés sur mon instance. Je vais à "List Posts" et je lis "Interrogez ce point de terminaison pour récupérer une collection d'articles. La réponse que vous recevez peut être contrôlée et filtrée en utilisant les paramètres de requête URL ci-dessous."

Cela semble être ce que je cherche. Selon la documentation, voici la requête :

```terminal
https://<BASE_URL>/wp-json/wp/v2/posts
```

Avant de commencer l'implémentation, je la teste en utilisant Postman. Voici ce que j'obtiens :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/postman.png)

Comme prévu, j'obtiens un JSON avec les informations relatives aux articles que j'ai créés sur mon instance WordPress. 

## Temps de coder

Pour compléter cette implémentation, je vais modifier index.html et je vais créer un nouveau fichier appelé blog.js.

Dans index.html, je vais supprimer les cartes statiques, ajouter un chargeur pour le faire apparaître pendant l'attente de la réponse de l'appel API, et ajouter un id – "wrapper" – à l'élément DOM où je veux que les cartes des articles apparaissent. Cela ressemble à ceci :

```html
<div id="wrapper" class="row gx-4 gx-lg-5">
	<div id=spinner class="text-center">
		<div class="spinner-grow spinner-grow-lg">
			<span class="visually-hidden">Chargement...</span>
		</div>
	</div>
</div>
```

Dans le fichier blog.js, je récupère l'URL et le premier `.then()` vérifie si la réponse est correcte :

```javascript
fetch('https://<BASE_URL>/wp-json/wp/v2/posts').then(function (response) {
	if (response.ok) {
        return response.json();
	} else {
		return Promise.reject(response);
	}
})
```

En utilisant un second `then()`, je supprime le chargeur du DOM et je mappe à la fois la carte et la modale pour chaque article que je trouve dans le JSON. Je choisis d'afficher seulement les trois derniers articles du blog. Cela ressemble à ceci :

```javascript
.then(function (data) {
    spinner.remove()
    for (let i = 0; i < 3; i++) {
      
        cardCreation = '<div class="col-md-4 mb-5">'
        cardCreation += '<div class="card h-100">'
        cardCreation += '<div class="card-body">'
        cardCreation += '<h2 id="test" class="card-title">' + data[i].title.rendered + '</h2>'
        cardCreation += '<p class="card-text">' + data[i].excerpt.rendered + '</p>'
        cardCreation += '</div>'
        cardCreation += '<div class="card-footer"><button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#modal-' + data[i].id + '">Lire la suite</button></div>'
        cardCreation += '</div>'
        cardCreation += '</div>'

        modalCreation = '<div class="modal fade" id="modal-' + data[i].id +'" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">'
        modalCreation += '<div class="modal-dialog" role="document">'
        modalCreation += '<div class="modal-content">'
        modalCreation += '<div class="modal-header">'
        modalCreation += '<h5 class="modal-title" id="exampleModalLongTitle">' + data[i].title.rendered + '</h5>'
        modalCreation += '</div>'
        modalCreation += '<div class="modal-body">' + data[i].content.rendered + '</div>'
        modalCreation += '<div class="modal-footer">'
        modalCreation += '<button type="button" class="btn btn-secondary" data-dismiss="modal">Fermer</button>'
        modalCreation += '</div>'
        modalCreation += '</div>'
        modalCreation += '</div>'
        modalCreation += '</div>'
  
        document.querySelector("#wrapper").insertAdjacentHTML("beforeend",cardCreation)
        document.querySelector("#wrapper").insertAdjacentHTML("beforeend",modalCreation)
      }
})
```

Enfin, j'utilise la méthode `catch()` pour gérer les erreurs. J'ai décidé d'ajouter une bannière d'erreur Bootstrap où j'explique qu'un problème est survenu et j'ajoute un lien vers des ressources que les utilisateurs peuvent trouver utiles :

```javascript
.catch(function (err) {
    spinner.remove();
    errorMsg = '<div class="alert alert-danger" role="alert">'
    errorMsg += 'Désolé, nous ne pouvons pas récupérer les articles pour le moment. Veuillez visiter www.notreblog.com'
    errorMsg += '</div>'

    document.querySelector("#wrapper").insertAdjacentHTML("beforeend",errorMsg)

	console.warn('Quelque chose s\'est mal passé.', err);
});
```

J'ouvre le fichier index.html avec mon navigateur et maintenant je vois les cartes affichant les articles de mon blog WordPress

![Image](https://www.freecodecamp.org/news/content/images/2021/10/bottstrap_con_post_wp.png)

Pour tester si tout fonctionne bien, j'ajoute un nouvel article à mon blog. Voici ce que je vois sur mon site web statique :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/4posts.png)

Et si je clique sur "Lire la suite", je vois le contenu complet de l'article dans une modale :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/modal.png)

C'est ainsi que j'ai intégré un site web statique et un blog WordPress. Vous pouvez trouver le code complet [ici](https://github.com/mventuri/How-to-integrate-a-static-website-with-WordPress). J'espère que vous avez trouvé cet article utile. N'hésitez pas à le partager ! 😀