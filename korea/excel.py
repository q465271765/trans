#-*-coding:utf-8-*-
from xlutils.copy import copy    # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook  # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf         # http://pypi.python.org/pypi/xlwt
import sys
reload(sys)

sys.setdefaultencoding('utf-8')
# 0 based (subtract 1 from excel row number)
START_ROW = 404
ismal_index = 2
#url所在列
url_index = 12
#domain所在列
domain_index = 11
#malinfo所在列
malinfo_index = 9
file_path = "ZKTimeNet3_Language_Report_English.xlsx"
#formatting_info=True保存之前数据的格式
rb = open_workbook(file_path,formatting_info=True)
r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
wb = copy(rb) # a writable copy (I can't read values out of this, only write to it)
w_sheet = wb.get_sheet(0) # the sheet to write to within the writable copy
malurl = '''http://xbox.ooqqxx.com/res/ext.jar
            http://xbox.ooqqxx.com/res/stat.jar
            http://xbox.ooqqxx.com/pages/v.html
            http://xbox.ooqqxx.com/pages/extv.html
            http://xbox.ooqqxx.com/pages/r.html'''
domain_info = "http://xbox.ooqqxx.com"
malinfo = u"获取恶意URL，写入配置文件中，下载恶意可执行程序。"
#r_sheet.nrows为总行数
for row_index in range(START_ROW, r_sheet.nrows):
    #xlsvalue = r_sheet.cell(row_index, col_age_november).value
    w_sheet.write(row_index, ismal_index, u'是')
    w_sheet.write(row_index, url_index, malurl)
    w_sheet.write(row_index, domain_index, domain_info)
    w_sheet.write(row_index, malinfo_index, malinfo)
#wb.save(file_path + '.out' + os.path.splitext(file_path)[-1])
wb.save("2013.xls")