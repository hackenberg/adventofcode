day%:
	mkdir $@
	cp -n template.py $@/$@.py
	chmod 755 $@/$@.py
