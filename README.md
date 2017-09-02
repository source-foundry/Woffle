![](https://github.com/source-foundry/Woffle/raw/master/img/logo-head-crunch.png)

## About

Woffle is a GUI application that supports woff and woff2 web font compilation on OS X.  Drag and drop your ttf or otf font file on the GUI window and Woffle does the rest!

Woffle is built with the open source [sfnt2woff-zopfli](https://github.com/bramstein/sfnt2woff-zopfli) and [woff2_compress](https://github.com/google/woff2) font compilers and implements the same web font build approach that we use in [Hack](https://github.com/source-foundry/Hack), all in a tidy little GUI package.

![](https://github.com/source-foundry/Woffle/raw/master/img/woffle.gif)

## Installation

Select either of the following approaches to install Woffle on your OS X system.

### Download and Use the Installer (.dmg)

Download the installer for [the latest release](https://github.com/source-foundry/Woffle/releases/latest).  Double click the installer file and then drag the Woffle icon to the Applications directory when prompted to do so.

Click Launchpad and you will find Woffle on your desktop.

### Clone Repository with git and Install

Use the following commands to pull the Woffle repository to your system and open the repository in your Finder:

```
$ git clone https://github.com/source-foundry/Woffle.git
$ cd Woffle
$ open .
```

Drag and drop Woffle (in the top level of the repository directory) into your Applications directory.

Click Launchpad and you will find Woffle on your desktop.

## Usage

Drag and drop one or more ttf or otf font files onto the Woffle GUI window after you open it.  The compiled woff and woff2 files are located in the directory where your original fonts were located.

## License

Woffle is licensed under the MIT license.

sfnt2woff-zopfli is licensed under the Apache and Mozilla Public licenses

woff2_compress is licensed under the Apache license.

See [LICENSE.md](https://github.com/source-foundry/Woffle/blob/master/LICENSE.md) for details.

