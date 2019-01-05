def name(areacode, lab_en_m, lab_en_q):
    print('Population of {:s}, {:s} ({:s}).svg'.format(lab_en_q, lab_en_m, areacode))

def desc(areacode, date, lab_en_m, lab_fi_m, lab_en_q, lab_fi_q):
    print('=={{{{int:filedesc}}}}==\n{{{{Information\n|description={{{{en|1=Population of {:s}, {:s}.}}}}\n{{{{fi|1={:s} {:s} väestö.}}}}\n=={{{{int:licenceheader}}}}== {{{{Cc-zero}}}}\n'.format(lab_en_q, lab_en_m, lab_fi_m, lab_fi_q))

desc('1', '2018-12-04', 'Espoo', 'Espoon', 'Niittykumpu', 'Niittykummun')
name('1', 'Espoo', 'Niittykumpu')
