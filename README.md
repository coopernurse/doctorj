# doctorj: JSON messaging doc generator #

## motivation ##

I like building systems made up of loosely coupled components that send messages to each other.  There's a bunch of ways to serialize messages these days.

I like using JSON for message serialization.  It's cross-language, it expresses lists and maps in a human readable manner.  Javascript likes it. There's no tooling to setup.

The downside is that it's hard to document your JSON APIs once you have something you like.  Validating incoming messages is also a pain.  Lots of boilerplate.

JSON schema can help with the validation problem.  But writing JSON schema files by hand is a drag.

Orderly simplifies writing JSON schema, but you have to write individual files for each message.  My APIs may have 20-30 operations.  That's a lot of files!

I wanted to write one Markdown file to document my API and have it generate  a human readable HTML doc and JSON schema files I can use to validate messages in my app.  

That's what doctorj does.

## tl;dr ##

* Write one Markdown file to document your JSON API.  
 * Inline Orderly blocks per-message you wish to document
* Run doctorj
* Get a human readable API doc in HTML format
* Get a JSON schema file for each Orderly block

## example ##

Say you have this Markdown file:

    foo api
    ==========

    [TOC]

    ## overview ##

    The foo system lets you do great things.

    ## messages ##

    ### message: foo_request ###

    ~~~~{.orderly}
    object {
      string name;
      string description?;
      string homepage /^http:/;
      integer {1500,3000} invented;
    }*;
    ~~~~

    ### message: foo_response ###

    ~~~~{.orderly}
    object {
      string status;
      string description?;
    }*;
    ~~~~

And you run doctorj:

    src/doctorj.py foo.md \
         --outdir=out \
         --orderly=/Users/james/bitmechanic/orderly.js/bin/node-orderly2jsonschema \
         --clean

Then in the `out` dir you'll find:

    out/
        foo.html
        foo_request.json
        foo_response.json
        
## dependencies ##

You need to install some stuff:

    pip install markdown
    git clone git@github.com:coopernurse/orderly.js.git
    install a recent version of node (tested with 0.4.8 on macos)
    
Sorry, the node/orderly.js dependency is a drag.  The C version of orderly wasn't
working for me.

## reference ##

### syntax in markdown file ###

* In your Markdown file use `~~~~{.orderly}` to start an orderly block
* Each block *must* be preceeded by: `message: [name]`
 * [name] is used to name the generated `.json` files
 * In the above example, `message: foo_response` becomes `out/foo_response.json`
 
### html templates ###

* Use the `--template` switch to tell doctorj to use your HTML template file when merging in the Markdown output
* If you omit this switch, a hardcoded template will be used (see `doctorj.py` to view it)
* Currently templates can contain two tokens:
 * `{{ CONTENT }}` - Will be replaced with the output from your `.md` file
 * `{{ DATE }}` - Will be replaced with the current date/time

### clean ###

* Use the `--clean` switch to tell doctorj to remove all files in your `--outdir` directory before generating new output
