# list installed packages
apt list --installed

# show why a package is installed
apt-cache rdepends --installed --recurse <packagename>
