
# Unofficial Hi-Rez Studios API Developer Guide

[![License][project_bagde_license]][project_license]
[![*Nonsocial's support server*][project_bagde_discord_support_server]][project_discord_support_server]

> :construction: **It's a work in progress, still undergoing some change, documentation is in-progress.**

Unofficial Hi-Rez Studios API [documentation](#getting-started) (and [assets](#graphics) where possible) for [Paladins][paladins], [Realm Royale][realm_royale], and [Smite][smite].

## Purpose

Due to [Hi-Rez Studios][hi_rez_studios] not providing a detailed documentation for their API, this Developer Guide is here to assist those attempting to make their own API wrapper for their [API][hi_rez_studios_api_developer_guide].

This documentation holds the Methods Documentation and Source Code Examples, and its purpose is to provide Developers with the necessary information to access and utilize the API methods.

This documentation will consume a [JSON][json_website] response and therefore detailed descriptions of each data field are included where possible.

### Mantainance 🛠
As long as [Hi-Rez Studios][hi_rez_studios] doesn't change its APIs this documentation won't be changed. However, resources could be updated, added or removed when needed.

### [Getting Started][project_api_reference]

- [Registration][project_api_registration]

- Code Samples
To assist with development & debugging efforts, the following code samples are provided: [C Sharp][project_code_samples_csharp], [Java][project_code_samples_java] & [Python][project_code_samples_python].

The values for [API Keys][project_api_key] are removed for security purposes.  

Note that the API calls are synchronous and may take a few seconds before generating a response. You will probably call the API asynchronously, but for purposes of this exercise (to quickly understand how to work with the API methods) the synchronous method was used.

### Graphics

You can find any graphics [here][project_assets].
<!-- You can find any graphics that we’ve published for use [here][project_assets].-->

### How to contribute :octocat:

Feel free to contribute to this project, a helping hand is always appreciated.

 1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
 2. Fork [the repository][project_github_repo] on GitHub to start making your changes to the **master** branch (or branch off of it).
 3. Send a [pull request][github_help_pull_request] and bug the maintainer until it gets merged.

By contributing contents to this Wiki you shall implicitly accept that others might reuse these contents in other projects without restrictions.

If you have any questions, concerns, need further help, want to be up-to-date on, or like interested to contribute in any way or mantaining this project, please join [*Nonsocial's support server*][project_discord_support_server] on [Discord][discord].

### Disclaimer:

This project, including this repository, is neither created, affiliated, associated nor endorsed by [Hi-Rez Studios][hi_rez_studios], or any of its subsidiaries or its affiliates.

It is created by the community for the community.

Please refrain from contacting [Hi-Rez Studios][hi_rez_studios] regarding any issues or support of this project, instead feel free to submit an issue.

### Copyright & License 📝

This is a free, open source [![Open Source][open_source_icon]][open_source_definition], and MIT friendly project. Full license can be found in the [`LICENSE`][project_license] file. The programs in the “[code-samples][project_code_samples_folder]” subdirectory are in the public domain unless specified otherwise.

Please note, however, that this license does NOT cover third-party libraries used by project, they are under their own licenses. Please refer to those libraries for details on the license they use.

All information obtained is provided by Hi-Rez Studios API and is thus their property. According to Section 11a of the [`API Terms of Use`][hi_rez_studios_api_terms_of_use], you must attribute any data provided as below.

> Data provided by Hi-Rez. © 2019 Hi-Rez Studios, Inc. All rights reserved.

### Resources
<!-- Quick Links-->

#### Wrappers

* [![wrapper_cpp_hirezcpp][badge_wrapper_cpp_hirezcpp]][badge_wrapper_cpp_hirezcpp_github]
* [![wrapper_dotnet_paladins_dotnet][badge_wrapper_dotnet_paladins_dotnet]][badge_wrapper_dotnet_paladins_dotnet_github]
  [![wrapper_dotnet_realm_royale_dotnet][badge_wrapper_dotnet_realm_royale_dotnet]][badge_wrapper_dotnet_realm_royale_dotnet_github]
* [![wrapper_elixir_exrez][badge_wrapper_elixir_exrez]][badge_wrapper_elixir_exrez_github]
* [![wrapper_go_paladins_go][badge_wrapper_go_paladins_go]][badge_wrapper_go_paladins_go_github]
  [![wrapper_go_smite_paladins_realm_api_usage][badge_wrapper_go_smite_paladins_realm_api_usage]][badge_wrapper_go_smite_paladins_realm_api_usage_github]
  [![wrapper_go_go_smite_api][badge_wrapper_go_go_smite_api]][badge_wrapper_go_go_smite_api_github]
* [![wrapper_java_hi_rez_api][badge_wrapper_java_hi_rez_api]][badge_wrapper_java_hi_rez_api_github]
[![wrapper_java_paladins_java_api][badge_wrapper_java_paladins_java_api]][badge_wrapper_java_paladins_java_api_github]
[![wrapper_java_smite_api][badge_wrapper_java_smite_api]][badge_wrapper_java_smite_api_github]
* [![badge_wrapper_javascript_paladins_api][badge_wrapper_javascript_paladins_api]][badge_wrapper_javascript_paladins_api_github]
  [![wrapper_javascript_paladins.js][badge_wrapper_javascript_paladins.js]][badge_wrapper_javascript_paladins.js_github]
  [![wrapper_javascript_paladins_api_node.js][badge_wrapper_javascript_paladins_api_node]][badge_wrapper_javascript_paladins_api_node_github]
  [![wrapper_javascript_hirez.js][badge_wrapper_javascript_hirez.js]][badge_wrapper_javascript_hirez.js_github]
* [![wrapper_kotlin_hirez_sdk_kotlin][badge_wrapper_kotlin_hirez_sdk_kotlin]][badge_wrapper_kotlin_hirez_sdk_kotlin_github]
  [![wrapper_kotlin_paladins_api_kotlin][badge_wrapper_kotlin_paladins_api_kotlin]][badge_wrapper_kotlin_paladins_api_kotlin_github]
* [![wrapper_php_php_api][badge_wrapper_php_php_api]][badge_wrapper_php_php_api_github]
  [![wrapper_php_paladins_api_php_wrapper][badge_wrapper_php_paladins_api_php_wrapper]][badge_wrapper_php_paladins_api_php_wrapper_github]
  [![wrapper_php_smite_api_php_client][badge_wrapper_php_smite_api_php_client]][badge_wrapper_php_smite_api_php_client_github]
  [![wrapper_php_paladins_php][badge_wrapper_php_paladins_php]][badge_wrapper_php_paladins_php_github]
  [![wrapper_php_paladinsphp][badge_wrapper_php_paladinsphp]][badge_wrapper_php_paladinsphp_github]
* [![wrapper_python_pyrez][badge_wrapper_python_pyrez]][badge_wrapper_python_pyrez_github]
  [![wrapper_python_hirez_api][badge_wrapper_python_hirez_api]][badge_wrapper_python_hirez_api_github]
  [![wrapper_python_hi_rez_api][badge_wrapper_python_hi_rez_api]][badge_wrapper_python_hi_rez_api_github]
* [![wrapper_r_smite_r_files][badge_wrapper_r_smite_r_files]][badge_wrapper_r_smite_r_files_github]
* [![wrapper_ruby_paladins][badge_wrapper_ruby_paladins]][badge_wrapper_ruby_paladins_github]
  [![wrapper_ruby_smite_ruby][badge_wrapper_ruby_smite_ruby]][badge_wrapper_ruby_smite_ruby_github]
* [![wrapper_rust_hi_rust][badge_wrapper_rust_hi_rust]][badge_wrapper_rust_hi_rust_github]
  [![wrapper_rust_smite_motd][badge_wrapper_rust_smite_motd]][badge_wrapper_rust_smite_motd_github]
* [![wrapper_swift_swifty_smite_api][badge_wrapper_swift_swifty_smite_api]][badge_wrapper_swift_swifty_smite_api_github]
* [![wrapper_visual_basic_smite_vb][badge_wrapper_visual_basic_smite_vb]][badge_wrapper_visual_basic_smite_vb_github]
* [![wrapper_vue_realm_royale_first_vue_app][badge_wrapper_vue_realm_royale_first_vue_app]][badge_wrapper_vue_realm_royale_first_vue_app]
* [![wrapper_x_query_smite_api][badge_wrapper_x_query_smite_api]][badge_wrapper_x_query_smite_api]
<!--
  [![wrapper_php_smitephp][badge_wrapper_php_smitephp]][badge_wrapper_php_smitephp_github]
  [![wrapper_php_smite_php][badge_wrapper_php_smite_php]][badge_wrapper_php_smite_php_github]
  [![wrapper_php_smite_api_wp][badge_wrapper_php_smite_api_wp]][badge_wrapper_php_smite_api_wp_github]
-->

#### <pre>External Links</pre>

* :octocat: [GitHub Repository][project_github_repo]

* :link: [Hi-Rez Studios API · Development Credentials Application Form][hi_rez_studios_api_application_form]

* 📚 [Hi-Rez Studios API · Official Documentation][hi_rez_studios_api_developer_guide]

* :link: [Hi-Rez API Studios · Terms of Use Agreement][hi_rez_studios_api_terms_of_use]

* :link: [Hi-Rez Studios API Developer Collaboration · Podio][hi_rez_studios_api_podio_group]

* :link: [Hi-Rez Studios API · Press package][hi_rez_studios_press]

* :link: [Hi-Rez Studios · Website][hi_rez_studios]

* :link: [JSON Formatter][json_formatter]

* :link: [XML Formatter][xml_formatter]

<!--
	https://www.srcmake.com/home/paladins-smite-api
	http://paladins-api.herokuapp.com/api
	https://github.com/apugh/realm-api-docs/wiki
	https://github.com/PaladinsDev/API-Docs/tree/master/getting-started
	https://realmleaks.blogspot.com/

	https://img.shields.io/pypi/pyversions/boolify.svg?logo=cpp&logoColor=white&logoWidth=15&style=plastic
	https://img.shields.io/badge/Python-3.7.5-orange.svg?logo=python&logoColor=white&style=plastic
	https://img.shields.io/badge/hirezcpp-00bb88.svg?logo=python&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/p-groarke/hirezcpp

	https://pixlr.com/x/
	https://logodownload.org/

	https://www.hiclipart.com/free-transparent-background-png-clipart-gknlr
	https://www.pinpng.com/search/smite/
	https://www.pinpng.com/download/ibhxoo_logo-paladins-beta-black-sm-logo-paladins-beta/
	https://www.flaticon.com/search/2?word=mixer
-->

[discord]: https://discordapp.com/ "Discord App · Website"
[json_website]: https://json.org/ "Visit json.org"
[json_formatter]: https://jsonformatter.curiousconcept.com "JSON Formatter & Validator · Website"
[xml_formatter]: https://jsonformatter.org/xml-formatter "XML Formatter & Validator · Website"
[open_source_definition]: https://www.opensource.org "See http://www.opensource.org for the Open Source Definition"
[open_source_icon]: https://raw.githubusercontent.com/abhishekbanthia/Public-APIs/master/opensource.png
[github_help_pull_request]: https://help.github.com/en/articles/creating-a-pull-request-from-a-fork

[project_api_key]: ./api#api-key "Hi-Rez API Studios · API Key"
[project_api_reference]: ./api#api-reference "Hi-Rez API Studios · Reference"
[project_api_registration]: ./api#registration "Hi-Rez API Studios · Registration"
[project_assets]: ./_assets "Hi-Rez API Studios · Assets"
[project_code_samples_csharp]: ./code-samples/c-sharp.md "Code Sample · C#"
[project_code_samples_folder]: ./code-samples "Code Samples"
[project_code_samples_java]: ./code-samples/java.md "Code Sample · Java"
[project_code_samples_python]: ./code-samples/python.md "Code Sample · Python"
[project_discord_support_server]: https://discord.gg/XkydRPS "Support Server · Discord"
[project_bagde_discord_support_server]: https://img.shields.io/discord/549020573846470659.svg?logo=discordlogoWidth=15&style=plastic
[project_github_repo]: https://github.com/luissilva1044894/hirez-api-docs "hirez-api-docs · Github repo"
[project_license]: ./LICENSE "Hi-Rez API Docs · License"
[project_bagde_license]: https://img.shields.io/github/license/luissilva1044894/hirez-api-docs.svg?logo=githublogoWidth=10style=plastic

[hi_rez_studios]: https://www.hirezstudios.com "Visit Hi-Rez Studios Website"
[hi_rez_studios_api_application_form]: https://fs12.formsite.com/HiRez/form48/secure_index.html "Hi-Rez Studios API · Application Form"
[hi_rez_studios_api_developer_guide]: https://docs.google.com/document/d/1OFS-3ocSx-1Rvg4afAnEHlT3917MAK_6eJTR6rzr-BM "Smite / Paladins / Realm API Developer Guide"
[hi_rez_studios_api_podio_group]: https://podio.com/hirezstudioscom/smite-api-developer-collaboration "SMITE, Paladins, & Realm API Developer Collaboration"
[hi_rez_studios_api_terms_of_use]: https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/api-terms-of-use-agreement.pdf "Hi-Rez Studios API · Terms of Use"
[hi_rez_studios_press]: https://www.hirezstudios.com/press "Hi-Rez Studios API · Press"

[paladins]: https://www.paladins.com/ "Paladins Game · Website"
[realm_royale]: https://www.realmroyale.com/ "Realm Royale Game · Website"
[smite]: https://www.smitegame.com/ "Smite Game · Website"

[badge_wrapper_cpp_hirezcpp]: https://img.shields.io/static/v1?label=C%2B%2B&logo=github&message=hirezcpp&color=blueviolet&style=plastic&link=https://github.com/p-groarke/hirezcpp
[badge_wrapper_cpp_hirezcpp_github]: https://github.com/p-groarke/hirezcpp "hirezcpp · Github repo"

[badge_wrapper_dotnet_paladins_dotnet]: https://img.shields.io/static/v1?label=C%23&logo=.net&message=Paladins.NET&color=blueviolet&style=plastic&link=https://github.com/PaladinsDev/Paladins.NET
[badge_wrapper_dotnet_paladins_dotnet_github]: https://github.com/PaladinsDev/Paladins.NET "Paladins.NET · Github repo"

[badge_wrapper_dotnet_realm_royale_dotnet]: https://img.shields.io/static/v1?label=C%23&logo=.net&message=RealmRoyale.NET&color=blueviolet&style=plastic&link=https://github.com/fossilz/RealmRoyale.NET
[badge_wrapper_dotnet_realm_royale_dotnet_github]: https://github.com/fossilz/RealmRoyale.NET "RealmRoyale.NET · Github repo"

[badge_wrapper_elixir_exrez]: https://img.shields.io/static/v1?label=Elixir&logo=github&logoWidth=20&message=Exrez&color=blueviolet&style=plastic&link=https://github.com/luishendrix92/exrez
[badge_wrapper_elixir_exrez_github]: https://github.com/luishendrix92/exrez "exrez · Github repo"

[badge_wrapper_go_paladins_go]: https://img.shields.io/static/v1?label=Go&logo=go&logoWidth=20&message=PaladinsGo&color=blueviolet&style=plastic&link=https://github.com/danieljimenez/PaladinsGo
[badge_wrapper_go_paladins_go_github]: https://github.com/danieljimenez/PaladinsGo "PaladinsGo · Github repo"

[badge_wrapper_go_smite_paladins_realm_api_usage]: https://img.shields.io/static/v1?label=Go&logo=go&logoWidth=20&message=SMITE-Paladins-Realm-API-Usage&color=blueviolet&style=plastic&link=https://github.com/matin-n/SMITE-Paladins-Realm-API-Usage
[badge_wrapper_go_smite_paladins_realm_api_usage_github]: https://github.com/matin-n/SMITE-Paladins-Realm-API-Usage "SMITE-Paladins-Realm-API-Usage · Github repo"

[badge_wrapper_go_go_smite_api]: https://img.shields.io/static/v1?label=Go&logo=go&logoWidth=20&message=go-smite-api&color=blueviolet&style=plastic&link=https://github.com/duncanleo/go-smite-api
[badge_wrapper_go_go_smite_api_github]: https://github.com/duncanleo/go-smite-api "go-smite-api · Github repo"

[badge_wrapper_java_hi_rez_api]: https://img.shields.io/static/v1?label=Java&logo=java&logoWidth=20&message=HiRezAPI&color=blueviolet&style=plastic&link=https://github.com/stachu540/HiRezAPI
[badge_wrapper_java_hi_rez_api_github]: https://github.com/stachu540/HiRezAPI "HiRezAPI · Github repo"

[badge_wrapper_java_paladins_java_api]: https://img.shields.io/static/v1?label=Java&logo=java&logoWidth=20&message=Paladins%20Java%20API&color=blueviolet&style=plastic&link=https://github.com/HeyZeer0/Paladins-Java-API
[badge_wrapper_java_paladins_java_api_github]: https://github.com/HeyZeer0/Paladins-Java-API "Paladins-Java-API · Github repo"

[badge_wrapper_java_smite_api]: https://img.shields.io/static/v1?label=Java&logo=java&logoWidth=20&message=smite-api&color=blueviolet&style=plastic&link=https://github.com/Rabrg/smite-api
[badge_wrapper_java_smite_api_github]: https://github.com/Rabrg/smite-api "smite-api · Github repo"

[badge_wrapper_javascript_paladins_api]: https://img.shields.io/static/v1?label=Javascript&logo=javascript&logoWidth=20&message=paladins_api&color=blueviolet&style=plastic&link=https://github.com/itspauloroberto/paladins-api
[badge_wrapper_javascript_paladins_api_github]: https://github.com/itspauloroberto/paladins-api "paladins-api · Github repo"

[badge_wrapper_javascript_paladins.js]: https://img.shields.io/static/v1?label=Javascript&logo=javascript&logoWidth=20&message=paladins.js&color=blueviolet&style=plastic&link=https://github.com/PaladinsDev/paladins.js
[badge_wrapper_javascript_paladins.js_github]: https://github.com/PaladinsDev/paladins.js "paladins.js · Github repo"

[badge_wrapper_javascript_paladins_api_node]: https://img.shields.io/static/v1?label=Javascript&logo=javascript&logoWidth=20&message=paladins_api_node&color=blueviolet&style=plastic&link=https://github.com/barenddt/paladins-api-node
[badge_wrapper_javascript_paladins_api_node_github]: https://github.com/barenddt/paladins-api-node "paladins-api-node · Github repo"

[badge_wrapper_javascript_hirez.js]: https://img.shields.io/static/v1?label=Javascript&logo=javascript&logoWidth=20&message=hirez.js&color=blueviolet&style=plastic&link=https://github.com/messyfresh/hirez.js
[badge_wrapper_javascript_hirez.js_github]: https://github.com/messyfresh/hirez.js "hirez.js · Github repo"

[badge_wrapper_kotlin_hirez_sdk_kotlin]: https://img.shields.io/static/v1?label=Kotlin&logo=kotlin&logoWidth=20&message=Hirez_sdk_kotlin&color=blueviolet&style=plastic&link=https://github.com/tafel-io/Hirez-sdk-kotlin
[badge_wrapper_kotlin_hirez_sdk_kotlin_github]: https://github.com/tafel-io/Hirez-sdk-kotlin "Hirez-sdk-kotlin · Github repo"

[badge_wrapper_kotlin_paladins_api_kotlin]: https://img.shields.io/static/v1?label=Kotlin&logo=kotlin&logoWidth=20&message=Paladins_Api_Kotlin&color=blueviolet&style=plastic&link=https://github.com/geek0x90/Paladins-Api-Kotlin
[badge_wrapper_kotlin_paladins_api_kotlin_github]: https://github.com/geek0x90/Paladins-Api-Kotlin "Paladins-Api-Kotlin · Github repo"

[badge_wrapper_php_php_api]: https://img.shields.io/static/v1?label=PHP&logo=php&logoWidth=20&message=PHP_API&color=blueviolet&style=plastic&link=https://github.com/PaladinsDev/PHP-API
[badge_wrapper_php_php_api_github]: https://github.com/PaladinsDev/PHP-API "PHP-API · Github repo"

[badge_wrapper_php_paladins_api_php_wrapper]: https://img.shields.io/static/v1?label=PHP&logo=php&logoWidth=20&message=paladins_api_php_wrapper&color=blueviolet&style=plastic&link=https://github.com/lyrip/paladins-api-php-wrapper
[badge_wrapper_php_paladins_api_php_wrapper_github]: https://github.com/lyrip/paladins-api-php-wrapper "paladins-api-php · Github repo"

[badge_wrapper_php_smite_api_php_client]: https://img.shields.io/static/v1?label=PHP&logo=php&logoWidth=20&message=smite_api_php_client&color=blueviolet&style=plastic&link=https://github.com/dant89/smite-api-php-client
[badge_wrapper_php_smite_api_php_client_github]:https://github.com/dant89/smite-api-php-client "smite-api-php-client · Github repo"

[badge_wrapper_php_paladins_php]: https://img.shields.io/static/v1?label=PHP&logo=php&logoWidth=20&message=PaladinsPHP&color=blueviolet&style=plastic&link=https://github.com/teamreflex/PaladinsPHP
[badge_wrapper_php_paladins_php_github]: https://github.com/teamreflex/PaladinsPHP "PaladinsPHP · Github repo"

[badge_wrapper_php_paladinsphp]: https://img.shields.io/static/v1?label=PHP&logo=php&logoWidth=20&message=PaladinsPHP&color=blueviolet&style=plastic&link=https://github.com/bennetgallein/PaladinsPHP
[badge_wrapper_php_paladinsphp_github]: https://github.com/bennetgallein/PaladinsPHP "PaladinsPHP · Github repo"

[badge_wrapper_php_smitephp]: https://img.shields.io/static/v1?label=PHP&logo=php&logoWidth=20&message=SmitePHP&color=blueviolet&style=plastic&link=https://github.com/CurseStaff/SmitePHP
[badge_wrapper_php_smitephp_github]: https://github.com/CurseStaff/SmitePHP "SmitePHP · Github repo"

[badge_wrapper_php_smite_php]: https://img.shields.io/static/v1?label=PHP&logo=php&logoWidth=20&message=smite_php&color=blueviolet&style=plastic&link=https://github.com/AlekzB/smite-php
[badge_wrapper_php_smite_php_github]: https://github.com/AlekzB/smite-php "smite-php · Github repo"

[badge_wrapper_php_smite_api_wp]: https://img.shields.io/static/v1?label=PHP&logo=php&logoWidth=20&message=smite_api_wp&color=blueviolet&style=plastic&link=https://github.com/hirezstudios/smite-api-wp
[badge_wrapper_php_smite_api_wp_github]: https://github.com/hirezstudios/smite-api-wp "smite-api-wp · Github repo"

[badge_wrapper_python_pyrez]: https://img.shields.io/static/v1?label=Python&logo=python&logoWidth=20&message=Pyrez&color=blueviolet&style=plastic&link=https://github.com/luissilva1044894/Pyrez
[badge_wrapper_python_pyrez_github]: https://github.com/luissilva1044894/Pyrez "Pyrez · Github repo"

[badge_wrapper_python_hirez_api]: https://img.shields.io/static/v1?label=Python&logo=python&logoWidth=20&message=HiRezAPI&color=blueviolet&style=plastic&link=https://github.com/DevilXD/HiRezAPI
[badge_wrapper_python_hirez_api_github]: https://github.com/DevilXD/HiRezAPI "HiRezAPI · Github repo"

[badge_wrapper_python_hi_rez_api]: https://img.shields.io/static/v1?label=Python&logo=python&logoWidth=20&message=Hi_Rez_API&color=blueviolet&style=plastic&link=https://github.com/iforvard/Hi-RezAPI
[badge_wrapper_python_hi_rez_api_github]: https://github.com/iforvard/Hi-RezAPI "Hi-RezAPI · Github repo"

[badge_wrapper_r_smite_r_files]: https://img.shields.io/static/v1?label=R&logo=r&logoWidth=20&message=smiteRfiles&color=blueviolet&style=plastic&link=https://github.com/rwiedwald/smiteRfiles
[badge_wrapper_r_smite_r_files_github]: https://github.com/rwiedwald/smiteRfiles "smiteRfiles · Github repo"

[badge_wrapper_ruby_paladins]: https://img.shields.io/static/v1?label=Ruby&logo=ruby&logoWidth=20&message=paladins&color=blueviolet&style=plastic&link=https://github.com/davideghz/paladins
[badge_wrapper_ruby_paladins_github]: https://github.com/davideghz/paladins "paladins · Github repo"

[badge_wrapper_ruby_smite_ruby]: https://img.shields.io/static/v1?label=Ruby&logo=ruby&logoWidth=20&message=smite_ruby&color=blueviolet&style=plastic&link=https://github.com/NcUltimate/smite_ruby
[badge_wrapper_ruby_smite_ruby_github]: https://github.com/NcUltimate/smite_ruby "smite_ruby · Github repo"

[badge_wrapper_rust_hi_rust]: https://img.shields.io/static/v1?label=Rust&logo=rust&logoWidth=20&message=HiRust&color=blueviolet&style=plastic&link=https://github.com/JackStillwell/HiRust
[badge_wrapper_rust_hi_rust_github]: https://github.com/JackStillwell/HiRust "HiRust · Github repo"

[badge_wrapper_rust_smite_motd]: https://img.shields.io/static/v1?label=Rust&logo=rust&logoWidth=20&message=smite_motd&color=blueviolet&style=plastic&link=https://github.com/kdar/smitemotd
[badge_wrapper_rust_smite_motd_github]: https://github.com/kdar/smitemotd "smitemotd · Github repo"

[badge_wrapper_swift_swifty_smite_api]: https://img.shields.io/static/v1?label=Swift&logo=Swift&message=Swifty_Smite_API&color=blueviolet&style=plastic&link=https://github.com/OddMagnet/SwiftySmiteAPI
[badge_wrapper_swift_swifty_smite_api_github]: https://github.com/OddMagnet/SwiftySmiteAPI "SwiftySmiteAPI · Github repo"

[badge_wrapper_visual_basic_smite_vb]: https://img.shields.io/static/v1?label=Visual_Basic&logo=github&message=Smite_Vb&color=blueviolet&style=plastic&link=https://github.com/crimson-med/Smite-Vb
[badge_wrapper_visual_basic_smite_vb_github]: https://github.com/crimson-med/Smite-Vb "Smite-Vb · Github repo"

[badge_wrapper_vue_realm_royale_first_vue_app]: https://img.shields.io/static/v1?label=Vue&logo=github&message=realm_royale_first_vue_app&color=blueviolet&style=plastic&link=https://github.com/djlax805/realm_royale_first_vue_app
[badge_wrapper_vue_realm_royale_first_vue_app]: https://github.com/djlax805/realm_royale_first_vue_app "realm_royale_first_vue_app · Github repo"

[badge_wrapper_x_query_smite_api]: https://img.shields.io/static/v1?label=XQuery&logo=github&message=smite_api&color=blueviolet&style=plastic&link=https://github.com/LumielGR/smite-api
[badge_wrapper_x_query_smite_api]: https://github.com/LumielGR/smite-api "smite-api · Github repo"
