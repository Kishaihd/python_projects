#No need to manually check if a file exists before trying to open it!
#There's a possible race condition in that!

with ignored(OSError):
    os.remove('somefile.tmp')
