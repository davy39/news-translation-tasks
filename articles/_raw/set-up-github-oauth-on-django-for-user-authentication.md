---
title: How to Set Up GitHub OAuth in a Django App for User Authentication
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2023-12-05T21:19:14.000Z'
originalURL: https://freecodecamp.org/news/set-up-github-oauth-on-django-for-user-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Blog-Banner---Template.png
tags:
- name: authentication
  slug: authentication
- name: Django
  slug: django
- name: GitHub
  slug: github
- name: oauth
  slug: oauth
seo_title: null
seo_desc: "Maintaining safe and frictionless user authentication is paramount in today's\
  \ fast-changing web application landscape. \nAmong the many authentication methods\
  \ available, GitHub OAuth has emerged as a useful tool for improving user login\
  \ experience whi..."
---

Maintaining safe and frictionless user authentication is paramount in today's fast-changing web application landscape. 

Among the many authentication methods available, GitHub OAuth has emerged as a useful tool for improving user login experience while strengthening security measures. 

[Django](https://docs.djangoproject.com/en/4.2/), a Python web framework, has recently gained popularity in web development due to its efficiency and versatility. Adding GitHub OAuth to your Django projects helps improve the authentication process. 

Django developers can use GitHub OAuth to access a user's GitHub profile and (with permission) their repositories to personalize the user experience and tailor application services.

This article will walk you through how to implement GitHub OAuth. You'll see the benefits to your Django projects as we go. By embracing this technology, you can give users a seamless login experience while adhering to strict security standards.

## Prerequisites

If you wish to follow this guide, you need to have a basic understanding of these tools or have them installed on your PC: 

* [GitHub](https://github.com/)
* [Django](https://docs.djangoproject.com/en/4.2/)
* [Django Rest Framework](https://www.django-rest-framework.org/)

## How to Create a GitHub OAuth Application

You must sign into your GitHub account to create a GitHub OAuth application. 

First, login to your GitHub account, click on your GitHub profile picture, and select Settings.

![Image](https://lh7-us.googleusercontent.com/tLIRoSttp2_c3XAlLPzt_TbxCrGT70wcAubnY3ilywK9kxiGJ-z_5pzX3rDECRpTxKpXx61esK_NL5t1Jkg0kQNfMnvU6hhvfa7TRr9wVX0WyhQWhcvWivDbEQOqtehc87MPXzinHvY_da3IkORxFy8)
_Login to GitHub and select "Settings" from the sidebar menu_

Then, once the new page comes up, scroll to the bottom and select Developer Settings.

![Image](https://lh7-us.googleusercontent.com/jmWCI4fxgLc34a7tZhqXA1hvD6QnBTF1_ERfsq7VwleIuv21frXVxFyoeuIVPz-0SwAD3fJK8hTqIc8pTGaijVQrFUAUptYfGcUmljisdqjAlhQgElkXRb8iO4OeW9YyZ_DOYal-6bkDhL-5RYcvifY)
_Scroll to the bottom and select "Develop Settings"_

Select OAuth Apps and click on New OAuth App.

![Image](https://lh7-us.googleusercontent.com/2loAs8jJILhusyITEk6v2XUher8kP5jBZWEWuUszfD0_C1vD56L6hlIsAwXL7gMV_8gR28T1Mthv_VrSZwqWo2MuIVKdH0SfGsFWBZcK1M3FbMD6JTdszf1v56sKQHcpDYDsu7VSbfg0DFeQCPI6Af8)
_Creating a new OAuth app_

Define your OAuth application by naming it.

* The Homepage URL should be the URL that leads to the homepage of your website.
* The Authorization callback URL should be a site, or a page users view after their GitHub account has been authenticated. 

Once you are done defining it, click Register application.

![Image](https://lh7-us.googleusercontent.com/2jEfTNBil-Z5qCakfh8HkptyMm4Z8WOxsUfoN6T9nclv9soRmR4akgJJxuc52Xqzo2f3uBPZ6a_UMGJR8eukFdZk6HxSwPSdrPLG5m2n5NLRJXroCvr8_56DwWvHjtmi7KqZvga48RFbpry--FJq9zg)
_Register your application once all the info has been filled in_

Next, you'll need a client secret and a client ID key to access your GitHub OAuth app on your Django project.

The Client ID is already defined once you create an application. Click Generate a new client secret to create a client secret key.

![Image](https://lh7-us.googleusercontent.com/Fl2B2iqfYUejqWlb04TRUgN6XNP3m4IswS2JptoS-cVkQ4ft3SElu8xV0cF04buhrLdl3zRo6OEtvpg7rGnJ0Yj22KbmONEz0HWbjRRRk6R0H-XIN-hoaBQUjyQl_XPzcCAPCBFPEhcet7WcDwTrBoU)
_Creating a client secret key_

You might be prompted to sign in. Do so to continue. 

![Image](https://lh7-us.googleusercontent.com/ceMI0FXuKACvZeA_S-RWYs2qjlCgkPzK9DbJtA6vIH6Nh5GvVHA66_rb9bHmtdxrM5VIzA3S6rpWbsCXURbrRjPrs4yHCLPttCC_9g1vNfQV5qeUN-eKAueE4EqKAmcvSThhJcav-53Jz1PsC7z4JMI)
_Sign in to continue_

Once you log in, your client's secret key will be generated. Copy and save it on your .env file.

![Image](https://lh7-us.googleusercontent.com/Y0trI-EIYeKVBT_s3TSA7A-5FEkONt4fNfdUKqHXdBqsfxyxfnl5E9_DL02eynpj87i-cBworbxusUIRdNaH_qU_2TaKRDM1afpuBjVZBsaq-2GZyf4dz4sE43hjx24hknJwkHwkaiZOTDLBZvjxbHk)
_Copy your secret key to your .env file_

Now that you’ve set up your GitHub OAuth application, let’s connect it to your Django project.

## How to Integrate GitHub OAuth with Django

This part will link your Django project's GitHub OAuth application to it using the social-auth app package. 

First, install the [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) package and define it on your settings.py.

```python
pip install dj-rest-auth
```

Then configure dj-rest-auth package on your settings.py.

```python
# Application definition
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

You'll need to enable the authentication classes for dj-rest-auth by updating REST_FRAMEWORK and AUTHENTICATION_BACKENDS on your settings.py.

Optionally, you can configure `allauth` if you intend to use templates. Do this on your settings.py file. 

```python
AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)

REST_USE_JWT = True  # Use JWT for authentication with dj-rest-auth
SITE_ID = 1 #Set site ID

SITE_ID = 1  # Set the site ID

# Disable email verification for simplicity
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = "/"  # Redirect URL after successful login
LOGOUT_REDIRECT_URL = "/"  # Redirect URL after logout

SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "APP": {
            "client_id": "YOUR_GITHUB_CLIENT_ID",
            "secret": "YOUR_GITHUB_SECRET_KEY",
            "key": "",
            "redirect_uri": "http://localhost:8000/accounts/github/login/callback/",
        }
    }
}
```

A Django app is required for this guide. Let's call it users. Head over to the views of the Django app and define the following code:

```python
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
    
class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = CALLBACK_URL_YOU_SET_ON_GITHUB
    client_class = OAuth2Client
        
# Define the urls.py on the Django app
urlpatterns += [
    path('github/', GitHubLogin.as_view(), name='github_login')
    ]
```

## How to Set Up a New Application

To specify the GitHub OAuth credentials, you'll need to log into the Django social application model. This will provide your Django project with an additional degree of protection. Because of this, changing the OAuth credentials will be simple and won't damage your existing code.

Start by logging into your Django admin, clicking Social Applications, and selecting Add Application. This will prompt you to create a new application.

![Image](https://lh7-us.googleusercontent.com/9XQcRYZfLG8NOw-2ODor7Zgn-6x5Voq9F4ToVdp0eVLdnLnbWVkbB4PUEh68p3DJk9yjkKQf592_kDjipQQqHnpn7jeneWfu2X7Z4I2_n0wsltX5rGvbFSmyQteuDaXLUjWnNTBzDDJic6XQ8goBSd8)
_On Django admin, select "Social applications"_

You will be prompted to enter information on the new page.

* Select GitHub as the provider.
* Give your social app a name.
* Enter the Client Secret and Client ID created from your GitHub OAuth app.
* Select the site on Available sites and move it to Chosen sites. Once done, click Save. This will create a new application.

![Image](https://lh7-us.googleusercontent.com/pStq_1opKb7rkVNCqO2ouCfd2ZBLHFEwoxfWuHabFG12nT5v35NkXYSOH6Su2d_fISvwmO7LpCTfPsDK0EmmLUUvNYynoAgjuvsogP4Ee0xNBfIU_ai4TtXzzHZPFq2U0C3eFQfNCfXSuIoWup6PeCo)
_Create/Add a Social application_

Change your site domain to localhost since this is still the development phase.

![Image](https://lh7-us.googleusercontent.com/pRKpPs06V2j5ciPCLZRCd5weyc3X5HOGgWXhen_GS9-DhItBkkVJFYe6jBd3QmWMRwfBPagYxh6r1PRXHVeM_M3X6xWeq0lRKYM0GbVKDMlZS7hIVz4oAF6M6lMxYUGF5ZuuPwQyUF-1lfidzJPw79E)
_Select, "Site" to change the existing the site domain_

Select example.com and change it to http://127.0.0.1:8000/ then Save.

![Image](https://lh7-us.googleusercontent.com/ikQ9_lhABi-avsKcoIqH98znI3aJKN4RkZqGfYQwio8nujR0M1kEewfBYdekhVkQMqYQi5APqsqxqpEkbX78wFS8dw76tGH11eEQ2qqTzCuabzgx5qD85SPBgkVtyJVEUui4RAKR_y2Dr65dEiyh7P4)
_Change your site domain from example.com to http://127.0.0.1:8000/_

## How to Test the Defined Social App

Once you are done defining and setting up the social Django app on your project, you will need to test it and make sure that it works. 

If you open the route http://127.0.0.1:8000/auth/github/, you'll need to enter some information such as Access token, ID token, and code. 

We'll manually get this information, as the front end is meant to get and parse this information.

![Image](https://lh7-us.googleusercontent.com/eLkjj3nueZUf26fcORK9iJSvSyKNiO_ZgvfD9vFbF2momnDka6dVxngCQSKY9VwWcHJDduKDhGXhYsbimtSGZL5uzjrherU6bDXUFDfu5Bys1wylda6WZCOZsotH7ENkZAsHEYbhbImbx9JmbRKCtYM)
_Go to the GitHub registration page to test the defined social app_

To do this, head over to https://github.com/settings/apps and select Personal access tokens then select Generate new token. Use the second option, Generate new token (classic), since this guide is focused on authenticating users just to get their GitHub user info.

![Image](https://lh7-us.googleusercontent.com/E8bb0KrJ0IwoTqCf2f2WVMoycUNad3YuqQZnG6heWwpNh3euYesNjx_ipRAOxYZyGfT-DShM1OyIOznVByQCWqsFrllTXO-FQEUIYPKLbjcbCBrp6vsN_XLlZJhaB3ZaxyBmWGiTMfWD5vjq0VWEq5g)
_On GitHub settings, select "Personal access tokens" then select "Generate new token"._

Give the token a name and select scopes. Ensure you check all the user scopes.  Then generate a new token.

![Image](https://lh7-us.googleusercontent.com/ZLkgWxuIQ1y-jZ3Pere1I-cmDIlwS032kQ0i5bvYufflVfnjhezcgNRqY-UpnJMPbJZY1RcdKApbTz579_DqR-Cs2M6ba3gTcaS6H2utA9JVkW2KVVXqsDjGwItruyBKpktd8TvlIDzVvlgQqh-RqUE)
_Define your new token_

Your new token should look like this. Ensure you store it somewhere safe. 

![Image](https://lh7-us.googleusercontent.com/ywiFWxHFRJQwVZpGS-ePV7qR6YNIVi7gh3OoL9HgJvHc7TWHiSevr_Hmc8TRXbNxv0VAwwdt71O3PVchsLuRIlM9nbvhzj8X4IWBtgAjx17M8yYGApqxgBlU1lKeQYg8xwdwCg1PchuqiLuyj8YRCAg)
_Copy the generated personal access token generated by GitHub._

Head over to http://127.0.0.1:8000/auth/github/. Enter the access token generated and voilà!  Your user access token and GitHub username will be sent as a response on the body. 

![Image](https://lh7-us.googleusercontent.com/jd736d5yvsSPhvXCNX21CGHEzTdMhUerN4HVst57iOVqisAejH_T35D7AwKGGHgkJCtkzfkn4ut0YP2vxpYZgSa7ITEqaR2Wqw0J4qxWeIug0ciCEFM4GnDK-DjfooYRzg1sbU1z8cyFMtwRmgMG_bs)
_Using your token and GitHub username ensure the backend system works_

## How to Implement OAuth Authentication Flow

You have successfully installed and tested the dj-rest-auth package. Next, you will learn how to test the OAuth flow and how it obtains user data from GitHub.

To test the GitHub OAuth authentication flow, you'll need to send a request to https://github.com/login/oauth/authorize.

You can do so by either using curl:

```python
"https://github.com/login/oauth/authorize?client_id=YOUR_CLIENT_ID&amp;redirect_uri=http://127.0.0.1:8000/auth/callback/&amp;scope=user"
```

(and making sure you use the same redirect URI defined in your GitHub OAuth application) or opening https://github.com/login/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=http://127.0.0.1:8000/auth/callback/&scope=user on your browser. It will redirect you to an authorization page. 

![Image](https://lh7-us.googleusercontent.com/rJbNTlLFz8h-dMJNgeeMCX-kT-Y_Ofv-1Po0wNp2qZQVH_e6syyabIasdrjWzDDdtF6NQ-2o2oDxv_KX2wYmoUb7OiYcZGz66sbzNjfpfB0P3asAFh4oPV7OvybcQ4OYtiGKAUNYYvqAUt7H1-sn7mM)
_Send a request to GitHub OAuth authentication flow_

Click Authorize YOUR USERNAME to authorize the user.

![Image](https://lh7-us.googleusercontent.com/8GaW8izjQgcqd-9IbCeyDZcdnajXKBDETOIiZ5P2s3iziZQMUvROKmJQuJBDvmPdpAEEhSCCB_xdy1NSkgEEqU2o18lmwsbo8Eay8IYzKL-HJCKoB40ySLE9-vl3g5CLtMyuzmSwQy9u_fyI2iqfuwg)
_Click "Authorize" to authorize your GitHub user_

You will be redirected to a URL showing the code. With the code, you can generate the access token needed to authenticate the user.

![Image](https://lh7-us.googleusercontent.com/_RO4IqpLY0-zg8SiW7SXKk1gTCkJq_bVqIrDzH4_tzqWSzHUArqsQlDYSqzFHiGfxdyPpSXW5psYKnZVyHPgnDbETBncgpIrWxZAWc1RjQvcGmi5QRN5XpOyOxuy5n5DqiJkSJO8c0VizOFh3h-tqy4)
_Use the code from GitHub to generate an access token for your auth_

To get the access token, send a request to this URL: https://github.com/login/oauth/access_token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&code=CODE 

Or you can choose to use curl to send the request. 

```curl
"https://github.com/login/oauth/access_token?client_id=YOUR_CLIENT_ID&amp;client_secret=YOUR_CLIENT_SECRET&amp;code=CODE"
```

This should either download the access token for you or return it as a response body depending on how you defined it. The response should look like this:

![Image](https://lh7-us.googleusercontent.com/ZIn4u5kqdW3P7o27ReEsAyc-X9R2O28Bm2qfjDh0saywx7vpso41OLoOldHzii4AbnQe-jfqT__4aELgchdXUSQPIR6I86-KdOyZL4hrcFI38YBOjX27IbH2NNtS7SWS7hAFNTroZfVF17s8xoI0lBk)
_Your response from your backend authentication system_

Now, with this token, you can authenticate your user when they make any request. 

## Conclusion

In conclusion, setting up GitHub OAuth on Django is a helpful way to enable users to log in to your web applications using their GitHub credentials. 

By following this guide, you can enhance your application's security and access your users' data which improves the user experience of your Django app.   

