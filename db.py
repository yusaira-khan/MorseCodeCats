import psycopg2
import random

def recordCorrectness(code, correctness,cur):
    cur.execute("select * from results where  code = '"+code+"' ; ")
    rows = cur.fetchall()
    if len(rows)>1:
        cur.execute("delete from results where code = '"+code+"' ; ")
        def f (row, prev):
            _,c,i=row
            pc,pi=prev
            return (c+pc, i+pi)
        corr, incorr = reduce(f,rows,(0,0))
        cur.execute("insert into results values ('"+code+"',"+str(corr+int(correctness))+","+str(incorr+int(not correctness))+");")
    elif len(rows)==1:
        _,corr,incorr= rows[0]
        cur.execute("update results set correct = "+str(corr+int(correctness))+" , intcorrect = "+str(incorr+int(not correctness))+"where  code = '"+code+"' ; ")
    else:
        cur.execute("insert into results values ('"+code+"',"+str(int(correctness))+","+str(int(not correctness))+");")

def isCorrectCode(name, code):
    conn = psycopg2.connect(database='morsecode', user='root', host='localhost', port=26257)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute("select code, ascii from mini where ascii = '"+name+"' ; ")
    row = cur.fetchall()[0]
    correct = row[0]

    correctness = correct==code
    recordCorrectness(code,correctness,cur)
    cur.close()
    conn.close()
    return correctness


def getRandomLetter():
    conn = psycopg2.connect(database='morsecode', user='root', host='localhost', port=26257)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    random.seed()
    num = random.randrange(1,37)
    cur.execute("select id,spelling from words where id = "+str(num)+" ; ")

    row = cur.fetchall()[0]
    spell=row[1]

    cur.close()
    conn.close()
    return spell


def test():
    let= getRandomLetter()
    code = raw_input("what is the correct morse code for '"+let+"' ?\n")
    if(isCorrectCode(let,code)):
        print("correct")
    else:
        print "incorrect"

#test()
