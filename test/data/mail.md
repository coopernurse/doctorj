
mail api
==========

[TOC]

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

some other stuff
