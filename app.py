from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = "jarvis_secret_key"

users = {}

# HOME PAGE
@app.route("/")
def home():
    if "user" in session:
        return f"""
        <h1>Welcome {session['user']} 🎉</h1>
        <a href='/logout'>Logout</a>
        """
    return redirect("/login")


# LOGIN PAGE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect("/")

        return "<h2>Invalid Username or Password</h2>"

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login</title>

        <style>
            body{
                background:#0f172a;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                font-family:Arial;
            }

            .box{
                background:white;
                padding:40px;
                border-radius:15px;
                width:300px;
                animation:fade 1s ease;
            }

            input{
                width:100%;
                padding:10px;
                margin-top:10px;
            }

            button{
                width:100%;
                padding:10px;
                margin-top:15px;
                background:#2563eb;
                color:white;
                border:none;
                cursor:pointer;
            }

            a{
                text-decoration:none;
            }

            @keyframes fade{
                from{opacity:0; transform:translateY(-20px);}
                to{opacity:1; transform:translateY(0);}
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>Login</h1>

            <form method="POST">

                <input type="text" name="username" placeholder="Username" required>

                <input type="password" name="password" placeholder="Password" required>

                <button type="submit">Login</button>

            </form>

            <p>Don't have account?</p>

            <a href="/signup">Signup</a>

        </div>

    </body>
    </html>
    """)


# SIGNUP PAGE
@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        users[username] = password

        return redirect("/login")

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Signup</title>

        <style>
            body{
                background:#111827;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                font-family:Arial;
            }

            .box{
                background:white;
                padding:40px;
                border-radius:15px;
                width:300px;
                animation:fade 1s ease;
            }

            input{
                width:100%;
                padding:10px;
                margin-top:10px;
            }

            button{
                width:100%;
                padding:10px;
                margin-top:15px;
                background:#16a34a;
                color:white;
                border:none;
                cursor:pointer;
            }

            @keyframes fade{
                from{opacity:0; transform:translateY(-20px);}
                to{opacity:1; transform:translateY(0);}
            }
        </style>
    </head>

    <body>

        <div class="box">

            <h1>Signup</h1>

            <form method="POST">

                <input type="text" name="username" placeholder="Username" required>

                <input type="password" name="password" placeholder="Password" required>

                <button type="submit">Create Account</button>

            </form>

        </div>

    </body>
    </html>
    """)


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)