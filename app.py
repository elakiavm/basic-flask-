from mmap import PROT_READ
from flask import Flask

app = Flask(__name__)
PORT = 4538

@app.route("/",methods=["GET"])
def start ():
    # user=['Priyanka','Elakia','Vini']
    # return render_template('index3.html',name="elakia",members=user)

    return ('hello world')

if __name__ =="__main__":
    app.run(
            debug=True,
            host='0.0.0.0',
            port= PORT 
            )


    