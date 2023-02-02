# hyde-gemini

Serve your [Hyde](https://hyde.github.io/) site over
[Gemini](https://gemini.circumlunar.space/).

## Installation

<!-- ### Release

You can install the latest relase from PyPI by running

```shell
python3 -m pip install hyde-gemini
``` -->

### From source

If you want to use the latest development snapshot (which may be broken),
you'll need to clone or download the repository and then install the package with:

```shell
python3 -m pip install .
```

If you don't want to install anything, you can replace `hyde-gemini` with
`python3 -m hyde_gemini.main` in the following steps.

## Usage

### Setup

There are a few things you might want to configure but don't have to.

To do so, add the following lines to your `site.yaml`:

```yaml
gemini_layout_root: layout_gemini # this is the default
```

If you don't want to create your layout from scratch you can use a bundled one
 – to do so, run `hyde-gemini init`.

### Serve

You can use the built-in webserver for a quick test
 – and also for pre-viewing your site while editing it.

To do so, run `hyde-gemini serve`.

Per default, this will serve the site from the current working directory
at <gemini://localhost/>, placing generated files into `deploy_gemini/`.
(You can change this, see `hyde-gemini -h` and `hyde-gemini serve -h` for more options.)

### Generate

The primary purpose of hyde-gemini is to generate a static site (just like hyde's).

To do so, run `hyde-gemini gen`.

Per default, this will generate a static version of the site from the current
working directory to the folder `deploy_gemini/`.
(You can change this, see `hyde-gemini -h` and `hyde-gemini gen -h` for more options.)

## Knonwn issues / TODO

 * it doesn't actually work yet
 * just HTML files, binaries and folders are considered

## Gotchas

hyde-gemini needs Python >= 3.6.

The currenty stable release of hyde (0.8.9) needs Python < 3.
You'll need to install the pre-release of hyde 0.9.0 to get this working:

```shell
python3 -m pip install git+https://github.com/hyde/hyde.git@V0.9.0
```
