Skip to content

[](/)

  * [Features](/features/)
  * [Pricing](/pricing/)
  * Solutions
    * [Status](https://status.wpscan.com/)
    * [API Details](/api)
    * [CLI Scanner](/wordpress-cli-scanner/)
  * Vulnerabilities
    * [Themes](/themes)
    * [WordPress](/wordpresses)
    * [Plugins](/plugins)
    * [Stats](/statistics)
    * [Submit Vulnerabilities](/submit)
    * [Leaderboard](/leaderboard)
  * Resources
    * [Blog](/blog)
    * [Enterprise Features](/enterprise-customers-features/)
    * [How to Install WPScan](/how-to-install-wpscan/)
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

[ ![Plugin icon](https://s0.wp.com/wp-content/themes/a8c/wpscan/assets/img/plugin-icon.svg) drag-and-drop-multiple-file-upload-contact-form-7 ](/plugin/drag-and-drop-multiple-file-upload-contact-form-7/)

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

[53e47e67-c8c9-45a9-9a9c-da52c37047bf](/vulnerability/53e47e67-c8c9-45a9-9a9c-da52c37047bf/)

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

2015-07-13

Title 

[ CP Image Store with Slideshow <= 1.0.6 - Purchase ID Brute Force Prevention ](/vulnerability/47033831-eb37-4bfd-8ca9-906ded30e7f8/)

Published 

2017-01-26

Title 

[ WordPress 4.2.0-4.7.1 - Press This UI Available to Unauthorised Users ](/vulnerability/c448e613-6714-4ad7-864f-77659b4da893/)

Published 

2022-10-31

Title 

[ WP-Polls < 2.76.0 - IP Validation Bypass ](/vulnerability/c1896ab9-9585-40e2-abbf-ef5153b3c6b2/)

Published 

2014-08-01

Title 

[ WordPress 3.7.1 & 3.8.1 - Privilege Escalation ](/vulnerability/40586ac9-eb74-4663-850f-b84b14e563de/)

Published 

2024-03-29

Title 

[ VS Contact Form < 14.8 - CAPTCHA Bypass ](/vulnerability/09b6eaf9-e125-4526-ad8e-20928ec3374a/)

![](https://wpscan.com/wp-content/uploads/2023/10/wpscan-logo-dark.png?w=246)

### Vulnerabilities

  * [WordPress](/wordpresses)
  * [Plugins](/plugins)
  * [Themes](/themes)
  * [Our Stats](/statistics/)
  * [Submit vulnerabilities](/submit/)



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

Join 30,424 other subscribers

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




![](https://pixel.wp.com/g.gif?blog=221720208&v=wpcom&tz=-4&user_id=0&arch_home=1&subd=a8cteam5105&host=wpscan.com&ref=&rand=0.07484518227274795)

Notifications