---
title: Comment ignorer l'UX nuit à votre API et ce que vous pouvez y faire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T08:48:12.000Z'
originalURL: https://freecodecamp.org/news/how-ignoring-ux-hurts-your-api-and-what-to-do-about-it-e4f600f9cbfa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8c333d_YNEHG4q3UDb1wTA.jpeg
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment ignorer l'UX nuit à votre API et ce que vous pouvez y faire
seo_desc: 'By Ifeoluwa Arowosegbe

  Creating experiences that users love is crucial to the success of any product. Companies
  invest lots of resources trying to make sure they have kickass landing pages and
  cool page transitions. Yet, these efforts are often in sh...'
---

Par Ifeoluwa Arowosegbe

Créer des expériences que les utilisateurs adorent est crucial pour le succès de tout produit. Les entreprises investissent énormément de ressources pour s'assurer d'avoir des pages d'atterrissage exceptionnelles et des transitions de page fluides. Pourtant, ces efforts contrastent souvent nettement avec l'expérience des développeurs lorsqu'ils essaient de consommer leurs API.

Note rapide : Il s'agit ici des API dans le contexte des services RESTful.

Votre API est un produit à part entière. Elle est consommée par des développeurs qui sont considérés comme techniquement solides, mais cela ne signifie pas qu'ils méritent moins un traitement premium de premier ordre. **Les développeurs sont aussi des utilisateurs**.

> « L'objectif de la conception de l'expérience utilisateur dans l'industrie est d'améliorer la satisfaction et la fidélité des clients grâce à l'utilité, la facilité d'utilisation et le plaisir procurés par l'interaction avec un produit. » — [UX Curve](https://academic.oup.com/iwc/article/23/5/473/660020)

### Vous perdez de l'argent

Bien avant qu'un développeur ne décide de recommander votre produit/service au responsable technique ou à l'entreprise, sachez qu'il a déjà parcouru en détail votre page de documentation API. Il a essayé d'appeler plusieurs endpoints et s'est assuré d'être à l'aise — et dans de rares cas, satisfait — de votre offre.

Vous perdez des revenus si quoi que ce soit (documentation, temps de réponse, etc.) ne répond pas aux standards du développeur. Il préférera partir à la recherche d'alternatives plus attrayantes plutôt que de rester à essayer de comprendre la bonne façon de consommer votre API.

### Vous passez à côté de talents

Une [étude](https://www.glassdoor.com/employers/popular-topics/hr-stats.htm) de Glassdoor montre que 61 % de leurs utilisateurs effectuent activement des recherches sur une entreprise avant de décider d'y postuler. On ne peut que s'attendre à ce que ce chiffre soit plus élevé pour les développeurs professionnels qui ont un taux d'emploi de 98 % (3,9 % travaillent à temps partiel), selon le [StackOverflow’s Developer Survey](https://insights.stackoverflow.com/survey/2017#work).

Les développeurs examinent votre entreprise et vos produits à la loupe lorsqu'ils envisagent une opportunité de travailler avec vous. Pour les entreprises qui proposent des API accessibles au public, c'est un portail vers les pratiques d'ingénierie de votre entreprise (et cela offre la possibilité de découvrir des signaux d'alarme majeurs).

Des choses apparemment basiques comme l'utilisation de mauvaises méthodes HTTP pour effectuer des actions sur les ressources, l'absence de versioning des endpoints et une documentation médiocre pourraient être tout ce dont un développeur a besoin pour décider s'il envisagera de rejoindre votre équipe d'ingénierie ou s'il passera son chemin.

Je suis sûr que vous conviendrez que perdre les meilleurs talents au profit de la concurrence est la dernière chose qu'une entreprise ambitieuse souhaiterait.

### Éviter une mauvaise UX

Les effets de la négligence de l'expérience utilisateur en ce qui concerne vos API peuvent être très coûteux. Vous générez moins de revenus et accumulez une charge énorme sur le support client parce que presque tous vos utilisateurs peuvent à peine utiliser votre service sans avoir besoin d'aide.

Si vous souhaitez faciliter la vie des développeurs qui utilisent vos produits, les étapes suivantes pourraient vous aider.

#### **La documentation est essentielle**

La documentation est tout simplement la porte d'entrée de votre produit. Elle contient des instructions détaillées sur la façon dont votre API peut être utilisée, et vous ne voulez pas vous tromper. Elle doit être complète, bien structurée pour que l'information soit facile à trouver, et elle doit contenir des exemples.

De plus, toutes les informations nécessaires pour utiliser votre API doivent se trouver au même endroit. Vos utilisateurs ne devraient pas avoir à consulter différentes sources juste pour comprendre la bonne façon d'appeler un endpoint.

Vous devriez particulièrement éviter de partager la documentation API au format PDF. Cela introduit plus de problèmes que cela n'en résout, et vous ne voulez pas recevoir de tickets de support parce que l'utilisateur essaie de consommer votre API en utilisant un document obsolète comme guide.

Il existe des outils en ligne qui permettent aux utilisateurs de visualiser et de consommer des endpoints. Il est conseillé de tirer parti de ces outils pour créer et maintenir des documentations API robustes.

#### Adoptez les pratiques standards

Vous essayez de vendre un produit. L'objectif est d'attirer autant de clients que possible tout en éliminant les barrières qui pourraient empêcher les utilisateurs d'utiliser votre produit.

Lorsque vous essayez d'amener autant de développeurs que possible à utiliser votre API, vous n'avez pas à imposer vos propres standards ou modèles de développement d'API. Les grandes entreprises disposant d'une large base de clients peuvent se permettre de réaliser ce genre d'expérience, mais même dans ce cas, les résultats ne sont généralement pas favorables.

Versionez vos API, utilisez les bonnes méthodes HTTP pour effectuer des actions sur les ressources, assurez-vous que votre réponse est bien structurée et renvoyez les codes d'état corrects en fonction du succès ou de l'échec d'une requête.

L'[OpenAPI](https://www.openapis.org) est une spécification largement acceptée pour la conception d'API REST. Elle est soutenue par Microsoft, Google et de nombreux autres leaders du secteur technologique.

Une approche encore meilleure consisterait à mener une étude ou à envoyer des sondages aux développeurs qui représentent votre marché cible. Essayez de découvrir lesquelles de ces spécifications ils respectent et tentez d'adapter vos API à celles-ci.

Les développeurs sont moins enclins à adopter des technologies peu familières lorsqu'il existe des alternatives plus connues. Vous ne voulez certainement pas leur donner d'excuse pour ne pas utiliser le produit que vous proposez.

#### Des canaux de support ultra-actifs

Avoir plusieurs canaux de support dédiés pour gérer les plaintes des clients et les demandes d'aide est extrêmement important. Les développeurs de logiciels veulent obtenir des solutions rapides aux blocages qu'ils pourraient rencontrer lors de la consommation de vos API, ce qui rend le temps de réponse d'une importance capitale.

Les entreprises ont commencé à délaisser l'e-mail comme moyen par défaut de fournir un support aux utilisateurs car il est tout simplement trop lent. Et demander à des développeurs d'envoyer des extraits de code par e-mail est l'un des meilleurs moyens de les inciter à abandonner votre produit.

[Flutterwave](https://www.freecodecamp.org/news/how-ignoring-ux-hurts-your-api-and-what-to-do-about-it-e4f600f9cbfa/undefined) et Twitter disposent de forums dédiés pour répondre rapidement aux problèmes que les consommateurs pourraient rencontrer lors de l'utilisation de leurs produits. [Paystack](https://paystack.com/) dispose également d'un groupe Slack dédié pour aider les utilisateurs rencontrant des problèmes lors de la consommation de leurs API.

L'utilisation de canaux de communication en temps réel pour gérer les problèmes de support client n'est pas discutable. Vos utilisateurs sont des développeurs de logiciels, et il est essentiel qu'ils obtiennent de l'aide rapidement.

De plus, s'assurer que les extraits de code peuvent être facilement partagés via le support que vous avez choisi pour gérer les demandes d'assistance vous rapportera des points bonus auprès de vos utilisateurs.

#### Communiquez

Un infime changement dans vos formats de requête/réponse peut causer des dommages considérables aux produits de vos utilisateurs et à l'ensemble de leur activité. Il est très important que vous informiez vos utilisateurs des changements prévus et que vous leur laissiez suffisamment de temps pour s'y préparer. Tant que vous partagez des informations utiles et pertinentes, vos utilisateurs ne devraient pas avoir de raison de se plaindre.

Envoyez des e-mails et des e-mails de suivi rappelant à vos clients cet endpoint que vous allez supprimer dans les mois à venir. Informez-les rapidement des problèmes de sécurité et indiquez-leur ce qu'ils doivent faire pour être en sécurité.

Faites savoir à vos clients quand ils utilisent d'anciennes versions de votre produit et encouragez-les à mettre à jour. Sensibiliser les utilisateurs aux améliorations que vous avez apportées est un excellent moyen de les motiver à envisager une mise à jour. La plupart du temps, vos utilisateurs veulent simplement être assurés que la mise à jour contient les changements dont ils ont besoin.

Chaque consommateur qui décide d'utiliser votre API le fait parce qu'il a un niveau de confiance raisonnable dans l'offre de votre produit. Il est tout juste juste que vous récompensiez cette confiance en communiquant efficacement avec eux sur l'état de votre produit et sur la manière dont ils pensent que vous pouvez l'améliorer pour mieux les servir.

#### Conclusion

Le développement de produits est difficile. C'est encore plus vrai lorsque vous créez des API qui seront consommées par des développeurs de logiciels.

Cela dit, il n'est pas impossible de créer des API que les développeurs adoreront utiliser. Cela demande simplement beaucoup d'efforts conscients, et j'espère que ces étapes vous aideront à créer des services web que nous aimerions tous utiliser.

Si vous avez des questions ou des contributions concernant d'autres étapes qui pourraient aider les développeurs à apprécier de travailler avec nos API, n'hésitez pas à laisser un commentaire. Je serais ravi de les lire et d'y répondre.