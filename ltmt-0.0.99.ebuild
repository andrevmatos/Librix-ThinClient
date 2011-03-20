# Author: Librix Dev Team <tutooprog@las.ic.unicamp.br>

EAPI="3"
PYTHON_DEPEND="3"
inherit distutils python

DESCRIPTION="Librix ThinClient Management Tool"
SRC_URI="http://librixdev.las.ic.unicamp.br/pub/librix-sources/${P}.tar.bz2"
HOMEPAGE="http://librixdev.las.ic.unicamp.br"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="x86 amd64"

RDEPEND=">=dev-lang/python-3.1.1
	>=dev-python/PyQt4-4.8.1
	>=dev-python/lxml-2.2.8
	>=dev-python/argparse-1.0
	>=dev-tcltk/expect-5.43"

DEPEND=">=dev-lang/python-3.1.1
	>=dev-python/PyQt4-4.8.1"

pkg_setup() {
    python_set_active_version 3
}

src_compile() {
	distutils_src_compile
}

src_install() {
	# use distutils to install everything into it's correct path
	distutils_src_install

	# skel's icon
	exeinto /etc/init.d
	doexe ${WORKDIR}/${P}/init.d/ltmt
}

pkg_postinst() {
	distutils_pkg_postinst
	rc-update add ltmt default
}
