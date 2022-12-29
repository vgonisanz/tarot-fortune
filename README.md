<div align="center">

# vgonisanz's Tarot fortune

**DISCLAIMER**: Use for fantasy purposes only.
Translations, interpretations, predictions and other elements used may not correspond to reality.
No warranty of any kind.
Used for programming tinkering
Do not follow to the letter.
Do not rely on predictions.
Danger of death.

</div>

Small python project to do the mythological tarot card divination, but by terminal.

## Usage

TBD

## Features

- Several commands to get fortune, tarot spreads, and utils:
  - cards: List loaded cards
  - celtic-cross: The Celtic Cross spread
  - circle: Circle spread
  - human-body: Tarot spread for the human body
  - life-tree: Tarot spread for the tree of life
  - past-present-future: Past, present, and future spread
  - single: Single card draw
- Only `es` language supported by now.
- render bash *in development*

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

### Utils

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

## License

- [GNU General Public License v3](./LICENSE)
- About the `resources/rider-taite-tarot`:
  The original version of the Rider–Waite Tarot is in the public domain
  in all countries that have a copyright term of 70 years
  or fewer after the death of the last co-author.
  This includes the United Kingdom, where the deck was originally published.
  ~2021/12.
  So belong to the Public Domain.
