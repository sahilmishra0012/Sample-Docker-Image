from flask import Flask, render_template, request,redirect
import db_extraction
import pandas as pd

app = Flask(__name__,template_folder='')

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['GET','POST'])
def capture():
    if request.method == 'POST':
        bgroup=request.form['bgroup']
        output=db_extraction.get_person(bgroup)
        if len(output)!=0:
            df = pd.DataFrame(data=output,columns=['First Name','Last Name','Blood Group','Address','Phone Number'])
            df.head()
            return render_template('found.html',tables=[df.to_html(header=True,index=False,table_id='MyTable',justify='center')], titles=df.columns.values)
        else:
            return render_template('notfound.html')
    return render_template('notfound.html')

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8080, debug=True)