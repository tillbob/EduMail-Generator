import subprocess
import sys


def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])


def main():
    my_packages = ['requests', 'clint', 'faker', 'selenium>=4.20,<5', 'colorama']

    installed_pr = []

    for package in my_packages:
        install(package)
        print('\n')

    print('Setup complete.')
    print('Create prefBrowser.txt with either:')
    print('  chrome')
    print('  firefox')


if __name__ == '__main__':
    main()
