<div align="center">

# vgonisanz's Tarot fortune

</div>

## Usage

TBD

## Features

- Single card selection usable.
- es language supported only.
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
$ source ./.tox/tarot_fortune/bin/activate
```

Then, you can run `make help`.
Learn more about the different tasks
you can perform on this project using [make](https://www.gnu.org/software/make/).

### Upgrade dependencies

From scratch, use the following command to generate `requirements{-dev}.txt` files:

```bash
make env-compile
```

## Contributing

Please see the [Contributing Guidelines](./CONTRIBUTING.md) section for more details on how you can contribute to this project.

## License

[GNU General Public License v3](./LICENSE)
