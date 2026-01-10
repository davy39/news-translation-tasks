---
title: Comment utiliser les cookies pour personnaliser le contenu d'une page web
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2023-05-30T22:04:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-cookies-to-customize-web-page-content
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/vyshnavi-bisani-z8kriatLFdA-unsplash.jpg
tags:
- name: cookies
  slug: cookies
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les cookies pour personnaliser le contenu d'une page web
seo_desc: "If you develop websites or web apps, someday you’ll have to deal with cookies.\
  \ That’s why I decided to write this tutorial on how to use cookies to customize\
  \ a web page according to the previous web page the user comes from. \nI wrote this\
  \ tutorial us..."
---

Si vous développez des sites web ou des applications web, un jour ou l'autre, vous devrez gérer les cookies. C'est pourquoi j'ai décidé d'écrire ce tutoriel sur la façon d'utiliser les cookies pour personnaliser une page web en fonction de la page précédente d'où vient l'utilisateur. 

J'ai écrit ce tutoriel en utilisant PHP, mais vous pouvez également définir des cookies en utilisant d'autres langages de programmation populaires tels que Java, Python, et autres.

Avant d'entrer dans les détails, passons par une brève introduction et quelques recommandations.

## Qu'est-ce que les Cookies ?

Les cookies jouent un rôle vital dans le fonctionnement des sites web. Ils peuvent également améliorer l'expérience de navigation d'un utilisateur. 

En termes simples, un cookie est un petit fichier que les sites web stockent sur l'ordinateur ou l'appareil d'un utilisateur pendant qu'il navigue à travers diverses pages web. Ces fichiers contiennent des données qui sont utilisées par les sites web pour se souvenir de certaines informations et paramètres, améliorant ainsi la performance et la personnalisation du site web pour l'utilisateur.

Lorsque l'utilisateur visite un site web, le serveur du site envoie un cookie au navigateur de l'utilisateur, qui le stocke ensuite sur son ordinateur ou son appareil. La prochaine fois que l'utilisateur visite le même site web, le navigateur envoie le cookie stocké au serveur. Cela permet au site web de reconnaître l'utilisateur, de se souvenir de ses préférences et de fournir un contenu personnalisé.

Les cookies servent diverses fonctions, telles que se souvenir des informations de connexion, des préférences linguistiques et du contenu du panier d'achat. 

Par exemple, lorsque vous visitez un site web de shopping en ligne et ajoutez des articles à votre panier, les cookies aident à conserver ces articles même si vous naviguez vers d'autres pages. Les cookies peuvent également se souvenir de vos détails de connexion, afin que vous n'ayez pas à les ressaisir chaque fois que vous visitez un site web.

Les cookies peuvent également être utilisés pour suivre le comportement des utilisateurs et recueillir des informations sur l'utilisation du site web. Ces informations sont souvent anonymes et aident les propriétaires de sites web à analyser les schémas de trafic, à identifier les pages populaires et à améliorer la conception et la fonctionnalité de leur site web. 

Les annonceurs utilisent également les cookies pour diffuser des publicités ciblées en fonction des habitudes de navigation et des intérêts des utilisateurs. Cela leur permet de montrer des annonces pertinentes qui sont plus susceptibles d'intéresser l'utilisateur.

### Une note sur les cookies et la vie privée des utilisateurs

Les cookies sont conçus pour être un outil d'amélioration de l'expérience utilisateur et de la fonctionnalité des sites web. Mais les préoccupations concernant la vie privée et la sécurité ont conduit au développement de réglementations et de directives pour l'utilisation des cookies. De nombreux sites web fournissent désormais des avis de consentement aux cookies, permettant aux utilisateurs de choisir s'ils veulent accepter ou rejeter les cookies.

Au cours des dernières décennies, l'utilisation des cookies a fait l'objet de discussions approfondies par les organismes de réglementation, soulignant l'importance de s'assurer que les utilisateurs sont pleinement informés de leur mise en œuvre. 

Des progrès ont été réalisés dans cette direction, notamment l'introduction du Règlement général sur la protection des données (RGPD) par l'Union européenne (UE). Pour des informations plus complètes, vous pouvez obtenir des informations détaillées sur le portail web officiel de l'UE. 

Si vous envisagez l'intégration de cookies dans votre application, je vous recommande vivement de discuter des implications avec le département juridique de votre entreprise ou de consulter des professionnels du droit qui possèdent une expertise dans ce domaine. En faisant cela, vous pouvez garantir la conformité avec les cadres juridiques et réglementaires régissant l'utilisation des cookies, protégeant ainsi la vie privée des utilisateurs.

## Commençons

Supposons que je gère un site de commerce électronique pour les amoureux des animaux de compagnie, et que je mets en œuvre une stratégie de marketing de contenu pour attirer de nouveaux clients. 

Je crée une page d'information pour les amoureux des chats et une autre pour les amoureux des chiens. Les deux pages pointent vers la même page où je donne plus de détails sur le fait d'avoir des animaux de compagnie. 

Je veux que cette page affiche des publicités spécifiques (ciblées) en fonction de la page d'où vient l'utilisateur : s'ils ont visité la page sur les chats, je veux qu'ils voient des publicités sur la nourriture pour chats. S'ils ont visité celle sur les chiens, je veux qu'ils voient des publicités sur la nourriture pour chiens.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-124.png)

## Codons

Je construis trois pages :

1. Page pour les amoureux des chats : mainPageCat.php (capture d'écran ci-dessous)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-125.png)

2. Page pour les amoureux des chiens : mainPageDog.php

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-126.png)

3. La page cible : cookieTest.php

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-127.png)

Lors de la construction des pages 1 et 2, je définis des cookies en utilisant la fonction PHP `setcookie()`. Pour la page sur les chats, je passe à la fonction ces paramètres :

```php
<?php
$cookie_name = "cat";
$cookie_value = "catFoodAds";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 jour
?>
```

Pour la page sur les chiens, je passe ces paramètres :

```php
<?php
$cookie_name = "dog";
$cookie_value = "dogFoodAds";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 jour
?>
```

Pour la page "d'informations supplémentaires", j'ajoute une logique. Si le cookie chat est stocké, j'ajoute une classe CSS à la carte des publicités pour chiens pour la masquer. Je fais de même avec la carte des publicités pour chats si le cookie stocké est celui de la page des chiens.

```php
<div class="row">
			<div class="col-md-3">
				<div class="card <?php if(isset($_COOKIE['dog'])) echo ' cookieClass'; ?>" style="width: 18rem;">
					<img class="card-img-top" src="https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDl8fHxlbnwwfHx8fA%3D%3D&w=1000&q=80" alt="Card image cap">
					<div class="card-body">
						<h5 class="card-title">Acheter de la nourriture pour chats</h5>
						<h6 class="card-subtitle mb-2 text-muted">Excellente nourriture</h6>
						<p class="card-text">Je ne sais pas quoi dire d'autre sur la nourriture pour chats.</p>
						<a href="#" class="card-link">Acheter</a>
					</div>
				</div>
			</div>
			<div class="col-md-3">
				<div class="card ml-5 <?php if(isset($_COOKIE['cat'])) echo ' cookieClass'; ?>" style="width: 18rem;">
					<img class="card-img-top" src="https://images.unsplash.com/photo-1561037404-61cd46aa615b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MXwxMTU1Mjc2N3x8ZW58MHx8fHw%3D&w=1000&q=80" alt="Card image cap">	
					<div class="card-body">
						<h5 class="card-title">Acheter de la nourriture pour chiens</h5>
						<h6 class="card-subtitle mb-2 text-muted">Excellente nourriture</h6>
						<p class="card-text">Je ne sais pas quoi dire d'autre sur la nourriture pour chiens.</p>
						<a href="#" class="card-link">Acheter</a>
					</div>
				</div>
			</div>
		</div>
```

## Voyons comment cela fonctionne

Je teste le flux en tant qu'utilisateur qui souhaite visiter la page sur les chats. Je tape dans la barre d'URL de mon navigateur :

https://<base_url>/mainPageCat.php

Comme vous pouvez le voir, je vois la page que j'ai construite et le cookie est stocké dans mon navigateur

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-128.png)

Si je clique sur l'appel à l'action (bouton bleu), je vois la page de détails supplémentaires avec uniquement les publicités pour nourriture pour chats :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-129.png)

Testons maintenant le flux pour les amoureux des chiens. D'abord, je supprime les cookies de mon navigateur (ou utilise le mode incognito) puis je visite cette URL :

https://<base_url>/mainPageDog.php

Voici ce que je vois :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-130.png)

Comme nous pouvons le voir à nouveau, je vois la page que j'ai construite et le cookie est stocké dans mon navigateur

Si je clique sur l'appel à l'action (bouton bleu), je vois la page de détails supplémentaires avec uniquement les publicités pour nourriture pour chiens.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-131.png)

Terminé ! Voici un exemple simple et rapide de la façon dont vous pouvez utiliser les cookies pour personnaliser le contenu de vos pages web. Vous pouvez trouver le dépôt Github [ici](https://github.com/mventuri/cookiesPhp) avec le code complet.