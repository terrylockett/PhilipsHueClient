# PhilipsHueClient
quick and dirty tool to toggle me lights.

UI doesn't work.. cli works for me anyway.

## Pre reqs:
- pip install pyyaml
- pip install requests
- pip install keyring

## Setup
- get a 'username' as outlined here:
https://developers.meethue.com/develop/get-started-2/
- run `phue config`
- enter the IP of the bridge.. make it static
- enter in the 'username'
- GG


## Usage:
<pre>
$phue lights [OPTION]
or
$phue groups [OPTION]


-l 		List
-e [ID]		Enable
-d [ID]		Disable
-t [ID]		Toggle
</pre>
