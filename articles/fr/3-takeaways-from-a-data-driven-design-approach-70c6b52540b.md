---
title: Ce que j'ai appris d'une approche de conception basée sur les données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T12:47:57.000Z'
originalURL: https://freecodecamp.org/news/3-takeaways-from-a-data-driven-design-approach-70c6b52540b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E7Kp5eCfdHTRiBG5F0Lq1g.png
tags:
- name: analytics
  slug: analytics
- name: data
  slug: data
- name: UI
  slug: ui
- name: UX
  slug: ux
- name: Web Design
  slug: web-design
seo_title: Ce que j'ai appris d'une approche de conception basée sur les données
seo_desc: 'By Michael Loscalzo

  What happens when preconceived notions take a back seat to the lessons learned from
  metrics?


  Let’s begin at the end…

  ? My blog metrics indicate that 60% of readers don’t read the full post. So, let’s
  take an extremely quick look ...'
---

Par Michael Loscalzo

#### Que se passe-t-il lorsque les notions préconçues laissent place aux leçons tirées des métriques ?

![Image](https://cdn-media-1.freecodecamp.org/images/widiEqLbOV4j5PGXRvQF2TRAhBr7uL4jjgUQ)

### Commençons par la fin...

? Mes métriques de blog indiquent que 60 % des lecteurs ne lisent pas l'article complet. Alors, jetons un coup d'œil extrêmement rapide à ce que j'ai appris d'une refonte de site web basée sur les données !

#### LEÇON #1

**Si présenté correctement, un visiteur passera _plus_ de temps à consulter _moins_ de contenu.** Malgré une diminution du nombre de pages et une réduction du nombre de mots par page, j'ai observé une augmentation de la durée moyenne des sessions.

**Les changements :**

* Les longs blocs de texte ont été réévalués et tronqués en des descriptions plus concises.
* La structure consolidée du site a permis aux visiteurs de trouver rapidement le contenu pertinent.

![Image](https://cdn-media-1.freecodecamp.org/images/cCr3MsX7kj7vGzhvZIqghBzOEkcKKW8AR5yV)
_L'augmentation de la durée moyenne des sessions indique que les visiteurs restent plus longtemps sur le site web._

#### LEÇON #2

**Les modèles de conception fonctionnent !** Il peut être tentant de briser toutes les règles, mais la vérité est que les modèles de conception sont familiers aux visiteurs et utilisent une composition qui tire parti du mouvement naturel des yeux d'un spectateur.

**Les changements :**

* La page d'accueil révisée présente un [modèle en forme de Z](https://uxplanet.org/z-shaped-pattern-for-reading-web-content-ce1135f92f1c) (desktop) et priorise le contenu le plus fréquemment consulté. Sur les pages avec de grands blocs de texte, un modèle en forme de F (desktop) a été utilisé.
* La navigation principale a été révisée pour être plus intuitive et adaptée aux mobiles.

![Image](https://cdn-media-1.freecodecamp.org/images/yVs34Eiazyqr5YlN9AYXqiQ9APlxT34l7VR1)
_La diminution de 8 % du taux de rebond indique une visite plus approfondie du site web._

#### LEÇON #3

**Supprimez les étapes du parcours utilisateur pour améliorer le taux de conversion.** La suppression d'une seule étape dans le parcours utilisateur a entraîné une forte augmentation des conversions.

Les conversions ont été mesurées par le pourcentage de visiteurs ayant soumis un formulaire de questionnaire.

**Les changements :**

* Moins d'étapes pour qu'un visiteur atteigne le formulaire de questionnaire avec des informations adéquates sur les offres.
* Augmentation de la visibilité du formulaire.
* Au lieu d'un long formulaire (15 questions), le formulaire a été divisé en trois petites parties (5 questions par partie).

![Image](https://cdn-media-1.freecodecamp.org/images/gl3B-LuvnggO44-l4Dpk4kP8CXwdOmnDmV4W)
_Une forte augmentation du taux de conversion indique que plus de visiteurs effectuent une action souhaitée en réponse à un appel à l'action (CTA)._

Merci d'avoir lu jusqu'ici !

Ci-dessous, j'ai fourni un examen beaucoup plus granulaire des raisons pour lesquelles certains changements ont été apportés et des améliorations résultantes observées dans les indicateurs clés de performance (KPI).

### Le client

En 1980, Carol Yilmaz et neuf autres parents ont cherché une éducation appropriée pour leurs enfants surdoués. Ensemble, ils ont fondé la [**Long Island School for the Gifted**](http://lisg.org/learn-more.html) (LISG), une école privée mixte de jour.

**La déclaration de mission de la LISG :**

> Fournir une éducation appropriée aux enfants surdoués de la maternelle à la neuvième année, dans un environnement bienveillant où ils seront à la fois intellectuellement stimulés et socialement à l'aise, offrant ainsi à ces enfants l'opportunité de grandir et de se développer à leur potentiel.

Le site web de la LISG cherche à fournir aux étudiants potentiels et à leurs parents des détails sur les offres uniques disponibles à l'école. Une étape préliminaire dans le processus de candidature est le formulaire "Questionnaire d'introduction", qui peut être complété sur le site web. De plus, le site web fournirait des informations précieuses aux étudiants inscrits et à leurs parents.

### Site web de la LISG : 2014-2017

Avant 2014, le site web de la LISG était largement statique. Le site web de 2014-2017 présentait un carrousel de photos, un calendrier numérique des événements étudiants et un formulaire de [questionnaire d'introduction](http://lisg.org/admissions.html), qui aiderait les parents potentiels à démarrer le processus de candidature.

![Image](https://cdn-media-1.freecodecamp.org/images/h2E9ItwlD3p32hda3forHaIwlIBUMuMdo3XL)
_Le site web de 2014-2017 vu sur une tablette et un smartphone._

Bien que la refonte de 2014-2017 du site web de la LISG ait été une amélioration par rapport à la conception précédente, les métriques collectées indiquaient que des améliorations supplémentaires pouvaient être apportées.

#### LES OUTILS D'ANALYTIQUE

* **Google Analytics :** Mesure les données du site web, de l'application, du numérique et hors ligne pour obtenir des informations sur les clients.
* **JotForm :** est une application en ligne qui permet aux administrateurs de sites web de créer rapidement des formulaires en ligne personnalisés. JotForm offre un outil d'[analytique](https://www.jotform.com/form-analytics/).

#### LES PRINCIPALES DÉCOUVERTES

* **Types d'utilisateurs distincts :** Sur la base du trafic du site web et du flux de comportement, il semble y avoir deux types d'utilisateurs distincts avec deux besoins de contenu distincts. Les deux types d'utilisateurs sont les parents/étudiants potentiels et les parents/étudiants inscrits.
* **Durée moyenne des sessions :** Le visiteur typique ne passe qu'un court moment sur chaque page, ce qui indique que les longs blocs de texte ne sont pas lus.
* **Conversion :** Environ 0,69 % des visiteurs remplissent le questionnaire d'introduction.
* **Augmentation du trafic mobile :** Le trafic mobile vers le site web a augmenté de près de 50 % sur une période de trois ans.

### Site web de la LISG : refonte de 2017

Après avoir examiné les données de 2014-2017, nous avons commencé le processus de refonte avec des objectifs clairs en tête.

#### LES OBJECTIFS DE LA REFONTE

1. **Affiner la structure du site :** Consolider le contenu du site et réduire le texte.
2. **Améliorer l'interface mobile :** L'augmentation du trafic mobile a mis en évidence le besoin d'améliorations pour la navigation mobile.
3. **Utiliser des modèles de conception établis :** Les modèles de conception établis sont familiers aux visiteurs et utilisent une composition qui tire parti du mouvement naturel des yeux d'un spectateur.
4. **Améliorer le parcours utilisateur :** Supprimer les obstacles inutiles et permettre aux visiteurs de trouver rapidement et facilement ce qu'ils recherchent.
5. **Augmenter les conversions :** Améliorer la visibilité du formulaire de questionnaire d'introduction et le rendre moins intimidant à remplir.

![Image](https://cdn-media-1.freecodecamp.org/images/hhsnLeNOiXDynU23bu0vZkFXW0bPg73GvIli)
_La refonte du site web de 2017 vue sur une tablette et un smartphone._

#### OBJECTIF #1 : AFFINER LA STRUCTURE DU SITE

Bien que beaucoup du contenu du site web puisse être pertinent pour les étudiants/parents potentiels et inscrits, un effort a été fait pour déterminer quel type d'utilisateur serait principalement intéressé par chaque page. De plus, le contenu a été consolidé ou éliminé lorsque cela était approprié.

Cette approche nous a permis de réduire la taille du site web de quatre pages dans le but de créer une structure de site plus intuitive.

![Image](https://cdn-media-1.freecodecamp.org/images/oh4vg2OT7b73xl1ZuJJrpXs1eaZc-Jv6iXtj)
_Évaluation du contenu par type d'utilisateur et consolidation du contenu en moins de pages._

Lorsque nous avons développé la première refonte en 2014, il y avait un désir de partager beaucoup d'informations et de faire paraître le site web robuste. Les longs blocs de texte ont peut-être été décourageants pour les visiteurs qui recherchent et évaluent probablement plusieurs écoles en une seule fois.

![Image](https://cdn-media-1.freecodecamp.org/images/OBkL0X0aW5VyAlN5uWonlnFuPgS7LJ12hJPe)
_Les longs blocs de texte sont devenus des descriptions plus concises ou des puces._

#### OBJECTIF #2 : AMÉLIORER L'INTERFACE MOBILE

La navigation qui apparaissait sur le site web de 2014-2017 est devenue comprimée sur le côté gauche de la fenêtre d'affichage sur mobile. Pire encore, sur plusieurs appareils, certains des boutons ont disparu sous la ligne de flottaison. Ces problèmes ont probablement contribué à une augmentation du taux de rebond sur les smartphones.

![Image](https://cdn-media-1.freecodecamp.org/images/hvMRjaHnO5gMVuRQ20KVkYfilPuk4k3pDbLw)
_À gauche : La navigation mobile est devenue comprimée sur mobile. À droite : La disposition simplifiée offre des CTAs simples et un menu "hamburger"._

#### OBJECTIF #3 : UTILISER DES MODÈLES DE CONCEPTION ÉTABLIS

L'utilisation des modèles en F et en [Z](https://uxplanet.org/z-shaped-pattern-for-reading-web-content-ce1135f92f1c) peut aider à créer une hiérarchie visuelle dans la conception web.

> "Ce modèle [en forme de Z] fonctionne parce que la plupart des lecteurs occidentaux scanneront votre page de la même manière qu'ils scanneraient un livre — de haut en bas, de gauche à droite."

> — Nick Babich, UX Planet

![Image](https://cdn-media-1.freecodecamp.org/images/8orXuzIPU8g-AYO3c3ReaSn-NHq51Q9KCvpJ)
_Mouvement approximatif des yeux en "Z" sur la page d'accueil de la LISG de 2017._

![Image](https://cdn-media-1.freecodecamp.org/images/FQWbM20fOhUwE4Tr90xxkumHTCQZY-VP3ewe)
_À droite : La refonte du site web de 2017 supprime la navigation de la colonne de gauche et organise le contenu pour un modèle de visualisation en forme de F._

#### OBJECTIF #4 : AMÉLIORER LE PARCOURS UTILISATEUR

Sur la base des données démographiques et du trafic des pages, nous avons pu conclure que la majorité des visiteurs du site web étaient des étudiants/parents potentiels. Idéalement, un parent potentiel utilise le site web pour en savoir plus sur l'école, déterminer si son enfant est éligible à l'admission, et il peut même commencer le processus de candidature en remplissant le questionnaire d'introduction.

> "Les parcours utilisateurs sont le parcours étape par étape qu'un utilisateur suit pour atteindre son objectif. Ce parcours consistera souvent en un certain nombre de pages web et de points de décision qui transportent l'utilisateur d'une étape à une autre... Ce parcours est ensuite redessiné pour former un parcours utilisateur 'idéal' sans frustration."

> — [Experience UX](https://www.experienceux.co.uk/faqs/what-are-user-journeys/)

En utilisant les métriques de flux de comportement, nous avons pu voir qu'il fallait trois interactions avant qu'ils ne remplissent le questionnaire d'introduction. À chaque interaction, il y a une perte de visiteurs.

![Image](https://cdn-media-1.freecodecamp.org/images/QQHeVXyR81b20JUVTVMor4QJWTnpth1AjfZz)
_Le flux de comportement le plus courant sur la version 2014-2017 du site web._

Dans la version 2014-2017 du site web, les métriques indiquent que seulement environ 5 % des visiteurs atteignent la page des admissions avec suffisamment d'informations sur l'école pour déterminer en toute confiance s'ils voulaient remplir le formulaire de questionnaire d'introduction ou non.

![Image](https://cdn-media-1.freecodecamp.org/images/sLq9O6d7fpr1wiCkKacsNfW1Y0VJfmweyqmL)
_Le flux de comportement le plus courant sur la version 2017 du site web._

Dans la refonte de 2017, près de 15 % des visiteurs atteignent la page des admissions avec des informations adéquates sur l'école.

#### OBJECTIF #5 : AUGMENTER LES CONVERSIONS

Sur la base des données de 2014-2017, nous avons émis l'hypothèse que les utilisateurs pouvaient avoir des difficultés à trouver le formulaire de questionnaire d'introduction (il était logé dans un menu accordéon). De plus, le formulaire pouvait sembler intimidant car il était verticalement long.

![Image](https://cdn-media-1.freecodecamp.org/images/P06EGnPk71zpAMbdDmZi9J6Ija5ejsMvufyW)
_Le long formulaire a été divisé en trois segments plus petits._

Un formulaire d'une page avec 15 questions est moins susceptible d'être complété qu'un formulaire de 3 pages avec 5 questions par page.

Le nombre de soumissions de formulaires a augmenté de 129 %. Le taux de conversion est passé de 0,69 % à près de 1,6 %.

Et c'est ainsi que nous avons complété une refonte réussie. Merci d'avoir lu ! Si vous avez aimé cette histoire, vous pouvez [Lire plus](https://medium.com/@MichaelLoscalzo) ou [Me suivre sur Twitter](https://twitter.com/MichaelLoscalzo).