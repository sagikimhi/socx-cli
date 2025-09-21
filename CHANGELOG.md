
## [0.5.0]


### ⛰️  Features

- *(Makefile)* add Makefile to automate development tasks [6447162](https://bitbucket.org/wiliot/socenv/commits/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9)

- *(cli)* add --version flag for printing version info [02d9480](https://bitbucket.org/wiliot/socenv/commits/02d9480436e38d87ac0f6577c7efcc295a3881d8)

- *(cli)* add callbacks to ease handling of options and arguments [70bd332](https://bitbucket.org/wiliot/socenv/commits/70bd332e501ba2a1b1e1dad524a80220d242a161)

- *(cli/plugins)* add env subcommand and plugin [bf109dd](https://bitbucket.org/wiliot/socenv/commits/bf109ddba85072771e26c860387367491e714b99)

- *(console)* use and reconfigure global console [09baf1a](https://bitbucket.org/wiliot/socenv/commits/09baf1ac414e1bc29850656d604c23345a0b3954)

- *(console)* install pretty tracebacks on console [d65333a](https://bitbucket.org/wiliot/socenv/commits/d65333a6dc39d3c518472db4e60c3934694af8fa)

- *(decorators)* add option to pass verbosity level arg to log_it [e9bf43b](https://bitbucket.org/wiliot/socenv/commits/e9bf43bed1243f31f2d505c0c1632ca0e6227370)

- *(options)* [**breaking**] add global options, option groups, and callbacks [73f0583](https://bitbucket.org/wiliot/socenv/commits/73f058334a81f8ff40809891ea16aa464fe07cc2)

- *(plugin)* add plug command group for handling plugins (#54) [42ade7a](https://bitbucket.org/wiliot/socenv/commits/42ade7af08f61ba1473bb60c9112baad9dc02604)

- *(plugin)* add plug command group for handling plugins [c11dc1b](https://bitbucket.org/wiliot/socenv/commits/c11dc1bd653a87c9abd36e0d4444eadf1583b095)

- *(regression)* add regression rerun support to cli (#22) [8d5573f](https://bitbucket.org/wiliot/socenv/commits/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2)

- *(regression)* fix program not ending, log pass/fail at exit (#20) [2f869b3](https://bitbucket.org/wiliot/socenv/commits/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a)

- *(regression)* add async support to test and regression. [0a723d0](https://bitbucket.org/wiliot/socenv/commits/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a)

- *(regression)* add RegressionStatus enum [fd45eb2](https://bitbucket.org/wiliot/socenv/commits/fd45eb2d0ff9532419c7e74e76fc79f901277b21)

- *(rgr)* add tui command, change 'rrfh' command name to 'run' [9b610d4](https://bitbucket.org/wiliot/socenv/commits/9b610d4203f462c12a059cb4fe0b6f091b2c91a7)

- *(rich-click)* add rich click help menu for sub-commands (#23) [3ef833c](https://bitbucket.org/wiliot/socenv/commits/3ef833cee29307822ebc29d548f9f25291944065)

- *(rich-click)* add rich click help menu for sub-commands [92a4b80](https://bitbucket.org/wiliot/socenv/commits/92a4b80b4af6789935223db9cc2ad73c504d0e63)

- *(socx.config.serializers)* add object serialization module [c8e7592](https://bitbucket.org/wiliot/socenv/commits/c8e759282bd3ed27c253a28a7e9f841825c19f87)

- *(socx_plugins.converters)* add @command converter [bfc1c62](https://bitbucket.org/wiliot/socenv/commits/bfc1c620419543b663db8fbd795fab08484ea480)

- *(socx_plugins.git)* add ahead-behind status column to manifest [754c819](https://bitbucket.org/wiliot/socenv/commits/754c819895a3fa3398d088ae24688dedc2be8a21)

- *(socx_plugins.rgr)* handle arguments with callbacks [666c43e](https://bitbucket.org/wiliot/socenv/commits/666c43e1cf6bccb065344a4bf3c6fe15ed157dc1)

- *(test)* add base test class and asyncio support [74bbe8f](https://bitbucket.org/wiliot/socenv/commits/74bbe8fd909457e7b8ee671a172ede958ea36fd7)

- *(tui)* wip developing ui [f8a11b1](https://bitbucket.org/wiliot/socenv/commits/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a)

- *(tui)* add vim-like movement bind modes [13142ee](https://bitbucket.org/wiliot/socenv/commits/13142eebb58c37a233de573c1502ce0c4235da08)

- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) [a9d65aa](https://bitbucket.org/wiliot/socenv/commits/a9d65aab9323a48f7879c41f0ffdb66c9b320294)


### 🐛 Bug Fixes

- *(.env)* correct dotenv development env variables [bfe012e](https://bitbucket.org/wiliot/socenv/commits/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373)

- *(Makefile)* fix incorrect flags in `make publish` rule [b35f0bf](https://bitbucket.org/wiliot/socenv/commits/b35f0bfa9bca327858dd2074e89c5ce8d2182552)

- *(Makefile)* fix `make clean` rules [ab17ac2](https://bitbucket.org/wiliot/socenv/commits/ab17ac21cf22269760af8a2a4b0d990968a1bc16)

- *(_CmdLine)* fix _CmdLine inheritence [0126aef](https://bitbucket.org/wiliot/socenv/commits/0126aef8692abe3a638866254e42482bf0de48da)

- *(cli)* fix CLI after breaking changes of rich-click 1.9.0 [d2e9816](https://bitbucket.org/wiliot/socenv/commits/d2e98160402d4af35a53f417ab393c288d7646d8)

- *(cli)* fix tui decorator type annotation [a1b194f](https://bitbucket.org/wiliot/socenv/commits/a1b194f16b01f37538d53d3ffe3348ce46257a1c)

- *(cli)* fix type hints of tui decorator [f27d96e](https://bitbucket.org/wiliot/socenv/commits/f27d96e49b57dff1425bf43fa77045be7ed9f86d)

- *(cli)* add missing rich click dependency [48b4161](https://bitbucket.org/wiliot/socenv/commits/48b4161244681eeccca9145110e2d03c22fed0c9)

- *(cli)* add return code on exit from main [8f3eb61](https://bitbucket.org/wiliot/socenv/commits/8f3eb6147e3f70589168609460cb543d7a92d7c9)

- *(cli/callbacks)* fix option callbacks [2dfa959](https://bitbucket.org/wiliot/socenv/commits/2dfa959a4cd0c962dab1de1f7d07cd91405c020e)

- *(config.converters)* fix @command help texts [8ece5cb](https://bitbucket.org/wiliot/socenv/commits/8ece5cb4f3850b917059a7ab230665b3835ffbf1)

- *(config/metadata)* use __spec__.name instead of __package__ [9d27ca6](https://bitbucket.org/wiliot/socenv/commits/9d27ca628c98720a02b44e3873edd499eef63ee7)

- *(decorators)* log_it now logs to global socx.log run log [c18e495](https://bitbucket.org/wiliot/socenv/commits/c18e495d892b2770fcd4d9c751b5342e2d0958cd)

- *(dotenv)* correct dotenv configs [54f8cf5](https://bitbucket.org/wiliot/socenv/commits/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548)

- *(io)* fix mypy errors in log.py [5bb8e06](https://bitbucket.org/wiliot/socenv/commits/5bb8e06bd3af45240f8d3f19aa427a084ad4f197)

- *(io)* fix mypy errors in decorators.py [5fdecd5](https://bitbucket.org/wiliot/socenv/commits/5fdecd5e12893d03961c942200f6089854a4592e)

- *(io.decorators)* fix typing [9e7881f](https://bitbucket.org/wiliot/socenv/commits/9e7881f61f01915165c0373520051cd85c568138)

- *(log)* fix debug logging to socx.log when debug mode is enabled [6a14191](https://bitbucket.org/wiliot/socenv/commits/6a1419191bb654c88aaa494d7572d8e0613f1523)

- *(plugin/git)* fix ref and json formatted manifests [dcc992c](https://bitbucket.org/wiliot/socenv/commits/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b)

- *(plugins/convert/reader)* remove relative import and fix typing [6dd9ce0](https://bitbucket.org/wiliot/socenv/commits/6dd9ce07070bd8a9c0779f83e16a0252142684cf)

- *(plugins/git)* fix missing column names in json manifest [cc7f746](https://bitbucket.org/wiliot/socenv/commits/cc7f746fb98727ef5b110116217ed2a6595b0757)

- *(plugins/git)* fix inconsistent revision hash length in manifest [b5f0d88](https://bitbucket.org/wiliot/socenv/commits/b5f0d88789287a9a289fbc20e66fa220d915b08c)

- *(plugins/rgr)* fix failed and passed test file formatting [06cb7e5](https://bitbucket.org/wiliot/socenv/commits/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf)

- *(plugins/rgr)* fix mypy errors in _rgr.py [061625d](https://bitbucket.org/wiliot/socenv/commits/061625d1ab5c03609b00b92f3a3cefc9b7a42766)

- *(plugins/tui, pre-commit)* fix broken terminal ui, set up pre-commit [bd60074](https://bitbucket.org/wiliot/socenv/commits/bd600741c34a4c009d4cbe72b6567c95013ba3da)

- *(regression)* fix broken rgr command due to mypy fixes [a5ac756](https://bitbucket.org/wiliot/socenv/commits/a5ac7566be05acd5e683b689d2c7392c1d2e28e4)

- *(regression)* fix mypy errors in regression subpackage [3626bed](https://bitbucket.org/wiliot/socenv/commits/3626beddedb914f370a9d920dbaf2bb91aefdd21)

- *(regression)* replace print with log in meth 'start', add missing await (#24) [8133742](https://bitbucket.org/wiliot/socenv/commits/81337423de743af0d67af43b2457e3f7c3ecb1b8)

- *(regression)* correct default gateway configurations (#21) [1b3bf5d](https://bitbucket.org/wiliot/socenv/commits/1b3bf5d088b7f19ec94947d636b161c15cea0d06)

- *(regression)* fix issue ignoring limit causing all cmds to be ran [eddd01f](https://bitbucket.org/wiliot/socenv/commits/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76)

- *(regression, plugins/rgr)* fix mypy typing errors [ceb0dbf](https://bitbucket.org/wiliot/socenv/commits/ceb0dbfdff2ad645940a435f06803f33b87921a1)

- *(regression.yaml)* fix default path value [5b20254](https://bitbucket.org/wiliot/socenv/commits/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf)

- *(ruff-check)* fix linter errors [8207c63](https://bitbucket.org/wiliot/socenv/commits/8207c6342287279f97909eec94c3b79382debd59)

- *(settings)* fix issue with reconfigure not overriding old values [1375123](https://bitbucket.org/wiliot/socenv/commits/137512363db8f12c2ed1b74f509ae5b9e956c947)

- *(settings/rgr)* fix incorrect assets path setting [7719ecf](https://bitbucket.org/wiliot/socenv/commits/7719ecf97bbe223e0076745f268836819a6b3ba3)

- *(socx.cli)* only load `click.Command` subclasses as plugins [7426e54](https://bitbucket.org/wiliot/socenv/commits/7426e54b3610c45d21eba71fc5ee7e524a756dfc)

- *(socx.cli)* fix tui decorator type annotation [3e30a0f](https://bitbucket.org/wiliot/socenv/commits/3e30a0f57300d4828b7bfd0958e534238ba47d14)

- *(socx.cli._cli)* fix _CmdLine inheritence [554c5b8](https://bitbucket.org/wiliot/socenv/commits/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb)

- *(socx.config)* fix configuration overriding and loading order [e57ef5b](https://bitbucket.org/wiliot/socenv/commits/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d)

- *(socx.config._config)* fix incorrect settings_file argument [f6cd1ff](https://bitbucket.org/wiliot/socenv/commits/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce)

- *(socx.config.metadata)* fix exception due to missing __spec__ [8ed76e5](https://bitbucket.org/wiliot/socenv/commits/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30)

- *(socx.io)* fix missing `log` export [f9589bf](https://bitbucket.org/wiliot/socenv/commits/f9589bfe924fb627c0d023b6e202459d8c6ef55c)

- *(socx.io.decorators)* fix typing [a7bc0e1](https://bitbucket.org/wiliot/socenv/commits/a7bc0e1e928aa910843c1370081e23f40dd7fad1)

- *(socx.io.log)* set up 'socx' logger instead of root logger [62473f8](https://bitbucket.org/wiliot/socenv/commits/62473f82fdecde2e0771b4b71c59bb159e4c1883)

- *(socx.regression.regression)* set start and finish times [9c0b64c](https://bitbucket.org/wiliot/socenv/commits/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e)

- *(socx_plugins.config.edit)* fix edit command [7133779](https://bitbucket.org/wiliot/socenv/commits/71337798f37918f47c720840c4e3231bda1708eb)

- *(socx_plugins.git)* fix some typing issues in manifest, utils [b72a44a](https://bitbucket.org/wiliot/socenv/commits/b72a44a0a08e15c486e131689cc418ca1e3329f6)

- *(socx_plugins.git)* minor typing fixes in git manifest plugin [64acf03](https://bitbucket.org/wiliot/socenv/commits/64acf03864dd9be029f3956967e2c710ad4de786)

- *(socx_plugins.rgr.pixie_test)* correct path to test's log file [f525fa5](https://bitbucket.org/wiliot/socenv/commits/f525fa568cb4cb37195bb0c080dc9395c9680817)

- *(socx_plugins.version)* fix version command [b8fba3a](https://bitbucket.org/wiliot/socenv/commits/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a)

- *(socx_tui)* fix AttributeError when loading regression from file [4dcda47](https://bitbucket.org/wiliot/socenv/commits/4dcda47e23fa775885fd1468357dbaaa36a28305)

- *(tui)* fix mypy typing errors, discard Vim implementation [24737e3](https://bitbucket.org/wiliot/socenv/commits/24737e336505d271d7c60008c3e154adf2d4d316)

- *(tui)* fix mypy errors [73ddf0f](https://bitbucket.org/wiliot/socenv/commits/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404)

- *(visitor)* fix type hints and implementation of traversals [105220b](https://bitbucket.org/wiliot/socenv/commits/105220bedca8859aff323410858c624e5bc25092)

- *(visitor)* add empty __slots__ to protocol classes [356fdcd](https://bitbucket.org/wiliot/socenv/commits/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e)

- fix all mypy errors [dd80f31](https://bitbucket.org/wiliot/socenv/commits/dd80f31155efff34ca9451e3147bfcf6dd4bf50c)

- correct warea to WAREA [155ae59](https://bitbucket.org/wiliot/socenv/commits/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a)

- add misssing socx_patches package [a2a20d8](https://bitbucket.org/wiliot/socenv/commits/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6)

- add missing log module exports [78e001e](https://bitbucket.org/wiliot/socenv/commits/78e001e6d066fe627797d6a2f513f2ba0bddfc9a)


### 🚜 Refactor

- *(Makefile)* add changelog generation variables [6a9887a](https://bitbucket.org/wiliot/socenv/commits/6a9887a14786914bacc69a99e0994b0cb6b5004c)

- *(Makefile)* use `$(UV)` instead of `uv` in export_svg [893daa8](https://bitbucket.org/wiliot/socenv/commits/893daa82215e0a567ed253ce6e95e5ca73dfb821)

- *(cli.cfg)* adjust default configurations [ddc414b](https://bitbucket.org/wiliot/socenv/commits/ddc414b855d38778344bf3d096844dafc69d743e)

- *(cli.cfg)* remove unused `cfg` function [062f6ee](https://bitbucket.org/wiliot/socenv/commits/062f6eebabf0cbccdad07715bf321cea5a6e2f64)

- *(config._config)* pass logger to `log_it` decorator [dc86e0c](https://bitbucket.org/wiliot/socenv/commits/dc86e0ca6b2f2d49a2834964a5aba07797ee298e)

- *(config.converters)* improve error handling [09fbe8f](https://bitbucket.org/wiliot/socenv/commits/09fbe8fbc25f03f4994557bd01cb88f01a24112f)

- *(io.decorators)* add optional logger parameter [eecef55](https://bitbucket.org/wiliot/socenv/commits/eecef55c588f85ec21e83f6a8f847c83b9eccfba)

- *(log)* rename level to get_level, export get_logger [0b0f41c](https://bitbucket.org/wiliot/socenv/commits/0b0f41cfca7792f503adb12ece74193d11bcccc6)

- *(mixins)* move mixins into patterns subpackage [b620400](https://bitbucket.org/wiliot/socenv/commits/b620400a7da2066e45bb0f30c2e8d8536ece091c)

- *(plugins)* [**breaking**] rename env cmd to git and rewrite as package [464f183](https://bitbucket.org/wiliot/socenv/commits/464f1830450ea722835034e2fdf948cd009885de)

- *(plugins/env)* cleanup env code and add debug logging [d15e5f1](https://bitbucket.org/wiliot/socenv/commits/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075)

- *(settings)* rewrite settings.toml and plugins.toml as yaml [68dc3ad](https://bitbucket.org/wiliot/socenv/commits/68dc3adc6a32885eaf31838355dca1c568019f78)

- *(socx.cli.cfg)* adjust default configurations [486442f](https://bitbucket.org/wiliot/socenv/commits/486442f17e1c24d1cf16ae1cab73b46744070d7a)

- *(socx.cli.cfg)* remove unused `cfg` function [b0e0a04](https://bitbucket.org/wiliot/socenv/commits/b0e0a049c26adfd2b170549933d50d2da2fbe1cf)

- *(socx.config._config)* pass logger to `log_it` decorator [e3a5e30](https://bitbucket.org/wiliot/socenv/commits/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c)

- *(socx.config.converters)* improve exception handling [8c72a77](https://bitbucket.org/wiliot/socenv/commits/8c72a77fe2a18dbd93b152be50373a0c0a422c66)

- *(socx.config.converters)* use universal_pathlib [701015d](https://bitbucket.org/wiliot/socenv/commits/701015dfcc2132e87ca6a2d8444740cb24f3359b)

- *(socx.config.paths)* use upath.UPath instead of pathlib.Path [a60c8fa](https://bitbucket.org/wiliot/socenv/commits/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be)

- *(socx.config.paths)* add APP_ROOT_DIR to paths module [003cb48](https://bitbucket.org/wiliot/socenv/commits/003cb48e7bf6b622e86c132630eabbb8dfe2c07e)

- *(socx.io.decorators)* add optional logger parameter [fa69f79](https://bitbucket.org/wiliot/socenv/commits/fa69f7938023e64b66ed548d459302885bfae7e0)

- *(socx_plugins.git.manifest)* move str to symbol conversion to code [e563195](https://bitbucket.org/wiliot/socenv/commits/e563195293fc1f070849d3d594681cef84eaeae2)

- *(socx_plugins.rgr)* wrap `regression.start` with asyncio task [707bc15](https://bitbucket.org/wiliot/socenv/commits/707bc15142c57af9307d22e019671b246e829bc0)

- *(test)* raise exception if start is called on a running test [520fbd0](https://bitbucket.org/wiliot/socenv/commits/520fbd094b2e13736bc411b6dbbc64858a4a0c18)

- simplify and improve plugin support and loading [bfa6d65](https://bitbucket.org/wiliot/socenv/commits/bfa6d65c128b1cfe2cbade121e392a9e51f5990d)

- [**breaking**] clean up and re organize code and structure [ab35344](https://bitbucket.org/wiliot/socenv/commits/ab353445e51bb5b95fc6fc069b4f593fcf1bd996)

- rename _uid to _meta and add singleton metaclass [d4c8a19](https://bitbucket.org/wiliot/socenv/commits/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90)

- remove nested sub packages [41cda37](https://bitbucket.org/wiliot/socenv/commits/41cda37905487be04c579e12ea7d5c6529c60114)

- rename package to socx (#5) [29bdf68](https://bitbucket.org/wiliot/socenv/commits/29bdf682f9e562c7370e6ab8f24eef010b1c07ab)


### 📚 Documentation

- *(README)* add old readme [4974d6b](https://bitbucket.org/wiliot/socenv/commits/4974d6b3a5c32fd1023dc22de02c88b181de5fee)

- *(README.md)* update README.md [6400289](https://bitbucket.org/wiliot/socenv/commits/6400289be3f48b88a207195a2a0ff7642cf67fd1)

- *(assets/svg)* update svg assets [5578381](https://bitbucket.org/wiliot/socenv/commits/5578381c57838454c646a037bc99bb66e4995f2e)

- *(cli.cfg)* correct docs of `GROUP_ARGUMENT_OPTIONS` [17807c8](https://bitbucket.org/wiliot/socenv/commits/17807c891d202849d4203428f6a01f7d927e2814)

- *(socx.cli.cfg)* correct docs of `GROUP_ARGUMENT_OPTIONS` [9864f7b](https://bitbucket.org/wiliot/socenv/commits/9864f7bb3d841722a518774dc565d2f1bfef565b)

- configure and build documentation with mkdocs [325efb2](https://bitbucket.org/wiliot/socenv/commits/325efb2f5b0affc415d7d4a04af5deb70e9d0149)

- add CHANGELOG.md [218eabd](https://bitbucket.org/wiliot/socenv/commits/218eabd807070137d1b47bcd66936f39e26ed08e)

- update svg assets [0e54e76](https://bitbucket.org/wiliot/socenv/commits/0e54e76fefb8029b3642269fa4e59f2386ef61c3)


### ⚙️ Miscellaneous Tasks

- *(.env)* remove redundant comment lines [31766f7](https://bitbucket.org/wiliot/socenv/commits/31766f770cc8401855fa7ff92f5f854e8d176ef3)

- *(.env)* remove redundant comment lines [1abf1dc](https://bitbucket.org/wiliot/socenv/commits/1abf1dc09fb31ba0c9bb19f8d4a39d7a789d764a)

- *(Makefile)* add changelog rule to generate CHANGELOG.md [b5ba650](https://bitbucket.org/wiliot/socenv/commits/b5ba650138f15753fcdf5b6ff3f6628ab9c4b5fc)

- *(cli)* clean up relative imports and add typing types [a241b73](https://bitbucket.org/wiliot/socenv/commits/a241b731d5f4b9d9d842a8b029136a56085b9883)

- *(cli)* remove unused help_option [c19d241](https://bitbucket.org/wiliot/socenv/commits/c19d241f14531879ec41cb563c985db56c885c6d)

- *(cli)* convert cli to a sub-package with multiple modules [a7daa39](https://bitbucket.org/wiliot/socenv/commits/a7daa392d23ee5e0d389f0509b26eca25050f780)

- *(cli)* adjust cli help text formatting [8b222bb](https://bitbucket.org/wiliot/socenv/commits/8b222bbe69578a02701cef1754916d95414212d7)

- *(cli/plugins)* add debug command to config plugin [f5b0ae9](https://bitbucket.org/wiliot/socenv/commits/f5b0ae92a45e841acefca6c133e9c7d1c2309d45)

- *(cli/plugins)* refactor rgr as script file instead of sub-pkg [7e643d5](https://bitbucket.org/wiliot/socenv/commits/7e643d5a07ef3fb89ba86ec58796e9492016da46)

- *(cli/plugins)* mv convert cmd to script file instaed of subpackage [7e12a74](https://bitbucket.org/wiliot/socenv/commits/7e12a74e63e71f4ceedb7858af96c40dbe5511f7)

- *(config)* remove app version subdir from app directories [8f47c13](https://bitbucket.org/wiliot/socenv/commits/8f47c133449f31ef1dc6f8a4a49084d0fc181218)

- *(config)* enable load_dotenv and disable dotenv_override [6eebcf5](https://bitbucket.org/wiliot/socenv/commits/6eebcf55ce018ef9d47713eb9c542b643518470b)

- *(config)* add Dynaconf type annotation to settings [4c0aa52](https://bitbucket.org/wiliot/socenv/commits/4c0aa52ba3e1686d91e5b81f61c7761d26015b50)

- *(config.paths)* remove version from log path [6816bbe](https://bitbucket.org/wiliot/socenv/commits/6816bbe5831986ca8fedfd231baeafa30ef66270)

- *(core)* rename TypedPtrMixin to PtrMixin [7ed88ed](https://bitbucket.org/wiliot/socenv/commits/7ed88ed352a9c628176c4da8a29a0489a109e601)

- *(core)* export PtrMixin from mixins [5388209](https://bitbucket.org/wiliot/socenv/commits/5388209b3b2d1b8af079cdad8d13834f4f99e564)

- *(documentation)* add README.md [adc871f](https://bitbucket.org/wiliot/socenv/commits/adc871f0addc7f84e4761d623b449c90a744a460)

- *(format)* run ruff format [7819f42](https://bitbucket.org/wiliot/socenv/commits/7819f42153f90b06e9100712b2baab1c222c0122)

- *(gitignore)* remove non existent legacy paths [8a1fccd](https://bitbucket.org/wiliot/socenv/commits/8a1fccd5707c79570ac0c6324ae4f4b868dd4eed)

- *(log)* change default verbosity level [ac9afe5](https://bitbucket.org/wiliot/socenv/commits/ac9afe535cfd8a56b99e765338bf93c5fbd727ac)

- *(lsp)* add basedpyright config file [87b293b](https://bitbucket.org/wiliot/socenv/commits/87b293b2e89109046cb3cc0253a0765b26ad8b76)

- *(parser)* remove dead code [d213e05](https://bitbucket.org/wiliot/socenv/commits/d213e05e4e0fbad5c6b3599de46204b8b5ea620b)

- *(plugings/convert/converter)* organize imports [7d936fe](https://bitbucket.org/wiliot/socenv/commits/7d936fef8e6901e67b3a133c186617898aaea52f)

- *(plugins.yaml)* add 'enabled' field to all plugins [8fe1055](https://bitbucket.org/wiliot/socenv/commits/8fe10550a7ecdc89a80040decb2fc160cc04f3ee)

- *(plugins/convert/writer)* add logging, remove generic from base [9f9075d](https://bitbucket.org/wiliot/socenv/commits/9f9075d970484282445f03f5f2af801d0cafa777)

- *(plugins/git)* add manifest support for default_format setting [40a0e14](https://bitbucket.org/wiliot/socenv/commits/40a0e14e01ab01a3dfb490ea70904ec5a4bc380e)

- *(plugins/rgr)* rename functions to more appropriate names [585fe20](https://bitbucket.org/wiliot/socenv/commits/585fe20be8568132d0d9287a29df8cbfe94001f2)

- *(plugins/version)* add logging and make output prettier [cdde915](https://bitbucket.org/wiliot/socenv/commits/cdde915b554ab3d7d8684d5cc847e6ec9cd1f717)

- *(pre-commit)* update pre-commit config [6108920](https://bitbucket.org/wiliot/socenv/commits/61089206655258637cca8a2d29d22a59e38e1571)

- *(pyproject.toml)* update pyproject.toml [3f9ea5b](https://bitbucket.org/wiliot/socenv/commits/3f9ea5b884c48cdeb4b7a985f24d233c691849f0)

- *(pyproject.toml)* update pyproject.toml [4198400](https://bitbucket.org/wiliot/socenv/commits/41984005ab252945a0a22057b8cde096421fe7ac)

- *(pyproject.toml)* adjust dev deps and tool configurations [4dc1a0a](https://bitbucket.org/wiliot/socenv/commits/4dc1a0ac3af58f217c3cbf7df13a95dcd78c9685)

- *(pyproject.toml)* add dependencies [ecabbb9](https://bitbucket.org/wiliot/socenv/commits/ecabbb93261be89c269437a9bb8691e7b39161ca)

- *(pyproject.toml)* add textual-autocomplete dependency [d1f9015](https://bitbucket.org/wiliot/socenv/commits/d1f901523d4c662de9eecc49f3445b3575f3d912)

- *(pyproject.toml)* update scripts and entry-points [a732c1a](https://bitbucket.org/wiliot/socenv/commits/a732c1a813ffd39331c1d52d9fbcf5f7476744e5)

- *(pyproject.toml)* cleanups and corrections [9ad9968](https://bitbucket.org/wiliot/socenv/commits/9ad9968284633fb6d7f24979b5834581b0a3c9c6)

- *(pyproject.toml)* add pre-commit dependency to dev group [117ecac](https://bitbucket.org/wiliot/socenv/commits/117ecac3de5b001b2f61363ab31964531791b784)

- *(pyproject.toml,uv.lock)* update deps [a14498f](https://bitbucket.org/wiliot/socenv/commits/a14498f286c0eef9c014b79df55df834d6e1dfe3)

- *(regression)* improve output smoothness, scheduler and runner timings [ef8ba51](https://bitbucket.org/wiliot/socenv/commits/ef8ba5115fc4d50e716340dbdf67ac66b3136cad)

- *(regression)* remove unused imports [9c74a40](https://bitbucket.org/wiliot/socenv/commits/9c74a401a42bbdbf52956ef564309fc9d9d5eeb3)

- *(regression)* fine tune configurations [ae90412](https://bitbucket.org/wiliot/socenv/commits/ae904125988f6b368c75c4d612cdcbf88d36d461)

- *(regression)* rename Status,Command to TestStatus,TestCommand [ce4792a](https://bitbucket.org/wiliot/socenv/commits/ce4792aa138c9b0d0e888bf23c1e0f93c73862db)

- *(regression.toml)* add max_parallel_runs configuration [11098b0](https://bitbucket.org/wiliot/socenv/commits/11098b07079f21cbfaf9c621972c6b565b099c3c)

- *(settings)* delete unused toml configuration files [e212c76](https://bitbucket.org/wiliot/socenv/commits/e212c76a6ffaf88b2331f5a382fd5662ac274752)

- *(settings)* reorganize settings load order [10cf095](https://bitbucket.org/wiliot/socenv/commits/10cf095f0bbd82af8ea1a943efa396ab63ddc5b2)

- *(settings/git)* adjust column names [2989be4](https://bitbucket.org/wiliot/socenv/commits/2989be47520f9213956e63ae7731bcd796357d9b)

- *(socx)* remove some internal exports [4bdd47f](https://bitbucket.org/wiliot/socenv/commits/4bdd47fcf27aeb08c0f5653ff6bf3ef6e374b8eb)

- *(socx.config.paths)* remove version from log path [6268445](https://bitbucket.org/wiliot/socenv/commits/6268445ed505822d0b71625cfa2971a141139e67)

- *(test)* add empty constructor and 'escaped' member to TestCommand [7d55644](https://bitbucket.org/wiliot/socenv/commits/7d55644910ca850334649a81c1468c43d3a15607)

- *(tui)* add hoptex to project dependencies [e31e828](https://bitbucket.org/wiliot/socenv/commits/e31e828a6f3c7d98c52da51c5d0d628b1a7e243d)

- *(uv)* remove and ignore uv.lock [ae798fd](https://bitbucket.org/wiliot/socenv/commits/ae798fdd07aba31487ebe906519b2d63145a2466)

- *(uv)* update uv.lock [bb8d095](https://bitbucket.org/wiliot/socenv/commits/bb8d095763c3719e9747d5b0698f28acf68fc61a)

- *(uv.lock)* update lockfile [5093fe2](https://bitbucket.org/wiliot/socenv/commits/5093fe2fc6100efee3a3ae422fe01bbb5dd8f6e3)

- *(uv.lock)* update lock file [e68727e](https://bitbucket.org/wiliot/socenv/commits/e68727ec50797168dfa52ebfb80a4e8660b78584)

- *(version)* bump version to 0.4.4.dev1 [8f071f5](https://bitbucket.org/wiliot/socenv/commits/8f071f5f47778c6e245585d340851c17ac9e3cac)

- *(visitor)* sort exports [bb376e2](https://bitbucket.org/wiliot/socenv/commits/bb376e216f8a183855dabb123e738b84c522c648)

- prepare release 0.5.0 [26d2175](https://bitbucket.org/wiliot/socenv/commits/26d2175fb30854176ec9b49a220c6381728b04ff)

- update changelog [1bfbfa5](https://bitbucket.org/wiliot/socenv/commits/1bfbfa53b114dc708fffc1e3c45e5c3a2ff20c9e)

- add binary build target, remove 'socx_patches' [2aa1a26](https://bitbucket.org/wiliot/socenv/commits/2aa1a26d17a0eb68acf3baf4742b67c42f455814)

- remove old svg assets [116c6d7](https://bitbucket.org/wiliot/socenv/commits/116c6d78ccce223a16c1ed072643be9129aea1ba)

- add help rule to Makefile [fad8847](https://bitbucket.org/wiliot/socenv/commits/fad8847b802afbb6ca6679facd1c37c53752a1ed)

- add cliff.toml config for git-cliff [8aeda97](https://bitbucket.org/wiliot/socenv/commits/8aeda97380ade462bd35c355885b68b49f5c7233)

- remove double settings reference [ac67dec](https://bitbucket.org/wiliot/socenv/commits/ac67dec5c2b68af506118a03f8abd0518d206f04)

- bump version to 0.4.3 [e3393c5](https://bitbucket.org/wiliot/socenv/commits/e3393c5025076df66656c596822da84e6e633031)

- update uv.lock [0e37705](https://bitbucket.org/wiliot/socenv/commits/0e37705243eab3788de658781d0282028b578d14)

- minor meaningless yaml format correction in settings.yaml [c896ac1](https://bitbucket.org/wiliot/socenv/commits/c896ac1c90b93c02b34c4c91c847945109e85b0d)

- update uv.lock and pyproject dependencies [78f6a48](https://bitbucket.org/wiliot/socenv/commits/78f6a486c43fa7af8cae3a339af2da1885639c10)

- update .gitignore [d4ae578](https://bitbucket.org/wiliot/socenv/commits/d4ae57817d8cf3efc0a2bafbc3307b6aff35122d)

- update uv.lock [e6ba00f](https://bitbucket.org/wiliot/socenv/commits/e6ba00f148914696e3d39ac23f1d7c8971b9e5f7)

- update dependencies and uv lock file [81b57c7](https://bitbucket.org/wiliot/socenv/commits/81b57c79d94e8bc7f33e545128a113bf0eb0ee37)

- update uv.lock [b14b09a](https://bitbucket.org/wiliot/socenv/commits/b14b09ab79e4531fef1fe4bd3bb35fc5f7f08745)

- remove double settings reference [d322cb6](https://bitbucket.org/wiliot/socenv/commits/d322cb61c311d3179ab387e7fd0f9a74bd29ab9d)

- add basedpyright config file [d697d9c](https://bitbucket.org/wiliot/socenv/commits/d697d9cb93165e8fc12e2aaf4420d87c809f326b)

- update uv.lock [983c4f4](https://bitbucket.org/wiliot/socenv/commits/983c4f49f510406febdf28aa8023f2d0a1623524)

- add dummy socrun script [85ef118](https://bitbucket.org/wiliot/socenv/commits/85ef1181f081d76755355b0aab0a91c1a6760860)

- fix 'config get' plugin docs, update dependencies [9708a66](https://bitbucket.org/wiliot/socenv/commits/9708a66b5f4ce7cb4cebf5c00e4d6f2d8496fdaa)

- update mypy settings, fix ruff lint errors [fae79e8](https://bitbucket.org/wiliot/socenv/commits/fae79e8e671fed95a12e20f3fc7cd5c37616a898)

- format with `ruff format` and fix `ruff check` errors [028d689](https://bitbucket.org/wiliot/socenv/commits/028d68971e4fc30fbe7adf6a346e1ead93562c5e)

- format files with ruff [d59869b](https://bitbucket.org/wiliot/socenv/commits/d59869ba2c8dad3d0871f530666bb64e2c3312e9)

- restore .env testing env variables [15ffe8b](https://bitbucket.org/wiliot/socenv/commits/15ffe8b3735a36169aa3037027f7a8007eb2e346)

- add feature request and bug report templates (#32) [0ee31b0](https://bitbucket.org/wiliot/socenv/commits/0ee31b06b14e38eb49900af53779d404d26b44bb)

- correct cli->rgr->rrfh options metavars [77843dc](https://bitbucket.org/wiliot/socenv/commits/77843dc12bf7050941d3924eb341464c72e11250)

- export RichGroup and RichCommand defined in cli.py [a16c8b8](https://bitbucket.org/wiliot/socenv/commits/a16c8b8dc964a5b772ad37d5fed78ff922170c58)

- remove unused test.toml config [66be11b](https://bitbucket.org/wiliot/socenv/commits/66be11bc533f307a2bbff07e5e8e7ca0d01627ab)

- add numpy and psutil dependencies [3ed51e6](https://bitbucket.org/wiliot/socenv/commits/3ed51e6f7cff5211ce6a738df741a0b8d5e4df76)

- rename plugins to socx_plugins [4a59605](https://bitbucket.org/wiliot/socenv/commits/4a59605a14de9cf29b3b210a8ee2301b378b009e)

<!-- generated by git-cliff -->
