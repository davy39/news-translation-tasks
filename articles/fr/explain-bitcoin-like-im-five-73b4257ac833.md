---
title: Expliquer Bitcoin comme si j'avais cinq ans
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2013-12-12T18:04:05.000Z'
originalURL: https://freecodecamp.org/news/explain-bitcoin-like-im-five-73b4257ac833
coverImage: https://cdn-media-1.freecodecamp.org/images/1*d3ASVo4LX_QKtOXaeCdWmg.jpeg
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: Ethereum
  slug: ethereum
- name: technology
  slug: technology
seo_title: Expliquer Bitcoin comme si j'avais cinq ans
seo_desc: 'By Nik Custodio

  If you still can’t figure out what the heck a bitcoin is…


  We’re sitting on a park bench. It’s a great day.

  I have one apple with me. I give it to you.

  You now have one apple and I have zero.

  That was simple, right?

  Let’s look closely...'
---

Par Nik Custodio

#### Si vous ne comprenez toujours pas ce que diantre est un bitcoin

![Image](https://cdn-media-1.freecodecamp.org/images/1*d3ASVo4LX_QKtOXaeCdWmg.jpeg)

Nous sommes assis sur un banc de parc. C'est une belle journee.

J'ai une pomme avec moi. Je vous la donne.

Vous avez maintenant une pomme et j'en ai zero.

C'etait simple, n'est-ce pas ?

**Regardons de plus pres ce qui s'est passe :**

Ma pomme a ete physiquement mise dans votre main.

Vous savez que c'est arrive. J'etais la. Vous etiez la. Vous l'avez touchee.

Nous n'avions pas besoin d'une _troisieme personne_ pour nous aider a effectuer le transfert. Nous n'avions pas besoin de faire appel a l'oncle Tommy (qui est un juge celebre) pour s'asseoir avec nous sur le banc et confirmer que la pomme est passee de moi a vous.

La pomme est a vous ! Je _ne peux pas_ vous donner une autre pomme car je n'en ai plus. Je ne peux plus la controler. La pomme a completement quitte ma possession. Vous avez maintenant un control total sur cette pomme. Vous pouvez la donner a votre ami si vous le souhaitez, et ensuite cet ami peut la donner a son ami. Et ainsi de suite.

Donc, c'est ce a quoi ressemble un echange en personne. Je suppose que c'est vraiment la meme chose, que je vous donne une banane, un livre, ou disons un quart de dollar, ou un _billet de dollar_...

Mais je m'emporte.

### Retour aux pommes !

![Image](https://cdn-media-1.freecodecamp.org/images/1*XfYdSLPWgOrBAX9d6GhJDw.jpeg)

Maintenant, disons que j'ai une pomme _numerique_. En voici une, je vous donne ma pomme _numerique_.

Ah ! Maintenant, ca devient interessant.

Comment savez-vous que _cette_ pomme numerique qui m'appartenait autrefois, est maintenant a vous, et seulement a vous ? Pensez-y un instant.

C'est plus complique, n'est-ce pas ? Comment savez-vous que je n'ai pas d'abord envoye cette pomme a l'oncle Tommy en piece jointe par email ? Ou a votre ami Joe ? Ou a ma copine Lisa aussi ?

Peut-etre ai-je fait quelques copies de cette pomme numerique sur mon ordinateur. Peut-etre l'ai-je mise sur internet et un million de personnes l'ont telechargee.

Comme vous pouvez le voir, cet echange numerique pose un peu de problemes. **Envoyer des pommes _numeriques_ ne ressemble pas a envoyer des pommes _physiques_.**

Certains informaticiens brillants ont d'ailleurs un nom pour ce probleme : c'est ce qu'on appelle le [**probleme de la double depense**](http://blogs.cornell.edu/info4220/2013/03/29/bitcoin-and-the-double-spending-problem/). Mais ne vous en faites pas. Tout ce que vous devez savoir, c'est que cela les a confondus pendant un certain temps et qu'ils ne l'ont jamais resolu.

Jusqu'a maintenant.

Mais essayons de trouver une solution par nous-memes.

### Les registres

![Image](https://cdn-media-1.freecodecamp.org/images/1*QwB9iJE4R7ndvA7kHt3Tbw.jpeg)

Peut-etre que ces pommes numeriques doivent etre suivies dans un **registre**. Il s'agit essentiellement d'un livre ou l'on suit toutes les transactions - un livre de comptabilite.

Ce registre, etant numerique, doit vivre dans son propre monde et avoir quelqu'un a sa tete.

Disons, comme World of Warcraft. _Blizzard_, les gars qui ont cree le jeu en ligne, ont un "registre numerique" de toutes les epees de feu flamboyantes rares qui existent dans leur systeme. Donc, super, quelqu'un comme eux pourrait garder une trace de nos pommes numeriques. Super - nous l'avons resolu !

### Problemes

Il y a un petit probleme, cependant :

1) Que se passe-t-il si un type chez _Blizzard_ en a cree plus ? Il pourrait simplement ajouter quelques pommes numeriques a son solde chaque fois qu'il le souhaite !

2) Ce n'est pas exactement comme lorsque nous etions sur le banc ce jour-la. Il n'y avait que vous et moi alors. Passer par _Blizzard_, c'est comme faire appel a l'oncle Tommy (_une tierce partie_) hors de cour (ai-je mentionne qu'il est un juge celebre ?) pour toutes nos transactions sur le banc du parc. Comment puis-je simplement vous donner ma pomme numerique, comme, vous savez la maniere habituelle ?

> Y a-t-il un moyen de reproduire de pres notre transaction sur le banc du parc, juste entre vous et moi, **numeriquement** ? Cela semble assez difficile

### La Solution

![Image](https://cdn-media-1.freecodecamp.org/images/1*4JGxA3T6jKlzzCnTB3N-Dw.gif)

Et si nous donnions ce registre  a **tout le monde** ? Au lieu que le registre vive sur un ordinateur Blizzard, il vivra sur les ordinateurs de tout le monde. Toutes les transactions qui ont jamais eu lieu, depuis toujours, en pommes numeriques seront enregistrees dans celui-ci.

Vous ne pouvez pas le tricher. Je ne peux pas vous envoyer des pommes numeriques que je n'ai pas, car alors cela ne _synchroniserait pas_ avec tout le monde dans le systeme. Ce serait un systeme difficile a battre. Surtout s'il devenait vraiment grand.

De plus, il n'est pas controle par _une seule personne_, donc je sais qu'il n'y a personne qui puisse decide de se donner plus de pommes numeriques. Les regles du systeme ont ete _definies au depart_. Et le code et les regles sont [open-source](http://en.wikipedia.org/wiki/Open_source). Il est la pour que les personnes intelligentes puissent y contribuer, le maintenir, le securiser, l'ameliorer et le verifier.

Vous pourriez egalement participer a ce reseau et mettre a jour le registre et vous assurer que tout est correct. Pour la peine, vous pourriez obtenir comme [25 pommes numeriques](https://www.weusecoins.com/en/mining-guide) en recompense. En fait, c'est la seule facon de creer plus de pommes numeriques dans le systeme.

### J'ai simplifie pas mal

mais ce systeme que j'ai explique existe. Il s'appelle le _protocole Bitcoin_. Et ces pommes numeriques sont les _"bitcoins"_ au sein du systeme. Fancy !

Alors, avez-vous vu ce qui s'est passe ? **Qu'est-ce que le registre public permet ?**

1) Il est open source, n'est-ce pas ? Le nombre total de pommes a ete defini dans le registre public au depart. Je connais la quantite exacte qui existe. **_Dans le systeme,_ je sais qu'elles sont limitees (_rares_).**

2) Lorsque j'effectue un echange, je sais maintenant que cette pomme _numerique_ a certifiement **quitte ma possession et est maintenant completement a vous**. **Je ne pouvais pas dire cela des choses numeriques auparavant.** Elle sera mise a jour et verifiee par le registre public.

3) Parce que c'est un registre public, **je n'ai pas eu besoin de l'oncle Tommy (tierce partie) pour m'assurer que je ne trichais pas, ou que je ne faisais pas de copies supplementaires pour moi-meme, ou que je n'envoyais pas des pommes deux fois, ou trois fois**

> _Dans le systeme, l'echange d'une pomme_ numerique _est maintenant comme l'echange d'une pomme_ physique. _C'est maintenant aussi bon que de voir une pomme_ physique _quitter ma main et tomber dans votre poche. Et comme sur le banc du parc, l'echange n'a implique que_ deux personnes. _Vous_ et _moi_  nous n'avions pas besoin de l'oncle Tommy pour le rendre valide._

En d'autres termes, cela _se comporte_ comme un objet physique.

Mais vous savez ce qui est cool ? C'est toujours numerique. Nous pouvons maintenant traiter _1 000 pommes_, ou 1 _million de pommes_, ou meme _.0000001 pomme_. Je peux l'envoyer d'un clic de bouton, et je peux toujours la deposer dans votre poche _numerique_ si j'etais au Nicaragua et que vous etiez de l'autre cote a New York.

Je peux meme faire _monter d'autres choses numeriques_ sur ces pommes numeriques ! C'est numerique apres tout. Peut-etre puis-je y attacher du texte  une note numerique. Ou peut-etre puis-je y attacher des choses plus importantes ; comme un contrat, un certificat d'actions, une carte d'identite

Donc, c'est super ! Comment devons-nous traiter ou valoriser ces "pommes numeriques" ? Elles sont assez utiles, n'est-ce pas ?

Eh bien, beaucoup de gens en debattent maintenant. Il y a un debat entre telle et telle ecole economique. Entre les politiciens. Entre les programmeurs. Ne les ecoutez pas tous, cependant. Certaines personnes sont intelligentes. D'autres sont mal informees. Certaines disent que le systeme vaut beaucoup, d'autres disent qu'il vaut en fait zero. Un type a meme mis un chiffre precise : [$1 300 par pomme](http://www.forbes.com/sites/kashmirhill/2013/12/05/bank-of-america-analysts-say-bitcoins-value-is-1300/). Certains disent que c'est _de l'or numerique_, d'autres une _monnaie_. D'autres disent qu'ils sont comme des tulipes. Certaines personnes disent que cela va changer le monde, d'autres disent que ce n'est qu'une mode.

J'ai [mon propre avis](http://nikcustodio.tumblr.com/post/150500263430/why-blockchains-an-eli21) a ce sujet.

C'est une histoire pour une autre fois, cependant. Mais mon enfant, vous en savez maintenant plus sur Bitcoin que la plupart des gens.

**_Lecture recommandee (Mise a jour 2017)_**

[_Vous ne comprenez pas Bitcoin parce que vous pensez que l'argent est reel_](https://medium.com/@mariabustillos/you-dont-understand-bitcoin-because-you-think-money-is-real-5aef45b8e952?source=linkShare-2d6f142ff3cc-1512362100) _par [Maria Bustillos](https://www.freecodecamp.org/news/explain-bitcoin-like-im-five-73b4257ac833/undefined) est une bonne lecture complementaire._

_Vous pouvez egalement lire plus sur [Ethereum et les Smart Contracts ici](https://medium.freecodecamp.org/smart-contracts-for-dummies-a1ba1e0b9575?source=linkShare-2d6f142ff3cc-1512086124). Amusez-vous !_

![Image](https://cdn-media-1.freecodecamp.org/images/1*2UQq8CuqaNOdfiL_kwue5g.png)