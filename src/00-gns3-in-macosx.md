date: 2011-08-08
Title: Installing GNS3 in Mac OS X
Category: networking
Tags: shell, mac, gns3

Some coworkers wanted to be able to emulate Networking hardware so I scripted up this installer. If anyone uses it, let me know how it goes for them.

	#!/usr/bin/env bash
	
	# When compiling code, we need to ensure that all libraries compiled by,
	# and for, MacPorts are available to the compiler. The below does that,
	# and in turn, fixes the 'Cannot find file: gnutls/gnutls.h header'
	# error message
	export CFLAGS='-I/opt/local/include'
	
	# Colors make the world a happier place
	if [ $TERM == 'xterm' ]; then
	  export TERM='xterm-color'
	fi
	
	# To make this easier to follow, we're going to define some functions to
	# colorize the text as we see fit:
	function warning() {
	  echo -e "\033[1;33m${1}\033[0m"
	}
	function success() {
	  echo -e "\033[1;32m${1}\033[0m"
	}
	function error() {
	  echo -e "\033[1;31m${1}\033[0m"
	} 
	
	SUDO_BIN="$(which sudo)"
	PORT_BIN="$(which port)"
	CURL_BIN="$(which curl)"
	QEMU_BIN="$(which qemu)"
	QEMU_OPTS='install'
	QEMU_VERSION='0.11.0'
	QEMU_MIRROR='http://download.savannah.gnu.org/releases-redirect/qemu'
	QEMU_SRC='http://downloads.sourceforge.net/gns-3'
	GNS_VERSION='0.7.4'
	GNS_MIRROR='http://downloads.sourceforge.net/gns-3'
	GNS_ARCH='intel-x86_64'
	
	# NOTE: Original version constraints:
	#sudo $PORT_BIN install py26-sip @4.9.3_0
	#sudo $PORT_BIN install py26-pyqt4 @4.6.2_0
	#sudo $PORT_BIN install qt4-mac @4.5.3_0
	PORT_PKG_LIST=( python26 python_select py26-sip py26-pyqt4 qt4-mac zlib libpcap )
	
	if [ "${SUDO_BIN}x" == 'x' ]; then
	  error 'Sudo is not installed. Refusing to continue'
	  exit 255
	fi
	
	echo ''
	echo 'Beginning the installation of GNS3 on Mac OS X. This'
	echo "is $(error 'BETA') code, so \"Hold on to your butts!\""
	echo "as Samuel L. Jackson would say! $(warning 'If you do not want')"
	warning 'to run this, please press CTRL+C in the next 10 seconds'
	echo ''
	sleep 10
	
	if [ "${PORT_BIN}x" != 'x' ] && [ -x $PORT_BIN ]; then
	  success 'Ports are found to be installed. Installing support libraries...'
	  set -e
	  for PORT in ${PORT_PKG_LIST[*]}; do
	    warning "Installing ${PORT}..."
	    sleep 3
	    $SUDO_BIN $PORT_BIN $QEMU_OPTS $PORT
	  done
	  set +e
	  PYHON_SELECT_BIN=$(which python_select)
	  if [ "${PYTHON_SELECT_BIN}x" != 'x' ] && [ -x ${PYTHON_SELECT_BIN} ]; then
	    $SUDO_BIN $PYTHON_SELECT_BIN python26
	    success 'If you are seeing this, all ports should have installed correctly!'
	    success 'Let us move on, shall we?'
	  else
	#    error 'python_select is NOT installed! Please investigate.'
	#    exit 1
	    error 'ERROR: python_select cannot be found. Alas, this is not the end of the world'
	    error 'The install should continue fine. Carrying on...'
	  fi
	else
	  error 'MacPorts are not installed or are not available to the current user'
	  exit 2
	fi
	
	# The very awkward install block for QEmu
	# setting '-e' to bail on error
	if ! [ "${QEMU_BIN}x" != 'x' ] && [ -x $QEMU_BIN ]; then
	  cd /tmp
	  curl -L ${QEMU_MIRROR}/qemu-${QEMU_VERSION}.tar.gz -o qemu-${QEMU_VERSION}.tar.gz
	  if [ -e qemu-${QEMU_VERSION}.tar.gz]; then
	    tar xvf qemu-${QEMU_VERSION}.tar.gz
	    cd qemu-${QEMU_VERSION}
	    curl -L ${QEMU_SRC}/qemu-${QEMU_VERSION}-macosx.patch?download -o qemu-${QEMU_VERSION}-macosx.patch
	    if [ -e qemu-${QEMU_VERSION}-macosx.patch ]; then
	      patch -p1 -i qemu-${QEMU_VERSION}-macosx.patch
	    else
	      error 'Failed to download the -macosx patch! Check your internet or URL'
	      exit 3
	    fi
	    curl -L ${QEMU_SRC}/qemu-${QEMU_VERSION}-olive.patch?download -o qemu-${QEMU_VERSION}-olive.patch
	    if [ -e qemu-${QEMU_VERSION}-olive.patch ]; then
	      patch -p1 -i qemu-${QEMU_VERSION}-olive.patch
	    else
	      error 'Failed to download the -olive patch! Check your internet or URL'
	      exit 4
	    fi
	    ./configure --disable-aio --disable-kvm --disable-kqemu --disable-sdl --target-list=i386-softmmu
	    make
	    ${SUDO_BIN} make install
	    if ! [ -x $(which qemu) ]; then
	      error 'QEmu failed to install! Please report problems to me@kmwhite.net'
	      exit 5
	    fi
	  else
	    error 'Downloading QEmu failed! Check your internet connection!'
	    exit 6
	  fi
	else
	  warning 'QEmu is already installed! Skipping installation.'
	fi
	
	warning 'Downloading GNS3 for installation...'
	curl -L ${GNS_MIRROR}/GNS3-${GNS_VERSION}-${GNS_ARCH}.dmg?download -o gns3-${GNS_VERSION}.dmg
	if [ -e gns3-${GNS_VERSION}.dmg ]; then
	  success 'Success downloading GNS3! Opening for installation...'
	  open gns3-${GNS_VERSION}.dmg
	else
	  error 'Failure to download GNS3 correctly! Please check your internet connection or mirror'
	  exit 7
	fi
	
	success 'Installation complete!'
	success 'Please follow the instructions at http://ng.networkfoo.org/cisco-articles/running-cisco-asa-firewall-gns3-os-x for configuration!'
	exit 0

