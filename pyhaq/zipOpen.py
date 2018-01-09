import optparse
import zipfile
from threading import Thread


def extract_zip(zippedFile, password):
    try:
        zippedFile.extractall(pwd=password)
        print("[+] Password Found: %s\n") %(password)
    except:
        pass


def main():
    parser = optparse.OptionParser("Usage %prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest = 'zname', type = 'string', help = 'specify zip file')
    parser.add_option('-d', dest = 'dname', type = 'string', help = 'specify zip file')
    
    (options, arg) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
    else:
        zname = options.zname
        dname = options.dname

        zippedFile = zipfile.ZipFile(zname)
        passFile = open(dname)

        for line in passFile.readlines():
            password = line.strip('\n')
            t = Thread(target = extract_zip, args=(zipfile, password))
                t.start()

if __name__ == '__main__':
    main()

