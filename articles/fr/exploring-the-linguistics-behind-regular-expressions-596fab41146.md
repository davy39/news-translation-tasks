---
title: Exploration de la linguistique derrière les expressions régulières
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-20T15:38:09.000Z'
originalURL: https://freecodecamp.org/news/exploring-the-linguistics-behind-regular-expressions-596fab41146
coverImage: https://cdn-media-1.freecodecamp.org/images/1*w-_7zxjx3gZgx_rLNVq60A.png
tags:
- name: computational linguistics
  slug: computational-linguistics
- name: Computer Science
  slug: computer-science
- name: linguistics
  slug: linguistics
- name: Regex
  slug: regex
- name: Regular Expressions
  slug: regular-expressions
seo_title: Exploration de la linguistique derrière les expressions régulières
seo_desc: 'By Alaina Kafkes

  How a linguistic breakthrough ended up in code


  _Image Credit: [xkcd](https://xkcd.com/" rel="noopener" target="blank" title=")

  Regular expressions inspire fear in new and experienced programmers alike. When
  I first saw a regular exp...'
---

Par Alaina Kafkes

#### Comment une percée linguistique a abouti dans le code

![Image](https://cdn-media-1.freecodecamp.org/images/-X06qYZoSEvRExXkwcADhu5kjKD64s6zg80F)
_Crédit image : [xkcd](https://xkcd.com/" rel="noopener" target="_blank" title=")_

Les expressions régulières inspirent la peur chez les programmeurs débutants et expérimentés. Lorsque j'ai vu une expression régulière pour la première fois — souvent abrégée en « regex » — je me souviens m'être sentie étourdie en regardant la litanie de parenthèses, d'astérisques, de lettres et de chiffres. Les expressions régulières semblaient nonsensiques, impénétrables.

Je m'attendais à ce que les expressions régulières réapparaissent dans mes cours avancés d'informatique — peut-être qu'à ce moment-là je me sentirais enfin prête à les aborder — mais je les ai rencontrées dans un cours d'introduction que j'avais reporté jusqu'à ma dernière année. Le but de ce cours était d'attirer les étudiants qui n'avaient jamais écrit une ligne de code vers l'informatique en les initiant à des concepts comme la cryptographie, l'interaction homme-machine, l'apprentissage automatique — vous savez, seulement les derniers et meilleurs mots à la mode de la technologie.

Je n'ai pas assisté à plus d'une poignée de cours, mais l'une des missions m'a marquée. Je devais écrire un essai sur un informaticien ou un académicien célèbre dont le travail a impacté l'informatique. J'ai choisi Noam Chomsky.

Je ne savais pas que l'apprentissage de Chomsky me mènerait dans un terrier de lapin vers les expressions régulières, et transformerait magiquement les expressions régulières en quelque chose qui me fascinait. Ce qui m'a enchantée dans les expressions régulières, c'était le concept linguistique homonyme qui les alimentait.

J'espère vous ensorceler, vous aussi, avec la linguistique derrière les expressions régulières, une histoire méconnue de la plupart des programmeurs. Bien que je ne vous apprenne pas à utiliser les expressions régulières dans un langage de programmation particulier, j'espère que mon introduction linguistique vous inspirera à plonger plus profondément dans le fonctionnement des expressions régulières dans votre langage de programmation préféré.

Pour commencer, revenons à Chomsky : quel est son rapport avec les expressions régulières ? En fait, quel est son rapport avec l'informatique ?

### Un informaticien par accident

Wikipedia présente [Noam Chomsky](https://en.wikipedia.org/wiki/Noam_Chomsky) comme un linguiste, philosophe, scientifique cognitif, historien, critique social et activiste politique, mais _pas_ comme un informaticien. Parce qu'il est si hautement considéré dans tous ces domaines, ses contributions indirectes au domaine de l'informatique sont souvent négligées.

Plus je recherchais le travail académique de Chomsky, plus son incursion dans l'informatique semblait accidentelle. Cela a confirmé ma croyance que tous les domaines — même ceux qui semblent disparates de l'informatique — ont quelque chose à offrir à l'informatique et à l'industrie technologique.

Ses contributions au domaine de la linguistique en particulier exemplifient l'impact de la recherche interdisciplinaire sur l'informatique. La hiérarchie de Chomsky a transformé le code que les informaticiens, les ingénieurs logiciels et les amateurs écrivent aujourd'hui.

Oui, c'est cette hiérarchie qui a introduit les expressions régulières en informatique. Mais, avant de comprendre le saut de Chomsky aux expressions régulières, je vais décrire la hiérarchie de Chomsky.

### Ordre et loi linguistiques

La [**hiérarchie de Chomsky**](https://en.wikipedia.org/wiki/Chomsky_hierarchy) est un classement des [**grammaires formelles**](https://en.wikipedia.org/wiki/Formal_grammar) — pensez aux règles syntaxiques pour les [**langages formels**](http://interactivepython.org/courselib/static/thinkcspy/GeneralIntro/FormalandNaturalLanguages.html) — de sorte que chaque grammaire existe comme un [sous-ensemble propre](http://mathworld.wolfram.com/ProperSubset.html) des grammaires au-dessus d'elle dans la hiérarchie. Certains langages formels ont des grammaires plus strictes que d'autres, donc Chomsky a cherché à organiser les grammaires formelles dans sa hiérarchie éponyme.

J'ai brièvement mentionné que les grammaires formelles sont des règles syntaxiques : des règles qui donnent toutes les phrases valides possibles pour un langage formel donné. Les grammaires fournissent les règles qui construisent les langages. En langage de linguiste, la grammaire formelle d'un langage fournit un cadre avec lequel les **non-terminaux** (valeurs de chaîne d'entrée ou intermédiaires) peuvent être convertis en **terminaux** (valeurs de chaîne de sortie).

Pour élucider ce nouveau vocabulaire, je vais passer par un exemple de conversion d'un ensemble de non-terminaux en terminaux en utilisant une grammaire formelle inventée. Supposons que notre langage formel fictif, [Parseltongue](http://harrypotter.wikia.com/wiki/Parseltongue), ait la grammaire formelle suivante :

* Terminaux : {s, sh, ss}
* Non-terminaux : {snake, I, am}
* Règles de production : {I → sh, am → s, snake → ss}

En utilisant les règles de production, je peux convertir la phrase d'entrée « I am snake » en « sh s ss ». Cette conversion se fait pièce par pièce : « I am snake » → « sh am snake » → « sh s snake » → « sh s ss ».

Comme le montre mon exemple de Parseltongue, les grammaires formelles analysent les chaînes de non-terminaux en chaînes de terminaux uniquement — des phrases grammaticalement correctes. Mais les grammaires formelles agissent non seulement comme des _générateurs_ d'un langage, mais aussi comme des _reconnaisseurs_ pour déterminer si une chaîne correspond à la grammaire formelle. Alors que la chaîne d'exemple « I am a snake » peut être entièrement convertie en terminaux, la chaîne « I am not a snake » ne peut pas être écrite en Parseltongue car le non-terminal « not » ne peut pas être traduit en un terminal Parseltongue.

Pour réaffirmer quelque chose que j'ai mentionné plus tôt : les grammaires formelles génèrent des langages formels. Cela signifie qu'en créant une hiérarchie de grammaires formelles, Chomsky a également catégorisé les langages eux-mêmes.

Avec cette introduction, examinons les quatre grammaires formelles de la hiérarchie de Chomsky. De la plus stricte à la moins stricte, elles sont :

* **Grammaires régulières**, qui ne conservent aucune connaissance de l'état passé de la chaîne d'entrée à la chaîne de sortie
* **Grammaires hors contexte**, qui conservent uniquement la connaissance récente de l'état de la chaîne d'entrée à la chaîne de sortie
* **Grammaires sensibles au contexte**, qui conservent toutes les connaissances de l'état passé de la chaîne d'entrée à la chaîne de sortie
* **Grammaires non restreintes** (ou **énumérables de manière récursive**), qui ont toutes les connaissances de l'état et peuvent ainsi créer chaque chaîne de sortie imaginable à partir d'une chaîne d'entrée donnée

Qu'est-ce que cette « connaissance de l'état » dont je parle ? Pensez à la connaissance en termes de [portée](https://en.wikipedia.org/wiki/Scope_(computer_science)). Les grammaires régulières, par exemple, n'ont aucune connaissance des états passés de la chaîne dans leur « portée » lors du processus de conversion d'une chaîne d'entrée en une chaîne de sortie. Cela suggère qu'une fois que la grammaire effectue une conversion individuelle de non-terminal en terminal (plus une série de zéro ou plusieurs non-terminaux), la grammaire « oublie » l'état précédent de la chaîne.

D'autre part, les grammaires non restreintes conservent chaque état possible de la chaîne en traduction. Les grammaires hors contexte et sensibles au contexte se situent quelque part entre les deux.

![Image](https://cdn-media-1.freecodecamp.org/images/DixBS4lQwkJv5Qdc7tSrQMsVjdQdevpMfyLh)

Si vous cherchez une explication plus détaillée des grammaires dans la hiérarchie de Chomsky, vous devrez jeter un coup d'œil à la [théorie des automates](https://en.wikipedia.org/wiki/Automata_theory). Je vais me concentrer sur la grammaire qui nous ramène aux expressions régulières, appelée de manière appropriée la grammaire régulière.

### Sur les expressions régulières

Les expressions régulières et les grammaires régulières sont équivalentes. Elles communiquent le même ensemble de règles syntaxiques, bien qu'en utilisant des formalismes différents, et produisent toutes deux les mêmes langages régulières.

En linguistique, une **expression régulière** est définie récursivement comme suit :

* L'ensemble vide est une expression régulière.
* La chaîne vide est une expression régulière.
* Pour tout caractère x dans l'alphabet d'entrée, x est une expression régulière qui produit le langage régulier {x}.
* **Alternance** : Si x et y sont des expressions régulières, alors x | y est une expression régulière. Par exemple, l'expression régulière `0|1` produit le langage régulier `{0,1}`.
* **Concatenation** : Si x et y sont des expressions régulières, alors x 7 y est une expression régulière. Par exemple, l'expression régulière `071` produit le langage régulier `{01}`.
* **Répétition** (aussi connue sous le nom d'**étoile de Kleene**) : Si x et y sont des expressions régulières, alors x* est une expression régulière. Par exemple, le langage régulier `071*` produit le langage régulier `{0, 01, 011, 0111, ...}`, ad infinitum.

Une grammaire régulière est composée de règles comme celles de Parseltongue. Tout comme une grammaire régulière peut être utilisée pour analyser une chaîne d'entrée en une chaîne de sortie, une expression régulière convertit les chaînes de manière assez similaire. Vous pouvez voir des exemples de cette analyse pour les opérations d'alternance, de concaténation et de répétition — ou, pour utiliser mon analogie précédente, les règles — que les expressions régulières adoptent.

Revenons à notre ami Noam Chomsky pour un moment. Selon sa hiérarchie des grammaires, les grammaires régulières ne conservent aucune information sur les étapes intermédiaires de la conversion d'une chaîne d'entrée en une chaîne de sortie. Que nous dit cela sur les expressions régulières ?

L'« oubli » des grammaires régulières implique que les traductions dans une partie de la chaîne n'ont pas d'impact sur la manière dont les autres non-terminaux de la chaîne sont traduits dans les étapes futures. Il n'y a pas de coordination entre différentes parties de la chaîne dans la création de la chaîne de sortie.

Regarder la linguistique derrière les grammaires régulières nous donne un aperçu de la raison pour laquelle les programmeurs ont d'abord introduit les expressions régulières dans le code. Bien que je n'aie discuté des grammaires formelles que comme générateurs et reconnaisseurs de langage, le fait que les grammaires régulières convertissent la chaîne d'entrée en chaîne de sortie pièce par pièce en fait des _reconnaisseurs de motifs_. En programmation, les expressions régulières utilisent des règles de production pour convertir une chaîne d'entrée — un motif — en un langage régulier — un ensemble de chaînes qui correspondent à ce motif.

Mais je n'aurais jamais écrit cet article de blog si les créateurs de langages de programmation avaient implémenté les expressions régulières exactement comme elles sont définies dans le domaine de la linguistique. Les expressions régulières computationnelles sont très différentes de leur précurseur linguistique, mais les expressions régulières linguistiques que j'ai couvertes fournissent un cadre utile pour comprendre les expressions régulières dans le code.

### Deux expressions régulières, toutes deux semblables en dignité

Par la suite, j'utiliserai le terme **expression régulière** pour désigner une expression régulière _linguistique_ et le terme **regex** pour signifier une expression régulière _programmatique_. Dans la nature, les expressions régulières linguistiques et programmatiques sont toutes deux appelées « expressions régulières » bien qu'elles soient assez différentes l'une de l'autre — quelle confusion !

La différence entre les expressions régulières et les regex provient de la manière dont elles sont utilisées. Les expressions régulières — ou grammaires régulières — font partie de la [théorie des langages _formels_](https://en.wikipedia.org/wiki/Formal_language), qui existe pour _décrire_ les éléments communs des **langues naturelles** — des langues qui ont évolué au fil du temps sans préméditation humaine. Les _linguistes_ utilisent les expressions régulières à des fins théoriques, comme la catégorisation des grammaires formelles dans la hiérarchie de Chomsky. Les expressions régulières aident les linguistes à comprendre les langues que parlent les humains.

Les regex, en revanche, sont utilisées par les _programmeurs quotidiens_ qui veulent _rechercher_ des chaînes qui _correspondent_ à un motif donné. Alors que les expressions régulières sont théoriques, les regex sont pragmatiques. Les langages de programmation sont des **langages formels** : des langues conçues par des personnes (ici, des programmeurs) pour des fins spécifiques. Comme vous pouvez l'imaginer, les créateurs de langages de programmation ont augmenté la fonctionnalité des regex dans le code. Examinons ces améliorations.

Rappelez-vous que les expressions régulières ont trois opérations : l'alternance, la concaténation et la répétition. Je ne suis pas une experte en regex — regexpert ? — mais il suffit de jeter un coup d'œil à la [page Wikipedia des expressions régulières](https://en.wikipedia.org/wiki/Regular_expression) pour remarquer que les regex implémentent plus de trois opérations.

Par exemple, en utilisant la [syntaxe regex POSIX](https://www.regular-expressions.info/posix.html), le motif `.ork` correspond à toutes les chaînes de quatre caractères qui se terminent par les trois caractères « ork ». Ce point est plus puissant que la simple alternance, la concaténation et la répétition, n'est-ce pas ?

Non. En vérité, même les plus fantaisistes des **métacaractères** regex — des caractères qui invoquent une opération regex — dérivent des opérations des expressions régulières. En supposant que les vingt-six lettres minuscules de l'alphabet sont les seuls caractères dans la grammaire régulière, le motif regex `.ork` pourrait être écrit en utilisant uniquement les opérations des expressions régulières comme `[a|b|c|...|z]ork`.

Bien que le volume de métacaractères suggère que les regex ont un ensemble d'opérations plus puissant que les expressions régulières elles-mêmes, les métacaractères ne sont que des raccourcis pour diverses permutations des opérations qui définissent les expressions régulières. Les métacaractères regex fournissent une abstraction conviviale pour les programmeurs pour les combinaisons courantes d'alternance, de concaténation et de répétition.

Jusqu'à présent, j'ai présenté les regex comme des expressions régulières avec des raccourcis incroyables et des cas d'utilisation clairs. Cependant, comme vous vous en souvenez peut-être de la hiérarchie de Chomsky, les grammaires régulières ont les règles les plus strictes et aucune portée. Heureusement, les regex ont un peu plus de latitude que leur précurseur linguistique, leur conférant ainsi plus de pouvoir pratique.

### Enfreindre les règles des grammaires régulières

Rappelez-vous que, selon la hiérarchie de Chomsky, les grammaires régulières ne conservent aucune connaissance lors de la conversion d'une chaîne d'entrée en une chaîne de sortie. Puisque les expressions régulières sont équivalentes aux grammaires régulières, cela signifie que les expressions régulières n'ont également aucun souvenir des états intermédiaires d'une chaîne lorsqu'elle passe de l'entrée à la sortie. Cela signifie également que la traduction d'un non-terminal dans une partie d'une expression régulière n'a aucun effet sur la traduction d'un non-terminal dans une autre partie de l'expression.

Pour les regex, c'est une autre histoire. Les regex violent cette caractéristique clé des grammaires régulières en supportant la capacité de rétro-référence. La **rétro-référence** permet au programmeur de séparer parenthétiquement une sous-section d'une expression régulière et de s'y référer en utilisant un métacaractère. Pour donner un exemple, le motif `(la)\1` correspond à « lala » en utilisant le métacaractère `\1` pour répéter la recherche de « la ».

Parce que différentes parties de la chaîne ne peuvent pas s'influencer mutuellement dans les expressions régulières, la rétro-référence donne aux regex beaucoup plus de pouvoir que leur prédécesseur. Plus important encore, la rétro-référence facilite les utilisations pratiques des regex telles que la recherche de fautes de frappe dans lesquelles le même mot a été accidentellement tapé deux fois de suite. Le pragmatisme donne un aperçu de la raison pour laquelle les expressions régulières ont été modifiées pour créer des regex en programmation.

Une autre fonctionnalité qui augmente la fonctionnalité des regex est la capacité de modifier l'avidité de la correspondance. Différents **quantificateurs** — catégories de motifs regex — peuvent sembler similaires mais correspondre à des parties très différentes d'une chaîne. Un **quantificateur avide** (*) tentera de faire correspondre autant de la chaîne que possible, tandis qu'un **quantificateur réticent** (?) essaiera de faire correspondre le nombre minimum de caractères dans la chaîne. Étant donné la chaîne « abcorgi », le motif `.*corgi` correspondrait à la chaîne entière mais le motif `.?corgi` ne correspondrait qu'à « bcorgi ».

Un **quantificateur possessif** (+) tente également de faire correspondre autant de la chaîne que possible, mais, contrairement au quantificateur avide, il ne reviendra pas en arrière vers les caractères précédents de la chaîne afin de trouver la correspondance la plus grande possible. Étant donné la chaîne « abcorgi », les motifs `.*corgi` et `.+corgi` correspondraient à la chaîne entière. Bien que les quantificateurs possessifs et avides produisent souvent le même résultat, les quantificateurs possessifs tendent à être plus efficaces car ils évitent de revenir en arrière.

Parce que les quantificateurs sont des métacaractères, ils peuvent techniquement être construits à partir d'alternance, de concaténation et de répétition : les trois opérations des expressions régulières. Cependant, les quantificateurs créent une abstraction simple qui permet aux programmeurs de spécifier rapidement le type de correspondance qu'ils souhaitent.

### Conclusion et lectures complémentaires

Quel voyage nous avons entrepris ! Nous avons appris sur Chomsky et sa hiérarchie éponyme, puis nous avons plongé plus profondément dans les grammaires régulières. À partir des grammaires régulières, nous avons exploré la définition linguistique d'une expression régulière. Enfin, nous avons utilisé les différences entre les expressions régulières et les regex pour motiver comment les programmeurs utilisent les regex aujourd'hui.

Bien que je retrace l'histoire des expressions régulières de Chomsky aux langages de programmation modernes, cet article de blog n'est pas la fin de l'histoire des regex. Si vous souhaitez en savoir plus sur les expressions régulières linguistiques et computationnelles, j'ai quelques questions motivantes pour vous.

* Qu'est-ce que la théorie des automates et comment se rapporte-t-elle à la hiérarchie de Chomsky ?
* Comment les regex sont-elles implémentées ? Quels sont les compromis des divers algorithmes regex ?
* Quand est-il approprié d'utiliser des regex au lieu des bibliothèques intégrées de correspondance et de manipulation de chaînes ?

J'ai également une liste de ressources que j'ai utilisées pour étudier les éléments linguistiques et computationnels des expressions régulières. Bon regex-ing !

* [Regular-Expressions.info](https://www.regular-expressions.info/)
* [Wikipedia : Expressions régulières](https://en.wikipedia.org/wiki/Regular_expression)
* [StackOverflow : Hiérarchie de Chomsky en anglais simple](https://stackoverflow.com/questions/8398030/chomsky-hierarchy-in-plain-english)
* [_Introduction à la théorie des automates, des langages et de la computation_](https://www.amazon.com/Introduction-Automata-Theory-Languages-Computation/dp/0321455363) par Hopcroft et al.
* [StackOverflow : Différence entre l'expression régulière et la grammaire dans les automates](https://cs.stackexchange.com/questions/45755/difference-between-regular-expression-and-grammar-in-automata)
* [Comment penser comme un informaticien : Langages formels et naturels](http://interactivepython.org/courselib/static/thinkcspy/GeneralIntro/FormalandNaturalLanguages.html)
* [Tutoriels Java d'Oracle : Quantificateurs](https://docs.oracle.com/javase/tutorial/essential/regex/quant.html)
* [StackOverflow : Comparaison des regex dans les langages de programmation avec les expressions régulières des automates/langages formels](https://cs.stackexchange.com/questions/53397/compare-regex-in-programming-languages-with-regular-expression-from-automata-for?rq=1)
* [Quora : Comment les expressions régulières sont-elles implémentées ?](https://www.quora.com/How-are-regular-expressions-implemented)

_Aimez ce que vous avez lu ? Partagez l'amour en aimant et en partageant cet article. Avez-vous des pensées ou des questions ? Contactez-moi sur [Twitter](https://twitter.com/alainakafkes) ou dans les commentaires ci-dessous. Merci à [Miles Hinson](https://www.freecodecamp.org/news/exploring-the-linguistics-behind-regular-expressions-596fab41146/undefined) pour la relecture de cet article !_