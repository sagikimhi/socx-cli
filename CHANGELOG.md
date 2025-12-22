
## [unreleased]


### ⛰️  Features

- *(Makefile)* add Makefile to automate development tasks [6447162](https://github.com/sagikimhi/socx-cil/commits/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9)

- *(cli)* add support for short_help in addition to help in plugins [75298aa](https://github.com/sagikimhi/socx-cil/commits/75298aa4a417afe58f8ae09f34aced4a6c59e51e)

- *(cli)* add --version flag for printing version info [02d9480](https://github.com/sagikimhi/socx-cil/commits/02d9480436e38d87ac0f6577c7efcc295a3881d8)

- *(cli)* add callbacks to ease handling of options and arguments [70bd332](https://github.com/sagikimhi/socx-cil/commits/70bd332e501ba2a1b1e1dad524a80220d242a161)

- *(cli.plugin)* add support for shell script plugins (#104) [c9305af](https://github.com/sagikimhi/socx-cil/commits/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59)

- *(cli.plugin)* add support for shell script plugins (#103) [8d50e38](https://github.com/sagikimhi/socx-cil/commits/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e)

- *(cli.plugin)* add support for shell script plugins [88faffe](https://github.com/sagikimhi/socx-cil/commits/88faffe9018817a7f60154edb106e9355165811c)

- *(cli/plugins)* add env subcommand and plugin [bf109dd](https://github.com/sagikimhi/socx-cil/commits/bf109ddba85072771e26c860387367491e714b99)

- *(console)* use and reconfigure global console [09baf1a](https://github.com/sagikimhi/socx-cil/commits/09baf1ac414e1bc29850656d604c23345a0b3954)

- *(console)* install pretty tracebacks on console [d65333a](https://github.com/sagikimhi/socx-cil/commits/d65333a6dc39d3c518472db4e60c3934694af8fa)

- *(decorators)* add option to pass verbosity level arg to log_it [e9bf43b](https://github.com/sagikimhi/socx-cil/commits/e9bf43bed1243f31f2d505c0c1632ca0e6227370)

- *(options)* [**breaking**] add global options, option groups, and callbacks [73f0583](https://github.com/sagikimhi/socx-cil/commits/73f058334a81f8ff40809891ea16aa464fe07cc2)

- *(plugin)* add plug command group for handling plugins (#54) [42ade7a](https://github.com/sagikimhi/socx-cil/commits/42ade7af08f61ba1473bb60c9112baad9dc02604)

- *(plugin)* add plug command group for handling plugins [c11dc1b](https://github.com/sagikimhi/socx-cil/commits/c11dc1bd653a87c9abd36e0d4444eadf1583b095)

- *(regression)* add async runtime writes of regression tests outputs [c69b678](https://github.com/sagikimhi/socx-cil/commits/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b)

- *(regression)* write regression results, per-test stdout and stderr to disk [d7fed4d](https://github.com/sagikimhi/socx-cil/commits/d7fed4d27985ba0293aa9433bd69d4e5700eb567)

- *(regression)* add regression rerun support to cli (#22) [8d5573f](https://github.com/sagikimhi/socx-cil/commits/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2)

- *(regression)* fix program not ending, log pass/fail at exit (#20) [2f869b3](https://github.com/sagikimhi/socx-cil/commits/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a)

- *(regression)* add async support to test and regression. [0a723d0](https://github.com/sagikimhi/socx-cil/commits/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a)

- *(regression)* add RegressionStatus enum [fd45eb2](https://github.com/sagikimhi/socx-cil/commits/fd45eb2d0ff9532419c7e74e76fc79f901277b21)

- *(rgr)* add tui command, change 'rrfh' command name to 'run' [9b610d4](https://github.com/sagikimhi/socx-cil/commits/9b610d4203f462c12a059cb4fe0b6f091b2c91a7)

- *(rich-click)* add rich click help menu for sub-commands (#23) [3ef833c](https://github.com/sagikimhi/socx-cil/commits/3ef833cee29307822ebc29d548f9f25291944065)

- *(rich-click)* add rich click help menu for sub-commands [92a4b80](https://github.com/sagikimhi/socx-cil/commits/92a4b80b4af6789935223db9cc2ad73c504d0e63)

- *(settings)* configure rich-click from yaml configuration settings [0d2335c](https://github.com/sagikimhi/socx-cil/commits/0d2335cddefb9520f370ab07e3c9509ebc0a3410)

- *(socx.config.serializers)* add object serialization module [c8e7592](https://github.com/sagikimhi/socx-cil/commits/c8e759282bd3ed27c253a28a7e9f841825c19f87)

- *(socx_plugins.converters)* add @command converter [bfc1c62](https://github.com/sagikimhi/socx-cil/commits/bfc1c620419543b663db8fbd795fab08484ea480)

- *(socx_plugins.git)* add more `socx git` commands (#101) [a84fd1a](https://github.com/sagikimhi/socx-cil/commits/a84fd1a03c9846975ec71841819f8692d5acafc5)

- *(socx_plugins.git)* add live and pager output support [5476f2d](https://github.com/sagikimhi/socx-cil/commits/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa)

- *(socx_plugins.git)* implement git log command [57a575a](https://github.com/sagikimhi/socx-cil/commits/57a575a5c946075787afd184f6fde8346fee7011)

- *(socx_plugins.git)* execute manifest git commands in parallel [76ffcfb](https://github.com/sagikimhi/socx-cil/commits/76ffcfb27952479f05d1ebfb635bf37dd2ea6955)

- *(socx_plugins.git)* add git diff and git pull commands [2d3ec39](https://github.com/sagikimhi/socx-cil/commits/2d3ec39d9e63cb25023e1847b36a03cba968ec34)

- *(socx_plugins.git)* implement git multi-status [13cb570](https://github.com/sagikimhi/socx-cil/commits/13cb570c169301f70ba519e6b8b64424001d04ee)

- *(socx_plugins.git)* add ahead-behind status column to manifest [754c819](https://github.com/sagikimhi/socx-cil/commits/754c819895a3fa3398d088ae24688dedc2be8a21)

- *(socx_plugins.git.manifest)* add cmd_timeout cfg field [7ade98a](https://github.com/sagikimhi/socx-cil/commits/7ade98ae506e3a08218ebab67cb3700469863ee0)

- *(socx_plugins.rgr)* handle arguments with callbacks [666c43e](https://github.com/sagikimhi/socx-cil/commits/666c43e1cf6bccb065344a4bf3c6fe15ed157dc1)

- *(test)* add base test class and asyncio support [74bbe8f](https://github.com/sagikimhi/socx-cil/commits/74bbe8fd909457e7b8ee671a172ede958ea36fd7)

- *(tui)* wip developing ui [f8a11b1](https://github.com/sagikimhi/socx-cil/commits/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a)

- *(tui)* add vim-like movement bind modes [13142ee](https://github.com/sagikimhi/socx-cil/commits/13142eebb58c37a233de573c1502ce0c4235da08)

- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) [a9d65aa](https://github.com/sagikimhi/socx-cil/commits/a9d65aab9323a48f7879c41f0ffdb66c9b320294)


### 🐛 Bug Fixes

- *(.env)* correct dotenv development env variables [bfe012e](https://github.com/sagikimhi/socx-cil/commits/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373)

- *(Makefile)* fix export_svg rule [c2427ca](https://github.com/sagikimhi/socx-cil/commits/c2427ca98fd39232966819da69453084ba765b51)

- *(Makefile)* fix incorrect flags in `make publish` rule [b35f0bf](https://github.com/sagikimhi/socx-cil/commits/b35f0bfa9bca327858dd2074e89c5ce8d2182552)

- *(Makefile)* fix `make clean` rules [ab17ac2](https://github.com/sagikimhi/socx-cil/commits/ab17ac21cf22269760af8a2a4b0d990968a1bc16)

- *(_CmdLine)* fix _CmdLine inheritence [0126aef](https://github.com/sagikimhi/socx-cil/commits/0126aef8692abe3a638866254e42482bf0de48da)

- *(cli)* fix runtime loading of CLI plugins [38c7148](https://github.com/sagikimhi/socx-cil/commits/38c714805f7e49a098d97078c0af473777a546c5)

- *(cli)* fix CLI after breaking changes of rich-click 1.9.0 [d2e9816](https://github.com/sagikimhi/socx-cil/commits/d2e98160402d4af35a53f417ab393c288d7646d8)

- *(cli)* fix tui decorator type annotation [a1b194f](https://github.com/sagikimhi/socx-cil/commits/a1b194f16b01f37538d53d3ffe3348ce46257a1c)

- *(cli)* fix type hints of tui decorator [f27d96e](https://github.com/sagikimhi/socx-cil/commits/f27d96e49b57dff1425bf43fa77045be7ed9f86d)

- *(cli)* add missing rich click dependency [48b4161](https://github.com/sagikimhi/socx-cil/commits/48b4161244681eeccca9145110e2d03c22fed0c9)

- *(cli)* add return code on exit from main [8f3eb61](https://github.com/sagikimhi/socx-cil/commits/8f3eb6147e3f70589168609460cb543d7a92d7c9)

- *(cli/callbacks)* fix option callbacks [2dfa959](https://github.com/sagikimhi/socx-cil/commits/2dfa959a4cd0c962dab1de1f7d07cd91405c020e)

- *(config)* correct typing of `get_settings` [edc084d](https://github.com/sagikimhi/socx-cil/commits/edc084d10265a1136eabd93455170a9b6d3548a8)

- *(config.converters)* fix IncludeConverter [147ef9a](https://github.com/sagikimhi/socx-cil/commits/147ef9a0506e0c36f604d6475e5961fd72847127)

- *(config.converters)* fix @command help texts [8ece5cb](https://github.com/sagikimhi/socx-cil/commits/8ece5cb4f3850b917059a7ab230665b3835ffbf1)

- *(config/metadata)* use __spec__.name instead of __package__ [9d27ca6](https://github.com/sagikimhi/socx-cil/commits/9d27ca628c98720a02b44e3873edd499eef63ee7)

- *(convert)* fix lst to sv converter [6f5e58f](https://github.com/sagikimhi/socx-cil/commits/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9)

- *(converters)* fix command converter runtime warning [04a8ca7](https://github.com/sagikimhi/socx-cil/commits/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46)

- *(decorators)* log_it now logs to global socx.log run log [c18e495](https://github.com/sagikimhi/socx-cil/commits/c18e495d892b2770fcd4d9c751b5342e2d0958cd)

- *(dotenv)* correct dotenv configs [54f8cf5](https://github.com/sagikimhi/socx-cil/commits/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548)

- *(io)* fix mypy errors in log.py [5bb8e06](https://github.com/sagikimhi/socx-cil/commits/5bb8e06bd3af45240f8d3f19aa427a084ad4f197)

- *(io)* fix mypy errors in decorators.py [5fdecd5](https://github.com/sagikimhi/socx-cil/commits/5fdecd5e12893d03961c942200f6089854a4592e)

- *(io.decorators)* fix typing [9e7881f](https://github.com/sagikimhi/socx-cil/commits/9e7881f61f01915165c0373520051cd85c568138)

- *(log)* fix debug logging to socx.log when debug mode is enabled [6a14191](https://github.com/sagikimhi/socx-cil/commits/6a1419191bb654c88aaa494d7572d8e0613f1523)

- *(plugin/git)* fix ref and json formatted manifests [dcc992c](https://github.com/sagikimhi/socx-cil/commits/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b)

- *(plugins)* fix loading of external/3rd-party plugins [fd87676](https://github.com/sagikimhi/socx-cil/commits/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8)

- *(plugins/convert/reader)* remove relative import and fix typing [6dd9ce0](https://github.com/sagikimhi/socx-cil/commits/6dd9ce07070bd8a9c0779f83e16a0252142684cf)

- *(plugins/git)* fix missing column names in json manifest [cc7f746](https://github.com/sagikimhi/socx-cil/commits/cc7f746fb98727ef5b110116217ed2a6595b0757)

- *(plugins/git)* fix inconsistent revision hash length in manifest [b5f0d88](https://github.com/sagikimhi/socx-cil/commits/b5f0d88789287a9a289fbc20e66fa220d915b08c)

- *(plugins/rgr)* fix failed and passed test file formatting [06cb7e5](https://github.com/sagikimhi/socx-cil/commits/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf)

- *(plugins/rgr)* fix mypy errors in _rgr.py [061625d](https://github.com/sagikimhi/socx-cil/commits/061625d1ab5c03609b00b92f3a3cefc9b7a42766)

- *(plugins/tui, pre-commit)* fix broken terminal ui, set up pre-commit [bd60074](https://github.com/sagikimhi/socx-cil/commits/bd600741c34a4c009d4cbe72b6567c95013ba3da)

- *(regression)* fix broken rgr command due to mypy fixes [a5ac756](https://github.com/sagikimhi/socx-cil/commits/a5ac7566be05acd5e683b689d2c7392c1d2e28e4)

- *(regression)* fix mypy errors in regression subpackage [3626bed](https://github.com/sagikimhi/socx-cil/commits/3626beddedb914f370a9d920dbaf2bb91aefdd21)

- *(regression)* replace print with log in meth 'start', add missing await (#24) [8133742](https://github.com/sagikimhi/socx-cil/commits/81337423de743af0d67af43b2457e3f7c3ecb1b8)

- *(regression)* correct default gateway configurations (#21) [1b3bf5d](https://github.com/sagikimhi/socx-cil/commits/1b3bf5d088b7f19ec94947d636b161c15cea0d06)

- *(regression)* fix issue ignoring limit causing all cmds to be ran [eddd01f](https://github.com/sagikimhi/socx-cil/commits/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76)

- *(regression, plugins/rgr)* fix mypy typing errors [ceb0dbf](https://github.com/sagikimhi/socx-cil/commits/ceb0dbfdff2ad645940a435f06803f33b87921a1)

- *(regression.yaml)* fix default path value [5b20254](https://github.com/sagikimhi/socx-cil/commits/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf)

- *(ruff-check)* fix linter errors [8207c63](https://github.com/sagikimhi/socx-cil/commits/8207c6342287279f97909eec94c3b79382debd59)

- *(settings)* fix issue with reconfigure not overriding old values [1375123](https://github.com/sagikimhi/socx-cil/commits/137512363db8f12c2ed1b74f509ae5b9e956c947)

- *(settings/rgr)* fix incorrect assets path setting [7719ecf](https://github.com/sagikimhi/socx-cil/commits/7719ecf97bbe223e0076745f268836819a6b3ba3)

- *(socx.cli)* only load `click.Command` subclasses as plugins [7426e54](https://github.com/sagikimhi/socx-cil/commits/7426e54b3610c45d21eba71fc5ee7e524a756dfc)

- *(socx.cli)* fix tui decorator type annotation [3e30a0f](https://github.com/sagikimhi/socx-cil/commits/3e30a0f57300d4828b7bfd0958e534238ba47d14)

- *(socx.cli._cli)* fix _CmdLine inheritence [554c5b8](https://github.com/sagikimhi/socx-cil/commits/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb)

- *(socx.config)* fix configuration overriding and loading order [e57ef5b](https://github.com/sagikimhi/socx-cil/commits/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d)

- *(socx.config._config)* fix incorrect settings_file argument [f6cd1ff](https://github.com/sagikimhi/socx-cil/commits/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce)

- *(socx.config.metadata)* fix exception due to missing __spec__ [8ed76e5](https://github.com/sagikimhi/socx-cil/commits/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30)

- *(socx.io)* fix missing `log` export [f9589bf](https://github.com/sagikimhi/socx-cil/commits/f9589bfe924fb627c0d023b6e202459d8c6ef55c)

- *(socx.io.decorators)* fix typing [a7bc0e1](https://github.com/sagikimhi/socx-cil/commits/a7bc0e1e928aa910843c1370081e23f40dd7fad1)

- *(socx.io.log)* set up 'socx' logger instead of root logger [62473f8](https://github.com/sagikimhi/socx-cil/commits/62473f82fdecde2e0771b4b71c59bb159e4c1883)

- *(socx.regression.regression)* set start and finish times [9c0b64c](https://github.com/sagikimhi/socx-cil/commits/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e)

- *(socx_plugins.config)* fix `socx config get` help menu [97a4d04](https://github.com/sagikimhi/socx-cil/commits/97a4d0405cc9e40105c64106e7adb052f80893b7)

- *(socx_plugins.config.edit)* fix edit command [7133779](https://github.com/sagikimhi/socx-cil/commits/71337798f37918f47c720840c4e3231bda1708eb)

- *(socx_plugins.git)* fix some typing issues in manifest, utils [b72a44a](https://github.com/sagikimhi/socx-cil/commits/b72a44a0a08e15c486e131689cc418ca1e3329f6)

- *(socx_plugins.git)* minor typing fixes in git manifest plugin [64acf03](https://github.com/sagikimhi/socx-cil/commits/64acf03864dd9be029f3956967e2c710ad4de786)

- *(socx_plugins.git.cli)* fix typing issue in print_command_outputs [12e2e1b](https://github.com/sagikimhi/socx-cil/commits/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9)

- *(socx_plugins.git.utils)* fix current directory repo missing from manifest [582b688](https://github.com/sagikimhi/socx-cil/commits/582b68804db6c813f54359c1497e9bdcf08c7783)

- *(socx_plugins.git.utils)* fix typing errors [1014cdc](https://github.com/sagikimhi/socx-cil/commits/1014cdc191bcec494a8001469430f4f56f3f9d11)

- *(socx_plugins.rgr)* fix -h flag not triggering help menu [717b424](https://github.com/sagikimhi/socx-cil/commits/717b424c85ec2f9ff43891a7258da3809fd62d0a)

- *(socx_plugins.rgr.pixie_test)* correct path to test's log file [f525fa5](https://github.com/sagikimhi/socx-cil/commits/f525fa568cb4cb37195bb0c080dc9395c9680817)

- *(socx_plugins.version)* fix version command [b8fba3a](https://github.com/sagikimhi/socx-cil/commits/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a)

- *(socx_tui)* fix AttributeError when loading regression from file [4dcda47](https://github.com/sagikimhi/socx-cil/commits/4dcda47e23fa775885fd1468357dbaaa36a28305)

- *(test)* fix test failed status even when passed [026dd55](https://github.com/sagikimhi/socx-cil/commits/026dd55220be8bb6f5db250eb7a11e6169ba3998)

- *(tui)* fix mypy typing errors, discard Vim implementation [24737e3](https://github.com/sagikimhi/socx-cil/commits/24737e336505d271d7c60008c3e154adf2d4d316)

- *(tui)* fix mypy errors [73ddf0f](https://github.com/sagikimhi/socx-cil/commits/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404)

- *(visitor)* fix type hints and implementation of traversals [105220b](https://github.com/sagikimhi/socx-cil/commits/105220bedca8859aff323410858c624e5bc25092)

- *(visitor)* add empty __slots__ to protocol classes [356fdcd](https://github.com/sagikimhi/socx-cil/commits/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e)

- discard uvloop dependency to support for python3.14 [621a1f2](https://github.com/sagikimhi/socx-cil/commits/621a1f214fb18d98218796fdd785a6168496fa87)

- fix mypy typing errors [702ec05](https://github.com/sagikimhi/socx-cil/commits/702ec052803011b8e0184751ee8ca4ae01b66f55)

- fix all mypy errors [dd80f31](https://github.com/sagikimhi/socx-cil/commits/dd80f31155efff34ca9451e3147bfcf6dd4bf50c)

- correct warea to WAREA [155ae59](https://github.com/sagikimhi/socx-cil/commits/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a)

- add misssing socx_patches package [a2a20d8](https://github.com/sagikimhi/socx-cil/commits/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6)

- add missing log module exports [78e001e](https://github.com/sagikimhi/socx-cil/commits/78e001e6d066fe627797d6a2f513f2ba0bddfc9a)


### 🚜 Refactor

- *(Makefile)* run 'make clean' at the end of 'docs_deploy' [db554b3](https://github.com/sagikimhi/socx-cil/commits/db554b33c0762161e46ce133d33851c183740988)

- *(Makefile)* add changelog generation variables [6a9887a](https://github.com/sagikimhi/socx-cil/commits/6a9887a14786914bacc69a99e0994b0cb6b5004c)

- *(Makefile)* use `$(UV)` instead of `uv` in export_svg [893daa8](https://github.com/sagikimhi/socx-cil/commits/893daa82215e0a567ed253ce6e95e5ca73dfb821)

- *(cli)* read context_settings from settings.cli [80eabdd](https://github.com/sagikimhi/socx-cil/commits/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9)

- *(cli.cfg)* adjust default configurations [ddc414b](https://github.com/sagikimhi/socx-cil/commits/ddc414b855d38778344bf3d096844dafc69d743e)

- *(cli.cfg)* remove unused `cfg` function [062f6ee](https://github.com/sagikimhi/socx-cil/commits/062f6eebabf0cbccdad07715bf321cea5a6e2f64)

- *(cli.options)* rename method add_options to join_decorators [96f9afe](https://github.com/sagikimhi/socx-cil/commits/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe)

- *(config._config)* pass logger to `log_it` decorator [dc86e0c](https://github.com/sagikimhi/socx-cil/commits/dc86e0ca6b2f2d49a2834964a5aba07797ee298e)

- *(config.converters)* improve error handling [09fbe8f](https://github.com/sagikimhi/socx-cil/commits/09fbe8fbc25f03f4994557bd01cb88f01a24112f)

- *(io.console)* stop using global rich.console.console instance [d9c3e52](https://github.com/sagikimhi/socx-cil/commits/d9c3e520addde8307f86f44a4093349d718f61ad)

- *(io.decorators)* add optional logger parameter [eecef55](https://github.com/sagikimhi/socx-cil/commits/eecef55c588f85ec21e83f6a8f847c83b9eccfba)

- *(log)* enable tracebacks in logs [b4f0579](https://github.com/sagikimhi/socx-cil/commits/b4f057932d29ee59341b678db1885914be5e9bf0)

- *(log)* rename level to get_level, export get_logger [0b0f41c](https://github.com/sagikimhi/socx-cil/commits/0b0f41cfca7792f503adb12ece74193d11bcccc6)

- *(mixins)* move mixins into patterns subpackage [b620400](https://github.com/sagikimhi/socx-cil/commits/b620400a7da2066e45bb0f30c2e8d8536ece091c)

- *(plugins)* [**breaking**] rename env cmd to git and rewrite as package [464f183](https://github.com/sagikimhi/socx-cil/commits/464f1830450ea722835034e2fdf948cd009885de)

- *(plugins/env)* cleanup env code and add debug logging [d15e5f1](https://github.com/sagikimhi/socx-cil/commits/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075)

- *(regression)* clean up code and improve progress visualization [5e327ed](https://github.com/sagikimhi/socx-cil/commits/5e327ed9a2c5c829bccab71d723a40f36a310d6d)

- *(regression)* improve input assets for testing and adjust settings [483bd79](https://github.com/sagikimhi/socx-cil/commits/483bd790aa47c2f4df87314ca70bb6c639b179a9)

- *(settings)* rewrite settings.toml and plugins.toml as yaml [68dc3ad](https://github.com/sagikimhi/socx-cil/commits/68dc3adc6a32885eaf31838355dca1c568019f78)

- *(settings.git.manifest)* rename 'default_format' field to 'format' [0bc6dd0](https://github.com/sagikimhi/socx-cil/commits/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe)

- *(settings/git.yaml)* add --no-write-fetch-head to fetch flags [db8cf61](https://github.com/sagikimhi/socx-cil/commits/db8cf611f14fedf7aee1142b5aa9a25460157756)

- *(socx.cli.cfg)* adjust default configurations [486442f](https://github.com/sagikimhi/socx-cil/commits/486442f17e1c24d1cf16ae1cab73b46744070d7a)

- *(socx.cli.cfg)* remove unused `cfg` function [b0e0a04](https://github.com/sagikimhi/socx-cil/commits/b0e0a049c26adfd2b170549933d50d2da2fbe1cf)

- *(socx.config._config)* pass logger to `log_it` decorator [e3a5e30](https://github.com/sagikimhi/socx-cil/commits/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c)

- *(socx.config.converters)* improve exception handling [8c72a77](https://github.com/sagikimhi/socx-cil/commits/8c72a77fe2a18dbd93b152be50373a0c0a422c66)

- *(socx.config.converters)* use universal_pathlib [701015d](https://github.com/sagikimhi/socx-cil/commits/701015dfcc2132e87ca6a2d8444740cb24f3359b)

- *(socx.config.formatter)* adjust tree formatter output style [55434a1](https://github.com/sagikimhi/socx-cil/commits/55434a1a1e62587b3eef038a4cb218f9d7870050)

- *(socx.config.paths)* use upath.UPath instead of pathlib.Path [a60c8fa](https://github.com/sagikimhi/socx-cil/commits/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be)

- *(socx.config.paths)* add APP_ROOT_DIR to paths module [003cb48](https://github.com/sagikimhi/socx-cil/commits/003cb48e7bf6b622e86c132630eabbb8dfe2c07e)

- *(socx.io.decorators)* add optional logger parameter [fa69f79](https://github.com/sagikimhi/socx-cil/commits/fa69f7938023e64b66ed548d459302885bfae7e0)

- *(socx_plugins.git)* transition to using sh package instead of git [3490660](https://github.com/sagikimhi/socx-cil/commits/3490660e3e8b4e844451007a56d348c94d121f68)

- *(socx_plugins.git)* set pager flag default value to False [b453cc2](https://github.com/sagikimhi/socx-cil/commits/b453cc292d771f828a041e4ddd2521682a6f8888)

- *(socx_plugins.git)* make status tree formatting prettier [286e29c](https://github.com/sagikimhi/socx-cil/commits/286e29ce9b209746b3dd6c31581119aa6f60d1b3)

- *(socx_plugins.git)* improve error handling, adjust default settings [63cd90f](https://github.com/sagikimhi/socx-cil/commits/63cd90f3982ff799cfe4a2b63df8a4d832300014)

- *(socx_plugins.git)* rename manifest cmd, class and config to summary [0dd3176](https://github.com/sagikimhi/socx-cil/commits/0dd3176b5478f668d0c2c6068b2a59371db1dccd)

- *(socx_plugins.git.manifest)* move str to symbol conversion to code [e563195](https://github.com/sagikimhi/socx-cil/commits/e563195293fc1f070849d3d594681cef84eaeae2)

- *(socx_plugins.rgr)* cleanup regression settings and improve help text [33e3383](https://github.com/sagikimhi/socx-cil/commits/33e33838e408404afa936d108254aa39ab5f499a)

- *(socx_plugins.rgr)* wrap `regression.start` with asyncio task [707bc15](https://github.com/sagikimhi/socx-cil/commits/707bc15142c57af9307d22e019671b246e829bc0)

- *(socx_plugins.version)* display version using uv instead of pip [4ee39b3](https://github.com/sagikimhi/socx-cil/commits/4ee39b3d3efb74edb2884cb1140ad8fec787fc13)

- *(test)* raise exception if start is called on a running test [520fbd0](https://github.com/sagikimhi/socx-cil/commits/520fbd094b2e13736bc411b6dbbc64858a4a0c18)

- add settings.cli.context_settings config field [2416e2b](https://github.com/sagikimhi/socx-cil/commits/2416e2b69e68b512194fb2e3cbe76980f16f1cdd)

- simplify and improve plugin support and loading [bfa6d65](https://github.com/sagikimhi/socx-cil/commits/bfa6d65c128b1cfe2cbade121e392a9e51f5990d)

- [**breaking**] clean up and re organize code and structure [ab35344](https://github.com/sagikimhi/socx-cil/commits/ab353445e51bb5b95fc6fc069b4f593fcf1bd996)

- rename _uid to _meta and add singleton metaclass [d4c8a19](https://github.com/sagikimhi/socx-cil/commits/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90)

- remove nested sub packages [41cda37](https://github.com/sagikimhi/socx-cil/commits/41cda37905487be04c579e12ea7d5c6529c60114)

- rename package to socx (#5) [29bdf68](https://github.com/sagikimhi/socx-cil/commits/29bdf682f9e562c7370e6ab8f24eef010b1c07ab)


### 📚 Documentation

- *(README)* add old readme [4974d6b](https://github.com/sagikimhi/socx-cil/commits/4974d6b3a5c32fd1023dc22de02c88b181de5fee)

- *(README.md)* update README.md [6400289](https://github.com/sagikimhi/socx-cil/commits/6400289be3f48b88a207195a2a0ff7642cf67fd1)

- *(assets/svg)* update svg assets [5578381](https://github.com/sagikimhi/socx-cil/commits/5578381c57838454c646a037bc99bb66e4995f2e)

- *(cli.cfg)* correct docs of `GROUP_ARGUMENT_OPTIONS` [17807c8](https://github.com/sagikimhi/socx-cil/commits/17807c891d202849d4203428f6a01f7d927e2814)

- *(index.md)* update overview page (#115) [a741e3d](https://github.com/sagikimhi/socx-cil/commits/a741e3d03c44d6caeab9389c8450e2ad3629919f)

- *(index.md)* update overview page [320d1a9](https://github.com/sagikimhi/socx-cil/commits/320d1a99f927fe4958691e63922135efd44c63c7)

- *(socx.cli.cfg)* correct docs of `GROUP_ARGUMENT_OPTIONS` [9864f7b](https://github.com/sagikimhi/socx-cil/commits/9864f7bb3d841722a518774dc565d2f1bfef565b)

- move zensical.toml to config until feature parity [248db56](https://github.com/sagikimhi/socx-cil/commits/248db56eb39353d83842c50252ebd9b040537c6a)

- update documentation [1f8b46c](https://github.com/sagikimhi/socx-cil/commits/1f8b46c0aa91693902f7180a1b45041630b6be7e)

- transition from mkdocs to zensical [c859d1e](https://github.com/sagikimhi/socx-cil/commits/c859d1e11a2558e277f87a5308e9787be3f4abc2)

- update documentation (#97) [cd9a35d](https://github.com/sagikimhi/socx-cil/commits/cd9a35daad66ef5db27b145623b54f49b2820b56)

- update documentation [3410b17](https://github.com/sagikimhi/socx-cil/commits/3410b179d891535851f5ae3375ab9da5655e7981)

- update documentation [b805a30](https://github.com/sagikimhi/socx-cil/commits/b805a30edfc8fc34abfb3c56f541210e3ba69019)

- add a 'Core Concepts' section to the top navigation menu [7e45d2b](https://github.com/sagikimhi/socx-cil/commits/7e45d2bb8bbb87457a6123f26e28758cf0bc2814)

- add/update missing/outdated python docstrings (#71) [6fdba72](https://github.com/sagikimhi/socx-cil/commits/6fdba7202efce2ffa1d03d39886c5f7ebf311e99)

- update project documentation [7988e0c](https://github.com/sagikimhi/socx-cil/commits/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81)

- add/update missing/outdated python docstrings [7f6dee1](https://github.com/sagikimhi/socx-cil/commits/7f6dee149190eef4dbae2f801cf295c1f86d0afc)

- add missing mkdocs.yml [bd46cb0](https://github.com/sagikimhi/socx-cil/commits/bd46cb0410e6e57a98807feb9ed9b64e5d092576)

- configure and build documentation with mkdocs [325efb2](https://github.com/sagikimhi/socx-cil/commits/325efb2f5b0affc415d7d4a04af5deb70e9d0149)

- add CHANGELOG.md [218eabd](https://github.com/sagikimhi/socx-cil/commits/218eabd807070137d1b47bcd66936f39e26ed08e)

- update svg assets [0e54e76](https://github.com/sagikimhi/socx-cil/commits/0e54e76fefb8029b3642269fa4e59f2386ef61c3)


### ⚙️ Miscellaneous Tasks

- *(.env)* remove redundant comment lines [31766f7](https://github.com/sagikimhi/socx-cil/commits/31766f770cc8401855fa7ff92f5f854e8d176ef3)

- *(.env)* remove redundant comment lines [1abf1dc](https://github.com/sagikimhi/socx-cil/commits/1abf1dc09fb31ba0c9bb19f8d4a39d7a789d764a)

- *(.gitignore)* stop ignoring pre-commit config [f8f31ec](https://github.com/sagikimhi/socx-cil/commits/f8f31ec47b4809d536eb9e8e8de1bddf6e40c5ce)

- *(Makefile)* clean up unused variables [646d294](https://github.com/sagikimhi/socx-cil/commits/646d2947e6e01912ff4f4be0a7c50f4572ce85b2)

- *(Makefile)* explicitly specify python wheel path in `make publish` [b5b3044](https://github.com/sagikimhi/socx-cil/commits/b5b3044726f19081db396ded3fc67f4090214593)

- *(Makefile)* add changelog rule to generate CHANGELOG.md [b5ba650](https://github.com/sagikimhi/socx-cil/commits/b5ba650138f15753fcdf5b6ff3f6628ab9c4b5fc)

- *(cli)* move commands panel under options panel [2c1eb75](https://github.com/sagikimhi/socx-cil/commits/2c1eb7523b269616e885a841e4c62627af8090f7)

- *(cli)* clean up relative imports and add typing types [a241b73](https://github.com/sagikimhi/socx-cil/commits/a241b731d5f4b9d9d842a8b029136a56085b9883)

- *(cli)* remove unused help_option [c19d241](https://github.com/sagikimhi/socx-cil/commits/c19d241f14531879ec41cb563c985db56c885c6d)

- *(cli)* convert cli to a sub-package with multiple modules [a7daa39](https://github.com/sagikimhi/socx-cil/commits/a7daa392d23ee5e0d389f0509b26eca25050f780)

- *(cli)* adjust cli help text formatting [8b222bb](https://github.com/sagikimhi/socx-cil/commits/8b222bbe69578a02701cef1754916d95414212d7)

- *(cli/plugins)* add debug command to config plugin [f5b0ae9](https://github.com/sagikimhi/socx-cil/commits/f5b0ae92a45e841acefca6c133e9c7d1c2309d45)

- *(cli/plugins)* refactor rgr as script file instead of sub-pkg [7e643d5](https://github.com/sagikimhi/socx-cil/commits/7e643d5a07ef3fb89ba86ec58796e9492016da46)

- *(cli/plugins)* mv convert cmd to script file instaed of subpackage [7e12a74](https://github.com/sagikimhi/socx-cil/commits/7e12a74e63e71f4ceedb7858af96c40dbe5511f7)

- *(cliff.toml)* correct remote_url macro's url [e7484e4](https://github.com/sagikimhi/socx-cil/commits/e7484e41f1b0eced3804bb9f59d177faf165e421)

- *(config)* remove app version subdir from app directories [8f47c13](https://github.com/sagikimhi/socx-cil/commits/8f47c133449f31ef1dc6f8a4a49084d0fc181218)

- *(config)* enable load_dotenv and disable dotenv_override [6eebcf5](https://github.com/sagikimhi/socx-cil/commits/6eebcf55ce018ef9d47713eb9c542b643518470b)

- *(config)* add Dynaconf type annotation to settings [4c0aa52](https://github.com/sagikimhi/socx-cil/commits/4c0aa52ba3e1686d91e5b81f61c7761d26015b50)

- *(config.paths)* remove version from log path [6816bbe](https://github.com/sagikimhi/socx-cil/commits/6816bbe5831986ca8fedfd231baeafa30ef66270)

- *(core)* rename TypedPtrMixin to PtrMixin [7ed88ed](https://github.com/sagikimhi/socx-cil/commits/7ed88ed352a9c628176c4da8a29a0489a109e601)

- *(core)* export PtrMixin from mixins [5388209](https://github.com/sagikimhi/socx-cil/commits/5388209b3b2d1b8af079cdad8d13834f4f99e564)

- *(documentation)* add README.md [adc871f](https://github.com/sagikimhi/socx-cil/commits/adc871f0addc7f84e4761d623b449c90a744a460)

- *(format)* run ruff format [7819f42](https://github.com/sagikimhi/socx-cil/commits/7819f42153f90b06e9100712b2baab1c222c0122)

- *(gitignore)* remove non existent legacy paths [8a1fccd](https://github.com/sagikimhi/socx-cil/commits/8a1fccd5707c79570ac0c6324ae4f4b868dd4eed)

- *(log)* change default verbosity level [ac9afe5](https://github.com/sagikimhi/socx-cil/commits/ac9afe535cfd8a56b99e765338bf93c5fbd727ac)

- *(lsp)* add basedpyright config file [87b293b](https://github.com/sagikimhi/socx-cil/commits/87b293b2e89109046cb3cc0253a0765b26ad8b76)

- *(parser)* remove dead code [d213e05](https://github.com/sagikimhi/socx-cil/commits/d213e05e4e0fbad5c6b3599de46204b8b5ea620b)

- *(plugings/convert/converter)* organize imports [7d936fe](https://github.com/sagikimhi/socx-cil/commits/7d936fef8e6901e67b3a133c186617898aaea52f)

- *(plugins.yaml)* add 'enabled' field to all plugins [8fe1055](https://github.com/sagikimhi/socx-cil/commits/8fe10550a7ecdc89a80040decb2fc160cc04f3ee)

- *(plugins/convert/writer)* add logging, remove generic from base [9f9075d](https://github.com/sagikimhi/socx-cil/commits/9f9075d970484282445f03f5f2af801d0cafa777)

- *(plugins/git)* add manifest support for default_format setting [40a0e14](https://github.com/sagikimhi/socx-cil/commits/40a0e14e01ab01a3dfb490ea70904ec5a4bc380e)

- *(plugins/rgr)* rename functions to more appropriate names [585fe20](https://github.com/sagikimhi/socx-cil/commits/585fe20be8568132d0d9287a29df8cbfe94001f2)

- *(plugins/version)* add logging and make output prettier [cdde915](https://github.com/sagikimhi/socx-cil/commits/cdde915b554ab3d7d8684d5cc847e6ec9cd1f717)

- *(pre-commit)* update python version to 3.13 [1c8bd01](https://github.com/sagikimhi/socx-cil/commits/1c8bd01ddc78835e0170834eb64ddcb488712522)

- *(pre-commit)* update pre-commit config [86c8789](https://github.com/sagikimhi/socx-cil/commits/86c8789e17b6e84f8c360cceae65c38b51bfdaae)

- *(pre-commit)* update pre-commit config [6108920](https://github.com/sagikimhi/socx-cil/commits/61089206655258637cca8a2d29d22a59e38e1571)

- *(pyproject.toml)* organize and cleanup contents [0479b12](https://github.com/sagikimhi/socx-cil/commits/0479b12e6f237c909cf1b55505d58aacd2438ddd)

- *(pyproject.toml)* update pyproject.toml [3f9ea5b](https://github.com/sagikimhi/socx-cil/commits/3f9ea5b884c48cdeb4b7a985f24d233c691849f0)

- *(pyproject.toml)* update pyproject.toml [4198400](https://github.com/sagikimhi/socx-cil/commits/41984005ab252945a0a22057b8cde096421fe7ac)

- *(pyproject.toml)* adjust dev deps and tool configurations [4dc1a0a](https://github.com/sagikimhi/socx-cil/commits/4dc1a0ac3af58f217c3cbf7df13a95dcd78c9685)

- *(pyproject.toml)* add dependencies [ecabbb9](https://github.com/sagikimhi/socx-cil/commits/ecabbb93261be89c269437a9bb8691e7b39161ca)

- *(pyproject.toml)* add textual-autocomplete dependency [d1f9015](https://github.com/sagikimhi/socx-cil/commits/d1f901523d4c662de9eecc49f3445b3575f3d912)

- *(pyproject.toml)* update scripts and entry-points [a732c1a](https://github.com/sagikimhi/socx-cil/commits/a732c1a813ffd39331c1d52d9fbcf5f7476744e5)

- *(pyproject.toml)* cleanups and corrections [9ad9968](https://github.com/sagikimhi/socx-cil/commits/9ad9968284633fb6d7f24979b5834581b0a3c9c6)

- *(pyproject.toml)* add pre-commit dependency to dev group [117ecac](https://github.com/sagikimhi/socx-cil/commits/117ecac3de5b001b2f61363ab31964531791b784)

- *(pyproject.toml,uv.lock)* update deps [a14498f](https://github.com/sagikimhi/socx-cil/commits/a14498f286c0eef9c014b79df55df834d6e1dfe3)

- *(regression)* improve output smoothness, scheduler and runner timings [ef8ba51](https://github.com/sagikimhi/socx-cil/commits/ef8ba5115fc4d50e716340dbdf67ac66b3136cad)

- *(regression)* remove unused imports [9c74a40](https://github.com/sagikimhi/socx-cil/commits/9c74a401a42bbdbf52956ef564309fc9d9d5eeb3)

- *(regression)* fine tune configurations [ae90412](https://github.com/sagikimhi/socx-cil/commits/ae904125988f6b368c75c4d612cdcbf88d36d461)

- *(regression)* rename Status,Command to TestStatus,TestCommand [ce4792a](https://github.com/sagikimhi/socx-cil/commits/ce4792aa138c9b0d0e888bf23c1e0f93c73862db)

- *(regression.toml)* add max_parallel_runs configuration [11098b0](https://github.com/sagikimhi/socx-cil/commits/11098b07079f21cbfaf9c621972c6b565b099c3c)

- *(settings)* delete unused toml configuration files [e212c76](https://github.com/sagikimhi/socx-cil/commits/e212c76a6ffaf88b2331f5a382fd5662ac274752)

- *(settings)* reorganize settings load order [10cf095](https://github.com/sagikimhi/socx-cil/commits/10cf095f0bbd82af8ea1a943efa396ab63ddc5b2)

- *(settings/git)* adjust column names [2989be4](https://github.com/sagikimhi/socx-cil/commits/2989be47520f9213956e63ae7731bcd796357d9b)

- *(socx)* remove some internal exports [4bdd47f](https://github.com/sagikimhi/socx-cil/commits/4bdd47fcf27aeb08c0f5653ff6bf3ef6e374b8eb)

- *(socx.config.paths)* remove version from log path [6268445](https://github.com/sagikimhi/socx-cil/commits/6268445ed505822d0b71625cfa2971a141139e67)

- *(test)* add empty constructor and 'escaped' member to TestCommand [7d55644](https://github.com/sagikimhi/socx-cil/commits/7d55644910ca850334649a81c1468c43d3a15607)

- *(tui)* add hoptex to project dependencies [e31e828](https://github.com/sagikimhi/socx-cil/commits/e31e828a6f3c7d98c52da51c5d0d628b1a7e243d)

- *(uv)* remove and ignore uv.lock [ae798fd](https://github.com/sagikimhi/socx-cil/commits/ae798fdd07aba31487ebe906519b2d63145a2466)

- *(uv)* update uv.lock [bb8d095](https://github.com/sagikimhi/socx-cil/commits/bb8d095763c3719e9747d5b0698f28acf68fc61a)

- *(uv.lock)* update lockfile [5093fe2](https://github.com/sagikimhi/socx-cil/commits/5093fe2fc6100efee3a3ae422fe01bbb5dd8f6e3)

- *(uv.lock)* update lock file [e68727e](https://github.com/sagikimhi/socx-cil/commits/e68727ec50797168dfa52ebfb80a4e8660b78584)

- *(version)* bump version to 0.4.4.dev1 [8f071f5](https://github.com/sagikimhi/socx-cil/commits/8f071f5f47778c6e245585d340851c17ac9e3cac)

- *(visitor)* sort exports [bb376e2](https://github.com/sagikimhi/socx-cil/commits/bb376e216f8a183855dabb123e738b84c522c648)

- prepare release 0.7.0 [147e48d](https://github.com/sagikimhi/socx-cil/commits/147e48d807725f4463ed45cbcd1aa85f49724d4f)

- prepare release 0.6.0 [1b79590](https://github.com/sagikimhi/socx-cil/commits/1b795902e558815c6e2fb75ada7e9438ccc4c2a4)

- prepare release 0.5.9 (#102) [753639a](https://github.com/sagikimhi/socx-cil/commits/753639a804671aab74eb13c6a81e337716a154cb)

- prepare release 0.5.9 [40480c6](https://github.com/sagikimhi/socx-cil/commits/40480c6376864d2d6b5ff2369331f62966b5c067)

- prepare for release 0.5.8 [263c708](https://github.com/sagikimhi/socx-cil/commits/263c70871db588030041222c8105399a9e910ccb)

- prepare release 0.5.7 [9aadefd](https://github.com/sagikimhi/socx-cil/commits/9aadefd64ae155ae77aac8a120daec12e0bb900d)

- prepare release 0.5.5 [6555978](https://github.com/sagikimhi/socx-cil/commits/6555978b0a304009d2e8f99f7f7d495a14a6373b)

- update pyproject metadata [88ce3ea](https://github.com/sagikimhi/socx-cil/commits/88ce3eadd6568bcda877767f00a0a69d34a7085e)

- update changelog [5c2e48a](https://github.com/sagikimhi/socx-cil/commits/5c2e48aa2aaeab2b32a502fea06ee5790c62ebf3)

- apply `ruff check` auto fixes [29eccd0](https://github.com/sagikimhi/socx-cil/commits/29eccd074af4a0e84eabebe3c790180024163ab5)

- update issue templates [fe7b988](https://github.com/sagikimhi/socx-cil/commits/fe7b9888d03160c507b3abed2024c5ddda9b1c05)

- prepare release 0.5.4 [cf6446f](https://github.com/sagikimhi/socx-cil/commits/cf6446f3b22494970bc22060b9905eab45384524)

- prepare release 0.5.3 [17df8d0](https://github.com/sagikimhi/socx-cil/commits/17df8d0f7bc7f93f29e4f039793a618cf3b85724)

- prepare release 0.5.2 [4aaaddc](https://github.com/sagikimhi/socx-cil/commits/4aaaddcc931fdfd32c1ee29620916729b34eac68)

- add mypy dev dependency and enable 'check_types' duty [d6e1cba](https://github.com/sagikimhi/socx-cil/commits/d6e1cba13cd71da7fa8b17b41c3ca01a8c8bacb5)

- prepare release 0.5.1 [c5365c0](https://github.com/sagikimhi/socx-cil/commits/c5365c0ab09f6bd9b0d0a082ff9de081b0349820)

- fix duties.py release flow [5637b47](https://github.com/sagikimhi/socx-cil/commits/5637b4776d16fff842153325eb668ba22f1de57f)

- update changelog version to 0.5.0 [959970d](https://github.com/sagikimhi/socx-cil/commits/959970df083ebf2b7c0d92b58f223bfa2bed7e99)

- prepare release 0.5.0 [785773c](https://github.com/sagikimhi/socx-cil/commits/785773c304478f76d095fe96cb2c85e4d0a80655)

- update changelog [1bfbfa5](https://github.com/sagikimhi/socx-cil/commits/1bfbfa53b114dc708fffc1e3c45e5c3a2ff20c9e)

- add binary build target, remove 'socx_patches' [2aa1a26](https://github.com/sagikimhi/socx-cil/commits/2aa1a26d17a0eb68acf3baf4742b67c42f455814)

- remove old svg assets [116c6d7](https://github.com/sagikimhi/socx-cil/commits/116c6d78ccce223a16c1ed072643be9129aea1ba)

- add help rule to Makefile [fad8847](https://github.com/sagikimhi/socx-cil/commits/fad8847b802afbb6ca6679facd1c37c53752a1ed)

- add cliff.toml config for git-cliff [8aeda97](https://github.com/sagikimhi/socx-cil/commits/8aeda97380ade462bd35c355885b68b49f5c7233)

- remove double settings reference [ac67dec](https://github.com/sagikimhi/socx-cil/commits/ac67dec5c2b68af506118a03f8abd0518d206f04)

- bump version to 0.4.3 [e3393c5](https://github.com/sagikimhi/socx-cil/commits/e3393c5025076df66656c596822da84e6e633031)

- update uv.lock [0e37705](https://github.com/sagikimhi/socx-cil/commits/0e37705243eab3788de658781d0282028b578d14)

- minor meaningless yaml format correction in settings.yaml [c896ac1](https://github.com/sagikimhi/socx-cil/commits/c896ac1c90b93c02b34c4c91c847945109e85b0d)

- update uv.lock and pyproject dependencies [78f6a48](https://github.com/sagikimhi/socx-cil/commits/78f6a486c43fa7af8cae3a339af2da1885639c10)

- update .gitignore [d4ae578](https://github.com/sagikimhi/socx-cil/commits/d4ae57817d8cf3efc0a2bafbc3307b6aff35122d)

- update uv.lock [e6ba00f](https://github.com/sagikimhi/socx-cil/commits/e6ba00f148914696e3d39ac23f1d7c8971b9e5f7)

- update dependencies and uv lock file [81b57c7](https://github.com/sagikimhi/socx-cil/commits/81b57c79d94e8bc7f33e545128a113bf0eb0ee37)

- update uv.lock [b14b09a](https://github.com/sagikimhi/socx-cil/commits/b14b09ab79e4531fef1fe4bd3bb35fc5f7f08745)

- remove double settings reference [d322cb6](https://github.com/sagikimhi/socx-cil/commits/d322cb61c311d3179ab387e7fd0f9a74bd29ab9d)

- add basedpyright config file [d697d9c](https://github.com/sagikimhi/socx-cil/commits/d697d9cb93165e8fc12e2aaf4420d87c809f326b)

- update uv.lock [983c4f4](https://github.com/sagikimhi/socx-cil/commits/983c4f49f510406febdf28aa8023f2d0a1623524)

- add dummy socrun script [85ef118](https://github.com/sagikimhi/socx-cil/commits/85ef1181f081d76755355b0aab0a91c1a6760860)

- fix 'config get' plugin docs, update dependencies [9708a66](https://github.com/sagikimhi/socx-cil/commits/9708a66b5f4ce7cb4cebf5c00e4d6f2d8496fdaa)

- update mypy settings, fix ruff lint errors [fae79e8](https://github.com/sagikimhi/socx-cil/commits/fae79e8e671fed95a12e20f3fc7cd5c37616a898)

- format with `ruff format` and fix `ruff check` errors [028d689](https://github.com/sagikimhi/socx-cil/commits/028d68971e4fc30fbe7adf6a346e1ead93562c5e)

- format files with ruff [d59869b](https://github.com/sagikimhi/socx-cil/commits/d59869ba2c8dad3d0871f530666bb64e2c3312e9)

- restore .env testing env variables [15ffe8b](https://github.com/sagikimhi/socx-cil/commits/15ffe8b3735a36169aa3037027f7a8007eb2e346)

- add feature request and bug report templates (#32) [0ee31b0](https://github.com/sagikimhi/socx-cil/commits/0ee31b06b14e38eb49900af53779d404d26b44bb)

- correct cli->rgr->rrfh options metavars [77843dc](https://github.com/sagikimhi/socx-cil/commits/77843dc12bf7050941d3924eb341464c72e11250)

- export RichGroup and RichCommand defined in cli.py [a16c8b8](https://github.com/sagikimhi/socx-cil/commits/a16c8b8dc964a5b772ad37d5fed78ff922170c58)

- remove unused test.toml config [66be11b](https://github.com/sagikimhi/socx-cil/commits/66be11bc533f307a2bbff07e5e8e7ca0d01627ab)

- add numpy and psutil dependencies [3ed51e6](https://github.com/sagikimhi/socx-cil/commits/3ed51e6f7cff5211ce6a738df741a0b8d5e4df76)

- rename plugins to socx_plugins [4a59605](https://github.com/sagikimhi/socx-cil/commits/4a59605a14de9cf29b3b210a8ee2301b378b009e)

<!-- generated by git-cliff -->
