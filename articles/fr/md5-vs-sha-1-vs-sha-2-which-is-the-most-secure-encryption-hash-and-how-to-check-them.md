---
title: MD5 vs SHA-1 vs SHA-2 - Quel est le hachage de chiffrement le plus sécurisé
  et comment les vérifier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-26T23:12:18.000Z'
originalURL: https://freecodecamp.org/news/md5-vs-sha-1-vs-sha-2-which-is-the-most-secure-encryption-hash-and-how-to-check-them
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Hash_function_long.png
tags:
- name: hash functions, MD5, SHA-1, SHA-2, checksum
  slug: hash-functions-md5-sha-1-sha-2-checksum
seo_title: MD5 vs SHA-1 vs SHA-2 - Quel est le hachage de chiffrement le plus sécurisé
  et comment les vérifier
seo_desc: 'By Jeff M Lowery

  What''s a hash function?

  A hash function takes an input value (for instance, a string) and returns a fixed-length
  value. An ideal hash function has the following properties:


  it is very fast

  it can return an enormous range of hash val...'
---

Par Jeff M Lowery

# Qu'est-ce qu'une fonction de hachage ?

Une fonction de hachage prend une valeur d'entrée (par exemple, une chaîne) et retourne une valeur de longueur fixe. Une fonction de hachage **idéal** a les propriétés suivantes :

* elle est [très rapide](https://en.wikipedia.org/wiki/Hash_function#Efficiency)
* elle peut retourner une énorme gamme de valeurs de hachage
* elle génère un hachage unique pour chaque entrée unique (pas de collisions)
* elle génère des valeurs de hachage dissemblables pour des valeurs d'entrée similaires
* les valeurs de hachage générées n'ont aucun motif discernable dans leur [distribution](https://en.wikipedia.org/wiki/Hash_function#Uniformity)

Aucune fonction de hachage idéale n'existe, bien sûr, mais chacune vise à fonctionner aussi près de l'idéal que possible. Étant donné que (la plupart) des fonctions de hachage retournent des valeurs de longueur fixe et que la gamme de valeurs est donc contrainte, cette contrainte peut pratiquement être ignorée. Le nombre de valeurs possibles qui peuvent être retournées par une fonction de hachage 256 bits, par exemple, est à peu près le même que le nombre d'[atomes dans l'univers](https://nakamoto.com/hash-functions/#collision-resistance).

Idéalement, une fonction de hachage ne retourne pratiquement aucune _collision_ – c'est-à-dire que deux entrées différentes ne génèrent pas la même valeur de hachage. Cela est particulièrement important pour les [fonctions de hachage cryptographiques](https://en.wikipedia.org/wiki/Cryptographic_hash_function) : les collisions de hachage sont considérées comme une [vulnérabilité](https://en.wikipedia.org/wiki/Collision_resistance).

Enfin, une fonction de hachage doit générer des valeurs de hachage différentes de manière imprévisible pour toute valeur d'entrée. Par exemple, prenons les deux phrases très similaires suivantes :

```
1. "The quick brown fox."
2. "The quick brown fax."

```

Nous pouvons comparer les [valeurs de hachage MD5 générées](https://www.md5hashgenerator.com/) à partir de chacune des deux phrases :

```
1. 2e87284d245c2aae1c74fa4c50a74c77
2. c17b6e9b160cda0cf583e89ec7b7fc22

```

Deux hachages très dissemblables ont été générés pour deux phrases similaires, ce qui est une propriété utile à la fois pour la validation et la cryptographie. Cela est un corollaire de la [distribution](https://en.wikipedia.org/wiki/Hash_function#Uniformity) : les valeurs de hachage de toutes les entrées doivent être réparties de manière uniforme et imprévisible sur toute la gamme des valeurs de hachage possibles.

# Fonctions de hachage courantes

Il existe plusieurs fonctions de hachage qui sont largement utilisées. Toutes ont été conçues par des mathématiciens et des informaticiens. Au cours de recherches ultérieures, certaines se sont révélées avoir des faiblesses, bien que toutes soient considérées comme suffisamment bonnes pour des applications non cryptographiques.

## MD5

La fonction de hachage MD5 produit une valeur de hachage de 128 bits. Elle a été conçue pour être utilisée en cryptographie, mais des vulnérabilités ont été découvertes au fil du temps, donc elle n'est plus recommandée à cette fin. Cependant, elle est encore utilisée pour le partitionnement de bases de données et le calcul de sommes de contrôle pour valider les transferts de fichiers.

## SHA-1

SHA signifie Secure Hash Algorithm. La première version de l'algorithme était SHA-1, suivie plus tard par SHA-2 (voir ci-dessous).

Alors que MD5 produit un hachage de 128 bits, SHA1 génère un hachage de 160 bits (20 octets). En format hexadécimal, c'est un entier de 40 chiffres. Comme MD5, il a été conçu pour des applications cryptologiques, mais on a rapidement découvert qu'il avait également des vulnérabilités. À ce jour, il n'est plus considéré comme étant moins résistant aux attaques que MD5.

## SHA-2

La deuxième version de SHA, appelée SHA-2, a de nombreuses variantes. Probablement celle qui est la plus couramment utilisée est SHA-256, que le National Institute of Standards and Technology (NIST) recommande d'utiliser à la place de MD5 ou SHA-1.

L'algorithme SHA-256 retourne une valeur de hachage de 256 bits, ou 64 chiffres hexadécimaux. Bien que pas tout à fait parfait, les recherches actuelles indiquent qu'il est considérablement plus sécurisé que MD5 ou SHA-1.

En termes de performance, un hachage SHA-256 est environ 20-30 % plus lent à calculer que les hachages MD5 ou SHA-1.

## SHA-3

Cette méthode de hachage a été développée à la fin de 2015 et n'a pas encore été largement utilisée. Son algorithme n'est pas lié à celui utilisé par son prédécesseur, SHA-2.

L'algorithme SHA3-256 est une variante avec une applicabilité équivalente à celle du SHA-256 précédent, le premier prenant légèrement plus de temps à calculer que le second.

# Utilisation des valeurs de hachage pour la validation

Une utilisation typique des fonctions de hachage est d'effectuer des vérifications de validation. Une utilisation fréquente est la validation de collections compressées de fichiers, telles que les fichiers d'archives .zip ou .tar.

Étant donné une archive et sa valeur de hachage attendue (communément appelée [checksum](https://techterms.com/definition/checksum)), vous pouvez effectuer votre propre calcul de hachage pour valider que l'archive que vous avez reçue est complète et non corrompue.

Par exemple, je peux générer une somme de contrôle MD5 pour un fichier tar sous Unix en utilisant les commandes suivantes :

```
tar cf - files | tee tarfile.tar | md5sum -

```

Pour obtenir le hachage MD5 d'un fichier sous Windows, utilisez la commande PowerShell [Get-FileHash](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7) :

```
Get-FileHash tarfile.tar -Algorithm MD5

```

La somme de contrôle générée peut être publiée sur le site de téléchargement, à côté du lien de téléchargement de l'archive. Le destinataire, une fois qu'il a téléchargé l'archive, peut valider qu'elle est arrivée correctement en exécutant la commande suivante :

```
echo '2e87284d245c2aae1c74fa4c50a74c77 tarfile.tar' | md5sum -c

```

où **2e87284d245c2aae1c74fa4c50a74c77** est la somme de contrôle générée qui a été publiée. L'exécution réussie de la commande ci-dessus générera un statut OK comme ceci :

```
echo '2e87284d245c2aae1c74fa4c50a74c77 tarfile.tar' | md5sum -ctarfile.tar: OK
```