---
title: How to Catch Hackers in Your Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-05T16:57:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-catch-hackers-in-your-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/How-to-Catch-Hackers-in-Your-Code.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Security
  slug: security
- name: software development
  slug: software-development
seo_title: null
seo_desc: "By Bedirhan Urgun\nWhat would you do if hackers were abusing your software\
  \ in production? \nThis is not a hypothetical question. They are probably doing\
  \ it right now. \nYou might be thinking about all the secure design choices you\
  \ have made, or preventa..."
---

By Bedirhan Urgun

What would you do if hackers were abusing your software in production? 

This is not a hypothetical question. They are probably doing it right now. 

You might be thinking about all the secure design choices you have made, or preventative techniques you applied, so there’s nothing to worry about. 

If so, that’s great – even if there are always things that get overlooked, you should always be thinking about the security of your system. 

But there’s a **huge difference** between preventing security bugs and forgiving malicious attempts.

How about we catch and act upon the hackers who are trying to break into our software? In this post, I’ll try to give you practical and simple examples of catching typical hacker behaviors in your code early.

## Why Catch Malicious Attempts?

Isn’t preventing security bugs enough? I can hear you saying, “As long as I write secure code, I don’t care whether hackers play with my rock-solid software or not. So, why should I care about malicious attempts?” 

Let’s first answer this valid question.

A somewhat complex piece of software is difficult to keep secure all the time. More complexity means more potential weaknesses for a hacker to abuse while you're designing, implementing, deploying, or maintaining the code.

Just look at the [CVE numbers](https://www.cvedetails.com/browse-by-date.php) over the years. It’s a lot:

![Image](https://lh4.googleusercontent.com/xHM7o5NKsWBrELAL-pjl90rlDxpHzIMz4e33OHzJLpl82tpJFEsaUVJ8_c5GFoxPHaJGtpk-s5qUZ8pJhghA-E71Z9xLdtqkf3SCUtfGR_8bPMdQXxx9p1tfr7NH1BZqepSDQJeG)
_The number of security bugs published over the years by cvedetails.com_

Moreover, because of its nature, a security bug is not just a regular item in your backlog. There are some nasty consequences if a vulnerability gets exploited: a loss of trust, a bad reputation, or even financial loss.

So, security best practices such as the [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/) or [Mozilla’s Secure Coding Guidelines](https://wiki.mozilla.org/WebAppSec/Secure_Coding_Guidelines) exist in order to help developers produce secure software.

However, since new ways of bypassing existing security controls or new weaknesses emerge on an almost daily basis, there’s a consensus around the security community that “There’s no 100% security.” So we always have to be alert and responsive to security news and improvements. 

There’s also one more thing we can do to ensure secure software: noticing hackers as early as possible, before they do something that we don’t expect or even know about. Moreover, keeping track of their malicious behavior over a long period of time makes us more proactive.

There’s a popular notion of [Security Operations Center (SOC)](https://en.wikipedia.org/wiki/Security_operations_center) along these lines – SOCs are a type of team in an organization which is outsourced or in-house. Their job is to continuously monitor the security state of the organization. They do it by detecting, analyzing, and responding to cyber security incidents. 

SOC teams look for abnormal activities, including software security anomalies. The idea of noticing and responding to a successful or failed cyber-attack gives organizations an upper-hand against threats, which is ultimately reducing the response time to attacks through continuous monitoring.

An SOC is strong only with the rich and quality input it gets from different sources of IT components. Since our software is also an important part of the inventory, appropriate security alarms due to abnormal behaviors sent by our software to SOC teams are invaluable.

## How to Check for Abnormal Behaviors

Here are a number of checks and controls we can implement throughout our code that reveal malicious and abnormal behaviors. 

Before we start, I’d like to emphasize that I’m not presenting complicated solutions like [Web Application Firewall (WAF)](https://en.wikipedia.org/wiki/Web_application_firewall) here. Instead, I will just try to show you that simple conditionals, smart exception handling, and similar little to no effort actions in your code can help you notice abnormal behaviors as soon as they occur. 

Let’s dig in.

### Zero Length or Null Returns

The first action we can take to detect a malicious action is by checking zero length aggregates or null returns. 

Here’s a simple code block to illustrate the point:

```csharp
Receipt receipt = GetReceipt(transferId);
if (receipt == null)
{
    // what does this mean?
    // log, notify, alarm
}
```

Here, we try to access the receipt of a certain transfer provided by our end users through the `transferId` parameter. 

In order to prevent anyone from accessing someone else’s receipts, let’s assume that inside the `GetReceipt` method, our developer is smart enough to check whether the `transferId` really belongs to the current user. 

Checking ownership is a good security best practice.

Let’s further assume that we are sure by design that every transfer should have at least one related receipt, so getting none at runtime is suspicious. Why? Because getting an empty receipt means the provided `transferId` doesn’t belong to any transfer executed by the current user. 

In other words, the current user provided a forged `transferId` to our code and waits to see the content if that `transferId` happens to relate to someone else’s transaction. 

And since we have the appropriate ownership control, the `GetReceipt` method returns an empty or null receipt. That’s where we have to take some security actions. 

I won’t go into details of the security actions in this post. However, security logging and/or sending detailed notifications ,Security Information and Event Management ([SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management)) systems are two of them.

Here’s another example of how checking the null value allows us to seize a malicious attempt. 

Consider that we have the following three endpoints, `ShowReceipt`, `Success`, and `Error`:

```csharp
// ShowReceipt endpoint
if(CurrentUser.Owns(receiptId))
{
   Session["receiptid"] = receiptId;
   redirect "Success";
}
else
{
    redirect "Error";
}
```

```csharp
// Success endpoint
receiptId = Session["receiptid"];
return ReadReceipt(receiptId);
```

```csharp
// Error endpoint
return "Error";
```

This is a simple application that shows the content of a user’s receipt. 

In `ShowReceipt`, the first line is an important one. It checks whether the end user is sending us a valid `receiptId` to see its contents. Without this control, a malicious user can provide any `receiptId` and access the content.

The place of the statement in the third line is equally important, though. If we move this line just before the if statement, that wouldn’t break anything. However, it would create the same security problem we were trying to avoid by checking whether the end user is requesting a valid receipt or not. 

Please take a moment to make sure you understand why this is the case.

Now, it’s a good idea that we placed that line in the correct place and that creates another opportunity to notice malicious attempts. Then, in the `Success` endpoint, what does it mean if we get null `receiptId` from the `Session`? 

That means someone is calling this endpoint, just after they made a request to `ShowReceipt` endpoint with someone else’s `receiptId`. Even if they got `Error` redirect back because of the ownership check! 

Of course with the control we have at the first line, this is impossible.

So, the `Success` endpoint is a nice place to write a security log entry and send any notifications to our monitoring solutions when we get a null `receiptId` from the `Session`.

```csharp
// Success endpoint (Revisited)
receiptId = Session["receiptid"];
if(receiptId == null)
{
    // log, notify, alarm
}
return ReadReceipt(receiptId);
```

### Targeted Exception Handling

Exception handling is maybe the most important mechanism for developers to respond to any anomalous condition during the execution of the program. 

Most of the time the main opportunity it provides is cleaning up resources that were borrowed such as file/network streams or database connections upon unexpected problems. This is a fail-safe behavior that lets us write more reliable programs.

In parallel we can effectively use runtime exceptions to notice malicious attempts towards our software.

Here are some popular sources of weakness where we can utilize related exceptions to notice fishy behavior:  


* Deserialization
* Cryptography
* XML Parsing
* Regular Expression
* Arithmetic Operations

The list is not complete, of course. And here I’ll go through only a few of these APIs.

Let’s start with Regular Expressions. Here’s a code block that applies a strict validation method on a user input:

```csharp
if(!Regex.IsMatch(query.Search, @"^([a-zA-Z0-9]+ ?)+$"))
{
    return RedirectToAction("Error");
}
```

The regular expression pattern used here is a solid whitelist one, which means it checks what is expected as an input. Not the other insecure way around, which is checking what is known to be bad. 

Still, here’s a much secure version of the same code block:

```csharp
if(!Regex.IsMatch(query.Search, @"^([a-zA-Z0-9]+ ?)+$", 
                  RegexOptions.Compiled, TimeSpan.FromSeconds(10)))
{
    return RedirectToAction("Error");
}
```

This is an overloaded version of the `IsMatch` method of which the last argument is the key. 

It enforces that the execution of the regular expression during runtime can not exceed 10 seconds. If it does, that means something suspicious is going on since the pattern used is not that complicated. 

There’s an actual security weakness that might be used to abuse this pattern called [ReDoS](https://en.wikipedia.org/wiki/ReDoS), though I won't go into the details of it here. But in short, an end-user can send the following string as the search parameter and make our back-end miserable, spending an awful amount of CPU power in vain. 

Notice the quotation mark at the end (and don’t try this in production!):

==AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!==

The question is, what happens when the execution time actually exceeds 10 seconds? 

The .NET environment throws an exception, namely `RegexMatchTimeoutException`. So, if we specifically catch this exception, we now have the opportunity to report this suspicious incident or do something about it. 

Here’s the final code block to that end:

```csharp
try
{
    if(!Regex.IsMatch(query.Search, @"^([a-zA-Z0-9]+ ?)+$", 
                        RegexOptions.Compiled, TimeSpan.FromSeconds(10)))
    {
        return RedirectToAction("Error");
    }
}
catch(RegexMatchTimeoutException rmte)
{
    // log, notify, alarm
}
```

Another important venue where we can utilize exceptions is XML parsing. Here’s an example code block:

```csharp
XmlReader xmlReader = XmlReader.Create(input);
var root = XDocument.Load(xmlReader, LoadOptions.PreserveWhitespace);
```

The input XML is fed into `XmlReader.Create`, and then we get the root element. Hackers can abuse this piece of code by providing some malicious XML files, which, when parsed by the above code, gives ownership of our servers to them. 

Scary, right? The security bug is called [XML External Entity](https://en.wikipedia.org/wiki/XML_external_entity_attack) (XXE) attack, and as with the Regular Expression exploit, I won't go into all the details here.

However, in order to prevent that super critical weakness, we ignore the usage of Document Type Definitions (DTD) through the `XmlReaderSettings`. So now, there’s no possibility of XXE security bugs anymore. 

Here’s the secure version:

```csharp
XmlReaderSettings settings = new XmlReaderSettings();
settings.DtdProcessing = DtdProcessing.Ignore;

XmlReader xmlReader = XmlReader.Create(input, settings);
var root = XDocument.Load(xmlReader, LoadOptions.PreserveWhitespace);
```

We can leave the code just like this and move on. However, if a hacker still tries to abuse this attack in vain, it's better that we can catch this behavior and produce an invaluable security alert:

```csharp
try
{
    XmlReaderSettings settings = new XmlReaderSettings();
    settings.DtdProcessing = DtdProcessing.Ignore;

    XmlReader xmlReader = XmlReader.Create(input, settings);
    var root = XDocument.Load(xmlReader, LoadOptions.PreserveWhitespace);
}
catch(XmlException xe)
{
    // log, notify, alarm
}
```

Moreover, in order to prevent false positives, you can ==further customize the catch block by using the message content provided by the `XmlException` instance==.

There’s a general programming best practice that denies using generic `Exception` types in catch blocks. What we have shown is also a good supporting case for this. Same goes with another best practice that denies using empty catch blocks, which is effectively doing nothing when an abnormal behavior occurs in our code. 

Apparently though, instead of empty catch blocks, here we have a very solid opportunity to react to malicious attempts.

### Normalization on Inputs

By definition, normalization is to get the simplest form of something. In fact, canonicalization is the term used for this purpose. But it is hard to pronounce, so, let's stick to normalization.

Of course, “the simplest form of something” is a little bit abstract. What do we mean by the “simplest form”? 

It is always good to show by example. Here is a string:

==%3cscript%3e==

According to the [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding), this string is not in its simplest form. Because if we apply URL decoding on it, we get this one:

==\<script\>==

This is the simplest form of the original string according to URL encoding transformation standard. 

How do we know that? We know it not because it is understandable to us now. We know it because if we apply URL decoding again, we will get the same string:

==\<script\>==

And that means URL decoding does not successfully transform it anymore. We hit the simplest form. Normalization can take more than one step, as originally the encoding might be applied more than once.

URL encoding is just one example of the transformation used for normalization, or in other words, decoding. HTML encoding, JavaScript encoding, and CSS encoding are other important encoding/decoding methods widely used for normalization. 

Over the years, attackers find genuine techniques to bypass defense systems. And one of the most prevalent techniques they utilize is encoding. They use crazy encoding techniques on their original malicious inputs, in order to fool defenses around applications. 

History is full of these demonstrations, and you can read the details of one of the most famous ones called [Microsoft’s infamous IIS dotdot attack](https://en.wikipedia.org/wiki/Directory_traversal_attack#Directory_traversal_on_Microsoft_Windows) that took place in the early 2000s.

Since hackers rely on encoding techniques substantially when they are sending malicious inputs, normalization can be one of the most effective and easy ways to seize them.

Here is the rule of thumb: we recursively apply URL/HTML/CSS/JavaScript decoding to user input until the output no longer changes. And if the output is a different string than the original input, that means we may have a possible malicious request. 

Here’s a simplified version of legendary [OWASP ESAPI Java](https://github.com/ESAPI/esapi-java-legacy/blob/develop/src/main/java/org/owasp/esapi/reference/DefaultEncoder.java#L147) that implements this idea:

```java
int foundCount = 0;
boolean clean = false;
while(!clean)
{
    clean = true;
    // whatever codes you want; URL/Javascript/HTML/...
    Iterator i = codecs.iterator();
    while (i.hasNext())
    {
        Codec codec = (Codec)i.next();
          String old = input;
          input = codec.decode(input);
          if (!old.equals(input))
         {
            if (clean)
           {
               foundCount++;
            }
            clean = false;
        }
    }
}
```

When the code block ends, if the value of `foundCount` is bigger or equal to 2, that means what? It means someone is sending multiple encoded input to our application, and the odds of this happening is really rare. 

Normal users do not send multiple encoded strings to our application. There is a high probability that this is a malicious user. We have to log this event with the original input for further analysis.

The above mechanism, while part of the software itself, functions like a filter in front of the application. It runs on every untrusted input and gives us an opportunity to know about malicious attempts. 

However, you may be suspicious about the additional delay this way of validation incurs. I understand if you don’t want to opt-in.

Here's another example of using normalization as a means to seize malicious attempts during file uploads or downloads. Consider the following code:

```csharp
if (!String.IsNullOrEmpty(fileName))
{
    fileName = new FileInfo(fileName).Name;
    string path = @"E:\uploaded_files\" + fileName;
    if (File.Exists(path))
    {
        response.ContentType = "image/jpg";
        response.BinaryWrite(File.ReadAllBytes(path));
    }
}
```

Here we get a `fileName` parameter from our client, locate the image it points to, read, and present the content. This is a download example. It might also have been an upload scenario. 

Nevertheless, in order to prevent the client manipulating the `fileName` parameter to their heart’s content, we utilize the `Name` property of the `FileInfo` class. This will only get the name part of the `fileName`, even if the client sends us anything other than what we expect (i.e. a file name with forged paths such as below):

==../../WebSites/Cross/Web.config==

Here the malicious client wants to read the contents of a sensitive `Web.Config` file by using our code. Getting only the file name part, we get rid of this possibility. 

That is good but there is still something we can do:

```csharp
if (!String.IsNullOrEmpty(fileName))
{
    string normalizedFileName = new FileInfo(fileName).Name;
    if (normalizedFileName != fileName)
    {
        // log, notify, alarm
        response = ResponseStatus.Unauthorized;
    }

    string path = @"E:\uploaded_files\" + fileName;
    if (File.Exists(path))
    {
        response.ContentType = "image/jpg";
        response.BinaryWrite(File.ReadAllBytes(path));
    }
}
```

We compare the normalized version of `fileName` with itself (the original input). If they differ, that means someone is trying to send us a manipulated `fileName` and we take appropriate action. 

Normally the browser just sends the uploaded file name in its simplest form with no transformation.

For the sake of the argument, we may not even use the file name when the user uploads a file. We may be generating a `GUID` and use that instead. 

Nevertheless, applying this control to the provided file name still matters, because hackers will definitely poke with that parameter no matter what.

### Invalid Input Against Whitelists

Whitelisting is “accepting only what is expected”. In other words, if we come across some input that we do not expect, we reject it. 

This input validation strategy is one of the most secure and effective strategies we have to this date. By using this strategy consistently throughout your software, you can close a lot of known and unknown venues that a malicious user can attack you. 

This way of building a software is like building a closed castle with only thoroughly controlled doors opening outside, if that makes any sense. 

OK, back to our topic.

Let’s analyze whitelisting with a simple scenario. Assume that our users have the freedom to choose their own, specific usernames when registering. And prior to coding, as a requirement we were informed how a username should look like.

Then, in order to comply with this requirement we can easily devise some rigid rules to apply against the username input before we accept it. If the input passes the test, we take in. Otherwise, we reject the input.

The whitelist rules may be in different forms, though. Some may contain a list of expected hard-coded values, others may check whether the input is integer or not. And others may be in the form of regular expressions.

Here is an example regular expression for usernames:

==\^\[a-zA-Z0-9]{4,15}$==

This regular expression is a very rigid whitelisting pattern. It matches with every string whose characters are nothing but a-z, A-Z, or 0-9. Not only this, but the length of the input should be minimum of 4 characters and maximum of 15 characters. 

The hat at the beginning and dollar character at the end of the regular expression denote that the match should occur for the whole input.

Now assume that at runtime we get the following input which won’t pass our regular expression test:

==o'neal==

Does that mean our software is facing a hacker? 

The input seems innocent. However, it might also be the case that a malicious user is just trying the existence of an [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) security bug before getting into the action, which is also known as reconnaissance. 

Anyway, it’s still hard to deduce any malice from this particular case.

However, we can still seize the hackers using other forms of failed whitelists, such as failed input attempts against a list of expected hard-coded values. 

An excellent example is [JSON Web Token (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token) standard. We use JWT when we want third parties to send us a claim that we can validate and then trust the data inside.

The standard has a simple JSON structure: a header, a body and a signature. The header contains how this particular claim should be produced and therefore validated. The body contains the claim itself. The signature is there for, well, validation.

For instance, when we get the following token from a third part, such as a user, we validate it using the algorithm it presents in the header value. 

In this instance, the token itself tells us that we should use cryptographic hash [HMACSHA256](https://en.wikipedia.org/wiki/HMAC) algorithm (HS256 in the token is a short version) on both the header and body data to test whether it produces the same signature given. 

If it produces the same signature value, then the token is authentic and we can trust the body:

```json
// Header
{
 "alg" : "HS256",
 "typ" : "JWT"
}
// Body
{
  "userid": "johndoe@gmail.com",
  "name": "John Doe",
  "iat": 1516239022
}
// Signature
AflcxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5g
```

There are various external libraries that we can easily use to produce and validate JWTs. Some of them had a serious security bug which let any JWT to be taken as an authentic token. 

Here’s what went wrong with those libraries. 

What happens when a token that we should validate contains a header like below? I just present the header here, but it also contains body and signature parts:

```json
// Header
{
 "alg" : "None",
 "typ" : "JWT"
}
```

It seems that for that specific token some of those JWT validation libraries just accept the body as it is without any validation, because `None` says that no algorithm is applied for signature production. 

To put this into perspective, that means any end user can send us any `userid` inside the token and we will not apply any validation against it and let them login.

The best way to avoid this and similar security problems is to keep a valid list of algorithms on our side. In this case the list may contain only one valid algorithm. 

Moreover, it's better not to process the algorithm we get inside the header part of the JSON Web Token, whatever it might be.

But as you might have already guessed, there’s a huge opportunity here. We may just get the algorithm value from the header part and check even if we won’t use it. If the value is anything other than we expect, let’s say HS256, that means someone is messing around with us.

The same method can be used for any list of hard-coded values presented to the end user and one of which we expect to get as an input. 

For example, if we provide a list of cities in a select box, we are sure that we will get back one of them when the form is posted. If we get a completely different value, there’s surely something wrong with the behavior of the user or automated tool we are facing.

### Actions Against AuthN and AuthZ

One of the most critical parts of software from a security point of view are the authentication and the authorization mechanisms. These are places where we enforce that only the parties we know of access the application and they access certain parts within their roles. 

In other words, our users shouldn’t use certain parts of our application without any credential validation and they shouldn’t access parts where they don’t have any privileges.

There are various attack scenarios against both of the mechanisms, however, the most obvious one against authentication is brute forcing. It is trying a set of pre-populated or generated on the fly credentials one after another in the hope that one or more of them would work. 

Of course there are well-known ways to prevent such attacks: using [CAPTCHAs](https://en.wikipedia.org/wiki/CAPTCHA) or applying throttling on problematic IP addresses or usernames.

Usually authentication attacks are well-known and when noticed are already logged and possibly fed into the security monitoring systems.

The same is possible with attacks against authorization. 

It’s easy to produce a security log and an alarm when our application returns an 403 response to our users. This well-known HTTP response is the indicator of an authorization problem, so it’s wise to log it. 

However, both the authentication and the authorization cases so far have the potential to produce false alarms. However, I still encourage logging and producing alarms whenever these occur.

Now, let’s concentrate on a more solid case. Whenever we use Model-View-Controller (MVC) frameworks, we utilize the built-in auto-binding feature for our `Action` method parameters. So, the MVC framework we are using is in charge of binding parameters in HTTP requests onto our model objects automatically. 

This is a great relief for us since getting each user input by using the low-level APIs of a framework really becomes tedious after some time.

What happens if this auto-binding becomes too permissive? Assume that we have a `User` model. It would probably have at least ten or twenty member fields. But for clarity, let’s say it has a `FullName` and a `IsAdmin` member fields. 

The second member field will denote if a particular user is administrator or not:

```csharp
public class User
{
    public string FullName { get; set; }
    public bool IsAdmin { get; set; }
}
```

In order for users to update their own profile, we prepare a `View` including the appropriate form and bindings. 

At last, when the form is submitted, a controller action will auto-bind the HTTP parameters to a `User` class instance. Then, perhaps it will save it to the database just like below:

```csharp
[HttpPost]
public Result Update(User user)
{
    UserRepository.Store(user);
    return View("Success");
}
```

Obviously here, a malicious non-administrative user may also set values of unwanted model members, such as `IsAdmin`. Since the binding is automatic, our malicious user can make themselves administrator by requesting a simple HTTP POST request to this action!

By using the MVC pattern, every model we use in action method parameters becomes fully visible and editable to end-users. 

The best way to prevent this is using extra `ViewModels` or DTO objects for `Views` and `Actions` and include only the permitted fields. For example, here is a `UserViewModel` that only contains editable fields of `User` model class.

```csharp
public class UserViewModel
{
    public string FullName { get; set; }
}
```

So, the end user, albeit she can add an additional `IsAdmin` parameter to the HTTP POST request, that value will not be used at all to result in a security problem. Excellent!

But wait, there’s a golden opportunity here to seize sophisticated hackers. How about we still include `IsAdmin` property in our `UserViewModel`, but produce a security log and maybe alarms when the setter is called:

```csharp
public class UserViewModel
{
    public string FullName { get; set; }
    public bool IsAdmin
    {
        set
        {
            // log, alarm, notify
        }
    }
}
```

Just make sure that we don’t use this member field when we are creating a `User` model class instance out of this `UserViewModel` instance.

### Miscellaneous

It is impossible to list or classify every possible case where we can place our little controls to notice any hacking attempts as early as possible. However, here are some of the other opportunities we have:

* If our application provides a flow of actions which should be followed in a specific order, then any invalid order of calling indicates an abnormal behaviour.
* Injection attacks are one of the most severe security bug categories that stem from insecure code and data concatenation. Cross Site Scripting (XSS), SQL Injection, and Directory Traversal are some common bugs in this category. Once we use secure constructs like contextual encodings, whitelist validation, and prepared statements, then we get rid of them. However, unfortunately, there are no simple and  non-blacklist ways to seize the hackers who are still trying to abuse these security bugs once they are fixed.
* Setting up traps is also a valid way of catching malicious attempts but I’m against this if the effort takes a huge amount of time or is likely to produce false alarms. For example, it’s possible to include hidden links (display:none) in our web pages and trigger security logging when these links are accessed by automated security scanners (because they try to access every link that they can extract). However, this may also produce false alarms for legitimate crawlers, such as Google. Still, this is a design choice and there are a lot of traps that can be set, such as non-existing but easy to guess:
    - username, password pairs, e.g. the infamous ==admin:admin==
    - administrative URL paths, e.g. ==/admin==
    - HTTP headers, parameters, e.g. ==IsAdmin==

## Conclusion

> “Forgiveness isn’t approving what happened. It’s choosing to rise above it.” Robin Sharma

It is unforgivably naive to let malicious attempts towards our software go unnoticed while we already have the tools under our belt to do otherwise. Forgiveness is such a supreme moral quality, but we have to be on top of risky activities around our code.

Despite chaotic facets of software development, developing secure code is an important survival skill in this hacker-loaded world. 

Moreover, we have the chance to improve this skill even further by noticing malicious activities in a precise manner in our code and producing security log entries and alarms for SOC teams.

Doing something about malicious behaviors in our code, like you read in this article ==is just one of the coding mistakes that lead to hacker abuse.== I encourage you to check my [Coding Mistakes that Hackers Abuse online training](https://www.udemy.com/course/coding-mistakes-that-hackers-abuse/?referralCode=DB84A20CFA4F65DDE427) in order to master the rest of them.


