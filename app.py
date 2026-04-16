from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Intégration d'un peu de HTML/CSS pour un rendu plus propre
    return """
    <html>
        <head><title>Mon App Docker</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f4f4f9;">
            <div style="padding: 20px; background-color: white; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
                <h1 style="color: #2c3e50;">Bonjour à tous ! 👋</h1>
                <p style="font-size: 18px; color: #34495e;">
                    Ceci est une simple application conteneurisée avec Docker par <strong>Ralph Santiago</strong> !
                </p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)