---
title: Pourquoi je poursuis la FCC
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-15T13:11:01.000Z'
originalURL: https://freecodecamp.org/news/why-im-suing-the-fcc-887764b35499
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb363740569d1a4cac885.jpg
tags:
- name: Net Neutrality
  slug: net-neutrality
- name: News
  slug: news-tag
- name: politics
  slug: politics
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi je poursuis la FCC
seo_desc: 'By Jason Prechtel

  After over four months of confusion, controversy, and complete failures of Cybersecurity
  101, the Federal Communication Commission’s “Restoring Internet Freedom” proposal
  — a set of rule-changes that could dismantle Net Neutrality a...'
---

Par Jason Prechtel

Après plus de quatre mois de confusion, de controverse et d'échecs complets en matière de cybersécurité 101, la proposition de la Federal Communication Commission intitulée « [Restoring Internet Freedom](https://www.fcc.gov/restoring-internet-freedom) » — un ensemble de modifications de règles qui pourrait démanteler la [neutralité du net](https://en.wikipedia.org/wiki/Net_neutrality) et altérer à jamais le tissu de l'internet — a abouti à [22 149 776](https://www.fcc.gov/ecfs/search/filings?proceedings_name=17-108&sort=date_disseminated,DESC) commentaires publics en ligne en réponse.

Mais nous ne savons toujours pas combien de ces commentaires ont été laissés par **_des personnes réelles_**. 

En bref, c'est pourquoi j'ai commencé une enquête qui a abouti à [ce procès](http://jasonprechtel.com/FOIA/Prechtel-v-FCC.pdf).

Pour raconter l'histoire longue, revenons d'abord sur ce qui s'est passé au cours des derniers mois :

* Le commissaire de la FCC, Ajit Pai, a annoncé [une proposition de règle](https://apps.fcc.gov/edocs_public/attachmatch/DOC-344614A1.pdf) pour changer la réglementation de l'internet haut débit du Titre II au Titre I, ainsi qu'une période pour que le public laisse des commentaires qui pourraient façonner la décision finale de l'agence.
* Le même jour où la fiche d'information « Restoring Internet Freedom » a été publiée, [un autre avis public](https://apps.fcc.gov/edocs_public/attachmatch/DOC-344623A1.pdf) donnant des directives sur la manière de commenter la procédure a été publié, indiquant « nous anticipons que certains pourraient souhaiter soumettre un grand nombre de commentaires de la part de plusieurs individus, **chacun avec le même contenu ou un contenu similaire** » et « nous anticipons que pendant certaines périodes du cycle de commentaires, l'ECFS [Electronic Comment Filing System] pourrait connaître des volumes de trafic beaucoup plus élevés, et que **une partie de ce trafic pourrait être malveillante** ».
* John Oliver a appelé ses téléspectateurs à [commenter contre la proposition](https://www.youtube.com/watch?v=92vuuZt7wak), pour que le [site web de la FCC plante](http://thehill.com/policy/technology/332414-fcc-says-it-was-victim-of-cyberattack-after-john-oliver-show) dans ce qui pourrait (ou non) avoir été une [cyberattaque coordonnée](http://www.zdnet.com/article/cio-diary-lessons-from-the-fcc-bot-swarm/).
* Des commentaires publics sous les noms de vraies personnes ont été trouvés avoir été postés [sans leur connaissance](http://thehill.com/policy/technology/335154-the-individuals-whose-identities-were-used-to-file-fake-anti-net-neutrality).
* [Plusieurs](https://medium.com/@csinchok/an-analysis-of-the-anti-title-ii-bots-463f184829bc) [analyses](https://www.recode.net/2017/8/30/16223210/net-neutrality-fcc-21-million-record-comments-duplicates-suspicious-data) ont affirmé que jusqu'à des millions de commentaires (pour ou contre) étaient probablement faux.
* Des membres du Congrès ont [exigé des enquêtes](https://www.engadget.com/2017/08/17/congressmen-call-investigation-fcc-cyberattack/) de la part de plusieurs agences sur la prétendue cyberattaque.
* Le dernier jour de la date limite prolongée pour commenter, quelqu'un a découvert qu'une partie du système de commentaires pouvait être utilisée pour télécharger [n'importe quel type de fichier sur FCC.gov](https://medium.com/contratastic/the-fcc-gov-website-lets-you-upload-documents-and-host-them-there-bdcd5c1a5b8b), couronnant un processus de retour public déjà semé d'embûches avec encore plus de drapeaux rouges.

Ce type de période de commentaires publics n'est pas inhabituel pour la FCC. L'agence [annonce régulièrement de nouvelles procédures](https://www.fcc.gov/proceedings-actions) et est tenue de permettre au public de donner son avis sur celles-ci, soit en soumettant des commentaires en ligne, soit par courrier.

Pour cette proposition particulière, l'agence avait trois méthodes de soumission en ligne :

1. Soumettre un commentaire unique via le formulaire ECFS sur leur site web
2. Soumettre un modèle de téléchargement en masse ECFS « Restoring Internet Freedom » correctement formaté (avec plusieurs noms et commentaires individuels) à un widget de soumission spécial [créé spécialement pour cette règle](https://www.fcc.gov/restoring-internet-freedom-comments-wc-docket-no-17-108)
3. Soumettre des commentaires directement dans la base de données de la FCC via leur [Interface de Programmation d'Applications (API)](https://www.fcc.gov/ecfs/public-api-docs.html), en utilisant une [clé API enregistrée sur Data.gov](https://api.data.gov/signup/) qui nécessite un prénom, un nom de famille et une adresse e-mail valide

Ces trois méthodes permettaient facilement de falsifier des commentaires. Cependant, ce sont les deux dernières méthodes qui ont permis le problème clé avec le processus de commentaires « Restoring Internet Freedom » : **_n'importe qui pouvait soumettre des commentaires en masse_**. 

Heureusement, ces commentaires en masse ne pouvaient pas être envoyés complètement anonymement. La méthode de téléchargement en masse nécessitait également la soumission de l'adresse e-mail de la personne qui téléchargeait. La méthode API nécessitait une adresse e-mail valide pour recevoir la clé API Data.gov nécessaire pour commencer — de plus, le but d'un système de clé API est de donner (et de suivre) l'accès individuel des utilisateurs à un serveur donné.

En réalisant cela, j'ai soumis une demande de la loi sur la liberté de l'information à la FCC le 4 juin, demandant ce qui suit :

1. Toutes les clés API publiques, y compris les noms et adresses e-mail associés, qui ont été utilisées pour soumettre des commentaires en ligne via ECFS à la Procédure 17–108, « Restoring Internet Freedom » entre le 26 avril 2017 et aujourd'hui, et des copies de tous les fichiers de données soumis via ces clés API pour la même période.
2. Les journaux de toutes les dates et heures où lesdites clés API publiques ont été utilisées pour soumettre des commentaires en ligne via ECFS à la Procédure 17–108, « Restoring Internet Freedom » entre le 26 avril 2017 et aujourd'hui.
3. Les adresses e-mail associées à toutes les soumissions de commentaires .CSV, ainsi que tous les fichiers .CSV téléchargés en réponse à la Procédure 17–108, « Restoring Internet Freedom » entre le 26 avril 2017 et aujourd'hui (y compris les soumissions .CSV acceptées qui n'ont PAS utilisé le modèle de fichier .CSV « Restoring Internet Freedom ECFS Bulk Upload Template » de la FCC).
4. Les journaux de toutes les dates et heures où lesdites adresses e-mail ont soumis des commentaires en ligne via la boîte de soumission .CSV en ligne de la FCC à la Procédure 17–108, « Restoring Internet Freedom » entre le 26 avril 2017 et aujourd'hui.
5. Toutes les demandes par e-mail à [ECFSHelp@fcc.gov](mailto:ECFSHelp@fcc.gov) concernant les soumissions de commentaires .CSV en réponse à la Procédure 17–108, « Restoring Internet Freedom » entre le 26 avril 2017 et aujourd'hui.

Normalement, les demandes FOIA reçoivent des réponses des agents de liaison FOIA désignés dans les agences gouvernementales. Au lieu de cela, j'ai reçu un e-mail le 14 juin de la part de Kevin Baker, CIO associé de la FCC, accusant réception de ma demande et m'informant qu'ils prolongeaient leur délai légal pour répondre à ma demande du 3 juillet au 18 juillet.

Je n'ai plus jamais eu de nouvelles de la FCC.

Comme l'agence est légalement tenue de répondre à ma demande, et comme les questions sous-jacentes à ma demande n'ont toujours pas reçu de réponse, j'ai intenté un procès contre la FCC pour leur refus de mener une recherche en temps opportun des documents, et j'ai exigé la publication de ces documents.

Même maintenant, plus de trois mois après ma demande FOIA, et même après avoir intenté un procès, cette demande est **_toujours_** répertoriée comme « [en cours de révision par l'agence](https://foiaonline.regulations.gov/foia/action/public/view/request?objectId=090004d28136a9dc) ».

Bien sûr, ces documents demandés ne concernent que la période jusqu'au 4 juin, et ne tiendront pas compte de trois mois de millions de commentaires. Cependant, cette taille d'échantillon devrait être suffisante pour déterminer :

1. Si des schémas de téléchargement suspects avec des récidivistes ont eu lieu pendant la période de la prétendue cyberattaque des 7–8 mai
2. Si des groupes de commentaires soumis par certaines adresses e-mail correspondent à ce que d'autres analyses de commentaires précédentes suspectent être des commentaires falsifiés
3. Si des URL d'adresses e-mail suspectes (lobbyistes, firmes de relations publiques, adresses .gov, noms de domaine non américains, etc.) ont été autorisées à soumettre des commentaires en masse

S'il s'avère qu'il existe des preuves frappantes de ce que la FCC elle-même a appelé un trafic « malveillant », ils auront beaucoup d'explications à donner aux citoyens américains, aux entreprises et aux membres du Congrès.

Quelles que soient vos propres opinions sur la manière dont l'internet devrait être réglementé, il y a ici un problème flagrant de transparence gouvernementale.

Après tout, comment pouvons-nous faire confiance à l'intégrité du processus de prise de décision de la FCC lorsqu'ils refusent de divulguer des documents montrant comment des millions de commentaires **_qui sont déjà publics_** ont été soumis en premier lieu, et par qui ?

Édition : Un remerciement spécial à Matt Topic et Josh Burday de [Lovey & Loevy](https://loevy.com/) pour avoir pris mon affaire. Matt m'a précédemment représenté dans un [procès FOIA](https://loevy.com/content/uploads/2014/07/Jason-Prechtel-v.-Chicago-Transit-Authority.pdf) contre la [Chicago Transit Authority](https://www.chicagoreader.com/chicago/jason-prechtel-interview-ventra-cta/Content?oid=18650024) en 2014.