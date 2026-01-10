---
title: Améliorez vos messages de commit Git avec Atom
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-20T21:22:01.000Z'
originalURL: https://freecodecamp.org/news/towards-better-git-commit-messages-using-atom-6dbda5e14984
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5El6ItJ_0MabNL0UXNvShw.jpeg
tags:
- name: Git
  slug: git
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Améliorez vos messages de commit Git avec Atom
seo_desc: 'By Hasit Mistry

  Recently, I came across two enlightening posts about writing better Git commit messages.
  These posts give suggestions about how a well structured commit message should look
  like, and provide clear examples.


  Better Commit Messages wit...'
---

Par Hasit Mistry

Récemment, je suis tombé sur deux articles éclairants sur la rédaction de meilleurs messages de commit Git. Ces articles donnent des suggestions sur la façon dont un message de commit bien structuré devrait ressembler, et fournissent des exemples clairs.

* [De meilleurs messages de commit avec un modèle .gitmessage](https://robots.thoughtbot.com/better-commit-messages-with-a-gitmessage-template) par [Matthew Summer](http://appallingfarrago.com/)
* [Comment écrire un message de commit Git](http://chris.beams.io/posts/git-commit/) par [Chris Beams](http://chris.beams.io/)

Ces deux articles de blog m'ont fait revenir à mes dépôts et relire mes messages de commit. Et pour être honnête, je me suis un peu honteux de mon passé.

Vous pourriez demander, « pourquoi les messages de commit sont-ils même importants ? » Si vous vous posez cette question, vous êtes comme la version de moi d'il y a une semaine.

Juste pour vous donner une idée, la Figure 1 montre certains des messages de commit de mon projet [licensethis](https://github.com/hasit/licensethis/). Je promets que le code est bien meilleur que les messages de commit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qlezTXx2CxPpbS4wa4XKqg.png)
_Figure 1. Messages de commit de [licensethis](https://github.com/hasit/licensethis/" rel="noopener" target="_blank" title=") du début de cette année._

Il n'est pas surprenant que ces messages de commit ne me disent que peu de choses sur mon travail passé. C'est parce que je n'ai pas pris leur rédaction au sérieux.

Pour comprendre réellement les changements apportés par chaque commit, j'ai dû ouvrir chaque commit et lire les changements ligne par ligne. C'est fastidieux, pour le moins.

Au moment de la rédaction de ces messages de commit, je me contentais de dire ce qui me passait par la tête à ce moment-là, sans tenir compte de la façon dont moi — ou toute autre personne — comprendrais le texte plus tard.

Tout d'abord, synthétisons toutes les informations que nous avons absorbées des articles de blog mentionnés ci-dessus. Ensuite, je donnerai des conseils pratiques sur la façon dont [Atom](https://atom.io/) peut être utilisé comme outil pour écrire de meilleurs messages de commit pour moi et pour ceux qui sont intéressés à faire de même.

Notez que je ne vais pas écrire sur la façon d'écrire un bon message de commit. L'article merveilleux de [Chris Beams](http://chris.beams.io/) sur [Comment écrire un message de commit Git](http://chris.beams.io/posts/git-commit/) explique cela et plus encore en sept règles.

Avant de commencer, examinons le bloc de texte suivant pour comprendre ce qui est considéré comme un message de commit bien structuré, intentionnel et bien écrit :

```
# Sujet en (de préférence) moins de 50 caractèresCeci est le sujet de ce message de commit
```

```
# Corps en détailCeci est le corps de ce message de commit. Le corps est écrit après la ligne de sujet avec une ligne vide entre les deux. La ligne vide est utilisée par divers outils (comme 'git log', 'git show', etc.) pour différencier le sujet du corps. Les paragraphes supplémentaires sont également séparés par des lignes vides.
```

```
Expliquez le problème résolu par ce commit. Plus important encore, expliquez pourquoi ces changements sont apportés, plutôt que comment. La partie 'pourquoi' est de votre responsabilité, la partie 'comment' est de la responsabilité du code.
```

```
- Vous pouvez également utiliser des puces comme ceci.- Ou, comme cela.
```

De grands exemples de tels messages de commit peuvent être trouvés dans les dépôts [Linux](https://github.com/torvalds/linux) et [Git](https://github.com/git/git) sur [GitHub](https://github.com/).

Maintenant, il est compréhensible que chaque commit n'apporte pas de grands changements au dépôt. Certains commits seront pour corriger des fautes de frappe, et d'autres pour changer l'ordre des lignes ou l'indentation. Dans de tels cas, une ligne de sujet devrait suffire.

Atom est un éditeur de texte que j'utilise pour tout ! Je l'utilise pour prendre des notes en classe, compléter des travaux d'écriture en [Markdown](https://daringfireball.net/projects/markdown/) (sauf si j'ai absolument besoin des super pouvoirs de MS Word), et pour des projets de programmation au quotidien.

Je continue à ajuster Atom petit à petit chaque fois que j'apprends quelque chose de nouveau, c'est amusant de voir mes fichiers de configuration grandir lentement en taille.

Alors, commençons par définir Atom comme notre éditeur de commit par défaut pour git, et vérifions si cela a été fait correctement en utilisant les commandes suivantes dans votre terminal :

```
git config --global core.editor "atom --wait"
```

```
git config --get core.editor
```

```
# Ce qui devrait vous donner la sortie : atom --wait
```

#### Changer la couleur de la ligne de sujet selon sa longueur

Tout d'abord, nous allons configurer Atom pour qu'il change la couleur de la ligne de sujet en orange si la longueur dépasse 50 caractères et en rouge si la longueur dépasse 65 caractères. Vous pouvez en savoir plus sur les intégrations git pour Atom à [Git Integration](http://blog.atom.io/2014/03/13/git-integration.html).

Ouvrez le fichier styles.less de votre Atom, qui se trouve sous l'option de menu « Atom » :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zkgNf5LtktODM49BOgVQ2g.jpeg)

Écrivez les lignes de code suivantes dans le fichier styles.less d'Atom :

```
atom-text-editor::shadow { .git-commit.invalid.deprecated.line-too-long {  color: @text-color-warning;  text-decoration: none; }
```

```
 .git-commit.invalid.illegal.line-too-long {  color: @text-color-selected;  background: @background-color-error;  opacity: 0.9; }}
```

Une fois que vous avez apporté les modifications et enregistré le fichier, Atom se comportera comme montré dans la Figure 2.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LrrcnjYYKGNePP0T-79uCQ.gif)
_Figure 2. Comportement de la ligne de sujet du message de commit dans Atom._

#### Écrire un extrait pour la structure du message de commit

Deuxièmement, nous allons écrire un court extrait pour les messages de commit. Cet extrait fournira des espaces réservés pour la ligne de sujet et le corps qui peuvent être navigués en utilisant la touche TAB.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U8y5zf56tzuPQx0kTn3L2Q.jpeg)

Écrivez les lignes de code suivantes dans le fichier snippets.cson d'Atom :

```
'.text.git-commit':  'commit-message':    'prefix': 'comm'    'body': """      ${1:Subject < 50 chars}
```

```
      ${2:Body in detail}    """
```

Après avoir apporté les modifications et enregistré le fichier des extraits, la prochaine fois que vous ouvrirez votre message de commit, vous n'aurez qu'à taper **comm** et appuyer sur TAB pour développer votre extrait.

Une fois l'extrait développé, vous pouvez appuyer à nouveau sur TAB pour sauter le curseur de la 'ligne de sujet' au 'corps'. La Figure 3 montre cet extrait en action.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dSJ0TgQUPX2ukRwgZi9RBQ.gif)
_Figure 3. Extrait 'comm' en action._

Ces petits extraits de code ont certainement amélioré mon flux de travail de commit git, et je suis confiant qu'ils peuvent améliorer le vôtre.

Si vous avez d'autres extraits liés aux commits que vous utilisez dans Atom, n'hésitez pas à les publier. J'adorerais y jeter un coup d'œil et peut-être les incorporer dans mon flux de travail.

Aussi — pour les curieux — voici une liste des thèmes et des packages que j'ai utilisés dans les figures ci-dessus :

* Thème UI — [Nucleus Dark](https://atom.io/themes/nucleus-dark-ui)
* Thème Syntax — [Atom Dark Fusion](https://atom.io/themes/atom-dark-fusion-syntax)
* Support d'édition Git pour Atom — [language-git](https://atom.io/packages/language-git)