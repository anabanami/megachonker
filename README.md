# megachonker
Use `megachonker` for optimizing the backup of large files. 

Requires the `tqdm` python package: `pip3 install tqdm`

## usage
```
usage: megachonker [-h] [-q] in_file out_file

Use megachonker for optimizing the backup of large files. megachonker dissects large
file objects into 1MB chunks and it hashes each chunk. Each hash is then
compared to a hash for the respective chunk in the previous version of the
file. The chunk gets copied into the old file and backed up iff hashes differ.
A file <out_file>.hashes will be stored alongside the backed up file.

positional arguments:
  in_file      This is the file to be chunked, hashed and copied
  out_file     This is the backed up version of the file

optional arguments:
  -h, --help   show this help message and exit
  -q, --quiet  Do not show any output.
  ```
