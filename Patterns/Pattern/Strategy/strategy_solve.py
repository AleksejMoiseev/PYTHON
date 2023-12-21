from abc import ABC, abstractmethod


class Installer:
    def install(self, strategy: 'OS', package):
        strategy.install(package=package)


class OS(ABC):
    @abstractmethod
    def install(self, package):
        pass


class Ubuntu(OS):

    def __init__(self, version):
        self.version = version

    def install(self, package):
        print(f"in Ubuntu installed  {package} package")


class CentOS(OS):
    def __init__(self, version):
        self.version = version

    def install(self, package):
        print(f"in CentOS installed  {package} package")


if __name__ == '__main__':
    installer = Installer()
    ubuntu = Ubuntu(version=16)
    installer.install(strategy=ubuntu, package='PyTest')
    cent_os = CentOS(version=20)
    installer.install(strategy=cent_os, package='Django')