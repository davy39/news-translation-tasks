---
title: Comment activer le mode sombre dans les emails HTML – Tout ce que vous devez
  savoir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-16T12:20:00.000Z'
originalURL: https://freecodecamp.org/news/dark-mode-in-html-email-everything-you-need-to-know
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/iPhone-X-XS
seo_title: Comment activer le mode sombre dans les emails HTML – Tout ce que vous
  devez savoir
---

7@2x.png
étiquettes:
- nom: mode sombre
  slug: mode-sombre
- nom: email
  slug: email
- nom: Développement Web
  slug: developpement-web
seo_title: null
seo_desc: 'Par Patrik Krupař

Avec la nouvelle mise à jour iOS 13, Apple Mail obtient un thème sombre. Cela signifie qu'il s'agit
du premier client de messagerie majeur qui prend en charge la requête multimédia CSS prefers-color-scheme.
Ainsi, vous pouvez maintenant concevoir des emails spécifiquement pour les thèmes sombre et clair...'
---

Par Patrik Krupař

Avec la nouvelle mise à jour iOS 13, Apple Mail obtient un thème sombre. Cela signifie qu'il s'agit du premier client de messagerie majeur qui prend en charge la requête multimédia CSS `prefers-color-scheme`. Ainsi, vous pouvez maintenant concevoir des emails spécifiquement pour les thèmes sombre et clair.

Je suis un énorme fan du mode sombre, et les emails aveuglants sont mon ennemi. Alors, lorsque j'ai appris le mode sombre dans iOS 13, j'ai fait la seule chose évidente et j'ai commandé un tout nouveau iPhone pour tester les choses.

Pendant que j'y étais, j'ai également testé comment le mode sombre fonctionne dans presque tous les clients de messagerie, y compris le fauteur de troubles Outlook. Voici ce que j'ai trouvé.

**Mais d'abord, qu'est-ce que prefers-color-scheme ?**
La requête multimédia CSS `prefers-color-scheme` est utilisée pour détecter si l'utilisateur préfère un thème clair ou sombre, ce qui permet de concevoir des emails spécifiquement pour les deux.

Avec la mise à jour iOS 13, **le support dans la plupart des clients de messagerie populaires est passé de 2,3 % à 38,4 %** ! Une énorme étape grâce à la popularité d'Apple Mail. Étonnamment, Outlook était le seul client de messagerie qui supportait cela avant Apple Mail.

## Comment le mode sombre fonctionne dans les clients de messagerie populaires

Pour rendre le message électronique sombre lui-même, les clients de messagerie inversent automatiquement les couleurs de l'email en arrière-plan. Pour les emails réguliers de particulier à particulier, cela fonctionne bien et de manière cohérente dans tous les clients de messagerie.

Cependant, ce n'est pas si simple pour les emails HTML personnalisés — ceux qui remplissent la plupart de nos boîtes de réception. Je parle des emails transactionnels et promotionnels.

Voici les différences que j'ai trouvées dans la façon dont les clients de messagerie gèrent le rendu des emails en mode sombre :

|Client de messagerie|Popularité|Interface sombre|Inversion automatique des couleurs de l'email|Prend en charge @media (prefers-color-scheme)| |
|--- |--- |--- |--- |--- |--- |
|**Apple Mail** iPhone + iPad|36,1%|✔ Oui|✔ Oui|✔ Oui|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/applemail-ios.png)
|**Gmail** Android 10|27,8% *|✔ Oui|✔ Oui|✖ Non|	[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/gmail-android-1.png)
|**Gmail** iOS 13|27,8% *|✖ Non|✖ Non|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/gmail-ios.png)
|**Gmail** webmail|27,8% *|✔ Oui|✖ Non|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/gmail-webmail.png)
|**Outlook** iOS 13|9,1% *|✔ Oui|✔ Oui|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/outlook-ios.png)
|**Outlook** Android 10|9,1% *|✔ Oui|✔ Oui|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/outlook-android-1.png)
|**Outlook** Windows 10|9,1% *|✔ Oui|✔ Oui|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/outlook-windows-10.png)
|**Outlook** macOS|9,1% *|✔ Oui|✔ Oui|✔ Oui|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/outlook-macos.png)
|**Apple Mail** macOS|7,5%|✔ Oui|✔ Oui|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/applemail-macos.png)
|**Yahoo!** webmail|6,3% *|✔ Oui|✖ Non|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/yahoo-webmail.png)
|**AOL** webmail|6,3% *|✖ Non|✖ Non|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/aol-webmail.png)
|**Outlook.com** webmail|2,3%|✔ Oui|✔ Oui|✔ Oui|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/outlook-webmail.png)
|**Windows 10 Mail** Windows 10|0,5%|✔ Oui|✔ Oui|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/windows-10-mail.png)
|**Zoho Mail** webmail|moins de 0,5%|✔ Oui|✔ Oui|✖ Non|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/zoho-webmail.png)
|**Mozilla Thunderbird** Windows 10|moins de 0,5%|✔ Oui|✖ Non|✔ Oui|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/thunderbird-windows-10.png)
|**Spark** macOS|moins de 0,5%|✔ Oui|✔ Oui|✔ Oui|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/spark-macos-dark-mode.png)
|**Spark** iOS 13|moins de 0,5%|✔ Oui|✔ Oui|✔ Oui|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/spark-ios-dark-mode.png)
|**Spark** Android 9|moins de 0,5%|✔ Oui|✔ Oui|✔ Oui|[(Voir la capture d'écran)](https://sidemail.io/assets/dark-mode-in-html-email/spark-android-dark-mode.png)

_* La popularité est partagée sur toutes les plateformes pour le même client de messagerie car elle ne peut pas être distinguée de manière fiable. Source de popularité :_ [Litmus, la part de marché des clients de messagerie en 2019](https://litmus.com/blog/infographic-the-2019-email-client-market-share)_._

([Visitez l'article original](https://sidemail.io/articles/dark-mode-in-html-email/) pour voir mes notes des tests, et pour voir les derniers tests au fur et à mesure que je teste plus de clients de messagerie et que je mets à jour l'article en premier.)

## Comment rendre les emails HTML compatibles avec le mode sombre

J'ai déjà utilisé les données, et après quelques défis liés à Outlook, j'ai rendu nos emails compatibles avec le mode sombre. **Voici comment vous pouvez faire de même :**

> **Ce que disent les données :**
> Plus de 55 % des emails pourraient être ouverts avec le mode sombre activé. Une fois que Gmail rejoindra le côté sombre, les emails qui pourraient être ouverts avec le mode sombre activé vont exploser à 83 % !

### 1) Ajuster les couleurs

Faites attention à Apple Mail, car il inverse les couleurs uniquement si la couleur de fond est transparente ou non spécifiée — **un fond blanc ne fonctionnera pas**. La manière la plus simple de s'assurer que vos emails n'éblouiront personne est de vérifier si une couleur de fond est spécifiée. Pour plus de contrôle sur la conception, c'est là que `prefers-color-scheme` devient pratique.

**Syntaxe (@media prefers-color-scheme) :**

```css
<style>
	/* Vos styles de mode clair (par défaut) : */
	body {
		background: white;
		color: #393939;
	}

	@media (prefers-color-scheme: dark) {
		/* Vos styles de mode sombre : */

		body {
			background: black;
			color: #ccc;
		}
	}
</style>
```

**Un conseil de conception :** Évitez le blanc pur `#fff` comme couleur de texte. J'ai trouvé qu'un ratio de contraste d'environ 11,5 pour le texte principal est un bon compromis entre pas trop brillant et pas trop terne. Vérifiez le ratio de contraste ici : [https://contrast-ratio.com](https://contrast-ratio.com/) ou utilisez les outils de développement Chrome.

![Basculer entre les versions claire et sombre du logo dans un email HTML avec la requête multimédia prefers-color-scheme](https://sidemail.io/static/switching-logo-ccb909c2e5c3de55aeb36e5e69ca4d8b.svg)

### 2) Basculer entre le logo clair et sombre

Un texte sombre sur un fond sombre est pratiquement invisible, et c'est précisément ce qui arrive à un logo s'il est vu dans un client de messagerie avec le mode sombre activé.

De nos jours, un logo typique a généralement un fond transparent, une icône colorée et une copie sombre. Voyez le problème ? Parce que les clients de messagerie n'inversent pas les couleurs des images, vous devez le gérer vous-même.

Pour résoudre ce problème, vous pouvez soit :

1. enregistrer le logo avec un fond blanc au lieu d'un fond transparent (la manière la plus simple de corriger cela). Mais je ne recommanderais pas cette approche — les utilisateurs du mode sombre ne seront pas contents.
2. placer un logo clair sur un fond sombre, et garder le reste de l'email sur un fond blanc ([voir comment Litmus le fait](https://sidemail.io/assets/dark-mode-in-html-email/litmus-light-logo-on-dark-background.png)).
3. faire du mode sombre le mode par défaut de votre email. Un bon candidat pour cela serait Spotify, car ils ne proposent qu'un thème sombre dans leurs applications.
4. inclure les versions claire et sombre de votre logo et basculer entre elles avec la requête multimédia `prefers-color-scheme`.

Ma préférence va à la dernière approche, alors voici comment faire :

Un simple `"display: none"` sur le logo sombre fonctionne très bien dans tous les clients de messagerie modernes. Mais, à la surprise de tous, cela ne fonctionne pas dans Outlook et Windows 10 Mail.

Dans les styles CSS :

```css
<style>
	@media (prefers-color-scheme: dark) {
		.darkLogo {
			display: none !important;
		}

		.lightLogoWrapper,
		.lightLogo {
			display: block !important;
		}
	}
</style>
```

...et la structure HTML :

```html
<image src="dark-logo.png" class="darkLogo" />

<!--
	Pour masquer parfaitement le logo clair dans Outlook et Windows 10 Mail,
	vous devez envelopper la balise d'image du logo clair avec une div.
-->
<div class="lightLogoWrapper" style="mso-hide: all; display: none">
	<image src="light-logo.png" class="lightLogo" style="display: none" />
</div>
```

Cette approche fonctionne assez bien, mais elle ne fonctionnera toujours pas correctement partout. Le problème du texte sombre sur fond sombre se produira avec les clients de messagerie qui prennent en charge le mode sombre mais pas `prefers-color-scheme`. C'est-à-dire Outlook, Windows 10 Mail, Zoho, et potentiellement Gmail.

![Méthode infaillible : basculer entre les versions claire et sombre du logo dans un email HTML avec la requête multimédia prefers-color-scheme](https://sidemail.io/static/switching-logo-bulletproof-00ecb22b52186ddbf8bf6deec5c9b9f5.svg)

Ainsi, pour rendre le logo dans l'email totalement infaillible, je vais combiner les méthodes 1 et 4 ci-dessus. La méthode 1 couvrira tous les clients de messagerie qui prennent en charge le mode sombre, mais pas `prefers-color-scheme`. Et la méthode 4 couvrira Apple Mail, Outlook sur macOS, et Outlook.com, qui prennent en charge les deux.

De plus, au lieu d'enregistrer le logo sur un fond blanc, j'ajouterai une bordure de 3 pixels de large correspondant au fond et je l'enregistrerai sur un fond transparent comme d'habitude.

Cela commence à devenir assez complexe (juste pour un logo), alors voyons d'abord le balisage HTML :

```html
<!-- Logo par défaut avec une bordure de 3 pixels de large correspondant au fond -->
<image src="dark-logo-with-background.png" class="darkLogoDefault" />

<!-- Thème clair (donc logo sombre) :
Ceci est pour Apple Mail, Outlook sur macOS, Outlook.com -->
<div class="darkLogoWrapper" style="mso-hide: all; display: none">
	<image src="dark-logo.png" class="darkLogo" style="display: none" />
</div>

<!-- Thème sombre (donc logo clair) :
Ceci est pour Apple Mail, Outlook sur macOS, Outlook.com -->
<div class="lightLogoWrapper" style="mso-hide: all; display: none">
	<image src="light-logo.png" class="lightLogo" style="display: none" />
</div>
```

...et les styles CSS :

```css
<style>
	@media (prefers-color-scheme: light) {
		.darkLogoDefault,
		.lightLogo {
			display: none !important;
		}

		.darkLogoWrapper,
		.darkLogo {
			display: block !important;
		}
	}

	@media (prefers-color-scheme: dark) {
		.darkLogoDefault,
		.darkLogo {
			display: none !important;
		}

		.lightLogoWrapper,
		.lightLogo {
			display: block !important;
		}
	}
</style>
```

## Le mode sombre arrive dans Gmail

Le mode sombre arrive sur Android dans le nouveau Android 10, et Gmail devrait également devenir complètement sombre, enfin. Tout ce dont vous avez besoin est Android 10 et la dernière version de Gmail (au moins la version 2019.09.01.268168002). Cependant, Google a tendance à activer de nouvelles fonctionnalités (un thème sombre dans ce cas) pour les utilisateurs progressivement avec une mise à jour côté serveur, et je n'ai pas encore eu de chance avec cela.

Je suis curieux de voir si le support pour `@media prefers-color-scheme` arrive dans Gmail. D'après ce que j'ai lu, cela ne semble pas prometteur. Je suppose que nous devons attendre pour le découvrir. Je mettrai à jour l'article une fois que j'aurai activé le thème sombre dans Gmail.

## Conclusion

Le mode sombre arrive dans les emails HTML, et j'adore ça ! Mais c'est une autre chose à laquelle il faut penser — comme si utiliser des tableaux HTML pour la mise en page n'était pas suffisant.

[Restez à jour sur le mode sombre dans les emails en rejoignant notre liste de diffusion](https://hosted.sidemail.io/5d919d2fcc34a000fc97cfed). Nous y partageons également des informations et des défis auxquels nous sommes confrontés en construisant et en développant notre produit SaaS — [Sidemail](https://sidemail.io/).

Merci d'avoir lu !