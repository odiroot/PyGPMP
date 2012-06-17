# Prepare dependencies for Maemo - as far as possible.
PIP_INSTALL=pip install --upgrade --force-reinstall --no-deps --no-install --build=.
DPKG_BUILD=dpkg-buildpackage -rfakeroot -uc -b -d

# Can be run everywhere
download-sources:
	$(PIP_INSTALL) decorator
	$(PIP_INSTALL) validictory==0.7.2



# Should be run under scratchbox or on the device.
# Running on desktop system will produce incompatible packages.
build-debs: build-decorator build-validictory

build-decorator:
	cd decorator; $(DPKG_BUILD)

build-validictory:
	cd validictory; $(DPKG_BUILD)
