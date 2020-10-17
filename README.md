# Penn State IEEE Macro Pad

## Circuit
Four buttons connected to pins 2-5 of a Pro Micro. Other Leonardo boards should also work but comptibility has not been tested.

## Sketchgen
This script is designed to build an Arduino sketch from a macro configuration file. A base template file is provided as *base.template*.

```
usage: sketchgen.py [-h] [-b BASEFILE] -o OUTFILE -i INFILE

optional arguments:
  -h, --help            show this help message and exit
  -b BASEFILE, --basefile BASEFILE
                        Specify a different base file

required arguments:
  -o OUTFILE, --outfile OUTFILE
                        Address of file to be created or overwritten
  -i INFILE, --infile INFILE
                        Address of macro config file
```
The macro configuration file uses keywords to describe each of the four macros
```
START [macro]    >> Starts description of a macro with its letter code
END              >> Ends the current macro
HOLD [key(s)]    >> Presses and holds a key or combination of keys
RELEASE [key]    >> Releases a single key held with HOLD
RELEASEALL       >> Releases all keys currently held with HOLD
WAIT [millis]    >> Pauses for some amount of time
DELAY [millis]   >> Alias for WAIT
TYPE [text]      >> Types out a string
COMBO [keys]     >> Presses and releases a key combination
KEY [key]        >> Presses and releases a single key
PRESS [key]      >> Alias for KEY
```
### A few notes
* Codes for non-alphanumeric keys can be found [here](https://www.arduino.cc/en/Reference/KeyboardModifiers)
* Single alphanumeric characters should be surrounded with single quotes. Strings for TYPE must be surrounded with double quotes.
* Combinations of keys should be attached with a '+' (ie. KEY_LEFT_CTRL+'c' for Ctrl+c)
* Any line not starting with a keyword will be ignored
* If you are having trouble getting a more complicated macro to work, delays may help
### Example
I haven't tested this because I am lazy but this should give you an idea of how to put together a simple macro config
```
# undo
START A
COMBO KEY_LEFT_CTRL+'z'
END

# type hello world
START B
TYPE "Hello, World"
END

# open chrome from windows menu
START C
PRESS KEY_LEFT_GUI
WAIT 250
TYPE "chrome"
WAIT 250
PRESS KEY_RETURN
END

# hold the shift key for 10 seconds
START D
HOLD KEY_LEFT_SHIFT
WAIT 10000
RELEASEALL
END
```


**Penn State IEEE 2020-21**

Will McGloughlin
