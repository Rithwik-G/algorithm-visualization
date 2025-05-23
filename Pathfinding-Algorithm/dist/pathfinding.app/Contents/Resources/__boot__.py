def _reset_sys_path():
    # Clear generic sys.path[0]
    import sys
    import os

    resources = os.environ['RESOURCEPATH']
    while sys.path[0] == resources:
        del sys.path[0]


_reset_sys_path()


def _site_packages(prefix, real_prefix, global_site_packages):
    import site
    import sys
    import os

    paths = []

    paths.append(
        os.path.join(
            prefix, 'lib', 'python' + sys.version[:3], 'site-packages'))
    if os.path.join('.framework', '') in os.path.join(prefix, ''):
        home = os.environ.get('HOME')
        if home:
            paths.append(
                os.path.join(
                    home, 'Library', 'Python',
                    sys.version[:3], 'site-packages'))

    # Work around for a misfeature in setuptools: easy_install.pth places
    # site-packages way to early on sys.path and that breaks py2app bundles.
    # NOTE: this is hacks into an undocumented feature of setuptools and
    # might stop to work without warning.
    sys.__egginsert = len(sys.path)

    for path in paths:
        site.addsitedir(path)

    # Ensure that the global site packages get placed on sys.path after
    # the site packages from the virtual environment (this functionality
    # is also in virtualenv)
    sys.__egginsert = len(sys.path)

    if global_site_packages:
        site.addsitedir(
            os.path.join(
                real_prefix, 'lib', 'python' + sys.version[:3],
                'site-packages'))


_site_packages('/Users/rithwikgupta/Documents/Coding/Python/Pathfinding-Algorithm/venv', '/Users/rithwikgupta/opt', 0)

def _chdir_resource():
    import os
    os.chdir(os.environ['RESOURCEPATH'])


_chdir_resource()


def _setup_ctypes():
    from ctypes.macholib import dyld
    import os
    frameworks = os.path.join(os.environ['RESOURCEPATH'], '..', 'Frameworks')
    dyld.DEFAULT_FRAMEWORK_FALLBACK.insert(0, frameworks)
    dyld.DEFAULT_LIBRARY_FALLBACK.insert(0, frameworks)


_setup_ctypes()


def _path_inject(paths):
    import sys
    sys.path[:0] = paths


_path_inject(['/Users/rithwikgupta/Documents/Coding/Python/Pathfinding-Algorithm'])


import re
import sys

cookie_re = re.compile(b"coding[:=]\s*([-\w.]+)")
if sys.version_info[0] == 2:
    default_encoding = 'ascii'
else:
    default_encoding = 'utf-8'


def guess_encoding(fp):
    for i in range(2):
        ln = fp.readline()

        m = cookie_re.search(ln)
        if m is not None:
            return m.group(1).decode('ascii')

    return default_encoding


def _run():
    global __file__
    import os
    import site  # noqa: F401
    sys.frozen = 'macosx_app'

    argv0 = os.path.basename(os.environ['ARGVZERO'])
    script = SCRIPT_MAP.get(argv0, DEFAULT_SCRIPT)  # noqa: F821

    sys.argv[0] = __file__ = script
    if sys.version_info[0] == 2:
        with open(script, 'rU') as fp:
            source = fp.read() + "\n"
    else:
        with open(script, 'rb') as fp:
            encoding = guess_encoding(fp)

        with open(script, 'r', encoding=encoding) as fp:
            source = fp.read() + '\n'

        BOM = b'\xef\xbb\xbf'.decode('utf-8')

        if source.startswith(BOM):
            source = source[1:]

    exec(compile(source, script, 'exec'), globals(), globals())


DEFAULT_SCRIPT='/Users/rithwikgupta/Documents/Coding/Python/Pathfinding-Algorithm/pathfinding.py'
SCRIPT_MAP={}
try:
    _run()
except KeyboardInterrupt:
    pass
