---
title: Comment les entreprises utilisent le filtrage collaboratif pour savoir exactement
  ce que vous voulez
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T17:31:49.000Z'
originalURL: https://freecodecamp.org/news/how-companies-use-collaborative-filtering-to-learn-exactly-what-you-want-a3fc58e22ad9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AtkN2_Kcob5Gw_IAUA0kGA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment les entreprises utilisent le filtrage collaboratif pour savoir
  exactement ce que vous voulez
seo_desc: 'By Ajay Uppili Arasanipalai

  How do companies like Amazon and Netflix know precisely what you want? Whether it’s
  that new set of speakers that you’ve been eyeballing, or the next Black Mirror episode
  — their use of predictive algorithms has made the j...'
---

Par Ajay Uppili Arasanipalai

Comment des entreprises comme Amazon et Netflix savent-elles précisément ce que vous voulez ? Qu'il s'agisse de ce nouvel ensemble d'enceintes que vous avez repéré, ou du prochain épisode de Black Mirror — leur utilisation d'algorithmes prédictifs a rendu le travail de vous vendre des produits ridiculement efficace.

Mais aussi tentante qu'une théorie du complot puisse être, non, elles n'emploient pas de médiums.

Elles utilisent quelque chose de bien plus magique — les mathématiques. Aujourd'hui, nous allons examiner une approche appelée filtrage collaboratif.

### Qu'est-ce que le filtrage collaboratif exactement ?

Comme le mentionne [Jeremy Howard](https://www.freecodecamp.org/news/how-companies-use-collaborative-filtering-to-learn-exactly-what-you-want-a3fc58e22ad9/undefined) dans son cours de deep learning génial chez [fast.ai](http://course.fast.ai/), les modèles de deep learning structurés ne reçoivent pas beaucoup d'amour ces jours-ci.

Probablement parce que vous ne verriez pas des choses comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*5H_9SgYh3XXhVF0k.gif)
_Source : [https://cdn.vox-cdn.com/thumbor/NN7jTnph9VCkyyt2nrTFml3XbYw=/0x0:600x338/1200x800/filters:focal(252x121:348x217):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/57380619/ezgif.com_gif_maker__1_.0.gif](https://cdn.vox-cdn.com/thumbor/NN7jTnph9VCkyyt2nrTFml3XbYw=/0x0:600x338/1200x800/filters:focal(252x121:348x217):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/57380619/ezgif.com_gif_maker__1_.0.gif" rel="noopener" target="_blank" title=")_

Mais des algorithmes structurés comme le filtrage collaboratif sont ceux qui sont le plus souvent utilisés dans le monde réel. Ils sont la raison pour laquelle les articles qui apparaissent en bas de page sur Amazon semblent si tentants à acheter.

![Image](https://cdn-media-1.freecodecamp.org/images/0*a9h-fsLmOrDPK65d.png)
_Source : [https://www.highspot.com/wp-content/uploads/Amazon_Recommended_Edit.png](https://www.highspot.com/wp-content/uploads/Amazon_Recommended_Edit.png" rel="noopener" target="_blank" title=")_

Le filtrage collaboratif repose sur un principe fondamental : **vous êtes susceptible d'aimer ce qu'une personne similaire à vous aime.**

Le travail de l'algorithme est de trouver quelqu'un qui a des habitudes d'achat ou de visionnage similaires aux vôtres, et de vous suggérer ce qu'il/elle a noté hautement.

Cela peut aussi fonctionner dans l'autre sens.

L'algorithme peut recommander un produit qui est similaire à un autre produit que vous avez précédemment noté hautement. Toutes ces vérifications et comparaisons de similarité sont effectuées par une algèbre linéaire assez simple (mathématiques matricielles).

![Image](https://cdn-media-1.freecodecamp.org/images/0*GrCpb3IEGbsPT654.png)
_Source : [https://johnolamendy.files.wordpress.com/2015/10/01.png](https://johnolamendy.files.wordpress.com/2015/10/01.png" rel="noopener" target="_blank" title=")_

#### Est-ce vraiment si simple ?

Pas si vite. Avant de commencer à lancer des vecteurs et des produits scalaires, abordons un problème significatif auquel est confronté tout algorithme de système de recommandation — [le problème du démarrage à froid](https://www.yuspify.com/blog/cold-start-problem-recommender-systems/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*EsGFfoQpfpeLVDD99iIo8Q.jpeg)
_Source : [https://thermex-systems.com/wp-content/uploads/portathaw-cold-start-system-on-heavy-dump-truck.jpg](https://thermex-systems.com/wp-content/uploads/portathaw-cold-start-system-on-heavy-dump-truck.jpg" rel="noopener" target="_blank" title=")_

Vous voyez, le filtrage collaboratif fonctionne bien lorsque vous avez deux choses :

* beaucoup de données sur ce que chaque client aime (basé sur ce qu'ils ont précédemment noté hautement)
* beaucoup de données sur le public auquel chaque film ou produit pourrait s'adresser (basé sur le type de personnes qui l'ont noté hautement).

Mais qu'en est-il des nouveaux utilisateurs et des nouveaux produits, pour lesquels vous n'avez pas beaucoup d'informations ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*1cwwCKEpTlShWxvW-gkFOg.jpeg)
_Source : [https://1843magazine.static-economist.com/sites/default/files/styles/article-main-image-overlay/public/0312ILIN03-web.jpg](https://1843magazine.static-economist.com/sites/default/files/styles/article-main-image-overlay/public/0312ILIN03-web.jpg" rel="noopener" target="_blank" title=")_

Le filtrage collaboratif ne fonctionne pas bien dans ces scénarios, donc vous devrez peut-être essayer autre chose. Certaines solutions courantes impliquent l'analyse des métadonnées ou faire passer de nouveaux utilisateurs par quelques questions pour apprendre leurs préférences initiales.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tkL_S_n7qBeHwN0dzoI8Uw.png)
_Source : [http://img.techiesparks.com/2015/07/apple-music-artists.png](http://img.techiesparks.com/2015/07/apple-music-artists.png" rel="noopener" target="_blank" title=")_

### Bon, passons maintenant aux choses intéressantes

Comme pour la plupart des problèmes de machine learning, il est probablement bon de commencer par examiner les données. À partir de maintenant, je vais utiliser l'exemple des films et des notes (principalement inspiré par le jeu de données [movielens](https://grouplens.org/datasets/movielens/) utilisé dans le cours fast.ai).

Nous allons le visualiser en construisant un tableau des utilisateurs par rapport aux notes qu'ils ont données aux films.

Chaque ligne représente un utilisateur, et chaque colonne un film.

Le croisement vous indiquera quelle note un utilisateur a attribuée à un film (sur une échelle de 1 à 5, où 0 signifie « n'a pas regardé »).

Nous considérerons notre modèle de filtrage collaboratif comme un succès s'il est capable de remplir les zéros. Cela signifierait qu'il est capable de prédire comment chaque utilisateur noterait un film, en fonction à la fois de ce que l'utilisateur est et de ce que le film est.

Maintenant, pour l'algorithme. Nous allons configurer 2 matrices : une pour les utilisateurs et une autre pour les films. Celles-ci sont appelées [matrices d'embedding](https://medium.com/@Petuum/embeddings-a-matrix-of-meaning-4de877c9aa27). Appelons-les **W_u** (pour les utilisateurs) et **W_m** (pour les films).

Chaque matrice sera remplie de vecteurs de dimension _e_ (basiquement des tableaux de taille _e_). Qu'est-ce que _e_, demandez-vous ? C'est un nombre magique que j'aborderai plus tard. Pour l'instant, laissez simplement _e_ être votre nombre naturel préféré.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MlTozbCaTJImOmgWsw4YBg.png)

Remarquez que le tableau ci-dessus, si vous retirez les en-têtes de lignes et de colonnes, ressemble également à une matrice. Ce n'est pas une coïncidence. Si vous êtes familier avec la multiplication de matrices, vous savez qu'une matrice _2*3_ multipliée par une matrice _3*2_ donne une matrice _2*2_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UdE2uuKF0zlZQcZSbx0JYA.png)

Si vous voulez en savoir plus sur la multiplication de matrices, vous devriez consulter [cette playlist sur Khan Academy](https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro).

En utilisant la même logique, nous pouvons multiplier nos matrices de films et d'utilisateurs. Les dimensions fonctionneront exactement pour donner une matrice de la taille du jeu de données du tableau original (bien, techniquement, vous devez transposer l'une d'entre elles, mais je saute les détails d'implémentation).

Si nous pouvons apprendre les valeurs des entrées dans notre matrice de films et notre matrice d'utilisateurs, nous pourrions, en théorie, retrouver notre tableau original en multipliant les deux.

Nous avons notre vérité de terrain : le tableau original. Tout ce que nous avons à faire est de déterminer les nombres (également connus sous le nom de poids) qui se multiplient d'une certaine manière pour nous redonner le tableau original.

Entrez l'art mystique du machine learning.

Voici comment nous allons procéder :

* Nous commençons avec des nombres complètement aléatoires dans la matrice de films et la matrice d'utilisateurs.
* Ensuite, nous multiplions les deux pour obtenir une autre matrice (qui, à ce stade, est également complètement aléatoire) qui ressemble à notre tableau original.
* En comparant nos valeurs prédites avec les valeurs réelles du tableau, nous définissons une fonction de perte. Il s'agit essentiellement d'une mesure de l'écart entre notre note prédite et la note réelle.

Notez que nous devons également ignorer les zéros, car nous ne voulons pas que notre modèle prédise une note de 0 pour qui que ce soit. Cela serait assez inutile.

Si vous voulez plus d'informations sur les fonctions de perte, je recommande la [vidéo](https://www.youtube.com/watch?v=IVVVjBSk9N0) de [Siraj Raval](https://www.freecodecamp.org/news/how-companies-use-collaborative-filtering-to-learn-exactly-what-you-want-a3fc58e22ad9/undefined).

Après avoir trouvé les pertes, nous utilisons la [rétropropagation](http://colah.github.io/posts/2015-08-Backprop/) et la [descente de gradient](https://www.youtube.com/watch?v=IHZwWFHWa-w&index=2&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) pour optimiser les deux matrices afin d'obtenir les bonnes valeurs.

BOOM ! C'est fait !

Bon, un rapide récapitulatif :

* Nous avons un tableau avec les notes que chaque utilisateur a données à chaque film. Si un utilisateur n'a pas regardé le film, le tableau indique '0'. Nous voulons prédire les zéros.
* Pour ce faire, nous avons construit deux matrices, une pour les utilisateurs et une pour les films. Chaque matrice est essentiellement une pile de vecteurs de dimension _e_.
* Pour prédire les notes, nous multiplions les matrices ensemble pour obtenir une autre matrice de la même forme que le tableau avec nos prédictions. Initialement, le tableau ne contient que des données aléatoires.
* Mais après avoir utilisé des fonctions de perte pour trouver nos erreurs, et employé le duo dynamique de la rétropropagation et de la descente de gradient, nous avons maintenant un modèle qui peut prédire avec précision la note qu'un utilisateur donnerait à un film. Super.

### **D'accord… mais pourquoi ça marche ?**

Maintenant, si vous êtes comme moi, vous comprenez. Mais vous ne comprenez pas vraiment. Comment ces multiplications aléatoires lisent-elles les esprits ? Pourquoi ne pouvons-nous pas simplement rétropropager le tableau original et remplir les zéros ? Pourquoi passer par le schéma élaboré de créer deux matrices séparées et ensuite reconstruire le tableau ? Pourquoi ? Pourquoi ? Pourquoi ? Patience, jeune grasshopper. Tout est comme la force le veut.

Vous vous souvenez quand j'ai dit que j'allais aborder le mystère du '_e_' ? Eh bien, je vais le faire maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*i5v_BryWOrdbqyQMCDKxyA.jpeg)
_Source : [https://i.imgflip.com/1lai6f.jpg](https://i.imgflip.com/1lai6f.jpg" rel="noopener" target="_blank" title=")_

Rappelez-vous que les matrices que nous avons construites étaient essentiellement des piles de vecteurs. Un vecteur par utilisateur, et un vecteur par film. Ce n'était pas une décision sans signification.

Chaque vecteur est une représentation du type de personne qu'est l'utilisateur correspondant. Il condense vos goûts et vos dégoûts, vos pensées et vos sentiments, vos espoirs et vos peurs, dans un `numpy.array[]`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*njE9KJw930vaiaqq_rw97A.jpeg)

Pour mieux comprendre cela, zoomons sur un vecteur d'utilisateur particulier, en supposant que _e_=3 :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y8Y0E8kpiVvm13ooX6lF4g.png)

Ici, les trois composantes du vecteur sont `[100, 0, 50]`. Chaque composante représente une caractéristique de l'utilisateur, que la machine apprend en regardant ses notes précédentes.

Supposons (et ce n'est pas vraiment exact, c'est juste une analogie) que les trois composantes ont la signification suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lQTLgEoAnZDTOQsd7a-J4A.png)

Espérons que vous pouvez vous faire une idée de la manière dont le vecteur représente l'idée des préférences de l'utilisateur.

Ainsi, dans l'exemple ci-dessus, notre bon ami _u_ adore apparemment les films d'action, n'est pas très fan des films romantiques, et aime aussi les comédies, mais pas autant que les films d'action.

C'est ainsi que notre modèle de machine learning comprend la complexité humaine — en l'intégrant dans un espace vectoriel de dimension _e_.

Ainsi, _e_ n'est qu'un petit nombre que nous choisissons (appelé hyper-paramètre). Plus il est grand, plus nous pouvons capturer d'informations nuancées sur nos utilisateurs. Mais le rendre trop grand, et le calcul prendra trop de temps.

Mais attendez. Cela devient encore plus intéressant. Jetez un coup d'œil à un vecteur de film :

![Image](https://cdn-media-1.freecodecamp.org/images/1*96HXXvfps4RQnUOQkD4OgA.png)

Et maintenant, analysez la signification (interprétée par l'homme) des composantes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zY7B5mmHlPxfeQwDs4x-LA.png)

Notre blockbuster, _m_, semble être principalement un film romantique, avec une bonne dose de comédie saupoudrée par-dessus. Et nous savons tout cela sans même regarder le film ou lire une seule critique nous-mêmes !

En regardant quels types d'utilisateurs ont donné des notes élevées et basses aux films, l'algorithme peut maintenant construire des vecteurs qui représentent l'essence de ce qu'est un film.

Pour la grande finale, considérons comment nous pourrions utiliser cette information. Nous avons un utilisateur, _u_, et un film, _m_. Tous deux sont des vecteurs. Comment prédire la note que _u_ pourrait donner à _m_ ? Nous utilisons le [produit scalaire](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/vector-dot-product-and-vector-length).

Le produit scalaire est ce que vous obtenez lorsque vous multipliez les composantes d'un vecteur avec les composantes d'un autre, et additionnez les résultats. Le résultat est un scalaire (un nombre réel régulier, sans attache, à l'ancienne).

Ainsi, pour notre cas, le produit scalaire de u et m sera :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ioe9H9pQHENBlBEhefNmEg.png)

Un maigre 1350. Eh bien, tout est relatif. Mais nous aurions obtenu un nombre considérablement plus grand si nous n'avions pas multiplié deux des composantes par 0.

Il est assez clair que ce serait une mauvaise idée de recommander _m_ à _u_. Une terrible idée, en fait.

### Nous pouvons rendre notre modèle encore meilleur

Pour obtenir la prédiction de note réelle, nous compressons la valeur scalaire à travers une fonction sigmoïde mise à l'échelle, qui borne le résultat entre 0 et 5.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BcWCS1IWYV_afLpnLYssEw.png)
_Source : [https://www.desmos.com/calculator/c4omt4vni3](https://www.desmos.com/calculator/c4omt4vni3" rel="noopener" target="_blank" title=")_

Si vous êtes un peu préoccupé par tous les trucs flous que nous faisons, soyez assuré, l'ordinateur peut tout comprendre.

En fait, nous facilitons simplement son travail, en faisant des choses comme lui dire explicitement que toutes les notes doivent être supérieures à 0 et inférieures à 5.

Voici un autre truc — avant de compresser notre valeur scalaire (appelée activation) dans la fonction sigmoïde, nous pouvons ajouter un petit nombre appelé le biais, _b_. Il y aura deux biais, un pour chaque utilisateur et un pour chaque film.

En les empilant ensemble, nous obtenons un vecteur de biais pour tous les utilisateurs (ensemble), et un vecteur de biais pour tous les films (ensemble). Les biais tiennent compte du fait que certains films sont universellement aimés/détestés et que certains utilisateurs aiment/détestent les films en général.

Et avec cela, je vous présente l'équation qui peut contrôler votre vie (ou au moins, vos habitudes d'achat/en ligne) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oeZcbFIRKNUOwpgV2IvnWQ.png)

### Que signifie tout cela ?

Pour moi, la partie la plus folle de tout cela est que nous parlons de concepts humains. Action, romance, comédie, goûts, dégoûts. Tous sont des idées humaines. Et penser qu'ils pourraient tous être communiqués dans un objet mathématique est vraiment fascinant.

Maintenant, je sais que ce ne sont que des algorithmes clairement définis et des données humaines. Mais je pense qu'il y a encore quelque chose d'incroyable dans le fait que les multiplications de matrices peuvent enseigner aux ordinateurs qui nous sommes en tant qu'individus.

Après tout, malgré toutes les choses qui nous rendent différents — ce que nous aimons, notre apparence, avec qui nous passons du temps, où nous sommes, comment nous pensons, comment nous interagissons et comment nous ressentons — pour les machines qui déterminent ce que nous achetons, ce que nous regardons, avec qui nous parlons, ce que nous faisons, où nous passons notre temps et où nous ne le passons pas, nous sommes tous des éléments du même espace vectoriel linéaire.

Il y a de la beauté là-dedans.