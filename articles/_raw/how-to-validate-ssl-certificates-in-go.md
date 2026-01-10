---
title: How to Validate SSL Certificates in Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T20:11:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-ssl-certificates-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/S3MQd1604428653.png
tags:
- name: golang
  slug: golang
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: SSL
  slug: ssl
seo_title: null
seo_desc: 'By Umesh Yadav

  Recently, I came across a SaaS product that validates SSL certificates for your
  website. I wanted to try writing the same thing in Go – and it turns out that it''s
  pretty straightforward (just 17 lines of code).

  You will need to perform...'
---

By Umesh Yadav

Recently, I came across a SaaS product that validates SSL certificates for your website. I wanted to try writing the same thing in Go – and it turns out that it's pretty straightforward (just 17 lines of code).

You will need to perform three major checks on your website.

1. First, check to see whether your site has an SSL certificate or not. You'll also need to know if your website is using a self-signed SSL certificate which is not considered a valid certificate (it needs to be signed by a certificate authority).
2. Second, to see if the SSL certificate has the correct hostname.
3. And third, you need to know the expiration date of the server certificate.

Prerequisites:

* You should have `go` setup on your computer.

### Step 1: Check if your website has an SSL certificate

First, we will try to check if the website has an SSL certificate or not. 

To do this we need to establish a TLS connection with the website. If that succeeds it means the website has a valid TLS certificate. 

To establish a TLS connection we can use the Go `crypto/tls` package. We'll use the `Dial` method to connect to the website, like this:

```go
package main

import (
	"crypto/tls"
)

func main() {
	conn, err := tls.Dial("tcp", "example.com:80", nil)
	if err != nil {
		panic("Server doesn't support SSL certificate err: " + err.Error())
	}
}

```

We will try to run our test on `example.com`. When you run the above code, you should get the following error:

```
$ go run main.go
panic: Server doesn't support SSL certificate err: tls: first record does not look like a TLS handshake

goroutine 1 [running]:
main.main()
        /Users/umesh/personal/spike/main.go:99 +0x2ca
exit status 2

```

Basically it tried to establish the connection but failed. The `Dial` method succeeds only when the website has a valid certificate (it will fail if the certificate is self-signed).

Now try the same code on a website that has SSL enabled. I am using my own website's URL as an example:

```go
package main

import (
	"crypto/tls"
)

func main() {
	conn, err := tls.Dial("tcp", "blog.umesh.wtf:443", nil)
	if err != nil {
		panic("Server doesn't support SSL certificate err: " + err.Error())
	}
}

```

This time, we should be able to successfully establish the connection without the code panic.

In production you should not use panic, but rather should handle the error gracefully.

### Step 2: Check whether the SSL certificate and website hostname match

To verify the hostname we will need to call `VerifyHostname` on the `conn` return by `Dial`. This method tries to match the common name or subject alt name specified in the certificate with the domain passed as a parameter.

```go
package main

import (
	"crypto/tls"
)

func main() {
	conn, err := tls.Dial("tcp", "blog.umesh.wtf:443", nil)
	if err != nil {
		panic("Server doesn't support SSL certificate err: " + err.Error())
	}

	err = conn.VerifyHostname("blog.umesh.wtf")
	if err != nil {
		panic("Hostname doesn't match with certificate: " + err.Error())
	}
}

```

This will successfully execute without any error as the certificate's common name and hostname are the same.

### Step 3: Verify the expiration date of the server's SSL certificate

We can get the certificate chain using `conn.ConnectionState().PeerCertificates`. We can then use this certificate to get the expiration date of the server certificate. 

We will use the first certificate from the list of certificates and try to get the expiration date using the field `NotAfter`.

```go
package main

import (
	"crypto/tls"
	"fmt"
	"time"
)

func main() {
	conn, err := tls.Dial("tcp", "blog.umesh.wtf:443", nil)
	if err != nil {
		panic("Server doesn't support SSL certificate err: " + err.Error())
	}

	err = conn.VerifyHostname("blog.umesh.wtf")
	if err != nil {
		panic("Hostname doesn't match with certificate: " + err.Error())
	}
	expiry := conn.ConnectionState().PeerCertificates[0].NotAfter
	fmt.Printf("Issuer: %s\nExpiry: %v\n", conn.ConnectionState().PeerCertificates[0].Issuer, expiry.Format(time.RFC850))
}

```

The output should contain the certificate's expiration date and Issuer Name.

```
$ go run main.go
Issuer: CN=Let's Encrypt Authority X3, O=Let's Encrypt, C=US
Expiry: Wednesday, 16-Dec-20 16:20:00 UTC
```

Now we have successfully validated the site's certificate.

### Conclusion

You can also get detailed information like root CA, the date the certificate was issued, and all the chained certificates. 

This tool was just written using the core libraries of Go (and no external libraries). Do let me know what do you think about it!

If you liked this article, you can head over to [my personal blog](https://umesh.dev/blog) to see more stuff I've written. 

I regularly write about programming and software, so do subscribe to my newsletter and get the latest posts from me delivered straight into your inbox. You can also get in touch with me on [Twitter](https://twitter.com/imumesh18).

