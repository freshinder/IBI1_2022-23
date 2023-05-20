# import dom
# import openpyxl
# create a workbook

# define a function called 'num_of_childnodes'
#   find all childnodes of the selected GO
#   repeat finding of the childnodes of the childnodes just found
#   until there are no more

# define a function to find the autophagosome
#

import xml.dom.minidom
DOMTree = xml.dom.minidom.parse('go_obo.xml')

from openpyxl import workbook
wb = workbook.Workbook
sheet = wb.worksheets

def num_cn(id):
    n = 0
    dic = {}
    list = []
    for go in GO:
        if go.getElementsByTagName('is_a')[0].data == id:
            n += 1
            list.append(go.getElementsByTagName('id'))
    dic['num'] = n
    dic['id_list'] = list
    return dic

def T_num_cn(id):
    num = 0
    x = num_cn(id)
    num += x['num']
    l1 = x['id_list']
    while l1:
        l2 = l1
        l1 = []
        for i in l2:
            x = num_cn(i)
            num += x['num']
            l1.extend(x['id_list'])
    return num

root = DOMTree.documentElement
GO = root.getElementsByTagName('term')
Dic = {}
count = 0
for go in GO:
    defstr = go.getElementsByTagName('defstr')[0].firstChild.data
    match = defstr.find('autophagosome')
    if match >= 0:
        id = go.getElementsByTagName('id')[0].firstChild.data
        name = go.getElementsByTagName('name')[0].firstChild.data
        cn = T_num_cn(id)
        count += 1
        key = str(count)
        Dic[key] = [id, name, defstr, cn]

for i in Dic:
    for j in Dic[i]:
        cell = sheet.cell(j,i)
        cell.value = Dic[i][j]
wb.save('autophagosome.xlsx')
