<div align="center">

# vgonisanz's Tarot fortune

Small python project to do the mythological tarot card divination,
but by terminal.

</div>

- **DISCLAIMER**: Use for fantasy purposes only.
    Translations, interpretations, predictions and other elements used may not correspond to reality.
    No warranty of any kind.
    Used for programming tinkering
    Do not follow to the letter.
    Do not rely on predictions.
    Danger of death.
- If you think this is all claptrap,
  you may or may not be right.
  But as a programming practice it is interesting.
  Don't you think?
  Surely you are a [skeptic](https://en.wikipedia.org/wiki/Skepticism).
  Congratulations.
- If not, you are probably right and want to pay for my children's college.
  You can send me money and I'll schedule some more moves for you.
  Thanks for being such a [Parasychologist](https://en.wikipedia.org/wiki/Parapsychology)

## Features

- Several commands to get fortune, tarot spreads, and utils:
  - cards: List loaded cards
  - celtic-cross: The Celtic Cross spread
  - circle: Circle spread
  - human-body: Tarot spread for the human body
  - life-tree: Tarot spread for the tree of life
  - past-present-future: Past, present, and future spread
  - single: Single card draw
- Card bash rendering.
- Only `es` language supported by now.

### TODO

- Multilanguage.
- Mkdocs wiki.
- Github CI/CD
- Fastapi server.
- Telegram bot server.
- Pypi publish.
- IA conversation support.
- Testing.

## Usage

TBD

## Development

To start developing this project, clone this repo and do:

```bash
make env-create
```

This will create a virtual environment with all the needed dependencies
(using [tox](https://tox.readthedocs.io/en/latest/)).
You can activate this environment with:

```bash
source ./.tox/tarot_fortune/bin/activate
```

Then, you can run `make help`.
Learn more about the different tasks
you can perform on this project using [make](https://www.gnu.org/software/make/).

### Extra Utils

These files are not included in the distributable.
You can use to do additional development tasks:

- card-term-viewer: It is a helper to render in terminal images.
  That could help in development.
- tarot_csv_to_json: This is a CSV to JSON converter to ease data exchange.

### Upgrade dependencies

From scratch, use the following command to generate `requirements{-dev}.txt` files:

```bash
make env-compile
```

## Contributing

Please see the [Contributing Guidelines](./CONTRIBUTING.md) section for more details on how you can contribute to this project.

## Dependencies

- [Term image](https://github.com/AnonymouX47/term-image): Still in development,
  It is a good dependency to render in terminal.
  Maybe in the future will add more interesting features (like flip or rotate)
- Other alternatives like [imgrender](https://github.com/djentleman/imgrender)
  can be used to this purpose.
- Pydantic, typer, rich and structlog are classics.

## License

- [GNU General Public License v3](./LICENSE)
- About the `resources/rider-taite-tarot`:
  The original version of the Rider–Waite Tarot is in the public domain
  in all countries that have a copyright term of 70 years
  or fewer after the death of the last co-author.
  This includes the United Kingdom, where the deck was originally published.
  ~2021/12.
  So belong to the Public Domain.
