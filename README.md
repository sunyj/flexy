# Flexy – *Flex*ible *Y*AML Loader

Flexy provides lightweight and flexible YAML configs to applications.

**Flexy** is [listed on PyPI](https://pypi.org/project/flexy/).

I created this library in the despair of the fact that YAML's powerful
features (explicit typing, anchors, aliases, etc.) are in fact of little use
to me, as well as in the belief that
[simple is better than complex](https://peps.python.org/pep-0020/).

Hope it makes your life easier too.

## Lightweight

Flexy **ONLY** supports Python built-in types: `dict`, `list`, `str`, `int`,
`float`, `bool`.  Flexy also guarantees that only these types are returned.

## Flexible: file inclusion

Flexy supports non-intrusive file inclusion.  Including entries are written in
a special format in comments, very similar to C/C++ header inclusion.

```YAML
conf: value
...
#include <parallel-conf.yaml>
#include <../another-config.yaml>
#include <~/.config/conf-in-my-home.yml>
#include </absolute/path/to/config.yml>
...
```

Inclusions are expanded as semantic-blind plain texts before sending them to
YAML parser.

## Flexible: variable substitutions

Flexy supports variable substitution with the great power of
[revo](https://github.com/sunyj/revo) ([PyPI](https://pypi.org/project/revo/)).
