import re 
pattern = re.compile(u'.*')
str = 'Letmein123Letmein123'
#print(pattern.search(str))

edi_api='http://wml-edi.edi-mgmt-wjpre:9000/dlim/v1/'
pattern = u'http://wml-edi.(.*):9000/dlim/v1'
match = re.match(pattern, edi_api)
print(match)
print(match.group(1))