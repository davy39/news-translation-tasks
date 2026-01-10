---
title: L'algorithme de Rabin-Karp expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-rabin-karp-algorithm-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d0b740569d1a4ca3596.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: L'algorithme de Rabin-Karp expliqué
seo_desc: 'The Rabin-Karp algorithm is a string matching/searching algorithm developed
  by Michael O. Rabin and Richard M. Karp. It uses hashing technique and brute force
  for comparison, and is a good candidate for plagiarism detection.

  Important terms


  pattern ...'
---

L'algorithme de Rabin-Karp est un algorithme de recherche de chaînes de caractères développé par Michael O. Rabin et Richard M. Karp. Il utilise la technique de **_hachage_** et la **_force brute_** pour la comparaison, et est un bon candidat pour la détection de plagiat.

## Termes importants

* **_motif_** est la chaîne de caractères à rechercher. Considérez la longueur du motif comme étant de **_M_** caractères.
* **_texte_** est le texte entier dans lequel le motif doit être recherché. Considérez la longueur du texte comme étant de **_N_** caractères.

## Qu'est-ce que la comparaison par force brute ?

Dans la comparaison par force brute, chaque caractère du motif est comparé avec chaque caractère du texte jusqu'à ce que des caractères qui ne correspondent pas soient trouvés.

## Comment fonctionne l'algorithme de Rabin-Karp

1. Calculer la valeur de hachage du _motif_
2. Calculer la valeur de hachage des premiers _M_ caractères du _texte_
3. Comparer les deux valeurs de hachage
4. Si elles sont différentes, calculer la valeur de hachage pour les _M_ caractères suivants du _texte_ et comparer à nouveau.
5. Si elles sont égales, effectuer une comparaison par force brute.

```text
hash_p = valeur de hachage du motif
hash_t = valeur de hachage des premières M lettres dans le corps du texte
faire
	if (hash_p == hash_t) 
		comparaison par force brute du motif et de la section sélectionnée du texte
	hash_t = valeur de hachage de la section suivante du texte, un caractère plus loin
while (fin du texte ou comparaison par force brute == true)
```

## Avantages par rapport à l'algorithme de recherche de chaînes naïf

Cette technique ne nécessite qu'une seule comparaison par sous-séquence de texte et la force brute n'est nécessaire que lorsque les valeurs de hachage correspondent.