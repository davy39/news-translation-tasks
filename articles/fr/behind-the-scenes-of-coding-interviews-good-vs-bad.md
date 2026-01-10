---
title: Les entretiens de codage dans les coulisses - le bon et le mauvais
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-05T16:15:22.000Z'
originalURL: https://freecodecamp.org/news/behind-the-scenes-of-coding-interviews-good-vs-bad
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca112740569d1a4ca4c7d.jpg
tags:
- name: coding
  slug: coding
- name: coding interview
  slug: coding-interview
- name: Job Interview
  slug: job-interview
seo_title: Les entretiens de codage dans les coulisses - le bon et le mauvais
seo_desc: 'By Srinivasan C

  Interviewing is a skill in and of itself. You can be the best developer in the world
  but you may still screw up an interview.

  https://twitter.com/mxcl/status/608682016205344768?ref_src=twsrc%5Etfw

  How many times have you come out of a...'
---

Par Srinivasan C

Passer un entretien est une compétence en soi. Vous pouvez être le meilleur développeur au monde, mais vous pouvez toujours rater un entretien.

%[https://twitter.com/mxcl/status/608682016205344768?ref_src=twsrc%5Etfw]

Combien de fois êtes-vous sorti d'un entretien en vous demandant : qu'ai-je fait de mal ? Pourquoi m'ont-ils rejeté ?

En tant que candidat, il est très utile de comprendre les attentes lors d'un entretien.

Dans cet article, je souhaite montrer à chaque candidat aspirant la différence entre un bon et un mauvais entretien et comment cela est perçu par l'interviewer.

Nous allons comparer et contraster deux entretiens différents et apprendre de chacun d'eux afin que vous puissiez ajuster vos actions pour répondre aux attentes.

## Premier entretien

Prenons la même question que précédemment : "Inverser un arbre binaire".

_Interviewer (I)_ : Bonjour, bienvenue dans notre entreprise. Je suis xxx et je fais yyy. Alors, parlez-moi de vous.

_Candidat (C)_ : Je suis xxx. J'ai environ 5 ans d'expérience en développement backend. J'adore résoudre des problèmes techniques...

_I_ : C'est bien. Alors, passons à la partie résolution de problèmes ?

_C_ : Bien sûr !

_I_ : Donc, vous avez un arbre binaire. Je veux que vous inversiez l'arbre binaire et que vous imprimiez l'arbre résultant.

_C_ : **(Réfléchit dans sa tête)** Hmmm, d'accord. Un arbre binaire a deux enfants. Donc, je suppose que l'inversion signifie imprimer de la feuille à la racine. Donc, le moyen le plus simple de faire cela est de parcourir l'arbre jusqu'à la fin et de trouver les feuilles...

_I_ : **(Après 5 minutes de silence complet)** Comprenez-vous la question ? Avez-vous besoin de clarifications ?

_C_ : Je suis **clair**. Maintenant, je réfléchis simplement à un moyen d'imprimer les nœuds en commençant par la feuille.

_I_ : Que voulez-vous dire par imprimer les nœuds en commençant par la feuille ?

_C_ : Donc, en gros, je devrais imprimer de la feuille à la racine, non ? Il est facile de parcourir jusqu'à la feuille. Mais la partie difficile est de revenir en arrière ?

_I_ : Hmmm. Êtes-vous sûr d'avoir bien compris la question ? Inverser un arbre signifie que vous devez **échanger les enfants gauche et droit**.

_C_ : Désolé, je ne suis pas clair. Quand vous avez dit inverser, j'ai **supposé** que vous vouliez dire imprimer de la feuille à la racine.

_I_ : Ce n'est pas grave **(C'est ici que vous avez perdu le poste)**. Maintenant que vous êtes clair, continuons.

_C_ : Oui, je suis clair. Donc maintenant, je dois échanger les nœuds gauche et droit. C'est facile, non ?
**(Écrit du code en silence)**

```ruby
def invert(node)
  t = node.left 
  node.left = node.right
  node.right = t
  return node
end

```

_C_ : J'ai terminé le code.

_I_ : Bien. Donc, qu'avez-vous fait ici ?

_C_ : J'ai inversé l'arbre en échangeant les nœuds gauche et droit. Donc, je garde une variable temporaire pour y parvenir.

_I_ : **(Essaie de guider vers une solution appropriée)** Mais cela n'échange que le nœud racine, non ?

_C_ : **(Perplexe)** Hmm oui, donc les enfants gauche et droit seront inversés. C'est la question, non ?

_I_ : **(Il n'y a toujours pas de clarté dans la question)** Donc, la question est que l'arbre complet doit être inversé. Pas seulement la racine.

_C_ : Oh, mince. Donc, ce n'est pas seulement la racine, mais l'arbre complet. Ai-je raison ?

_I_ : Oui, c'est correct.

_C_ : D'accord. Laissez-moi réfléchir.

**(Après 2 minutes)**

_C_ : Je pense que j'ai compris. Donc, en gros, je dois appliquer le même algorithme que j'ai écrit pour l'arbre entier. Ai-je raison ?

_I_ : Oui, mais comment faites-vous cela ?

_C_ : **(Commence à écrire du code)**

```ruby
def invert(node)
  n = Node.new(node.val)
  invert(node.left)
  invert(node.right)
  n.left = node.right
  n.right = node.left
  return n
end
```

Donc, je **suppose** que cela devrait fonctionner.

_I_ : Hmmm, laissez-moi voir. **(Trouve le problème. Et vous ?)** Je ne suis pas sûr que cela fonctionne. Pouvez-vous me l'expliquer ?

_C_ : Bien sûr. D'abord, j'inverse le sous-arbre gauche, puis le sous-arbre droit, et ensuite j'échange leurs positions pour que la racine soit inversée.

_I_ : Hmmm. Mais les nœuds gauche et droit retournent de nouveaux nœuds après l'échange, non ? Vous échangez toujours les anciens nœuds.

_C_ : Je ne suis pas sûr de ce que vous voulez dire par là. Je pense que cela **fonctionnera** pour tous les cas.

_I_ : Super ! Nous avons manqué de temps. Merci pour votre temps, c'était un plaisir de discuter avec vous. Le service RH vous recontactera.

## Retour d'information

Maintenant, selon vous, quelle a été la décision finale et quel a été le retour de l'interviewer ? Le retour hypothétique serait quelque chose comme ceci :

* Le candidat a fait beaucoup de suppositions et n'a pas clarifié le problème.
* Le candidat a proposé une approche sans raisonnement clair derrière celle-ci. (Vous vous souvenez du silence pendant l'entretien ?)
* Le candidat n'était pas clair avec les exigences, même lors de la phase d'implémentation.
* Le candidat a eu des difficultés avec l'implémentation et n'a pas été capable de saisir les indices menant à la solution.
* Le candidat n'a pas réussi à identifier les bugs dans le code, même après avoir eu suffisamment de temps et de questions pour vérifier si la solution était correcte.

Si cela avait été un véritable entretien, le candidat aurait été rejeté. Maintenant, comment devrait se dérouler l'entretien idéal ?

## Deuxième entretien

_Interviewer (I)_ : Bonjour, bienvenue dans notre entreprise. Je suis xxx et je fais yyy. Alors, parlez-moi de vous.

_Candidat (C)_ : Je suis xxx. J'ai environ 5 ans d'expérience en développement backend. J'adore résoudre des problèmes techniques...

_I_ : C'est bien. Alors, passons à la partie résolution de problèmes ?

_C_ : Bien sûr !

_I_ : Donc, vous avez un arbre binaire. Je veux que vous inversiez l'arbre binaire et que vous imprimiez l'arbre résultant.

_C_ : **(Réfléchit à voix haute)** Bien. Donc, un arbre binaire a deux nœuds. Donc, qu'est-ce que l'inversion exactement ? Est-ce échanger la gauche et la droite ?

_I_ : Exactement. Donc, le nœud gauche devrait être à droite et vice versa.

_C_ : D'accord. Donc, dans ce cas, que se passe-t-il ?

_**Fournit un exemple et clarifie l'entrée et la sortie**_

_I_ : Vous avez raison dans une certaine mesure. Mais cela devrait se produire pour l'arbre entier, pas seulement pour la racine. **(Remarquez comment les exigences ont été solidifiées tôt)**

_C_ : Oh, compris ! Donc, je pense que je dois le faire de manière récursive. C'est difficile ! Laissez-moi voir. Mais avant cela, je vais simplement vérifier ma compréhension en passant par un autre exemple.
_ Fournit un autre exemple pour clarifier les éléments manquants _

_I_ : Oui, vous avez raison. C'est la sortie. Je pense que vous avez complètement compris le problème. Donc, comment allez-vous l'aborder ?

_C_ : Laissez-moi voir. Donc, pour échanger la gauche et la droite, je peux simplement utiliser une variable temporaire. Mais ensuite, comment vais-je le faire pour le reste ? Oh oui, je pourrais simplement récurser pour les autres et faire la même chose.

_I_ : Bien. Y a-t-il un problème avec cette approche ?

_C_ : Hmmm. Oui, si j'échange simplement la gauche et la droite de manière récursive, comment vais-je suivre l'ancien et le nouvel arbre ?

_I_ : Je ne suis pas sûr de vous suivre. Qu'est-ce que l'ancien et le nouveau ?

_C_ : Ce que je voulais dire, c'est qu'il y aura des enfants mis à jour, je dois les échanger et non les anciens enfants.

_I_ : Oui, correct.

_C_ : Oui, je peux simplement appeler cette fonction de manière récursive pour la gauche et la droite et stocker ces valeurs dans une variable. Je pourrais alors mettre à jour l'arbre avec ces variables. De cette façon, je peux m'assurer que l'arbre entier est inversé.

_I_ : Bien. Autre chose que vous avez manqué ?

_C_ : Non, je pense. Donc, cela prendra un temps O(n) et un espace O(1) car je n'utilise pas d'espace supplémentaire. **(Remarquez comment le candidat discute proactivement du temps et de l'espace)**

_I_ : Je suis d'accord. Vous pouvez commencer à coder.

_C_ : Bien sûr. **(Parle à travers le code pendant le codage)**

```ruby
def invert(node)
  invert(node.left)
  invert(node.right)
  node.left,node.right = node.right, node.left
  return node
end

```

_C_ : Donc, j'ai terminé. Laissez-moi vous expliquer mon code. Donc, pour un arbre comme ... **(Explique et exécute à sec avec un exemple)**

_I_ : Je pense que vous avez raison. Cela fonctionne-t-il pour tous les cas ?

_C_ : Hmmm. Je pense que je vais obtenir une exception de pointeur null pour un arbre vide. Laissez-moi corriger cela en ajoutant une vérification de null.

_I_ : Maintenant, cela semble bon. Autre chose que vous avez manqué.

_C_ : Non, je pense que j'ai couvert les autres cas comme pas de feuilles, une feuille, etc. **(Remarquez comment il mentionne chaque cas qu'il a considéré)**

_I_ : Bien. Je suis satisfait. Des questions ? :)

## Retour d'information

Alors, que pensez-vous de cet entretien ?

* Le candidat a clarifié les exigences avant de commencer l'implémentation.
* Le candidat a également figé les exigences en passant par quelques exemples et en clarifiant sa compréhension.
* Le candidat a proposé une solution fonctionnelle sans aucune incitation.
* Le candidat a discuté proactivement des complexités de temps et d'espace.
* Pendant le codage, le candidat avait une vision claire de ce qu'il faisait et où il allait.
* Le candidat avait un bug dans son code, et lorsqu'on lui a demandé de vérifier les erreurs, il a trouvé l'erreur et l'a corrigée lui-même.

## Conclusion

Passer un entretien est une compétence complètement différente du codage. Même si vous êtes bon en résolution de problèmes, l'entretien est un cadre où l'interviewer essaie de décider s'il doit vous embaucher ou non. Donc, en plus du codage, vous devez également comprendre la perspective de l'interviewer afin de lui faciliter la tâche pour vous embaucher. Dans cet article, je voulais comparer et contraster un bon entretien avec un entretien médiocre. Essayez de pratiquer les compétences d'entretien séparément, car plus vous pratiquez, meilleur vous devenez. Vous pouvez [me contacter](https://kaizencoder.com/about) si vous avez besoin d'aide pour passer des entretiens simulés.

Cet article a été publié pour la première fois sur [http://kaizencoder.com](http://kaizencoder.com/). Si vous avez aimé cet article, veuillez [visiter](http://kaizencoder.com) pour en lire d'autres comme celui-ci ou en apprendre plus sur moi !