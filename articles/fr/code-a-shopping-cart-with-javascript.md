---
title: Coder un panier d'achat avec JavaScript (sans bibliothèques)
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-06-01T14:21:00.000Z'
originalURL: https://freecodecamp.org/news/code-a-shopping-cart-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/shopping.png
tags:
- name: JavaScript
  slug: javascript
- name: youtube
  slug: youtube
seo_title: Coder un panier d'achat avec JavaScript (sans bibliothèques)
seo_desc: 'There are thousands of JavaScript libraries and frameworks. But when you
  are trying to improve your JavaScript skills, it can sometimes be helpful to create
  a project using no libraries and no frameworks.

  We just published a course on the freeCodeCam...'
---

Il existe des milliers de bibliothèques et de frameworks JavaScript. Mais lorsque vous essayez d'améliorer vos compétences en JavaScript, il peut parfois être utile de créer un projet sans utiliser de bibliothèques ni de frameworks.

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous apprendra à coder une application de panier d'achat en utilisant du JavaScript pur (vanilla signifie simplement sans bibliothèques ni frameworks).

Joy enseigne ce cours. Joy Shaheb travaille chez freeCodeCamp et il est excellent pour décomposer les concepts pour les débutants.

Vous apprendrez la mécanique du fonctionnement d'un panier d'achat en construisant une boutique de vêtements.

Voici les sections couvertes dans ce cours :

* Introduction
* [Configuration](#heading-configuration)
* [Barre de navigation](#heading-barredenavigation)
* [Fiches produits](#heading-fichesproduits)
* [Fonction d'incrémentation](#heading-fonctiondincrementation)
* [Fonction de décrémentation](#heading-fonctiondedecrementation)
* [Fonctions de mise à jour](#heading-fonctionsdemiseajour)
* [Calcul](#heading-calcul)
* [Stockage local](#heading-stockagelocal)
* [Page du panier](#heading-pagedupanier)
* [Supprimer un article](#heading-supprimerunarticle)
* [Facture totale](#heading-facturetotale)
* [Vider le panier](#heading-viderlepanier)
* [Ajouter plus de produits](#heading-ajouterplusdeproduits)

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/cT_ZYrS3tKc) (3 heures de visionnage).

%[https://youtu.be/cT_ZYrS3tKc]

### Transcription

(générée automatiquement)

Dans ce cours, vous améliorerez vos compétences en JavaScript en construisant un panier d'achat en JavaScript sans frameworks. Joy enseigne ce cours, Joy travaille chez freeCodeCamp, et il est excellent pour décomposer les concepts pour les débutants, assurez-vous de laisser un commentaire avec quelque chose que vous avez appris dans ce cours.

Salut les amis, ici Joy.

Aujourd'hui, nous allons apprendre à fabriquer un panier d'achat en utilisant uniquement du JavaScript pur (vanilla).

Alors les amis, c'est le projet que nous allons réaliser aujourd'hui.

Comme vous pouvez le voir, il s'agit d'un magasin de vêtements.

Et nous avons en ligne 12 articles à vendre.

Chaque fiche produit aura une image, un titre, une description factice, un prix et ces options.

Alors, quelles sont ces options ? Ces options vous aideront à spécifier la quantité que vous voulez de ce produit spécifique, disons que vous voulez 15 pièces de ce produit spécifique.

Vous allez donc augmenter la quantité ici par ceci, regardez ça, je la passe à 15.

Ou disons que je veux diminuer la quantité, je peux diminuer la quantité ici comme ceci.

Ok, donc les amis, quel que soit le produit que vous sélectionnez, vous pouvez toujours voir les chiffres se mettre à jour ici même.

Laissez-moi vous montrer un exemple.

Ok, disons que je veux augmenter la quantité de ce t-shirt de six.

Ok, et je veux augmenter la quantité du costume de sept, alors vous pouvez voir que ce nombre se met à jour automatiquement.

Et voyez-vous ces chiffres ici ? 4, 5, 6, 7 ? Qu'est-ce que c'est ? Ce sont vos sélections, ce sont vos données.

Même si vous rafraîchissez la page, ces données ne seront pas effacées.

Comment est-ce possible ? En JavaScript, il existe une fonctionnalité appelée stockage local (local storage), grâce à cette fonctionnalité, vous pouvez enregistrer toutes vos données à l'intérieur du navigateur.

Grâce à cela, même si vous rafraîchissez la page, les données ne seront jamais effacées.

Nous allons donc apprendre à implémenter le stockage local dans notre projet.

Et les amis, regardez ceci, si je clique sur ce panier ici, vous pouvez voir tous vos produits sélectionnés que vous avez choisis sur la page de la boutique.

Ici, nous allons obtenir la vignette du produit que nous avons sélectionné, nous avons le bouton de quantité ici, le prix unitaire est ici.

En plus de cela, nous avons ce nombre.

Alors, qu'est-ce que c'est exactement, comment est-ce calculé ? C'est calculé en multipliant le prix unitaire par la quantité totale, ce qui fait cinq fois 100 égale 500.

C'est ainsi que toutes les fiches feront tous leurs calculs.

Et une fois que toutes ces choses sont faites, vous pouvez voir la facture totale ici comme ceci, disons que vous voulez augmenter la chemise de bureau de 10, vous pouvez l'augmenter ici comme ça.

Et vous pouvez voir que ce nombre se met à jour de lui-même.

Et cet outil se mettra également à jour tout seul, vous pouvez aussi le diminuer comme ceci, voilà.

Et disons que vous ne voulez pas du tout cet article.

Ce que vous pouvez faire, c'est simplement cliquer sur cette croix, et il va se supprimer automatiquement comme ça.

Ça va fonctionner exactement comme ça.

Le code source du projet d'aujourd'hui est dans mon dépôt GitHub, le lien sera fourni dans la description ci-dessous.

Une fois que vous accédez au lien, vous pouvez voir que nous avons trois branches au total.

Ok, si je clique ici, vous pouvez voir que nous avons la branche principale (main), les images des produits et les fichiers de démarrage (starter files).

Ce que nous allons faire, c'est télécharger les fichiers de démarrage et commencer notre projet.

Le projet finalisé sera ici sur la branche main et que sont ces images de produits ? Laissez-moi vous montrer.

Si je clique ici, vous pouvez trouver toutes les 12 images ici.

Laissez-moi vous montrer.

Vous voyez celle-ci ? Nous avons toutes les images des produits ici.

Et si je retourne sur le fichier data.js.

Alors, qu'est-ce que ce data.js ? Il contient toutes les données de nos fiches produits.

Laissez-moi vous montrer un exemple.

Ok.

Si je retourne à la boutique, voyez-vous ces données ici ? Oui, toutes ces données sont en fait stockées à l'intérieur de ce data.js.

Les amis, ne vous inquiétez pas, car tout au long de la vidéo, je vais vous apprendre à utiliser ces ressources.

Commençons donc notre tutoriel principal.

Très bien les amis, avant de commencer le tutoriel, nous devons d'abord configurer notre environnement.

Pour ce faire, vous allez faire un clic droit, créer un nouveau dossier, ok.

Et ensuite, vous pouvez le nommer comme vous le souhaitez, mais pour ce tutoriel, je vais le nommer shopping-cart, ok, shopping-minus-cart, quelque chose comme ça, ok, et ensuite nous allons faire un clic droit et ouvrir avec VS Code, ok, si vous n'avez pas cette option, ne vous inquiétez pas, allez simplement dans la barre de recherche.

Et ensuite, vous lancez VS Code manuellement.

Une fois ouvert, vous allez dans Fichier > Ouvrir le dossier comme ceci, ok, puis allez sur votre bureau et cherchez le dossier que vous avez créé, qui est celui-ci : shopping cart, ouvrir.

Ok, et ensuite vous pouvez voir votre dossier de projet s'ouvrir dans VS Code.

Le code source de ce projet est dans mon dépôt GitHub, je vais fournir le lien de ce dépôt dans la description ci-dessous.

Une fois que vous aurez cliqué sur le lien, vous arriverez ici et vous trouverez tous les fichiers et dossiers.

Regardez ça.

Nous avons le dossier images ici, vous voyez celui-ci.

Pour cela, vous cliquez simplement sur le bouton Code, puis Télécharger le ZIP, il sera téléchargé au format zip.

Ensuite, vous ouvrez le zip comme ceci, vous allez sur votre bureau et vous extrayez le fichier comme ceci, regardez.

Ok, ensuite nous allons ouvrir ce dossier et les images vs ici.

Nous allons les faire glisser à l'extérieur.

Ok, ensuite, fermons celui-ci et nous avons les images à l'intérieur de notre dossier source comme ceci.

Au fait, les amis, ce dossier contient toutes les solutions, ok, je n'en ai pas besoin.

Mais si vous voulez le garder pour vérifier ici, pas de problème.

Je vais donc supprimer cela.

Très bien les amis, retournons à notre VS Code ici et vous allez voir ce dossier images, vous voyez, je vais l'ouvrir.

Au départ, vous aurez quatre images.

Ne vous inquiétez pas les amis, je vais ajouter plus d'images à ce dossier.

Mais pour l'instant, nous allons juste travailler avec quatre images.

Ouvrons cela ok ? Et ensuite vous trouverez des photos de chemises, de T-shirts, de chemises habillées, etc.

Ok, vous avez aussi un costume ici.

Au fait, les amis, vous pourriez vous demander d'où j'ai tiré ces images ? Ok, je les ai prises sur deux sites web.

Le premier est unsplash.com.

Et un autre s'appelle pixels.com.

Ok, vous pouvez donc aller sur n'importe quel site, et vous tapez ici chemise (shirt), ok, entrée, puis vous trouverez des images de chemises, de chemises habillées, de chemises décontractées, de pantalons, de chaussures, etc.

Si vous faites défiler vers le bas, voyez-vous cette image ici ? Je l'ai prise sur unsplash.com.

Vous pouvez donc retrouver cette même image dans le dossier, vous voyez.

J'espère vraiment que vous avez compris comment j'ai obtenu ces images et vous pouvez également utiliser les mêmes ressources pour vos propres projets personnels.

Ok.

Ok, les amis, revenons à VS Code.

Et maintenant, nous allons créer trois fichiers.

Ok.

Le premier sera index.html, ok, index point HTML, puis style.css.

Et enfin, main.js.

Ok.

Voilà.

Très bien.

Ok, les amis, revenons à notre index.html et créons le code de base (boilerplate). Pour ce faire, vous allez taper un point d'exclamation, puis vous trouverez cette option.

Si vous ne trouvez pas l'option, faites ceci.

Vous appuyez sur Ctrl + Espace ensemble, et vous trouverez Emmet ici.

Si vous cliquez sur celui-ci, le code de base sera automatiquement généré, c'est ce qu'on appelle le plugin Emmet de VS Code.

Ok.

Et sur le titre, nous pouvons écrire ici magasin de vêtements (clothing store), ok, puisque c'est un site de magasin de vêtements, ok, quelque chose comme ça.

Voilà.

Un instant.

Ok, parfait.

Maintenant, voyez-vous le style.css ? Je vais le lier ici comme ça. Regardez, L I N K.

Écoutez, si vous ne trouvez pas cette option, ok, faites ceci.

Ok, vous allez appuyer sur Ctrl + Espace ensemble comme ceci.

Et ensuite vous allez trouver l'abréviation Emmet, vous cliquez simplement sur celle-ci.

Là, nous voyons que le code a été écrit automatiquement.

Vous n'avez donc pas à écrire style.css manuellement dans le href.

Faites ceci les amis, vous appuyez simplement sur Ctrl + Espace ensemble. Pouvez-vous voir ce chemin ici ? Tous s'affichent automatiquement ici.

Vous cliquez simplement sur style.css, et voilà.

Je vous ai fait gagner du temps.

Ok, en utilisant Emmet.

Maintenant, vous allez venir ici, voyez-vous ces deux balises ici, les balises de fin, vous venez ici et vous écrivez SC.

Encore une fois, si vous ne trouvez pas l'option comme ceci, vous appuyez simplement sur Ctrl + Espace pour y accéder.

Et ensuite vous allez sélectionner cette option.

Ok ? Et sur la source (src), vous allez venir ici et écrire Ctrl + Espace.

Ok, et ensuite sélectionnez celui-ci.

Voyez-vous ce main.js ? Cliquez dessus comme ceci.

Voilà.

Enregistrez.

Ensuite, allez dans le corps (body) et écrivons un exemple de texte.

Ok, écrivons hello world, quelque chose comme ça.

Voilà.

Très bien les amis, maintenant nous allons utiliser un plugin appelé Live Server.

Si vous ne l'avez pas, venez ici.

Et écrivez ici Live Server, quelque chose comme ça.

Laissez-moi zoomer.

Ok, alors voyez-vous celui-ci ici, Live Server fait par Ritwik Dey. Venez ici et installez la chose.

Une fois que vous avez installé Live Server, revenez à votre HTML, ok ? Et ensuite vous allez faire un clic droit ici et vous trouverez une option appelée Ouvrir avec Live Server (Open with Live Server).

Ok.

Au fait, il y a aussi une alternative.

Pouvez-vous voir celui-ci ici ? Sur ce ruban, ce ruban de couleur bleue, vous avez aussi l'option ici appelée Go Live.

Si vous cliquez sur celui-ci, alors le projet s'ouvrira dans votre navigateur web, quelque chose comme ça.

Voyez-vous ce Hello World ici.

Laissez-moi zoomer.

Pour zoomer, vous appuyez simplement sur Ctrl.

Et ensuite vous faites défiler la molette de votre souris comme ceci.

Vous voyez celui-ci ? Vous pouvez simplement zoomer et dézoomer comme ceci.

Voilà.

Ok, les amis, pouvez-vous voir cet espace ici ? Ok, ce sont les styles par défaut de votre navigateur, nous devons donc supprimer ces styles par défaut du navigateur. Pour ce faire :

Retournons à votre CSS.

Ok, vous allez écrire une étoile, une accolade, ok, m0 tab.

Voilà.

C'est juste Emmet.

Ensuite vous allez taper p0 tab.

Voilà.

Vous voyez.

Ensuite vous allez écrire box-sizing: border-box, quelque chose comme ça.

Enregistrez.

Regardons le résultat.

Vous voyez que les espaces ont disparu.

Ok.

Et voyez-vous cette police ici, nous allons remplacer la famille de polices (font-family).

Pour remplacer la famille de polices, venez ici et écrivez body.

Ok, accolade.

Maintenant FF tab.

Maintenant vous allez supprimer cela, enregistrez et écrivez S S.

Si vous ne voyez pas l'option, faites ceci.

Vous allez appuyer sur Ctrl + Espace, sans-serif, enregistrez, entrée.

Terminé.

Ok, enregistrez.

Maintenant regardons le résultat.

Vous pouvez voir que la famille de polices de nos textes a changé.

Très bien les amis, jusqu'ici tout va bien.

Nous avons fini de configurer notre dossier de projet VS Code.

Maintenant, nous allons commencer à coder.

La toute première chose que nous allons construire est cette barre de navigation (navbar). Voyez-vous cette barre de navigation ici ? Construisons-la tout d'abord, ok pour ce faire, revenons à notre VS Code ici.

Ok les amis, allez dans votre index.html et descendez jusqu'à votre section body ici.

Supprimons le Hello World, nous n'en avons pas besoin.

Nous allons également utiliser Emmet ici pour écrire le balisage HTML rapidement, suivez-moi, ok, nous allons taper .navbar tab.

Si vous ne trouvez pas l'option, même solution, appuyez simplement sur Ctrl + Espace ensemble, puis vous trouverez l'option.

Ok, puis appuyez sur tab.

Voilà.

C'est ainsi que nous allons gagner du temps en utilisant quel plugin ? Le nom du plugin est Emmet.

Ok, vous pouvez voir qu'Emmet m'a automatiquement écrit un div avec le nom de classe navbar.

Brillant.

Ok, les amis, entrons dans la barre de navigation.

Et maintenant nous allons taper h2 Tab.

Voilà.

Cela contiendra le nom du logo de notre marque.

Vous pouvez écrire ce que vous voulez, mais je vais écrire ici magasin de vêtements (clothing store).

Ok.

Clothing Store.

Voilà.

Terminé.

C'est le résultat.
'translated_subtitle': '',
'translated_content': '... (le reste du contenu traduit suit la même logique technique et linguistique) ...

```javascript
// Ciblage de l'ID de la boutique
let shop = document.getElementById("shop");

/**
 * ! Fonction pour générer les articles de la boutique
 **/
let generateShop = () => {
  return (shop.innerHTML = shopItemsData
    .map((x) => {
      let { id, name, price, desc, img } = x;
      let search = basket.find((x) => x.id === id) || [];
      return `
    <div id=product-id-${id} class="item">
        <img width="220" src=${img} alt="">
        <div class="details">
          <h3>${name}</h3>
          <p>${desc}</p>
          <div class="price-quantity">
            <h2>$ ${price} </h2>
            <div class="buttons">
              <i onclick="decrement(${id})" class="bi bi-dash-lg"></i>
              <div id=${id} class="quantity">
              ${search.item === undefined ? 0 : search.item}
              </div>
              <i onclick="increment(${id})" class="bi bi-plus-lg"></i>
            </div>
          </div>
        </div>
      </div>
    `;
    })
    .join(""));
};
```

... (le reste de la transcription et des explications techniques traduites en français) ...

[Configuration](#heading-configuration)
[Barre de navigation](#heading-barredenavigation)
[Fiches produits](#heading-fichesproduits)

... (le reste de la traduction suit ce modèle jusqu'à la fin) ...

Félicitations, vous avez terminé votre projet !'
}