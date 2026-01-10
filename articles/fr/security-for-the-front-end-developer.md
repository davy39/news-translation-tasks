---
title: 'Comment concevoir des formulaires web sécurisés : valider, nettoyer et contrôler'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-12-12T13:55:00.000Z'
originalURL: https://freecodecamp.org/news/security-for-the-front-end-developer
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/D34F9C4D-1AAC-4EA2-804C-3F56BAFA3BC9.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: forms
  slug: forms
- name: Front-end Development
  slug: front-end-development
- name: SQL
  slug: sql
- name: user experience
  slug: user-experience
- name: User Interface
  slug: user-interface
seo_title: 'Comment concevoir des formulaires web sécurisés : valider, nettoyer et
  contrôler'
seo_desc: "While cybersecurity is often thought of in terms of databases and architecture,\
  \ much of a strong security posture relies on elements in the domain of the front-end\
  \ developer. \nFor certain potentially devastating vulnerabilities like SQL injection\
  \ and..."
---

Bien que la cybersécurité soit souvent associée aux bases de données et à l'architecture, une grande partie d'une posture de sécurité solide repose sur des éléments relevant du domaine du développeur front-end. 

Pour certaines vulnérabilités potentiellement dévastatrices comme l'[injection SQL](https://www.owasp.org/index.php/Top_10-2017_A1-Injection) et le [Cross-Site Scripting (XSS)](https://www.owasp.org/index.php/Top_10-2017_A7-Cross-Site_Scripting_(XSS)), une interface utilisateur bien conçue est la première ligne de défense.

Voici quelques domaines de concentration pour les développeurs front-end qui souhaitent aider à combattre le bon combat.

## Contrôler les entrées utilisateur

Une foule de [choses folles](https://victoria.dev/blog/sql-injection-and-xss-what-white-hat-hackers-know-about-trusting-user-input/) peuvent se produire lorsque les développeurs créent un formulaire qui ne contrôle pas les entrées utilisateur. Pour lutter contre les vulnérabilités comme l'injection, il est important de valider ou de nettoyer les entrées utilisateur.

Vous pouvez valider les entrées en les contraignant à des valeurs connues, par exemple en utilisant des [types d'entrée sémantiques](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation#Semantic_input_types) ou des [attributs liés à la validation](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation#Validation-related_attributes) dans les formulaires. Des frameworks comme [Django](https://www.djangoproject.com/) aident également en fournissant des [types de champs](https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types) à cet effet. Le nettoyage des données peut être effectué en supprimant ou en remplaçant des caractères contextuellement dangereux, par exemple en utilisant une liste blanche ou en échappant les données d'entrée.

Bien que cela puisse ne pas être intuitif, même les données qu'un utilisateur soumet à sa propre zone sur un site doivent être validées. L'un des virus les plus rapides à se propager était le [ver Samy](https://en.wikipedia.org/wiki/Samy_(computer_worm)) sur MySpace (oui, je suis vieux), grâce au code que Samy Kamkar a pu injecter dans sa propre page de profil. Ne retournez aucune entrée directement sur votre site sans une validation ou un nettoyage approfondi.

Pour quelques conseils supplémentaires sur la lutte contre les attaques par injection, consultez la [feuille de triche de prévention des injections OWASP](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Injection_Prevention_Cheat_Sheet.md).

## Méfiez-vous des champs cachés

Ajouter `type="hidden"` est un moyen tentant et pratique de cacher des données sensibles dans les pages et les formulaires, mais malheureusement pas un moyen efficace. 

Avec des outils comme [ZapProxy](https://www.zaproxy.org/) et même des outils d'inspection dans les navigateurs web ordinaires, les utilisateurs peuvent facilement cliquer pour révéler des morceaux savoureux d'informations invisibles. 

Cacher des cases à cocher peut être une astuce pratique pour créer des interrupteurs CSS uniquement, mais les champs cachés contribuent peu à la sécurité.

## Considérez soigneusement les champs de remplissage automatique

Lorsque un utilisateur choisit de vous donner ses [informations personnellement identifiables](https://en.wikipedia.org/wiki/Personal_data) (PII), cela devrait être un choix conscient. Les champs de formulaire de remplissage automatique peuvent être pratiques - pour les utilisateurs et les attaquants. [Les exploits utilisant des champs cachés peuvent récolter des PII](https://freedom-to-tinker.com/2017/12/27/no-boundaries-for-user-identities-web-trackers-exploit-browser-login-managers/) précédemment capturées par un champ de remplissage automatique.

De nombreux utilisateurs ne sont même pas conscients des informations que leur navigateur a stockées pour le remplissage automatique. Utilisez ces champs avec parcimonie, et désactivez les formulaires de remplissage automatique pour les données particulièrement sensibles.

Il est également important de peser votre profil de risque contre ses compromis. Si votre projet doit être conforme à [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/), la désactivation du remplissage automatique peut rompre votre entrée pour différentes modalités. Pour plus d'informations, voir [1.3.5 : Identifier le but de l'entrée dans WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/identify-input-purpose.html).

## Gardez les erreurs génériques

Bien qu'il puisse sembler utile de faire savoir aux utilisateurs si une donnée existe, cela est également très utile pour les attaquants. Lorsque vous traitez des comptes, des emails et des PII, il est plus sécurisé de faire une erreur (?) du côté de la prudence. Au lieu de retourner « Votre mot de passe pour ce compte est incorrect », essayez le retour plus ambigu « Informations de connexion incorrectes », et évitez de révéler si le nom d'utilisateur ou l'email est dans le système.

Afin d'être plus utile, fournissez un moyen visible de contacter un humain en cas d'erreur. Évitez de révéler des informations qui ne sont pas nécessaires. Si rien d'autre, pour l'amour du ciel, ne suggérez pas de données qui sont proches de l'entrée utilisateur.

## Soyez un méchant

Lorsque vous considérez la sécurité, il est utile de faire un pas en arrière, d'observer les informations affichées et de vous demander comment un attaquant malveillant pourrait les utiliser. Jouez l'avocat du diable. Si un méchant voyait cette page, quelles nouvelles informations obtiendrait-il ? La vue montre-t-elle des PII ?

Demandez-vous si tout ce qui se trouve sur la page est réellement nécessaire pour un utilisateur authentique. Si ce n'est pas le cas, rédigez ou supprimez-le. Moins c'est plus sûr.

## La sécurité commence à la porte d'entrée

De nos jours, il y a beaucoup plus de chevauchement entre le codage sur le front-end et le back-end. Pour créer une application bien équilibrée et sécurisée, il est utile d'avoir une compréhension générale des moyens par lesquels les attaquants peuvent mettre le pied dans la porte d'entrée.