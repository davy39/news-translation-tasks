---
title: Cisco sera-t-il la prochaine victime d'AWS ?
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-07T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/will-cisco-be-the-next-roadkill-for-aws
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/cisco.png
tags:
- name: AWS
  slug: aws
- name: networking
  slug: networking
- name: virtualization
  slug: virtualization
seo_title: Cisco sera-t-il la prochaine victime d'AWS ?
seo_desc: I’m not keeping very close track, but it feels like months since Amazon
  Web Services (AWS) most recently turned a major tech industry upside down. But with
  all their resources and market power, I’m sure there’s always something interesting
  cooking in...
---

Je ne suis pas très attentif, mais il me semble que cela fait des mois qu'Amazon Web Services (AWS) n'a pas bouleversé une grande industrie technologique. Mais avec toutes leurs ressources et leur pouvoir de marché, je suis sûr qu'il y a toujours quelque chose d'intéressant qui se prépare dans les cuisines du siège d'Amazon, où qu'il soit actuellement.

Alors, laissez-moi lancer ma prédiction purement spéculative dans le silence. Comme je le décris dans mon livre [Learn AWS in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&a_bid=1c1b5e27&chan=medium), AWS a joyeusement remplacé votre salle serveur par EC2, votre SAN et NAS par S3, votre entrepôt de données par Redshift, et votre base de données par RDS (et Aurora). Ils ont également inventé des modèles de déploiement entièrement nouveaux : vous informant poliment, par exemple, que vous devez simplement servir vos applications mobiles via des fonctions serverless (Lambda).

Alors, quoi de neuf ? Et bien, pourquoi pas le routage d'entreprise ?

## Qu'est-ce que le routage d'entreprise de nos jours ?

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-18.png)

Pendant des décennies, les grandes organisations ont contrôlé leur trafic réseau interne avec des commutateurs et des routeurs configurés par des systèmes d'exploitation propriétaires. Le matériel est coûteux (un seul appareil peut facilement coûter 10 000 $) et le coût de l'embauche des administrateurs formés nécessaires pour les maintenir peut être beaucoup plus élevé.

Mais tout cela est-il vraiment encore nécessaire ?

De nos jours, vos charges de travail sont plus susceptibles de résider dans le cloud que dans votre bureau réel. Même les appareils Internet des objets en interne peuvent facilement être contrôlés depuis le cloud en utilisant, par exemple, [AWS IoT](https://aws.amazon.com/iot/). Je suppose que la plupart des routages d'entreprise modernes sur site impliquent de contrôler la manière dont les personnes se connectent aux ressources de production et entre elles (e-mail, VOIP, vidéo), mais même cela est de plus en plus susceptible d'être externalisé vers des solutions SaaS.

Je peux manquer quelque chose, mais je ne vois tout simplement pas un cas convaincant pour les commutateurs matériels ici. Le réseau défini par logiciel (SDN) devrait facilement être à la hauteur de la tâche. Pourquoi ne pas simplement couvrir votre campus de points d'accès sans fil, authentifier les utilisateurs en utilisant Kerberos ou Active Directory, et configurer votre chemin vers la perfection des permissions/connectivité.

## Comment AWS peut dominer le monde du routage ?

Ce qui me ramène à AWS. Ils ont déjà couvert toutes les bases pour l'authentification ([AWS Directory Service](https://aws.amazon.com/directoryservice/)) et la connectivité à distance haut de gamme ([AWS Direct Connect](https://aws.amazon.com/directconnect/)). Il ne leur faudrait probablement pas beaucoup pour étendre leurs réseaux à votre campus. Peut-être qu'ils vous permettraient de créer des [VPCs](https://aws.amazon.com/vpc/) locaux, complets avec des sous-réseaux configurables, que vous utiliseriez pour organiser votre infrastructure locale.

J'imagine un administrateur d'entreprise se connectant à la console AWS pour intégrer quelques nouveaux employés du marketing. Ils seraient ajoutés à un groupe AWS IAM "Marketing" qui a déjà accès aux tableaux de bord Amazon QuickSight et aux données de streaming de vos serveurs web publics fonctionnant sur EC2. Mais le groupe pourrait tout aussi facilement être configuré pour permettre à ses membres d'accéder à une base de données qui, pour des raisons réglementaires, doit rester locale.

Qu'en pensez-vous ? Les jours de l'administrateur réseau de système propriétaire sont-ils comptés ?

_Vous cherchez plus ? Vous pourriez apprécier mes [livres et cours Pluralsight](https://bootstrap-it.com/) sur les sujets liés à Linux, AWS et Docker._