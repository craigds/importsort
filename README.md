# Decent import sorting for python files.

This is a pre-alpha quality package. It has no pypi release or setup.py yet.
It might break your code. Sorry about that, but your fault for running this really.

The *goal* is to soon be able to sort the top-of-file imports in your python file, with correctness and style

### Usage

Start with code like this:

```python
from __future__ import print_function
import thirdpartylib
import sys
from collections import abc
import os, io

x = 5

import zipfile
```

Then run importsort across it:

```bash
$ ./importsort.py testfile.py
--- testfile.py
+++ testfile.py
@@ -1,8 +1,8 @@
 from __future__ import print_function
-import thirdpartylib
+import io, os
 import sys
 from collections import abc
-import os, io
+import thirdpartylib

 x = 5

```

Now it looks better!

### This might break things!

In python, imports execute code. So if the imports are in a different order, code will run in a different order. This can easily cause import loops and other strange behaviour.

USE THIS AT YOUR OWN RISK.

### TODO

* Add support for whitelisted first-party packages; put first-party modules last.
* Prettier vertical whitespace, especially between blocks of imports.
