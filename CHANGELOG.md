# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [0.11.5](https://github.com/sagikimhi/socx-cli/releases/tag/0.11.5) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.11.5)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- update credits ([91898b9](https://github.com/sagikimhi/socx-cli/commit/91898b9a62943a8cc30bff1f880e0aef10894ca1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration reference page ([715e918](https://github.com/sagikimhi/socx-cli/commit/715e91827e1708c27b5ed03dd773ff752a039140) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor corrections ([127fdaa](https://github.com/sagikimhi/socx-cli/commit/127fdaae6ad633aba43a191fc6f62947de47fa90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update svg assets ([3d09c34](https://github.com/sagikimhi/socx-cli/commit/3d09c3462f5e8c12a68916d0d749794a764b84ac) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve looks a bit ([ea75bda](https://github.com/sagikimhi/socx-cli/commit/ea75bdafaa5a7c147a67805b5fbd748aab95ea28) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- remove 'convert' and 'lang' from config reference ([90bb358](https://github.com/sagikimhi/socx-cli/commit/90bb3586757d5548201487066eb5fcf103497e6c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.11.4](https://github.com/sagikimhi/socx-cli/releases/tag/0.11.4) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.11.4)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- minor corrections ([127fdaa](https://github.com/sagikimhi/socx-cli/commit/127fdaae6ad633aba43a191fc6f62947de47fa90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update svg assets ([3d09c34](https://github.com/sagikimhi/socx-cli/commit/3d09c3462f5e8c12a68916d0d749794a764b84ac) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve looks a bit ([ea75bda](https://github.com/sagikimhi/socx-cli/commit/ea75bdafaa5a7c147a67805b5fbd748aab95ea28) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- remove 'convert' and 'lang' from config reference ([90bb358](https://github.com/sagikimhi/socx-cli/commit/90bb3586757d5548201487066eb5fcf103497e6c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.11.3](https://github.com/sagikimhi/socx-cli/releases/tag/0.11.3) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.11.3)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- minor corrections ([127fdaa](https://github.com/sagikimhi/socx-cli/commit/127fdaae6ad633aba43a191fc6f62947de47fa90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update svg assets ([3d09c34](https://github.com/sagikimhi/socx-cli/commit/3d09c3462f5e8c12a68916d0d749794a764b84ac) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve looks a bit ([ea75bda](https://github.com/sagikimhi/socx-cli/commit/ea75bdafaa5a7c147a67805b5fbd748aab95ea28) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- remove 'convert' and 'lang' from config reference ([90bb358](https://github.com/sagikimhi/socx-cli/commit/90bb3586757d5548201487066eb5fcf103497e6c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.11.2](https://github.com/sagikimhi/socx-cli/releases/tag/0.11.2) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.11.2)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- minor corrections ([127fdaa](https://github.com/sagikimhi/socx-cli/commit/127fdaae6ad633aba43a191fc6f62947de47fa90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update svg assets ([3d09c34](https://github.com/sagikimhi/socx-cli/commit/3d09c3462f5e8c12a68916d0d749794a764b84ac) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve looks a bit ([ea75bda](https://github.com/sagikimhi/socx-cli/commit/ea75bdafaa5a7c147a67805b5fbd748aab95ea28) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- remove 'convert' and 'lang' from config reference ([90bb358](https://github.com/sagikimhi/socx-cli/commit/90bb3586757d5548201487066eb5fcf103497e6c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.11.1](https://github.com/sagikimhi/socx-cli/releases/tag/0.11.1) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.11.1)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- update svg assets ([3d09c34](https://github.com/sagikimhi/socx-cli/commit/3d09c3462f5e8c12a68916d0d749794a764b84ac) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve looks a bit ([ea75bda](https://github.com/sagikimhi/socx-cli/commit/ea75bdafaa5a7c147a67805b5fbd748aab95ea28) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- remove 'convert' and 'lang' from config reference ([90bb358](https://github.com/sagikimhi/socx-cli/commit/90bb3586757d5548201487066eb5fcf103497e6c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.11.0](https://github.com/sagikimhi/socx-cli/releases/tag/0.11.0) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.11.0)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- improve looks a bit ([ea75bda](https://github.com/sagikimhi/socx-cli/commit/ea75bdafaa5a7c147a67805b5fbd748aab95ea28) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- remove 'convert' and 'lang' from config reference ([90bb358](https://github.com/sagikimhi/socx-cli/commit/90bb3586757d5548201487066eb5fcf103497e6c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.10.1](https://github.com/sagikimhi/socx-cli/releases/tag/0.10.1) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.10.1)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.9.0](https://github.com/sagikimhi/socx-cli/releases/tag/0.9.0) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.9.0)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.8.0](https://github.com/sagikimhi/socx-cli/releases/tag/0.8.0) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.8.0)</small>

### Features

- add cmd_timeout cfg field ([7ade98a](https://github.com/sagikimhi/socx-cli/commit/7ade98ae506e3a08218ebab67cb3700469863ee0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix current directory repo missing from manifest ([582b688](https://github.com/sagikimhi/socx-cli/commit/582b68804db6c813f54359c1497e9bdcf08c7783) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing errors ([1014cdc](https://github.com/sagikimhi/socx-cli/commit/1014cdc191bcec494a8001469430f4f56f3f9d11) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix typing issue in print_command_outputs ([12e2e1b](https://github.com/sagikimhi/socx-cli/commit/12e2e1bc04f5cefd7be1d979e8bb20f0e1981dd9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- add --no-write-fetch-head to fetch flags ([db8cf61](https://github.com/sagikimhi/socx-cli/commit/db8cf611f14fedf7aee1142b5aa9a25460157756) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- update overview page (#115) ([a741e3d](https://github.com/sagikimhi/socx-cli/commit/a741e3d03c44d6caeab9389c8450e2ad3629919f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update overview page ([320d1a9](https://github.com/sagikimhi/socx-cli/commit/320d1a99f927fe4958691e63922135efd44c63c7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move zensical.toml to config until feature parity ([248db56](https://github.com/sagikimhi/socx-cli/commit/248db56eb39353d83842c50252ebd9b040537c6a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([1f8b46c](https://github.com/sagikimhi/socx-cli/commit/1f8b46c0aa91693902f7180a1b45041630b6be7e) by Sagi Kimhi). Related issues/PRs: [#108](https://github.com/sagikimhi/socx-cli/issues/108) References: #108, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.7.0](https://github.com/sagikimhi/socx-cli/releases/tag/0.7.0) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.7.0)</small>

### Features

- add support for short_help in addition to help in plugins ([75298aa](https://github.com/sagikimhi/socx-cli/commit/75298aa4a417afe58f8ae09f34aced4a6c59e51e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- configure rich-click from yaml configuration settings ([0d2335c](https://github.com/sagikimhi/socx-cli/commit/0d2335cddefb9520f370ab07e3c9509ebc0a3410) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add support for shell script plugins (#104) ([c9305af](https://github.com/sagikimhi/socx-cli/commit/c9305af8a8a22f3e9a6c21be9c74dc7f37883b59) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- transition to using sh package instead of git ([3490660](https://github.com/sagikimhi/socx-cli/commit/3490660e3e8b4e844451007a56d348c94d121f68) by Sagi Kimhi). Related issues/PRs: [#83](https://github.com/sagikimhi/socx-cli/issues/83) References: #83, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- cleanup regression settings and improve help text ([33e3383](https://github.com/sagikimhi/socx-cli/commit/33e33838e408404afa936d108254aa39ab5f499a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust tree formatter output style ([55434a1](https://github.com/sagikimhi/socx-cli/commit/55434a1a1e62587b3eef038a4cb218f9d7870050) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- rename method add_options to join_decorators ([96f9afe](https://github.com/sagikimhi/socx-cli/commit/96f9afe34cf9f4a1872b89ba75b9aa88fb21bcbe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([3410b17](https://github.com/sagikimhi/socx-cli/commit/3410b179d891535851f5ae3375ab9da5655e7981) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.6.0](https://github.com/sagikimhi/socx-cli/releases/tag/0.6.0) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.6.0)</small>

### Features

- add support for shell script plugins (#103) ([8d50e38](https://github.com/sagikimhi/socx-cli/commit/8d50e383d0e1bf7ff58bd0dc2c6868f29aab5d9e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add support for shell script plugins ([88faffe](https://github.com/sagikimhi/socx-cli/commit/88faffe9018817a7f60154edb106e9355165811c) by Sagi Kimhi). Related issues/PRs: [#81](https://github.com/sagikimhi/socx-cli/issues/81) Closes: #81, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([3410b17](https://github.com/sagikimhi/socx-cli/commit/3410b179d891535851f5ae3375ab9da5655e7981) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.5.9](https://github.com/sagikimhi/socx-cli/releases/tag/0.5.9) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.5.9)</small>

### Features

- add more `socx git` commands (#101) ([a84fd1a](https://github.com/sagikimhi/socx-cli/commit/a84fd1a03c9846975ec71841819f8692d5acafc5) by Sagi Kimhi). - **feat(socx_plugins.git): add git diff and git pull commands**, - **feat(socx_plugins.git): execute manifest git commands in parallel**, - **feat(socx_plugins.git): implement git log command**, - **feat(socx_plugins.git): add live and pager output support**
- add live and pager output support ([5476f2d](https://github.com/sagikimhi/socx-cli/commit/5476f2de8829ec6da0dc1f6a13b56628c05bbdaa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git log command ([57a575a](https://github.com/sagikimhi/socx-cli/commit/57a575a5c946075787afd184f6fde8346fee7011) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- execute manifest git commands in parallel ([76ffcfb](https://github.com/sagikimhi/socx-cli/commit/76ffcfb27952479f05d1ebfb635bf37dd2ea6955) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add git diff and git pull commands ([2d3ec39](https://github.com/sagikimhi/socx-cli/commit/2d3ec39d9e63cb25023e1847b36a03cba968ec34) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- implement git multi-status ([13cb570](https://github.com/sagikimhi/socx-cli/commit/13cb570c169301f70ba519e6b8b64424001d04ee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- set pager flag default value to False ([b453cc2](https://github.com/sagikimhi/socx-cli/commit/b453cc292d771f828a041e4ddd2521682a6f8888) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- make status tree formatting prettier ([286e29c](https://github.com/sagikimhi/socx-cli/commit/286e29ce9b209746b3dd6c31581119aa6f60d1b3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling, adjust default settings ([63cd90f](https://github.com/sagikimhi/socx-cli/commit/63cd90f3982ff799cfe4a2b63df8a4d832300014) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- stop using global rich.console.console instance ([d9c3e52](https://github.com/sagikimhi/socx-cli/commit/d9c3e520addde8307f86f44a4093349d718f61ad) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename manifest cmd, class and config to summary ([0dd3176](https://github.com/sagikimhi/socx-cli/commit/0dd3176b5478f668d0c2c6068b2a59371db1dccd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename 'default_format' field to 'format' ([0bc6dd0](https://github.com/sagikimhi/socx-cli/commit/0bc6dd0bd82dbf3aa332ec0f01c971c68a5e56fe) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- transition from mkdocs to zensical ([c859d1e](https://github.com/sagikimhi/socx-cli/commit/c859d1e11a2558e277f87a5308e9787be3f4abc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation (#97) ([cd9a35d](https://github.com/sagikimhi/socx-cli/commit/cd9a35daad66ef5db27b145623b54f49b2820b56) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update documentation ([3410b17](https://github.com/sagikimhi/socx-cli/commit/3410b179d891535851f5ae3375ab9da5655e7981) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.5.7](https://github.com/sagikimhi/socx-cli/releases/tag/0.5.7) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.5.7)</small>

### Features

- add async runtime writes of regression tests outputs ([c69b678](https://github.com/sagikimhi/socx-cli/commit/c69b678b92fd1b78ea905fe6b9fb8abd2f8c347b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- write regression results, per-test stdout and stderr to disk ([d7fed4d](https://github.com/sagikimhi/socx-cli/commit/d7fed4d27985ba0293aa9433bd69d4e5700eb567) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix lst to sv converter ([6f5e58f](https://github.com/sagikimhi/socx-cli/commit/6f5e58fedd3afb7c2d6c86ec2ce0a1212e3ed4c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix test failed status even when passed ([026dd55](https://github.com/sagikimhi/socx-cli/commit/026dd55220be8bb6f5db250eb7a11e6169ba3998) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix -h flag not triggering help menu ([717b424](https://github.com/sagikimhi/socx-cli/commit/717b424c85ec2f9ff43891a7258da3809fd62d0a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix `socx config get` help menu ([97a4d04](https://github.com/sagikimhi/socx-cli/commit/97a4d0405cc9e40105c64106e7adb052f80893b7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix IncludeConverter ([147ef9a](https://github.com/sagikimhi/socx-cli/commit/147ef9a0506e0c36f604d6475e5961fd72847127) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix export_svg rule ([c2427ca](https://github.com/sagikimhi/socx-cli/commit/c2427ca98fd39232966819da69453084ba765b51) by Sagi Kimhi). Related issues/PRs: [#82](https://github.com/sagikimhi/socx-cli/issues/82) Fixes: #82, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- clean up code and improve progress visualization ([5e327ed](https://github.com/sagikimhi/socx-cli/commit/5e327ed9a2c5c829bccab71d723a40f36a310d6d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- enable tracebacks in logs ([b4f0579](https://github.com/sagikimhi/socx-cli/commit/b4f057932d29ee59341b678db1885914be5e9bf0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve input assets for testing and adjust settings ([483bd79](https://github.com/sagikimhi/socx-cli/commit/483bd790aa47c2f4df87314ca70bb6c639b179a9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- read context_settings from settings.cli ([80eabdd](https://github.com/sagikimhi/socx-cli/commit/80eabdd1a9e81f6f7d667f93472176fbc72fe4b9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add settings.cli.context_settings config field ([2416e2b](https://github.com/sagikimhi/socx-cli/commit/2416e2b69e68b512194fb2e3cbe76980f16f1cdd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- run 'make clean' at the end of 'docs_deploy' ([db554b3](https://github.com/sagikimhi/socx-cli/commit/db554b33c0762161e46ce133d33851c183740988) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- update documentation ([3410b17](https://github.com/sagikimhi/socx-cli/commit/3410b179d891535851f5ae3375ab9da5655e7981) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a 'Core Concepts' section to the top navigation menu ([7e45d2b](https://github.com/sagikimhi/socx-cli/commit/7e45d2bb8bbb87457a6123f26e28758cf0bc2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.5.4](https://github.com/sagikimhi/socx-cli/releases/tag/0.5.4) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.5.4)</small>

### Features

- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- discard uvloop dependency to support for python3.14 ([621a1f2](https://github.com/sagikimhi/socx-cli/commit/621a1f214fb18d98218796fdd785a6168496fa87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.5.3](https://github.com/sagikimhi/socx-cli/releases/tag/0.5.3) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.5.3)</small>

### Features

- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix command converter runtime warning ([04a8ca7](https://github.com/sagikimhi/socx-cli/commit/04a8ca7ef9e6819125c43fdab1e7fb60ff810c46) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- add/update missing/outdated python docstrings (#71) ([6fdba72](https://github.com/sagikimhi/socx-cli/commit/6fdba7202efce2ffa1d03d39886c5f7ebf311e99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- update project documentation ([7988e0c](https://github.com/sagikimhi/socx-cli/commit/7988e0c1d9121cd1bf95beab4d1b32de6efb1b81) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add/update missing/outdated python docstrings ([7f6dee1](https://github.com/sagikimhi/socx-cli/commit/7f6dee149190eef4dbae2f801cf295c1f86d0afc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.5.2](https://github.com/sagikimhi/socx-cli/releases/tag/0.5.2) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.5.2)</small>

### Features

- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix mypy typing errors ([702ec05](https://github.com/sagikimhi/socx-cli/commit/702ec052803011b8e0184751ee8ca4ae01b66f55) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix runtime loading of CLI plugins ([38c7148](https://github.com/sagikimhi/socx-cli/commit/38c714805f7e49a098d97078c0af473777a546c5) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.5.1](https://github.com/sagikimhi/socx-cli/releases/tag/0.5.1) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.5.1)</small>

### Features

- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix loading of external/3rd-party plugins ([fd87676](https://github.com/sagikimhi/socx-cli/commit/fd876760c06c50d109505b3b4ce2c1eb8c23e9e8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct typing of `get_settings` ([edc084d](https://github.com/sagikimhi/socx-cli/commit/edc084d10265a1136eabd93455170a9b6d3548a8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- display version using uv instead of pip ([4ee39b3](https://github.com/sagikimhi/socx-cli/commit/4ee39b3d3efb74edb2884cb1140ad8fec787fc13) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- add missing mkdocs.yml ([bd46cb0](https://github.com/sagikimhi/socx-cli/commit/bd46cb0410e6e57a98807feb9ed9b64e5d092576) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.5.0](https://github.com/sagikimhi/socx-cli/releases/tag/0.5.0) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.5.0)</small>

### Features

- add Makefile to automate development tasks ([6447162](https://github.com/sagikimhi/socx-cli/commit/6447162ac840a8b8a69f7f3eb50c3e470cadf9e9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add ahead-behind status column to manifest ([754c819](https://github.com/sagikimhi/socx-cli/commit/754c819895a3fa3398d088ae24688dedc2be8a21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add object serialization module ([c8e7592](https://github.com/sagikimhi/socx-cli/commit/c8e759282bd3ed27c253a28a7e9f841825c19f87) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add @command converter ([bfc1c62](https://github.com/sagikimhi/socx-cli/commit/bfc1c620419543b663db8fbd795fab08484ea480) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wip developing ui ([f8a11b1](https://github.com/sagikimhi/socx-cli/commit/f8a11b1e87a825b93fbb62e933b3a8aaf279fd1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add vim-like movement bind modes ([13142ee](https://github.com/sagikimhi/socx-cli/commit/13142eebb58c37a233de573c1502ce0c4235da08) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add option to pass verbosity level arg to log_it ([e9bf43b](https://github.com/sagikimhi/socx-cli/commit/e9bf43bed1243f31f2d505c0c1632ca0e6227370) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- install pretty tracebacks on console ([d65333a](https://github.com/sagikimhi/socx-cli/commit/d65333a6dc39d3c518472db4e60c3934694af8fa) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add --version flag for printing version info ([02d9480](https://github.com/sagikimhi/socx-cli/commit/02d9480436e38d87ac0f6577c7efcc295a3881d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add global options, option groups, and callbacks ([73f0583](https://github.com/sagikimhi/socx-cli/commit/73f058334a81f8ff40809891ea16aa464fe07cc2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add callbacks to ease handling of options and arguments ([70bd332](https://github.com/sagikimhi/socx-cli/commit/70bd332e501ba2a1b1e1dad524a80220d242a161) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add env subcommand and plugin ([bf109dd](https://github.com/sagikimhi/socx-cli/commit/bf109ddba85072771e26c860387367491e714b99) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- fix some typing issues in manifest, utils ([b72a44a](https://github.com/sagikimhi/socx-cli/commit/b72a44a0a08e15c486e131689cc418ca1e3329f6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix CLI after breaking changes of rich-click 1.9.0 ([d2e9816](https://github.com/sagikimhi/socx-cli/commit/d2e98160402d4af35a53f417ab393c288d7646d8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix version command ([b8fba3a](https://github.com/sagikimhi/socx-cli/commit/b8fba3ac4a04547934bfe2cf5e5c5bafc3d9d88a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect flags in `make publish` rule ([b35f0bf](https://github.com/sagikimhi/socx-cli/commit/b35f0bfa9bca327858dd2074e89c5ce8d2182552) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix @command help texts ([8ece5cb](https://github.com/sagikimhi/socx-cli/commit/8ece5cb4f3850b917059a7ab230665b3835ffbf1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix `make clean` rules ([ab17ac2](https://github.com/sagikimhi/socx-cli/commit/ab17ac21cf22269760af8a2a4b0d990968a1bc16) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix edit command ([7133779](https://github.com/sagikimhi/socx-cli/commit/71337798f37918f47c720840c4e3231bda1708eb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect settings_file argument ([f6cd1ff](https://github.com/sagikimhi/socx-cli/commit/f6cd1ff2b258ee4396bfaff62a0c2fe4cc18b3ce) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- only load `click.Command` subclasses as plugins ([7426e54](https://github.com/sagikimhi/socx-cli/commit/7426e54b3610c45d21eba71fc5ee7e524a756dfc) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix AttributeError when loading regression from file ([4dcda47](https://github.com/sagikimhi/socx-cli/commit/4dcda47e23fa775885fd1468357dbaaa36a28305) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix default path value ([5b20254](https://github.com/sagikimhi/socx-cli/commit/5b20254ca1dd8bdb8a16a71f7e3c5e86cbebafaf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix exception due to missing __spec__ ([8ed76e5](https://github.com/sagikimhi/socx-cli/commit/8ed76e51aa142585ba67bc5354ef5ca3b3dc2a30) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct path to test's log file ([f525fa5](https://github.com/sagikimhi/socx-cli/commit/f525fa568cb4cb37195bb0c080dc9395c9680817) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- minor typing fixes in git manifest plugin ([64acf03](https://github.com/sagikimhi/socx-cli/commit/64acf03864dd9be029f3956967e2c710ad4de786) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set start and finish times ([9c0b64c](https://github.com/sagikimhi/socx-cli/commit/9c0b64cbcd62b721e362da19e0ef87ba19ce5c2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- set up 'socx' logger instead of root logger ([62473f8](https://github.com/sagikimhi/socx-cli/commit/62473f82fdecde2e0771b4b71c59bb159e4c1883) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix configuration overriding and loading order ([e57ef5b](https://github.com/sagikimhi/socx-cli/commit/e57ef5b1e2c236f661d4bdd1da0e2522eb737a3d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix missing `log` export ([f9589bf](https://github.com/sagikimhi/socx-cli/commit/f9589bfe924fb627c0d023b6e202459d8c6ef55c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([9e7881f](https://github.com/sagikimhi/socx-cli/commit/9e7881f61f01915165c0373520051cd85c568138) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix typing ([a7bc0e1](https://github.com/sagikimhi/socx-cli/commit/a7bc0e1e928aa910843c1370081e23f40dd7fad1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([0126aef](https://github.com/sagikimhi/socx-cli/commit/0126aef8692abe3a638866254e42482bf0de48da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix _CmdLine inheritence ([554c5b8](https://github.com/sagikimhi/socx-cli/commit/554c5b8b1040a06ebe9e2cd9ef03b61307afd7bb) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([a1b194f](https://github.com/sagikimhi/socx-cli/commit/a1b194f16b01f37538d53d3ffe3348ce46257a1c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix tui decorator type annotation ([3e30a0f](https://github.com/sagikimhi/socx-cli/commit/3e30a0f57300d4828b7bfd0958e534238ba47d14) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- use __spec__.name instead of __package__ ([9d27ca6](https://github.com/sagikimhi/socx-cli/commit/9d27ca628c98720a02b44e3873edd499eef63ee7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix type hints of tui decorator ([f27d96e](https://github.com/sagikimhi/socx-cli/commit/f27d96e49b57dff1425bf43fa77045be7ed9f86d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove relative import and fix typing ([6dd9ce0](https://github.com/sagikimhi/socx-cli/commit/6dd9ce07070bd8a9c0779f83e16a0252142684cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct dotenv development env variables ([bfe012e](https://github.com/sagikimhi/socx-cli/commit/bfe012e20a896e3efbf6a9d1f0a633b85ae5f373) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- fix mypy typing errors, discard Vim implementation ([24737e3](https://github.com/sagikimhi/socx-cli/commit/24737e336505d271d7c60008c3e154adf2d4d316) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy typing errors ([ceb0dbf](https://github.com/sagikimhi/socx-cli/commit/ceb0dbfdff2ad645940a435f06803f33b87921a1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix all mypy errors ([dd80f31](https://github.com/sagikimhi/socx-cli/commit/dd80f31155efff34ca9451e3147bfcf6dd4bf50c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors ([73ddf0f](https://github.com/sagikimhi/socx-cli/commit/73ddf0fab4313e1bd3eb01c10f6efa3b959ad404) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken terminal ui, set up pre-commit ([bd60074](https://github.com/sagikimhi/socx-cli/commit/bd600741c34a4c009d4cbe72b6567c95013ba3da) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix failed and passed test file formatting ([06cb7e5](https://github.com/sagikimhi/socx-cli/commit/06cb7e56ece7cc3b49cc2d5a329d051fa96c32cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix broken rgr command due to mypy fixes ([a5ac756](https://github.com/sagikimhi/socx-cli/commit/a5ac7566be05acd5e683b689d2c7392c1d2e28e4) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in regression subpackage ([3626bed](https://github.com/sagikimhi/socx-cli/commit/3626beddedb914f370a9d920dbaf2bb91aefdd21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in log.py ([5bb8e06](https://github.com/sagikimhi/socx-cli/commit/5bb8e06bd3af45240f8d3f19aa427a084ad4f197) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in decorators.py ([5fdecd5](https://github.com/sagikimhi/socx-cli/commit/5fdecd5e12893d03961c942200f6089854a4592e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix mypy errors in _rgr.py ([061625d](https://github.com/sagikimhi/socx-cli/commit/061625d1ab5c03609b00b92f3a3cefc9b7a42766) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix type hints and implementation of traversals ([105220b](https://github.com/sagikimhi/socx-cli/commit/105220bedca8859aff323410858c624e5bc25092) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix incorrect assets path setting ([7719ecf](https://github.com/sagikimhi/socx-cli/commit/7719ecf97bbe223e0076745f268836819a6b3ba3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix missing column names in json manifest ([cc7f746](https://github.com/sagikimhi/socx-cli/commit/cc7f746fb98727ef5b110116217ed2a6595b0757) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix inconsistent revision hash length in manifest ([b5f0d88](https://github.com/sagikimhi/socx-cli/commit/b5f0d88789287a9a289fbc20e66fa220d915b08c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix ref and json formatted manifests ([dcc992c](https://github.com/sagikimhi/socx-cli/commit/dcc992cc53badc3854375ca9f1cbbfcc1fdea24b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix option callbacks ([2dfa959](https://github.com/sagikimhi/socx-cli/commit/2dfa959a4cd0c962dab1de1f7d07cd91405c020e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix debug logging to socx.log when debug mode is enabled ([6a14191](https://github.com/sagikimhi/socx-cli/commit/6a1419191bb654c88aaa494d7572d8e0613f1523) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- log_it now logs to global socx.log run log ([c18e495](https://github.com/sagikimhi/socx-cli/commit/c18e495d892b2770fcd4d9c751b5342e2d0958cd) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct warea to WAREA ([155ae59](https://github.com/sagikimhi/socx-cli/commit/155ae595fdd14695ab2c4dc81b9746c1e87a4e4a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- move str to symbol conversion to code ([e563195](https://github.com/sagikimhi/socx-cli/commit/e563195293fc1f070849d3d594681cef84eaeae2) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve error handling ([09fbe8f](https://github.com/sagikimhi/socx-cli/commit/09fbe8fbc25f03f4994557bd01cb88f01a24112f) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- simplify and improve plugin support and loading ([bfa6d65](https://github.com/sagikimhi/socx-cli/commit/bfa6d65c128b1cfe2cbade121e392a9e51f5990d) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add changelog generation variables ([6a9887a](https://github.com/sagikimhi/socx-cli/commit/6a9887a14786914bacc69a99e0994b0cb6b5004c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use `$(UV)` instead of `uv` in export_svg ([893daa8](https://github.com/sagikimhi/socx-cli/commit/893daa82215e0a567ed253ce6e95e5ca73dfb821) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use upath.UPath instead of pathlib.Path ([a60c8fa](https://github.com/sagikimhi/socx-cli/commit/a60c8fa3aa1e4abd771d6d1f7a0b7ec28104c1be) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- improve exception handling ([8c72a77](https://github.com/sagikimhi/socx-cli/commit/8c72a77fe2a18dbd93b152be50373a0c0a422c66) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- use universal_pathlib ([701015d](https://github.com/sagikimhi/socx-cli/commit/701015dfcc2132e87ca6a2d8444740cb24f3359b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add APP_ROOT_DIR to paths module ([003cb48](https://github.com/sagikimhi/socx-cli/commit/003cb48e7bf6b622e86c132630eabbb8dfe2c07e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- wrap `regression.start` with asyncio task ([707bc15](https://github.com/sagikimhi/socx-cli/commit/707bc15142c57af9307d22e019671b246e829bc0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- adjust default configurations ([ddc414b](https://github.com/sagikimhi/socx-cli/commit/ddc414b855d38778344bf3d096844dafc69d743e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- adjust default configurations ([486442f](https://github.com/sagikimhi/socx-cli/commit/486442f17e1c24d1cf16ae1cab73b46744070d7a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([062f6ee](https://github.com/sagikimhi/socx-cli/commit/062f6eebabf0cbccdad07715bf321cea5a6e2f64) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove unused `cfg` function ([b0e0a04](https://github.com/sagikimhi/socx-cli/commit/b0e0a049c26adfd2b170549933d50d2da2fbe1cf) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([dc86e0c](https://github.com/sagikimhi/socx-cli/commit/dc86e0ca6b2f2d49a2834964a5aba07797ee298e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- pass logger to `log_it` decorator ([e3a5e30](https://github.com/sagikimhi/socx-cli/commit/e3a5e30a7e89fa687fb56cdba819bf5f6f39df7c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([eecef55](https://github.com/sagikimhi/socx-cli/commit/eecef55c588f85ec21e83f6a8f847c83b9eccfba) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add optional logger parameter ([fa69f79](https://github.com/sagikimhi/socx-cli/commit/fa69f7938023e64b66ed548d459302885bfae7e0) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- move mixins into patterns subpackage ([b620400](https://github.com/sagikimhi/socx-cli/commit/b620400a7da2066e45bb0f30c2e8d8536ece091c) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- clean up and re organize code and structure ([ab35344](https://github.com/sagikimhi/socx-cli/commit/ab353445e51bb5b95fc6fc069b4f593fcf1bd996) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rewrite settings.toml and plugins.toml as yaml ([68dc3ad](https://github.com/sagikimhi/socx-cli/commit/68dc3adc6a32885eaf31838355dca1c568019f78) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename env cmd to git and rewrite as package ([464f183](https://github.com/sagikimhi/socx-cli/commit/464f1830450ea722835034e2fdf948cd009885de) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- cleanup env code and add debug logging ([d15e5f1](https://github.com/sagikimhi/socx-cli/commit/d15e5f155a7f5e952d67c26c6ff1cfca9db5d075) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Docs

- configure and build documentation with mkdocs ([325efb2](https://github.com/sagikimhi/socx-cli/commit/325efb2f5b0affc415d7d4a04af5deb70e9d0149) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add CHANGELOG.md ([218eabd](https://github.com/sagikimhi/socx-cli/commit/218eabd807070137d1b47bcd66936f39e26ed08e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([17807c8](https://github.com/sagikimhi/socx-cli/commit/17807c891d202849d4203428f6a01f7d927e2814) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- correct docs of `GROUP_ARGUMENT_OPTIONS` ([9864f7b](https://github.com/sagikimhi/socx-cli/commit/9864f7bb3d841722a518774dc565d2f1bfef565b) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([5578381](https://github.com/sagikimhi/socx-cli/commit/5578381c57838454c646a037bc99bb66e4995f2e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update svg assets ([0e54e76](https://github.com/sagikimhi/socx-cli/commit/0e54e76fefb8029b3642269fa4e59f2386ef61c3) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- update README.md ([6400289](https://github.com/sagikimhi/socx-cli/commit/6400289be3f48b88a207195a2a0ff7642cf67fd1) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add old readme ([4974d6b](https://github.com/sagikimhi/socx-cli/commit/4974d6b3a5c32fd1023dc22de02c88b181de5fee) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.3.0](https://github.com/sagikimhi/socx-cli/releases/tag/0.3.0) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.3.0)</small>

### Features

- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- add misssing socx_patches package ([a2a20d8](https://github.com/sagikimhi/socx-cli/commit/a2a20d8e896cfe84aadfe627e7d978c83ab53aa6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.2.11](https://github.com/sagikimhi/socx-cli/releases/tag/0.2.11) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.2.11)</small>

### Features

- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

## [0.2.6](https://github.com/sagikimhi/socx-cli/releases/tag/0.2.6) - 2026-01-28

<small>[Compare with first commit](https://github.com/sagikimhi/socx-cli/compare/8207c6342287279f97909eec94c3b79382debd59...0.2.6)</small>

### Features

- add rich click help menu for sub-commands (#23) ([3ef833c](https://github.com/sagikimhi/socx-cli/commit/3ef833cee29307822ebc29d548f9f25291944065) by Sagi Kimhi).
- add rich click help menu for sub-commands ([92a4b80](https://github.com/sagikimhi/socx-cli/commit/92a4b80b4af6789935223db9cc2ad73c504d0e63) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add regression rerun support to cli (#22) ([8d5573f](https://github.com/sagikimhi/socx-cli/commit/8d5573f7c6eecdf1543a0c2e9ceec13f7db3b7e2) by Sagi Kimhi).
- fix program not ending, log pass/fail at exit (#20) ([2f869b3](https://github.com/sagikimhi/socx-cli/commit/2f869b3fb19f374fa3a07a8c45d6fe7dc87b0a1a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add async support to test and regression. ([0a723d0](https://github.com/sagikimhi/socx-cli/commit/0a723d0c8c2f4d24178e4d8a929e8cfc680ac25a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add base test class and asyncio support ([74bbe8f](https://github.com/sagikimhi/socx-cli/commit/74bbe8fd909457e7b8ee671a172ede958ea36fd7) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add RegressionStatus enum ([fd45eb2](https://github.com/sagikimhi/socx-cli/commit/fd45eb2d0ff9532419c7e74e76fc79f901277b21) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add a stable working descriptive yet kinda useless cli and cli-tui (#16)(#17) ([a9d65aa](https://github.com/sagikimhi/socx-cli/commit/a9d65aab9323a48f7879c41f0ffdb66c9b320294) by Sagi Kimhi). Related issues/PRs: [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#15](https://github.com/sagikimhi/socx-cli/issues/15), [#9](https://github.com/sagikimhi/socx-cli/issues/9), [#10](https://github.com/sagikimhi/socx-cli/issues/10), [#11](https://github.com/sagikimhi/socx-cli/issues/11), [#12](https://github.com/sagikimhi/socx-cli/issues/12), [#14](https://github.com/sagikimhi/socx-cli/issues/14), [#15](https://github.com/sagikimhi/socx-cli/issues/15) Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>

### Bug Fixes

- add missing rich click dependency ([48b4161](https://github.com/sagikimhi/socx-cli/commit/48b4161244681eeccca9145110e2d03c22fed0c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- replace print with log in meth 'start', add missing await (#24) ([8133742](https://github.com/sagikimhi/socx-cli/commit/81337423de743af0d67af43b2457e3f7c3ecb1b8) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct default gateway configurations (#21) ([1b3bf5d](https://github.com/sagikimhi/socx-cli/commit/1b3bf5d088b7f19ec94947d636b161c15cea0d06) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue ignoring limit causing all cmds to be ran ([eddd01f](https://github.com/sagikimhi/socx-cli/commit/eddd01fe4cf2f8731e18c3df5193ec9ae1033b76) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix issue with reconfigure not overriding old values ([1375123](https://github.com/sagikimhi/socx-cli/commit/137512363db8f12c2ed1b74f509ae5b9e956c947) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add missing log module exports ([78e001e](https://github.com/sagikimhi/socx-cli/commit/78e001e6d066fe627797d6a2f513f2ba0bddfc9a) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add empty __slots__ to protocol classes ([356fdcd](https://github.com/sagikimhi/socx-cli/commit/356fdcdc8122c7db08e1bc3448a7a4f0f98fe77e) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- add return code on exit from main ([8f3eb61](https://github.com/sagikimhi/socx-cli/commit/8f3eb6147e3f70589168609460cb543d7a92d7c9) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- correct dotenv configs ([54f8cf5](https://github.com/sagikimhi/socx-cli/commit/54f8cf52b9f3dbb8f713527dcd9006de8c3a2548) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- fix linter errors ([8207c63](https://github.com/sagikimhi/socx-cli/commit/8207c6342287279f97909eec94c3b79382debd59) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>

### Code Refactoring

- raise exception if start is called on a running test ([520fbd0](https://github.com/sagikimhi/socx-cli/commit/520fbd094b2e13736bc411b6dbbc64858a4a0c18) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename level to get_level, export get_logger ([0b0f41c](https://github.com/sagikimhi/socx-cli/commit/0b0f41cfca7792f503adb12ece74193d11bcccc6) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename _uid to _meta and add singleton metaclass ([d4c8a19](https://github.com/sagikimhi/socx-cli/commit/d4c8a19d2f59d3646c68a77e5a12a1c8ed7c4a90) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
- remove nested sub packages ([41cda37](https://github.com/sagikimhi/socx-cli/commit/41cda37905487be04c579e12ea7d5c6529c60114) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>
- rename package to socx (#5) ([29bdf68](https://github.com/sagikimhi/socx-cli/commit/29bdf682f9e562c7370e6ab8f24eef010b1c07ab) by Sagi Kimhi). Signed-off-by: Sagi Kimhi <sagi.kim5@gmail.com>, Signed-off-by: Sagi Kimhi <sagi.kimhi@wiliot.com>, Co-authored-by: Sagi Kimhi <sagi.kimhi@wiliot.com>
