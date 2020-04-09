# ji-helper

_Mattias Hållsten 2020_

## Usage

``` bash
$ python3 ji-helper.py -f <commands> -r <ratios>
```

The ratios must be supplied with a forward slash, i.e `5/4` or
`9/8`. The commands are single-character, and will be executed in the
order that they come. For example, using `fm` as a command will _not_
be the same as `mf`.

## Commands

### `m`

Minimizes, or simplifies, the ratio. For example, `10/8` would become
5/4. This is handy for finding out the interval between two
frequencies.

### `f`

Forces the ratio into the octave. For example, `10/4` would become
`5/4`.

### `M`

Multiplies the ratios with one another, and results in one remaining
ratio.

### `D`

Divides the ratios (finding the internal intervals), resulting in one
less ratio in total.

### `a`

Approximates the interval being played by a 24EDO scale.
