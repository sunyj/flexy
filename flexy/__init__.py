################################################################################
# flexy --- flexible YAML loader
################################################################################
import re, revo, yaml
from pathlib import Path


def load(yaml_file, overrides=None):
    content = '\n'.join(expand_includes(yaml_file))
    return revo.Revo(yaml.safe_load(content), overrides).val.copy()


def expand_includes(fname, spec=r'^#\s*include\s+<(.+)>$'):
    lines = []
    path = Path(fname).expanduser()
    with open(path) as f:
        for line in f:
            mo = re.match(spec, line.strip())
            if not mo:
                lines.append(line.rstrip())
                continue
            ref = mo.group(1)
            if ref[0] not in '~/':
                ref = path.parent / ref
            else:
                ref = Path(ref).expanduser()
            if not ref.exists():
                raise RuntimeError(f'{ref} not found! (included from {path})')
            lines += expand_includes(ref, spec=spec)
    return lines

### flexy/__init__.py ends here
