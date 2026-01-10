---
title: 'Maîtriser les bases : comment concevoir la navigation, la recherche et la
  page d''accueil de votre site'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T16:13:43.000Z'
originalURL: https://freecodecamp.org/news/get-the-basics-right-how-to-design-your-sites-navigation-search-and-homepage-adeb57a881f4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*judVnmYTutcBhqRI
tags:
- name: Design
  slug: design
- name: technology
  slug: technology
- name: UI
  slug: ui
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: 'Maîtriser les bases : comment concevoir la navigation, la recherche et
  la page d''accueil de votre site'
seo_desc: 'By Anant Jain

  A 7-minute guide to getting these three foundational components just right.


  _Source: [Unsplash](https://unsplash.com/@naffiq?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Galymzhan Abdugalimov on <a hre...'
---

Par Anant Jain

#### Un guide de 7 minutes pour bien concevoir ces trois composants fondamentaux.

![Image](https://cdn-media-1.freecodecamp.org/images/vIrqY20hUWlVlYv1fOfyvOY4ugEir62exVJL)
_Source : [Unsplash](https://unsplash.com/@naffiq?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Galymzhan Abdugalimov</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Si vous souhaitiez acheter un nouveau marteau dans un magasin de bricolage, imaginez comment vous procéderiez :

* **Option 1** : vous pouvez soit parcourir le magasin — il y a des allées avec des noms de départements en haut et, dans un département, il y a des panneaux à la fin de chaque allée.
* **Option 2** : vous pouvez trouver le vendeur le plus proche et lui demander simplement où se trouvent les marteaux.

Cela peut être un mélange des deux — vous pouvez essayer de naviguer un peu pour voir à quel point c'est facile. Si vous ne trouvez pas ce que vous cherchez, vous pouvez demander à un vendeur.

![Image](https://cdn-media-1.freecodecamp.org/images/sUb9RgTz1vWXzPMUgICxYdEukZGnP6d0lXoC)

Si vous y réfléchissez, c'est exactement ainsi que nous utilisons les sites web. Nous regardons un peu autour de nous (**Navigation**) et, si nous ne trouvons pas ce que nous cherchions, nous utilisons la fonctionnalité **Recherche**. Ce sont les deux composants critiques de votre site. De mineurs défauts d'utilisabilité ici peuvent causer une grande frustration à vos utilisateurs.

Ce court guide, en partie basé sur le livre séminal de Steve Krug « Don’t Make Me Think », vous apprendra à concevoir la Navigation, la Recherche et la Page d'accueil de votre site web. Commençons par la Navigation.

### Concevoir une navigation efficace

#### Pourquoi avons-nous besoin de Navigation ?

Contrairement à notre exemple de magasin de bricolage, un site web n'est pas un espace physique. Il diffère d'un magasin de bricolage de trois manières :

1. Un site web ne donne pas à l'utilisateur un sens de l'**échelle**
2. Un site web ne donne pas à l'utilisateur un sens de la **direction**
3. Un site web ne donne pas à l'utilisateur un sens de la **localisation**

Lorsque nous voulons revenir à quelque chose sur un site web, nous ne pouvons pas compter sur un sens physique de l'endroit où il se trouve. Au lieu de cela, nous devons nous souvenir de l'endroit où il se trouve dans la **hiérarchie conceptuelle** du site web, puis retracer nos pas.

La **Navigation** met cette **hiérarchie conceptuelle** en avant et au centre. Elle devrait idéalement faire partie de chaque page. Elle nous indique ce qu'il y a sur le site web et comment l'utiliser, ce qui en fait une partie critique de l'expérience utilisateur de votre site.

![Image](https://cdn-media-1.freecodecamp.org/images/cKZ17A3SyMsS0maXbcsLBN93030kLfd1xzeb)

#### Comment concevoir la navigation ?

La navigation persistante est l'ensemble des éléments qui apparaissent en haut de **chaque page**. Ils suivent certaines conventions et, sauf si nous avons une raison substantielle, nous devrions nous y conformer :

* **Identifiant du site** en haut à gauche — cela indique à l'utilisateur sur quel site il se trouve (le logo Apple dans la capture d'écran ci-dessus).
* **Sections en haut** — un moyen de naviguer dans les différentes parties du site, avec la section actuelle mise en évidence pour indiquer où vous vous trouvez (par exemple, les sections Mac, iPad et iPhone dans la capture d'écran ci-dessus).
* **Onglets** (optionnel) — les onglets, lorsqu'ils sont bien faits, sont évidents, difficiles à manquer et élégants. Un onglet actif doit être d'une couleur différente et physiquement connecté à l'espace en dessous pour qu'il "ressorte" à l'avant.
* **Utilitaires** comme "Mon Compte", "Suivre votre commande" et "Magasins". Ne mettez pas plus de cinq de ces éléments — le reste peut aller dans la navigation de pied de page.
* **Fils d'Ariane** : il s'agit d'un autre ensemble d'indicateurs "Vous êtes ici", comme la section mise en évidence en haut. Rendez les fils d'Ariane petits et tout en haut d'une page, où ils n'interfèrent pas avec la navigation principale. La meilleure façon de procéder est d'utiliser `&`gt; entre les niveaux, et de mettre en gras le dernier élément (l'élément sur lequel vous vous trouvez actuellement et — puisque vous y êtes — il ne doit pas être un lien).

![Image](https://cdn-media-1.freecodecamp.org/images/54GnJ97ntnTOaeNzAHOo4NyFT6Fhzk7ctev0)
_Fils d'Ariane sur la page produit de Best Buy_

* **Un nom de page** : sur quelle page êtes-vous ? Chaque page web devrait idéalement avoir un nom qui correspond aux mots cliqués pour y accéder. Il doit être proéminent et au bon endroit. Dans la hiérarchie visuelle de la page, il doit sembler encadrer le contenu qui est unique à cette page.
* **Navigation locale** dans la barre latérale gauche (optionnelle) : ce sont les options disponibles au niveau actuel.
* **Navigation de pied de page** : c'est là que vont tous les autres utilitaires.

![Image](https://cdn-media-1.freecodecamp.org/images/nOUQohyFKB02wR8us7BXOmMGNC5i28-a2-we)
_Pied de page sur [NNGroup.com](https://www.nngroup.com" rel="noopener" target="_blank" title=")_

L'un des éléments les plus critiques de la navigation est un lien vers la Page d'accueil, généralement servi par l'Identifiant du site (logo). C'est ce que les utilisateurs cliquent s'ils se perdent — c'est l'ancre qui leur permet de revenir au point de départ s'ils veulent recommencer.

### Faciliter la recherche

Alors, comment concevoir la fonctionnalité de recherche ? Très simplement, faites en sorte que la boîte de recherche soit une boîte simple sans options, mais permettez de limiter la portée de la recherche sur la page des résultats.

De plus, si vous limitez la portée d'une recherche, ajoutez le mot "pour" pour qu'elle se lise comme une phrase : "Rechercher ___ pour ___." Voici un bon exemple alternatif où le texte de l'espace réservé indique que la recherche est limitée à la seule publication :

![Image](https://cdn-media-1.freecodecamp.org/images/f2NVvqtyqvrlO8NsZx1YrPE8X81pZLPIrodW)
_Lorsque la recherche est limitée à la seule publication, la zone de recherche l'indique._

#### Comment savoir si vous avez bien fait le travail avec la navigation ?

Voici un excellent test à faire avec vos amis pour voir si vous avez bien fait le travail avec la navigation. Laissez-les sur une page aléatoire quelque part au fond de votre site web et assurez-vous qu'ils peuvent répondre rapidement à ces questions, et sans hésitation :

* quel est ce site ? (Identifiant du site)
* sur quelle page suis-je ?
* quelles sont les principales sections de ce site ?
* quelles sont mes options à ce niveau ?
* où suis-je dans le schéma des choses ?
* comment puis-je rechercher ?

### Concevoir la page d'accueil

Pour la plupart des sites web, la page d'accueil est la première page sur laquelle les utilisateurs arrivent. C'est aussi l'étoile polaire fixe à laquelle les utilisateurs peuvent revenir s'ils se perdent. Votre Page d'accueil doit répondre à ces cinq questions que chaque utilisateur a en tête lorsqu'il entre sur le site pour la première fois :

1. Qu'est-ce que c'est ?
2. Qu'ont-ils ici ?
3. Que puis-je faire ici ?
4. Pourquoi devrais-je être ici — et pas ailleurs ?
5. Par où commencer...

...si je veux rechercher ?

...si je veux naviguer ?

...si je veux essayer leurs meilleurs produits ?

C'est le travail de la page d'accueil de répondre à ces questions.

Il y a trois endroits cruciaux sur la page d'accueil où les utilisateurs s'attendent à trouver des déclarations explicites sur le site :

1. **Le slogan** : les bons slogans sont clairs et informatifs, et expliquent ce que fait votre site ou organisation. Ils sont juste assez longs, mais pas trop, et transmettent la différenciation — ils ne sonnent pas génériques. Il est utile qu'ils soient personnalisés, vivants et (parfois) spirituels.
2. **Le texte de bienvenue** : assurez-vous qu'il s'agit de quelque chose qui transmet ce que fait le site.
3. **Le « En savoir plus »** : les produits innovants nécessitent souvent une quantité importante d'explications. Les gens se sont habitués à regarder de courtes vidéos sur leurs ordinateurs et appareils mobiles, et sont souvent prêts à en regarder une sur la Page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/B6n9gkmElDG5VDt0dk93ra6LRt5fVcQRfHoz)
_[Commonlounge](https://www.commonlounge.com" rel="noopener" target="_blank" title=") Page d'accueil_

**NN Group** a publié la liste suivante de [10 directives](https://www.nngroup.com/articles/top-ten-guidelines-for-homepage-usability/) pour l'utilisabilité de la page d'accueil, qui sert également de liste de contrôle avant le lancement :

1. Inclure un slogan d'une phrase
2. Écrire un titre de page avec une bonne visibilité dans les moteurs de recherche et les listes de favoris
3. Regrouper toutes les informations corporatives dans une zone distincte
4. Mettre l'accent sur les tâches prioritaires du site
5. Inclure une boîte de recherche
6. Montrer des exemples de contenu réel du site
7. Commencer les noms de liens par le mot-clé le plus important
8. Offrir un accès facile aux fonctionnalités récentes de la page d'accueil
9. Ne pas sur-formater le contenu critique, comme les zones de navigation
10. Utiliser des graphiques significatifs

Voici la liste en action sur leur propre site :

![Image](https://cdn-media-1.freecodecamp.org/images/un9wZKq4vaZQYMrHJv811HDvQtlEtTTrwLSW)
_[NNGroup](https://www.nngroup.com" rel="noopener" target="_blank" title=") Page d'accueil, mettant en œuvre la plupart de leurs directives._

N'oubliez pas que la page d'accueil est une ressource partagée entre tous les départements d'une entreprise — au moins en ce qui concerne ce qui est affiché en premier. Tout ce qui est en haut de la page d'accueil est le plus promu, donc en tant qu'équipe, vous devrez vous concentrer et décider de ce qui doit apparaître en haut.

![Image](https://cdn-media-1.freecodecamp.org/images/ldOxUIQ3-plBQqOi7VdZxLohPl-QpS-ouK10)

Merci d'avoir lu ce guide rapide. Cela a été publié à l'origine dans le cadre du [cours de conception UX](https://www.commonlounge.com/discussion/d8c1c96e92024adf9f496fe41dcaad1a) sur [Commonlounge](https://www.commonlounge.com/). C'est une plateforme qui propose des cours avec de petites leçons comme celles-ci sur des sujets allant de la [Gestion de projet](https://www.commonlounge.com/discussion/1013c511951f4c47a803c32c4e1ae0f2) à l'[Apprentissage automatique](https://www.commonlounge.com/discussion/35ccdb70826e434a876d612504297232) qui offrent le plus de valeur pour le temps que vous y consacrez.

Vous apprenez en travaillant sur des projets réels et en recevant des commentaires de mentors de l'industrie. Vous devriez le vérifier [ici](https://www.commonlounge.com/) !

![Image](https://cdn-media-1.freecodecamp.org/images/R1v85eRIzXSYTP9Jfy3tJcYe1Vxi4kuqyCys)