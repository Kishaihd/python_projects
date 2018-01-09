#Python sends it help to stdout, which sucks if you're not using cli.
#So redirect it to a file!

with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)


