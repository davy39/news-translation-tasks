---
title: Comment écrire un meilleur CSS en équipe avec ACSS — Une bibliothèque dynamique
  de CSS Atomique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T15:37:06.000Z'
originalURL: https://freecodecamp.org/news/acss-a-dynamic-atomic-css-library-402dff9756e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LJj4hmOES-c0DYj4Kwg89A.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: UI
  slug: ui
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment écrire un meilleur CSS en équipe avec ACSS — Une bibliothèque dynamique
  de CSS Atomique
seo_desc: 'By kushagra gour

  Writing good Cascading Style Sheets (CSS) is difficult and it becomes more difficult
  in a team where multiple developers write CSS.

  Through this article, I attempt to introduce you to an approach to writing (or not
  writing…we’ll see)...'
---

Par kushagra gour

Écrire de bonnes feuilles de style en cascade (CSS) est difficile et cela devient encore plus difficile dans une équipe où plusieurs développeurs écrivent du CSS.

À travers cet article, je tente de vous présenter une approche pour écrire (ou ne pas écrire… nous verrons) du CSS. Cette approche résout presque tous les problèmes auxquels on est confronté aujourd'hui avec du CSS mal écrit en équipe.

Mais d'abord, laissez-moi poser quelques conditions de base sur lesquelles mon article se base.

#### Quelques conditions que cet article suppose :

1. Vous travaillez dans une équipe où plusieurs développeurs écrivent du CSS.
2. Les directives sont difficiles à faire respecter sauf s'il y a des outils automatisés.
3. Les designers sont des oiseaux libres. Les redesigns arrivent.

Dans ces conditions, **je vais présenter une solution miracle qui résout presque tous les problèmes auxquels nous sommes confrontés à cause du mauvais CSS** (Rappelez-vous, le CSS n'est pas mauvais. C'est le CSS mal écrit qui l'est). Passons en revue ces problèmes pour commencer.

> **Avertissement** : Je ne suis, en aucun cas, affilié à la solution décrite dans cet article. Je suis simplement un développeur qui a ressenti la douleur du mauvais CSS dans une équipe et qui veut partager avec ses collègues développeurs mes réflexions sur la façon de surmonter cela. Cet article peut sembler promotionnel, mais c'est simplement parce que je suis très excité de partager cela avec tout le monde.

### Problème #1 : Nommer les classes est difficile

**_Développeur 1 (en codant)_** : Cela ressemble à un en-tête pour moi, laissez-moi utiliser le sélecteur `.header` pour cela.

**_Développeur 2 (dans la pull request)_** : Ce n'est pas un en-tête. Cela ressemble à un titre pour moi. De plus, nous ne pouvons pas l'appeler simplement 'header' car cet élément n'est pas assez générique. Appelons-le `.panel-header` ou mieux `.panel-title`.

Trouver des noms qui sont également significatifs est le problème le plus difficile à résoudre. C'est aussi l'aspect le plus difficile à apprendre car vous ne pouvez pas avoir de directives pour ce qui est un nom 'significatif'. Vous ne pouvez donner que des exemples de ce qui n'est pas significatif, et cela ne peut aider que jusqu'à un certain point. De plus, il ne s'agit pas seulement d'être 'significatif'. Les classes en CSS doivent également s'assurer qu'elles n'entrent pas en conflit avec d'autres noms de classes à l'avenir, car un nouveau développeur pourrait utiliser le même nom ou un nom similaire pour sa classe.

#### **Solutions disponibles :**

* [**BEM**](https://en.bem.info/methodology/) — des conventions de nommage comme BEM existent pour résoudre ce problème dans une certaine mesure. Mais au final, c'est une directive (nous savons tous à quel point il est facile de suivre les directives). BEM peut vous empêcher de faire complètement ad-hoc, mais vous devez toujours trouver un nom de classe initial pour vos composants.
* **Classes atomiques** — une autre approche courante ces jours-ci est d'utiliser des classes atomiques. De petites classes qui ne font qu'une seule chose. Par exemple, [Tachyons](http://tachyons.io/). Mélangez-les et associez-les pour obtenir ce dont vous avez besoin. C'est un bon pas vers le fait de 'sauter le nommage' complètement, mais que se passe-t-il si, à l'avenir, il n'existe aucune classe pour une chose particulière ? Comment personnaliser les classes atomiques existantes selon mon design ? Toutes les classes se chargent-elles toujours sur ma page, que je les utilise ou non ? Nous avons besoin de quelque chose de plus.

### Problème #2 : Forces des sélecteurs

Une autre chose dont les développeurs CSS doivent être constamment conscients est que la spécificité dans leur CSS ne devienne pas incontrôlable. Si vous avez des sélecteurs longs et complexes, votre CSS devient imprévisible et difficile à maintenir et à déboguer. Harry Roberts a écrit de nombreux articles sur [pourquoi c'est mauvais](https://csswizardry.com/2014/10/the-specificity-graph/) et [ce que vous pouvez faire pour y remédier](https://csswizardry.com/2014/07/hacks-for-dealing-with-specificity/).

#### **Solutions disponibles :**

La meilleure solution à ce problème est de simplement restreindre vos sélecteurs à une seule classe. Pas de chaînage, pas de nesting, pas d'IDs. Les noms BEM mentionnés ci-dessus et les classes atomiques résultent tous deux en des sélecteurs de classe unique dans votre CSS et aident ainsi à résoudre ce problème.

### Problème #3 : Que faire du CSS inutilisé ?

Le CSS est bloquant pour le rendu, il est donc très important de charger uniquement le CSS critique d'une page de manière synchrone et le reste, de manière asynchrone. Pour la même raison, il devient également important d'empêcher votre CSS de créer du bloat en supprimant le CSS inutilisé.

#### **Solutions disponibles :**

[De nombreux](https://github.com/purifycss/purifycss) [outils](https://github.com/giakki/uncss) se vantent d'extraire le CSS utilisé d'une page. Mais avec l'arrivée des applications monopages, cela est devenu plus difficile que jamais. Je ne suis pas sûr de leur fiabilité ou de leur efficacité, mais cela nécessite toujours un post-traitement supplémentaire de votre CSS.

### Problème #4 : Refactoring

**_Développeur 1_** : Ce CSS est devenu assez désordonné. Je pense que nous devrions le refactoriser.

**_Développeur 2_** : Pensez-vous que ce sélecteur que vous modifiez pourrait également être utilisé sur la page X ? Avez-vous vérifié ?

**_Développeur 1_** : Oh zut ! Vous avez raison… Je l'ai manqué. Cette page X est trop critique pour être touchée. Savez-vous pourquoi ce développeur a utilisé la même classe sur les deux pages ?

**_Développeur 2_** : Aucune idée. Il a quitté l'entreprise. Laissez simplement le CSS tel quel :(

Je n'ai rien de plus à dire ici. Ce dialogue explique tout.

Si je devais résumer les problèmes ci-dessus, je dirais qu'écrire un bon CSS (évolutif, lisible, maintenable) est définitivement possible. Cependant, le faire dans une grande équipe est extrêmement difficile. Même si vous essayez de le faire correctement dans une équipe, cela nécessiterait un effort constant de quelqu'un pour faire respecter toutes les meilleures pratiques.

> Dans une équipe, la solution la plus non évidente mais parfaite serait — d'arrêter d'écrire du CSS !

'Attendez, que dites-vous ? Ce n'est pas possible !'. Vous pourriez penser ainsi, mais laissez-moi vous présenter quelque chose.

### La solution tout-en-un — ACSS (Atomizer)

[**ACSS**](https://acss.io/) (dérivé de Atomic CSS) est un framework basé sur les composants pour le stylisme à travers des classes atomiques développé chez Yahoo ! Et [**Atomizer**](https://github.com/acss-io/atomizer) est un outil qui facilite cela. Je vais expliquer plus en détail. Mais avant cela, laissez-moi vous montrer comment vous faites le stylisme dans ACSS.

> Pour suivre les exemples de code dans cet article, je vous suggère d'installer [**Web Maker**](https://webmakerapp.com/) (un terrain de jeu front-end qui prend en charge l'écriture ACSS sans aucune configuration de build) sur le navigateur Chrome.

Maintenant, disons que vous avez un bouton qui doit être stylisé avec les propriétés habituelles de padding, de fond, de couleur, etc. Voici à quoi cela ressemblerait dans ACSS :

```
<button class="Bgc(blue) C(white) P(10px) D(ib) Cur(p) Bgc(red):h">Je suis un bouton</button>
```

**Une suggestion — ne portez pas de jugement à la première vue de cette syntaxe.** Continuez à lire, donnez-lui du temps, discutez, puis décidez. Les classes sur la balise `button` peuvent sembler différentes, mais vous conviendrez qu'elles sont devinables dans une large mesure quant à ce qu'elles font. C'est un bouton avec une couleur de fond _bleue_, une couleur _blanche_, un padding de _10px_, un affichage _inline-block_, un curseur _pointeur_ et une couleur de fond changée en _rouge_ au survol.

Si vous avez installé [Web Maker](https://webmakerapp.com), ouvrez-le en cliquant sur l'icône Web Maker dans le coin supérieur droit de votre navigateur Chrome. Collez le HTML ci-dessus dans le panneau de code HTML et sélectionnez **Atomic CSS** comme mode dans le panneau de code CSS. Dès que vous faites cela, vous verrez un CSS automatique généré dans le panneau de code CSS, comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/ofvqCkgGZfOvyZSKW80YnZViuXAr9DRH4rzw)

Le CSS que vous voyez est généré par l'outil _Atomizer_ que j'ai mentionné ci-dessus. Basiquement, il lit le HTML (ou tout fichier), détecte les classes ACSS et génère le CSS pour ces classes détectées. Vous écrivez simplement du HTML avec les classes appropriées que vous voulez utiliser et le CSS est généré automatiquement !

Maintenant que nous savons comment vous faites le stylisme dans ACSS, voyons pourquoi c'est la meilleure méthodologie CSS que votre équipe puisse avoir.

#### Inline, mais pas inline ?

Comme vous pouvez le voir, nous écrivons toujours des classes inline sur les balises. C'est ce que je voulais dire par stylisme inline. Mais ne le confondez pas avec [**les 'styles inline'**](https://www.codecademy.com/articles/html-inline-styles). Contrairement aux styles inline, nos classes inline se traduisent par des classes CSS réelles dans une feuille de style cachable. Donc, nous obtenons essentiellement la même puissance que les styles inline (écrire les choses rapidement) mais nous obtenons toujours un CSS atomique complètement valide en sortie.

#### Plus de nommage ! ?

Mon avantage absolu préféré. Vous n'aurez jamais à penser à un nom agréable, sémantique et non conflictuel pour une classe.

Un dicton très célèbre dit :

> Il n'y a que deux choses difficiles en informatique : l'invalidation du cache et le nommage des choses. — **Phil Karlton**

#### Mises à jour et refactoring super faciles

Allez dans le HTML et changez les classes pour mettre à jour le style. Supprimez n'importe quelle classe de n'importe où sans la crainte de casser quoi que ce soit ailleurs.

#### Pas un octet de CSS inutilisé ?

Puisque Atomizer génère le CSS à partir des classes que vous avez réellement utilisées, vous n'avez jamais de CSS inutilisé dans votre feuille de style. N'est-ce pas la performance folle que nous avons tous recherchée ? Il existe également un outil où vous pouvez vérifier combien un site web peut bénéficier de ACSS — [https://atomize-io.herokuapp.com/](https://atomize-io.herokuapp.com/)

#### Pas de directives pour les nouveaux développeurs ?

Tout ce dont vous avez besoin pour donner à un nouveau développeur dans le cadre de votre intégration CSS est un [guide de syntaxe pour ACSS](https://acss.io/guides/syntax.html) et un lien de référence de classe — [https://acss.io/reference](https://acss.io/reference). C'est une page où vous pouvez facilement rechercher la classe ACSS pour toute propriété:valeur. Même cette convention s'imprègne dans votre mémoire à mesure que vous continuez à l'utiliser.

De plus, il existe une petite [extension Visual Code](https://marketplace.visualstudio.com/items?itemName=pankaj-parashar.atomizer) par [Pankaj Parashar](https://twitter.com/pankajparashar) qui suggère automatiquement ces classes directement dans l'éditeur. Ainsi, même la référence n'est pas nécessaire avec cette extension. L'intégration des développeurs est terminée !

Outre ces avantages, ACSS offre plusieurs autres bonnes choses.

* Nous utilisons généralement les mêmes anciennes paires propriété/valeur dans une application. Ainsi, [**la feuille de style générée cesse essentiellement de croître après un certain point**](https://medium.com/@johnpolacek/by-the-numbers-a-year-and-half-with-atomic-css-39d75b1263b4). Parce que chaque paire propriété/valeur unique apparaît une fois dans la feuille de style finale.
* En raison du point ci-dessus, vous pourriez en fait utiliser **la même feuille de style dans votre suite de plusieurs produits** car elle ne serait jamais si grande. La même feuille de style CSS mise en cache pour tous les produits !
* Pull request qui semble être un rêve. **Imaginez des pull requests où vous ne voyez aucun fichier .css. Plus de vérification des classes pour leur significativité ou les conflits de spécificité**. Parce que vous savez que le bon CSS atomique, qui devrait être présent, serait généré. Ne serait-ce pas un monde merveilleux ?

### Démystification

De nombreux mythes se sont développés concernant ACSS sur Internet. Cela est dû à une évaluation superficielle du framework et à un jugement à première vue.

#### C'est la même chose que le stylisme inline. C'est mauvais !

Non, ce n'est pas le cas. Nous l'avons déjà vu ci-dessus. C'est définitivement aussi puissant que le stylisme inline mais n'en hérite aucun des inconvénients.

#### C'est difficile d'écrire toutes ces mêmes séries de classes encore et encore.

Oui, c'est le cas. ACSS dit que c'est un framework basé sur les composants. Si vous ne modélisez pas chacun de vos composants et que vous dupliquez déjà le HTML, par exemple pour créer un bouton à chaque fois, ACSS n'est pas pour vous.

Par exemple, vous devriez créer des boutons en utilisant un composant bouton abstrait comme suit :

```
<MyButton primary>Bonjour le monde</MyButton>
```

qui devrait être compilé en quelque chose comme :

```
<button type="button" class="D(ib) P(20px) Cur(p) Bgc(blue) Bgc(red):h">Bonjour le monde</button>
```

#### Les classes n'ont aucun sens

Je suis d'accord qu'elles sont différentes et peuvent sembler répulsives à première vue. Mais chaque framework de classes atomiques vient avec sa propre convention de nommage des choses. Et croyez-moi, ACSS a la meilleure des conventions de nommage. [Lisez plus sur pourquoi ils ont choisi un tel nommage](https://github.com/thierryk/ACSS-QA/blob/master/why-atomizer-did-not-use-more-readable-class-names.md).

Je voudrais citer un paragraphe d'un des [articles de Harry Roberts](https://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/) :

> Un argument courant contre BEM est qu'il est laid ; je me permets de dire que si vous évitez le code basé _purement_ sur son apparence, alors vous passez souvent à côté du point. À moins que le code ne devienne inutilement difficile à maintenir, ou réellement plus difficile à lire, alors peut-être que vous devez réfléchir à deux fois avant de l'utiliser, mais s'il 'semble simplement étrange' mais a un but valide, alors il devrait définitivement être pleinement considéré avant de l'écarter. — **Harry Roberts**

Mais nous voici, utilisant BEM pour rendre nos bases de code saines.

#### Je ne pourrai pas faire X chose dans ACSS

Vous serez surpris de voir [tout ce qui est possible](https://github.com/thierryk/ACSS-QA/) par de simples classes fournies dans ACSS. Pseudo-éléments, flexbox, media queries, vous l'appelez. Et la convention qu'ils ont inventée pour faire toutes ces choses est simplement brillante ! Bien qu'il puisse y avoir certaines choses non encore possibles dans ACSS, comme les CSS Grids, vous pouvez toujours [ouvrir un problème ou contribuer à Atomizer](https://github.com/acss-io/atomizer/issues).

### En fin de compte

Je vous demanderais d'essayer ACSS si vous comprenez la douleur d'écrire et de gérer du CSS en équipe. Et rappelez-vous, utiliser ACSS ne signifie pas que vous ne pouvez pas écrire de CSS simple. Les outils doivent être utilisés là où ils fonctionnent le mieux. Si vous pensez que le CSS simple serait plus approprié pour quelque chose, vous devriez définitivement l'utiliser.

De plus, ACSS n'est pas seul à adopter cette approche. Il existe des alternatives similaires comme [Blowdry CSS](http://blowdrycss.readthedocs.io/en/latest/), [Cell CSS](http://cellcss.com/), etc., chacune apportant son propre style pour atteindre le même objectif.

Si vous avez des questions concernant ACSS, vous pouvez contacter [Thierry Koblentz](https://twitter.com/thierrykoblentz), l'homme lui-même de l'équipe ACSS, sur [Twitter](https://twitter.com/thierrykoblentz). [Posez une question dans la compilation FAQ](https://github.com/thierryk/ACSS-QA/) qu'il maintient ou [rejoignez le groupe Atomizer sur Gitter](https://gitter.im/acss-io/atomizer). Ou mettez vos commentaires dans cet article.

Enfin, je voudrais remercier [Thierry Koblentz](https://twitter.com/thierrykoblentz) et [Jitendra Vyas](https://twitter.com/jitendravyas) pour avoir révisé cet article.

Si vous aimez cet article, montrez votre amour en applaudissant ?? l'article. Suivez-moi également sur [Twitter](https://twitter.com/intent/follow?screen_name=chinchang457), où je partage plus d'articles front-end et de projets secondaires.

### Plus à lire

* [https://www.smashingmagazine.com/2013/10/challenging-css-best-practices-atomic-approach/](https://www.smashingmagazine.com/2013/10/challenging-css-best-practices-atomic-approach/) — par Thierry Koblentz
* Dépôt GitHub Atomizer — [https://github.com/acss-io/atomizer](https://github.com/acss-io/atomizer)
* Documentation ACSS — [https://acss.io/quick-start.html](https://acss.io/quick-start.html)
* FAQ ACSS compilées par Thierry — [https://github.com/thierryk/ACSS-QA](https://github.com/thierryk/ACSS-QA)
* Terrain de jeu ACSS — [https://webmakerapp.com](https://webmakerapp.com)