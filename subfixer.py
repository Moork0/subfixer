<<<<<<< HEAD
#!/usr/bin/python3
import sys
print("Subtitle Fixer Ver 0.2")
=======
import sys
print("Subtitle Fixer Ver 0.1")
>>>>>>> 375b16646f44eae8b262500bd7b2f20f23c3fc8f
args = sys.argv
if len(args) < 1:
    print('Usage : python subfixer.py "subtitle.srt"\n')
presub = args[1]
orgsub = open(presub, 'r', encoding='latin').read().encode('latin', errors='replace').decode('cp1256')
open(str(presub).replace(".srt", "_fixed.srt"), 'w').write(orgsub)
print('Subtitle has been successfully fixed . saved on : {0}'.format(str(presub).replace(".srt", "_fixed.srt")))
