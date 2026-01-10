---
title: Bogues courants dans la documentation logicielle et comment les corriger
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-12-19T14:59:56.000Z'
originalURL: https://freecodecamp.org/news/word-bugs-in-software-documentation-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/cover-1.png
tags:
- name: documentation
  slug: documentation
- name: english
  slug: english
- name: open source
  slug: open-source
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
seo_title: Bogues courants dans la documentation logicielle et comment les corriger
seo_desc: 'I’ve been an editor longer than I’ve been a developer, so this topic for
  me is a real root issue. ? When I see a great project with poorly-written docs,
  it hits close to /home. Okay, okay, I’m done.

  I help the Open Web Application Security Project (O...'
---

J'ai été éditeur plus longtemps que développeur, donc ce sujet est pour moi un vrai problème de fond. 💡 Quand je vois un excellent projet avec une documentation mal écrite, cela me touche de près. Bon, bon, j'arrête.

J'aide le [Open Web Application Security Project (OWASP)](https://github.com/OWASP) avec leur [Guide de test de sécurité Web (WSTG)](https://github.com/OWASP/wstg). On m'a récemment chargé d'écrire un [guide de style](https://en.wikipedia.org/wiki/Style_guide) et un modèle d'article montrant comment rédiger des instructions techniques pour tester des applications logicielles.

J'ai pensé que certaines parties du guide pourraient bénéficier à plus de personnes que simplement les contributeurs d'OWASP, donc j'en partage quelques-unes ici.

De nombreux projets auxquels je participe sont open source. C'est une manière merveilleuse pour les gens de partager des solutions et de construire sur les idées des autres. Malheureusement, c'est aussi une excellente façon pour les mots mal utilisés et inexistants de se propager. Voici un extrait du guide avec quelques erreurs que j'ai remarquées et comment vous pouvez les corriger dans vos documents techniques.

## Utiliser les bons mots

Les mots suivants sont fréquemment mal utilisés avec des conseils pour les corriger.

### _et/ou_

Bien que parfois utilisé dans les documents juridiques, _et/ou_ entraîne de l'ambiguïté et de la confusion dans la rédaction technique. Utilisez plutôt _ou_, qui en anglais inclut _et_. Par exemple :

> Mauvais : « Le code affichera un numéro d'erreur et/ou une description. »  
> Bon : « Le code affichera un numéro d'erreur ou une description. »

La dernière phrase n'exclut pas la possibilité d'avoir à la fois un numéro d'erreur et une description.

Si vous devez spécifier tous les résultats possibles, utilisez une liste :

> « Le code affichera un numéro d'erreur, ou une description, ou les deux. »

### _frontend, backend_

Bien qu'il soit vrai que la langue anglaise évolue avec le temps, ces mots n'existent pas encore.

Lorsque vous faites référence à des noms, utilisez _front end_ et _back end_. Par exemple :

> La sécurité est tout aussi importante sur le front end que sur le back end.

En tant qu'adverbe descriptif, utilisez les formes avec trait d'union _front-end_ et _back-end_.

> Les développeurs front-end et back-end sont responsables de la sécurité des applications.

### _whitebox, blackbox, greybox_

Ces mots n'existent pas.

En tant que noms, utilisez _white box_, _black box_ et _grey box_. Ces noms apparaissent rarement en lien avec la cybersécurité.

> Mon chat aime sauter dans cette grey box.

En tant qu'adverbes, utilisez les formes avec trait d'union _white-box_, _black-box_ et _grey-box_. Ne les capitalisez pas sauf si les mots sont dans un titre.

> Bien que les tests white-box impliquent la connaissance du code source, les tests black-box ne le font pas. Un test grey-box est quelque part entre les deux.

### _ie, eg_

Ce sont des lettres.

L'abréviation _i.e._ fait référence au latin _id est_, qui signifie « c'est-à-dire » ou « en d'autres termes ». L'abréviation _e.g._ vient de _exempli gratia_, se traduisant par « par exemple ». Pour les utiliser dans une phrase :

> Écrivez en utilisant un anglais correct, i.e. orthographe et grammaire correctes. Utilisez des mots courants plutôt que des mots rares, e.g. « apprendre » au lieu de « glaner ».

### _etc_

Ce sont aussi des lettres.

L'expression latine _et cetera_ se traduit par « et le reste ». Elle est abrégée _etc._ et généralement placée à la fin d'une liste qui semble redondante à compléter :

> Les auteurs du WSTG aiment les couleurs de l'arc-en-ciel, comme le rouge, le jaune, le vert, etc.

Dans la rédaction technique, l'utilisation de _etc._ est problématique. Elle suppose que le lecteur sait de quoi vous parlez, ce qui peut ne pas être le cas. Le violet est l'une des couleurs de l'arc-en-ciel, mais l'exemple ci-dessus ne vous dit pas explicitement si le violet est une couleur que les auteurs du WSTG aiment.

Il est préférable d'être explicite et complet plutôt que de faire des suppositions sur le lecteur. N'utilisez _etc._ que pour éviter de compléter une liste qui a été donnée en entier plus tôt dans le document.

### _…_ (points de suspension)

Les points de suspension peuvent indiquer que des mots ont été omis dans une citation :

> Linus Torvalds a un jour dit : « Une fois que vous réalisez que la documentation devrait être prise avec humour… ALORS, et seulement alors, vous avez atteint le niveau où vous pouvez la lire en toute sécurité et essayer de l'utiliser pour implémenter un pilote. »

Tant que l'omission ne change pas le sens de la citation, c'est une utilisation acceptable des points de suspension dans la rédaction technique.

Toutes les autres utilisations des points de suspension, comme pour indiquer une pensée inachevée, ne le sont pas.

### _ex_

Bien que ce soit un mot, ce n'est probablement pas le mot que vous cherchez. Le mot _ex_ a une signification particulière dans les domaines de la finance et du commerce, et peut désigner une personne si vous parlez de vos relations passées. Aucun de ces sujets ne devrait apparaître dans la rédaction technique.

L'abréviation _ex._ peut être utilisée pour signifier « exemple » par des écrivains paresseux. S'il vous plaît, ne soyez pas paresseux, et écrivez _exemple_ à la place.

## Allez de l'avant et écrivez des docs

Si ces rappels sont utiles, partagez-les librement et utilisez-les lorsque vous écrivez vos propres READMEs et documentations ! Si j'ai oublié quelque chose, j'aimerais le savoir.

Et si vous êtes ici pour les commentaires…

![Image](https://www.freecodecamp.org/news/content/images/2019/12/crowder-change-my-mind.png)
_Mème « Change my mind »._

Si vous souhaitez contribuer au OWASP WSTG, veuillez lire [le guide de contribution](https://github.com/OWASP/wstg/blob/master/CONTRIBUTING.md).