from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "Hello my first flask application";  
  
if __name__ =='__main__':  
    app.run(host="0.0.0.0", port=8000, debug = True)
