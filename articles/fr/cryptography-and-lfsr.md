---
title: Une introduction à la cryptographie et aux registres à décalage à rétroaction
  linéaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-22T12:02:44.000Z'
originalURL: https://freecodecamp.org/news/cryptography-and-lfsr
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/tommy-lee-walker-409690-unsplash-1.jpg
tags:
- name: ciphers
  slug: ciphers
- name: Cryptography
  slug: cryptography
- name: encryption
  slug: encryption
- name: Mathematics
  slug: mathematics
- name: Python
  slug: python
seo_title: Une introduction à la cryptographie et aux registres à décalage à rétroaction
  linéaire
seo_desc: 'By Magdalena Stenius

  All around us data is transferred faster than ever. Sensitive data is also part
  of our everyday life. To protect that data, we use encryption. When we encrypt data,
  it changes in some way that renders it useless to the possible v...'
---

Par Magdalena Stenius

Autour de nous, les données sont transférées plus rapidement que jamais. Les données sensibles font également partie de notre vie quotidienne. Pour protéger ces données, nous utilisons le chiffrement. Lorsque nous chiffrons des données, elles sont modifiées de manière à les rendre inutilisables pour un éventuel observateur, mais peuvent être rétablies dans leur état d'origine lorsqu'elles arrivent en toute sécurité au destinataire prévu. Ces transformations reposent fortement sur les mathématiques, et particulièrement sur un domaine des mathématiques appelé théorie des nombres. Ce texte nous guide à travers les bases de la cryptographie, tant d'un point de vue mathématique que comme une question de programmation.

#### Les chiffres hier et aujourd'hui

Depuis que l'écriture existe, le concept de chiffrement a vécu et évolué aux côtés de l'écriture en texte clair. L'idée de rendre le texte apparemment incompréhensible dans le but de garder un secret a été centrale, surtout dans l'usage militaire et la politique. Le mot « chiffre » provient du Moyen Âge, de mots tels que le latin _cifra_ et l'arabe _صفر_ (sifr), qui signifie « zéro ». Il existe de nombreuses théories sur pourquoi zéro aurait été utilisé pour décrire le chiffrement, y compris le fait que le concept de zéro ne faisait pas partie du système de numération romain et était vu comme un mystère parmi les nombres. L'un des plus anciens et des plus connus chiffres utilisés dans un contexte militaire est le chiffre de César, également connu sous le nom de décalage de César.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IehC7dyPV4f4mFcAUwQtfA.png)
_Décalage de César en Python3._

Le décalage de César utilise une seule clé, qui est utilisée pour décaler chaque caractère dans le texte clair. Cette clé unique est la faiblesse du chiffre : une fois que le décalage correct est découvert, tout le message est révélé. Mathématiquement, ce type de chiffre peut être écrit comme un problème en arithmétique modulaire, qui fonctionne avec des valeurs enveloppées dans une plage spécifique. Nous en discuterons plus en profondeur plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_Mt2X5MKczLf0WpslKCUvkA.png)
_Chiffrement et déchiffrement par décalage en tant qu'arithmétique modulaire utilisant un alphabet de 26 lettres._

La manière dont nous pouvons résoudre le texte clair à partir du texte chiffré est de trouver la clé. Dans le cas d'un chiffre de César de valeur 3, découvrir la clé (3) nous permet de déchiffrer tout le texte en une seule fois. La clé spécifie la sortie de l'algorithme de chiffrement.

#### Facteurs et nombres premiers

Peut-être de manière surprenante, l'un des concepts fondamentaux qui pose les bases du chiffrement est celui de la divisibilité. Pour définir ce que cela signifie, établissons quelques règles. Tout d'abord, si nous avons _a_ et _b_ qui sont des entiers et que _a_ n'est pas 0, _a_ divise _b_ s'il existe un entier _k_ qui satisfait l'énoncé suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bBWKJzCZ7cSSXjV3Mdk6Og.png)
_A est un facteur de b._

Dans le cas où nous trouvons un entier qui est plus grand que 1 et qui n'a pas d'autres facteurs positifs que 1 et lui-même, nous l'appelons un _nombre premier_. Les entiers plus grands que un qui ne sont pas premiers sont connus sous le nom de _nombres composés_, en raison de leur nature composée. Par exemple, 4 est plus grand que 1 et il a un facteur 2. Par conséquent, c'est un composé. D'autre part, 3 est un entier plus grand que un, mais il n'a pas d'autres facteurs positifs que 1 et lui-même. C'est un nombre premier. D'autres petits nombres premiers sont 2, 5, 7, 11 et 13.

Selon le théorème fondamental de l'arithmétique, chaque entier plus grand que 1 peut être écrit comme un produit unique de nombres premiers. C'est une bonne nouvelle pour les cryptographes, car ils adorent travailler avec les nombres premiers. Pourquoi cela ? Eh bien, l'une des raisons les plus directes est que la factorisation en nombres premiers de grands nombres prend beaucoup de temps. De nombreux systèmes de chiffrement bien connus tels que RSA sont entièrement basés sur ce fait. Le principe sur lequel il repose est qu'il existe une clé publique (un produit de deux grands nombres premiers) qui est utilisée pour chiffrer le message, et une clé secrète (contenant ces nombres premiers) qui est utilisée pour déchiffrer le message. Ces nombres premiers font généralement environ 300 chiffres de long.

#### Une question de congruence

La modularité est l'un des piliers fondamentaux de la cryptographie. Abordons d'abord ce concept d'un point de vue de la division. Que se passe-t-il si nous avons 5 petits bonbons et trois étudiants ? Chaque étudiant reçoit un bonbon, et il en reste 2. Cela peut être décrit comme suit.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/rremainder.png)
_R est le reste de a lorsqu'il est divisé par n._

Pouvez-vous trouver les autres quantités de bonbons qui laissent 2 comme reste lorsqu'ils sont divisés entre les 3 étudiants ? La quantité suivante serait 8, car chaque étudiant recevrait deux bonbons et il en resterait à nouveau 2. Cela peut être décrit en utilisant la congruence. 8 et 5 sont congruents modulo 3, ce qui signifie qu'ils laissent le même reste lorsqu'ils sont divisés par 3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F0-jvG8EMA5hPMNJAgchxA.png)
_5 est congru à 8 modulo 3._

Dans l'exemple du décalage de César, nous utilisons un alphabet qui se compose de 26 lettres. Nous ne travaillons qu'avec ces 26 valeurs. Après 'Z', nous revenons à 'A'. C'est la modularité en pratique. 'A' sera toujours à la position 1 dans notre liste de 26 lettres, donc tout compte de position que nous obtenons, si nous le divisons par 26 et que le reste est 1, nous savons utiliser 'A'. Cela enveloppe nos nombres dans un champ fini, dans lequel la valeur la plus grande est 26. En pratique, si mon message secret serait 'ABC', je le convertirais d'abord en les nombres 123. Après cela, j'appliquerais le décalage. Dans le cas où la clé serait 3, le décalage produirait 456. Après cela, je pointerais les nombres vers leurs représentations en lettres, qui sont dans la classe de modulo 26. Le message chiffré devient 'DEF'.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/again.png)
_Encore une fois, chiffrement et déchiffrement en tant qu'arithmétique modulaire utilisant un alphabet de 26 lettres._

Vous pouvez penser à cela comme une horloge. Lorsque l'aiguille a fait le tour de l'horloge, elle se retrouve là où elle a commencé. En arithmétique modulaire, le dernier entier est suivi par le premier. Une autre façon de comprendre cela est que dans le monde d'un modulo spécifique, seule cette quantité de valeurs existe. Par exemple, en modulo 2, seules 2 valeurs existent. Dans notre alphabet, 26 valeurs existent, et ainsi de suite.

#### Types de chiffres

Le type de clés qu'un chiffre utilise peut être utilisé pour catégoriser le chiffre en clés asymétriques et symétriques. Ils diffèrent par la question de quelle clé est utilisée pour le chiffrement et le déchiffrement. Les chiffres symétriques sont chiffrés et déchiffrés en utilisant la même clé (comme le chiffre de César). Les chiffres à clé asymétrique sont déchiffrés avec une clé différente de celle avec laquelle ils sont créés, comme le système de chiffrement RSA dont nous avons brièvement parlé plus tôt. Cela entraîne un temps plus long pour créer le chiffrement, mais le résultat est également beaucoup plus sécurisé.

Une autre façon de catégoriser les chiffres est par leur manière de fonctionner en flux ou en blocs. Les chiffres en flux sont des chiffres à clé symétrique qui fonctionnent sur des flux continus de symboles. Par exemple, les chiffrements utilisés dans Bluetooth sont un chiffre en flux. Il va sans dire qu'à l'ère de la communication sans fil avec un besoin de chiffrement, les chiffres en flux sont devenus une partie vitale de la technologie mobile.

#### Un regard sur les chiffres en flux

Vous souvenez-vous que nous avons discuté du concept d'arithmétique modulaire plus tôt ? En bref, les arithmétiques modulaires sont des arithmétiques dans un champ fini. Maintenant, jetons un coup d'œil à un autre chiffre qui fonctionne avec un champ fini de valeurs (également connu sous le nom de champ de Galois). Ce chiffre, cependant, ne produit pas toujours les mêmes valeurs étant donné la même entrée, comme le fait le décalage. Son but est de produire un flux de clés utilisé pour chiffrer un autre flux. Comme un serpent qui se mord la queue (un symbole souvent utilisé pour l'éternité), les registres à décalage à rétroaction linéaire fonctionnent en se nourrissant de leur propre sortie. Ils sont construits de manière à ce qu'ils cyclent sans fin à travers un motif de valeurs tout en produisant ce motif apparemment aléatoire. La graine et toutes les valeurs produites sont binaires, ce qui signifie qu'elles prennent les valeurs 0 ou 1. La manière dont les nouvelles valeurs sont créées est en utilisant un opérateur logique, généralement le ou exclusif (XOR).

![Image](https://www.freecodecamp.org/news/content/images/2019/06/logical.png)
_Porte logique XOR._

Pour décrire cela de manière pratique, commençons à regarder ce dont nous avons besoin pour créer un LFSR. Nous avons besoin d'une graine, qui est une liste de uns et de zéros. La graine sera ce que nous commençons à décaler. En plus de notre graine (ou registre à décalage), nous avons une collection de prises. Les prises nous indiquent quelles parties du registre nous utilisons lorsque nous les réinjectons. Supposons que nous avons une graine 001 et deux prises, 1 et 3. Cela signifie que lorsque nous commençons à décaler, la nouvelle valeur sera une combinaison des premier et troisième nombres de la graine, 0 et 1. Nous utilisons une opération appelée ou exclusif pour combiner les deux. 0 xor 1 donne 1. Puisque nous travaillons avec des valeurs binaires, la rétroaction de nos prises peut être exprimée comme un polynôme en modulo 2.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o9K4JH2YxEzjieQco9pTxA.png)
_Le polynôme de rétroaction des prises 3 et 1._

Donc, si notre registre à décalage est 001 et que nous obtenons une nouvelle valeur, 1, nous l'insérons au début et nous supprimons le dernier nombre. Notre nouvel état de registre à décalage est maintenant 100. Nous continuons ce décalage jusqu'à ce que nous remarquions que notre registre à décalage est revenu à son état initial, 001. Selon la graine et les prises que nous sélectionnons, nous pouvons obtenir des boucles de différentes longueurs. Une boucle est appelée _longueur maximale_ si elle passe par toutes les combinaisons différentes possibles avant d'atteindre son état d'origine. Puisque nous utilisons le système binaire, la longueur maximale d'une boucle sera de 2^n-1. La boucle peut également finir par quitter son état d'origine et se retrouver bloquée dans une boucle plus courte à l'intérieur, ne revenant jamais à son état d'origine. Trouver les graines et les prises qui mènent à un cycle de longueur maximale est essentiel. Certains des critères pour trouver ces prises sont que le nombre de prises doit être pair et que les prises sont des co-premiers ensemblistes, ce qui signifie qu'ils n'ont pas de diviseur commun autre que 1.

Attendez, cela ne semble pas si aléatoire ! Une boucle comme celle-ci ne serait-elle pas assez facile à craquer ? Le problème avec les registres à décalage est qu'ils deviennent assez longs, assez rapidement. Supposons que nous choisissons une graine de 20 bits et une prise de deux valeurs, 2 et 19. La longueur de la boucle produite est de 1 048 575, ce qui signifie que nous obtiendrions une quantité assez grande de valeurs binaires apparemment aléatoires.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/lfsrpy.png)
_Registre à décalage à rétroaction linéaire en Python3._

La variante de LFSR que nous avons brièvement parcourue est appelée Fibonacci LFSR. Il existe également d'autres variations, dans lesquelles la manière dont le registre est décalé diffère. Ils fonctionnent tous pour produire un flux pseudo-aléatoire de bits utilisé pour chiffrer des flux. La gamme d'applications pour ce type de chiffrement va du Bluetooth aux normes GSM (communication cellulaire).

#### En conclusion

En tant que programmeur, apprendre le concept d'arithmétique modulaire et de division ouvre de nouvelles façons de penser aux problèmes de codage quotidiens. Cependant, dans les projets critiques pour la sécurité, l'utilisation de systèmes et de normes prêts à l'emploi pour le chiffrement est toujours recommandée, car les spécialistes dans le domaine de la cryptographie trouvent probablement une solution plus sûre et plus efficace qu'un hobbyiste enthousiaste.

Sources :

[Structures algébriques en cryptographie par V. Niemi](http://delta.utu.fi/about/monistemyynti/)

[Tutoriel sur les registres à décalage à rétroaction linéaire par EETimes](https://www.eetimes.com/document.asp?doc_id=1274550)

[Encyclopédie de la cryptographie et de la sécurité par Anne Canteout](https://www.rocq.inria.fr/secret/Anne.Canteaut/MPRI/chapter3.pdf)