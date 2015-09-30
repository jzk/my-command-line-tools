import fileinput

input = ""

for line in fileinput.input():
	input = input + line


indexOfInsert = input.find('insert into')
indexOfFirstParenthese = input.find('(')
indexOfFirstRightParenthese = input.find(')')

indexOfSecondParenthese = input.find('(', indexOfFirstRightParenthese)
indexOfSecondRightParenthese = input.rfind(')')

if indexOfInsert < 0:
	tableName = input[:indexOfFirstParenthese]
else:
	tableName = input[indexOfInsert+len("insert into "):indexOfFirstParenthese]

print "Table: %s" % tableName

tableFieldList = input[indexOfFirstParenthese+1:indexOfFirstRightParenthese]
tableValueList = input[indexOfSecondParenthese+1:indexOfSecondRightParenthese]

tableFieldList = tableFieldList.split(',')
tableValueList = tableValueList.split(',')

i = 1
for field in tableFieldList:
	print "field({i}):  {field}  : {value}".format(i=i, field = field.strip(), value=tableValueList[i-1].strip())
	i = i + 1
