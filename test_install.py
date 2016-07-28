import importlib
import sys
from warnings import warn

onpy2 = False

try:
    assert sys.version_info >= (3,0)
    import importlib.util
except AssertionError:
    warn('This workshop uses Python 3. Some pieces of code may break in Python 2.')
    onpy2 = True

def tuple_version(version):
    return tuple(int(x) for x in version.strip('<>+-=.').split('.'))

def check_versions():
    version_trouble=False
    mpl = importlib.import_module('matplotlib')
    mpl_version = tuple_version(mpl.__version__)
    if mpl_version < (1, 5, 0):
        print('Update matplotlib to version 1.5.0 or higher')
        version_trouble=True

    return version_trouble

def main():
    required_modules = ['numpy', 'matplotlib', 'jupyter',
                        'IPython',]
    missing_modules = []
    for mod in required_modules:
        if not onpy2:
            spec = importlib.util.find_spec(mod)
            if spec is None:
                missing_modules.append(mod)
        else:
            try:
                importlib.import_module(mod)
            except ImportError:
                missing_modules.append(mod)

    if missing_modules:
        print('The following modules are required but not installed:')
        print('    {}'.format(', '.join(missing_modules)))
        print('\nYou can install them using conda by running:')
        print('\n    conda install {}'.format(' '.join(missing_modules)))
        print('\nOr you can install them using pip by running:')
        print('\n    pip install {}'.format(' '.join(missing_modules)))
    else:
        if check_versions():
            print('All packages are installed but at least one needs updating. If\
                    you have any questions, do not hesitate to ask Cesar (crocha@ucsd.edu)')
        else:
            print('You are good to go!')

if __name__ == '__main__':
    main()
