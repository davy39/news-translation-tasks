---
title: EternalBlue Expliqué – Une Analyse Approfondie de la Célèbre Faille Windows
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-09-11T08:31:41.000Z'
originalURL: https://freecodecamp.org/news/eternalblue-explained-an-analysis-of-the-windows-flaw
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/eternalblue.png
tags:
- name: cybersecurity
  slug: cybersecurity
seo_title: EternalBlue Expliqué – Une Analyse Approfondie de la Célèbre Faille Windows
seo_desc: 'The world of cybersecurity never ceases to amaze us with its capacity for
  innovation and ingenuity.

  It also continually surprises us with unforeseen vulnerabilities. In the list of
  famous flaws, the EternalBlue vulnerability takes a special place.

  It...'
---

Le monde de la cybersécurité ne cesse de nous émerveiller par sa capacité d'innovation et d'ingéniosité.

Il nous surprend également par des vulnérabilités imprévues. Dans la liste des failles célèbres, la vulnérabilité EternalBlue occupe une place spéciale.

Ce n'est pas seulement son impact sur les systèmes mondiaux qui la rend remarquable, mais aussi la faiblesse sous-jacente de conception qui a permis une telle catastrophe.

## Qu'est-ce qu'EternalBlue ?

EternalBlue est une vulnérabilité logicielle dans le système d'exploitation Windows de Microsoft. Elle cible le protocole Server Message Block (SMB) de Windows, un protocole réseau qui permet l'accès partagé aux fichiers, imprimantes et autres ressources au sein d'un réseau.

L'Agence de Sécurité Nationale des États-Unis (NSA) a découvert cette vulnérabilité, et elle faisait partie de leur boîte à outils secrète. Elle est devenue publique lorsque le groupe de hackers Shadow Brokers a divulgué les outils de la NSA en avril 2017.

## Comprendre la Vulnérabilité

Pour saisir le cœur de la vulnérabilité EternalBlue, nous devons comprendre le protocole SMB. Il repose sur le port 445 pour permettre les communications réseau, et c'est là que réside la faille.

1. **Le Bug dans SMBv1 :** Le problème principal réside dans le traitement des paquets spécialement conçus par le protocole SMBv1. En envoyant des requêtes spécifiques à un serveur Windows exécutant SMBv1, un attaquant distant peut exécuter du code arbitraire sur le système cible.
2. **DoublePulsar :** Accompagnant EternalBlue, DoublePulsar est un outil d'implantation de porte dérobée. Une fois qu'EternalBlue ouvre la voie, DoublePulsar aide à injecter et exécuter du code malveillant sur un système cible.
3. **Manque de Segmentation :** La nature de SMB permet un mouvement latéral au sein du réseau. Elle permet à un attaquant de propager le logiciel malveillant d'un système à un autre. Cela signifie qu'une fois à l'intérieur, le logiciel malveillant pourrait se propager à travers un réseau entier s'il n'est pas correctement segmenté.

## Pourquoi Était-elle Si Critique ?

EternalBlue est devenue un sujet de grave préoccupation pour plusieurs raisons :

1. **Popularité de Windows :** Avec Windows étant le système d'exploitation le plus répandu au monde, une faille dans celui-ci met un grand nombre de systèmes en danger.
2. **Difficulté de Correction :** Bien que Microsoft ait publié des correctifs pour cette vulnérabilité, de nombreuses organisations ont été lentes à les implémenter ou utilisaient des versions obsolètes de Windows qui n'étaient plus supportées.
3. **Nature Weaponisée :** La sophistication de l'exploit le rendait extrêmement puissant. En tant que partie de la boîte à outils de la NSA, il était conçu pour l'espionnage, et non pour des activités cybercriminelles courantes.

## Découverte et Fuite

La NSA aurait découvert la vulnérabilité mais l'a gardée secrète comme partie de leur arsenal pour une utilisation potentielle. Malheureusement, ce secret n'est pas resté tel bien longtemps.

Les Shadow Brokers, un groupe de hackers dont l'identité reste inconnue, ont divulgué une trousse d'outils de la NSA, incluant le code d'exploitation pour EternalBlue, en avril 2017. Cette fuite a rendu le code accessible à quiconque ayant les connaissances pour l'utiliser.

Microsoft a publié un correctif pour la vulnérabilité (MS17-010) en mars 2017, avant la fuite. Cependant, de nombreux systèmes sont restés non corrigés, conduisant à une exploitation généralisée.

## Exploitation et Utilisation

Bien que l'accent principal ici soit la vulnérabilité elle-même, la série d'attaques déclenchées par EternalBlue ne peut être entièrement ignorée.

L'attaque du [ransomware WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack) a été la plus notoire, affectant plus de 200 000 ordinateurs dans 150 pays. Ce fut la première à montrer le potentiel destructeur complet d'EternalBlue.

De plus, d'autres logiciels malveillants comme [NotPetya](https://en.wikipedia.org/wiki/Petya_(malware_family)) et [Bad Rabbit](https://www.proofpoint.com/us/threat-reference/bad-rabbit) ont également exploité EternalBlue, causant des dommages substantiels et des pertes financières.

## Atténuation et Prévention

L'importance de traiter cette vulnérabilité ne peut être surestimée. Les organisations et les individus doivent s'assurer qu'ils ont appliqué les correctifs et mises à jour nécessaires pour protéger leurs systèmes.

* **Corrigez votre système :** Appliquez le correctif MS17-010 de Microsoft pour fermer la vulnérabilité.
* **Désactivez SMBv1 :** Si SMBv1 n'est pas requis, le désactiver peut protéger votre système.
* **Mises à jour régulières :** Garder votre système à jour garantit que vous recevez les correctifs de sécurité critiques dès leur publication.

## Leçons Apprises et Avancement

L'histoire d'EternalBlue nous rappelle la nature complexe et fragile de notre écosystème numérique. Voici ce que nous pouvons apprendre :

* **Importance des Correctifs Réguliers :** Garder les logiciels à jour n'est pas seulement une bonne pratique – c'est une nécessité.
* **Segmentation du Réseau :** Une segmentation appropriée peut limiter la propagation des logiciels malveillants au sein du réseau.
* **Responsabilité des Agences Gouvernementales :** La fuite de la NSA a soulevé des questions éthiques sur l'accumulation de vulnérabilités et leurs retombées potentielles.

## Conclusion

EternalBlue est un rappel frappant de l'importance de la vigilance en matière de cybersécurité.

De sa découverte par la NSA à sa fuite par les Shadow Brokers et son exploitation ultérieure par des campagnes de logiciels malveillants, elle souligne la nécessité de mesures de sécurité proactives.

Bien que les attaques exploitant EternalBlue aient causé des dommages substantiels, la vulnérabilité elle-même est la leçon cruciale à en tirer.

C'est une illustration vivante du paysage complexe et évolutif de la cybersécurité et souligne le besoin de surveillance continue, de mises à jour et d'éducation pour rester en avance sur les menaces potentielles.

Si vous avez trouvé cet article utile, visitez [Stealth Security](https://stealthsecurity.io/) pour lire plus d'articles sur le hacking éthique. Vous pouvez également [me contacter sur LinkedIn](https://www.linkedin.com/in/manishmshiva/).