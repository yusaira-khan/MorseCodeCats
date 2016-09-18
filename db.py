import psycopg2
import random
def isCorrectCode(name, code):
    conn = psycopg2.connect(database='morsecode', user='root', host='localhost', port=26257)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute("select code, ascii from mini where ascii = '"+name+"' ; ")
    row = cur.fetchall()[0]
    correct = row[0]
    cur.close()
    conn.close()
    return correct==code


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
