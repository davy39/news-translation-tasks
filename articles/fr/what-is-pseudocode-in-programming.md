---
title: Qu'est-ce que le pseudocode ? Comment utiliser le pseudocode pour résoudre
  des problèmes de codage
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-07-26T19:23:37.000Z'
originalURL: https://freecodecamp.org/news/what-is-pseudocode-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Pseudocode.png
tags:
- name: Problem Solving
  slug: problem-solving
- name: General Programming
  slug: programming
seo_title: Qu'est-ce que le pseudocode ? Comment utiliser le pseudocode pour résoudre
  des problèmes de codage
seo_desc: 'You might be wondering what pseudocode is and why it''s so useful for writing
  computer programs.

  But before we jump into pseudocode, let''s refresh our memories about what programming
  and coding are, in the simplest sense.

  Programming is the manifestat...'
---

Vous vous demandez peut-être ce qu'est le pseudocode et pourquoi il est si utile pour écrire des programmes informatiques.

Mais avant de plonger dans le pseudocode, rafraîchissons notre mémoire sur ce que sont la programmation et le codage, dans le sens le plus simple.

La programmation est la manifestation de la logique. Un programme est un ensemble d'instructions qui définit le comportement de votre application logicielle. Écrire du code est la manière dont vous l'implémentez pour la machine.

## Qu'est-ce que le pseudocode ?

Le pseudocode signifie littéralement « faux code ». C'est une manière **informelle** et **artificielle** d'écrire des programmes dans laquelle vous représentez la séquence d'actions et d'instructions (aka algorithmes) sous une forme que les humains peuvent facilement comprendre.

Vous voyez, les ordinateurs et les êtres humains sont assez différents, et c'est là que réside le problème.

Le langage d'un ordinateur est très rigide : vous n'êtes pas autorisé à faire des erreurs ou à vous écarter des règles. Même avec l'invention de langages de haut niveau, lisibles par les humains comme JavaScript et Python, il est encore assez difficile pour un développeur humain moyen de raisonner et de programmer dans ces langages de codage.

Avec le pseudocode, cependant, c'est exactement l'inverse. Vous établissez les règles. Peu importe le langage que vous utilisez pour écrire votre pseudocode. Tout ce qui compte, c'est la compréhension.

Dans le pseudocode, vous n'avez pas à penser aux points-virgules, aux accolades, à la syntaxe des fonctions fléchées, à la manière de définir les promesses, aux méthodes DOM et autres principes fondamentaux du langage. Vous devez simplement être capable d'expliquer ce que vous pensez et faites.

## Avantages de l'écriture de pseudocode

Lorsque vous écrivez du code dans un langage de programmation, vous devrez lutter contre une syntaxe stricte et des modèles de codage rigides. Mais vous écrivez du pseudocode dans un langage ou une forme avec laquelle vous êtes très familier.

Puisque le pseudocode est une méthode informelle de conception de programmes, vous n'avez pas à obéir à des règles établies. **Vous établissez les règles vous-même.**

Le pseudocode sert de pont entre votre cerveau et l'exécuteur de code de l'ordinateur. Il vous permet de planifier des instructions qui suivent un modèle logique, sans inclure tous les détails techniques.

Le pseudocode est un excellent moyen de commencer la programmation logicielle en tant que débutant. Vous n'aurez pas à submerger votre cerveau avec la syntaxe de codage.

En fait, de nombreuses entreprises organisent des tests de programmation pour leurs intervieweurs en pseudocode. Cela est dû au fait que l'importance de la résolution de problèmes dépasse la capacité à « pirater » le code informatique.

Vous pouvez obtenir du code de qualité sur de nombreuses plateformes en ligne, mais vous devez apprendre la résolution de problèmes et la pratiquer beaucoup.

La planification d'algorithmes informatiques avec du pseudocode vous rend méticuleux. Cela vous aide à expliquer exactement ce que chaque ligne d'un programme logiciel doit faire. Cela est possible parce que vous avez le contrôle total de tout, ce qui est l'une des grandes caractéristiques du pseudocode.

## Exemple de pseudocode

Le pseudocode est une manière très intuitive de développer des programmes logiciels. Pour illustrer cela, je vais me référer à un programme très simple que j'ai écrit dans mon [dernier article](https://www.freecodecamp.org/news/programming-coding-developement-whats-the-difference/) :

Lorsque l'utilisateur remplit un formulaire et clique sur le bouton de soumission, exécuter une fonction ValidateEmail. Que doit faire la fonction ?

1. Déduire une expression régulière (regex) pour tester l'adresse e-mail de l'utilisateur.

2. Accéder à l'e-mail de l'utilisateur depuis le DOM et le stocker dans une variable. Trouver et utiliser la bonne méthode DOM pour cette tâche.

3. Maintenant que la valeur de l'e-mail est accessible et stockée, créer une instruction conditionnelle :

* Si le format de l'e-mail ne correspond pas à la règle spécifiée par la regex, accéder à l'élément avec l'attribut id `myAlert` et passer le message « Invalid Email » pour que l'utilisateur le voie.

* Sinon, si la condition ci-dessus n'est pas vraie et que le format de l'adresse e-mail correspond réellement à la regex, vérifier si la base de données contient déjà une telle adresse e-mail. Si c'est le cas, accéder à l'élément avec l'attribut id `myAlert` et passer le message « Email exists! » pour que l'utilisateur le voie.

* Maintenant, si aucune de ces conditions n'est remplie (c'est-à-dire que le format de l'e-mail correspond à la regex et que la base de données ne contient pas encore une telle adresse e-mail stockée), pousser l'adresse e-mail de l'utilisateur dans la base de données et passer le message « Successful! » pour que l'utilisateur le voie.

Une fois que vous avez terminé de décrire les différentes étapes que vous voulez que votre code suive, tout devient plus facile et plus clair. Maintenant, transformons ce pseudocode en vrai code JavaScript :

```js
let database = ['test1@gmail.com', 'test2@gmail.com', 'test3@gmail.com'];

function validateEmail() {
    let regexEmail = /^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/;
    let emailAddress = document.getElementbyID('emailFld').value;
    if (!emailAddress.match(regexEmail)) {
        document.getElementbyID('myAlert').innerHTML = "Invalid Email!";
    } else if (database.includes(emailAddress)) {
        document.getElementbyID('myAlert').innerHTML = "Email exists!";
      else {
        database.push(emailAddress);
        document.getElementbyID('myAlert').innerHTML = "Successful!";
        return true;
      }
}
    
document.getElementById("myBtn").addEventListener("click", validateEmail);
```

Tout ce que vous avez à faire à ce stade est de trouver les constructions du langage de programmation qui vous aideront à réaliser chacune de vos étapes. Avez-vous remarqué à quel point la transition du pseudocode au code réel est devenue fluide ? C'est à quel point l'écriture de pseudocode peut être efficace pour la conception de programmes.

Le pseudocode est également un excellent moyen de résoudre des problèmes liés à la programmation lorsque vous avez du mal avec eux. Pour ceux qui pratiquent la programmation sur des plateformes de défis de codage comme [CodeWars](https://www.codewars.com/dashboard), le pseudocode peut être d'une aide immense.

## Comment résoudre des problèmes de programmation avec le pseudocode

Résoudre des problèmes de programmation peut être difficile. Non seulement vous devez gérer la partie logique, mais aussi la partie technique (formation du code). J'ai récemment découvert une formule brillante et efficace pour résoudre des problèmes de codage délicats.

Voici les étapes que vous pouvez suivre pour résoudre des problèmes de programmation avec le pseudocode :

### Étape 1 : Comprendre ce que fait la fonction

Tout d'abord, vous devez comprendre qu'une fonction ne fait que (facultativement) accepter des données en entrée, travailler sur les données petit à petit, et enfin retourner une sortie. Le corps de la fonction est ce qui résout réellement le problème et il le fait ligne par ligne.

### Étape 2 : Assurez-vous de bien comprendre la question

Ensuite, vous devez lire et comprendre correctement la question. C'est probablement l'étape la plus importante du processus.

Si vous ne comprenez pas correctement la question, vous ne pourrez pas travailler sur le problème et déterminer les étapes possibles à suivre. Une fois que vous avez identifié le problème principal à résoudre, vous serez prêt à le résoudre.

### Étape 3 : Décomposez le problème.

Maintenant, vous devez décomposer le problème en parties plus petites et en sous-problèmes. Chaque petit problème que vous résolvez vous rapproche de la résolution du problème principal.

Il est utile de représenter ces étapes de résolution de problèmes de la manière la plus claire et la plus facilement compréhensible possible - c'est-à-dire le pseudocode !

* Commencez à résoudre : ouvrez et utilisez des outils comme Google, Stack Overflow, MDN, et bien sûr freeCodeCamp ! :)

* Pour chaque étape du problème que vous résolvez, testez la sortie pour vous assurer que vous êtes sur la bonne voie. Continuez à résoudre ces petits problèmes jusqu'à ce que vous arriviez à la solution finale.

J'ai appris cette formule hautement efficace d'Aaron Jack et je pense que vous en bénéficierez. Regardez sa vidéo sur la façon de résoudre des problèmes de codage :

%[https://www.youtube.com/watch?v=Dblfmk3ATeg&t=526s]

## Conclusion

Comme vous pouvez le voir, le pseudocode est une stratégie très utile pour planifier des programmes informatiques.

Bien sûr, vous devez vous rappeler que le pseudocode n'est **pas une vraie représentation** d'un programme informatique. Bien que l'utilisation du pseudocode pour planifier votre algorithme soit excellente, vous devrez finalement le traduire en un programme réel lisible par ordinateur. Cela signifie que vous devrez éventuellement apprendre à programmer dans un vrai langage de programmation.

Relever des défis de codage en ligne est un excellent moyen d'apprendre à programmer car, comme on dit, la pratique rend parfait. Mais lorsque vous essayez votre prochain défi, n'oubliez pas d'implémenter le pseudocode dans le processus !

Vous pouvez consulter certains de mes autres articles liés à la programmation sur mon blog personnel [blog](https://ubahthebuilder.tech/). Je suis également disponible sur [Twitter](https://twitter.com/ubahthebuilder).

Merci d'avoir lu et à bientôt.

> P/S : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).