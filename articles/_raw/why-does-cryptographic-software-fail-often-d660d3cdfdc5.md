---
title: The many, many ways that cryptographic software can fail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-25T02:25:49.000Z'
originalURL: https://freecodecamp.org/news/why-does-cryptographic-software-fail-often-d660d3cdfdc5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eHaISV7BciMhq8o0AHmftg.png
tags:
- name: Cryptography
  slug: cryptography
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Nabeel Yoosuf

  When cryptographic software fails, what’s to blame?

  Algorithms?

  Cryptography libraries?

  Apps incorrectly using those libraries?

  Or is it something else entirely?

  We rely on cryptographic algorithms and protocols every day for secure ...'
---

By Nabeel Yoosuf

When cryptographic software fails, what’s to blame?

Algorithms?

Cryptography libraries?

Apps incorrectly using those libraries?

Or is it something else entirely?

We rely on cryptographic algorithms and protocols every day for secure communication over the Internet. We’re able to access our bank accounts online because cryptography protects us. We’re able to send private messages to our friends because cryptography protects us. We’re able to buy and sell things using credit cards and Bitcoin because cryptography protects us.

Let me give you a concrete example of this. When you check your email through your favorite browser, the connection between your browser and the email server is secured using the TLS (transport level security) protocol, so that no one can eavesdrop on your emails or modify them in transit without your knowledge.

In short, without cryptography, the Internet we know today could not be possible. Law and order on the internet depends on cryptography.

But this tool that we all rely upon so heavily is also quite brittle. Our cryptographic software often [lets us down](http://fortune.com/2016/05/18/linkedin-data-breach-email-password/). Sometime it [really lets us down](http://money.cnn.com/2013/12/22/news/companies/target-credit-card-hack/).

Have you ever wondered why the [cryptographic software](https://www.cl.cam.ac.uk/~rja14/Papers/wcf.pdf) — including implementations of the TLS protocol — [fail](https://www.schneier.com/essays/archives/1998/01/security_pitfalls_in.html) over and over again?

According Veracode’s state of security reports, our cryptographic software is just as vulnerabilities as it was two years ago.

![Image](https://cdn-media-1.freecodecamp.org/images/fe3A-m3hCNxrQMhkYQeuRcvTJB287TL-ot73)
_Veracode ranked cryptographic issues as #2 vulnerability found in apps in 2015_

![Image](https://cdn-media-1.freecodecamp.org/images/H94qJr0QwDiVakmegPWDXbYSmRMMb9tZED-O)
_Veracode again ranked cryptographic issues as #2 vulnerability found in apps in 2o16_

Are these failing because of weaknesses in the underlying cryptographic algorithms?

Well, several past attacks ([Apple iOS TLS](https://www.imperialviolet.org/2014/02/22/applebug.html), [WD self encrypting drives](http://hardwear.io/wp-content/uploads/2015/10/got-HW-crypto-slides_hardwear_gunnar-christian.pdf), [Heartbleed](https://www.us-cert.gov/ncas/alerts/TA14-098A), [WhatsApp messages](https://www.theguardian.com/technology/2017/jan/16/whatsapp-vulnerability-facebook), [Juniper’s ScreenOS](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=juniper%20screenos%20vulnerability), [DROWN](https://drownattack.com/), [Android N-encryption](http://karl-voit.at/2016/02/27/android-encryption/) and so on) show us that our cryptographic software is less likely to be broken due to the weaknesses in the underlying cryptographic algorithms. In other words, cryptanalysis is one of the less likely threats to our cryptographic software.

![Image](https://cdn-media-1.freecodecamp.org/images/9w3A4G6y-5zto71XmJxbTyDz8b5A6SwyVtaV)
_A sketch of the AES algorithm ([image credit](http://www.moserware.com/2009/09/stick-figure-guide-to-advanced.html" rel="noopener" target="_blank" title=")) AKA why you don’t want to roll your own cryptography._

Have you ever heard an attacker breaking a 256-bit AES encryption algorithm to recover the secret hidden within it? None that I know of. (Of course, if you use a vulnerable obsolete cryptographic protocol like [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard) or [RC4](http://www.securityweek.com/new-attack-rc4-based-ssltls-leverages-13-year-old-vulnerability), cryptanalysis might help break the software). So if the culprit isn’t cryptanalysis, then what is it?

![Image](https://cdn-media-1.freecodecamp.org/images/aK1G79PpqMPtvs478FBokRR0Imh5j-1rDK3j)
_Your security is only as good as its weakest link._

Well, it’s everything but cryptanalysis. In other words, cryptanalysis is not the weakest link of cryptographic software. Bad actors use numerous other weak links to break cryptographic software.

### **Cause of failure #1: bugs in crypto libraries**

One popular example is the Heartbleed bug.

![Image](https://cdn-media-1.freecodecamp.org/images/VwqT62a1y1lEhMiMcUkOwUnt7yaVV5a6pj5I)

What’s the matter with [Heartbleed](http://heartbleed.com/)? This bug ([CVE-2014–0160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2014-0160)) was introduced due to an incorrect implementation of the TLS heartbeat extension in the widely-used OpenSSL (read 66% of the internet), which is used to support TLS in web servers. What does this extension do? As the the name suggests, it’s a keep-alive feature where one end of the connection sends a payload of arbitrary data and the other end is supposed to send the exact copy of the data to prove that all is fine and well.

The bug turned out to be an age-old mistake of not bound checking before `memcpy()` that uses non-sanitized data. The vulnerable OpenSSL implementation [does not validate the payload length against the actual payload](http://www.theregister.co.uk/2014/04/09/heartbleed_explained/). An attacker could lie about the length and get the victim to send more bytes from its memory, as shown in the following diagram.

![Image](https://cdn-media-1.freecodecamp.org/images/iukZ8VzrmG8b3MRRD6xad7xNMBJV186XrGzp)
_Attacker sends only one byte payload but sets the length to 65535; the victim blindly copies 65535 from its memory and sends back to the attacker._

This in turn allowed the attacker to obtain session keys and other secret information (like your username and password) from any websites currently in your browser’s memory.

Let me show you the code. The patch is essentially a bound check added to the patched version 1.0.1g as shown below.

```
====== Vulnerable code =======/* Enter response type, length and copy payload */*bp++ = TLS1_HB_RESPONSE;s2n(payload, bp);memcpy(bp, pl, payload);
```

```
====== Patched code =========hbtype = *p++;n2s(p, payload);if (1 + 2 + payload + 16 > s->s3->rrec.length)  return 0; /* silently discard per RFC 6520 sec. 4 */pl = p;
```

**Lesson learned:** Always bound check your strings before using them. Sanitization is vital for stopping bad inputs from getting into your system.

### **Cause of failure #2: operating systems and apps**

You probably remember [Apple’s “goto” bug](https://www.imperialviolet.org/2014/02/22/applebug.html) ([CVE-2014–1266](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-1266)) in its SSL/TLS implementation, disclosed in February 2014.

Apple’s code with the “goto” bug:

```
1 static OSStatus2 SSLVerifySignedServerKeyExchange(SSLContext *ctx, bool isRsa,                                  SSLBuffer signedParams,3                       uint8_t *signature, UInt16 signatureLen)4 {5   OSStatus err;6 …78   if ((err = SSLHashSHA1.update(&hashCtx, &serverRandom)) != 0)9     goto fail;10  if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)11    goto fail;12    goto fail;13  if ((err = SSLHashSHA1.final(&hashCtx, &hashOut)) != 0)14    goto fail;15  …1617 fail:18   SSLFreeBuffer(&signedHashes);19   SSLFreeBuffer(&hashCtx);20   return err;21 }
```

So, what’s the issue here? The extra goto statement on line 12 bypasses all certificate checks for SSL/TLS connections in iOS and Mac devices. This makes lines 13 to 16 effectively dead code. This simple implementation mistake accepts any invalid certificate, making the connection susceptible to Man in the Middle attacks.

I was curious to find out whether the implementation bugs in crypto software are more due to bugs in the crypto libraries themselves than in the way apps use them. Well [researchers from MIT](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=0ahUKEwj--OSC7NrRAhXrJcAKHd2nDiEQFggbMAA&url=https%3A%2F%2Fpeople.csail.mit.edu%2Fnickolai%2Fpapers%2Flazar-cryptobugs.pdf&usg=AFQjCNGJvctaCQ8jDTUsZUgLX_AVl-LdKQ&sig2=P919CUo8W5fG7g7g1AroWQ) analyzed 269 cryptographic bugs reported in the Common Vulnerabilities and Exposures database between January 2011 and May 2014. They found that only 17% of bugs are caused by the crypto libraries themselves. The remaining 83% are due to misuse of crypto libs by app developers.

But just because the majority of bugs are due to misuse of crypto libraries in apps doesn’t mean that we can just blame app developers and get on with our day.

There could be many reasons behind the above statistics on the crypto misuse. The crypto libraries themselves may not be providing safe default options, may not have adequate documentation or may be difficult to use. Further, many developers may not have a formal understanding of applying cryptography in their software, even though they are experts at software development itself. These all could result in the misuse of crypto libs.

**Lesson learned:** always use tools to analyze your code. A dead code analysis tool should have caught this specific case.

### **Cause of failure #3: bad design**

In 2015, researchers uncovered a series of issues in WD self-encrypting drives. There were serious design flaws in their use of cryptographic algorithms. I wrote about this in a [previous post](https://decentralize.today/encryption-is-useless-completely-useless-part-1-14a5e3bd069b#.h94ta28eu). Let me show a couple of flaws here.

![Image](https://cdn-media-1.freecodecamp.org/images/ViJwzCkWz2D6nmxHoE4YQHOahxXMhkPzv-85)
_WD’s self encrypting drive architecture_

Following the best practices, WD did use two levels of keys to encrypt documents stored in the drive — master KEK (Key Encryption Key) and per file DEK (Data Encryption Key). Further, they did use a key derivation function to derive KEKs from the password.

But the way they designed the key derivation function itself was totally insecure. They used a fixed salt and a fixed number of iterations. Thus, it was susceptible to pre-computed hash table-based attacks. Attackers could recover keys much faster than a pure brute force attack would have been able to.

![Image](https://cdn-media-1.freecodecamp.org/images/xNOCC3T-Ejcup3h89XWOtgE103A8VD-2Hj3H)
_WD’s vulnerable key derivation algorithm_

And if this vulnerability weren’t enough, WD used a dismal random number generator to generate KEKs. It was not only predictable — it also didn’t have enough complexity (only 40 bits).

Cryptographic protocols critically rely on cryptographically secure pseudorandom number generators. If these aren’t secure enough, any cryptographic algorithm or protocol using these random numbers will be quite easy to break.

![Image](https://cdn-media-1.freecodecamp.org/images/GrNo2Nf1RAlPVyTrANT0mmHLv9bAevCTSgAz)
_WD’s weak random number generator_

**Lesson learned:** Have a good understanding of cryptographic constructs and know their limitations. Follow industry best practices for key derivation.

### **Cause of failure #4: misconfigurations or insecure default configurations**

![Image](https://cdn-media-1.freecodecamp.org/images/3-VGZNwxuYBBHi5dmH588z5M9lmD9YA9VlEb)
_Exploiting the weaknesses of SSLv2 ([source](https://drownattack.com/" rel="noopener" target="_blank" title="))_

[DROWN attack](https://drownattack.com/drown-attack-paper.pdf) of breaking TLS connections via SSLv2 is a good example of this. You may be using fairly secure TLS connection to communicate with a web server, but if the web server still supports (which it shouldn’t) old SSLv2, an attacker can exploit it to break the security provided by TLS and get at your keys and other sensitive information.

SSLv2 has long considered to be broken, and none of the clients today use it for secure connections. But researchers have found that out of 36 million HTTPS servers they probed, 6 million (about 17%) still supported SSLv2.

![Image](https://cdn-media-1.freecodecamp.org/images/DMIkoMXQS6V0KBwPI1whg2KPQTUkaFHYhADT)

The above research also uncovers another common lazy practice of using the same key pair in different servers of an organization. It shows how even when one server supports only TLS, if there are other servers supporting SSLv2 with a shared certificate, the server that only supports TLS is vulnerable as well.

**Lesson learned:** a system is only as secure as its weakest link. Try to protect all of your systems at least reasonably well.

### There are lots of other ways cryptographic software can fail

Can you think of some additional ways?

It fails due to users. How? Think about social engineering attacks. [RSA SecureID breach is said to originate from phishing emails exploiting users and a zero day vulnerability](http://www.theregister.co.uk/2011/04/04/rsa_hack_howdunnit/).

It fails due to unrealistic threat models ([Breaking web applications built on top of encrypted data](https://eprint.iacr.org/2016/920.pdf)).

It fails due to hardware ([Breaking hardware enforced technologies such as TPM with hypervisors](https://www.blackhat.com/docs/us-16/materials/us-16-Sharkey-Breaking-Hardware-Enforced-Security-With-Hypervisors.pdf)).

It fails due to side channels ([Timing attacks on RSA, DH and DSS algorithms](http://www.cryptography.com/resources/whitepapers/TimingAttacks.pdf)).

As you can see, cryptographic software can fail due to many reasons. Are we really doomed to never get cryptographic software right? Or can we at least can reduce the number of such failures? Why can’t we learn from the past and avoid the same mistakes happening again and again? What tools will help us spot most of these issues?

Our situation actually isn’t all that bleak. There are ways to prevent most of the failures discussed above. In a follow up post, I’ll explore the topic of how we can make cryptographic software fail less often.

Thanks for reading. If you found this article useful, please click the ? below so that others can see this on Medium.

#### **Further Reading**

* [Aderson, Why cryptosystems fail, CCS 1993](http://Why Cryptosystems Fail - University of Cambridge Computer Laboratory)
* [Lazar et. al., Why does cryptographic software fail? A case study and open problems, APSys, 2014](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwidioe4yOnRAhXIcBoKHYalBWAQFggbMAA&url=https%3A%2F%2Fpeople.csail.mit.edu%2Fnickolai%2Fpapers%2Flazar-cryptobugs.pdf&usg=AFQjCNGJvctaCQ8jDTUsZUgLX_AVl-LdKQ&sig2=jNxWe1fBL5LSymGIjNdhig)
* [Egele et. al., An empirical study of cryptographic misuse in Android applications, CCS, 2013](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwi_093EyOnRAhXDQBoKHVyBDEkQFggnMAE&url=https%3A%2F%2Fcs.ucsb.edu%2F~chris%2Fresearch%2Fdoc%2Fccs13_cryptolint.pdf&usg=AFQjCNEmwGK1lobalVteyWAzgvzThSPafg&sig2=5eV_mxv-XvkdcjprP_7SMQ)

