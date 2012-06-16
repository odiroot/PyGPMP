# Prepare dependencies for Maemo - as far as possible.
PIP_INSTALL=pip install --upgrade --no-install --build=.
DPKG_BUILD=dpkg-buildpackage -rfakeroot -uc -b -d

# Can be run everywhere
download-sources:
	$(PIP_INSTALL) decorator


# Should be run under scratchbox or on the device.
build-debs: build-decorator

build-decorator:
	cd decorator; $(DPKG_BUILD)
