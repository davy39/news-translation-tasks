---
title: How Time-based One-Time Passwords work and why you should use them in your
  app.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T23:14:56.000Z'
originalURL: https://freecodecamp.org/news/how-time-based-one-time-passwords-work-and-why-you-should-use-them-in-your-app-fdd2b9ed43c3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NtO_nq3H7lfuDd9nL9pRWg.jpeg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Two-factor authentication
  slug: two-factor-authentication
seo_title: null
seo_desc: 'By Prakash Sharma

  With the increase in cyber security threats, it has become more and more necessary
  to upgrade the security standards of your web applications. You need to make sure
  your users’ accounts are safe.

  Nowadays, a lot of online web applic...'
---

By Prakash Sharma

With the increase in cyber security threats, it has become more and more necessary to upgrade the security standards of your web applications. You need to make sure your users’ accounts are safe.

Nowadays, a lot of online web applications are asking users to add an extra layer of security for their account. They do it by enabling 2-factor authentication. There are various methods of implementing 2-factor authentication, and TOTP (the Time-based One-Time Password algorithm) authentication is one of them.

This article explains what it is, and how and why to use it. But before understanding that, let’s first briefly take a look at what two-factor authentication means.

### What is Two Factor Authentication?

Two-factor authentication (or multi factor authentication) is just an extra layer of security for a user’s account. That means that, after enabling two factor authentication, the user has to go through one more step to log in successfully. For example, the usual steps for logging in to an account are:

![Image](https://cdn-media-1.freecodecamp.org/images/ZqTllcloHTWpzWYDh-YsnOggoitxJSicGiVj)

But after enabling 2-factor authentication, the steps look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/inJY5oemUFqSO2g5G6HvPpNt0I74XF0hlRKV)

So this adds one more step to the login process. This method is more secure, because a criminal cannot access the user’s account unless they have access to both the user’s regular password and one time password.

Currently, there are two widely used methods to get that one time password:

1. **SMS-based:** In this method, every time the user logs in, they receive a text message to their registered phone number, which contains a One Time Password.
2. **TOTP-based:** In this method, while enabling 2-factor authentication, the user is asked to scan a QR image using a specific smartphone application.   
That application then continuously generates the One Time Password for the user.

The SMS-based method does not need any explanation. It’s easy, but it has its own problems, like waiting for the SMS on every login attempt, security issues, and so on. The TOTP-based method is becoming popular because of it’s advantages over the SMS-based method. So let’s understand how the TOTP-based method works.

### How the TOTP-based method works

Before understanding this, let’s first discuss what problems this method will solve for us.

By using the TOTP method, we are creating a one time password on the user side (instead of server side) through a smartphone application.

This means that users always have access to their one time password. So it prevents the server from sending a text message every time user tries to login.

Also, the generated password changes after a certain time interval, so it behaves like a one time password.

Great! Now let’s understand the workings of the TOTP-method and try to implement the above solution ourselves. Our requirement here is to create a password on the user side, and that password should keep changing.

The following could be a way to implement this solution:

```
When the user enables two factor authentication:
```

```
1. Backend server creates a secret key for that particular user.2. Server then shares that secret key with the user’s phone application.3. Phone application initializes a counter.4. Phone application generate a one time password using that secret key and counter.5. Phone application changes the counter after a certain interval and regenerates the one time password making it dynamic.
```

This should work, but there are three main problems with it:

1. How will the application generate a one time password using a secret key and counter?
2. How will the counter update? How will the web server keep track of the counter?
3. How will the server share the secret key with the phone’s application?

The solution to the first problem is defined in the HOTP algorithm.

### Understanding HOTP:

HOTP stands for “HMAC-Based One-Time Password”. This algorithm was published as [RFC4226](https://tools.ietf.org/html/rfc4226) by the [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force) (IETF). HOTP defines an algorithm to create a one time password from a secret key and a counter.

You can use this algorithm in two steps:

1. The first step is to create an [HMAC](https://en.wikipedia.org/wiki/HMAC) hash from a secret key and counter.

```
// Obtain HMAC hash (using SHA-1 hashing algorithm) by secretKey and counter
```

```
hmacHash = HMAC-SHA-1(secretKey, counter);
```

2. In this code, the output would be a 20 byte long string. That long string is not suitable as a one time password. So we need a way to truncate that string. HOTP defines a way to truncate that string to our desired length.

```
// hmacHash[19] means 19th byte of the string.offset = hmacHash[19] & 0xf;
```

```
truncatedHash = (hmacHash[offset++] & 0x7f) << 24 | (hmacHash[offset++] & 0xff) << 16 | (hmacHash[offset++] & 0xff) << 8 | (hmacHashh[offset++] & 0xff);
```

```
finalOTP = (truncatedHash % (10 ^ numberOfDigitsRequiredInOTP));
```

It might look scary, but it is not. In this algorithm, we first obtain `offset` which is the last 4 bits of `hmacHash[19]`. After that, we concatenate the bytes from `hmacHash[offset]` to `hmacHash[offset+3]` and store the last 31 bits to `truncatedHash`. Finally, using a simple modulo operation, we obtain the one time password that’s a reasonable length.

This pretty much defines the HOTP algorithm. The [RFA4226](https://tools.ietf.org/html/rfc4226) doc explains why this is the most secure way to obtain a one time password from these two values.

Great! So we have found a way to obtain a one time password using a secret key and counter. But what about the second problem? How to keep track of the counter?

The solution to second problem is found in the TOTP.

### Understanding TOTP:

TOTP stands for “Time-Based One-Time Password”. This was published as [RFC6238](https://tools.ietf.org/html/rfc6238) by [IETF](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force).

A TOTP uses the HOTP algorithm to obtain the one time password. The only difference is that it uses “Time” in the place of “counter,” and that gives the solution to our second problem.

That means that instead of initializing the counter and keeping track of it, we can use time as a counter in the HOTP algorithm to obtain the OTP. As a server and phone both have access to time, neither of them has to keep track of the counter.

Also, to avoid the problem of different time zones of the server and phone, we can use a [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time), which is independent of time zones.

However the Unix time is defined in seconds, so it changes every second. That means the generated password will change every second which is not good. Instead, we need to add a significant interval before changing the password. For example, the Google Authenticator App changes the code every 30 seconds.

```
counter = currentUnixTime / 30
```

So we have solved the problem of the counter. Now we need to address our third problem: sharing the secret key with the phone application. Here, a QR code can help us.

### Using a QR code

Though we can ask the users to type the secret key into their phone application directly, we want to make secret keys quite long for security reasons. Asking the user to type in such a long string would not be a user friendly experience.

Since the majority of smartphones are equipped with a camera, we can use it and ask the user to scan a QR code to obtain the secret key from it. So all we need to do is to convert the secret key in the QR code and show it to the user.

We have solved all three problems! And now you know how TOTP works. Let’s see how to implement it in an application.

### How to implement TOTP

There are some free phone applications (like Google Authenticator App, Authy, and so on) available which can generate an OTP for the user. Therefore, in most cases, creating your own phone application is not necessary.

The following pseudo codes explain a way to implement TOTP-based 2-factor authentication in a web application.

```
When user request to enable 2-factor authentication
```

```
// Generate a secret key of length 20.secretKey = generateSecretKey(20);
```

```
// Save that secret key in database for this particular user.saveUserSecretKey(userId, secretKey);
```

```
// convert that secret key into qr image.qrCode = convertToQrCode(secretKey);
```

```
// send the qr image as responseresponse(qrCode);
```

The user is asked to scan that QR code. When the phone application scans the QR code, it gets the user’s secret key. Using that secret key, the current Unix time, and the HOTP algorithm, the phone application will generate and display the password.

We ask the user to type the generated code after scanning the QR code. This is required, because we want to make sure that the user has successfully scanned the image and the phone application has successfully generated the code.

```
User types the code displayed in the application.
```

```
// Fetch secret key from database.secretKey = getSecretKeyOfUser(userId);
```

```
if (codeTypedByUser == getHOTP(secretKey, currentUnixTime / 30)) {   enableTwoFactorAuthentication(userId);}
```

Here we use the HOTP algorithm on the server side to get the OTP-based authentication on the secret key and current unix time. If that OTP is the same as the one typed by the user, then we can enable 2-factor authentication for that user.

Now after every login operation, we need to check if this particular user has 2-factor authentication enabled. If it is enabled, then we ask for the one time password displayed in the phone application. And if that typed code is correct, only then is the user authenticated.

```
User types the code displayed in the phone application to login
```

```
// Fetch secret key from database.secretKey = getSecretKeyOfUser(userId);
```

```
if (codeTypedByUser == getHOTP(secretKey, currentUnixTime)) {   signIn(userId);}
```

### What happens if the user loses the code?

There are a couple of ways to help the user to recover the code. Usually when they are enabling 2-factor authentication, we can show the secret key to them along with the QR code and ask them to save that code somewhere safely.

Applications like Google Authenticator App let you generate the password by directly entering the secret key. If the user loses the code, they can enter that safely saved secret key in the phone application to generate the OTP again.

If we have the user’s phone number, we can also use the SMS-based method to send an OTP to the user to help them recover the code.

### Wrapping Up

Two factor authentication is gaining popularity. A lot of web applications are implementing it for extra security.

Unlike the SMS-based method, the TOTP method does not require a lot of extra effort either. So this feature is worth implementing for any application.

