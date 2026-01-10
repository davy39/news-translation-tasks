---
title: Comment résoudre des problèmes de codage avec une méthode simple en quatre
  étapes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-04T18:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-coding-problems
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/iStock-527234840.jpg
tags:
- name: coding challenge
  slug: coding-challenge
- name: coding interview
  slug: coding-interview
- name: Interview tips
  slug: interview-tips
- name: Problem Solving
  slug: problem-solving
seo_title: Comment résoudre des problèmes de codage avec une méthode simple en quatre
  étapes
seo_desc: "By Madison Kanna\nI had fifteen minutes left, and I knew I was going to\
  \ fail.\nI had spent two months studying for my first technical interview. \nI thought\
  \ I was prepared, but as the interview came to a close, it hit me: I had no idea\
  \ how to solve codi..."
---

Par Madison Kanna

Il me restait quinze minutes, et je savais que j'allais échouer.

J'avais passé deux mois à étudier pour mon premier entretien technique. 

Je pensais être préparée, mais alors que l'entretien touchait à sa fin, cela m'a frappée : je n'avais aucune idée de comment résoudre des problèmes de codage. 

Parmi tous les tutoriels que j'avais suivis lorsque j'apprenais à coder, aucun d'entre eux n'incluait une approche pour résoudre des problèmes de codage. 

Je devais trouver une méthode pour résoudre des problèmes—ma carrière en tant que développeur en dépendait. 

J'ai immédiatement commencé à rechercher des méthodes. Et j'en ai trouvé une. En fait, ce que j'ai découvert était une stratégie inestimable. C'était une méthode en quatre étapes, éprouvée par le temps, qui était somehow sous le radar dans l'écosystème des développeurs.

Dans cet article, je vais passer en revue cette méthode de résolution de problèmes en quatre étapes que vous pouvez utiliser pour commencer à résoudre des problèmes de codage avec confiance. 

Résoudre des problèmes de codage ne fait pas seulement partie du processus d'entretien pour un poste de développeur—c'est ce qu'un développeur fait toute la journée. Après tout, _écrire du code, c'est résoudre des problèmes_.

## Une méthode pour résoudre des problèmes

Cette méthode provient du livre _Comment le résoudre_ de George Pólya. Il est initialement paru en 1945 et s'est vendu à plus d'un million d'exemplaires. 

Sa méthode de résolution de problèmes a été utilisée et enseignée par de nombreux programmeurs, des professeurs d'informatique (voir le cours d'introduction à l'informatique d'Udacity enseigné par le professeur David Evans) aux enseignants modernes du développement web comme Colt Steele.

Parcourons la résolution d'un simple problème de codage en utilisant la méthode de résolution de problèmes en quatre étapes. Cela nous permet de voir la méthode en action tout en l'apprenant. Nous utiliserons JavaScript comme langage de choix. Voici le problème :

Créez une fonction qui additionne deux nombres et retourne cette valeur.  
  
Il y a quatre étapes dans la méthode de résolution de problèmes :

1. Comprendre le problème.
2. Élaborer un plan.
3. Exécuter le plan.
4. Revoir.

Commençons avec la première étape.

## Étape 1 : Comprendre le problème. 

Lorsqu'on vous donne un problème de codage lors d'un entretien, il est tentant de se précipiter pour coder. Cela est difficile à éviter, surtout si vous avez une limite de temps. 

Cependant, essayez de résister à cette envie. Assurez-vous de bien comprendre le problème avant de commencer à le résoudre.

Lisez attentivement le problème. Si vous êtes en entretien, vous pourriez lire le problème à voix haute si cela vous aide à ralentir. 

En lisant le problème, clarifiez toute partie que vous ne comprenez pas. Si vous êtes en entretien, vous pouvez le faire en posant des questions à votre interlocuteur sur la description du problème. Si vous êtes seul, réfléchissez et/ou recherchez sur Google les parties de la question que vous ne comprenez peut-être pas.

**Cette première étape est vitale car nous ne prenons souvent pas le temps de bien comprendre le problème. Lorsque vous ne comprenez pas bien le problème, vous aurez beaucoup plus de mal à le résoudre.**

Pour vous aider à mieux comprendre le problème, posez-vous les questions suivantes :

### Quelles sont les entrées ?

Quels types d'entrées iront dans ce problème ? Dans cet exemple, les entrées sont les arguments que notre fonction prendra. 

Juste en lisant la description du problème jusqu'à présent, nous savons que les entrées seront des nombres. Mais pour être plus précis sur ce que seront les entrées, nous pouvons demander :

Les entrées seront-elles toujours juste deux nombres ? Que devrait-il se passer si notre fonction reçoit en entrée _trois_ nombres ? 

Ici, nous pourrions demander des éclaircissements à l'intervieweur, ou examiner davantage la description du problème. 

Le problème de codage pourrait avoir une note disant : « Vous ne devriez jamais vous attendre à plus de deux entrées dans la fonction. » Si c'est le cas, vous savez comment procéder. Vous pouvez être plus spécifique, car vous réaliserez probablement que vous devez poser plus de questions sur les types d'entrées que vous pourriez recevoir.

Les entrées seront-elles toujours des nombres ? Que devrait faire notre fonction si nous recevons les entrées « a » et « b » ? Clarifiez si notre fonction prendra toujours des nombres en entrée.

Optionnellement, vous pourriez écrire les entrées possibles dans un commentaire de code pour avoir une idée de leur apparence : 

`// entrées : 2, 4`

Ensuite, demandez :

### Quelles sont les sorties ?

Que retournera cette fonction ? Dans ce cas, la sortie sera un nombre qui est le résultat des deux entrées numériques. Assurez-vous de comprendre quelles seront vos sorties.

### Créer des exemples.

Une fois que vous avez saisi le problème et que vous connaissez les entrées et sorties possibles, vous pouvez commencer à travailler sur des exemples concrets.

Les exemples peuvent également être utilisés comme vérifications de cohérence pour tester votre problème éventuel. La plupart des éditeurs de défis de code avec lesquels vous travaillerez (que ce soit lors d'un entretien ou simplement en utilisant un site comme Codewars ou HackerRank) ont des exemples ou des cas de test déjà écrits pour vous. Même ainsi, écrire vos propres exemples peut vous aider à consolider votre compréhension du problème.

Commencez par un ou deux exemples simples d'entrées et de sorties possibles. Revenons à notre fonction d'addition.

Appelons notre fonction « add ».

Quel est un exemple d'entrée ? Un exemple d'entrée pourrait être :

`// add(2, 3)` 

Quelle est la sortie de cela ? Pour écrire la sortie de l'exemple, nous pouvons écrire : 

`// add(2, 3) ---> 5`

Cela indique que notre fonction prendra en entrée 2 et 3 et retournera 5 comme sortie.

### Créer des exemples complexes.

En parcourant des exemples plus complexes, vous pouvez prendre le temps de rechercher des cas limites que vous pourriez devoir prendre en compte.

Par exemple, que devrions-nous faire si nos entrées sont des chaînes de caractères au lieu de nombres ? Que se passe-t-il si nous avons en entrée deux chaînes de caractères, par exemple, add('a', 'b') ?

Votre interlocuteur pourrait éventuellement vous dire de retourner un message d'erreur s'il y a des entrées qui ne sont pas des nombres. Si c'est le cas, vous pouvez ajouter un commentaire de code pour gérer ce cas si cela vous aide à vous souvenir que vous devez le faire.

```javascript
// retourner une erreur si les entrées ne sont pas des nombres.
```

Votre interlocuteur pourrait également vous dire de supposer que vos entrées seront toujours des nombres, auquel cas vous n'avez pas besoin d'écrire de code supplémentaire pour gérer ce cas particulier d'entrée limite.

Si vous n'avez pas d'interlocuteur et que vous résolvez simplement ce problème, le problème pourrait indiquer ce qui se passe lorsque vous entrez des entrées invalides. 

Par exemple, certains problèmes diront : « Si il n'y a pas d'entrées, retourner undefined. » Pour des cas comme celui-ci, vous pouvez optionnellement écrire un commentaire.

`// vérifier s'il n'y a pas d'entrées.`

`// Si pas d'entrées, retourner undefined.`

Pour nos besoins, nous supposerons que nos entrées seront toujours des nombres. Mais en général, il est bon de penser aux cas limites. 

Le professeur d'informatique Evans dit d'écrire ce que les développeurs appellent du code _défensif_. Pensez à ce qui pourrait mal tourner et à la manière dont votre code pourrait se défendre contre les erreurs possibles.  

Avant de passer à l'étape 2, résumons l'étape 1, comprendre le problème : 

`-Lire attentivement le problème.`

`-Quelles sont les entrées ?`

`-Quelles sont les sorties ?`

`Créer des exemples simples, puis créer des exemples plus complexes.`

## 2. Élaborer un plan pour résoudre le problème.

Ensuite, élaborez un plan pour résoudre le problème. En élaborant un plan, écrivez-le en pseudocode. 

Le pseudocode est une description en langage clair des étapes d'un algorithme. En d'autres termes, votre pseudocode est votre plan étape par étape pour résoudre le problème.

Écrivez les étapes que vous devez suivre pour résoudre le problème. Pour un problème plus compliqué, vous auriez plus d'étapes. Pour ce problème, vous pourriez écrire :

`// Créer une variable sum.`

`Ajouter la première entrée à la deuxième entrée en utilisant l'opérateur d'addition`.

`// Stocker la valeur des deux entrées dans la variable sum.`

`// Retourner en sortie la variable sum.`  
  
Vous avez maintenant votre plan étape par étape pour résoudre le problème.  
  
Pour des problèmes plus complexes, le professeur Evans note : « Considérez systématiquement comment un humain résout le problème. » C'est-à-dire, oubliez comment votre code pourrait résoudre le problème pour un moment, et pensez à comment _vous_ le résoudriez en tant qu'humain. Cela peut vous aider à voir les étapes plus clairement.

## 3. Exécuter le plan (Résoudre le problème !)

![Main, Rubik, Cube, Puzzle, Jeu, Rubik Cube](https://cdn.pixabay.com/photo/2017/04/06/15/02/hand-2208491_960_720.jpg)

L'étape suivante dans la stratégie de résolution de problèmes est de résoudre le problème. En utilisant votre pseudocode comme guide, écrivez votre code réel. 

Le professeur Evans suggère de se concentrer sur une solution simple et mécanique. Plus votre solution est facile et simple, plus vous avez de chances de la programmer correctement.

En prenant notre pseudocode, nous pourrions maintenant écrire ceci :

```javascript
function add(a, b) {
 const sum = a + b;
 return sum;
}
```

Le professeur Evans ajoute : souvenez-vous de ne pas _optimiser prématurément_. C'est-à-dire, vous pourriez être tenté de commencer à dire : « Attendez, je fais ceci et cela va être un code inefficace ! »

D'abord, sortez simplement votre solution simple et mécanique.

Que faire si vous ne pouvez pas résoudre tout le problème ? Que faire s'il y a une partie que vous ne savez toujours pas résoudre ? 

Colt Steele donne un excellent conseil ici : Si vous ne pouvez pas résoudre une partie du problème, ignorez cette partie difficile qui vous bloque. Au lieu de cela, concentrez-vous sur tout le reste que vous pouvez commencer à écrire. 

Ignorez temporairement cette partie difficile du problème que vous ne comprenez pas tout à fait et écrivez les autres parties. Une fois cela fait, revenez à la partie plus difficile.

Cela vous permet de terminer au moins _une partie_ du problème. Et souvent, vous réaliserez comment aborder cette partie plus difficile du problème une fois que vous y reviendrez.

## Étape 4 : Revoir ce que vous avez fait.

Une fois que votre solution fonctionne, prenez le temps de réfléchir et de déterminer comment apporter des améliorations. Cela pourrait être le moment de refactoriser votre solution pour la rendre plus efficace. 

En examinant votre travail, voici quelques questions que Colt Steele suggère de vous poser pour déterminer comment vous pouvez améliorer votre solution :

* Pouvez-vous obtenir le résultat différemment ? Quelles sont les autres approches viables ?
* Pouvez-vous le comprendre d'un coup d'œil ? Est-ce que cela a du sens ?
* Pouvez-vous utiliser le résultat ou la méthode pour un autre problème ?
* Pouvez-vous améliorer les performances de votre solution ?
* Pouvez-vous penser à d'autres façons de refactoriser ?
* Comment d'autres personnes ont-elles résolu ce problème ?

Une façon dont nous pourrions refactoriser notre problème pour rendre notre code plus concis : supprimer notre variable et utiliser un retour implicite :

```javascript
function add(a, b) {
 return a + b;
}
```

Avec l'étape 4, votre problème pourrait ne jamais sembler terminé. Même les grands développeurs écrivent encore du code qu'ils regardent plus tard et veulent changer. Ce sont des questions directrices qui peuvent vous aider.

Si vous avez encore du temps lors d'un entretien, vous pouvez passer par cette étape et améliorer votre solution. Si vous codez seul, prenez le temps de passer en revue ces étapes. 

Lorsque je pratique le codage seul, je regarde presque toujours les solutions qui existent et qui sont plus élégantes ou efficaces que ce que j'ai proposé.

## Conclusion

Dans cet article, nous avons passé en revue la stratégie de résolution de problèmes en quatre étapes pour résoudre des problèmes de codage. 

Récapitulons-les ici :

* Étape 1 : **comprendre le problème.** 
* Étape 2 : **créer un plan étape par étape pour résoudre le problème**. 
* Étape 3 : **exécuter le plan** et écrire le code réel. 
* Étape 4 : **revoir** et éventuellement refactoriser votre solution si elle pourrait être meilleure.

Pratiquer cette méthode de résolution de problèmes m'a énormément aidée lors de mes entretiens techniques et dans mon travail en tant que développeur.  
  
Si vous ne vous sentez pas confiant lorsque vous devez résoudre des problèmes de codage, rappelez-vous simplement que la résolution de problèmes est une compétence que chacun peut améliorer avec le temps et la pratique.

Bonne chance !

### Si vous avez aimé cet article, rejoignez mon [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), où nous relevons des défis de codage ensemble chaque dimanche et nous soutenons mutuellement tout en apprenant de nouvelles technologies.  


### Si vous avez des commentaires ou des questions sur cet article, n'hésitez pas à me tweeter [@madisonkanna](https://twitter.com/Madisonkanna).