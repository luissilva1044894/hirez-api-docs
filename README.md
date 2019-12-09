
# Unofficial Hi-Rez Studios API Developer Guide

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

* [![wrapper_cpp_hirezcpp_][badge_wrapper_cpp_hirezcpp]][wrapper_cpp_hirezcpp]
* ![wrapper_dotnet_paladins_dotnet][badge_wrapper_dotnet_paladins_dotnet]
  ![wrapper_dotnet_realm_royale_dotnet][badge_wrapper_dotnet_realm_royale_dotnet]
* ![wrapper_elixir_exrez][badge_wrapper_elixir_exrez]
* ![wrapper_go_paladins_go][badge_wrapper_go_paladins_go]
  ![wrapper_go_smite_paladins_realm_api_usage][badge_wrapper_go_smite_paladins_realm_api_usage]
  ![wrapper_go_go_smite_api][badge_wrapper_go_go_smite_api]
* [![wrapper_java_hi_rez_api_][badge_wrapper_java_hi_rez_api]][wrapper_java_hi_rez_api]
[![wrapper_java_paladins_java_api_][badge_wrapper_java_paladins_java_api]][wrapper_java_paladins_java_api]
[![wrapper_java_smite_api_][badge_wrapper_java_smite_api]][wrapper_java_smite_api]

[Paladins-Java-API](https://github.com/HeyZeer0/Paladins-Java-API) [smite-api](https://github.com/Rabrg/smite-api)
* Javascript / NodeJS: [paladins-api](https://github.com/itspauloroberto/paladins-api), [paladins.js](https://github.com/PaladinsDev/paladins.js), [paladins-api-node](https://github.com/barenddt/paladins-api-node), [hirez.js](https://github.com/messyfresh/hirez.js)
* Kotlin: [Hirez-sdk-kotlin](https://github.com/tafel-io/Hirez-sdk-kotlin), [Paladins-Api-Kotlin](https://github.com/geek0x90/Paladins-Api-Kotlin)
* PHP: [PHP-API](https://github.com/PaladinsDev/PHP-API), [paladins-api-php-wrapper](https://github.com/lyrip/paladins-api-php-wrapper), [smite-api-php-client](https://github.com/dant89/smite-api-php-client), [PaladinsPHP](https://github.com/teamreflex/PaladinsPHP), [PaladinsPHP](https://github.com/bennetgallein/PaladinsPHP), [SmitePHP](https://github.com/CurseStaff/SmitePHP), [smite-php](https://github.com/AlekzB/smite-php), [smite-api-wp](https://github.com/hirezstudios/smite-api-wp)
* Python: [Pyrez](https://github.com/luissilva1044894/Pyrez), [HiRezAPI](https://github.com/DevilXD/HiRezAPI), [Hi-RezAPI](https://github.com/iforvard/Hi-RezAPI)
* R: [smiteRfiles](https://github.com/rwiedwald/smiteRfiles)
* Ruby: [paladins](https://github.com/davideghz/paladins), [smite_ruby](https://github.com/NcUltimate/smite_ruby)
* Rust: [HiRust](https://github.com/JackStillwell/HiRust), [smitemotd](https://github.com/kdar/smitemotd)
* Swift: [SwiftySmiteAPI](https://github.com/OddMagnet/SwiftySmiteAPI)
* Visual Basic: [Smite-Vb](https://github.com/crimson-med/Smite-Vb)
* Vue: [realm_royale_first_vue_app](https://github.com/djlax805/realm_royale_first_vue_app)
* XQuery: [smite-api](https://github.com/LumielGR/smite-api)

#### <pre>External Links</pre>

* :octocat: [GitHub Repository][project_github_repo]

* :link: [Development Credentials Application Form][hi_rez_studios_api_application_form]

* 📚 [Official Hi-Rez API Documentation][hi_rez_studios_api_developer_guide]

* :link: [Hi-Rez API Terms of Use Agreement][hi_rez_studios_api_terms_of_use]

* :link: [Realm Royale API Developer Collaboration - Podio][hi_rez_studios_api_podio_group]

* :link: [API Press package][hi_rez_studios_press]

* :link: [Hi-Rez Studios Website][hi_rez_studios]

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

[discord]: https://discordapp.com/ "Discord App"
[json_website]: https://json.org/ "Visit json.org"
[json_formatter]: https://jsonformatter.curiousconcept.com "JSON Formatter & Validator"
[xml_formatter]: https://jsonformatter.org/xml-formatter "XML Formatter & Validator"
[open_source_definition]: https://www.opensource.org "See http://www.opensource.org for the Open Source Definition"
[open_source_icon]: https://raw.githubusercontent.com/abhishekbanthia/Public-APIs/master/opensource.png
[github_help_pull_request]: https://help.github.com/en/articles/creating-a-pull-request-from-a-fork

[project_api_key]: ./api#api-key
[project_api_reference]: ./api#api-reference
[project_api_registration]: ./api#registration
[project_assets]: ./_assets
[project_code_samples_csharp]: ./code-samples/c-sharp.md
[project_code_samples_folder]: ./code-samples
[project_code_samples_java]: ./code-samples/java.md
[project_code_samples_python]: ./code-samples/python.md
[project_discord_support_server]: https://discord.gg/XkydRPS "Support Server · Discord"
[project_github_repo]: https://github.com/luissilva1044894/hirez-api-docs ""
[project_license]: https://github.com/luissilva1044894/hirez-api-docs ""

[hi_rez_studios]: https://www.hirezstudios.com "Hi-Rez Studios Website"
[hi_rez_studios_api_application_form]: https://fs12.formsite.com/HiRez/form48/secure_index.html
[hi_rez_studios_api_developer_guide]: https://docs.google.com/document/d/1OFS-3ocSx-1Rvg4afAnEHlT3917MAK_6eJTR6rzr-BM "Smite / Paladins / Realm API Developer Guide"
[hi_rez_studios_api_podio_group]: https://podio.com/hirezstudioscom/smite-api-developer-collaboration "SMITE, Paladins, & Realm API Developer Collaboration"
[hi_rez_studios_api_terms_of_use]: https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/api-terms-of-use-agreement.pdf "Hi-Rez Studios API · Terms of Use"
[hi_rez_studios_press]: https://www.hirezstudios.com/press

[badge_wrapper_cpp_hirezcpp]: https://img.shields.io/static/v1?label=C%2B%2B&logo=github&message=hirezcpp&color=blueviolet&style=plastic&link=https://github.com/p-groarke/hirezcpp
[wrapper_cpp_hirezcpp]: https://github.com/p-groarke/hirezcpp

[badge_wrapper_dotnet_paladins_dotnet]: https://img.shields.io/static/v1?label=C%23&logo=.net&message=Paladins.NET&color=blueviolet&style=plastic&link=https://github.com/PaladinsDev/Paladins.NET
[wrapper_dotnet_paladins_dotnet]: https://github.com/PaladinsDev/Paladins.NET

[badge_wrapper_dotnet_realm_royale_dotnet]: https://img.shields.io/static/v1?label=C%23&logo=.net&message=RealmRoyale.NET&color=blueviolet&style=plastic&link=https://github.com/fossilz/RealmRoyale.NET
[wrapper_dotnet_realm_royale_dotnet]: https://github.com/fossilz/RealmRoyale.NET

[badge_wrapper_elixir_exrez]: https://img.shields.io/static/v1?label=Elixir&logo=github&logoWidth=20&message=Exrez&color=blueviolet&style=plastic&link=https://github.com/luishendrix92/exrez
[wrapper_elixir_exrez]: https://github.com/luishendrix92/exrez

[badge_wrapper_go_paladins_go]: https://img.shields.io/static/v1?label=Go&logo=go&logoWidth=20&message=PaladinsGo&color=blueviolet&style=plastic&link=https://github.com/danieljimenez/PaladinsGo
[wrapper_go_paladins_go]: https://github.com/danieljimenez/PaladinsGo

[badge_wrapper_go_smite_paladins_realm_api_usage]: https://img.shields.io/static/v1?label=Go&logo=go&logoWidth=20&message=SMITE-Paladins-Realm-API-Usage&color=blueviolet&style=plastic&link=https://github.com/matin-n/SMITE-Paladins-Realm-API-Usage
[wrapper_go_smite_paladins_realm_api_usage]: https://github.com/matin-n/SMITE-Paladins-Realm-API-Usage

[badge_wrapper_go_go_smite_api]: https://img.shields.io/static/v1?label=Go&logo=go&logoWidth=20&message=go-smite-api&color=blueviolet&style=plastic&link=https://github.com/duncanleo/go-smite-api
[wrapper_go_go_smite_api]: https://github.com/duncanleo/go-smite-api

[badge_wrapper_java_hi_rez_api]: https://img.shields.io/static/v1?label=Java&logo=Java&logoWidth=20&message=HiRezAPI&color=blueviolet&style=plastic&link=https://github.com/stachu540/HiRezAPI
[wrapper_java_hi_rez_api]: https://github.com/stachu540/HiRezAPI

[badge_wrapper_java_paladins_java_api]: https://img.shields.io/static/v1?label=Java&logo=Java&logoWidth=20&message=Paladins%20Java%20API&color=blueviolet&style=plastic&link=https://github.com/HeyZeer0/Paladins-Java-API
[wrapper_java_paladins_java_api]: https://github.com/HeyZeer0/Paladins-Java-API

[badge_wrapper_java_smite_api]: https://img.shields.io/static/v1?label=Java&logo=Java&logoWidth=20&message=smite-api&color=blueviolet&style=plastic&link=https://github.com/Rabrg/smite-api
[wrapper_java_smite_api]: https://github.com/Rabrg/smite-api

[badge_wrapper_javascript_paladins_api]: https://img.shields.io/badge/paladins_api-blueviolet?logo=javascript&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/itspauloroberto/paladins-api
[badge_wrapper_javascript_paladins.js]: https://img.shields.io/badge/paladins.js-blueviolet?logo=javascript&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/PaladinsDev/paladins.js
[badge_wrapper_javascript_paladins_api_node]: https://img.shields.io/badge/paladins_api_node-blueviolet?logo=javascript&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/barenddt/paladins-api-node
[badge_wrapper_javascript_hirez.js]: https://img.shields.io/badge/hirez.js-blueviolet?logo=javascript&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/messyfresh/hirez.js

[badge_wrapper_kotlin_hirez_sdk_kotlin]: https://img.shields.io/badge/Hirez_sdk_kotlin-blueviolet?logo=kotlin&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/tafel-io/Hirez-sdk-kotlin
[badge_wrapper_kotlin_paladins_api_kotlin]: https://img.shields.io/badge/Paladins_Api_Kotlin-blueviolet?logo=kotlin&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/geek0x90/Paladins-Api-Kotlin

[badge_wrapper_php_php_api]: https://img.shields.io/badge/PHP_API-blueviolet?logo=php&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/PaladinsDev/PHP-API
[badge_wrapper_php_paladins_api_php_wrapper]: https://img.shields.io/badge/paladins_api_php_wrapper-blueviolet?logo=php&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/lyrip/paladins-api-php-wrapper
[badge_wrapper_php_smite_api_php_client]: https://img.shields.io/badge/smite_api_php_client-blueviolet?logo=php&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/dant89/smite-api-php-client
[badge_wrapper_php_paladins_php]: https://img.shields.io/badge/PaladinsPHP-blueviolet?logo=php&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/teamreflex/PaladinsPHP
[badge_wrapper_php_paladinsphp]: https://img.shields.io/badge/PaladinsPHP-blueviolet?logo=php&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/bennetgallein/PaladinsPHP
[badge_wrapper_php_smitephp]: https://img.shields.io/badge/SmitePHP-blueviolet?logo=php&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/CurseStaff/SmitePHP
[badge_wrapper_php_smite_php]: https://img.shields.io/badge/smite_php-blueviolet?logo=php&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/AlekzB/smite-php
[badge_wrapper_php_smite_api_wp]: https://img.shields.io/badge/smite_api_wp-blueviolet?logo=php&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/hirezstudios/smite-api-wp

[badge_wrapper_python_pyrez]: https://img.shields.io/badge/Pyrez-blueviolet?logo=python&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/luissilva1044894/Pyrez
[badge_wrapper_python_hirez_api]: https://img.shields.io/badge/HiRezAPI-blueviolet?logo=python&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/DevilXD/HiRezAPI
[badge_wrapper_python_hi_rez_api]: https://img.shields.io/badge/Hi_Rez_API-blueviolet?logo=python&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/iforvard/Hi-RezAPI

[badge_wrapper_python_smite_r_files]: https://img.shields.io/badge/smiteRfiles-blueviolet?logo=r&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/rwiedwald/smiteRfiles

[badge_wrapper_ruby_paladins]: https://img.shields.io/badge/paladins-blueviolet?logo=ruby&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/davideghz/paladins
[badge_wrapper_ruby_smite_ruby]: https://img.shields.io/badge/smite_ruby-blueviolet?logo=ruby&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/NcUltimate/smite_ruby

[badge_wrapper_rust_hi_rust]: https://img.shields.io/badge/HiRust-blueviolet?logo=rust&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/JackStillwell/HiRust
[badge_wrapper_rust_smite_motd]: https://img.shields.io/badge/smite_motd-blueviolet?logo=rust&logoColor=white&logoWidth=20&style=plastic&link=https://github.com/kdar/smitemotd

[badge_wrapper_swift_swifty_smite_api]: https://img.shields.io/static/v1?label=Swift&logo=Swift&message=Swifty_Smite_API&color=blueviolet&style=plastic&link=https://github.com/OddMagnet/SwiftySmiteAPI

[badge_wrapper_visual_basic_smite_vb]: https://img.shields.io/static/v1?label=Visual_Basic&logo=github&message=Smite_Vb&color=blueviolet&style=plastic&link=https://github.com/crimson-med/Smite-Vb

[badge_wrapper_vue_realm_royale_first_vue_app]: https://img.shields.io/static/v1?label=Vue&logo=github&message=realm_royale_first_vue_app&color=blueviolet&style=plastic&link=https://github.com/djlax805/realm_royale_first_vue_app

[badge_wrapper_x_query_smite_api]: https://img.shields.io/static/v1?label=XQuery&logo=github&message=smite_api&color=blueviolet&style=plastic&link=https://github.com/LumielGR/smite-api
