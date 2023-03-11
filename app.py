import gradio as gr
import pyshorteners
import pymssql 



def dbupdate(longname,shortname):
    dbconnect = pymssql.connect(server='nrtsqlserver1.database.windows.net', user='sqllogin1', password='Password1', database='nrtsql1')
    cursordb = dbconnect.cursor()
    cursordb.execute("""INSERT INTO webaddress (longurl, shorturl) VALUES (%s, %s)""", (longname, shortname))
    cursordb.close()
    dbconnect.commit()
    dbconnect.close()



def shortenurl(name):
    longname = name
    shortener = pyshorteners.Shortener()
    shortname = shortener.tinyurl.short(longname)
    dbupdate(longname,shortname)
    return (shortname)



app = gr.Interface(fn=shortenurl, inputs="text", outputs="text")
app.launch(server_name="0.0.0.0", server_port=80) 
