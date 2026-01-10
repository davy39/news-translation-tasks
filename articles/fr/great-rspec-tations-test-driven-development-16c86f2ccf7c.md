---
title: 'Grandes RSpec-tations : pourquoi j''adore le développement piloté par les
  tests'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-23T23:57:01.000Z'
originalURL: https://freecodecamp.org/news/great-rspec-tations-test-driven-development-16c86f2ccf7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OvF5QBJTAjMURU4G2BSWNA.jpeg
tags:
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: technology
  slug: technology
- name: test driven development
  slug: test-driven-development
- name: women in tech
  slug: women-in-tech
seo_title: 'Grandes RSpec-tations : pourquoi j''adore le développement piloté par
  les tests'
seo_desc: 'By Arit Amana

  When I first wrote about Test-Driven Development, I thought I was in love with the
  concept… but that was just the flirting stage. Now I’ve fallen head-over-Louboutins,
  girlfriend! ?

  The efficiency gains from not needing to fire my app u...'
---

Par Arit Amana

Lorsque j'ai écrit pour la première fois sur le [développement piloté par les tests](https://code.likeagirl.io/what-done-looks-like-test-driven-development-e9b0eaa38836), je pensais être amoureuse du concept… mais ce n'était que la phase de flirt. Maintenant, je suis tombée tête baissée, ma chère ! ?

Les gains d'efficacité liés à la non-nécessité de lancer mon application pour les tests ne sont qu'un début. Développer mes applications avec [RSpec](http://rspec.info/) me force à vraiment réfléchir à la manière dont je définis et structure mon code. De plus, chaque fois que mes tests échouent, ils fournissent fidèlement des conseils et des indices qui m'aident à dépanner ce qui manque, est cassé ou redondant. Voici une métaphore pour la vie en général… mais je m'égare. ?

Je crée une application d'échecs en ligne [dans le cadre d'une équipe de développement agile](https://code.likeagirl.io/no-longer-the-lone-coding-wolf-4fb52360b808), et cette semaine, j'ai été chargée de construire la méthode **move_to!(x,y)**. Cela devrait déplacer une pièce d'échecs (appelée **pawn** par la suite) vers la case de l'échiquier à l'emplacement **(x,y)**.

Si une pièce de l'adversaire (appelée **king** par la suite) occupe (x,y), pawn devrait la capturer. Si un frère d'armes de pawn occupe (x,y), la méthode devrait lever un message d'erreur et pawn ne devrait aller nulle part.

Note : move_to!(x,y) ne considère pas si les déplacements ou les captures sont valides. D'autres méthodes le feront.

J'ai configuré [FactoryBot](https://github.com/thoughtbot/factory_bot) pour générer des instances d'une partie d'échecs. Chaque pièce d'échecs a les attributs pertinents suivants : **:location_x**, **:location_y**, **:white** (un booléen ; **true** = couleur blanche), **:game_id**, et **:notcaptured** (un booléen ; **false** = la pièce a été capturée). Mon premier test a déterminé si pawn (actuellement sur 0,0) s'est déplacé vers une case vide (7,7) :

Ensuite, j'ai commencé à écrire la méthode **move_to!(x,y)**, puis j'ai exécuté mon test :

```
arit (master) chessapp $ rspec spec/models/piece_spec.rb
```

```
.
```

```
Terminé en 0,43495 secondes (les fichiers ont pris 15,68 secondes à charger)
```

```
1 exemple, 0 échecs
```

Oui ! Aucune erreur. ?? Ensuite, j'ai écrit un test pour déterminer si pawn restait en place si sa destination était occupée par une pièce amie (nous l'appellerons ro**ok) :**

Pourquoi ne teste-je pas les valeurs de **rook.notcaptured**, **rook.location_x** et **rook.location_y** ? Eh bien, la tour EST la pièce amie en question, mais ce que nous testons réellement, c'est la pièce (si elle existe) qui est **trouvée et sauvegardée dans la variable _destination_**. Maintenant, pour étoffer la méthode :

Mes tests ont encore réussi ! ?? Me sentant très confiante, je suis passée au troisième test : pour déterminer si le roi de l'adversaire était capturé et si pawn prenait sa place :

J'ai également complété la méthode :

Mais lorsque j'ai exécuté mes tests, j'ai reçu l'erreur suivante :

```
arit (master *) chessapp $ rspec spec/models/piece_spec.rb
```

```
..F
```

```
Échecs :
```

```
1) Piece captures opponent's piece on destination, then assumes that position
```

```
Échec/Erreur : expect(destination.notcaptured).to be false
```

```
attendu false
```

```
obtenu true
```

```
# ./spec/models/piece_spec.rb:104:in `block (2 levels) in <top (required)>'
```

```
Terminé en 0,21787 secondes (les fichiers ont pris 4,83 secondes à charger)
```

```
1 exemple, 1 échec
```

```
Exemples échoués :
```

```
rspec ./spec/models/piece_spec.rb:95 # Piece captures opponent's piece on destination, then assumes that position
```

Quoi ??? **destination.notcaptured** n'a pas été mis à jour ? Pourquoi ? J'ai relu ma méthode encore et encore. Rien ne semblait manquer ou être cassé (et, vraiment, combien de choses pouvais-je me tromper en 11 lignes de code ?).

Après avoir décidé de faire comme un ? et de revoir mon test rspec lentement, il m'est venu à l'esprit que la variable d**estination** était censée changer. La méthode move_to!(x,y) avait mis à jour ses attributs l**ocation_x, location_y** et n**otcaptured**.

Puis cela m'a frappé — je devais RECHARGER **destination** depuis la base de données dans RSpec. Ensuite, mes trois tests ont réussi magnifiquement :

Le développement piloté par les tests a eu un impact permanent sur ma pratique de la programmation, et j'ai savouré l'opportunité de convertir le reste de mes coéquipiers à cette méthode. Le TDD est léger, efficace, sûr, révélateur, et il m'aide à produire un code de meilleure qualité dès la première… eh bien, d'accord… en aussi peu de temps que possible ! ?