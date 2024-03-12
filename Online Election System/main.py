from flask import Flask, render_template, request
from mysql import mysql, register, check, can_num, candidates, up_count, count,max,voters,auther,u_p,find
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/details',methods=["POST",'GET'])
def info():
    result = mysql(request.form["user_name"], request.form["pwd"], request.form["role"])
    if result:
        return render_template('details.html')
    else:
        return render_template('index.html', content='Invalid Credentials!')
@app.route("/password",methods=['POST','GET'])
def update():
    return render_template('up.html')
@app.route('/check',methods=['POST','GET'])
def pcheck():
    test = request.form['email'] 
    user,otp = auther(test)
    
    if user:
        return render_template('up.html',content='Otp has sent to your email',Otp=otp,email=test)
    else:
        return render_template('up.html',message='email not exist')
@app.route('/verify',methods=['GET',"POST"])
def verify():
    email=request.form['email']
    otp=request.form['otp']
    Otp=request.form['Otp']
    if otp==Otp:
        return render_template('password.html',email=email)
    else:
        return render_template('up.html',content="Otp Did'nt Match")

@app.route('/upas',methods=['GET','POST'])
def u_pass():
    email=request.form['email']
    new=request.form['new']
    p=request.form['re'] 
    if new==p:
        u_p(email,new)
        return render_template('index.html')
    else:
        return render_template('password.html',content="password incorrect")
  
@app.route('/register', methods=['POST', 'GET'])
def register_redirect():
    return render_template('register.html')

@app.route('/register_Done', methods=['POST', 'GET'])
def register_page():
    Role = request.form['role']
    result,content = register(request.form['user_name'], request.form['pwd'],request.form['id'] ,request.form['email'], Role,
                      request.form['age'], request.form['gender'])
    if Role == 'Candidate':
        candidates(request.form['user_name'],request.form['id'])
    else:
        voters(request.form['user_name'],request.form['age'],request.form['id'], request.form['gender'])
    if result:
        return render_template('index.html')
    else:
        return render_template('register.html', content=content)

@app.route('/voting',methods=['GET',"POST"])
def voting_page():
    ud = check(request.form['voterid'])
    cd = can_num()
    if len(ud)!=0:
        return render_template('voting.html', name=ud[0][0], age=ud[0][1], id=ud[0][2],status=ud[0][3],
                               gender=ud[0][4], candidates=cd)
    else:
        return render_template('details.html')

@app.route('/vote/<candidate>', methods=['POST', 'GET'])
def thanks(candidate):
    up_count(candidate)
    return render_template('thanks.html', candidate=candidate)

@app.route('/result', methods=['POST', 'GET'])

def counting():
        
        
            cd=count()
            x = []
            y = []
            for row in cd:
                x.append(row[0])
                y.append(row[1])

            # Create a bar chart
            plt.switch_backend('Agg')
            fig, ax = plt.subplots(figsize=(11, 6))
            # Create a bar chart
            plt.bar(x, y, color='blue')
            plt.xlabel('Categories')
            plt.ylabel('Values')
            # Save the plot to a BytesIO object
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)

            # Encode the plot as base64
            plot_url = base64.b64encode(img.getvalue()).decode()
            name=max()
    
            # Render the HTML template with the embedded plot
            return render_template('count.html', plot_url=plot_url,content=name)
        
if __name__ == "__main__":
    app.run(port=600)
