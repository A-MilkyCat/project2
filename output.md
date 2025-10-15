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

# Drag and Drop Multiple File Upload for Contact Form 7 < 1.3.3.3 - Unauthenticated File Upload Bypass

### Description

Due to the plugin not properly checking the file being uploaded (via the dnd_codedropz_upload AJAX action), an attacker could bypass the checks in place and upload a PHP file.

There was a working exploit provided along with this vulnerability. It also requires the Contact Form 7 plugin to be installed on the target machine.

### Proof of Concept

https://github.com/amartinsec/CVE-2020-12800/blob/master/exploit.py

### Affects Plugins

[ ![Plugin icon](https://s0.wp.com/wp-content/themes/a8c/wpscan/assets/img/plugin-icon.svg) drag-and-drop-multiple-file-upload-contact-form-7 ](https://a8cteam5105.wordpress.com/plugin/drag-and-drop-multiple-file-upload-contact-form-7/)

![](https://s0.wp.com/wp-content/themes/a8c/wpscan/assets/img/checkmark-green-alt.svg) Fixed in 1.3.3.3 

### References

CVE 

[CVE-2020-12800](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-12800)

Exploitdb 

[48520](https://www.exploit-db.com/exploits/48520)

URL 

[exploit/multi/http/wp_dnd_mul_file_rce](https://www.rapid7.com/db/modules/#exploit/multi/http/wp_dnd_mul_file_rce)

URL 

<https://packetstormsecurity.com/files/#157837/>

URL 

<https://packetstormsecurity.com/files/#157951/>

URL 

<https://github.com/amartinsec/CVE-2020-12800>

### Miscellaneous

Original Researcher 

Austin Martin 

Verified 

Yes 

WPVDB ID 

[53e47e67-c8c9-45a9-9a9c-da52c37047bf](https://a8cteam5105.wordpress.com/vulnerability/53e47e67-c8c9-45a9-9a9c-da52c37047bf/)

### Timeline

Publicly Published 

2020-05-26 (about 5 years ago) 

Added 

2020-05-26 (about 5 years ago) 

Last Updated 

2020-10-21 (about 4 years ago) 

### Other

Published 

Title 

Published 

2023-03-06

Title 

[ Formidable Forms < 6.1 - IP Spoofing ](https://a8cteam5105.wordpress.com/vulnerability/a281f63f-e295-4666-8a08-01b23cd5a744/)

Published 

2019-01-25

Title 

[ Total Donations - Update Arbitrary WordPress Option Values ](https://a8cteam5105.wordpress.com/vulnerability/6e6342b0-82ca-4f5f-8b59-92ec3bdf1d02/)

Published 

2024-04-15

Title 

[ Zero Spam < 5.5.7 - Spam Protection Bypass ](https://a8cteam5105.wordpress.com/vulnerability/e8f53e21-dcba-4a99-8e95-8b9d28512304/)

Published 

2015-02-22

Title 

[ WP Ultimate CSV Importer <= 3.6.74 - Database Table Export ](https://a8cteam5105.wordpress.com/vulnerability/fc4865d1-00b9-4594-99d2-e2a3fc0d3951/)

Published 

2018-02-08

Title 

[ Swape Theme - Authentication Bypass and Stored XSS ](https://a8cteam5105.wordpress.com/vulnerability/46ee3aa5-947c-40a4-8572-aa2177230aef/)

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

Join 30,426 other subscribers

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




![](https://pixel.wp.com/g.gif?blog=221720208&v=wpcom&tz=-4&user_id=0&arch_home=1&subd=a8cteam5105&host=wpscan.com&ref=&rand=0.40634610883647393)

Notifications