# Prepare dependencies for Maemo - as far as possible.
PIP_INSTALL=pip install --upgrade --force-reinstall --no-deps --no-install --build=.
DPKG_BUILD=dpkg-buildpackage -rfakeroot -uc -b -d

# Can be run everywhere
download-sources:
	$(PIP_INSTALL) decorator
	$(PIP_INSTALL) validictory==0.7.2
	$(PIP_INSTALL) mutagen
	$(PIP_INSTALL) "https://github.com/odiroot/Unofficial-Google-Music-API/zipball/master#egg=gmusicapi"
	$(PIP_INSTALL) chardet


# Should be run under scratchbox or on the device.
# Running on desktop system will produce incompatible packages.
build-debs: build-decorator build-validictory build-mutagen build-gmusicapi build-chardet

build-decorator:
	cd decorator; $(DPKG_BUILD)

build-validictory:
	cd validictory; $(DPKG_BUILD)

build-mutagen:
	cd mutagen; $(DPKG_BUILD)

build-gmusicapi:
	cd gmusicapi; $(DPKG_BUILD)

build-chardet:
	cd chardet; $(DPKG_BUILD)
