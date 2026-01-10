---
title: How to set up React Native authentication with react-native-app-auth
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-01T17:07:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-react-native-authentication-with-react-native-app-auth-f6fd66e0e6d0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*k2549xFsiA_FKSv0
tags:
- name: app development
  slug: app-development
- name: authentication
  slug: authentication
- name: React Native
  slug: react-native
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Melih Yumak

  Versions

  Before we start, make sure you have the following versions installed:

  “react”: “16.8.3”,“react-native”: “0.59.1”,“react-native-contacts”: “3.1.5”,

  Here’s the link to the Github repo if you want to check it out: https://github....'
---

By Melih Yumak

#### Versions

Before we start, make sure you have the following versions installed:

“react”: “16.8.3”,  
“react-native”: “0.59.1”,  
“react-native-contacts”: “3.1.5”,

**Here’s the link to the Github repo if you want to check it out**: [https://github.com/FormidableLabs/react-native-app-auth](https://github.com/FormidableLabs/react-native-app-auth)

**React-native-app-auth** is used to provide authentication in your react-native applications. In my case, I was trying to use it with Google, so here is an explanation how you can install and use it for the versions above.

In their documentation it’s also explained as a React Native bridge for [AppAuth-iOS](https://github.com/openid/AppAuth-iOS) and [AppAuth-Android](https://github.com/openid/AppAuth-Android) SDKS for communicating with [OAuth 2.0](https://tools.ietf.org/html/rfc6749) and [OpenID Connect](http://openid.net/specs/openid-connect-core-1_0.html) providers.

### Tested OpenID providers:

These providers are OpenID compliant, which means you can use [autodiscovery](https://openid.net/specs/openid-connect-discovery-1_0.html):

* [Identity Server4](https://demo.identityserver.io/) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/identity-server-4.md))
* [Identity Server3](https://github.com/IdentityServer/IdentityServer3.md) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/identity-server-3.md))
* [Google](https://developers.google.com/identity/protocols/OAuth2) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/google.md))
* [Okta](https://developer.okta.com/) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/okta.md))
* [Keycloak](http://www.keycloak.org/) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/keycloak.md))
* [Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/azure-active-directory.md))
* [AWS Cognito](https://eu-west-1.console.aws.amazon.com/cognito) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/aws-cognito.md))

### Tested OAuth2 providers:

These providers implement the OAuth2 spec, but are not OpenID providers, which means you must configure the authorization and token endpoints yourself.

* [Uber](https://developer.uber.com/docs/deliveries/guides/three-legged-oauth.md) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/uber))
* [Fitbit](https://dev.fitbit.com/build/reference/web-api/oauth2/) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/fitbit.md))
* [Dropbox](https://www.dropbox.com/developers/reference/oauth-guide) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/dropbox.md))
* [Reddit](https://github.com/reddit-archive/reddit/wiki/oauth2) ([Example configuration](https://github.com/FormidableLabs/react-native-app-auth/blob/master/docs/config-examples/reddit.md))

#### **Installation**

```
npm install react-native-app-auth --savereact-native link react-native-app-auth
```

**IOS**  
In the documentation, there are three ways to implement this state but I prefer **CocoaPods.**

If you are using CocoaPods for the first time, please complete the steps below:

```
sudo gem install cocoapods
```

From your root folder open

```
cd ios
```

```
pod init
```

The pod init command will initialise the Podfile in your iOS directory.

Then add this line below in your Podfile after **target ‘your_app’ do**

```
pod 'AppAuth', '0.95.0'
```

#### **Register redirect URL scheme**

If you intend to support iOS 10 and older, you need to define the supported redirect URL schemes in your `Info.plist` as follows:

Note: you will get these values from **oauth provider**.   
For google: [https://console.developers.google.com/](https://console.developers.google.com/)

```
<key>CFBundleURLTypes</key><array>  <dict>    <key>CFBundleURLName</key>    <string>com.your.app.identifier</string>    <key>CFBundleURLSchemes</key>    <array>      <string>io.identityserver.demo</string>    </array>  </dict></array>
```

* `CFBundleURLName` is any globally unique string. A common practice is to use your app identifier.
* `CFBundleURLSchemes` is an array of URL schemes your app needs to handle. The scheme is the beginning of your OAuth Redirect URL, up to the scheme separator (`:`) character.

#### **Define openURL callback in AppDelegate**

You need to retain the auth session in order to continue the authorization flow from the redirect. Follow these steps:

Make `AppDelegate` conform to `RNAppAuthAuthorizationFlowManager` with the following changes to `AppDelegate.h`:

```
+ #import "RNAppAuthAuthorizationFlowManager.h"
```

```
- @interface AppDelegate : UIResponder <UIApplicationDelegate>+ @interface AppDelegate : UIResponder <UIApplicationDelegate, RNAppAuthAuthorizationFlowManager>
```

```
+ @property(nonatomic, weak)id<RNAppAuthAuthorizationFlowManagerDelegate>authorizationFlowManagerDelegate;
```

Change the following method from `UIApplicationDelegate` in `AppDelegate.m`:

```
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options { return [self.authorizationFlowManagerDelegate resumeExternalUserAgentFlowWithURL:url];}
```

**Android**

After successful linking you should add **android/app/build.grandle** file defaultConfig value as your identifiers redirect url.

```
manifestPlaceholders = [
```

```
appAuthRedirectScheme: “io.identityserver.demo”
```

```
]
```

#### Usage

```
import { authorize } from 'react-native-app-auth';
```

```
// base configconst config = {  issuer: '<YOUR_ISSUER_URL>',  clientId: '<YOUR_CLIENT_ID>',  redirectUrl: '<YOUR_REDIRECT_URL>',  scopes: ['<YOUR_SCOPES_ARRAY>'],};
```

```
// use the client to make the auth request and receive the authStatetry {  const result = await authorize(config);  // result includes accessToken, accessTokenExpirationDate and refreshToken} catch (error) {  console.log(error);}
```

**Happy Coding!**

**Thank you for reading this far. If you enjoyed this post, please share, comment, and press that ? a few times (up to 50 times). . . Maybe it will help someone.**

**Follow me on Medium or [Github](https://github.com/hadnazzar) if you’re interested in more in-depth and informative write-ups like these in the future.** ?

