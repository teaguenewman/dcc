ABOUT
-----

Default configuration changer is a small program that interfaces with 'Conpot's <http://github.com/glastopf/conpot/>' default configuration file. Default configuration changer, changes specific values in Conpot's default.xml file, so that the honeypot will have random values populated. The values that are changed are the facility name "Mouser Factory", the system name "Technodrome", the system location "Venus", and the serial number "88111222". After the default configuration changer is run, conpot will now start with random values. A random facility name will be created of one, two, or three words in length, and will be a logical sounding name. The system name will be one or two words and will be either a number (typed or numeric), a device name (pump, etc), or a combination of both. The system location will be a randomly chosen city name from the most populous cities in the world. The serial number will be a randomly generated 8 digit number. Any words used in the newly created values will have randomly capitalized first letters for any word.

The idea of this project is to vary the look of the conpot deployments running, so that they are not as easily identifiable as a honeypot. If they appear different, they are more likely to receive valid attacks, rather than being ignored because they appear obviously as a honeypot.

DOCUMENTATION
-------------

Extract all files to the conpot directory that default.xml is run from (usually /opt/conpot/conpot/templates/default.xml). Run conpot and see first line after startup to see where it was loaded from. Once extracted run default_configuration_changer.py. After running default_configuration_changer.py, conpot will now run with the random values that were created instead of using the default configuration values.

You may use a custom file by supplying your own dictionary file and replacing the existing ones. The names must be the same, and the file must be under 256MB.

USAGE
-------

python default_configuration_changer.py


SUPPORT
-------

Thanks to my brother for his help and input!

SAMPLE OUTPUT
-------------

.. code-block:: shell

	default.xml renamed to default_original.xml
	changes have now been written to default.xml
	Mouser Factory changed to Thomas construction corp
	Technodrome changed to 13
	Venus changed to Qingdao
	88111222 changed to 16111452

