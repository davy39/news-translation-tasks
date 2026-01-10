---
title: Comment utiliser Selenium et Python pour extraire des données de sites web
  plus efficacement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-11T22:53:43.000Z'
originalURL: https://freecodecamp.org/news/improve-web-scraping-with-selenium
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/web-scraping-articl-image.jpg
tags:
- name: Python
  slug: python
- name: selenium
  slug: selenium
- name: web scraping
  slug: web-scraping
seo_title: Comment utiliser Selenium et Python pour extraire des données de sites
  web plus efficacement
seo_desc: 'By Otávio Simões Silveira

  When you''re scraping data from the web with Python, Selenium will often come up
  as an helpful tool to use. It was originally designed for automated testing, but
  its scraping capabilities are impressive, too.

  This is because ...'
---

Par Otávio Simões Silveira

Lorsque vous extrayez des données du web avec Python, Selenium apparaît souvent comme un outil précieux. Il a été conçu à l'origine pour les tests automatisés, mais ses capacités de scraping sont également impressionnantes.

C'est parce que Selenium peut faire des choses que d'autres bibliothèques ou frameworks ne peuvent souvent pas faire lors de la collecte de données : accéder au contenu rendu par JavaScript et interagir avec la page de pratiquement n'importe quelle manière.

Cet article porte sur la deuxième capacité – interagir avec la page comme vous le souhaitez. Il couvrira trois sujets utiles pour vous donner plus d'options lorsque vous interagissez avec un site web afin d'accéder à son contenu.

Et bien que cet article se concentre sur le web scraping, ce n'est qu'un cas d'utilisation pour ces conseils, car vous pouvez les mettre en œuvre pour toutes les tâches où Selenium est utile.

Avant de commencer, un avertissement important : avant de commencer à scraper un site web, assurez-vous de vérifier si le site vous y autorise. De plus, c'est une bonne pratique de configurer votre scraper afin de ne pas surcharger le serveur du site web, car nous n'avons pas l'intention de causer de dommages.

Le scraping est amusant et constitue un excellent moyen de rassembler des données, mais il doit être effectué de manière correcte et légale.

## Comment cocher des cases

Le processus d'extraction de données ne consiste pas seulement à extraire les données. Parfois, vous devez naviguer sur le site web pour arriver là où se trouvent les données. Et en parcourant le site web, vous devrez peut-être remplir des formulaires, cliquer sur un ou deux boutons et cocher une case, par exemple.

Cocher une case peut sembler être une action très simple, mais cela peut être un peu délicat. C'est parce que vous pourriez penser qu'il suffit de localiser l'élément à l'aide de son Xpath, puis d'utiliser la méthode `click` pour cliquer dessus.

Et, oui, selon le site web, cela peut être le cas – mais ce n'est pas une règle. Pour la plupart des sites web, Selenium ne reconnaîtra pas une case à cocher comme un bouton cliquable. Ainsi, lorsque vous essaierez de cliquer dessus, une exception sera levée.

La solution de contournement consiste à localiser l'élément et à utiliser un objet ActionChains pour déplacer le curseur vers la case à cocher, puis à cliquer dessus. Voici le code pour le faire :

```python
check_box = driver.find_element_by_xpath('Xpath')

actions = webdriver.ActionChains(driver)
actions.move_to_element_with_offset(check_box, -5, 5).perform()
actions.click().perform()
```

La méthode `move_to_element_with_offset` déplacera la souris selon un décalage par rapport à un élément spécifique sur la page, par rapport à son coin supérieur gauche. Vous devez indiquer l'élément et la distance à laquelle vous souhaitez que le curseur s'éloigne du coin supérieur gauche.

L'objectif est d'avoir le curseur vers le milieu de la case à cocher. Pour trouver la distance appropriée pour le déplacement, exécutez le code avec l'attribut `size` de l'élément avant d'exécuter le code complet.

```python
check_box = driver.find_element_by_xpath('Xpath')
print(check_box.size)
```

La sortie devrait ressembler à ceci :

`{'height': 10, 'width': 10}`

Ensuite, une fois le curseur déplacé, il vous suffit d'effectuer un clic et la case sera cochée.

## Comment gérer les cadres

Il se peut que vous vous soyez retrouvé dans une situation où vous ne parvenez tout simplement pas à faire en sorte que Selenium trouve un élément particulier sur une page web. Peu importe la méthode utilisée – Xpath, nom de classe ou autre – vous continuez à obtenir des erreurs.

Vous vérifiez donc encore et encore les erreurs dans le code, mais tout semble correct. Alors, qu'est-ce qui ne va pas ?

En fait, rien ne va mal. Les données que vous souhaitez collecter ou l'élément avec lequel vous souhaitez interagir se trouvent simplement dans un autre cadre (frame) sur la page. Nous utilisons des cadres HTML pour diviser la page en sections qui chargent chacune une partie différente du contenu.

Pour résoudre le problème, il vous suffit de passer au cadre correct avant d'essayer d'interagir à nouveau avec la page. Si vous connaissez le nom du cadre, faites simplement ceci :

```python
driver.switch_to.frame('mainIframe')
```

Vous pouvez également utiliser l'index du cadre pour effectuer le changement :

```python
driver.switch_to.frame(0)
```

Mais si vous ne connaissez pas le nom du cadre ou le nombre de cadres sur la page, la solution consiste à trouver tous les cadres de la page puis à imprimer le nom de chacun d'eux. Voici comment cela fonctionnerait :

```
frames = driver.find_elements_by_tag_name('iframe')
for frame in frames:
   print(frame.get_attribute('name'))

```

Pour savoir combien de cadres il y a sur la page, imprimez simplement la longueur de l'objet `frames`.

```python
print(len(frames))
```

Et maintenant, vous êtes libre d'interagir avec la page et de collecter les données dont vous avez besoin.

## Comment changer d'onglet

Une autre situation courante que vous pourriez rencontrer lors de la navigation sur un site web pour collecter des données est qu'un bouton ouvre automatiquement un nouvel onglet. Lorsque cela se produit, il est important de savoir comment passer d'un onglet à l'autre afin d'obtenir les données dont vous avez besoin.

Heureusement, la gestion des onglets avec Selenium n'est pas un processus complexe. En fait, c'est assez similaire à la gestion des cadres.

Vous pouvez utiliser une approche plus rudimentaire utilisant deux objets : l'un contient l'onglet actuel et l'autre contient tous les onglets. Ensuite, il vous suffit d'itérer sur le second et si l'itérateur est différent de l'onglet actuel, vous changez.

```python
current_tab = driver.current_window_handle

all_tabs = driver.window_handles
for tab in all_tabs:
   if tab!= current_tab:
       driver.switch_to.window(tab)
```

Mais si vous avez plus de deux onglets et que vous voulez pouvoir accéder à n'importe lequel d'entre eux à tout moment, il existe une approche plus élégante – et vous n'aurez qu'à suivre l'ordre dans lequel les onglets sont ouverts.

Pour cette approche, vous n'avez pas besoin de connaître l'onglet actuel. C'est parce que vous pouvez changer d'onglet simplement en sélectionnant l'index correspondant de l'onglet vers lequel vous souhaitez vous déplacer dans l'objet contenant tous les onglets.

```python
driver.switch_to.window(all_tabs[i])
```

Si vous souhaitez parcourir tous les onglets en une seule fois, effectuer des actions et collecter des données de chacun d'eux, vous pouvez également facilement itérer sur tous les onglets.

```python
all_tabs = driver.window_handles
for tab in all_tabs:
   driver.switch_to.window(tab)
```

Cependant, si vous ouvrez plus d'onglets pour scraper des données et que vous avez beaucoup de liens à parcourir, vous devez être conscient que vous effectuez considérablement plus de requêtes au site web que d'habitude. C'est parce que pour chaque lien, vous ouvrez deux ou trois nouveaux onglets.

Dans ce cas, vous voudrez également insérer des pauses aléatoires dans votre code afin de ne pas surcharger le serveur. Vous voudrez également profiter d'un fournisseur de proxy, comme [Infatica](https://infatica.io/) (une entreprise qui s'engage à partager des informations via des articles comme celui-ci) pour vous assurer que votre code continuera à s'exécuter tant qu'il restera des pages à scraper.

Cela permet également de s'assurer que vous ne serez pas bloqué et que vous et votre connexion êtes protégés.

## Conclusion

J'espère que ces conseils sur Selenium vous aideront à l'utiliser et à extraire des données plus efficacement. Il y a bien d'autres choses que vous pouvez faire, mais je voulais que cet article reste relativement court.

Si vous êtes intéressé par plus de contenu de ce type ou si vous avez une question, une suggestion, ou si vous voulez simplement rester en contact, n'hésitez pas à me contacter. Peut-être qu'une deuxième partie arrivera bientôt !