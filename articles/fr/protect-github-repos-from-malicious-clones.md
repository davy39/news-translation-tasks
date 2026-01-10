---
title: Comment protéger vos dépôts GitHub contre les clones malveillants
subtitle: ''
author: brooklyn
co_authors: []
series: null
date: '2025-07-16T21:14:33.886Z'
originalURL: https://freecodecamp.org/news/protect-github-repos-from-malicious-clones
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752700407765/5fe06816-3d3a-40e4-8a4e-5cfe96a22368.png
tags:
- name: repo confusion
  slug: repo-confusion
- name: repository confusion
  slug: repository-confusion
- name: fake repos
  slug: fake-repos
- name: GitHub
  slug: github
- name: clone
  slug: clone
- name: Security
  slug: security
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: Malware
  slug: malware
- name: Supply Chain Attack
  slug: supply-chain-attack
- name: malicious
  slug: malicious
- name: checklist
  slug: checklist
- name: phishing
  slug: phishing
- name: infostealer
  slug: infostealer
- name: Prevention
  slug: prevention
- name: best practices
  slug: best-practices
seo_title: Comment protéger vos dépôts GitHub contre les clones malveillants
seo_desc: 'The world of open-source development comes with various cyber threats.
  GitHub is still facing a type of attack that is ongoing since last year where attackers
  mirrored a huge number of repositories. So as it turns out…the clone wars are not
  over!

  If ...'
---

Le monde du développement open-source comporte diverses menaces cyber. GitHub fait toujours face à un type d'attaque en cours depuis l'année dernière où des attaquants ont miroiré un grand nombre de dépôts. Il s'avère donc que... les guerres des clones ne sont pas terminées !

Si vous n'avez pas entendu parler de ce qui se passe :

> GitHub lutte pour contenir une attaque en cours qui inonde le site avec des millions de dépôts de code. Ces dépôts contiennent des logiciels malveillants obfusqués qui volent des mots de passe et des cryptomonnaies depuis les appareils des développeurs. [...] Le résultat est des millions de forks avec des noms identiques à l'original.
> 
> – Dan Goodin, [Ars technica](https://arstechnica.com/security/2024/02/github-besieged-by-millions-of-malicious-repositories-in-ongoing-attack/)

Parce que les moteurs de recherche et les classements de recherche de GitHub favorisent l'activité récente, ces dépôts clonés apparaissent souvent en haut des résultats – puis ils attirent des développeurs insoupçonnés à télécharger du code qui peut contenir des logiciels malveillants.

Un de mes [dépôts](http://github.com/brooks-code/miniature-fortnight) a été ciblé par une telle attaque, ce qui m'a incité à le surveiller de près. Ce guide offre des conseils pour repérer les clones de dépôts malveillants avant qu'ils ne vous prennent au dépourvu.

## **Table des matières**

1. [Qu'est-ce qu'une attaque de confusion de dépôt ?](#heading-qu-est-ce-qu-une-attaque-de-confusion-de-depot)
    
    * [Attaques de la chaîne d'approvisionnement](#heading-attaques-de-la-chaine-d-approvisionnement)
        
2. [🛡️ Stratégies de base pour atténuer les risques](#heading-strategies-de-base-pour-attenuation)
    
    * [Vérifier les profils des contributeurs](#heading-verifier-les-profils-des-contributeurs)
        
    * [Rechercher des dépôts clonés](#heading-rechercher-des-depots-clones)
        
    * [Examiner le modèle de commit](#heading-examiner-le-modele-de-commit)
        
    * [Examiner l'historique des commits](#heading-examiner-l-historique-des-commits)
        
    * [Examiner le contenu des commits](#heading-examiner-le-contenu-des-commits)
        
    * [Comparer les fichiers concernés](#heading-comparer-les-fichiers-concernes)
        
    * [Quelques informations sur le logiciel malveillant](#heading-quelques-informations-sur-le-logiciel-malveillant)
        
3. [Temps d'action](#heading-temps-d-action)
    
4. [Conclusion](#heading-conclusion)
    
5. [Plus de ressources](#heading-plus-de-ressources)
    

## **Qu'est-ce qu'une attaque de confusion de dépôt ?**

Une attaque de confusion de dépôt implique :

* Le clonage de dépôts légitimes.
    
* L'injection de code malveillant dans le clone.
    
* Le téléchargement du clone.
    
* La propagation par divers acteurs non avertis.
    

### **Attaques de la chaîne d'approvisionnement**

Si vous recherchez la confusion de dépôt sur Internet, vous découvrirez qu'il s'agit d'un type d'*attaque de la chaîne d'approvisionnement*.

Une attaque de la chaîne d'approvisionnement est une menace *indirecte* où les pirates tentent d'infiltrer un système en ciblant un tiers de confiance ou un composant logiciel, plutôt que d'attaquer directement la cible principale.

Ce n'est pas la première fois que cela se produit. Avant que GitHub ne soit ciblé, PyPI a été attaqué en 2023 avec des [paquets falsifiés](https://arstechnica.com/information-technology/2023/01/more-malicious-packages-posted-to-online-repository-this-time-its-pypi/) se faisant passer pour légitimes. Ces paquets ont attiré des utilisateurs négligents de pip à télécharger des charges utiles malveillantes (contenant dans la plupart des cas des [logiciels malveillants de type infostealer](https://fr.wikipedia.org/wiki/Infostealer)).

## **🛡️ Stratégies de base pour atténuer les risques**

**Avant** d'utiliser un dépôt, assurez-vous de suivre ces étapes et de prendre ces précautions.

### **Vérifier les profils des contributeurs**

C'est une première vérification : si vous voyez un profil GitHub plutôt vide – un profil sans réputation qui contient un seul dépôt mais avec beaucoup de commits quotidiens – eh bien, c'est un peu suspect.

Dans le dépôt falsifié, l'auteur original sera également listé comme contributeur. Vérifiez ce profil. Vous devriez pouvoir trouver le dépôt légitime et faire quelques comparaisons.

![Capture d'écran GitHub des contributeurs d'un dépôt](https://cdn.hashnode.com/res/hashnode/image/upload/v1752335573817/c39aca11-2605-47a2-8a6b-aded16547783.png align="left")

Sur la capture d'écran ci-dessus, vous pouvez voir solotech143, mon double maléfique *(il a été supprimé depuis)*.

### **Rechercher des dépôts clonés**

Vous pouvez effectuer une recherche GitHub par nom de dépôt et trier les résultats par les plus récents en premier. Les dépôts malveillants tendent à apparaître en haut des résultats de recherche car ils sont mis à jour plus fréquemment. Le dépôt original peut être caché plus profondément dans les résultats de recherche.

![Résultats de recherche de clones GitHub.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752335785307/943c6dd3-aa28-4d72-b63a-65736de06dcf.png align="left")

C'est comme des guerres de clones.

**C'est là que c'est dangereux :** les utilisateurs cliquent généralement sur les premiers résultats de recherche, et dans ce type d'attaque, vous êtes presque sûr de voir le faux dépôt de l'attaquant en haut des résultats. L'attaquant y parvient en donnant au faux dépôt des commits frais réguliers (et parfois même quelques étoiles !).

Dans mon cas, le dépôt original est une soumission pour le concours HackaViz 2025. Les hackathons offrent une bonne surface d'attaque car, au-delà du fait qu'ils attirent des communautés de niche, ils sont également sensibles au temps.

Maintenant, avançons d'un an et imaginons que Hackaviz 2026 commence bientôt. L'attaquant a facilement dépassé la soumission originale intacte. Quel dépôt est le plus susceptible d'être visité lorsque les futurs concurrents – ignorant l'escroquerie – chercheront les soumissions précédentes ?

### **Examiner le modèle de commit**

Voici où les choses prennent un tournant étrange. Les clones malveillants sont gérés par des agents automatisés, donc l'historique des commits suit un modèle plutôt inhabituel pour un humain. Bien sûr, vous pouvez automatiser pour de nombreuses raisons légitimes, mais... cela suivra toujours un objectif clair et il y aura toujours une touche humaine à un moment donné. Dans ce cas, les commits ne s'additionnent pas.

Voyons à quoi cela ressemble dans les captures d'écran ci-dessous :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1752335872381/1238dee9-3568-4d2b-88bb-f63258ffb045.png align="left")

Régulier comme une horloge...

![Une capture d'écran GitHub d'une activité de contribution très active..](https://cdn.hashnode.com/res/hashnode/image/upload/v1752335891381/77f835fe-cccf-409f-85d7-789f918d4aa3.png align="left")

... et hyperactive !

### **Examiner l'historique des commits**

Vous ne pouvez pas ! Et c'est la partie étrange. Vous ne pouvez voir que le dernier et le premier commit. Alors pourquoi cache-t-il tous les autres ? Aimez-vous quand quelqu'un vous cache des choses ?

![Une capture d'écran de l'historique des commits GitHub pour une journée.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752336385127/6274dd87-0a97-4c38-8849-9d547b9edb22.png align="left")

Pour le 10 juillet, nous devrions pouvoir voir 11 commits, où sont les dix autres ?

![Une capture d'écran de l'historique des commits GitHub pour une période entière.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752336355084/4c7c343d-2000-4359-ae98-dcc98fb08732.png align="left")

Eh bien, vous ne pouvez vérifier que le premier et le dernier commit. Ce n'est pas beaucoup pour un dépôt qui a plus de 2000 commits enregistrés.

### **Examiner le contenu des commits**

Eh bien, puisque je peux toujours vérifier le dernier commit, j'en ai vérifié quelques-uns. Ils partagent le même modèle : le bot modifie constamment le fichier README en effectuant les mêmes modifications. Comme vous pouvez le voir dans la capture d'écran ci-dessous, il met à jour le fichier avec des liens vers une version infectée.

![Une capture d'écran GitHub des commits vers un dépôt malveillant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752336493881/e8b57b4c-4d13-44f8-bca6-bd8fbad2738c.png align="left")

Au-dessus, vous pouvez voir un agent IA coincé dans la boucle de changement du Readme.

Les modifications humaines sont plus variées. Dans un projet piloté par des humains, vous verrez un large mélange de commits : commits de fonctionnalités, expériences exploratoires, corrections de bugs, ajustements de style, et parfois des annulations. Un clone bot va souvent simplement écraser des fichiers, augmenter des versions, ou réinjecter la même charge utile malveillante à plusieurs reprises sans réelle contribution au code.

### **Comparer les fichiers concernés**

C'est là que le bon sens est utile. Donc, vous avez deux README :

1. Le [premier](https://web.archive.org/web/20250711182419/https://github.com/solotech143/miniature-fortnight/blob/main/README.md) consiste en un contenu généré par IA, encombré d'emojis et d'informations de faible valeur. Il est conçu uniquement pour vous inciter à cliquer sur le lien de téléchargement de la version.
    
2. L'[autre](https://github.com/brooks-code/miniature-fortnight/blob/main/README.md) suit les [meilleures pratiques](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/) pour créer un bon fichier README. Il est précis et bien structuré et fonctionne comme un aide précieux et un explicateur du code. Il aborde également en profondeur les aspects les plus importants du projet. C'est généralement un bon signe qu'un dépôt est organique et authentique.
    

### **Quelques informations sur le logiciel malveillant**

Que savons-nous jusqu'à présent ? Eh bien, un lien suspect dans un fichier README généré par IA, qui est cohérent avec un modèle très suspect dans l'historique des commits.

Maintenant, examinons de plus près cette version douteuse et voyons ce qu'un scanner antivirus en ligne pourrait révéler à son sujet.

![Une capture d'écran GitHub des commits vers un dépôt malveillant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752336589656/124aecf2-39e9-4158-9a06-f0fd59cbf8c1.png align="left")

Le logiciel malveillant est emballé uniquement dans la version miniature-fortnight-v1.7.6.zip.

![Résultat d'une analyse de logiciel malveillant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752336609780/7eaf7fc8-73f2-4d9d-b169-1d5c50ce84f2.png align="left")

Au-dessus, vous pouvez voir le résultat d'un scan avec un scanner en ligne.

Le fichier .zip contient **uniquement** quatre fichiers :

* config.txt
    
* launch.bat
    
* lua51.dll
    
* luajit.exe
    

Ces fichiers sont **totalement sans rapport** avec le projet source (un projet de science des données Python avec des notebooks Jupyter combinés à une application React utilisant three.js).

Je ne vais pas entrer dans les détails dans cet article. Mais pour les curieux, il s'agit d'un logiciel malveillant de type infostealer (un logiciel malveillant qui exfiltrera vos identifiants et d'autres informations précieuses sur votre configuration) similaire à celui décrit en [détail ici](https://www.trendmicro.com/en_us/research/25/c/ai-assisted-fake-github-repositories.html#).

## **Temps d'action**

Si vous découvrez un dépôt potentiellement malveillant, voici quelques étapes que vous pouvez suivre :

1. Documenter certaines preuves.
    
2. Avertir les mainteneurs du dépôt original.
    
3. Signaler le clone malveillant à GitHub.
    

Signaler un dépôt ou un profil sur GitHub est facile et rapide. Allez sur la page de profil de l'utilisateur, cliquez sur « Bloquer ou signaler » dans la barre latérale gauche et choisissez « Signaler un abus » dans la fenêtre contextuelle. Vous devrez remplir un court formulaire de contact avec quelques détails sur le comportement avant de soumettre. Si nécessaire, vous pouvez trouver plus d'informations sur [GitHub](https://docs.github.com/fr/communities/maintaining-your-safety-on-github/reporting-abuse-or-spam#reporting-a-user).

## **Conclusion**

Il s'agit d'une description d'une seule attaque, du point de vue de quelqu'un qui a découvert que l'un de ses dépôts avait été ciblé. Il existe probablement des cas d'attaques plus sophistiquées. Mais l'inondation de dépôts clonés que nous pouvons voir sur GitHub est définitivement une automatisation de masse de faible qualité. La quantité plutôt que la qualité. 
Pour être honnête, je suis assez surpris que les algorithmes conçus chez GitHub n'aient pas réussi à repérer celui-ci.

Cela soulève également des questions liées à l'IA.

* Que se passe-t-il lorsque les LLM sont formés sur du contenu malveillant ? C'est une question plus générale sur l'[empoisonnement de l'IA](https://arstechnica.com/information-technology/2024/01/ai-poisoning-could-turn-open-models-into-destructive-sleeper-agents-says-anthropic/).
    
* Un humain pourrait facilement repérer les modèles et le contenu de faible qualité *pour l'instant*. Mais...
    
    * Imaginez que vous utilisez des agents de codage, beaucoup d'entre eux. Les agents choisiront-ils le clone malveillant au lieu de l'original ? Comment distinguer les dépôts du point de vue d'un automate ?
        
    * Les attaquants **vont** affiner leurs tactiques, rendant les clones plus humains et nous attirant ainsi plus facilement dans leurs pièges.
        
* C'est vraiment une situation qui me fait réfléchir aux premiers jours de Google. À l'époque, l'entreprise devait lutter contre d'énormes quantités de spam dues au bourrage de mots-clés et aux tactiques de SEO manipulatoires. Les grandes entreprises technologiques devront-elles passer par un moment de [mise à jour Florida](https://fr.wikipedia.org/wiki/Timeline_of_Google_Search#Full_timeline) pour faire face à la montée du spam généré par l'IA ?
    

## **Plus de ressources**

* [Une description détaillée de l'attaque](https://www.trendmicro.com/en_be/research/23/j/infection-techniques-across-supply-chains-and-codebases.html)
    
* [Recommandations de sécurité complètes](https://www.cisa.gov/sites/default/files/publications/ESF_SECURING_THE_SOFTWARE_SUPPLY_CHAIN_DEVELOPERS.PDF)
    

**Restez informé, restez en sécurité !**

Une **feuille de triche** est également disponible sur mon [GitHub](https://github.com/brooks-code/repo-confusion-guard). N'hésitez pas à y contribuer !