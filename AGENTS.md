This repository uses [Pixi](https://prefix.dev/pixi/) to manage dependencies.
Always invoke commands through `pixi run` so they use the correct environment.

The `dev` environment contains the `s2fft` git dependency used in the tests.
Run tests with:

```
pixi run --environment dev pytest
```

or simply `pixi run test`. Add `--frozen` to reuse the existing environment
without reinstalling packages each time.

You can also start a shell in the `dev` environment and execute commands there:

```
pixi shell --environment dev
```
