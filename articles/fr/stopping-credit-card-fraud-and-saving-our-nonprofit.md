---
title: Comment j'ai empêché un voleur de carte de crédit de voler 3 537 personnes
  – et sauvé notre organisation à but non lucratif dans le processus
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-01-13T18:42:06.000Z'
originalURL: https://freecodecamp.org/news/stopping-credit-card-fraud-and-saving-our-nonprofit
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dea740569d1a4ca3a56.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: nonprofit
  slug: nonprofit
- name: Security
  slug: security
seo_title: Comment j'ai empêché un voleur de carte de crédit de voler 3 537 personnes
  – et sauvé notre organisation à but non lucratif dans le processus
seo_desc: 'My 2 year old woke me up by canonballing from my bed''s headboard down
  onto my face. I groaned and peeled off my eye mask. My phone said it was Wednesday,
  January 8, 2020 – the big day.

  I tucked my son under my arm and jogged to my desk. I''d been up u...'
---

Mon fils de 2 ans m'a réveillé en faisant un plongeon du haut de la tête de lit sur mon visage. J'ai grommelé et enlevé mon masque pour les yeux. Mon téléphone indiquait qu'il était mercredi 8 janvier 2020 – le grand jour.

J'ai glissé mon fils sous mon bras et j'ai couru à mon bureau. J'avais travaillé jusqu'à 2 heures du matin pour terminer [l'annonce de notre nouveau #AWSCertified Challenge](https://www.freecodecamp.org/news/awscertified-challenge-free-path-aws-cloud-certifications/).

Et jusqu'à présent, le lancement se passait bien. Notre nouveau bot Twitter tweettait, et notre salon Discord bourdonnait de développeurs ambitieux désireux d'obtenir leurs certifications AWS.

Je me préparais à rencontrer mon équipe lorsque j'ai remarqué deux e-mails étranges – tous deux arrivés à quelques minutes d'intervalle.

"Vous êtes une fraude" disait l'un des e-mails en anglais truffé de fautes de frappe. "C'est exactement ce que je pense depuis que je vois un prélèvement sur mon institution financière de votre part et puisque je n'ai jamais entendu parler de vous. Oui, vous devez régler cela."

L'autre e-mail était... disons simplement qu'il s'agissait également d'une lettre en colère et laissons cela.

freeCodeCamp est une organisation à but non lucratif soutenue par des donateurs, et nous avons des milliers de personnes dans le monde qui nous font des dons chaque mois. De temps en temps, il y a des malentendus – généralement lorsqu'un membre de la famille fait un don sans en informer l'autre. Mais cela semblait différent.

Alors j'ai basculé vers Stripe, le service de traitement des cartes de crédit que notre organisation utilise pour les dons. Un jour typique, nous avions 20 ou 30 nouveaux donateurs. Mais voici ce que j'ai vu à la place :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Dashboard_-_freecodecamp_org_-_Stripe1-2.jpg)
_Le tableau de bord de Stripe montrant 11 000 nouveaux clients et 60 000 $ de revenus pour une période de 24 heures._

Il m'a fallu un moment pour comprendre ce qui se passait. Notre organisation – qui fonctionne avec un budget annuel de moins de 400 000 $ – venait de recevoir plus de 60 000 $ en 24 heures – et de milliers de donateurs.

Et mon cœur a commencé à couler. Il n'y avait aucun moyen que ces dons soient réels. Nous avons eu des pics de dons à partir d'articles dans de grands journaux. Bon sang – j'ai même été interviewé à Good Morning America. Mais aucun de ces pics n'a provoqué une telle vague de dons.

Non. Il n'y avait qu'une seule chose qui pouvait provoquer une telle vague de dons. La fraude. Une fraude extensive et programmatique par carte de crédit.

J'avais déjà entendu parler de cette technique. On l'appelle le "card testing". Voici comment cela fonctionne :

1. Un fraudeur trouve un site web avec un formulaire de carte de crédit relativement simple. 
2. Ensuite, ils exécutent des scripts pour tester des milliers de numéros de cartes de crédit volées en succession rapide. Ainsi, ils peuvent voir quelles cartes sont encore valides et lesquelles ont été annulées. 
3. Ensuite, ils revendent ces numéros de cartes valides sur le dark web.

Dans ce cas, j'avais détecté la fraude beaucoup plus rapidement que beaucoup d'autres sites web ne l'auraient fait. Donc j'avais une fenêtre d'opportunité.

Si j'agissais rapidement et signalais toutes ces cartes de crédit comme volées, je pourrais sauver des victimes dans le monde entier de nombreuses charges de carte de crédit ultérieures – et beaucoup plus substantielles. Je pourrais prévenir des milliers d'appels téléphoniques stressants aux banques.

# Évaluer les dégâts

J'ai exécuté quelques requêtes dans Stripe. J'ai découvert qu'un seul fraudeur avait fait des dons avec 20 000 cartes de crédit volées différentes.

La bonne nouvelle était que Stripe avait détecté toutes ces transactions, sauf 3 537, comme des cartes volées, et les avait refusées.

Mais la mauvaise nouvelle : cela laissait encore 3 537 personnes qui recevaient maintenant des notifications de leurs banques leur indiquant qu'elles venaient de faire un don à notre organisation.

Pour aggraver les choses, je ne savais pas qui étaient les victimes et je n'avais aucun moyen de les contacter pour leur expliquer ce qui s'était passé.

Je me suis enfoncé dans ma chaise. Mon esprit tournait à toute vitesse.

Comment un fraudeur avait-il réussi à passer la validation de notre formulaire de don ?

Comment avait-il réussi à faire passer 3 537 transactions devant la détection de fraude de Stripe ?

Et comment diable avait-il obtenu les 20 000 numéros de cartes de crédit volées pour commencer ?

Mais rien de tout cela n'avait d'importance pour le moment. Tout ce que je savais, c'est que je devais rembourser chacune de ces transactions immédiatement.

Mais attendez.

Oh non.

Ce n'était pas seulement une question de rendre leur argent à ces personnes.

C'était beaucoup plus sérieux que cela.

# Bienvenue dans l'enfer des rétrofacturations

Chaque fois que quelqu'un appelle sa banque pour contester une transaction par carte de crédit, la banque lance un processus appelé "rétrofacturation". Il s'agit d'une sorte de remboursement forcé.

Les titulaires de cartes de crédit bénéficient du doute dans ces cas. Ainsi, les commerçants supportent toujours la responsabilité de ces rétrofacturations.

Non seulement la banque reprend l'argent au commerçant – elle ajoute également des frais de rétrofacturation. Pour Stripe, ces frais s'élèvent à 15 $.

Cela signifiait que notre organisation pourrait potentiellement être redevable de 15 $ par transaction.

J'ai rapidement griffonné quelques chiffres sur mon papier millimétré.

15 $ multipliés par 3 537 transactions font...

53 000 $.

Mon cœur a commencé à battre. Ma bouche est devenue sèche.

53 000 $ ? Cela effacerait complètement le fonds de secours de notre organisation.

Pendant un moment, j'ai désespérément cherché dans mes pensées une ligne de conduite.

Puis j'ai bondi sur mon clavier. J'ai trouvé un moyen de faire en sorte que le support de Stripe m'appelle sur mon téléphone.

Et pendant que j'attendais leur rappel, j'ai trouvé une requête que je pouvais utiliser sur Stripe pour extraire toutes les transactions frauduleuses dans un seul rapport de 177 pages.

J'ai convoqué notre équipe pour réfléchir à une réponse.

Ils ont rapidement identifié lequel des points de terminaison de l'API de freeCodeCamp.org le fraudeur avait utilisé, et ont mis en place un correctif pour le désactiver.

L'un de nos développeurs a dit : "Je peux écrire un script qui supprime simplement toutes ces transactions."

"Ce n'est pas si simple", ai-je dit. "Nous devons conserver des enregistrements de toutes ces transactions. Non seulement pour des raisons d'audit, mais au cas où quelqu'un du FBI ou d'Interpol nous contacterait. De plus, nous devons rembourser ces transactions. Immédiatement. Chaque minute qui passe est une minute où des milliers de personnes pourraient appeler leurs banques et engager des rétrofacturations contre notre organisation."

"D'accord, je pense que j'ai compris", a dit un autre développeur. "Je regarde la documentation de l'API de Stripe et je pense avoir trouvé le bon point de terminaison de l'API. Je peux rassembler un script."

Mon téléphone a commencé à sonner avec un numéro que je ne reconnaissais pas. Alors j'ai dit : "Ça a l'air d'un plan, équipe. Faisons-le." Et j'ai quitté la réunion pour répondre à mon téléphone.

La première personne du support Stripe à qui j'ai parlé m'a immédiatement escaladé après que je lui ai expliqué ce qui s'était passé. Ils m'ont mis en attente.

Mais le temps était de l'essence, et chaque transaction que je pouvais rembourser – aussi manuellement soit-il – était une transaction qui ne pouvait pas aboutir à une rétrofacturation.

Une par une, j'ai commencé à cliquer sur "rembourser la transaction" puis sur "signaler la transaction comme frauduleuse". Deux clics, quelques secondes de chargement, et ensuite je pouvais passer à la transaction suivante.

Je me suis chronométré en descendant la page, cliquant machinalement sur "rembourser la transaction" et "signaler la transaction comme frauduleuse" encore et encore.

Puis j'ai attrapé mon papier millimétré et j'ai fait les calculs.

En continuant simplement à faire ce que je faisais – en cliquant à travers cette liste comme un robot – j'étais sur le point de rembourser toutes les 3 537 transactions en 4 heures de plus.

Il était possible que mon équipe ne puisse pas faire fonctionner le script à temps, de toute façon. Alors j'ai simplement continué à le faire.

Cliquez. Attendez. Cliquez. Attendez. "Transaction remboursée !" Faites défiler vers le bas. Rincez et répétez.

Finalement, le support de Stripe est revenu au téléphone. Ils avaient quelques conseils bien intentionnés mais assez évidents.

J'ai passé l'heure suivante à faire défiler manuellement les remboursements aussi vite que possible. J'ai eu deux autres appels avec le support de Stripe. J'ai parlé avec chaque technicien de support que j'ai pu pour voir si je pouvais obtenir une sorte de percée qui pourrait accélérer le processus de remboursement de ces transactions.

Mais vers 1 200 remboursements dans le processus, le message "Transaction remboursée !" a cessé de s'afficher. À la place, un message inquiétant s'est affiché : "Remboursement en attente".

J'ai essayé un autre remboursement. "Remboursement en attente".

Oh non.

# Ils ne vont pas me faciliter la tâche, n'est-ce pas.

J'ai immédiatement basculé vers la page de support de Stripe et demandé un autre rappel. Ils m'ont expliqué que je ne pouvais plus rembourser les transactions car nous n'avions plus d'argent sur notre compte Stripe.

"Impossible", ai-je dit. "Nous venons de recevoir 60 000 $ de dons."

"Oui", a dit la personne du support. "Mais 40 000 $ de cela sont en transit vers votre banque."

J'ai jeté un coup d'œil au tableau de bord de Stripe. La personne du support avait raison.

Lorsque j'avais configuré le compte Stripe de notre organisation 2 ans auparavant, j'avais défini le calendrier de paiement sur "Automatique tous les jours".

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Dashboard_-_freecodecamp_org_-_Stripe-1.jpg)
_Stripe vous permet de configurer des paiements automatiques vers votre compte bancaire. J'ai fait l'erreur de le faire, et cela m'a hanté._

Même si notre compte Stripe avait reçu 40 fois le montant habituel des dons ce jour-là, Stripe avait simplement transféré l'argent vers notre banque.

Alors j'ai vérifié notre compte bancaire. Mais les 40 000 $ n'y étaient pas. Le crédit était toujours en attente.

Les 40 000 $ n'étaient ni dans notre compte Stripe ni dans notre compte bancaire. Ils étaient quelque part entre les deux. Et jusqu'à ce qu'ils arrivent, nous n'avions aucun moyen d'y accéder.

Donc maintenant je ne pouvais même plus rembourser les transactions manuellement. Et tant que ces transactions étaient en statut "Remboursement en attente", nous étions à risque de rétrofacturations.

Je suis retourné au téléphone avec Stripe. Ils m'ont dit : "Vous avez un solde négatif sur votre compte Stripe et vous ne pouvez plus émettre de remboursements."

J'ai demandé : "Comment puis-je rendre mon solde Stripe positif à nouveau pour pouvoir émettre les 2 300 remboursements restants ?"

"Vous pouvez nous envoyer un virement bancaire", a suggéré la personne du support. Et un moment plus tard, les informations de virement de Stripe sont apparues dans ma boîte de réception. "Une fois que vous nous aurez envoyé l'argent par virement, envoyez-nous une confirmation. Dans les 24 à 48 heures, nous pouvons dégelé votre compte pour que vous puissiez commencer à émettre des remboursements à nouveau."

"Vous me dites que je dois attendre 2 jours pour terminer l'émission de ces remboursements ?" ai-je demandé, exaspéré.

Mon équipe avait un script prêt, et ils l'avaient testé en utilisant le bac à sable de Stripe. "Mais nous ne devrions pas l'exécuter si les dons sont en statut en attente", m'ont-ils dit. "Cela pourrait tout gâcher. Nous ne trouvons aucune documentation à ce sujet."

À ce moment-là, il faisait noir dehors. Mes enfants s'étaient couchés pour la nuit. Et j'avais passé toute la journée au téléphone avec Stripe.

Je me suis assis à mon bureau et j'ai fixé les informations de virement bancaire. J'ai vérifié l'e-mail pour toute indication de falsification – tout indice d'une escroquerie – mais je n'en ai trouvé aucun.

J'allais virer 40 000 $ – l'intégralité du fonds de secours de notre organisation – à une multinationale de plusieurs milliards de dollars. Juste pour que nous puissions terminer le remboursement d'un groupe de personnes malchanceuses dont les numéros de carte de crédit avaient été volés – probablement lors d'une violation de données chez une autre multinationale de plusieurs milliards de dollars.

Sûrement ces informations de virement seraient publiquement répertoriées quelque part sur le site web de Stripe. Mais j'ai saisi le numéro de virement dans Google et j'ai obtenu zéro résultat.

Il n'y avait aucun moyen d'être sûr que la personne du support Stripe m'avait donné les bonnes informations de virement – et non les informations de son propre compte bancaire personnel. Cela serait peu probable, oui.

Mais ce serait une abdication de ma responsabilité en tant que trésorier de notre organisation de risquer d'envoyer 40 000 $ de l'argent de nos propres donateurs dans un trou noir.

Alors j'ai appelé Stripe une fois de plus. Et à ce moment-là, je me suis dit : et puis quoi. Je vais simplement continuer à leur demander de m'escalader jusqu'à ce que j'atteigne l'un des frères Collison (les fondateurs de Stripe) – ou au moins quelqu'un dans la prévention de la fraude. Il était presque minuit, mais je me suis dit que cela valait le coup d'essayer.

Finalement, j'ai atteint un technicien de support un peu plus haut placé qui semblait différent. J'ai poussé extra fort, extra poliment. Je lui ai dit ce qui était en jeu.

Elle est restée silencieuse un moment. Puis elle a dit : "Je connais peut-être une autre façon."

C'était comme si quelqu'un avait soudainement enfoncé une seringue de vitamine B12 dans mon bras. Je me suis redressé et j'ai dit : "Vraiment ?"

"C'est possible. Mais je vais devoir vous mettre en attente pendant longtemps", a-t-elle dit.

Mais avant de me mettre en attente, j'ai confirmé – une fois les fonds disponibles sur notre compte Stripe, les remboursements qui étaient en attente passeraient-ils immédiatement ?

Elle a dit que oui.

Elle m'a également rassuré que si – si – je pouvais faire passer ces charges frauduleuses en statut "remboursé", il n'y aurait plus de risque de rétrofacturation. Lorsque les banques des gens contacteraient Stripe, Stripe dirait simplement aux banques que "la charge a déjà été remboursée".

Et juste comme ça, j'ai vu une lumière au bout du tunnel.

Si je pouvais convaincre Stripe de dégeler notre compte d'une manière ou d'une autre, toutes les transactions "remboursement en attente" passeraient en statut remboursé. Cela éliminerait le piano à queue suspendu au-dessus de ma tête des 53 000 $ de rétrofacturations à notre organisation.

Et avec cela, plus de musique d'attente.

J'ai ouvert les scripts que notre équipe avait créés pour rembourser programmatiquement toutes les victimes de fraude.

"Damn", ai-je pensé. "Si ce script ne fonctionne pas exactement comme il est censé le faire, il n'y a aucun moyen de savoir ce qui pourrait se passer."

Et donc, juste pour être sûr, j'ai décidé de commettre le péché le plus odieux qu'un programmeur puisse commettre. Je l'ai fait manuellement.

Pendant des heures de musique d'attente, de rappels et de mises à jour de différentes personnes chez Stripe, je suis resté assis à mon ordinateur à réduire la liste.

Cliquez. Attendez. Cliquez. Attendez. "Remboursement en attente." Faites défiler vers le bas. Rincez et répétez.

Puis une autre personne du support est venue au téléphone et m'a demandé exactement combien d'argent je devais encore rembourser au total.

Réalisant que je n'avais plus que quelques pages de remboursements à faire, je lui ai demandé d'attendre pendant que je cliquais. Au moment où j'ai vu la dernière page, c'était comme un marathon où la ligne d'arrivée était enfin en vue. Et ensemble nous avons célébré le dernier remboursement en attente.

Quand tout a été dit et fait, le solde du compte Stripe de notre organisation était de -53 060 $.

Elle a transmis le numéro au département de fraude et m'a dit que je pouvais aller dormir pour la nuit. Mais je lui ai dit que j'insistais pour rester éveillé jusqu'à ce que chaque dernière transaction soit entièrement remboursée, et je lui ai demandé de me rappeler pour me tenir au courant.

J'ai attrapé ma veste et je suis sorti me promener dans la douce nuit de janvier.

Après quelques heures à ne pas fixer un moniteur, je suis rentré et j'ai actualisé.

J'avais déjà signalé chaque transaction comme frauduleuse. Et maintenant chaque don avait été remboursé intégralement à toutes les 3 537 victimes de fraude par carte de crédit.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Search_-_freecodecamp_org_-_Stripe.jpg)
_Une capture d'écran de Stripe après avoir réussi à rembourser toutes les 3 537 transactions._

Et alors que je soupirais de soulagement, j'ai imaginé le fraudeur quelque part de l'autre côté de la planète. Je l'ai imaginé assis dans un cybercafé enfumé, bouillonnant, frappant la table et hurlant : "J'ai testé ces numéros de carte de crédit hier. Pourquoi ne fonctionnent-ils pas ?"

![Image](https://www.freecodecamp.org/news/content/images/2020/01/NkQ5PpJ.gif)
_Je t'aurai la prochaine fois, Gadget !_

J'ai envoyé à mon équipe une dernière mise à jour que tout était résolu. Grâce à leur action rapide et un peu de détermination lors du traitement avec le support de Stripe, tous les remboursements atteindraient les comptes des victimes dans les jours à venir.

La plupart des victimes ne sauraient pas ce qui s'était passé et ne remarqueraient probablement même pas la charge suivie d'une annulation de cette charge.

Ils recevraient simplement une nouvelle carte de crédit par la poste de leur banque, puis découperaient leurs anciennes cartes de crédit compromises et continueraient leur vie.

J'ai gravi les escaliers épuisé. Le lancement du défi #AWSCertified semblait se passer correctement sans moi. De toute façon, cela pouvait attendre.

Pour l'instant, je n'avais qu'une seule priorité : dormir autant d'heures que possible avant que mon fils de 2 ans ne saute à nouveau sur ma tête le matin.

# Leçons apprises

### Leçon #1 : Désactivez les paiements automatiques de Stripe

Si vous utilisez Stripe, désactivez les paiements automatiques.

J'ai simplement eu de la chance que nous avions une longue relation de travail avec eux, et assez d'argent sur notre compte courant au cas où nous aurions eu besoin de leur envoyer de l'argent par virement.

### Leçon #2 : Il est parfois acceptable de passer en mode manuel

N'ayez pas peur d'avaler votre fierté et de faire les choses à l'ancienne.

Parfois, faire les choses manuellement – bien que fastidieux – est le moyen le plus sûr de prévenir encore plus de catastrophes.

Comme le dit l'ancien proverbe des astronautes, "Il n'y a pas de problème si grave que vous ne puissiez pas l'aggraver."

Votre script astucieux pourrait vous faire gagner du temps. Ou il pourrait créer un désordre qui prendra beaucoup plus de temps à nettoyer. Pesez tous les résultats avant de l'exécuter.

### Leçon #3 : Soyez persistant lorsque vous traitez avec le support

Si je n'avais pas continué à faire pression sur Stripe pour une meilleure solution que de leur envoyer un tas d'argent, notre organisation aurait été vulnérable aux rétrofacturations pendant plusieurs jours de plus, et cela nous aurait coûté des milliers de dollars.

Cela paie d'être poli mais insistant.

### Leçon #4 : Il y a de vrais salauds par là.

> "La sécurité en informatique est comme verrouiller votre maison ou votre voiture – cela n'arrête pas les méchants, mais si c'est suffisamment bon, ils peuvent passer à une cible plus facile." - Paul Herbka

freeCodeCamp est open source et compte des tonnes de chercheurs en sécurité qui nous informent des vulnérabilités potentielles par le biais de la divulgation responsable. Nous verrouillons nos portes proverbiales.

Mais malgré tous nos efforts, un attaquant nous a toujours vus comme une cible plus facile que certains des grands sites de commerce électronique. Ils étaient suffisamment sophistiqués pour trouver leur propre vulnérabilité zero-day dans notre base de code. Et ils pourraient faire de même pour votre organisation.

N'oubliez jamais que vous et moi partageons une planète avec des méchants qui sont prêts à causer des désagréments à des milliers de personnes juste pour qu'ils puissent gagner rapidement de l'argent.

Restez vigilants, amis.