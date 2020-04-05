# megachonker
Use `megachonker` for optimizing the backup of large files. 

Installation command  `sudo pip install megachonker`

## usage
```
usage: megachonker [-h] [-q] in_file out_file

Use megachonker for optimizing the backup of large files. megachonker dissects
in_file into 1MB chunks and hashes each chunk. Each hash is then compared to a
hash for the respective chunk in out_file. The chunk gets copied into out_file
if hashes differ. A file <out_file>.hashes will be stored alongside out_file.
megachonker copies all file attributes of in_file to out_file. If in_file and
out_file have identical modification times then megachonker does nothing.

positional arguments:
  in_file      This is the file to be chunked, hashed and copied
  out_file     This is the backed up version of the file

optional arguments:
  -h, --help   show this help message and exit
  -q, --quiet  Do not show any output.

```
