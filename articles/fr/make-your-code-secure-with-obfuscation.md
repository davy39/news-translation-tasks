---
title: Qu'est-ce que l'obfuscation de code ? Comment déguiser votre code pour le rendre
  plus sécurisé
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-20T18:05:58.000Z'
originalURL: https://freecodecamp.org/news/make-your-code-secure-with-obfuscation
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/code-obfuscation-woman-coder.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Qu'est-ce que l'obfuscation de code ? Comment déguiser votre code pour
  le rendre plus sécurisé
seo_desc: "By Andrej Kovacevic\nIn the earliest days of computing, developers didn't\
  \ have to worry about networks. They could just focus on making sure their software\
  \ served its intended purpose and didn't crash too often. \nAnd the average person\
  \ who came into c..."
---

Par Andrej Kovacevic

Dans les premiers jours de l'informatique, les développeurs n'avaient pas à se soucier des réseaux. Ils pouvaient simplement se concentrer sur le fait que leur logiciel serve son but et ne plante pas trop souvent. 

Et la personne moyenne qui entrait en contact avec ce logiciel n'était pas une menace. La plupart des utilisateurs ne prendraient même pas la peine de lire les [manuels d'utilisation](https://manualsbrain.com/en/) livrés dans la boîte du logiciel, et encore moins de fouiller le code à la recherche de vulnérabilités.

Puis, Internet est arrivé et a tout changé.

Presque du jour au lendemain, les réseaux informatiques sont devenus interconnectés. Et à mesure que la complexité augmentait, les chances que quelqu'un trouve son chemin dans ces réseaux sans y appartenir ont également augmenté. 

Et plus souvent qu'autrement, ces personnes auraient les compétences nécessaires pour exploiter un code défectueux.

Et cela nous amène à aujourd'hui. C'est une époque de menaces cyber-sécuritaires sans précédent. Et les nouvelles de cyber-attaques semblent arriver quotidiennement.

En réponse, les gestionnaires de réseau déploient des systèmes défensifs de plus en plus [sophistiqués](https://www.cynet.com/xdr-security/understanding-xdr-security-concepts-features-and-use-cases/) pour renforcer leurs réseaux contre les intrus. Et ils s'attendent désormais à ce que les développeurs de logiciels fassent un effort supplémentaire pour sécuriser leur code afin de prévenir les accès non autorisés.

Et pourtant, le renforcement du code informatique n'est toujours pas beaucoup enseigné dans les écoles de codage. Mais cela devient une nécessité dans le développement d'applications modernes. 

Pour aider à remédier à cela, dans cet article, j'expliquerai ce qu'est l'obfuscation de code. Et je vous donnerai également un aperçu des six techniques d'obfuscation de code les plus cruciales utilisées aujourd'hui pour vous lancer sur la voie de l'écriture de logiciels plus sécurisés.

## Qu'est-ce que l'obfuscation de code ?

Comme son nom l'indique, l'obfuscation de code fait référence à une série de techniques de programmation conçues pour déguiser des éléments du code d'un programme. C'est le principal moyen pour les programmeurs de défendre leur travail contre l'accès ou la modification non autorisés par des pirates ou des voleurs de propriété intellectuelle. 

Et surtout, les techniques d'obfuscation de code peuvent modifier la structure et les méthodes qu'un programme utilise pour fonctionner, mais elles ne modifient jamais la sortie d'un programme.

Le problème est que de nombreuses techniques d'obfuscation de code peuvent ajouter à la surcharge d'un programme et augmenter le temps d'exécution. 

Pour cette raison, il est crucial de comprendre quelles techniques sont relativement sans pénalité et lesquelles peuvent causer des problèmes de performance. Une fois que vous connaissez les coûts, il est possible de trouver un équilibre entre protection et performance dans une application réelle.

Voici les six techniques d'obfuscation de code les plus utilisées aujourd'hui.

## 1. Supprimer les données superflues

La première technique de renforcement de code qui devrait être appliquée dans tous les cas est de se débarrasser de tout ce qui n'est pas nécessaire dans votre code.

Faire cela rationalisera votre base de code et réduira la surface d'attaque que vous défendez. 

Cela signifie supprimer les fonctions redondantes, les informations de débogage et autant de métadonnées que possible. En bref, tout ce qui pourrait donner à un attaquant une feuille de route qui pourrait le mener à une vulnérabilité.

## 2. Transformer les données

La prochaine chose à faire est de transformer les données que votre code traite pour les rendre méconnaissables. 

Des tactiques comme remplacer les valeurs par des expressions, modifier le format du stockage des données que vous utilisez, ou même [utiliser des versions binaires](https://pdf.sciencedirectassets.com/280203/1-s2.0-S1877050915X00329/1-s2.0-S1877050915032780/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCA8%2FbMNDwcr1XOpo7DeKQbXz83LMbSk24ZV4X8rpilJAIhAMsqbvQN5HTdd4zWOOXRcppnOAGYNVu6C5uAYw5uTykJKrQDCGUQAxoMMDU5MDAzNTQ2ODY1IgwV2aDE0qbSu9kgEtoqkQNrSQrQUa0Ja52RXLYbP8r9sekXFQ0TAfCAtrkTNTsiB%2FLgqZqmG%2BwY0Kz%2BJaud%2BDxrauuZZSE1dSTLcm6vNrlpabyNmPrIG%2BtY6INcm80IfLxpaTdfsTSPXXMrXykzY%2BXqDnQmfqGJ59rtulshtpTckzFN9HpY%2BrSdWWvXLklaiZdWVhz%2BxnG6jN%2F1wL%2FXwybqOBaKbmkremuUj09B1lUN32dOUe5qRnIGrf8qYyATGnbZHoMT5kz7Sq3P7F0Fy5yW7UjQVPSu2ABitFgXZVoUwRchriev6Aki6UBJ0mSxrUUHmNrXSvk5jETjuYMm8q0U3N%2B9xrYx27PPsWomPqlCOKGVlBaPoZmAmqo0BLamet3eY2Rp%2Bk0%2BPQNRqZQa8yhTDzfnRWYxJl7uLILFWe%2FjlRmILnxq%2BjmItjt6SjRaAlc7noGEv%2BNjN3AEpDC%2FcqACzJVqndzDS9V71FxSWN7klUdd4QUGLocw54pGHq1r7wuTgodPJjqnrIFmvB0iV296BFNtyj2fQjJcoeq0XlMPhDCssab9BTrqAaw64rV02aRHt4lBwTwoJJiSEDf%2Bt%2FiOQqAU%2FV%2FcX7eMhzYZKteQE52uUCMH0BO6g2L2a9MKOiRlZ6ryvpJac90eb7X9mvnvMbNcDWv3xxhfNRmlSOUDX48tLpbhKVzqncl8aZZJIPlXWKlHYOeIYLasptLMrU%2FzbqJjrOrFBqiazYHtPMI6XS1JeaUD8DmCEdGIJ9CYTLJiRyKD9dGiznGfZ%2F1L9A9zFZt%2FsDc6MybWNxTAHd3hrmvoF7zB2hNY6%2FTDdYmQv2TpAPw%2FzqbvheXrzjjIwDuQyn2mcNNz2i2U83N0uCCcbDsOvw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20201109T195727Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYXEEHGGB3%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=11d88d2c5915b160162922c34b6771ae59e987e847cb44a383faa6fcc111caa7&hash=2dbe5efcb60f98ccf53ef748c7791766189f5422149ec208f49987fac4baa432&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1877050915032780&tid=spdf-2b92f167-2272-4886-a286-4077d881be1a&sid=a173bdc61ca7a346b139b114192a80c41b85gxrqa&type=client) de vos nombres de code ajoutent tous de la complexité. Et cette complexité rendra difficile pour quiconque reverse-engineering votre code d'en tirer quelque chose d'utile.

Par exemple, vous pourriez utiliser le chiffrement de chaînes pour rendre les chaînes de texte en clair dans votre code illisibles. Le chiffrement de chaînes peut utiliser un simple encodage base64, qui transformerait ce code :

```js
String s = "Hello World";
En :
String s = new String(decryptString("SGVsbG8gV29ybGQ="));
```

Bien qu'il ne soit pas difficile pour un programmeur expérimenté de repérer ce qui se passe ici, devoir décrypter de nombreuses chaînes est chronophage et frustrant. 

Et lorsqu'il est combiné avec certaines des autres techniques d'obfuscation de code, les transformations de données sont une première ligne de défense efficace.

## 3. Utiliser l'obfuscation de l'ordre des processus

L'une des exigences difficiles de l'obfuscation de code est que vous avez toujours besoin que votre code fonctionne comme prévu une fois terminé. 

Mais il n'y a rien qui dise que vous devez exécuter votre code dans un ordre logique. Si vous mélangez l'ordre des opérations de votre code, vous pouvez toujours obtenir le bon résultat, mais rendre beaucoup plus difficile pour un tiers de comprendre ce que votre code fait. 

Le seul bémol est que vous devez faire attention à ne pas créer trop de boucles sans signification et d'impasses, car vous pourriez accidentellement ralentir le temps d'exécution de votre code.

Par exemple, regardez le snippet suivant, qui calcule la somme et la moyenne de 100 nombres :

```js
int i=1, sum=0, avg=0
while (i = 100)
{
sum+=i;
avg=sum/i;
i++;
}int i=1, sum=0, avg=0
while (i = 100)
{
sum+=i;
avg=sum/i;
i++;
}
```

En ajoutant une variable conditionnelle, il est possible de déguiser ce que fait le code. Cela est dû au fait qu'une analyse de la fonction nécessiterait de connaître ce qui est entré dedans pour commencer. 

Dans le snippet suivant, la variable conditionnelle 'random' crée une structure de code plus complexe qui la rend beaucoup plus difficile à déchiffrer :

```js
int random = 1;
while (random != 0)
{
switch (random)
{
Case 1:
{
i=0; sum=1; avg=1;
random = 2;
break;
}
case 2:
{
if (i = 100)
random = 3;
else random = 0;
break;
}
case 3:
{
sum+=i;avg=sum/i ; i++;
random = 2;
break;
}
}
}
```

## 4. Essayez l'obfuscation de débogage

Parfois, un attaquant déterminé peut apprendre toutes sortes d'informations utiles sur votre code en examinant ses informations de débogage. 

Et dans certains cas, ils pourraient trouver les clés pour dénouer certaines des autres techniques d'obfuscation que vous utilisez. 

Donc, chaque fois que possible, il est bon de supprimer l'accès aux informations de débogage. Et lorsque ce n'est pas une option, masquer toute information d'identification dans le rapport de débogage est essentiel.

## 5. Utiliser la randomisation des adresses

Depuis près de trente ans, les erreurs liées à la gestion de la mémoire sont les vulnérabilités logicielles les plus courantes exploitées par les pirates, même si chaque programmeur sait que le problème persiste. 

Et ce n'est pas seulement parmi les débutants. Environ [70% des vulnérabilités dans le navigateur web Chrome de Google](https://www.zdnet.com/article/chrome-70-of-all-security-bugs-are-memory-safety-issues/) proviennent d'erreurs de mémoire.

La réalité est qu'il est presque impossible de prévenir toutes les erreurs de programmation de mémoire, surtout si vous utilisez [des langages comme C et C++](https://neosmart.net/blog/2018/modern-c-isnt-memory-safe/). Mais ce que vous pouvez faire, c'est inclure certaines fonctionnalités de randomisation de la mémoire dans votre code qui aideront. 

À l'exécution, si les adresses virtuelles de votre code et de vos données se voient attribuer des valeurs aléatoires, il devient beaucoup plus difficile de trouver et d'exploiter les vulnérabilités non corrigées.

De plus, cela ajoute un autre avantage. Cela rend même un piratage réussi de votre code difficile, voire impossible, à reproduire. Cela seul rend beaucoup moins probable qu'un attaquant gaspille son temps à essayer de pirater votre logiciel.

## 6. Faire tourner le code obfusqué

Autant les techniques ci-dessus fonctionnent pour frustrer les attaquants, elles sont loin d'être une défense parfaite. Toute personne ayant suffisamment de temps et de compétences trouvera encore un moyen de les vaincre. Mais cela nous amène à l'une des techniques d'obfuscation les plus essentielles de toutes.

Puisque toutes les techniques d'obfuscation visent à augmenter la complexité du travail d'un attaquant, tout ce que vous pouvez faire pour le ramener à la case départ est une excellente mesure défensive. Donc, pour garder votre code protégé, utilisez Internet à votre avantage.

Vous pouvez émettre des mises à jour périodiques qui font tourner la nature et les spécificités des techniques d'obfuscation que vous utilisez. Chaque fois que vous le faites, tout le travail que quelqu'un pourrait avoir mis à craquer votre logiciel devient une perte de temps. 

Si vous faites tourner vos tactiques d'obfuscation suffisamment souvent, cela ne vaudra pas la peine pour quiconque d'essayer de maintenir une analyse suffisamment longue pour réussir.

## Sécurité par l'obscurité

Le fond du problème est qu'il n'existe pas de code "inpiratable". Peu importe à quel point un programmeur essaie, il y aura toujours une vulnérabilité quelque part. Ce qui ne signifie pas que vous ne devriez pas continuer à essayer, cependant.

Mais dans le monde réel, votre code n'a pas besoin d'être parfait. Il doit simplement être suffisamment difficile à craquer pour que personne dans son bon sens ne se donne la peine d'essayer. Et pour ceux qui ne sont pas dans leur bon sens, il doit simplement être suffisamment compliqué et chronophage pour les tenir à distance.

Et c'est exactement ce que les six tactiques ci-dessus peuvent vous aider à accomplir. Mais n'oubliez pas, aucune défense ne vient sans un coût. Lorsque vous déployez ces options, assurez-vous de peser les pénalités de temps d'exécution qu'elles peuvent créer contre les avantages qu'elles fournissent. 

Si vous travaillez sur quelque chose de particulièrement sensible, lancer toutes les balles courbes possibles pourrait en valoir la peine. Mais si vous écrivez un générateur de citation du jour, peut-être ne vous inquiétez pas autant.

Cependant, quelle que soit la manière dont vous choisissez de procéder, ne négligez jamais de prendre le temps de renforcer votre code d'une manière ou d'une autre. C'est simplement la bonne façon de faire les choses dans un monde rempli de menaces cyber-sécuritaires à chaque coin de rue.

_Photo en vedette par ThisIsEngineering de Pexels._