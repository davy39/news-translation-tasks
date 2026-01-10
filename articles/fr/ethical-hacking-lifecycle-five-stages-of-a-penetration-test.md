---
title: Le cycle du piratage éthique — Cinq étapes d'un test de pénétration
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-09T20:34:06.000Z'
originalURL: https://freecodecamp.org/news/ethical-hacking-lifecycle-five-stages-of-a-penetration-test
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/hacking.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: penetration testing
  slug: penetration-testing
seo_title: Le cycle du piratage éthique — Cinq étapes d'un test de pénétration
seo_desc: "Penetration testing is the process of exploiting an organization’s network\
  \ in order to figure out how defend it better. \nIn this article, we'll discuss\
  \ the five steps involved in a successful penetration test.\nBefore we get into\
  \ the article, a quick ..."
---

Le test de pénétration est le processus d'exploitation du réseau d'une organisation afin de déterminer comment le défendre mieux.

Dans cet article, nous discuterons des cinq étapes impliquées dans un test de pénétration réussi.

_Avant de commencer l'article_, un rapide avertissement : _Je tiens à souligner que je ne suis pas responsable des dommages que vous pourriez causer en essayant d'attaquer des systèmes._

Il est _illégal_ de faire un test de pénétration sans permission, alors assurez-vous de l'avoir par écrit _avant même d'essayer de scanner un système ou un réseau._

Cela étant dit, commençons.

## Qu'est-ce que la cybersécurité ?

La cybersécurité est l'un des domaines les plus en vogue, grâce à tant d'entreprises passant au télétravail. Les menaces cybernétiques augmentent et les cybercriminels trouvent de nouvelles façons d'exploiter les systèmes.

Le test de pénétration est la manière dont les pirates éthiques travaillent. Ils pensent comme des pirates malveillants et attaquent leurs propres systèmes. Cela les aide à comprendre leurs forces et leurs faiblesses et à protéger les actifs de leur organisation.

Un test de pénétration se compose de plusieurs étapes. Vous ne pouvez pas simplement accéder à un système en utilisant un outil, sauf si la cible est désespérément vulnérable.

Dans la plupart des cas, les systèmes sont sécurisés via des pare-feu, des logiciels antivirus, des configurations par défaut du système d'exploitation, et ainsi de suite. Il faut les bons outils, un ensemble de compétences solides et, surtout, de la patience, afin d'exploiter avec succès un réseau.

Alors, examinons les cinq principales étapes qu'un testeur de pénétration suivra, ainsi que les outils qu'il utilise pour pénétrer un réseau.

Vous pouvez également trouver [l'article que j'ai écrit sur les 10 outils que les professionnels de la cybersécurité utilisent ici](https://www.freecodecamp.org/news/10-tools-you-should-know-as-a-cybersecurity-engineer/).

## Reconnaissance

> "Donnez-moi six heures pour abattre un arbre et je passerai les quatre premières à aiguiser la hache." — Abraham Lincoln

La reconnaissance est la partie la plus importante d'un test de pénétration. C'est là que vous obtenez des informations sur la cible.

La reconnaissance est importante car plus vous avez d'informations sur la cible, plus il est facile d'obtenir un accès. Une fois que vous avez cartographié un réseau entier, vous pouvez identifier le point le plus faible et commencer par là.

Les outils de reconnaissance couramment utilisés incluent [Google (oui !)](https://en.wikipedia.org/wiki/Google_hacking) et les sites de médias sociaux où vous pouvez recueillir des informations sur la cible. Si vous effectuez un audit d'une entreprise, vous pouvez consulter les offres d'emploi de l'entreprise pour voir le type de technologies qu'ils utilisent.

Une fois que vous avez obtenu suffisamment d'informations, vous pouvez utiliser un outil comme [Maltego](https://www.maltego.com/) pour cartographier les cibles.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/maltego.jpg)
_Maltego_

Maltego supporte également la capacité d'importer automatiquement des données à partir des réseaux sociaux, des enregistrements DNS et des plugins personnalisés comme [FullContact](https://www.fullcontact.com/).

L'important à retenir en termes de reconnaissance est que vous ne touchez JAMAIS la cible. La reconnaissance est similaire à l'éclairage et à la recherche d'informations alors que vous êtes loin de la cible.

## Scanning

C'est la partie où vous entrez en contact avec la cible. Le scanning implique l'envoi de paquets de données à la cible et l'interprétation de leur réponse.

Le scanning vous donne des informations utiles sur la cible comme les ports ouverts, les adresses IP, les informations sur le système d'exploitation, les services installés, et ainsi de suite.

[Nmap est le meilleur scanner pour scanner un réseau](https://medium.com/manishmshiva/nmap-a-guide-to-the-greatest-scanning-tool-of-all-time-3bd1a973a5e5). Il vous aidera à cartographier le réseau et à fournir des informations détaillées sur les systèmes cibles.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/nmap.png)
_Nmap_

Nmap propose également un certain nombre d'options CLI, y compris des exports de scan que vous pouvez ensuite importer dans des outils d'exploitation.

[Nessus](https://en.wikipedia.org/wiki/Nessus_(software)) est un autre outil de scanning, mais il s'agit d'un produit commercial. Alors que Nmap vous donnera des informations sur la cible, Nessus vous dira comment vous pouvez exploiter la cible en faisant correspondre les vulnérabilités de la base de données [Common Vulnerabilities and Exposures](https://www.exploit-db.com/).

[OpenVas](https://www.openvas.org/) est une autre alternative open-source similaire à Nessus.

## Exploitation

C'est la partie où vous obtenez un accès au système. Une exploitation réussie devrait vous donner le contrôle du système au moins au niveau utilisateur. À partir de là, vous effectuez une [élévation de privilèges](https://searchsecurity.techtarget.com/definition/privilege-escalation-attack) pour obtenir un accès root à la cible.

En matière d'exploitation, [Metasploit est de loin le meilleur outil sur le marché](https://medium.com/manishmshiva/metasploit-a-walkthrough-of-the-powerful-exploitation-framework-6974c4ed0ea7). Il est open-source (avec une version commerciale également) et est facile à utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/metasploit.png)
_Metasploit_

Metasploit est fréquemment mis à jour avec de nouvelles exploits publiées dans la base de données Common Vulnerabilities and Exposures (CVE). Vous pouvez donc faire correspondre vos résultats de scan avec les exploits disponibles et utiliser cet exploit de Metasploit pour attaquer la cible.

Metasploit dispose d'une charge utile avancée appelée [Meterpreter](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/). Une fois que vous avez obtenu un accès au système cible, Meterpreter vous donne des options comme l'ouverture de webcams, le vidage des hachages de mots de passe, et ainsi de suite. Meterpreter vit également dans la mémoire de la cible, ce qui le rend très difficile à détecter.

Par exemple, si vos résultats de scan vous indiquent que la cible a la version 3.5 de Samba, vous pouvez utiliser la [Vulnérabilité d'exécution de code à distance Samba CVE-2017-7494](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7494) pour envoyer une charge utile via Metasploit et obtenir un accès au système cible.

Metasploit dispose également d'un outil GUI appelé Armitage. Armitage vous aide à visualiser les cibles et recommande des exploits en faisant correspondre les vulnérabilités avec la base de données des exploits.

## Maintenir l'accès

Obtenir un accès aux systèmes n'est pas facile, surtout sur les réseaux d'entreprise. Après tout le travail acharné que vous avez fait pour exploiter un système, il ne serait pas logique de passer par le même processus pour exploiter la cible à nouveau.

C'est là que le maintien de l'accès intervient. Vous pouvez installer des portes dérobées, des keyloggers et d'autres morceaux de code qui vous permettent d'accéder au système chaque fois que vous le souhaitez.

Metasploit vous donne des outils comme des keyloggers et des portes dérobées Meterpreter pour maintenir l'accès à un système exploité. Vous pouvez également installer des [Rootkits](https://www.veracode.com/security/rootkit) ou des chevaux de Troie personnalisés après avoir obtenu un accès.

Un rootkit est un morceau de code qui permet à l'attaquant d'avoir un accès administrateur au système auquel il est attaché. Les rootkits peuvent également être installés lorsque vous téléchargez des fichiers à partir de sites web malveillants.

Les chevaux de Troie sont des logiciels qui semblent être des logiciels utiles (par exemple, Adobe Photoshop) mais peuvent contenir un morceau caché de logiciel malveillant. Cela est courant parmi les logiciels piratés où les attaquants intègrent des chevaux de Troie dans des logiciels populaires comme MS Office.

## Rapport

Le rapport est la partie finale d'un test de pénétration. C'est ce qui différencie un attaquant d'un pirate éthique.

Une fois votre test de pénétration terminé, vous résumez toutes les étapes que vous avez suivies, de la reconnaissance à l'obtention de l'accès. Cela aidera l'organisation à comprendre son architecture de sécurité et à mieux se défendre.

Un rapport est également utile lorsque vous travaillez en équipe. Vous ne pourrez pas mener un test de pénétration pour une grande organisation seul. Les rapports aident également le client à comprendre les efforts de l'équipe et à justifier la rémunération.

[Voici un exemple de rapport créé après un test de pénétration réussi](https://www.offensive-security.com/reports/sample-penetration-testing-report.pdf).

## Résumé

La cybersécurité est un excellent choix de carrière, surtout en ces temps incertains. De plus en plus d'appareils sont exposés au réseau chaque jour. C'est le travail du testeur de pénétration d'aider à défendre le réseau d'une organisation.

J'espère que cet article vous a aidé à comprendre les différentes étapes d'un test de pénétration. Pour en savoir plus sur le piratage éthique ou l'intelligence artificielle, [vous pouvez visiter mon blog](https://medium.com/manishmshiva).