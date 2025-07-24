          
from flask import Flask, render_template, request, redirect
import re
import matplotlib.pyplot as plt
import numpy as np
app = Flask(__name__)
@app.route('/graph', methods = ['POST','GET'])
def graph():
    if request.method=='GET':
        return render_template("graph.html")
    eqn = str(request.form.get("eqn")).split("+")
    minx = int(request.form.get("min"))
    maxx= int(request.form.get("max"))
    plotStyle = request.form.get("plotStyle")
    equation = []
    for i in range(len(eqn)):
        equation.append(re.split(r'[*^]+',eqn[i]))
    """
    1*x^2 + 2*x^1 + 1*x^0
    x^1+2*x^0
    """
    """
        even power, odd power -> U or S accordingly
        roots: x=0 change in behaviour of graph at place
        
        how to store: list according to power -> position of the list
        [1,2,1]
        
        finding roots:
        
        create a sample list first then according to the shift and change ?:
        eg: len(eqn) = 3 | X^2
        
        or
        ->maybe specify range and just calculate each value -> takes so much time
    """
    x = [i for i in np.arange(minx,maxx+1,0.1)]
    y = []
    for i in x: 
        ssum = 0
        for j in range(len(equation)):
            ssum+=int(equation[j][0])*(i**int(equation[j][2]))
        y.append(ssum)
    plt.figure()
    if plotStyle == 'line':
        plt.plot(x,y)
    if plotStyle == 'scatter':
        plt.scatter(x,y)
    if plotStyle == 'bar':
        plt.plot(x,y)
    plt.plot([minx,0,maxx+1],[0,0,0],scalex=False,scaley=False)
    plt.plot([0,0,0],[min(y),0,max(y)],scalex=False,scaley=False)
    plt.title('Line Graph')
    filename = 'static/graph.png'
    plt.savefig(filename)
    plt.close
    return render_template("graph.html",graph = 'static/graph.png')
size1m,size1n,size2m,size2n=0,0,0,0
@app.route('/matrix', methods=['POST','GET'])
def matrix():
    if request.method== 'GET':
        return render_template("matrix.html")
    if request.method =='POST':
        global size1m,size1n,size2m,size2n
        size1m,size1n = int(request.form.get('size1m')),int(request.form.get('size1n'))
        size2m,size2n = int(request.form.get('size2m')),int(request.form.get('size2n'))
        return redirect('/mulmatrix')
@app.route('/mulmatrix',methods=['POST','GET'])
def mulmatrix():
    global size1m,size1n,size2m,size2n
    print(size1m,size1n,size2m,size2n)
    if request.method=='GET':
        return render_template("mulmatrix.html",size1m=size1m,size1n=size1n,size2m=size2m,size2n=size2n)
    matrix1=[[0 for _ in range(size1n)] for _ in range(size1m)]
    matrix2=[[0 for _ in range(size2n)] for _ in range(size2m)]
    for i in range(0,size1m):
        for j in range(0,size1n):
            matrix1[i][j] = int(request.form.get(f'm1_{i}_{j}'))
    for i in range(0,size2m):
        for j in range(0,size2n):
            matrix2[i][j] = int(request.form.get(f'm2_{i}_{j}'))
    if size1n == size2m:
        mulMatrix =[[0 for _ in range(size2n)] for _ in range(size1m)]
        return render_template("mulmatrix.html",mulMatrix=mulMatrix,size1m=size1m,size1n=size1n,size2m=size2m,size2n=size2n)
    else:
        return render_template("error.html")
@app.route('/eqnsolve',methods=['POST','GET'])
def eqnsolve():
    if request.method =='GET':
        return render_template('eqnsolve.html')
    else:
        eeqn1 = str(request.form.get('eqn1')).split('+')
        eqn1=[]
        for i in range(len(eeqn1)):
            eqn1.append(re.split(r'[*^]+',eeqn1[i]))
        """
        -b , root(b^2-4ac) /2a
        """
        d =eqn1[1][0]**2 - 4*eqn1[2][0]*eqn1[0][0]
        if d<0:
            return render_template('error.html')
        else:
            root1 = (d-eqn1[1][0])/2*eqn1[2][0]
            root2 = (-d-eqn1[1][0])/2*eqn1[2][0]
            return render_template('eqnsolve.html',root1 = root1,root2=root2)
app.run(debug=True)