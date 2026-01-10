---
title: Comment configurer GitHub OAuth dans une application Django pour l'authentification
  des utilisateurs
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2023-12-05T21:19:14.000Z'
originalURL: https://freecodecamp.org/news/set-up-github-oauth-on-django-for-user-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Blog-Banner
seo_title: Comment configurer GitHub OAuth dans une application Django pour l'authentification
  des utilisateurs
---

Template.png
tags:
- name: authentification
  slug: authentification
- name: Django
  slug: django
- name: GitHub
  slug: github
- name: oauth
  slug: oauth
seo_title: null
seo_desc: "Maintenir une authentification utilisateur sûre et sans friction est primordial dans le paysage actuel des applications web en constante évolution. 

Parmi les nombreuses méthodes d'authentification disponibles, GitHub OAuth s'est imposé comme un outil utile pour améliorer l'expérience de connexion des utilisateurs tout en renforçant les mesures de sécurité. 

[Django](https://docs.djangoproject.com/en/4.2/), un framework web Python, a récemment gagné en popularité dans le développement web grâce à son efficacité et sa polyvalence. L'ajout de GitHub OAuth à vos projets Django aide à améliorer le processus d'authentification. 

Les développeurs Django peuvent utiliser GitHub OAuth pour accéder au profil GitHub d'un utilisateur et (avec permission) à ses dépôts pour personnaliser l'expérience utilisateur et adapter les services de l'application.

Cet article vous guidera à travers la mise en œuvre de GitHub OAuth. Vous verrez les avantages pour vos projets Django au fur et à mesure. En adoptant cette technologie, vous pouvez offrir aux utilisateurs une expérience de connexion transparente tout en respectant des normes de sécurité strictes.

## Prérequis

Si vous souhaitez suivre ce guide, vous devez avoir une compréhension de base de ces outils ou les avoir installés sur votre PC : 

* [GitHub](https://github.com/)
* [Django](https://docs.djangoproject.com/en/4.2/)
* [Django Rest Framework](https://www.django-rest-framework.org/)

## Comment créer une application GitHub OAuth

Vous devez vous connecter à votre compte GitHub pour créer une application GitHub OAuth. 

Tout d'abord, connectez-vous à votre compte GitHub, cliquez sur votre photo de profil GitHub et sélectionnez Paramètres.

![Image](https://lh7-us.googleusercontent.com/tLIRoSttp2_c3XAlLPzt_TbxCrGT70wcAubnY3ilywK9kxiGJ-z_5pzX3rDECRpTxKpXx61esK_NL5t1Jkg0kQNfMnvU6hhvfa7TRr9wVX0WyhQWhcvWivDbEQOqtehc87MPXzinHvY_da3IkORxFy8)
_Connectez-vous à GitHub et sélectionnez "Paramètres" dans le menu de la barre latérale_

Ensuite, une fois que la nouvelle page apparaît, faites défiler jusqu'en bas et sélectionnez Paramètres du développeur.

![Image](https://lh7-us.googleusercontent.com/jmWCI4fxgLc34a7tZhqXA1hvD6QnBTF1_ERfsq7VwleIuv21frXVxFyoeuIVPz-0SwAD3fJK8hTqIc8pTGaijVQrFUAUptYfGcUmljisdqjAlhQgElkXRb8iO4OeW9YyZ_DOYal-6bkDhL-5RYcvifY)
_Faites défiler jusqu'en bas et sélectionnez "Paramètres du développeur"_

Sélectionnez Applications OAuth et cliquez sur Nouvelle application OAuth.

![Image](https://lh7-us.googleusercontent.com/2loAs8jJILhusyITEk6v2XUher8kP5jBZWEWuUszfD0_C1vD56L6hlIsAwXL7gMV_8gR28T1Mthv_VrSZwqWo2MuIVKdH0SfGsFWBZcK1M3FbMD6JTdszf1v56sKQHcpDYDsu7VSbfg0DFeQCPI6Af8)
_Création d'une nouvelle application OAuth_

Définissez votre application OAuth en lui donnant un nom.

* L'URL de la page d'accueil doit être l'URL qui mène à la page d'accueil de votre site web.
* L'URL de rappel d'autorisation doit être un site, ou une page que les utilisateurs voient après que leur compte GitHub a été authentifié. 

Une fois que vous avez terminé de la définir, cliquez sur Enregistrer l'application.

![Image](https://lh7-us.googleusercontent.com/2jEfTNBil-Z5qCakfh8HkptyMm4Z8WOxsUfoN6T9nclv9soRmR4akgJJxuc52Xqzo2f3uBPZ6a_UMGJR8eukFdZk6HxSwPSdrPLG5m2n5NLRJXroCvr8_56DwWvHjtmi7KqZvga48RFbpry--FJq9zg)
_Enregistrez votre application une fois que toutes les informations ont été remplies_

Ensuite, vous aurez besoin d'une clé secrète client et d'un identifiant client pour accéder à votre application GitHub OAuth sur votre projet Django.

L'identifiant client est déjà défini une fois que vous créez une application. Cliquez sur Générer une nouvelle clé secrète client pour créer une clé secrète client.

![Image](https://lh7-us.googleusercontent.com/Fl2B2iqfYUejqWlb04TRUgN6XNP3m4IswS2JptoS-cVkQ4ft3SElu8xV0cF04buhrLdl3zRo6OEtvpg7rGnJ0Yj22KbmONEz0HWbjRRRk6R0H-XIN-hoaBQUjyQl_XPzcCAPCBFPEhcet7WcDwTrBoU)
_Création d'une clé secrète client_

Il se peut que vous soyez invité à vous connecter. Faites-le pour continuer. 

![Image](https://lh7-us.googleusercontent.com/ceMI0FXuKACvZeA_S-RWYs2qjlCgkPzK9DbJtA6vIH6Nh5GvVHA66_rb9bHmtdxrM5VIzA3S6rpWbsCXURbrRjPrs4yHCLPttCC_9g1vNfQV5qeUN-eKAueE4EqKAmcvSThhJcav-53Jz1PsC7z4JMI)
_Connectez-vous pour continuer_

Une fois connecté, votre clé secrète client sera générée. Copiez-la et sauvegardez-la dans votre fichier .env.

![Image](https://lh7-us.googleusercontent.com/Y0trI-EIYeKVBT_s3TSA7A-5FEkONt4fNfdUKqHXdBqsfxyxfnl5E9_DL02eynpj87i-cBworbxusUIRdNaH_qU_2TaKRDM1afpuBjVZBsaq-2GZyf4dz4sE43hjx24hknJwkHwkaiZOTDLBZvjxbHk)
_Copiez votre clé secrète dans votre fichier .env_

Maintenant que vous avez configuré votre application GitHub OAuth, connectons-la à votre projet Django.

## Comment intégrer GitHub OAuth avec Django

Cette partie va lier votre application GitHub OAuth à votre projet Django en utilisant le package social-auth app.

Tout d'abord, installez le package [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) et définissez-le dans votre fichier settings.py.

```python
pip install dj-rest-auth
```

Ensuite, configurez le package dj-rest-auth dans votre fichier settings.py.

```python
# Définition de l'application
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "oauth2_provider",
    "users",
]
```

Vous devrez activer les classes d'authentification pour dj-rest-auth en mettant à jour REST_FRAMEWORK et AUTHENTICATION_BACKENDS dans votre fichier settings.py.

Optionnellement, vous pouvez configurer `allauth` si vous prévoyez d'utiliser des templates. Faites cela dans votre fichier settings.py. 

```python
AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)

REST_USE_JWT = True  # Utiliser JWT pour l'authentification avec dj-rest-auth
SITE_ID = 1 # Définir l'ID du site

SITE_ID = 1  # Définir l'ID du site

# Désactiver la vérification par email pour simplifier
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = "/"  # URL de redirection après une connexion réussie
LOGOUT_REDIRECT_URL = "/"  # URL de redirection après la déconnexion

SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "APP": {
            "client_id": "VOTRE_CLIENT_ID_GITHUB",
            "secret": "VOTRE_CLE_SECRETE_GITHUB",
            "key": "",
            "redirect_uri": "http://localhost:8000/accounts/github/login/callback/",
        }
    }
}
```

Une application Django est requise pour ce guide. Appelons-la users. Rendez-vous dans les vues de l'application Django et définissez le code suivant :

```python
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
    
class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = CALLBACK_URL_YOU_SET_ON_GITHUB
    client_class = OAuth2Client
        
# Définir les urls.py dans l'application Django
urlpatterns += [
    path('github/', GitHubLogin.as_view(), name='github_login')
    ]
```

## Comment configurer une nouvelle application

Pour spécifier les identifiants GitHub OAuth, vous devrez vous connecter au modèle d'application sociale Django. Cela fournira à votre projet Django un degré supplémentaire de protection. Grâce à cela, la modification des identifiants OAuth sera simple et n'endommagera pas votre code existant.

Commencez par vous connecter à votre admin Django, cliquez sur Applications sociales, et sélectionnez Ajouter une application. Cela vous invitera à créer une nouvelle application.

![Image](https://lh7-us.googleusercontent.com/9XQcRYZfLG8NOw-2ODor7Zgn-6x5Voq9F4ToVdp0eVLdnLnbWVkbB4PUEh68p3DJk9yjkKQf592_kDjipQQqHnpn7jeneWfu2X7Z4I2_n0wsltX5rGvbFSmyQteuDaXLUjWnNTBzDDJic6XQ8goBSd8)
_Dans l'admin Django, sélectionnez "Applications sociales"_

Vous serez invité à entrer des informations sur la nouvelle page.

* Sélectionnez GitHub comme fournisseur.
* Donnez un nom à votre application sociale.
* Entrez le Secret Client et l'ID Client créés à partir de votre application GitHub OAuth.
* Sélectionnez le site dans les sites disponibles et déplacez-le vers les sites choisis. Une fois terminé, cliquez sur Enregistrer. Cela créera une nouvelle application.

![Image](https://lh7-us.googleusercontent.com/pStq_1opKb7rkVNCqO2ouCfd2ZBLHFEwoxfWuHabFG12nT5v35NkXYSOH6Su2d_fISvwmO7LpCTfPsDK0EmmLUUvNYynoAgjuvsogP4Ee0xNBfIU_ai4TtXzzHZPFq2U0C3eFQfNCfXSuIoWup6PeCo)
_Créer/Ajouter une application sociale_

Changez le domaine de votre site en localhost puisque cela est encore la phase de développement.

![Image](https://lh7-us.googleusercontent.com/pRKpPs06V2j5ciPCLZRCd5weyc3X5HOGgWXhen_GS9-DhItBkkVJFYe6jBd3QmWMRwfBPagYxh6r1PRXHVeM_M3X6xWeq0lRKYM0GbVKDMlZS7hIVz4oAF6M6lMxYUGF5ZuuPwQyUF-1lfidzJPw79E)
_Sélectionnez "Site" pour changer le domaine du site existant_

Sélectionnez example.com et changez-le en http://127.0.0.1:8000/ puis Enregistrez.

![Image](https://lh7-us.googleusercontent.com/ikQ9_lhABi-avsKcoIqH98znI3aJKN4RkZqGfYQwio8nujR0M1kEewfBYdekhVkQMqYQi5APqsqxqpEkbX78wFS8dw76tGH11eEQ2qqTzCuabzgx5qD85SPBgkVtyJVEUui4RAKR_y2Dr65dEiyh7P4)
_Changez le domaine de votre site de example.com à http://127.0.0.1:8000/_

## Comment tester l'application sociale définie

Une fois que vous avez terminé de définir et de configurer l'application sociale Django sur votre projet, vous devrez la tester et vous assurer qu'elle fonctionne. 

Si vous ouvrez la route http://127.0.0.1:8000/auth/github/, vous devrez entrer certaines informations telles que le jeton d'accès, l'ID du jeton et le code. 

Nous obtiendrons ces informations manuellement, car le front-end est censé obtenir et analyser ces informations.

![Image](https://lh7-us.googleusercontent.com/eLkjj3nueZUf26fcORK9iJSvSyKNiO_ZgvfD9vFbF2momnDka6dVxngCQSKY9VwWcHJDduKDhGXhYsbimtSGZL5uzjrherU6bDXUFDfu5Bys1wylda6WZCOZsotH7ENkZAsHEYbhbImbx9JmbRKCtYM)
_Allez sur la page d'inscription GitHub pour tester l'application sociale définie_

Pour ce faire, rendez-vous sur https://github.com/settings/apps et sélectionnez Jetons d'accès personnel puis sélectionnez Générer un nouveau jeton. Utilisez la deuxième option, Générer un nouveau jeton (classique), car ce guide est axé sur l'authentification des utilisateurs pour obtenir leurs informations utilisateur GitHub.

![Image](https://lh7-us.googleusercontent.com/E8bb0KrJ0IwoTqCf2f2WVMoycUNad3YuqQZnG6heWwpNh3euYesNjx_ipRAOxYZyGfT-DShM1OyIOznVByQCWqsFrllTXO-FQEUIYPKLbjcbCBrp6vsN_XLlZJhaB3ZaxyBmWGiTMfWD5vjq0VWEq5g)
_Dans les paramètres GitHub, sélectionnez "Jetons d'accès personnel" puis sélectionnez "Générer un nouveau jeton"._

Donnez un nom au jeton et sélectionnez les étendues. Assurez-vous de cocher toutes les étendues utilisateur. Ensuite, générez un nouveau jeton.

![Image](https://lh7-us.googleusercontent.com/ZLkgWxuIQ1y-jZ3Pere1I-cmDIlwS032kQ0i5bvYufflVfnjhezcgNRqY-UpnJMPbJZY1RcdKApbTz579_DqR-Cs2M6ba3gTcaS6H2utA9JVkW2KVVXqsDjGwItruyBKpktd8TvlIDzVvlgQqh-RqUE)
_Définissez votre nouveau jeton_

Votre nouveau jeton devrait ressembler à ceci. Assurez-vous de le stocker quelque part en sécurité. 

![Image](https://lh7-us.googleusercontent.com/ywiFWxHFRJQwVZpGS-ePV7qR6YNIVi7gh3OoL9HgJvHc7TWHiSevr_Hmc8TRXbNxv0VAwwdt71O3PVchsLuRIlM9nbvhzj8X4IWBtgAjx17M8yYGApqxgBlU1lKeQYg8xwdwCg1PchuqiLuyj8YRCAg)
_Copiez le jeton d'accès personnel généré par GitHub._

Rendez-vous sur http://127.0.0.1:8000/auth/github/. Entrez le jeton d'accès généré et voilà ! Votre jeton d'accès utilisateur et votre nom d'utilisateur GitHub seront envoyés en réponse dans le corps. 

![Image](https://lh7-us.googleusercontent.com/jd736d5yvsSPhvXCNX21CGHEzTdMhUerN4HVst57iOVqisAejH_T35D7AwKGGHgkJCtkzfkn4ut0YP2vxpYZgSa7ITEqaR2Wqw0J4qxWeIug0ciCEFM4GnDK-DjfooYRzg1sbU1z8cyFMtwRmgMG_bs)
_Utilisez votre jeton et votre nom d'utilisateur GitHub pour vous assurer que le système backend fonctionne_

## Comment implémenter le flux d'authentification OAuth

Vous avez installé et testé avec succès le package dj-rest-auth. Ensuite, vous apprendrez comment tester le flux OAuth et comment il obtient les données utilisateur de GitHub.

Pour tester le flux d'authentification GitHub OAuth, vous devrez envoyer une requête à https://github.com/login/oauth/authorize.

Vous pouvez le faire soit en utilisant curl :

```python
"https://github.com/login/oauth/authorize?client_id=VOTRE_CLIENT_ID&redirect_uri=http://127.0.0.1:8000/auth/callback/&scope=user"
```

(et en vous assurant d'utiliser la même URI de redirection définie dans votre application GitHub OAuth) ou en ouvrant https://github.com/login/oauth/authorize?client_id=VOTRE_CLIENT_ID&redirect_uri=http://127.0.0.1:8000/auth/callback/&scope=user sur votre navigateur. Cela vous redirigera vers une page d'autorisation. 

![Image](https://lh7-us.googleusercontent.com/rJbNTlLFz8h-dMJNgeeMCX-kT-Y_Ofv-1Po0wNp2qZQVH_e6syyabIasdrjWzDDdtF6NQ-2o2oDxv_KX2wYmoUb7OiYcZGz66sbzNjfpfB0P3asAFh4oPV7OvybcQ4OYtiGKAUNYYvqAUt7H1-sn7mM)
_Envoyez une requête au flux d'authentification GitHub OAuth_

Cliquez sur Autoriser VOTRE_NOM_D_UTILISATEUR pour autoriser l'utilisateur.

![Image](https://lh7-us.googleusercontent.com/8GaW8izjQgcqd-9IbCeyDZcdnajXKBDETOIiZ5P2s3iziZQMUvROKmJQuJBDvmPdpAEEhSCCB_xdy1NSkgEEqU2o18lmwsbo8Eay8IYzKL-HJCKoB40ySLE9-vl3g5CLtMyuzmSwQy9u_fyI2iqfuwg)
_Cliquez sur "Autoriser" pour autoriser votre utilisateur GitHub_

Vous serez redirigé vers une URL affichant le code. Avec ce code, vous pouvez générer le jeton d'accès nécessaire pour authentifier l'utilisateur.

![Image](https://lh7-us.googleusercontent.com/_RO4IqpLY0-zg8SiW7SXKk1gTCkJq_bVqIrDzH4_tzqWSzHUArqsQlDYSqzFHiGfxdyPpSXW5psYKnZVyHPgnDbETBncgpIrWxZAWc1RjQvcGmi5QRN5XpOyOxuy5n5DqiJkSJO8c0VizOFh3h-tqy4)
_Utilisez le code de GitHub pour générer un jeton d'accès pour votre authentification_

Pour obtenir le jeton d'accès, envoyez une requête à cette URL : https://github.com/login/oauth/access_token?client_id=VOTRE_CLIENT_ID&client_secret=VOTRE_CLE_SECRETE&code=CODE 

Ou vous pouvez choisir d'utiliser curl pour envoyer la requête. 

```curl
"https://github.com/login/oauth/access_token?client_id=VOTRE_CLIENT_ID&client_secret=VOTRE_CLE_SECRETE&code=CODE"
```

Cela devrait soit télécharger le jeton d'accès pour vous, soit le retourner comme corps de réponse, selon la manière dont vous l'avez défini. La réponse devrait ressembler à ceci :

![Image](https://lh7-us.googleusercontent.com/ZIn4u5kqdW3P7o27ReEsAyc-X9R2O28Bm2qfjDh0saywx7vpso41OLoOldHzii4AbnQe-jfqT__4aELgchdXUSQPIR6I86-KdOyZL4hrcFI38YBOjX27IbH2NNtS7SWS7hAFNTroZfVF17s8xoI0lBk)
_Votre réponse de votre système d'authentification backend_

Maintenant, avec ce jeton, vous pouvez authentifier votre utilisateur lorsqu'il fait une requête. 

## Conclusion

En conclusion, la configuration de GitHub OAuth sur Django est un moyen utile de permettre aux utilisateurs de se connecter à vos applications web en utilisant leurs identifiants GitHub. 

En suivant ce guide, vous pouvez améliorer la sécurité de votre application et accéder aux données de vos utilisateurs, ce qui améliore l'expérience utilisateur de votre application Django.