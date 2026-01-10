---
title: Comment construire un réseau de neurones en trois lignes de maths
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T21:55:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-neural-net-in-three-lines-of-math-a0c42f45c40e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ywTIyzbs2xJUagX16XLsQw.jpeg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
seo_title: Comment construire un réseau de neurones en trois lignes de maths
seo_desc: 'By Ajay Uppili Arasanipalai

  A code-free guide to Artificial Intelligence

  So about a year ago, I read this fantastic article by Trask.

  If you didn’t click the link, do it now.

  Did you? Ok, good.

  Now here’s the thing — The article requires you to know ...'
---

Par Ajay Uppili Arasanipalai

#### Un guide sans code pour l'Intelligence Artificielle

Il y a environ un an, j'ai lu cet [article fantastique](https://iamtrask.github.io/2015/07/12/basic-python-network/) de [Trask](https://www.freecodecamp.org/news/how-to-build-a-neural-net-in-three-lines-of-math-a0c42f45c40e/undefined).

Si vous n'avez pas cliqué sur le lien, faites-le maintenant.

Vous l'avez fait ? Bon, bien.

Voici le truc — L'article nécessite que vous connaissiez un peu de Python, ce que vous savez probablement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6VNsJJdDZ2q_pExXzcZfig.png)
_Un réseau de neurones en 11 lignes de code_

Dans le cas peu probable où vous seriez intéressé par les réseaux de neurones (si cette phrase vous semble complètement étrangère, regardez cette [playlist YouTube](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)) et que vous n'ayez pas encore appris Python, félicitations, vous êtes au bon endroit.

Mais peu importe où vous en êtes dans le vaste paysage de l'apprentissage profond, je pense que de temps en temps, il est bon de revenir aux bases et de revisiter les idées mathématiques fondamentales qui nous ont apporté Siri, Alexa et d'innombrables heures de binge-watching sur Netflix.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fDC0bpwdnQYjOlSjRjNKxA.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/11SgH7U6TmI?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">freestocks.org</a> sur <a href="https://unsplash.com/search/photos/netflix?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Alors, sans plus tarder, je vous présente les trois équations qui constituent ce que j'appellerai le **théorème fondamental de l'apprentissage profond.**

### 1. Régression linéaire

![Image](https://cdn-media-1.freecodecamp.org/images/1*p14OPI_k6kpsqwW9lHFZSg.png)

La première équation est assez basique. Je suppose que les autres le sont aussi, mais nous y viendrons en temps voulu.

Pour l'instant, tout ce que nous faisons est de calculer un vecteur **_z_** (à partir de l'équation ci-dessus), où **_W_** est une matrice qui est initialement remplie d'un tas de nombres aléatoires, **_b_** est un vecteur qui est initialement remplie d'un tas de nombres aléatoires, et **_x_** est un vecteur qui n'est pas initialement rempli d'un tas de nombres aléatoires.

**_x_** est un exemple d'entraînement de notre ensemble de données. Par exemple, si vous entraînez un réseau de neurones pour prédire l'âge de quelqu'un en fonction de son genre et de sa taille, vous aurez d'abord besoin de quelques exemples (ou de préférence beaucoup, plus il y en a, mieux c'est) de données sous la forme `[[taille, genre], âge]`. Le vecteur `[taille, genre]` est ce que nous appelons **_x._**

### 2. Fonctions d'activation

![Image](https://cdn-media-1.freecodecamp.org/images/1*WEimhu4k7w-53sqwkaQU0Q.png)

Du côté gauche, nous avons nos valeurs prédites de **_y_**, qui est la variable que j'utilise pour désigner les étiquettes de nos données.

Le chapeau sur le dessus signifie que cette valeur de **_y_** est une valeur prédite, par opposition aux étiquettes de vérité terrain de notre ensemble de données.

Le **_z_** dans cette équation est le même que celui que nous avons calculé ci-dessus. Le sigma représente la fonction d'activation sigmoïde, qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3uWAr0YlfWPvojVtj0gyXA.png)

Donc, en anglais simple, nous prenons **_z_**, un vecteur de nombres réels qui peut être arbitrairement grand ou petit, et nous écrasons ses composantes pour qu'elles soient comprises entre 0 et 1.

Avoir un nombre entre 0 et 1 est utile car si nous essayons de construire un classificateur, disons qui prédit si une image est un chat ou un chien, nous pouvons laisser 1 représenter les chiens, et nous pouvons laisser 0 représenter les chats. Ou l'inverse si vous préférez les chats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m6kFnJ4brAKfUKINkE8_1Q.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/tzzpfLiRPlA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Erik-Jan Leusink</a> sur <a href="https://unsplash.com/search/photos/cat?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Mais supposons que nous ne faisons pas de chiens et de chats (oui, comme s'il y avait une meilleure utilisation pour l'apprentissage automatique). Revenons à notre prédicteur d'âge. Là-bas, nous ne pouvons pas simplement prédire des 1 et des 0.

En général, vous pourriez utiliser n'importe quelle fonction que vous aimez, pas nécessairement une sigmoïde. Mais un tas de gens intelligents ont remarqué que la sigmoïde fonctionnait plutôt bien. Donc nous sommes coincés avec elle.

Cependant, c'est une autre histoire lorsque nous traitons avec des étiquettes qui sont des nombres réels, et non des classes. Pour notre prédicteur d'âge, nous devons utiliser une fonction d'activation différente.

Entrez ReLU.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zELUGfDZ_auGRlajOM8Cnw.png)
_Source : [https://upload.wikimedia.org/wikipedia/commons/8/85/ReLU_and_Nonnegative_Soft_Thresholding_Functions.svg](https://upload.wikimedia.org/wikipedia/commons/8/85/ReLU_and_Nonnegative_Soft_Thresholding_Functions.svg" rel="noopener" target="_blank" title=")_

Permettez-moi de dire d'emblée que je pense que c'est la partie la plus ennuyeuse de l'apprentissage profond. Je veux dire, sérieusement, juste une vieille fonction droite et ennuyeuse ? Où est le plaisir là-dedans ?

Les apparences peuvent être trompeuses. Bien qu'elle soit assez terne — ReLU(**_x_**) est simplement `max(0,x)` — la fonction ReLU fonctionne vraiment bien en pratique. Donc, hé, vivez avec.

### 3. Rétropropagation et descente de gradient

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wt0LjmWqTzb5o72JBS-vhw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*WQ0yI_YpPqAEJKEQl4MJ8g.png)

D'accord, vous m'avez eu. J'ai triché. Ce sont techniquement quatre lignes de maths. Mais hé, vous pourriez condenser les étapes 1 et 2 en une seule étape, donc je suppose que je sors vainqueur.

Maintenant, pour digérer tout ce (littéral) truc grec.

Dans la première équation, nous faisons ce truc fantastique à **_y_** et **_y_**-hat pour calculer un seul nombre appelé la perte, noté par **_L_**. 

Comme on peut l'inférer par le nom, la perte mesure à quel point nous avons perdu dans notre bataille vicieuse pour conquérir le grimoire de l'apprentissage automatique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CmLBszy1cH5jFeyXQXjKSA.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/79Ut1cRYoQ0?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Karly Santiago</a> sur <a href="https://unsplash.com/search/photos/magic?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

En particulier, notre **_L_** ici mesure quelque chose appelé la perte d'entropie croisée binaire, qui est un raccourci pour sonner comme si vous aviez un doctorat en maths alors que vous mesurez simplement à quel point **_y_** est éloigné de **_y_**-hat. Néanmoins, il y a beaucoup plus sous la surface de l'équation, donc consultez l'[article](https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a) de [Daniel Godoy](https://www.freecodecamp.org/news/how-to-build-a-neural-net-in-three-lines-of-math-a0c42f45c40e/undefined) sur le sujet.

Tout ce que vous devez savoir pour comprendre l'intuition derrière tout cela est que **_L_** devient grand si nos valeurs prédites sont éloignées des valeurs de vérité terrain, et **_L_** devient minuscule lorsque nos prédictions et la réalité correspondent.

La somme est là pour que nous puissions additionner toute la confusion pour chacun des exemples d'entraînement, afin que notre réseau de neurones comprenne à quel point il est confus dans l'ensemble.

Maintenant, la partie apprentissage réelle de l'apprentissage profond commence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rka-cGjoHmoOpLLNz8ANbA.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/1MHU3zpTvro?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ben White</a> sur <a href="https://unsplash.com/search/photos/learning?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

L'étape finale dans notre pile est de mettre à jour la matrice **_W_** et le vecteur **_b_** afin que notre perte diminue. En faisant cela, nous minimisons effectivement à quel point nos prédictions sont éloignées des valeurs de vérité terrain, et ainsi, notre modèle devient plus précis.

Voici l'équation à nouveau :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WQ0yI_YpPqAEJKEQl4MJ8g.png)

**_W_** est la matrice avec des nombres mis à jour qui nous rapproche de la vérité terrain. Alpha est une constante que nous pouvons choisir. Ce dernier terme que vous regardez est le gradient de la perte par rapport à un paramètre. En termes simples, c'est une mesure de combien notre perte change pour un petit ajustement des nombres dans la matrice **_W_**. 

Encore une fois, je ne vais pas trop approfondir la descente de gradient (le processus de mise à jour de nos nombres dans la matrice) puisque il y a déjà beaucoup de grandes ressources sur le sujet. Je recommande vivement [cet article](http://ruder.io/optimizing-gradient-descent/) de [Sebastian Ruder](https://www.freecodecamp.org/news/how-to-build-a-neural-net-in-three-lines-of-math-a0c42f45c40e/undefined).

Au fait, nous pouvons faire la même chose pour les valeurs initialement aléatoires dans le vecteur **_b_**. Il suffit de les ajuster de la bonne quantité dans la bonne direction, et BOOM ! Nous venons de nous rapprocher d'une perte historiquement basse.

### Conclusion

Et voilà. Les trois grandes équations qui constituent les fondations des réseaux de neurones que nous utilisons aujourd'hui.

![Image](https://cdn-media-1.freecodecamp.org/images/1*t1pOCVMrO3DHlcYoJrGTnw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wt0LjmWqTzb5o72JBS-vhw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*WQ0yI_YpPqAEJKEQl4MJ8g.png)

Pause et réfléchissez pendant une seconde. Ce que vous venez de voir est une compilation de la compréhension de l'humanité des intrications de l'intelligence.

Bien sûr, c'est un réseau de neurones assez basique et vanille que nous venons de voir, et il y a eu d'innombrables améliorations dans les algorithmes d'apprentissage au fil des ans qui ont abouti à des percées significatives. Couplé avec l'explosion sans précédent de données et de puissance de calcul au fil des ans, il semble, dans une certaine mesure, presque inévitable que des mathématiques bien réfléchies soient capables de saisir l'art subtil de distinguer les chats et les chiens.

Mais quand même. C'est là que tout a commencé.

D'une certaine manière, le cœur et l'âme de l'avancée technologique la plus significative de cette décennie (on peut en discuter) se trouvent juste devant vos yeux. Alors prenez une seconde. Pause et réfléchissez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jnrV5dFixRqcCvkHb48_Vw.jpeg)
_Source : [https://pbs.twimg.com/media/C1hNo_KUcAAJDQ9.jpg:large](https://pbs.twimg.com/media/C1hNo_KUcAAJDQ9.jpg:large" rel="noopener" target="_blank" title=")_