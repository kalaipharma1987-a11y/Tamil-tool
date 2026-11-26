from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    age_result = ""
    disc_result = ""
    
    if request.method == "POST":
        if "dob" in request.form and request.form["dob"]:
            try:
                dob = datetime.strptime(request.form["dob"], "%Y-%m-%d")
                today = datetime.today()
                years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                days = (today - dob).days
                age_result = f"Ungal Vayadhu: {years} Varudangal (Mottham {days} Naatkal)"
            except:
                age_result = "Sariyana Thedhiyai (Date) Therndhedukkavum."
                
        if "price" in request.form and "discount" in request.form:
            try:
                price = float(request.form["price"])
                disc = float(request.form["discount"])
                saved = (price * disc) / 100
                final_price = price - saved
                disc_result = f"Thallubadi: Rs.{saved:.2f} | Selutha Vendiya Vilai: Rs.{final_price:.2f}"
            except:
                disc_result = "Sariyana Engalai (Numbers) Ullidavum."

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tamil Smart Tools</title>
        <style>
            body {{ font-family: sans-serif; background: #f4f6f9; margin: 0; padding: 0; text-align: center; }}
            .header {{ background: #1a73e8; color: white; padding: 18px; font-size: 20px; font-weight: bold; }}
            .ad-box {{ background: #fff3cd; border: 1px dashed #ffc107; margin: 12px; padding: 12px; font-size: 13px; color: #856404; border-radius: 8px; }}
            .card {{ background: white; margin: 15px; padding: 20px; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }}
            input {{ width: 90%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 6px; font-size: 16px; }}
            button {{ background: #28a745; color: white; border: none; padding: 12px 20px; font-size: 16px; border-radius: 6px; width: 95%; cursor: pointer; font-weight: bold; }}
            .res {{ margin-top: 12px; font-weight: bold; color: #d93025; font-size: 16px; }}
        </style>
    </head>
    <body>
        <div class="header">Tamil Smart Utility App</div>
        
        <!-- விளம்பரம் வைக்கும் இடம் 1 -->
        <div class="ad-box">Advertisement Space (Ingu Adsterra / Affiliate Link Vaikkalam)</div>

        <!-- 1. வயது கால்குலேட்டர் -->
        <div class="card">
            <h3>1. Vayadhu Kanakkidu (Age Calculator)</h3>
            <form method="POST">
                <label>Pirandha Thedhi (Date of Birth):</label><br>
                <input type="date" name="dob" required><br>
                <button type="submit">Vayadhai Paar</button>
            </form>
            <div class="res">{age_result}</div>
        </div>

        <!-- 2. தள்ளுபடி கால்குலேட்டர் -->
        <div class="card">
            <h3>2. Thallubadi Kanakkidu (Discount Calculator)</h3>
            <form method="POST">
                <input type="number" name="price" placeholder="Porulin Vilai (Rs.)" required><br>
                <input type="number" name="discount" placeholder="Thallubadi Sadhavigidham (%)" required><br>
                <button type="submit">Vilaiyai Kanakkidu</button>
            </form>
            <div class="res">{disc_result}</div>
        </div>

        <!-- விளம்பரம் வைக்கும் இடம் 2 -->
        <div class="ad-box">Amazon / Meesho Best Offers Link Ingu Vaikkalam</div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
