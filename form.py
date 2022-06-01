from flask import Flask, request, render_template
import numpy
import pickle
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":


        with open('model_pkl', 'rb') as f:
            lr = pickle.load(f)

        bathroom = request.form.get("no.of bathrooms")
        bedroom = request.form.get("no.of bedrooms")
        total_sqft = request.form.get("sqft_total")
        price = request.form.get("price")

        statearr = []

        states = request.form['state']

        if (states == 'newYork'):
            statearr = [0,0,1]

        elif (states == 'california'):
            statearr = [1,0,0]

        else:
            statearr = [0,1,0]


        z = []
        z.append(bathroom)
        z.append(bedroom)
        z.append(total_sqft)
        z.append(price)

        z.extend(statearr)

        arr = numpy.array(z,dtype = float)

        result = lr.predict([arr])

        return render_template('form.html', prediction_text="Your house_price is Rs. {:.2f}".format(result[0,0]))


    return render_template("form.html")

if __name__=='__main__':
   app.run()
