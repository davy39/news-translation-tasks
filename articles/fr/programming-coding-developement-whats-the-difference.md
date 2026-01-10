---
title: Programmation VS Codage VS Développement – Quelle est la différence ?
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-07-20T20:04:12.000Z'
originalURL: https://freecodecamp.org/news/programming-coding-developement-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Programming-vs-coding.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Programmation VS Codage VS Développement – Quelle est la différence ?
seo_desc: 'In my very early days as a budding web developer, I made a fairly common
  mistake.

  On Facebook, I sent a friend request to a senior software engineer (I wasn''t aware
  of his position at the time) and started a chat with him thereafter. Done with greeti...'
---

Dans mes tout premiers jours en tant que développeur web en herbe, j'ai fait une erreur assez courante.

Sur Facebook, j'ai envoyé une demande d'ami à un ingénieur logiciel senior (je ne connaissais pas sa position à l'époque) et j'ai commencé une discussion avec lui par la suite. Après les salutations et les politesses, je lui ai curieusement demandé ceci : « Donc, tu es un codeur ? »

Cela a suscité une réponse à laquelle je ne m'attendais pas et j'ai reçu une leçon que j'étais plus que heureux de recevoir.

Beaucoup de gens font exactement la même chose – ils utilisent les termes **"programmeur"**, **"codeur"** et **"développeur"** de manière synonyme. Mais ces trois termes signifient-ils la même chose ?

Eh bien, pas tout à fait.

## Qu'est-ce que la programmation ?

La programmation est de la logique. La programmation est de la réflexion.

La programmation consiste à prendre des décisions, ou à dire à l'ordinateur quelles décisions prendre dans différentes circonstances. Une fois que vous avez cliqué sur le bouton rouge, vous pouvez programmer un ordinateur/navigateur pour accéder à des données et faire une requête réseau.

**Voici un exemple grossièrement simplifié d'un programme :**

*Si un email fourni par un utilisateur ne suit pas le format conventionnel (c'est-à-dire qu'il manque le '@' et le '.com'), afficher un message d'erreur. Sinon, prendre l'email et vérifier s'il existe déjà dans la base de données. S'il existe déjà, afficher un message personnalisé à l'utilisateur. Sinon, stocker l'email dans la base de données et afficher un message de succès.*

Ceci est une logique simple et n'a rien à voir avec le code (pour l'instant). Bien sûr, plus l'application est complexe, plus vous devez réfléchir.

La programmation utilise vos compétences en pensée critique et votre capacité à résoudre des problèmes logiques. Il s'agit de réfléchir et de créer le réseau de décisions possibles qu'un ordinateur ou un navigateur doit prendre ([également connu sous le nom d'algorithmes](https://www.freecodecamp.org/news/algorithm-definition/)).

En fait, vous pouvez faire de la programmation en anglais car cela n'a rien à voir avec une langue particulière.

Cela nous amène au deuxième terme : le codage.

## Qu'est-ce que le codage ?

Je considérerai le codage comme un sous-ensemble de la programmation. Le codage englobe les sujets et activités suivants :

* Langages de programmation

* La syntaxe d'un langage et comment elle diffère de la syntaxe d'autres langages

* Organisation du code

* Optimisation du code

* Débogage

* Écriture et exécution de tests

* Création et utilisation de bibliothèques et de frameworks

Et ainsi de suite.

> Vous pouvez être un programmeur sans être un codeur, mais vous ne pouvez pas être un codeur sans être un programmeur.

Alors qu'un programmeur doit simplement réfléchir et construire un cadre logique de décisions pour l'application, un codeur doit implémenter cette logique avec un langage de programmation particulier de manière standard et efficace.

Un codeur doit se familiariser avec la syntaxe du code et être à jour avec les nouvelles façons recommandées d'écrire du code.

Un codeur doit être bon dans les tâches techniques comme les tests, le débogage, etc.

Le code est simplement le langage qu'une machine comprend. Pour implémenter une application, vous devez prendre l'ensemble d'instructions créé par un programmeur et le rendre compréhensible par la machine. C'est l'acte de coder.

En utilisant le même exemple de validation et de stockage d'email, implémentons cette logique en code JavaScript :

```js
let database = ['test1@gmail.com', 'test2@gmail.com', 'test3@gmail.com'];

function validateEmail() {
    let regexEmail = /^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/;
    let emailAddress = document.getElementbyID('emailFld').value;
    if (!emailAddress.match(regexEmail)) {
        document.getElementbyID('myAlert').innerHTML = "Email invalide !";
    } else if (database.includes(emailAddress)) {
        document.getElementbyID('myAlert').innerHTML = "Email existe !";
      else {
        database.push(emailAddress);
        document.getElementbyID('myAlert').innerHTML = "Succès !";
        return true;
      }
}
    
document.getElementById("myBtn").addEventListener("click", validateEmail);
```

Maintenant, nous avons codé cette logique de programmation pour qu'un navigateur web l'exécute. En d'autres termes, nous avons **programmé** le moteur du navigateur pour **prendre des décisions**. Cela n'aurait pas été possible sans écrire de code.

Tous les types de code ne peuvent pas être utilisés pour coder des programmes/instructions. Un [exemple de tel code est HTML](https://www.freecodecamp.org/news/the-html-handbook/).

## Qu'est-ce que le développement logiciel ?

Alors maintenant, vous vous demandez peut-être, **qu'est-ce que le développement logiciel ?** Selon [Wikipedia](https://en.wikipedia.org/wiki/Software_development), le développement logiciel est :

> "le processus de conception, de spécification, de design, de programmation, de documentation, de test et de correction de bugs impliqués dans la création et la maintenance d'applications, de frameworks, ou d'autres composants logiciels.
> 
> Le développement logiciel est un processus d'écriture et de maintenance du code source, mais dans un sens plus large, il inclut tout ce qui est impliqué entre la conception du logiciel souhaité jusqu'à la manifestation finale du logiciel, parfois dans un processus planifié et structuré.
> 
> Par conséquent, le développement logiciel peut inclure la recherche, le nouveau développement, le prototypage, la modification, la réutilisation, la réingénierie, la maintenance, ou toute autre activité qui aboutit à des produits logiciels."

Comme vous pouvez le voir à partir de la définition extensive ci-dessus, le développement est plus grand que la simple programmation et le codage. Il s'agit de créer une solution à un problème réel en construisant une application qui résout ce problème, en maintenant cette application, en la commercialisant, en recherchant des moyens de l'optimiser, et ainsi de suite.

Le développement doit prendre en considération l'utilisateur final, DevOps (un mot-valise de « développement » et « opérations »), la gestion d'équipe, et bien d'autres choses.

Un développeur analyse tout ce qui est nécessaire pour créer une application proposée et supervise également ce processus de développement.

Un excellent exemple de développeur logiciel serait un fondateur technique de startup.

Ils conçoivent une application comme un produit logiciel qui sera un service précieux pour les gens dans la vie réelle. Ils entreprennent le processus de donner vie à cette conception, y compris la programmation et le codage réels de l'application.

Ensuite, ils supervisent la maintenance de l'application. Ils pourraient même financer des recherches pour améliorer les performances et l'efficacité du service de leur entreprise, et ainsi de suite.

Le développement est le package complet.

## Mes réflexions sur la programmation vs le codage vs le développement

Votre état d'esprit est très important. Considérez le développement logiciel comme un processus qui devrait toujours commencer par la programmation. Vous serez mieux loti en vous formant en tant que programmeur avant de devenir un codeur.

Je l'admets, certaines personnes apprennent réellement à programmer en étudiant des boucles simples et du code. C'est aussi bien. C'est pourquoi je conseille aux nouveaux venus de suivre des [cours sur les structures de données et les algorithmes](https://www.freecodecamp.org/news/data-structures-and-algorithms-in-javascript/).

Faire une distinction claire entre ces trois termes peut vous aider à apprendre le développement logiciel plus rapidement. Cela vous aidera à savoir quoi prioriser dans votre apprentissage. Et cela vous permettra de regarder l'ensemble du processus de développement logiciel sous un angle différent.

Sur une note plus légère, cela peut vous aider à éviter des situations gênantes avec des développeurs qui aiment un peu trop leurs titres. :)

Récemment, je suis tombé sur une vidéo YouTube qui distingue aptement la différence entre les trois termes. Je pense que vous pourriez en bénéficier :

%[https://www.youtube.com/watch?v=CIRGjwYgdT4]

## Conclusion

La programmation consiste à concevoir un réseau de motifs logiques qui définit le comportement de votre application.

Le codage implique la mise en œuvre de l'ensemble d'instructions sous une forme qu'une machine comprend et de manière optimale.

Le développement consiste à livrer un produit propre et à le maintenir. Le développement englobe les processus de création d'un package complet pour le plaisir et la satisfaction des utilisateurs finaux.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/programming-vs-coding-vs-deve.png align="left")

*Note de résumé rapide*

J'espère que vous avez gagné quelques connaissances grâce à cet article. Ce sujet a fait l'objet d'un énorme débat et vous pourriez être en désaccord avec moi sur certains points, ce qui est totalement normal. Je partage simplement mon opinion sur la question.

Vous pouvez consulter certains de mes autres articles sur mon blog personnel [blog](https://ubahthebuilder.tech).

Merci d'avoir lu.

> P/S : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).