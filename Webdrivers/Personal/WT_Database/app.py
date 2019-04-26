import sys
sys.path.append('/personal/WT_Database')
import db_function
from flask import Flask, render_template, request


app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    print(db_function.db_conn())
    result = db_function.view_table('conditions')
    print("**RESULT * * * * - ",result)
    return result


if __name__ == "__main__":
    app.run(debug=True)