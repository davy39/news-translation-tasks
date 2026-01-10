---
title: Une histoire de la traduction automatique, de la Guerre froide à l'apprentissage
  profond
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T12:12:26.000Z'
originalURL: https://freecodecamp.org/news/a-history-of-machine-translation-from-the-cold-war-to-deep-learning-f1d335ce8b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d-iF6wcVYCWFDLkghpJvkw.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une histoire de la traduction automatique, de la Guerre froide à l'apprentissage
  profond
seo_desc: 'By Ilya Pestov

  I open Google Translate twice as often as Facebook, and the instant translation
  of the price tags is not a cyberpunk for me anymore. That’s what we call reality.
  It’s hard to imagine that this is the result of a centennial fight to bui...'
---

Par Ilya Pestov

J'ouvre Google Translate deux fois plus souvent que Facebook, et la traduction instantanée des étiquettes de prix n'est plus de la cyberpunk pour moi. C'est ce que nous appelons la réalité. Il est difficile d'imaginer que cela soit le résultat d'un combat centenaire pour construire les algorithmes de traduction automatique et qu'il n'y ait eu aucun succès visible pendant la moitié de cette période.

Les développements précis dont je vais discuter dans cet article ont jeté les bases de tous les systèmes modernes de traitement des langues — des moteurs de recherche aux micro-ondes à commande vocale. Je parle de l'évolution et de la structure de la traduction en ligne aujourd'hui.

![Image](https://cdn-media-1.freecodecamp.org/images/rprYZbDrYxFKrq8uSJmNnr4rld9jmUf6ffSZ)
_La machine traductrice de P. P. Troyanskii (Illustration réalisée à partir de descriptions. Aucune photo n'a été conservée, malheureusement.)_

### Au commencement

L'histoire commence en 1933. Le scientifique soviétique Peter Troyanskii a présenté « la machine pour la sélection et l'impression de mots lors de la traduction d'une langue à une autre » à l'Académie des sciences de l'URSS. L'invention était super simple — elle avait des cartes dans quatre langues différentes, une machine à écrire et une caméra de cinéma old-school.

L'opérateur prenait le premier mot du texte, trouvait une carte correspondante, prenait une photo et tapait ses caractéristiques morphologiques (nom, pluriel, génitif) sur la machine à écrire. Les touches de la machine à écrire codaient l'une des caractéristiques. La bande et le film de la caméra étaient utilisés simultanément, créant un ensemble de cadres avec des mots et leur morphologie.

![Image](https://cdn-media-1.freecodecamp.org/images/d6EZXLmcj0m-0ILBEBafviYN9ITSLJmXum-F)

Malgré tout cela, comme cela arrivait souvent en URSS, l'invention a été considérée comme « inutile ». Troyanskii est mort d'une sténocardie après avoir tenté de terminer son invention pendant 20 ans. Personne dans le monde ne savait rien de la machine jusqu'à ce que deux scientifiques soviétiques trouvent ses brevets en 1956.

C'était au début de la Guerre froide. Le 7 janvier 1954, au siège d'IBM à New York, l'[expérience Georgetown-IBM](https://en.wikipedia.org/wiki/Georgetown%E2%80%93IBM_experiment) a commencé. L'ordinateur IBM 701 a traduit automatiquement 60 phrases russes en anglais pour la première fois de l'histoire.

> _« Une fille qui ne comprenait pas un mot de la langue des Soviétiques a perforé les messages russes sur des cartes IBM. Le « cerveau » a produit ses traductions anglaises sur une imprimante automatique à la vitesse vertigineuse de deux lignes et demie par seconde »_, a rapporté le communiqué de presse d'IBM.

![Image](https://cdn-media-1.freecodecamp.org/images/1MJctJSHzUaYpUNIhvQdQtz4RKFq06nN7FJ9)
_IBM 701_

Cependant, les titres triomphaux cachaient un petit détail. Personne n'a mentionné que les exemples traduits avaient été soigneusement sélectionnés et testés pour exclure toute ambiguïté. Pour un usage quotidien, ce système n'était pas meilleur qu'un guide de conversation de poche. Néanmoins, ce genre de course aux armements a été lancé : le Canada, l'Allemagne, la France et surtout le Japon ont tous rejoint la course à la traduction automatique.

### La course à la traduction automatique

Les luttes vaines pour améliorer la traduction automatique ont duré quarante ans. En 1966, le comité ALPAC des États-Unis, dans son célèbre rapport, a qualifié la traduction automatique de coûteuse, d'inexacte et de peu prometteuse. Ils ont plutôt recommandé de se concentrer sur le développement de dictionnaires, ce qui a éliminé les chercheurs américains de la course pendant près d'une décennie.

Néanmoins, une base pour le traitement moderne du langage naturel a été créée uniquement par les scientifiques et leurs tentatives, recherches et développements. Tous les moteurs de recherche, filtres anti-spam et assistants personnels actuels sont apparus grâce à un groupe de pays qui s'espionnaient les uns les autres.

![Image](https://cdn-media-1.freecodecamp.org/images/l6Av1jJRcgtfL5n9vEvrspxpEJJalwHAusRx)

### Traduction automatique basée sur des règles (RBMT)

Les premières idées entourant la traduction automatique basée sur des règles sont apparues dans les années 70. Les scientifiques ont observé le travail des interprètes, essayant de contraindre les ordinateurs extrêmement lents à répéter ces actions. Ces systèmes se composaient de :

* Un dictionnaire bilingue (RU -> EN)
* Un ensemble de règles linguistiques pour chaque langue (Par exemple, les noms se terminant par certains suffixes tels que -heit, -keit, -ung sont féminins)

C'est tout. Si nécessaire, les systèmes pouvaient être complétés par des astuces, telles que des listes de noms, des correcteurs orthographiques et des translittérateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/fDCtcK15iABLixdZslASHztO0H3033UHjQm5)

PROMPT et Systran sont les exemples les plus célèbres de systèmes RBMT. Il suffit de regarder AliExpress pour ressentir le souffle doux de cet âge d'or.

Mais même eux avaient quelques nuances et sous-espèces.

#### Traduction automatique directe

C'est le type de traduction automatique le plus simple. Il divise le texte en mots, les traduit, corrige légèrement la morphologie et harmonise la syntaxe pour que l'ensemble sonne correctement, plus ou moins. Lorsque le soleil se couche, des linguistes formés écrivent les règles pour chaque mot.

Le résultat retourne une sorte de traduction. Habituellement, elle est assez médiocre. Il semble que les linguistes aient perdu leur temps pour rien.

Les systèmes modernes n'utilisent plus du tout cette approche, et les linguistes modernes en sont reconnaissants.

![Image](https://cdn-media-1.freecodecamp.org/images/gfF1OTGY1E6QQBDW6l6kh1Daa4iingQmt86V)

#### Traduction automatique basée sur le transfert

Contrairement à la traduction directe, nous préparons d'abord en déterminant la structure grammaticale de la phrase, comme on nous l'a enseigné à l'école. Ensuite, nous manipulons des constructions entières, et non des mots, par la suite. Cela aide à obtenir une conversion assez décente de l'ordre des mots dans la traduction. En théorie.

En pratique, cela résultait toujours en une traduction mot à mot et des linguistes épuisés. D'une part, cela a apporté des règles de grammaire générale simplifiées. Mais d'autre part, cela est devenu plus compliqué en raison du nombre accru de constructions de mots par rapport aux mots simples.

![Image](https://cdn-media-1.freecodecamp.org/images/AfcjFhnoMFmb8koHf42YQeE6WfKdFNjqpkGL)

#### Traduction automatique interlinguale

Dans cette méthode, le texte source est transformé en une représentation intermédiaire, unifiée pour toutes les langues du monde (interlingua). C'est la même interlingua dont Descartes rêvait : une méta-langue, qui suit des règles universelles et transforme la traduction en une simple tâche de « va-et-vient ». Ensuite, l'interlingua serait convertie en n'importe quelle langue cible, et voici la singularité !

En raison de la conversion, l'interlingua est souvent confondue avec les systèmes basés sur le transfert. La différence réside dans les règles linguistiques spécifiques à chaque langue et à l'interlingua, et non aux paires de langues. Cela signifie que nous pouvons ajouter une troisième langue au système interlingua et traduire entre les trois. Nous ne pouvons pas faire cela dans les systèmes basés sur le transfert.

![Image](https://cdn-media-1.freecodecamp.org/images/jE7o846MC7p596-VFd0akSV99i90aSvrq1dY)

Cela semble parfait, mais dans la vie réelle, ce n'est pas le cas. Il était extrêmement difficile de créer une telle interlingua universelle — beaucoup de scientifiques y ont travaillé toute leur vie. Ils n'ont pas réussi, mais grâce à eux, nous avons maintenant des niveaux morphologiques, syntaxiques et même sémantiques de représentation. Mais la seule [théorie du texte-signification](https://en.wikipedia.org/wiki/Meaning-text_theory) coûte une fortune !

L'idée de langue intermédiaire reviendra. Attendons un peu.

![Image](https://cdn-media-1.freecodecamp.org/images/vEPJYMmjDV0LLXIy07LksIiOsecXdlHcs8nI)

Comme vous pouvez le voir, tous les RBMT sont stupides et terrifiants, et c'est la raison pour laquelle ils sont rarement utilisés sauf pour des cas spécifiques (comme la traduction des bulletins météo, etc.). Parmi les avantages des RBMT, on mentionne souvent leur précision morphologique (ils ne confondent pas les mots), la reproductibilité des résultats (tous les traducteurs obtiennent le même résultat) et la capacité à l'ajuster au domaine (pour enseigner aux économistes ou aux termes spécifiques aux programmeurs, par exemple).

Même si quelqu'un réussissait à créer un RBMT idéal, et que les linguistes l'amélioraient avec toutes les règles d'orthographe, il y aurait toujours des exceptions : tous les verbes irréguliers en anglais, les préfixes séparables en allemand, les suffixes en russe, et les situations où les gens disent simplement les choses différemment. Toute tentative de prendre en compte toutes les nuances gaspillerait des millions d'heures de travail.

Et n'oublions pas les homonymes. Le même mot peut avoir une signification différente dans un contexte différent, ce qui conduit à une variété de traductions. Combien de significations pouvez-vous trouver ici : _J'ai vu un homme sur une colline avec un télescope_ ?

Les langues ne se sont pas développées sur la base d'un ensemble fixe de règles — un fait que les linguistes adorent. Elles ont été beaucoup plus influencées par l'histoire des invasions des trois cents dernières années. Comment pourriez-vous expliquer cela à une machine ?

Quarante ans de Guerre froide n'ont pas aidé à trouver une solution distincte. Le RBMT était mort.

### Traduction automatique basée sur des exemples (EBMT)

Le Japon était particulièrement intéressé par la lutte pour la traduction automatique. Il n'y avait pas de Guerre froide, mais il y avait des raisons : très peu de personnes dans le pays connaissaient l'anglais. Cela promettait d'être un problème lors de la prochaine fête de la mondialisation. Les Japonais étaient donc extrêmement motivés pour trouver une méthode de traduction automatique fonctionnelle.

La traduction automatique basée sur des règles de l'anglais vers le japonais est extrêmement compliquée. La structure de la langue est complètement différente, et presque tous les mots doivent être réarrangés et de nouveaux ajoutés. En 1984, Makoto Nagao de l'Université de Kyoto a eu l'idée d'**utiliser des phrases toutes faites au lieu de traductions répétées**.

Imaginons que nous devons traduire une phrase simple — « Je vais au cinéma. » Et disons que nous avons déjà traduit une autre phrase similaire — « Je vais au théâtre » — et que nous pouvons trouver le mot « cinéma » dans le dictionnaire.

Tout ce dont nous avons besoin est de comprendre la différence entre les deux phrases, de traduire le mot manquant, puis de ne pas tout gâcher. Plus nous avons d'exemples, meilleure est la traduction.

Je construis des phrases dans des langues inconnues exactement de la même manière !

![Image](https://cdn-media-1.freecodecamp.org/images/H-VtzpHN02SMIhwYjqmn04Uyd-nGWLwLmBwW)

L'EBMT a montré la lumière du jour aux scientifiques du monde entier : il s'avère que vous pouvez simplement nourrir la machine avec des traductions existantes et ne pas passer des années à former des règles et des exceptions. Pas encore une révolution, mais clairement la première étape vers celle-ci. L'invention révolutionnaire de la traduction statistique aurait lieu dans seulement cinq ans.

### Traduction automatique statistique (SMT)

Au début des années 1990, au Centre de recherche IBM, un système de traduction automatique a été présenté pour la première fois qui ne connaissait rien des règles et de la linguistique en général. Il analysait des textes similaires dans deux langues et essayait de comprendre les motifs.

![Image](https://cdn-media-1.freecodecamp.org/images/5qBpooShbY6xVngSotA6KINHyHP7NKeTJryb)

L'idée était simple mais belle. Une phrase identique dans deux langues était divisée en mots, qui étaient ensuite appariés. Cette opération était répétée environ 500 millions de fois pour compter, par exemple, combien de fois le mot « Das Haus » était traduit par « maison » vs « bâtiment » vs « construction », et ainsi de suite.

Si la plupart du temps le mot source était traduit par « maison », la machine utilisait cela. Notez que nous n'avons défini aucune règle ni utilisé de dictionnaires — toutes les conclusions étaient faites par la machine, guidée par les statistiques et la logique que « si les gens traduisent de cette manière, moi aussi ». Et ainsi est née la traduction statistique.

![Image](https://cdn-media-1.freecodecamp.org/images/jG95Sgc2W4VJbwi4LFlJeMHnjLZbdGydCCzI)

La méthode était beaucoup plus efficace et précise que toutes les précédentes. Et aucun linguiste n'était nécessaire. Plus nous utilisions de textes, meilleure était la traduction.

![Image](https://cdn-media-1.freecodecamp.org/images/uF96He1UZaLMkC1TEuBGzoHAhw3PAvF8mgam)
_La traduction statistique de Google de l'intérieur. Elle montre non seulement les probabilités mais compte aussi les statistiques inverses._

Il restait encore une question : comment la machine corrélerait-elle le mot « Das Haus » et le mot « bâtiment » — et comment saurions-nous que ce sont les bonnes traductions ?

La réponse était que nous ne le saurions pas. Au début, la machine supposait que le mot « Das Haus » était également corrélé avec n'importe quel mot de la phrase traduite. Ensuite, lorsque « Das Haus » apparaissait dans d'autres phrases, le nombre de corrélations avec « maison » augmentait. C'est l'« algorithme d'alignement de mots », une tâche typique pour l'apprentissage automatique de niveau universitaire.

La machine avait besoin de millions et de millions de phrases dans deux langues pour collecter les statistiques pertinentes pour chaque mot. Comment les avons-nous obtenues ? Eh bien, nous avons décidé de prendre les résumés des réunions du Parlement européen et du Conseil de sécurité des Nations Unies — ils étaient disponibles dans les langues de tous les pays membres et étaient maintenant disponibles pour le téléchargement sur [UN Corpora](https://catalog.ldc.upenn.edu/LDC2013T06) et [Europarl Corpora](http://www.statmt.org/europarl/).

#### SMT basée sur les mots

Au début, les premiers systèmes de traduction statistique fonctionnaient en divisant la phrase en mots, puisque cette approche était simple et logique. Le premier modèle de traduction statistique d'IBM s'appelait Modèle un. Plutôt élégant, non ? Devinez comment ils ont appelé le deuxième ?

**_Modèle 1 : « le sac de mots »_**

![Image](https://cdn-media-1.freecodecamp.org/images/4dBTKxFLuXkmeALMuxILitzmBd0zVOQVrhnP)

Le modèle un utilisait une approche classique — diviser en mots et compter les statistiques. L'ordre des mots n'était pas pris en compte. La seule astuce était de traduire un mot en plusieurs mots. Par exemple, « Der Staubsauger » pouvait devenir « Vacuum Cleaner », mais cela ne signifiait pas que cela fonctionnerait dans l'autre sens.

Voici quelques implémentations simples en Python : [shawa/IBM-Model-1](https://github.com/shawa/IBM-Model-1).

**_Modèle 2 : en tenant compte de l'ordre des mots dans les phrases_**

![Image](https://cdn-media-1.freecodecamp.org/images/AWurqrK2Zag9dIZSgYVGZCFxklsrZot7WLZ2)

Le manque de connaissances sur l'ordre des mots dans les langues est devenu un problème pour le Modèle 1, et c'est très important dans certains cas.

Le Modèle 2 a traité cela : il mémorisait la place habituelle que le mot prend dans la phrase de sortie et mélangeait les mots pour un son plus naturel à l'étape intermédiaire. Les choses se sont améliorées, mais elles étaient toujours un peu médiocres.

**_Modèle 3 : fertilité supplémentaire_**

![Image](https://cdn-media-1.freecodecamp.org/images/aPxpW2ssFd2wDio9C51Zbb0sIdXLBAV8DoYP)

De nouveaux mots apparaissaient souvent dans la traduction, comme les articles en allemand ou l'utilisation de « do » lors de la négation en anglais. « Ich will keine Persimonen » → « I **do** not want Persimmons. » Pour y remédier, deux étapes supplémentaires ont été ajoutées au Modèle 3.

* L'insertion du jeton NULL, si la machine considère la nécessité d'un nouveau mot
* Le choix de la bonne particule grammaticale ou du bon mot pour chaque alignement mot-jeton

**_Modèle 4 : alignement des mots_**

Le Modèle 2 considérait l'alignement des mots, mais ne savait rien du réordonnancement. Par exemple, les adjectifs échangeaient souvent de place avec le nom, et peu importe à quel point l'ordre était mémorisé, cela n'améliorait pas la sortie. Par conséquent, le Modèle 4 tenait compte de ce que l'on appelle l'« ordre relatif » — le modèle apprenait si deux mots échangeaient toujours de place.

**_Modèle 5 : corrections de bugs_**

Rien de nouveau ici. Le Modèle 5 a obtenu quelques paramètres supplémentaires pour l'apprentissage et a corrigé le problème des positions de mots conflictuelles.

Malgré leur nature révolutionnaire, les systèmes basés sur les mots échouaient toujours à traiter les cas, le genre et l'homonymie. Chaque mot était traduit de manière unique, selon la machine. De tels systèmes ne sont plus utilisés, car ils ont été remplacés par des méthodes plus avancées basées sur les phrases.

#### SMT basée sur les phrases

Cette méthode est basée sur tous les principes de traduction basée sur les mots : statistiques, réordonnancement et astuces lexicales. Cependant, pour l'apprentissage, elle divise le texte non seulement en mots mais aussi en phrases. Il s'agissait des n-grammes, pour être précis, qui étaient une séquence contiguë de n mots à la suite.

Ainsi, la machine apprenait à traduire des combinaisons stables de mots, ce qui améliorait notablement la précision.

![Image](https://cdn-media-1.freecodecamp.org/images/lGJNqYGZOJMjs23F8-xf6E4buXptvm2IBzjg)

L'astuce était que les phrases n'étaient pas toujours des constructions syntaxiques simples, et la qualité de la traduction chutait considérablement si quelqu'un qui était conscient de la linguistique et de la structure des phrases intervenait. Frederick Jelinek, le pionnier de la linguistique informatique, en a plaisanté une fois : « Chaque fois que je renvoie un linguiste, la performance du reconnaisseur de parole augmente. »

Outre l'amélioration de la précision, la traduction basée sur les phrases offrait plus d'options dans le choix des textes bilingues pour l'apprentissage. Pour la traduction basée sur les mots, la correspondance exacte des sources était cruciale, ce qui excluait toute traduction littéraire ou libre. La traduction basée sur les phrases n'avait aucun problème à apprendre d'eux. Pour améliorer la traduction, les chercheurs ont même commencé à analyser les sites d'actualités dans différentes langues à cette fin.

![Image](https://cdn-media-1.freecodecamp.org/images/Y9xbp5BnvnRGFuAlJOamXjfYEcAYVr9lVJDA)

À partir de 2006, tout le monde a commencé à utiliser cette approche. Google Translate, Yandex, Bing et autres traducteurs en ligne de haut niveau fonctionnaient comme des systèmes basés sur les phrases jusqu'en 2016. Chacun d'entre vous peut probablement se rappeler les moments où Google traduisait la phrase de manière impeccable ou résultait en un non-sens complet, non ? Le non-sens venait des caractéristiques basées sur les phrases.

La bonne vieille approche basée sur les règles fournissait de manière constante un résultat prévisible, bien que terrible. Les méthodes statistiques étaient surprenantes et déconcertantes. Google Translate transforme « three hundred » en « 300 » sans aucune hésitation. C'est ce qu'on appelle une anomalie statistique.

La traduction basée sur les phrases est devenue si populaire que lorsque vous entendez « traduction automatique statistique », c'est ce qui est réellement entendu. Jusqu'en 2016, toutes les études [louaient](http://www.aclweb.org/anthology/D16-1161) la traduction basée sur les phrases comme l'état de l'art. À l'époque, personne ne pensait même que Google attisait déjà ses feux, se préparant à changer notre image de la traduction automatique.

### SMT basée sur la syntaxe

Cette méthode doit également être mentionnée, brièvement. De nombreuses années avant l'émergence des réseaux de neurones, la traduction basée sur la syntaxe était considérée comme « l'avenir de la traduction », mais l'idée n'a pas décollé.

Les partisans de la traduction basée sur la syntaxe croyaient qu'il était possible de la fusionner avec la méthode basée sur les règles. Il est nécessaire de faire une analyse syntaxique assez précise de la phrase — pour déterminer le sujet, le prédicat et les autres parties de la phrase, puis pour construire un arbre de phrase. En l'utilisant, la machine apprend à convertir les unités syntaxiques entre les langues et traduit le reste par des mots ou des phrases. Cela aurait résolu le problème de l'alignement des mots une fois pour toutes.

![Image](https://cdn-media-1.freecodecamp.org/images/JKfKjepj-r-NgsmX7A1qipPF7Jb1LEJYghAQ)
_Exemple tiré de la [grande présentation](http://www.aclweb.org/anthology/P01-1067" rel="noopener" target="_blank" title="">Yamada et Knight [2001]</a> et de celle-ci <a href="http://homepages.inf.ed.ac.uk/pkoehn/publications/esslli-slides-day5.pdf" rel="noopener" target="_blank" title=")._

Le problème est que l'analyse syntaxique fonctionne terriblement, malgré le fait que nous la considérions comme résolue il y a quelque temps (puisque nous avons les bibliothèques prêtes à l'emploi pour de nombreuses langues). J'ai essayé d'utiliser des arbres syntaxiques pour des tâches un peu plus compliquées que l'analyse du sujet et du prédicat. Et à chaque fois, j'ai abandonné et utilisé une autre méthode.

Faites-moi savoir dans les commentaires si vous réussissez à l'utiliser au moins une fois.

### Traduction automatique neuronale (NMT)

Un article assez amusant sur l'utilisation des réseaux de neurones dans la traduction automatique a été publié en 2014. Internet ne l'a pas remarqué du tout, sauf Google — ils ont sorti leurs pelles et ont commencé à creuser. Deux ans plus tard, en novembre 2016, Google a fait une annonce révolutionnaire.

L'idée était proche du transfert de style entre les photos. Vous vous souvenez des applications comme [Prisma](https://prisma-ai.com/), qui amélioraient les images dans le style d'un artiste célèbre ? Il n'y avait pas de magie. Le réseau de neurones [a été enseigné](https://harishnarayanan.org/writing/artistic-style-transfer/) à reconnaître les peintures de l'artiste. Ensuite, les dernières couches contenant la décision du réseau ont été supprimées. L'image stylisée résultante était simplement l'image intermédiaire que le réseau obtenait. C'est la fantaisie du réseau, et nous la considérons comme belle.

![Image](https://cdn-media-1.freecodecamp.org/images/BzkZsyBq0kWiBKdPvt41ZPhyL-vecimThXod)

Si nous pouvons transférer le style à la photo, que se passe-t-il si nous essayons d'imposer une autre langue à un texte source ? Le texte serait ce style précis de « l'artiste », et nous essaierions de le transférer tout en conservant l'essence de l'image (en d'autres termes, l'essence du texte).

Imaginez que j'essaie de décrire mon chien — taille moyenne, nez pointu, queue courte, aboie toujours. Si je vous donnais cet ensemble de caractéristiques du chien, et si la description était précise, vous pourriez le dessiner, même si vous ne l'avez jamais vu.

![Image](https://cdn-media-1.freecodecamp.org/images/6oDjU1XWlLo1313uKFsTLN43bv5FbVTTC5Oh)

Maintenant, imaginez que le texte source est l'ensemble de caractéristiques spécifiques. En gros, cela signifie que vous l'encodez, et laissez un autre réseau de neurones le décoder en texte, mais dans une autre langue. Le décodeur ne connaît que sa langue. Il n'a aucune idée de l'origine des caractéristiques, mais il peut les exprimer en, par exemple, espagnol. En continuant l'analogie, peu importe comment vous dessinez le chien — avec des crayons, de l'aquarelle ou votre doigt. Vous le peignez comme vous pouvez.

Encore une fois — un réseau de neurones ne peut encoder la phrase qu'en un ensemble spécifique de caractéristiques, et un autre ne peut les décoder qu'en texte. Les deux n'ont aucune idée l'un de l'autre, et chacun d'eux ne connaît que sa propre langue. Cela vous rappelle quelque chose ? L'interlingua est de retour. Ta-da.

![Image](https://cdn-media-1.freecodecamp.org/images/2TRCJS9nG0g1YVZPzbeg3DKvZLgsMEEiBXRs)

La question est, comment trouvons-nous ces caractéristiques ? C'est évident lorsque nous parlons du chien, mais comment traiter avec le texte ? Il y a trente ans, les scientifiques ont déjà tenté de créer le code de langue universelle, et cela s'est terminé par un échec total.

Néanmoins, nous avons maintenant l'apprentissage profond. Et c'est sa tâche essentielle ! La distinction principale entre l'apprentissage profond et les réseaux de neurones classiques réside précisément dans la capacité à rechercher ces caractéristiques spécifiques, sans aucune idée de leur nature. Si le réseau de neurones est suffisamment grand, et qu'il y a quelques milliers de cartes graphiques à portée de main, il est possible de trouver ces caractéristiques dans le texte également.

Théoriquement, nous pouvons transmettre les caractéristiques obtenues des réseaux de neurones aux linguistes, afin qu'ils puissent ouvrir de nouveaux horizons.

La question est, quel type de réseau de neurones devrait être utilisé pour l'encodage et le décodage ? Les réseaux de neurones convolutifs (CNN) conviennent parfaitement pour les images puisqu'ils opèrent avec des blocs indépendants de pixels.

Mais il n'y a pas de blocs indépendants dans le texte — chaque mot dépend de son environnement. Le texte, la parole et la musique sont toujours cohérents. Les réseaux de neurones récurrents (RNN) seraient donc le meilleur choix pour les traiter, puisqu'ils se souviennent du résultat précédent — le mot précédent, dans notre cas.

Maintenant, les RNN sont utilisés partout — la reconnaissance vocale de Siri (il analyse la séquence de sons, où le suivant dépend du précédent), les suggestions du clavier (mémorise le précédent, devine le suivant), la génération de musique, et même les chatbots.

![Image](https://cdn-media-1.freecodecamp.org/images/DD6GvRmtxZGhC9toN1CHXUBWLhUXLpJSiJF5)

> **Pour les passionnés comme moi :** en fait, l'architecture des traducteurs neuronaux varie largement. Le RNN régulier était utilisé au début, puis mis à niveau en bidirectionnel, où le traducteur considérait non seulement les mots avant le mot source, mais aussi le mot suivant. C'était beaucoup plus efficace. Ensuite, il a suivi avec le RNN multicouche hardcore avec des unités LSTM pour le stockage à long terme du contexte de traduction.

En deux ans, les réseaux de neurones ont surpassé tout ce qui était apparu au cours des 20 dernières années de traduction. La traduction neuronale contient 50 % d'erreurs d'ordre des mots en moins, 17 % d'erreurs lexicales en moins et 19 % d'erreurs de grammaire en moins. Les réseaux de neurones ont même appris à harmoniser le genre et le cas dans différentes langues. Et personne ne leur a appris à le faire.

Les améliorations les plus notables se sont produites dans des domaines où la traduction directe n'a jamais été utilisée. Les méthodes de traduction automatique statistique fonctionnaient toujours en utilisant l'anglais comme source clé. Ainsi, si vous traduisiez du russe vers l'allemand, la machine traduisait d'abord le texte en anglais puis de l'anglais vers l'allemand, ce qui conduit à une double perte.

La traduction neuronale n'a pas besoin de cela — seul un décodeur est requis pour qu'elle puisse fonctionner. C'était la première fois que la traduction directe entre des langues sans dictionnaire commun devenait possible.

![Image](https://cdn-media-1.freecodecamp.org/images/9RYJB0uToAIdePWQ3ZDqO392eXNJqKA46C6S)

#### Google Translate (depuis 2016)

En 2016, Google a activé la traduction neuronale pour [neuf langues](https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation). Ils ont développé leur système nommé Google Neural Machine Translation (GNMT). Il se compose de 8 couches d'encodeurs et 8 couches de décodeurs de RNN, ainsi que de connexions d'attention du réseau de décodeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/9ZNTL9njX6FZP3zKlE7q5fnOgedwQGi6H6Ws)

Ils n'ont pas seulement divisé les phrases, mais aussi les mots. C'est ainsi qu'ils ont traité l'un des principaux problèmes de la NMT — les mots rares. Les NMT sont impuissants lorsque le mot n'est pas dans leur lexique. Disons, « Vas3k ». Je doute que quelqu'un ait appris au réseau de neurones à traduire mon surnom. Dans ce cas, GMNT essaie de diviser les mots en morceaux de mots et de récupérer leur traduction. Intelligent.

> Astuce : Google Translate utilisé pour la traduction de sites Web dans le navigateur utilise toujours l'ancien algorithme basé sur les phrases. D'une manière ou d'une autre, Google ne l'a pas mis à niveau, et les différences sont assez visibles par rapport à la version en ligne.

Google utilise un mécanisme de crowdsourcing dans la version en ligne. Les gens peuvent choisir la version qu'ils considèrent comme la plus correcte, et si de nombreux utilisateurs l'aiment, Google traduira toujours cette phrase de cette manière et la marquera avec un badge spécial. Cela fonctionne fantastiquement pour les phrases courtes et quotidiennes telles que « Allons au cinéma » ou « Je t'attends ». Google connaît l'anglais conversationnel mieux que moi :(

Bing de Microsoft fonctionne exactement comme Google Translate. Mais Yandex est différent.

#### Yandex Translate (depuis 2017)

Yandex a lancé son système de traduction neuronale en 2017. Sa principale caractéristique, comme déclaré, était l'hybridité. Yandex combine les approches neuronales et statistiques pour traduire la phrase, puis choisit la meilleure avec son algorithme préféré CatBoost.

Le problème est que la traduction neuronale échoue souvent lors de la traduction de phrases courtes, car elle utilise le contexte pour choisir le bon mot. Cela serait difficile si le mot apparaissait très peu de fois dans les données d'entraînement. Dans de tels cas, une simple traduction statistique trouve rapidement et simplement le bon mot.

![Image](https://cdn-media-1.freecodecamp.org/images/-7nyvsxkdMVtSkHOErvs4fINwnbg9shky24U)

Yandex ne partage pas les détails. Il nous repousse avec des communiqués de presse marketing [press-releases](https://yandex.com/company/blog/one-model-is-better-than-two-yu-yandex-translate-launches-a-hybrid-machine-translation-system/). D'ACCORD.

> Il semble que Google utilise la SMT pour la traduction des mots et des phrases courtes. Ils ne le mentionnent dans aucun article, mais c'est assez visible si vous regardez la différence entre la traduction des expressions courtes et longues. De plus, la SMT est utilisée pour afficher les statistiques des mots.

### La conclusion et l'avenir

Tout le monde est toujours excité par l'idée du « poisson Babel » — la traduction instantanée de la parole. Google a fait des pas dans cette direction avec ses Pixel Buds, mais en fait, ce n'est toujours pas ce dont nous rêvions. La traduction instantanée de la parole est différente de la traduction habituelle. Vous devez savoir quand commencer à traduire et quand vous taire et écouter. Je n'ai pas encore vu d'approches appropriées pour résoudre cela. Sauf, peut-être, Skype...

Et voici un autre domaine vide : tout l'apprentissage est limité à un ensemble de blocs de texte parallèles. Les réseaux de neurones les plus profonds apprennent toujours à partir de textes parallèles. Nous ne pouvons pas enseigner au réseau de neurones sans lui fournir une source. Les gens, en revanche, peuvent compléter leur lexique en lisant des livres ou des articles, même sans les traduire dans leur langue maternelle.

Si les gens peuvent le faire, le réseau de neurones peut le faire aussi, en théorie. J'ai trouvé [un seul](https://arxiv.org/abs/1710.04087) prototype tentant d'inciter le réseau, qui connaît une langue, à lire les textes dans une autre langue afin de gagner de l'expérience. J'essaierais moi-même, mais je suis stupide. Bon, c'est tout.

> Cette histoire a été écrite à l'origine en russe puis traduite en anglais sur [**Vas3k.com**](http://vas3k.com/blog/machine_translation/) par Vasily Zubarev. Il est mon ami par correspondance et je suis assez sûr que son blog devrait être diffusé.

### Liens utiles

* [Philipp Koehn: Statistical Machine Translation](https://www.amazon.com/dp/0521874157/). La collection la plus complète des méthodes que j'ai trouvée.
* [Moses](http://www.statmt.org/moses/) — bibliothèque populaire pour créer ses propres traductions statistiques
* [OpenNMT](http://opennmt.net/) — une autre bibliothèque, mais pour les traducteurs neuronaux
* L'article de l'un de mes blogueurs préférés [expliquant RNN et LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* Une vidéo [How to Make a Language Translator](https://www.youtube.com/watch?v=nRBnh4qbPHI), un gars drôle, une explication soignée. Toujours pas assez.
* Guide texte de TensorFlow sur la [création de votre propre traducteur neuronal](https://www.tensorflow.org/tutorials/seq2seq), pour ceux qui veulent plus d'exemples et essayer le code.

#### Autres articles de Vas3k.com

[**Comment Ethereum et les Smart Contracts fonctionnent**](http://vas3k.com/blog/ethereum/)  
[_Machine de Turing distribuée avec protection Blockhain_vas3k.com](http://vas3k.com/blog/ethereum/)[**Blockchain Inside Out: How Bitcoin Works**](http://vas3k.com/blog/blockchain/)  
[_Une fois pour toutes en mots simples_vas3k.com](http://vas3k.com/blog/blockchain/)

#### Une dernière chose...

_Si vous avez aimé cet article, cliquez sur le_? _ci-dessous, et partagez-le avec d'autres personnes pour qu'elles puissent en profiter également._