---
titel: Magic Mirror Voice Control skill
description: 
---
This mycroft skill passes commands to a MagicMirror installed on a Raspberry Pi. It requires a working install of [MagicMirror](https://github.com/MichMich/MagicMirror) and the [MMM-Remote-Control module](https://github.com/Jopyth/MMM-Remote-Control) must be installed AND ACCESSIBLE ON YOUR LOCAL NETWORK.

This skill requires MMM-Remote-Control be installed and working properly.

You must configure the MagicMirror's config.js file to properly whitelist the ip address of your Mycroft.

You can use this skill to hide or show modules, update the mirror or individual modules,
refresh or restart the mirror, list installed modules, install modules by name (will still require you
to configure the MagicMirror config.js by SSH or VNC), change pages of modules by either swipe commands
or telling mycroft to "go to page [number]"(requires that [MMM-pages](https://github.com/edward-shen/MMM-pages)
be installed), restart or reboot the Raspberry Pi.

MMM-Remote-Control requires the module identifier to know which module to
perform ModuleActionKeywords on (HIDE|SHOW) for example. This skill parses the MODULE_DATA returned from
the MMM-Remote-Control and compares it to the file "AvailableModules.json"
It then creates another file called file "AvailableModulesWithIdentifier.json"
to store the module identifier that matches the ModuleKeywords. Modules identifiers may change
depending on their order in the MagicMirror config.js file. Everytime you install a new module
the module identifiers may change. If you run into issues, restart MagicMirror and Mycroft,
and this skill should update the changed module identifiers. Just be aware after installing new modules
and updating the config.js file that voice commands may not work properly until you restart both
MagicMirror and Mycroft.

To match what Mycroft hears to a module, for instance a user would say
'weather' but if MMM-WunderGround is installed and displayed, it would be considered the "weather" module.
These adjustments are made by changing the "mycroftname" in the file "AvailableModules.json"
For example: search for "weather" in the file "AvailableModules.json" and change it's
mycroftname to something other than weather like 'weather old' or 'current weather'.
Then search for MMM-Wunderground and change it's mycroftname to 'weather'. The change must be
to a module name that is also reflected in the ModuleKeywords.voc otherwise mycroft will not recognize the name.
For your changes to persist all modifications should be made to the file "AvailableModules.json"

The way this skill works is by requests.get(url,params) sending a get request to the MMM-Remote-Control module via
url for example 'http://localhost:8080/remote?action=someaction&param=someparameter'

This skill includes intents for 90% of what the MMM-Remote-Control module is capable of doing. The other 10% is a work in progress.
