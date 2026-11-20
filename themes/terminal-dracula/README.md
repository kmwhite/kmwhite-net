# Terminal Dracula

A Hugo theme component for [Terminal](https://github.com/panr/hugo-theme-terminal) (v4) that gives you:

- **Page:** Terminal.css's "Black & White" preset (`#000000` background, `#ffffff` text and accent)
- **Code blocks:** the [Dracula](https://draculatheme.com) syntax colors, with token mapping taken from the official `dracula/pygments` style (Chroma uses the same token classes)

It doesn't fork Terminal. It only replaces two of its stylesheets with files of the same name, so you can keep updating Terminal as normal.

## Files

```
terminal-dracula/
├── assets/css/terminal.css   # Black & White colors (replaces Terminal's empty placeholder)
├── assets/css/syntax.css     # Dracula code blocks (replaces Terminal's monotone syntax.css)
├── hugo.toml                 # markup.highlight defaults
└── theme.toml
```

## Install

1. Copy `terminal-dracula/` into your site's `themes/` folder, next to `terminal/`.
2. In your site's `hugo.toml`, list it **before** `terminal` (the leftmost theme wins):

   ```toml
   theme = ["terminal-dracula", "terminal"]

   [markup.highlight]
     noClasses = false   # required, or Chroma writes inline styles and ignores syntax.css
   ```

3. Remove `static/terminal.css` from your site if you have one, because it loads last and would override these colors.
4. Run `hugo server` and open a post that has a fenced code block with a language, such as ```` ```go ````.

### Using Hugo Modules instead

If you load Terminal as a module, import this component first:

```toml
[module]
  [[module.imports]]
    path = "terminal-dracula"          # or its git path, if you push it to a repo
  [[module.imports]]
    path = "github.com/panr/hugo-theme-terminal/v4"
```

## Customizing

All Dracula colors are CSS variables at the top of `syntax.css` (`--dracula-pink`, `--dracula-comment`, and so on). Some options:

- **Dracula for inline code too.** Add this to `syntax.css`:
  `:not(pre) > code { color: var(--dracula-pink); background: var(--dracula-background); }`
- **Line numbers.** Set `lineNos = true` under `[markup.highlight]`, or use ```` ```go {linenos=true} ```` on a single block.
- **Highlighted lines.** Use ```` ```go {hl_lines=[2,3]} ````. These lines get Dracula's current-line color, `#44475a`.
