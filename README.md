# Firefox vertical tabs

![vertical-tabs-demo-cut](https://github.com/lucaspar/firefox-vertical-tabs/assets/7535699/62239850-2f2a-4a06-86f4-59019a976900)

> [!TIP]
>
> If using Firefox 137, upgrade it to 138. Alternatively, go to `about:config`, set `sidebar.visibility` to `expand-on-hover`.

## Setting it up

0. Install the [Sidebery extension](https://addons.mozilla.org/en-US/firefox/addon/sidebery/).
1. In Sidebery settings:
    1. Set the title preface must as `"[S] "` (without quotes, trailing space is optional but makes titles more readable).
        This is used by CSS rules below to identify when Sidebery is active.
    2. Set 'Tabs tree structure' to `false` -- this stylesheet doesn't adapt to
        multiple tab levels, but feel free to tweak it!
    3. Copy and paste the `SIDEBERY STYLES` section in the [userChrome.css](./userChrome.css) to
        Sidebery's Styles Editor → Sidebar.
    4. Optionally sync Sidebery settings to Firefox account to get other customizations.
2. Go to `about:support` → copy the 'Profile Directory' location, setting it as the variable `FF_USER_DIR`: `FF_USER_DIR="/path/to/profile/dir"`.
3. Move CSS files to FF user location:
    + `mkdir -p "${FF_USER_DIR}/chrome"`
    + `mv userChrome.css "${FF_USER_DIR}/chrome/userChrome.css"`
    + `mv userContent.css "${FF_USER_DIR}/chrome/userContent.css"`
4. Go to `about:config` → `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`.
5. Restart Firefox (`about:restartrequired` to reopen your current tabs).

## Tweaking and Debugging

### How to inspect the browser interface

> [Source](https://superuser.com/questions/1608096/how-to-inspect-firefoxs-ui)

1. Enable the Browser Toolbox

    Press `F12` to open the Page Inspector.

    > Alternate: Right click the page then `Inspect Element (Q)`.

    Press `F1` to open the Page Inspector Settings.

    > Alternate: In the top right of the Page Inspector next to the close button; press the `⋯` button, then `Settings`.

    Ensure the following settings are checked:

    + `Enable Browser chrome and add-on debugging toolbox`
    + `Enable remote debugging`

2. Open the Browser Toolbox

    Press `Ctrl`+`Alt`+`Shift`+`I`

    > Alternate: Press `Alt` on the keyboard to bring the window menu → `Tools` → `Web Developer` → `Browser Toolbox`.

### How to inspect extensions interface

You can use the [Browser Toolbox](#how-to-inspect-the-browser-interface) to inspect extensions, or do it through `about:debugging`:

1. Navigate to `about:debugging`.
2. Go to the `This Firefox` page.
3. Find the extension you want to inspect.
4. Press `Inspect` and a console window should open.
5. Change *`targeted iframe`* if needed by clicking the blue "layout" icon
    in the upper right corner, located close to the ellipsis menu icon.

## Resources

+ [Firefox release notes](https://www.mozilla.org/en-US/firefox/releasenotes/)
+ [Firefox source code (GitHub mirror)](https://github.com/mozilla/gecko-dev/)
