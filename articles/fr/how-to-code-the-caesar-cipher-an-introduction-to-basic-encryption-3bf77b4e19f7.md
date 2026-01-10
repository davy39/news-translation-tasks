---
title: 'Comment coder le Chiffre de César : une introduction au chiffrement de base'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T19:23:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-the-caesar-cipher-an-introduction-to-basic-encryption-3bf77b4e19f7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tuogeHoQ53SQACY-.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Java
  slug: java
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Comment coder le Chiffre de César : une introduction au chiffrement de
  base'
seo_desc: 'By Brendan Massey

  The Caesar Cipher is a famous implementation of early day encryption. It would take
  a sentence and reorganize it based on a key that is enacted upon the alphabet. Take,
  for example, a key of 3 and the sentence, “I like to wear hats....'
---

Par Brendan Massey

Le Chiffre de César est une célèbre implémentation du chiffrement des premiers jours. Il prenait une phrase et la réorganisait en fonction d'une clé appliquée à l'alphabet. Prenons, par exemple, une clé de 3 et la phrase, « I like to wear hats. »

Lorsque cette phrase est chiffrée avec une clé de 3, elle devient :

L olnh wr zhdu kdwv.

Cela la rend difficile à lire et permet de transmettre des messages non détectés.

Bien que ce soit un exemple très simple de chiffrement, c'est un projet parfait pour quelqu'un qui apprend à coder pour s'exercer.

#### Comprendre le chiffre

Pour implémenter ce code, au moins en JAVA, il faudrait réfléchir à ce qui est réellement fait. Alors, examinons les étapes nécessaires pour coder cela.

Étape 1 : Identifier le caractère dans la phrase.

Étape 2 : Trouver l'emplacement de ce caractère dans l'alphabet.

Étape 3 : Identifier l'emplacement de ce caractère + la clé dans l'alphabet.

*Note : si l'emplacement + la clé > 26, revenez au début et commencez à compter à un.

Étape 4 : Construire une nouvelle phrase en utilisant les nouveaux caractères à la place des caractères originaux.

Étape 5 : répéter jusqu'à atteindre la longueur de la phrase. (Boucle For).

Étape 6 : retourner le résultat.

#### Coder le chiffre

Bien que ce soient de bonnes étapes à suivre, nous devrions penser à ce que nous devrions faire en code.

Étape 0 : Établir une fonction qui lit un message et une clé.

Quelque chose comme ceci :

```
public String Encrypt(String message, int key) {
```

```
}
```

Étape 1 : Identifier le caractère dans la phrase.

Pour ce faire, nous devrons établir un alphabet à consulter.

Établir une variable « alphabet » qui contient les 26 lettres de l'alphabet.

```
String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";String alphabet2 = alphabet.toLowerCase();
```

Étape 2 : Trouver l'emplacement de ce caractère dans l'alphabet.

Ensuite, créer une boucle for qui parcourt chaque caractère du message. Il sera plus facile de le faire si nous établissons un StringBuilder.

```
StringBuilder encrypted = new StringBuilder(message);
```

```
for (int q = 0; q < encrypted.length(); q++) {    char currchar = encrypted.charAt(q);    int index = alphabet.indexOf(currchar);}
```

À ce stade, nous devrions nous assurer que l'emplacement est une lettre.

```
if (index != -1) {
```

```
}    
```

Étape 3 : Identifier l'emplacement de ce caractère + la clé dans l'alphabet.

Si c'est une lettre, alors nous devons trouver l'emplacement dans l'alphabet modifié. Nous n'avons pas encore établi de variable d'alphabet modifié, alors nous devrions le faire maintenant.

Étape 4 : Construire une nouvelle phrase en utilisant les nouveaux caractères à la place des caractères originaux.

Une fois que nous avons trouvé la valeur dans l'alphabet modifié, nous devrions la définir au même emplacement dans le StringBuilder que nous avons créé.

```
public String Encryption(String input, int key){        StringBuilder encrypted = new StringBuilder(input);        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";        String alphabet2 = alphabet.toLowerCase();        String keyedalphabet = alphabet.substring(key) + alphabet.substring(0, key);for (int q = 0; q < encrypted.length(); q++) {            char currChar = encrypted.charAt(q);            int index = alphabet.indexOf(currChar);            if (index != -1) {                char newChar = keyedalphabet.charAt(index);                encrypted.setCharAt(q, newChar);            }
```

Étape 5 : répéter jusqu'à atteindre la longueur de la phrase. (Boucle For)

Maintenant, nous avons vérifié si le caractère est en majuscule, mais nous devons aussi vérifier si le caractère est en minuscule. Pour ce faire, nous devons accéder à alphabet2 que nous avons établi précédemment.

```
index = alphabet2.indexOf(currChar);            if (index != -1) {                String keyedalphabet2 = keyedalphabet.toLowerCase();                char newChar = keyedalphabet2.charAt(index);                encrypted.setCharAt(q, newChar);            }
```

Étape 6 : retourner le résultat.

Maintenant, nous avons terminé la boucle For. Il ne nous reste plus qu'à en sortir et à retourner la String.

```
public String Encryption(String input, int key){        StringBuilder encrypted = new StringBuilder(input);        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";        String alphabet2 = alphabet.toLowerCase();        String keyedalphabet = alphabet.substring(key) + alphabet.substring(0, key);        for (int q = 0; q < encrypted.length(); q++) {            char currChar = encrypted.charAt(q);            int index = alphabet.indexOf(currChar);            if (index != -1) {                char newChar = keyedalphabet.charAt(index);                encrypted.setCharAt(q, newChar);            }            index = alphabet2.indexOf(currChar);            if (index != -1) {                String keyedalphabet2 = keyedalphabet.toLowerCase();                char newChar = keyedalphabet2.charAt(index);                encrypted.setCharAt(q, newChar);            }        }        return encrypted    }
```

Étape 7 : Déboguer.

Mais attendez ! Cela ne fonctionnera pas ! encrypted n'est pas une String, c'est un StringBuilder et cette fonction nécessite spécifiquement qu'une String soit retournée !

Heureusement, il existe une fonction très simple pour remédier à cet oubli.

```
public String Encryption(String input, int key){        StringBuilder encrypted = new StringBuilder(input);        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";        String alphabet2 = alphabet.toLowerCase();        String keyedalphabet = alphabet.substring(key) + alphabet.substring(0, key);        for (int q = 0; q < encrypted.length(); q++) {            char currChar = encrypted.charAt(q);            int index = alphabet.indexOf(currChar);            if (index != -1) {                char newChar = keyedalphabet.charAt(index);                encrypted.setCharAt(q, newChar);            }            index = alphabet2.indexOf(currChar);            if (index != -1) {                String keyedalphabet2 = keyedalphabet.toLowerCase();                char newChar = keyedalphabet2.charAt(index);                encrypted.setCharAt(q, newChar);            }        }        return encrypted.toString();    }
```

C'est ainsi que vous obtenez la version chiffrée de votre phrase originale. Essayez par vous-même !

Merci d'avoir lu !