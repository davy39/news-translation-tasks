---
title: 'Comment renforcer votre code : Principes essentiels de conception sécurisée
  pour les développeurs'
subtitle: ''
author: Chama Jennane
co_authors: []
series: null
date: '2024-10-09T20:17:10.359Z'
originalURL: https://freecodecamp.org/news/essential-secure-design-principles-for-developers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728461315564/0ec07485-8537-475e-8b15-3ab653ababfc.jpeg
tags:
- name: secure coding
  slug: secure-coding
- name: software development
  slug: software-development
- name: softwaresecurity
  slug: softwaresecurity
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: information security
  slug: information-security
- name: infosec
  slug: infosec-cjbi6apo9015yaywu2micx2eo
- name: appsec
  slug: appsec
seo_title: 'Comment renforcer votre code : Principes essentiels de conception sécurisée
  pour les développeurs'
seo_desc: 'Secure design principles have long been the foundation for building secure
  systems. And they remain a crucial aspect of modern cybersecurity.

  Introduced in 1975 by Saltzer and Schroeder in their landmark paper The Protection
  of Information in Compute...'
---

Les principes de conception sécurisée sont depuis longtemps le fondement de la construction de systèmes sécurisés. Et ils restent un aspect crucial de la cybersécurité moderne.

Introduits en 1975 par Saltzer et Schroeder dans leur article fondateur *The Protection of Information in Computer Systems*, ces principes intemporels continuent de guider la conception de systèmes sécurisés aujourd'hui.

Les principes de conception sécurisée visent à protéger les informations stockées sur ordinateur contre les accès non autorisés. Dans cet article, nous discuterons de ces principes en détail, en soulignant leur pertinence continue dans la prévention des vulnérabilités de sécurité. Vous verrez quelques exemples concrets qui mettent en évidence l'importance de respecter ces principes pour créer des systèmes robustes et sécurisés.

Saltzer et Schroeder ont décrit huit principes fondamentaux ainsi que deux principes supplémentaires. Ces principes supplémentaires, bien que initialement considérés comme s'appliquant de manière imparfaite aux systèmes informatiques, se sont depuis avérés essentiels.

Commençons par esquisser ces principes de conception sécurisée avant d'approfondir chacun d'eux.

## Principes clés de conception sécurisée :

1. Économie de mécanisme : Gardez les conceptions simples et minimales.

2. Échec sécurisé par défaut : Basez l'accès sur la permission, pas sur l'exclusion.

3. Médiation complète : Vérifiez chaque demande d'accès pour l'autorité.

4. Conception ouverte : Les secrets résident dans les données, pas dans la conception.

5. Séparation des privilèges : Exigez deux parties pour les décisions critiques, c'est plus sûr.

6. Moindre privilège : Opérez avec les permissions minimales nécessaires.

7. Moindre mécanisme commun : Limitez les sous-systèmes partagés entre les utilisateurs.

8. Acceptabilité psychologique : Assurez la convivialité pour les humains.

Principes supplémentaires :

9. Facteur de travail : Pesez le coût de la violation de la sécurité contre les ressources de l'attaquant.

10. Enregistrement des compromis : Journalisez les violations lorsqu'elles se produisent.

## **Les huit principaux principes de conception sécurisée**

### **Économie de mécanisme**

Le premier principe indique que vous devez garder votre conception simple et compacte pour minimiser les chemins d'accès indésirables.

Les erreurs passent souvent inaperçues lors d'une utilisation normale, ce qui rend crucial d'avoir des conceptions simples qui sont plus faciles à inspecter pour les vulnérabilités. Une base de code plus simple réduit la surface d'attaque, offrant moins d'opportunités d'exploitation et facilitant la vérification du code.

Mais rappelez-vous que la simplicité n'est pas simplement un synonyme de brièveté. Par exemple, considérons ce code C :

```c
// Exemple A
if (a = b)

// Exemple B
a = b;
if (a != 0)
```

Ici, quelqu'un qui regarde ce code peut penser que le développeur voulait "==" au lieu de "=". Le premier exemple pourrait prêter à confusion, tandis que le second exprime clairement l'intention du développeur. Cela peut sembler trivial, mais cette confusion a été clé dans une [tentative d'installer une porte dérobée dans le noyau Linux en 2003](https://freedom-to-tinker.com/2013/10/09/the-linux-backdoor-attempt-of-2003/) !

En fin de compte, il est tentant d'écrire des hacks concis qui fonctionnent, mais ils peuvent devenir confus, même pour vous-même à l'avenir. Privilégiez un code propre et respectez les normes et les meilleures pratiques de codage.

### **Échec sécurisé par défaut**

Vous devez baser les décisions d'accès sur la permission plutôt que sur l'exclusion. Les erreurs dans les systèmes basés sur les permissions entraînent généralement des refus accidentels, c'est-à-dire que les utilisateurs se voient refuser l'accès à des informations nécessaires. Ces refus peuvent être rapidement identifiés.

En revanche, les erreurs dans les systèmes basés sur l'exclusion peuvent conduire à des accès non autorisés. Ceux-ci peuvent souvent passer inaperçus, car les gens signalent rarement avoir des permissions inutiles.

En essence, vous devez privilégier les listes d'autorisation plutôt que les listes de refus, non seulement dans le contrôle d'accès, mais aussi dans la validation des entrées.

Une liste d'autorisation (autrefois connue sous le nom de liste blanche) spécifie qui peut accéder à quoi, en refusant tout le monde par défaut. En revanche, une liste de refus (autrefois connue sous le nom de liste noire) permet tous les accès sauf pour les exclusions spécifiées. Celles-ci sont souvent mises en œuvre sous forme de règles, telles que l'autorisation d'une valeur entière comprise entre 0 et 200, ou une chaîne qui doit correspondre à une expression régulière avant de pouvoir être acceptée comme adresse e-mail.

### **Médiation complète**

Ce principe stipule que chaque accès à chaque objet doit subir une vérification d'autorité. Il garantit une vue d'ensemble du contrôle d'accès, englobant toutes les opérations du système, de l'initialisation à la récupération, à l'arrêt et à la maintenance.

Il nécessite une méthode fiable pour identifier la source de chaque demande, et tout changement d'autorité doit être rapidement mis à jour. Ce principe s'applique également à la validation des entrées.

La médiation complète souligne qu'aucun accès ne doit dépendre de vérifications précédentes ou d'hypothèses de validité, reflétant l'approche de défense en profondeur. Chaque demande d'accès doit être validée en temps réel pour prévenir les vulnérabilités, telles que les attaques de type time-of-check to time-of-use (TOCTTOU).

Considérons ce scénario : Vous avez deux cartes ATM liées au même compte bancaire. Lorsque vous tentez de retirer vos fonds à un ATM, il vérifie votre solde et demande confirmation. En attendant, vous utilisez l'autre ATM pour retirer le montant entier. Si le premier ATM ne vérifiait pas à nouveau votre solde, vous pourriez exploiter cela pour retirer des fonds deux fois.

Heureusement, la médiation complète garantit que l'ATM vérifie à nouveau votre solde avant de distribuer de l'argent, empêchant ainsi efficacement une telle exploitation.

### **Conception ouverte**

La transparence de la conception est cruciale. La sécurité ne doit pas reposer sur l'ignorance des attaquants potentiels, mais plutôt sur des clés ou des mots de passe bien protégés. Maintenir le secret dans des systèmes largement distribués est irréaliste.

Le principe de conception ouverte est basé sur le [principe de Kerckhoff](https://petitcolas.net/kerckhoffs/index.html), qui affirme que la sécurité d'un système cryptographique repose uniquement sur le secret de ses clés, tandis que l'algorithme lui-même doit être une connaissance publique.

En revanche, la sécurité par l'obscurité suppose la sécurité par la dissimulation, ce qui est fondamentalement défectueux. Les attaquants peuvent obtenir des documents de conception, inverser des produits ou exploiter des vulnérabilités cachées. Au-delà de cela, garder l'implémentation secrète complique les audits et les revues de sécurité. Une conception de sécurité efficace ne doit jamais dépendre de la confidentialité de l'implémentation.

### **Séparation des privilèges**

L'utilisation d'un système à double clé est généralement plus sécurisée et adaptable que de compter sur une seule clé pour l'accès. Un principe clé de la conception sécurisée est de mettre en œuvre plusieurs couches de protection. Plus il y a de vérifications en place, plus il devient difficile pour les attaquants.

Mais ces vérifications doivent employer des mécanismes différents. Par exemple, dans l'authentification multifactorielle, combinez des méthodes basées sur la connaissance (comme un mot de passe) avec des méthodes basées sur la possession (comme un jeton) ou des méthodes biométriques (comme une empreinte digitale).

Pour une sécurité supplémentaire, envisagez d'incorporer des données de localisation. Si votre carte de crédit est utilisée à Londres puis à nouveau à Moscou peu après, la détection de fraude de votre banque signalera probablement la deuxième transaction. Mais il est important de noter que les données de localisation ne peuvent pas se substituer à l'un des facteurs d'authentification principaux.

Ce principe implique également la nécessité de créer des utilisateurs avec des rôles et des privilèges spécialisés au lieu de compter sur des superutilisateurs qui peuvent accéder à tout.

### **Moindre privilège**

Chaque programme et chaque utilisateur ne doivent avoir que les privilèges minimaux nécessaires pour accomplir leurs tâches. Identifiez les capacités spécifiques dont un programme a besoin et fournissez uniquement ces permissions. Cette approche réduit considérablement l'impact des attaques potentielles.

Par exemple, un visualiseur d'images ne devrait pas nécessiter d'accès réseau, et une application d'horaires de bus ne devrait pas accéder à votre historique d'appels ou à vos contacts. Bien que la mise en œuvre de cela puisse être difficile, la meilleure stratégie est de refuser toutes les permissions par défaut et de les accorder progressivement si nécessaire.

### **Moindre mécanisme commun**

Minimisez les mécanismes partagés entre les utilisateurs, car chaque composant partagé, en particulier ceux impliquant des variables communes, peut créer des risques de sécurité. Toute dépendance entre les composants peut entraîner des conséquences généralisées si l'un d'eux est compromis.

Soyez prudent avec le code partagé, car les hypothèses peuvent changer lorsque le code interagit avec différents environnements. Par exemple, le désastre de la fusée Ariane 5 a résulté de la réutilisation du code d'Ariane 4 sans le tester avec la nouvelle trajectoire qui avait un biais horizontal beaucoup plus élevé. Cela a causé probablement le [débordement d'entier le plus coûteux de l'histoire](https://hownot2code.wordpress.com/2016/09/02/a-space-error-370-million-for-an-integer-overflow/).

Les données partagées posent des risques similaires. Si deux processus accèdent aux mêmes fichiers temporaires, une compromission de l'un des processus peut affecter l'autre. La séparation et l'isolement des processus ainsi que l'utilisation de techniques comme les conteneurs et la virtualisation peuvent aider à prévenir l'effet domino.

### **Acceptabilité psychologique**

Concevez des interfaces utilisateur faciles à utiliser pour garantir que les utilisateurs appliquent correctement les mécanismes de sécurité. Lorsque les modèles mentaux des utilisateurs s'alignent avec les mécanismes de protection, les erreurs sont minimisées. Si le processus d'authentification est trop compliqué, les utilisateurs peuvent le contourner ou trouver des moyens de le contourner.

Équilibrer la sécurité et la convivialité peut être difficile, car l'augmentation de l'une diminue souvent l'autre. Visez un compromis où les mesures de sécurité sont efficaces mais permettent toujours une expérience utilisateur positive.

## **Les deux principes supplémentaires**

### **Facteur de travail**

Évaluez le coût de contournement des mécanismes de sécurité par rapport aux ressources d'un attaquant, connu sous le nom de "facteur de travail". Bien que certains facteurs de travail soient simples à calculer, de nombreux mécanismes de sécurité informatique défient une évaluation facile, ce qui rend difficile l'estimation précise des risques.

Vous devez viser un équilibre entre les coûts de sécurité et les pertes potentielles, en tenant compte à la fois des motivations de l'attaquant et de la valeur de vos actifs.

Par exemple, sécuriser votre voiture est généralement suffisant si elle est plus difficile à voler que celle de votre voisin. Mais si votre voiture est particulièrement convoitée par les voleurs, vous aurez besoin de mesures de sécurité plus fortes.

Pour un exemple pratique, les algorithmes de stockage de mots de passe, tels que Argon2, bcrypt et scrypt, ont un paramètre de "facteur de travail" qui détermine la quantité de ressources à utiliser. Cela peut être mis à l'échelle pour garder l'algorithme suffisamment rapide pour une utilisation régulière, mais prohibitivement coûteux pour une attaque par force brute.

### **Enregistrement des compromis**

Ce principe souligne la nécessité d'une journalisation efficace et de la collecte de preuves. Si une attaque passe inaperçue, les conséquences peuvent être graves, donc détecter rapidement les violations est vital pour minimiser les dommages et faciliter la réponse aux incidents.

## Conclusion

Comme nous le rappellent Saltzer et Schroeder, ces principes servent d'avertissements utiles plutôt que de règles strictes. Si vous remarquez qu'un principe est violé dans votre conception, c'est un signe que quelque chose pourrait ne pas aller et devrait être examiné de près pour vous assurer que le problème est traité ou n'est pas significatif.

Rappelez-vous, même les systèmes les mieux conçus peuvent être vulnérables si un seul bug se glisse pendant l'implémentation. C'est pourquoi la conception sécurisée et l'implémentation doivent travailler ensemble - la sécurité est une approche globale. La plupart des faiblesses exploitables proviennent soit de la phase de conception, soit de la phase d'implémentation, et les attaquants ne se soucient pas du type qu'ils exploitent - ils veulent simplement s'introduire.

Le dernier OWASP Top 10 souligne le rôle critique de la conception en [mettant en avant "Conception non sécurisée" pour la première fois](https://owasp.org/Top10/A04_2021-Insecure_Design/). Pour y remédier, il est essentiel que les équipes de développeurs comprennent parfaitement les meilleures pratiques.

Le programme de formation au codage sécurisé de [Cydrill](https://cydrill.com/) approfondit ces principes, offrant des exemples concrets qui démontrent comment les négliger peut conduire à des vulnérabilités graves. Consultez-le si vous souhaitez en savoir plus.