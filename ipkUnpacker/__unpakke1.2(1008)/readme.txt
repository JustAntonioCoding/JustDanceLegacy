--------------------------------------------------------------------------------

                ____ ___                    __    __
               |    |   \____ ___________  |  | _|  | __ ____
               |    |   /    \\____ \__  \ |  |/ /  |/ // __ \
               |    |  /   |  \  |_> > __ \|    <|    <\  ___/
               |______/|___|  /   __(____  /__|_ \__|_ \\___  >
                            \/|__|       \/     \/    \/    \/

--------------------------------------------------------------------------------

 Run unpakke.exe without parameters to start it as GUI or unpakke.exe /? to get
 command line (CLI) help.

 You can find additional help here:
   http://nullsecurity.org/unpakke/sdk/

 Latest version can be found here:
   http://nullsecurity.org/unpakke/

 You might also like to visit the forums here:
   http://nullsecurity.org/forum/

 If you like to pat me on the back or throw some curses, do it here:
   xpozed@nullsecurity.org
   or here:
   xpozed.dgt@gmail.com

 In case you like to sponsor my beer budget there's a donation button here:
   http://nullsecurity.org/

 There's also a Discord here:
   https://discord.gg/ZzaWJFB

--------------------------------------------------------------------------------
Version history (just because):

[15 Nov, 2017] 1.2 (build 1008)
 - file entry FILETIME is now properly holding the creation timestamp of 
   the file
 - fixed a bug with unpakke.ini load/save

[26 May, 2017] 1.2 (build 1007)
 - added support of LZF compression (requires the "lzflib.dll" to be placed in
   your "/libs" directory)
 - upkkInsertData and upkkInsertFile now accept FILE_RESTORE flag
 - Unpakke module SDK is now updated to v1.2

[07 Feb, 2017] 1.1 (build 1006)
 - archiveRow structure fileSizeRaw, fileSizeZip and fileOffset are changed to
   DWORD64 so we can now handle big (>4GB) archives. I should made this long
   ago, but oh well - better late than never?
 - dataArchive structure archiveSize is changed to WDORD64. Same as above.
 - upkkExtractFile now extract files by chunks of 10 megabytes. Apparently,
   allocating 500 megabytes at once, then writing them to the disk was
   absolutely stupid. Who would have thought? (not me, obviously)
 - Offset parameters to some of the API functions are now sized as DWORD64
   (because big files)
 - When unpacking the base directory is set to the output directory
 - When packing the base directory is set to the input directory
 - upkkCreateDirectory function is added.
 - upkkRawCreateFile function is added.
 - upkkRawReadFile function is added.
 - upkkRawWriteFile function is added.
 - upkkRawCloseFile function is added.
 - Unpakke module SDK is now updated to v1.1 If you have the old v1.0 throw
   it away and get the new version. Seriously.

[24 Jan, 2016] 1.0 (build 1005)
 - upkkReadFile function is added.
 - Unpakke module SDK v1.0 is now released to the public.

[18 Jan, 2016] 1.0 (build 1004)
 - upkkInsertData and upkkInsertFile can now write into container archives.
   Something I should predict long ago...

[17 Jan, 2016] 1.0 (build 1003)
 - Slightly modified the upkkOpenStorage function, so it can also create storage
   files (when packing back).

[11 Jan, 2016] 1.0 (build 1002)
 - Completely rewritten code. New bugs to discover and/or break your PC.
 - Completely new type of modules. Well sort of. Overall, this means the old
   ones are no longer supported, and they will probably never will, unless I
   rewrite them too. (I won't.)
 - Added program GUI for those kind of people. You know who you are.
 - Added SDK for open source/3rd party module development. Good luck using it...

[04 Apr, 2011] 0.4b
 - Every memory leak I wasn't able to catch in the previous versions was fixed.
   Probably.

[28 Feb, 2011] 0.3b
 - Different backslash style in game archives is now supported, because some
   games used "\" while others used "/" and Windows is only happy when slashes
   are "\".

[25 Feb, 2011] 0.2b
 - Some of the initial release bugs were fixed (mostly memory leaks oops)
 - Added DEFLATE compression support using ZLib

[21 Feb, 2011] 0.1b
 - First release. As expected it was a bag of badly written, bug infested code.

--------------------------------------------------------------------------------
 Yes, that's a readme, shut up             last readme.txt update [2017-Nov-15]