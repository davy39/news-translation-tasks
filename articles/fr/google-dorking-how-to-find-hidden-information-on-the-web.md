---
title: 'Google Dorking : Comment trouver des informations cachées sur le Web'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-10-25T19:37:41.468Z'
originalURL: https://freecodecamp.org/news/google-dorking-how-to-find-hidden-information-on-the-web
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729872503418/1e5921bc-52ba-4410-86a3-5e96a2c22405.jpeg
tags:
- name: Web Security
  slug: web-security
- name: ethicalhacking
  slug: ethicalhacking
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: 'Google Dorking : Comment trouver des informations cachées sur le Web'
seo_desc: 'Let’s learn how to find hidden information online by using advanced search
  operators on Google.

  The internet holds vast amounts of information. Much of this information is accessible
  through Google.

  But did you know you can use Google in ways beyond ...'
---

Apprenons à trouver des informations cachées en ligne en utilisant des opérateurs de recherche avancés sur Google.

Internet contient une quantité immense d'informations. Une grande partie de ces informations est accessible via Google.

Mais saviez-vous que vous pouvez utiliser Google de manières qui vont au-delà des simples recherches ? Il existe une méthode appelée « Google Dorking » qui vous permet de faire cela.

Le Google Dorking vous aide à trouver des données cachées ou négligées sur les sites web. Il utilise des opérateurs de recherche avancés pour localiser des fichiers cachés, des données sensibles, et plus encore.

Le Google Dorking nous permet d'être très spécifiques dans nos recherches. Au lieu de simplement taper des mots-clés ordinaires, nous les combinons avec des opérateurs. Ces opérateurs aident Google à affiner ses résultats de recherche.

Avant de plonger dans le sujet, un mot d'avertissement. Bien que le Google Dorking puisse être un outil puissant pour la recherche ou les tests de cybersécurité, il comporte également certains risques. L'utiliser pour accéder sans autorisation à des informations sécurisées est illégal. Alors utilisez-le de manière sûre et correcte !

Maintenant, apprenons à « dorker » Google.

# **Opérateurs de Google Dorking**

Voici une liste de tous les opérateurs courants de Google Dorking ainsi que leur utilité.

### **Site**

Restreint les résultats de recherche à un domaine ou un site web spécifique. Exemple : `site:`[`example.com`](http://example.com) affichera les résultats uniquement de ce site.

### **InTitle**

Recherche des pages avec un mot ou une phrase spécifique dans le titre de la page. Exemple : `intitle:login` trouvera des pages avec "login" dans le titre.

![Résultats InTitle](https://cdn.hashnode.com/res/hashnode/image/upload/v1729872545025/c2c88f8b-d14c-4da4-91f5-78ea9d87fb48.jpeg align="center")

### **InURL**

L'opérateur `inurl` est utilisé pour trouver des mots spécifiques dans la structure de l'URL des pages web. Il peut aider à localiser des pages avec des mots-clés particuliers intégrés dans leur adresse web.

Par exemple, utiliser `inurl:login` avec d'autres termes comme `inurl:customer` ou `inurl:secure` peut révéler des pages de connexion pour différents sites.

Un exemple de son utilisation est `inurl:`[`admin`](http://admin.It). Cela affiche les URL contenant "admin", menant souvent à des pages administratives ou de gestion.

Pour des recherches plus avancées, `inurl:pho?id=` peut être utile pour identifier des sites qui pourraient être vulnérables aux injections SQL. Les URL structurées de cette manière incluent souvent des chaînes de requêtes de base de données.

### **FileType**

L'opérateur `filetype` permet aux utilisateurs de rechercher des documents avec une extension de fichier spécifique. Cela inclut des extensions comme PDF, DOC ou XLS.

L'opérateur `filetype` est utile pour localiser des rapports, des présentations et des documents publics. Par exemple, `filetype:pdf financial report` trouve des fichiers PDF liés aux rapports financiers.

En combinant `filetype` avec certains mots-clés, on peut effectuer des recherches plus ciblées. Par exemple, rechercher `filetype:xlsx budget` pourrait trouver des fichiers Excel liés aux détails budgétaires.

`filetype:docx confidential` pourrait révéler des documents DOCX contenant des termes potentiellement sensibles comme "confidential", menant à des fichiers à usage interne qui pourraient être accessibles publiquement.

### **Cache**

Affiche la version mise en cache par Google d'une page web, même si elle a été supprimée. Exemple : `cache:`[`example.com`](http://example.com) montre la version mise en cache de cette page.

### **AllInText**

Recherche des pages qui contiennent tous les mots spécifiés dans le texte principal. Exemple : `allintext:"username password"` retournera des pages avec les deux mots dans le texte.

![Résultats All in text](https://cdn.hashnode.com/res/hashnode/image/upload/v1729872601325/87fbbd02-d5b0-43c0-9893-cef035927711.jpeg align="center")

### **AllInTitle**

Recherche des pages avec tous les mots spécifiés dans le titre. Exemple : `allintitle:login admin` trouve des pages avec les deux mots dans le titre.

### **AllInUrl**

Recherche des pages avec plusieurs mots spécifiés dans l'URL. Exemple : `allinurl:admin login` trouve des URL qui contiennent à la fois "admin" et "login".

### **InAnchor**

Trouve des pages avec un texte spécifique dans les liens d'ancrage (le texte cliquable d'un lien). Exemple : `inanchor:"click here"` trouve des liens où le texte cliquable est "click here".

### **Before et After**

Trouve des pages publiées avant ou après une date spécifique. Exemple : `before:2020` trouvera des pages publiées avant 2020. `after:2020` trouvera des pages publiées après 2020.

![Résultats Before and after](https://cdn.hashnode.com/res/hashnode/image/upload/v1729872642187/5e3a17ca-c428-4711-82d8-c904182d1d58.jpeg align="center")

### **OR**

Combine deux termes de recherche et retourne des résultats contenant l'un ou l'autre. Exemple : `admin OR login` affiche des pages avec soit "admin", soit "login".

### **Moins (-)**

Exclut des mots spécifiques des résultats de recherche. Exemple : `admin -login` affiche des pages avec "admin" mais sans "login".

### **Astérisque (*)**

Agit comme un joker pour substituer n'importe quel mot ou phrase. Exemple : `"admin * login"` trouvera des pages avec n'importe quel mot entre "admin" et "login".

### **InText**

Recherche des mots spécifiques dans le corps principal de la page, pas seulement dans les titres ou les URL. Exemple : `intext:"confidential"` trouve des pages où "confidential" apparaît dans le contenu.

### **Location**

Restreint les résultats à une localisation géographique spécifique. Exemple : `location:USA` affiche des résultats centrés sur les États-Unis.

## **Comment se protéger du Google Dorking**

Si vous possédez un site web ou gérez des informations sensibles en ligne, comprendre le Google Dorking peut vous aider à sécuriser vos données. Voici quelques étapes que vous pouvez suivre pour vous protéger :

1. **Utiliser des fichiers Robots.txt** Le fichier robots.txt sur un site web indique aux moteurs de recherche quel contenu ils ne doivent pas indexer. Assurez-vous que les pages web ou fichiers sensibles sont protégés contre l'indexation par Google.

2. **Utiliser une protection par mot de passe** Si certaines parties de votre site web sont sensibles, utilisez une protection par mot de passe. Google ne peut pas accéder au contenu protégé par mot de passe, donc il n'apparaîtra pas dans les résultats de recherche.

3. **Éviter de stocker des fichiers sensibles publiquement** Ne stockez pas d'informations sensibles comme des sauvegardes de bases de données, des fichiers de configuration ou des listes d'emails sur des parties publiquement accessibles de votre serveur.

4. **Vérifier régulièrement les informations exposées** Utilisez vos propres recherches Google Dorking pour voir si des fichiers sensibles apparaissent sur Google. Cela peut vous aider à détecter et sécuriser les informations avant que quelqu'un d'autre ne les trouve.

5. **Utiliser des scanners de vulnérabilités web** Des outils comme OWASP ZAP ou Burp Suite peuvent vous aider à scanner votre propre site pour détecter les données exposées. Ces outils peuvent repérer des choses que vous pourriez manquer manuellement.

## **Conclusion**

Le Google Dorking peut être à la fois utile et dangereux, selon la manière dont vous l'utilisez. D'une part, il vous permet de découvrir des informations cachées et d'affiner vos compétences de recherche. D'autre part, il peut exposer des données sensibles s'il est utilisé de manière irresponsable.

Comprendre les techniques du Google Dorking peut faire de vous un meilleur utilisateur d'Internet et vous aider à sécuriser vos propres données.

Pour apprendre à pirater des machines dans le monde réel, rejoignez notre communauté privée [Hacker's Hub.](https://www.skool.com/hackershub)