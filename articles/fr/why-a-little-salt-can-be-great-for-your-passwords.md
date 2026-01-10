---
title: Pourquoi un peu de sel peut être excellent pour vos mots de passe (mais pas
  de poivre !)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-30T23:23:00.000Z'
originalURL: https://freecodecamp.org/news/why-a-little-salt-can-be-great-for-your-passwords
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9be2740569d1a4ca2e82.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: information security
  slug: information-security
- name: passwords
  slug: passwords
seo_title: Pourquoi un peu de sel peut être excellent pour vos mots de passe (mais
  pas de poivre !)
seo_desc: "By Megan Kaczanowski\nA brief note - this article is about the theory of\
  \ how to crack hashed passwords. Understanding how cybercriminals execute attacks\
  \ is extremely important for understanding how to secure systems against those types\
  \ of attacks. \nBu..."
---

Par Megan Kaczanowski

Une brève note - cet article traite de la théorie sur la façon de craquer des mots de passe hachés. Comprendre comment les cybercriminels exécutent des attaques est extrêmement important pour comprendre comment sécuriser les systèmes contre ces types d'attaques. 

Mais tenter de pirater un système que vous ne possédez pas est probablement illégal dans votre juridiction (de plus, pirater vos propres systèmes peut [et souvent] violer toute garantie pour ce produit). 

Cet article suppose un certain niveau de connaissance des fonctions de hachage et des techniques de base de craquage de mots de passe - si vous ne comprenez pas ces sujets, consultez [ces](https://www.freecodecamp.org/news/how-did-someone-get-my-password-2/) [articles](https://www.freecodecamp.org/news/an-intro-to-password-cracking/).

Donc, vous avez obtenu un ensemble de mots de passe hachés. Forcer brutalement le hachage prendra un [très](https://www.quora.com/How-long-would-it-take-to-brute-force-a-10-digit-passwords-MD5-hash-using-the-fastest-computer-available-on-consumer-market) long moment. Comment pouvez-vous accélérer ce processus ?

### Attendez, je pensais que les fonctions de hachage étaient à sens unique ! Comment craquez-vous les fonctions de hachage ? 

Malheureusement, les fonctions de hachage utilisées pour hacher les mots de passe ne sont pas toujours aussi sécurisées que les fonctions de hachage généralement approuvées. Par exemple, la fonction de hachage utilisée pour les anciens appareils Windows est connue sous le nom de LM Hash, qui est si faible qu'elle peut être craquée en quelques secondes.

De plus, vous n'avez pas besoin de reverse engineer le hachage. Au lieu de cela, vous pouvez utiliser un ensemble pré-calculé de mots de passe en texte clair et la valeur de hachage correspondante (<password>, <hash>). Cela indique à un pirate quel texte clair produit un hachage spécifique.

Avec cela, vous saurez quelle valeur en texte clair produit le hachage que vous recherchez. Lorsque vous entrez un mot de passe, l'ordinateur hachera cette valeur et la comparera à la valeur stockée (où elle correspondra) et vous pourrez vous authentifier. Ainsi, vous n'avez pas réellement besoin de deviner le mot de passe de quelqu'un, juste une valeur qui créera le même hachage.

Cela s'appelle une collision. Essentiellement, comme un hachage peut prendre des données de n'importe quelle longueur ou contenu, il existe des possibilités illimitées pour les données qui peuvent être hachées. 

Puisqu'un hachage convertit ce texte en un contenu de longueur fixe (par exemple, 32 caractères), il existe un nombre fini de combinaisons pour un hachage. C'est un nombre très très grand de possibilités, mais pas infini.

Finalement, deux ensembles de données différents produiront la même valeur de hachage. 

Les tables pré-calculées sont très utiles pour y parvenir, car elles économisent beaucoup de temps et de puissance de calcul. L'utilisation d'un ensemble pré-calculé de hachages pour rechercher un hachage de mot de passe s'appelle une 'attaque par table de recherche'. Ces tables sont utilisées par les administrateurs système pour tester la force des mots de passe de leurs utilisateurs, et sont souvent disponibles en ligne ou à l'achat. Cependant, elles peuvent également être utilisées par des pirates malveillants.

Si un mot de passe est peu sécurisé (disons que quelqu'un utilise un mot de passe de 5 caractères), il peut être relativement facilement craqué. Par exemple, un mot de passe de 5 caractères en minuscules ne peut être utilisé que pour créer 11 881 376 mots de passe différents (26^5). 

Pour un hachage de ce mot de passe, même si le hachage est cryptographiquement sécurisé (utilise un algorithme approprié), il serait encore très facile de calculer tous les mots de passe possibles et leurs hachages correspondants. Les tables de recherche fonctionnent très bien pour ces types de hachages de mots de passe. 

Cependant, à mesure que les mots de passe augmentent en longueur, le stockage (et donc le coût de stockage) dont vous avez besoin pour chaque mot de passe possible et le hachage correspondant croît exponentiellement. 

Par exemple, si le mot de passe que vous essayez de craquer fait 8 caractères de long mais utilise des chiffres (10 chiffres), des lettres minuscules (26), des lettres majuscules (26) et quelques caractères spéciaux (10), le nombre de mots de passe possibles passe à 722 204 136 308 736 - ce qui est BEAUCOUP d'espace de stockage, lorsque vous réalisez que chacun est haché avec une fonction de hachage comme SHA-256.

Les tables arc-en-ciel abordent ce problème en offrant des besoins de stockage réduits, mais elles prennent plus de temps pour calculer les mots de passe potentiels. Au niveau le plus basique, ce sont essentiellement des tables de recherche pré-calculées qui vous permettent de trouver rapidement le texte clair qui correspond au hachage que vous avez. Si le hachage et le texte clair sont contenus dans la table que vous avez - similaire aux attaques par dictionnaire - vous ne cherchez qu'à voir si le mot de passe est contenu dans la table que vous avez. Si ce n'est pas le cas, vous ne pourrez pas craquer le mot de passe. Vous pouvez trouver ces tables en ligne gratuitement ou à l'achat. 

Consultez [cet article](https://null-byte.wonderhowto.com/how-to/create-rainbow-tables-for-hashing-algorithms-like-md5-sha1-ntlm-0193022/) pour un tutoriel sur la création de vos propres tables arc-en-ciel.

### Je suis toujours intéressé. Comment fonctionnent les tables arc-en-ciel ? 

_Si vous souhaitez sauter l'explication détaillée de leur fonctionnement, n'hésitez pas à faire défiler jusqu'à la section 'Comment se protéger contre ces attaques'._

Afin de vous éviter de hacher et de stocker chaque texte clair possible jusqu'à ce que vous trouviez le hachage dont vous avez besoin (comme une table de recherche), vous hachez chaque texte clair et stockez le résultat dans une table à rechercher plus tard sans avoir à les régénérer. Cela prend plus de temps, mais économise de la mémoire. 

Pour générer la table, vous créez des 'chaînes' de hachages et de textes clairs en utilisant une fonction de hachage et une fonction de réduction. Une fonction de réduction crée simplement du texte clair à partir d'un hachage (elle ne reverse pas le hachage, mais crée plutôt un texte clair différent à partir du hachage). C'est aussi une fonction à sens unique.

Ainsi, afin de calculer la table, vous utilisez l'un de vos hachages, h1, dans votre fonction de réduction, R(), afin de créer le texte clair p1.

R(h1) = p1.

Ensuite, vous utilisez la fonction de hachage H() avec p1 pour créer un nouveau hachage.

H(p1) = h2.

En utilisant notre exemple précédent :

Si l'ensemble de textes clairs est [abcdefghijklmnopqrstuvwxyz]{5} (nous cherchons une table arc-en-ciel de tous les mots de passe composés de lettres minuscules de longueur 5) et que nous utilisons MD5 (un algorithme de hachage) :

Un hachage pourrait être ab56b4d92b40713acc5af89985d4b786 (h1). Maintenant, nous appliquons la fonction de réduction, qui pourrait être aussi simple que de prendre les 5 dernières lettres du hachage.

R(ab56b4d92b40713acc5af89985d4b786) = cafdb

H(cafdb) = 81a516edabf924cd0f727d329e855b1f

### Pourquoi sont-elles appelées tables arc-en-ciel ?

Chaque colonne utilise une fonction de réduction différente. Donc, si chaque colonne était colorée, ce serait un très long arc-en-ciel étroit.  

L'utilisation de fonctions de réduction différentes réduit le nombre de fusions de chaînes (collisions) qui se produisaient fréquemment avec les chaînes de hachage, le prédécesseur des tables arc-en-ciel. Cela signifie essentiellement que si vous continuez à utiliser la même fonction de réduction, il y a une chance que vous finissiez avec deux chaînes différentes qui convergent vers le même texte clair. L'utilisation de fonctions de réduction différentes réduit la chance que cela se produise, bien que ce ne soit pas impossible. 

### Super, comment créez-vous une chaîne ?

Afin de créer une chaîne, vous utilisez votre fonction de réduction et votre fonction de hachage (toutes deux à sens unique) pour créer une 'chaîne' de hachages et de textes clairs. Chacune de ces 'chaînes' continuerait pour k étapes, et lorsque la chaîne se termine, elle ne stocke que le premier texte clair et le dernier hachage de la chaîne. 

Ainsi, une chaîne d'exemple ressemble à ceci :

p1 -> h1 = H(p1) -> R1(h1) = p2 -> H(p2) = h2 -> R2(h2) = p3 -> H(p3) = h3

Chaque fonction de réduction est différente (représentée par R1, R2, R3, etc.) Un exemple de table de chaînes (chaque ligne est une chaîne de longueur 5) ressemble à ce qui suit. Notez que cela est peuplé de fausses données juste pour vous donner un exemple - la fonction de hachage n'est pas une fonction de hachage que vous trouveriez utilisée pour hacher les mots de passe. 

Les fonctions de réduction, R1 et R2 sont définies comme suit – R1 prend les 3 premiers chiffres du hachage, et R2 prend les 2 dernières lettres du hachage :

p1 -> h1 = H(p1) -> R1(h1) = p2 -> H(p2) = h2 -> R2(h2) = p3 -> H(p3) = h3

2  -	>  abdu2934   -	>  293  -	>  83kdnif8  -	>  if  -	>  ike83jd3		

15  -	>  dks2ne94  -	>   294  -	>  ld932nd9  -	>  ld  -	>  ldie938d	

20  -	>  ld93md8d  -	>  938  -	>  lxked93k  -	>  lx  -	>  93mdkg8d		

Dans une table arc-en-ciel, seul le premier point de départ et le point final sont sauvegardés pour économiser de l'espace de stockage, comme ceci :

point de départ (texte clair)					point final, après k étapes à travers la chaîne (hachage)

			p1							  -	>  							 h1k

			p2							  -	>  							h2k

			p3							  -	>  					        h3k

Ensuite, lorsque vous avez un hachage (h) où vous ne connaissez pas le texte clair (?), vous le comparerez aux chaînes.

1. Tout d'abord, vous vérifierez si le hachage est dans la liste des hachages finaux (h1k, h2k, etc.). Si c'est le cas, vous pouvez passer à l'étape 3.
2. Si ce n'est pas le cas, vous pouvez réduire le hachage à différents textes clairs (R1) puis hacher ce texte clair (en utilisant la fonction de hachage et la fonction de réduction suivante ci-dessus) et le comparer à la liste des hachages finaux (h1k, h2k, h3k, etc.). Lorsqu'il correspond à l'un des hachages finaux, cette chaîne contiendra probablement le hachage original.
3. Afin de trouver le hachage original dans la chaîne, prenez le texte clair de départ de cette chaîne (donc si elle correspond à h1k, commencez avec p1) et appliquez les fonctions de hachage et de réduction pour vous déplacer le long de la chaîne jusqu'à ce que vous atteigniez le hachage connu et son texte clair correspondant. De cette façon, vous pouvez parcourir les hachages de la chaîne sans qu'ils ne prennent de place de stockage sur votre machine.

Bien que vous ne puissiez pas être sûr que les chaînes contiendront le hachage dont vous avez besoin, plus vous avez généré de chaînes (ou que vous référencez), plus vous pouvez être certain. Malheureusement, chaque chaîne prend du temps à générer, et augmenter le nombre de chaînes augmente le temps dont vous avez besoin.

### Comment vous défendre contre ces types d'attaques ?

Tout d'abord, une défense en couches de tous les systèmes. Si vous pouvez empêcher la compromission de vos systèmes via d'autres méthodes (de sorte que l'attaquant ne puisse pas obtenir une copie de vos mots de passe hachés), l'attaquant ne pourra pas les craquer. 

Vous pouvez également utiliser le salage, qui ajoute une valeur aléatoire au mot de passe avant de le chiffrer. Cela signifie que la valeur pré-calculée que vous avez trouvée (qui correspond au hachage) ne fonctionnera pas. Le texte chiffré n'est pas basé uniquement sur le texte non chiffré. Parce que le sel est différent pour chaque mot de passe, chacun doit être craqué individuellement. 

Le salage est maintenant inclus dans la plupart des types de hachage majeurs en tant qu'option. Bien que Windows n'utilise pas actuellement le salage, ils peuvent chiffrer les hachages stockés si vous utilisez l'outil 'SYSKEY'. 

Vous pouvez également utiliser des 'rounds', ou hacher un mot de passe plusieurs fois. L'utilisation de rounds (en particulier si le nombre de rounds est choisi aléatoirement pour chaque utilisateur) rend le travail du pirate plus difficile. Cela est plus efficace lorsqu'il est combiné avec le salage.

Malheureusement, un pirate qui a les mots de passe hachés aura également accès au nombre de rounds utilisés et au sel utilisé (parce que pour obtenir cette liste, ils ont probablement compromis . Le sel et le nombre de rounds utilisés sont stockés avec le hachage du mot de passe, ce qui signifie que si l'attaquant en a un, il a aussi l'autre. Cependant, ils ne pourront pas utiliser les tables arc-en-ciel pré-calculées disponibles en ligne, et devront calculer leurs propres tables (ce qui est extrêmement chronophage). 

Une autre méthode conçue pour augmenter la difficulté de craquage du mot de passe est d'utiliser un poivre. Le poivre est similaire au sel, mais tandis qu'un sel n'est pas secret (il est stocké avec le mot de passe haché), le poivre est stocké séparément (par exemple, dans un fichier de configuration) afin d'empêcher un pirate d'y accéder. Cela signifie que le poivre est secret, et son efficacité dépend de cela.

Le poivre doit être différent pour chaque application pour laquelle il est utilisé, et doit être suffisamment long pour être sécurisé. Au moins 112 bits sont recommandés par le National Institute of Standards and Technology. 

Bien que l'utilisation d'un poivre puisse être efficace dans certains cas, il y a quelques inconvénients. Tout d'abord, aucun algorithme actuel ne supporte les poivres, ce qui signifie que, pratiquement, cela est impossible à mettre en œuvre à grande échelle. C'est-à-dire, sauf si vous créez vos propres algorithmes. Écoutez [Bruce Schneier](https://www.schneier.com/blog/archives/2011/04/schneiers_law.html). **Ne faites pas cela.** 

Pour un article plus long sur les problèmes avec les poivres, consultez [ce fil.](https://stackoverflow.com/questions/16891729/best-practices-salting-peppering-passwords)

Enfin, utilisez des mots de passe forts (au moins 12 caractères), complexes, et mettez en œuvre des politiques de mots de passe forts sur tous les systèmes. Cela peut inclure le fait de forcer les utilisateurs à créer des mots de passe forts, de tester leur force régulièrement, d'utiliser des gestionnaires de mots de passe au niveau de l'entreprise, d'imposer l'utilisation de la 2FA, et ainsi de suite.

Confus quant à ce qui fait un mot de passe fort ?

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-26-at-5.21.11-PM-1.png)
_[https://xkcd.com/936/](https://xkcd.com/936/)_

### Cela semble vraiment facile de se faire pirater. Devrais-je être inquiet ? 

La chose la plus importante à retenir sur le piratage est que personne ne veut faire plus de travail que nécessaire. Par exemple, calculer des tables arc-en-ciel est un travail fastidieux. S'il y a une manière plus facile d'obtenir votre mot de passe, c'est probablement ce qu'un acteur malveillant essaiera en premier (comme le phishing !). 

Cela signifie que l'activation des meilleures pratiques de base en matière de cybersécurité est probablement le moyen le plus facile d'empêcher de se faire pirater. En fait, Microsoft a [récemmentsignalé](https://www.zdnet.com/article/microsoft-using-multi-factor-authentication-blocks-99-9-of-account-hacks/) que simplement activer la 2FA finira par bloquer 99,9 % des attaques automatisées. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-27-at-1.18.47-PM.png)
_[https://xkcd.com/538/](https://xkcd.com/538/)_

## Bon piratage !



**Lectures supplémentaires :**

[Plus de détails sur les chaînes de hachage](https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture24.pdf)

[Une autre explication des tables arc-en-ciel](http://kestas.kuliukas.com/RainbowTables/)

[Une liste de tables arc-en-ciel en ligne](http://project-rainbowcrack.com/table.htm)