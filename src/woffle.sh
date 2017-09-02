#!/bin/sh

WOFFLE_TITLE="

██╗    ██╗ ██████╗ ███████╗███████╗██╗     ███████╗
██║    ██║██╔═══██╗██╔════╝██╔════╝██║     ██╔════╝
██║ █╗ ██║██║   ██║█████╗  █████╗  ██║     █████╗
██║███╗██║██║   ██║██╔══╝  ██╔══╝  ██║     ██╔══╝
╚███╔███╔╝╚██████╔╝██║     ██║     ███████╗███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝

                                            v0.9.0"


SUCCESS_THUMB="
┈┈┈┈┈┈▕▔╲
┈┈┈┈┈┈┈▏▕
┈┈┈┈┈┈┈▏▕▂▂▂
▂▂▂▂▂▂╱┈▕▂▂▂▏
▉▉▉▉▉┈┈┈▕▂▂▂▏
▉▉▉▉▉┈┈┈▕▂▂▂▏
▔▔▔▔▔▔╲▂▕▂▂▂▏
"

SFNTWOFF_BIN="./sfnt2woff-zopfli"
ZOPFLI_ITERATIONS="3"

WOFF2_BIN="./woff2_compress"

# Message on application open (no arguments passed to script on initial open)
if [ $# -eq 0 ]; then
	echo " "
	echo " "
	printf "%s\n" "$WOFFLE_TITLE"
	echo "woff and woff2 web font generator"
	echo "Built with sfnt2woff-zopfli and woff2 compilers"
	echo "======================================================"
	echo "Copyright 2017 Christopher Simpkins"
	echo "MIT License"
	echo "Source: github.com/source-foundry/Woffle"
	echo "Issues: github.com/source-foundry/Woffle/issues"
	echo "======================================================"
	echo " "
	echo "Drag and drop your ttf or otf files on this window to begin."
fi

# test file extensions to confirm dealing with appropriate font files
for FONTPATH in "$@"
do
	FILE_EXTENSION="${FONTPATH##*.}"
	if [ "$FILE_EXTENSION" = "ttf" ] || [ "$FILE_EXTENSION" = "otf" ]; then
		echo " " >/dev/null  # do nothing...
	else
		echo " "
		echo "ERROR: You appear to have dropped a file on the window that is not a ttf or otf font.  Please try again."
	   	exit
	fi
done


# woff compilation

if [ $# -eq 1 ]; then
	echo "===> Beginning compilation of woff file..."
	echo " "
elif [ $# -gt 1 ]; then
	echo "===> Beginning compilation of woff files..."
	echo " "
fi

for FONTPATH in "$@"
do
	FILE_EXTENSION="${FONTPATH##*.}"
	if ! "$SFNTWOFF_BIN" -n $ZOPFLI_ITERATIONS "$FONTPATH" 2>&1 >/dev/null; then
		echo "ERROR: Unable to build woff from $FONTPATH." 1>&2
		exit
	else
		echo "[NEW] ${FONTPATH%.*}.woff"
		echo " "
	fi
done


# woff2 compilation

if [ $# -eq 1 ]; then
	echo "===> Beginning compilation of woff2 file..."
	echo " "
elif [ $# -gt 1 ]; then
	echo "===> Beginning compilation of woff2 files..."
	echo " "
fi

for FONTPATH in "$@"
do
	if ! "$WOFF2_BIN" "$FONTPATH" >/dev/null 2>&1; then
		echo "ERROR: Unable to build woff2 from $FONTPATH." 1>&2
		exit
	else
		echo "[NEW] ${FONTPATH%.*}.woff2"
		echo " "
	fi
done

if [ $# -gt 0 ]; then
	echo " "
	echo "✓ Complete!"
	echo " "
	printf "%s\n" "$SUCCESS_THUMB"
fi
