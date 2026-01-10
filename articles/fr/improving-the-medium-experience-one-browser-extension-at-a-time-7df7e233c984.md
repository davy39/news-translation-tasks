---
title: Améliorer l'expérience Medium
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T09:45:06.000Z'
originalURL: https://freecodecamp.org/news/improving-the-medium-experience-one-browser-extension-at-a-time-7df7e233c984
coverImage: https://cdn-media-1.freecodecamp.org/images/0*x-bORZmgzqDVzW-g.
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Améliorer l'expérience Medium
seo_desc: 'By cedric amaya

  One browser extension at a time.


  _Photo by [Unsplash](https://unsplash.com/@barnimages?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Barn Images on <a href="https://unsplash.com?utm_source=medium&utm_...'
---

Par cedric amaya

#### Une extension de navigateur à la fois.

![Image](https://cdn-media-1.freecodecamp.org/images/5ykRlwzkzFJzHOky-2arac3AWBNCySxbrPAD)
_Photo par [Unsplash](https://unsplash.com/@barnimages?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Barn Images</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

J'adore Medium. En tant que consommateur, il m'a fourni d'innombrables articles qui m'ont aidé à m'améliorer, tant sur le plan personnel que professionnel. Et en tant que producteur, il m'a offert une plateforme sur laquelle je peux m'exprimer le plus authentiquement possible à travers l'écrit.

Cependant, depuis que j'utilise Medium, j'ai remarqué certaines choses concernant la plateforme de publication qui me semblaient manquantes ou perfectibles. Et en tant que développeur web et bricoleur, j'aime trouver moi-même des solutions à ces problèmes. Voici quelques extensions que j'ai créées pour rendre votre expérience Medium encore meilleure.

### Medium Bookmarklets ?

La première fois que j'ai essayé d'améliorer l'expérience Medium, c'était avec mon extension Firefox, [Medium Bookmarklets](https://medium-bookmarklets.com/) (que j'ai découvert après avoir nommé le produit, ne sont pas réellement des bookmarklets).

Cela visait à apporter une véritable fonctionnalité de marque-page, dans le sens où vous pouviez sauvegarder votre position dans un article pour plus tard, sans avoir besoin de vous souvenir ou de faire défiler jusqu'à cette section. Cela résolvait un problème auquel j'étais constamment confronté et que je pensais que d'autres pouvaient également rencontrer.

#### Comment cela fonctionne

Sachant que les éléments HTML dans les articles Medium contiennent un attribut `id` unique, j'ai développé une solution qui ajoutait un marqueur / surligneur sur l'élément sélectionné. Cela correspondait à un paragraphe, un titre ou une citation dans l'article où l'utilisateur voulait sauvegarder sa position, ce qui sauvegardait à son tour l'`id` de cet élément.

La navigation directe vers cet endroit dans l'article est effectuée en utilisant un identifiant de fragment de l'`id` sauvegardé. Par exemple, si ce paragraphe avait un `id` de « 3b75 », alors pour ouvrir cet article avec ce paragraphe spécifique en haut de la page, l'URL ressemblerait à quelque chose comme `https://blog.cedricamaya.me/improving-medium-experience-7df7e233c678**#3b75**` **.** Notez l'identifiant de fragment (`#3b75`) à la fin.

Cette même fonctionnalité est généralement utilisée par les écrivains / éditeurs pour inclure une table des matières dans leurs articles sur Medium. [Voici une excellente explication et un guide pratique qui entrent plus dans les détails.](https://medium.freecodecamp.org/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549)

Avec cette fonctionnalité en tête, j'ai codé une extension Firefox qui créait une barre latérale de cartes cliquables représentant les _bookmarklets_ sauvegardés de l'utilisateur, comme je les appelais. Le gestionnaire d'événements de clic sur chaque carte naviguait vers la page actuelle à l'URL du _bookmarklet_. Ainsi, si vous placiez un _bookmarklet_ à mi-chemin dans un long article, le besoin de faire défiler jusqu'à cette section où vous vous étiez arrêté était complètement éliminé.

![Image](https://cdn-media-1.freecodecamp.org/images/zBx9xbR2vlqxbauf-L4tmKI7yLpTkrqgf5d-)
_Image promotionnelle mettant en avant la barre latérale Medium Bookmarklets et un surlignage de bookmarklet dans un article._

Il y a plus de fonctionnalités incluses dans Medium Bookmarklets, comme la nécessité de mettre sur liste blanche les publications dont vous souhaitez sauvegarder les _bookmarklets_ (pour des raisons de sécurité), ainsi que des notifications lorsqu'un _bookmarklet_ est ajouté ou supprimé. Autrement, c'est une extension assez simple qui vise à améliorer vos capacités de marque-page.

_Découvrez [**Medium Bookmarklets**](https://addons.mozilla.org/en-US/firefox/addon/medium-bookmarklets/) sur Mozilla Addons._

### Signature ✒️

Si Medium Bookmarklets a été développé en pensant aux consommateurs de Medium, alors [Signature](https://chrome.google.com/webstore/detail/signature/hgabbjfneihcmbbcnbnfdnfdcbpodnhp) a été développé pour ceux qui créent du contenu sur Medium.

Le but de Signature est simple : offrir aux écrivains et éditeurs la possibilité d'ajouter instantanément la signature de leur blog / formule de politesse avec un clic de bouton—éliminant le besoin de copier et coller ou de retaper à chaque fois.

L'idée pour Signature est née après être tombé sur de nombreux articles dans une publication spécifique qui se terminaient tous par le même texte / copie. Il s'agissait généralement d'un appel à l'action avec des hyperliens, et était stylisé avec du texte en gras ou en italique pour le faire ressortir.

Je me suis dit : « les gens tapent-ils cette signature ou la copient-ils et la collent-ils depuis un article précédent à chaque fois qu'ils écrivent un nouveau billet de blog ? » Quoi qu'il en soit, retaper ou copier et coller prend du temps, et voulant simplifier le processus, j'ai développé une autre extension de navigateur (cette fois pour Chrome et Firefox) pour résoudre ce problème.

#### Comment cela fonctionne

Avec Signature installé, les utilisateurs remplissent simplement la signature de leur blog dans l'éditeur trouvé dans la page des paramètres de l'extension. Cet éditeur, une instance de [Quill](https://quilljs.com/), est un éditeur de texte riche, ce qui signifie que tout formatage de texte (c'est-à-dire gras, italique, citation, titre, code, etc.) peut facilement être transféré et appliqué à un brouillon d'article de blog Medium, qui utilise également la capacité de texte riche.

Une fois qu'une signature a été définie dans la page des paramètres, les utilisateurs pourront alors cliquer sur le bouton « signature » (avec l'icône de plume) situé dans l'infobulle en ligne, comme montré ci-dessous. Cliquer sur ce bouton colle ensuite la signature qui a été définie dans la page des paramètres dans le brouillon.

![Image](https://cdn-media-1.freecodecamp.org/images/h8kqbC09qw8J2Bu96z0DXb5rcC8wwEniR1sK)
_Bouton « Signature », à l'extrême droite._

Assez parlé de son fonctionnement, voyons-le en action !

![Image](https://cdn-media-1.freecodecamp.org/images/R48SQUC-Qy8E5kJOQFanlP2zVzDYhvN8diZ5)
_Signature ajoutée dans la page des paramètres, puis bouton « signature » utilisé pour ajouter la signature dans le brouillon Medium._

_Découvrez **Signature** sur [Mozilla Addons](https://addons.mozilla.org/en-US/firefox/addon/medium-signature/) et sur le [Chrome Webstore](https://chrome.google.com/webstore/detail/signature/hgabbjfneihcmbbcnbnfdnfdcbpodnhp)._

#### Conclusion

Comme tous les produits, Medium a ses défauts. Cependant, avec une utilisation créative de votre imagination et une attitude de bricolage, vous pouvez grandement améliorer ces problèmes avec un peu de programmation.

Je vous encourage maintenant à améliorer l'expérience Medium à votre manière et à partager le résultat en utilisant #MediumExperience. Si vous ne pouvez pas penser à votre propre idée ou si vous commencez tout juste à programmer, n'hésitez pas à implémenter une nouvelle fonctionnalité ou à corriger un bug dans Medium Bookmarklets ou Signature — les deux sont open-source et peuvent être trouvés sur GitHub.

[**cedricium/medium-bookmarklets**](https://github.com/cedricium/medium-bookmarklets)
[**cedricium/signature**](https://github.com/cedricium/signature)

Merci d'avoir lu et j'ai hâte de voir comment vous choisirez d'améliorer l'expérience Medium !

**~ cedric amaya**
⚡️ manieur qui aime créer des choses avec du code
G[itHub](https://github.com/cedricium) | L[inkedIn](https://www.linkedin.com/in/cedricamaya) | T[witter](https://twitter.com/cedricamaya)