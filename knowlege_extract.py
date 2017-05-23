import sys
import re
inputFile = 'output.txt'
outputFile = 'extractorOut.txt'

aux_verbs = ['am', 'is', 'are' ,'was' ,'were', 'being', 'been', 'does', 'do', 'did' , 'has', 'have', 'had' , 'having' , 'can', 'could', 'may', 'might', 'must', 'ought to', 'shall', 'should', 'will', 'would']
connectors = ['therefore', 'as a consequence', 'for this reason', 'for all these reasons', 'thus', 'because', 'because of', 'since', 'on account of', 'due to', 'for the reason', 'so, that', 'so that', 'when']

file = open(sys.argv[1],"r")
fileOut =open(outputFile,"w")
parse_list = []
temp_list = []

def getWord(dep_tuple):
    return dep_tuple.split('(')[1].split(',')[1].split(')')[0]

def breakConn(list):
    str = ''
    for i,v in enumerate(list):
        word_with_no = getWord(v)
        word = getWord(v).split('-')[0]

        if i==0:
            str += word
        else:
            prev_word_with_no = getWord(list[i-1])
            if(word_with_no != prev_word_with_no):
                str += word

    str = str.strip()

    conn = ''
    for i in connectors:
        if re.search(i, str):
            conn = i
            break
    
    low = 0
    up = 0

    conn_arr = conn.split(' ')
    str_arr = str.split(' ')
    #print conn_arr
    #print str_arr
    for i,v in enumerate(str_arr):
        count = 0
        for j,w in enumerate(conn_arr):
            if w == str_arr[i+j]:
                count+=1
        if count == len(conn_arr):
            low = 1 + (i)
            up = 1 + (i + len(conn_arr) - 1)
            break

    d = {'front':[], 'end':[]}
    # print low , up
    # print list
    # print len(list)

    for i,v in enumerate(list):
        # print i
        word_with_no = getWord(v)
        # print v, '------', word_with_no, '------', int(word_with_no.split('-')[1])
        if int(word_with_no.split('-')[1]) < low:
            d['front'].append(v)
        if int(word_with_no.split('-')[1]) > up:
            d['end'].append(v)

    return d


for line in file:
    print 'in loop'

    if line == "\n":
        print breakConn(temp_list)
        print '\n\n\n'
        parse_list.append(breakConn(temp_list))
        temp_list = []
    else:
        line = line.replace("\n","")
        temp_list.append(line)

print parse_list[0]

for item in parse_list:
    reg_one = re.compile('^nsubj.*')
    reg_two = re.compile('^advcl.*')
    reg_third = re.compile('^neg.*')
    reg_fourth = re.compile('^(dobj|iobj|case).*')
    
    res1 = filter(reg_one.match,item)
    res2 = filter(reg_two.match,item)
    res3 = filter(reg_third.match,item)
    res4 = filter(reg_fourth.match,item)
    
    #print res1, res2
    nsubj_1 = res1[0].split(',')[0].split('(')[1].split('-')[0]
    nsubj_2 = res1[0].split(',')[1].split('-')[0]
    print "first nsubj : ",nsubj_1,",",nsubj_2
    advcl_1 = res2[0].split(',')[0].split('(')[1].split('-')[0]
    advcl_2 = res2[0].split(',')[1].split('-')[0]
    print "advcl : ", advcl_1,",",advcl_2
    nsubj_1_1 = res1[1].split(',')[0].split('(')[1].split('-')[0]
    nsubj_1_2 = res1[1].split(',')[1].split('-')[0]
    print "second nsubj : ",nsubj_1_1,",",nsubj_1_2
    dobj_1 = res4[0].split(',')[0].split('(')[1].split('-')[0]
    dobj_2 = res4[0].split(',')[1].split('-')[0]
    print "dobj : ", dobj_1,",",dobj_2
    if len(res3) != 0:
        neg_1 = res3[0].split(',')[0].split('(')[1].split('-')[0]
        neg_2 = res3[0].split(',')[1].split('-')[0]
            #print "neg : ",neg_1,",",neg_2
    if len(res3) != 0:
        str = nsubj_2+"."+advcl_2+" = false may cause execution of "+nsubj_1+" ["+nsubj_2+","+dobj_2+"]"
    else:
        str = nsubj_2+"."+advcl_2+" = true may cause execution of "+nsubj_1+" ["+nsubj_2+","+dobj_2+"]"
    print str
    fileOut.write(str+'\n')




###################
#item = parse_list[2]
#reg_one = re.compile('^nsubj.*')
#reg_two = re.compile('^advcl.*')
#reg_third = re.compile('^neg.*')
#reg_fourth = re.compile('^dobj.*')
#res1 = filter(reg_one.match,item)
#res2 = filter(reg_two.match,item)
#res3 = filter(reg_third.match,item)
#res4 = filter(reg_fourth.match,item)
#print res1, res2
#nsubj_1 = res1[0].split(',')[0].split('(')[1].split('-')[0]
#nsubj_2 = res1[0].split(',')[1].split('-')[0]
#print "first nsubj : ",nsubj_1,",",nsubj_2
#advcl_1 = res2[0].split(',')[0].split('(')[1].split('-')[0]
#advcl_2 = res2[0].split(',')[1].split('-')[0]
#print "advcl : ", advcl_1,",",advcl_2
#nsubj_1_1 = res1[1].split(',')[0].split('(')[1].split('-')[0]
#nsubj_1_2 = res1[1].split(',')[1].split('-')[0]
#print "second nsubj : ",nsubj_1_1,",",nsubj_1_2
#dobj_1 = res4[0].split(',')[0].split('(')[1].split('-')[0]
#dobj_2 = res4[0].split(',')[1].split('-')[0]
#print "dobj : ", dobj_1,",",dobj_2
#if len(res3) != 0:
#    neg_1 = res3[0].split(',')[0].split('(')[1].split('-')[0]
#    neg_2 = res3[0].split(',')[1].split('-')[0]
    #print "neg : ",neg_1,",",neg_2
#if len(res3) != 0:
#    str = nsubj_2+"."+advcl_1+" = false may cause execution of "+nsubj_1+" ["+nsubj_2+","+dobj_2+"]"
#else:
#    str = nsubj_2+"."+advcl_1+" = true may cause execution of "+nsubj_1+" ["+nsubj_2+","+dobj_2+"]"
#print str
