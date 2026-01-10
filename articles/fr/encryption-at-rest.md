---
title: Qu'est-ce que le chiffrement au repos ? Expliqué pour les débutants en sécurité
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-04-04T15:49:01.000Z'
originalURL: https://freecodecamp.org/news/encryption-at-rest
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-cottonbro-studio-7319078.jpg
tags:
- name: encryption
  slug: encryption
- name: information security
  slug: information-security
seo_title: Qu'est-ce que le chiffrement au repos ? Expliqué pour les débutants en
  sécurité
seo_desc: 'Encryption is a technique for secure communication that converts plain
  text into a coded form that can only be deciphered with a secret key. Let''s explore
  some of encryption''s fun bits.

  Encryption works by using an algorithm to convert plaintext into...'
---

Le chiffrement est une technique de communication sécurisée qui convertit le texte en clair en une forme codée qui ne peut être déchiffrée qu'avec une clé secrète. Explorons quelques aspects amusants du chiffrement.

Le chiffrement fonctionne en utilisant un algorithme pour convertir le texte en clair en texte chiffré, qui est illisible sans la clé de déchiffrement correspondante. 

Cet article provient de [The Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). Vous pouvez également suivre cette vidéo :

%[https://www.youtube.com/watch?v=kWBLfhf8eto&list=PLSiZCpRYoTZ7wEwmKRsRjaQF3qSi4bbdl&index=2]

Le processus de chiffrement prend les données originales et les transforme de manière à ce que seule une personne possédant la clé de déchiffrement correcte puisse inverser le processus et lire les données originales. Cela aide à garantir que les informations sensibles sont protégées contre les accès non autorisés ou les interceptions pendant la transmission ou le stockage.

## Comprendre les outils de chiffrement

Le chiffrement au repos fait référence à la pratique de protection des données stockées sur un appareil, tel qu'un disque dur ou un smartphone, en les codant à l'aide d'algorithmes de chiffrement. Les données chiffrées ne peuvent être déchiffrées qu'avec la clé appropriée, ce qui aide à garantir que les informations sensibles restent confidentielles même si l'appareil est perdu ou volé. 

Il s'agit d'une mesure de sécurité courante utilisée pour protéger les informations sensibles telles que les numéros de carte de crédit, les données personnelles et les informations confidentielles de l'entreprise.

Le hachage de mot de passe est une technique de stockage des mots de passe de manière sécurisée en les convertissant en une représentation cryptographique appelée hachage. Le hachage est créé à l'aide d'une fonction à sens unique qui transforme le mot de passe en une chaîne de caractères de longueur fixe qui ne peut pas être facilement inversée pour révéler le mot de passe original.

```
$ echo -n mySecretPassword | sha256sum
2250e74c6f823de9d70c2222802cd059dc970f56ed8d41d5d22d1a6d4a2ab66f  -

```

Le salage est une mesure de sécurité ajoutée au hachage de mot de passe pour augmenter sa résilience contre les attaques. Un sel est une valeur aléatoire générée pour chaque mot de passe et combinée avec le mot de passe avant qu'il ne soit haché. 

```
$ openssl passwd -salt 29 mytext
$1$29$WKQPJOxDf2nJLoPwT6cnz1
```

Cela donne un hachage unique pour chaque mot de passe, même si plusieurs utilisateurs ont le même mot de passe, ce qui rend beaucoup plus difficile pour un attaquant d'utiliser des tables de hachages pré-calculées (telles que les tables arc-en-ciel) pour craquer les mots de passe. 

Lors de la vérification d'un mot de passe, le sel est utilisé pour régénérer le hachage, qui est ensuite comparé au hachage stocké pour déterminer si le mot de passe est correct.

## Outils d'attaque de mot de passe

Une table arc-en-ciel est une table de hachages pré-calculée utilisée pour craquer les mots de passe en recherchant une valeur de hachage correspondante. Il s'agit d'une optimisation d'une attaque par force brute qui réduit le nombre de hachages à calculer en réutilisant les hachages calculés pour les devinettes de mots de passe précédents.

Une attaque par dictionnaire est une méthode de craquage de mots de passe en utilisant un grand dictionnaire de mots, de phrases et de mots de passe couramment utilisés pour générer des hachages et les comparer aux hachages cibles. Ce type d'attaque est efficace contre les mots de passe faibles qui sont facilement devinables.

Une attaque par force brute est une méthode de craquage de mots de passe en essayant toutes les combinaisons possibles de caractères jusqu'à ce qu'une correspondance soit trouvée. Il s'agit d'une méthode lente et gourmande en ressources pour craquer les mots de passe, mais elle est efficace contre les mots de passe forts qui ne peuvent pas être facilement devinés. 

Les attaques par force brute peuvent être atténuées en utilisant des mots de passe forts, en limitant le nombre de tentatives de connexion et en utilisant le chiffrement et le hachage pour stocker les mots de passe de manière sécurisée.

## Chiffrement symétrique et asymétrique

La cryptographie symétrique, également connue sous le nom de cryptographie à secret partagé, est un type de chiffrement où la même clé est utilisée pour le chiffrement et le déchiffrement des données. Cela signifie que l'expéditeur et le destinataire des données doivent avoir la même clé et doivent la garder confidentielle. 

La cryptographie symétrique est rapide et efficace mais peut être vulnérable si la clé est compromise.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-09.png)
_Diagramme montrant le fonctionnement du chiffrement symétrique_

La cryptographie asymétrique, également connue sous le nom de cryptographie à clé publique, utilise une paire de clés, une pour le chiffrement et une autre pour le déchiffrement. La clé de chiffrement, connue sous le nom de clé publique, peut être largement distribuée, tandis que la clé de déchiffrement, connue sous le nom de clé privée, est gardée confidentielle. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-10.png)
_Diagramme montrant le fonctionnement du chiffrement asymétrique_

La cryptographie asymétrique est utilisée pour des tâches telles que les signatures numériques, l'échange de clés et le chiffrement de données, et est considérée comme plus sécurisée que la cryptographie symétrique car la clé privée ne doit jamais être transmise ou partagée.

La cryptographie hybride est une combinaison de la cryptographie symétrique et asymétrique. 

Dans un schéma de chiffrement hybride typique, les données sont chiffrées à l'aide d'un algorithme symétrique, et la clé symétrique est ensuite chiffrée à l'aide d'un algorithme asymétrique et envoyée au destinataire avec les données chiffrées. Le destinataire utilise sa clé privée pour déchiffrer la clé symétrique, puis utilise la clé symétrique pour déchiffrer les données. 

La cryptographie hybride offre les avantages de sécurité de la cryptographie symétrique et asymétrique, ce qui en fait une méthode de chiffrement couramment utilisée.

## Infrastructure à clé publique (PKI) 

La PKI est un système de communication sécurisée qui utilise une combinaison de cryptographie à clé publique, de certificats numériques et d'autorités de certification (CA) pour authentifier l'identité des parties impliquées dans une communication et sécuriser leurs communications.

Les autorités de certification (CA) sont des organisations ou des entités qui émettent des certificats numériques, utilisés pour valider l'identité des parties impliquées dans une communication. 

Les CA agissent en tant que tiers de confiance qui vérifient l'identité des parties et émettent des certificats attestant de cette identité. Le certificat inclut des informations telles que l'identité du propriétaire, la clé publique du propriétaire et la signature numérique de la CA.

Les CA racines de confiance sont les CA de plus haut niveau dans la hiérarchie PKI. Elles sont responsables de l'émission de certificats pour les CA intermédiaires, qui à leur tour émettent des certificats pour les entités finales, telles que les individus ou les organisations. 

La fiabilité de l'ensemble du système PKI est basée sur la confiance dans les CA racines. Une CA racine de confiance est une CA largement reconnue et digne de confiance par les utilisateurs, les systèmes et les applications. 

Le certificat de la CA racine de confiance est généralement préinstallé dans les logiciels et les appareils, tels que les navigateurs web, pour faciliter la communication sécurisée et vérifier l'authenticité des certificats numériques émis par d'autres CA.

## Conclusion

Avec ce que vous avez appris ici, vous êtes maintenant prêt à utiliser des outils de chiffrement comme [VeraCrypt](https://www.veracrypt.fr/en/Home.html) et [GnuPG](https://gnupg.org/) pour protéger les données que vous stockez sur vos machines locales. Vous serez en mesure d'évaluer correctement la sécurité et l'intégrité des plateformes de stockage en ligne et dans le cloud où vous stockez des données à distance.

Cet article et la vidéo qui l'accompagne sont extraits de [mon cours Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)