# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, session

# import my python files
from callOption import euro_vanilla_call
from putOption import euro_vanilla_put

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["SECRET_KEY"] = "hkvezwtyfyninoera345y6iuij"

@app.route("/", methods=["GET", "POST"])

def index():
    errors = ""
    if request.method == "POST":
        S = None
        K = None
        T = None
        r = None
        sigma = None
        try:
            S = float(request.form["S"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["S"])
        try:
            K = float(request.form["K"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["K"])
        try:
            T = float(request.form["T"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["T"])
        try:
            r = float(request.form["r"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["r"])
        try:
            sigma = float(request.form["sigma"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["sigma"])
        if S is not None and K is not None and T is not None and r is not None and sigma is not None:
            call = euro_vanilla_call(S, K, T, r, sigma)
            put = euro_vanilla_put(S, K, T, r, sigma)
            return '''
            <!doctype html>
                <html>
                    <head>
                        <!-- Required meta tags -->
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <!-- Bootstrap CSS -->
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                        <link rel="stylesheet" href="static/style.css">
                    </head>
                    <body>

                    <!--##################################-->

                    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a class="navbar-brand" href="/">BSM</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                        <div class="navbar-nav">
                          <a class="nav-item nav-link active" href="/">Home</a>
                          <a class="nav-item nav-link" target="_blank" href="https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model">Wiki</a>
                        </div>
                    </div>
                </nav>

                <main role="main">
                <!-- Main jumbotron for a primary marketing message or call to action -->
                <div class="jumbotron">
                    <div class="container">
                        <h1 class="text-light bg-dark">What is the <i>Black-Scholes</i> Model?</h1>
                        <h4>The Black Scholes model, also known as the Black-Scholes-Merton (BSM) model, is a differential equation used to solve for European options prices. The formula, developed by three economists – Fischer Black, Myron Scholes and Robert Merton – awarded them the 1997 Nobel Prize in Economics. It was introduced in their 1973 paper, "<a target="_blank" href="https://www.cs.princeton.edu/courses/archive/fall09/cos323/papers/black_scholes73.pdf">The Pricing of Options and Corporate Liabilities,</a>" published in the Journal of Political Economy.</h4>
                    </div>
                </div>

                <div class="container">

                    <div class="row">

                      <div class="col-md-6">
                        <h2>Call Option</h2>
                        <p>A Call option gives the owner the right, but not the obligation, to buy an asset (the underlying), at a specified price (the strike), at a predetermined date (the expiry or maturity) to a given party.</p>
                      </div>

                      <div class="col-md-6">
                        <h2>Put Option</h2>
                        <p>A Put option gives the owner the right, but not the obligation, to sell an asset (the underlying), at a specified price (the strike), at a predetermined date (the expiry or maturity) to a given party.</p>
                      </div>

                    </div>

                </div>

                <div class="jumbotron bg-white">
                    <div class="container">

                    <form class="form-box">
                        <fieldset>
                            <h3>Results</h3>
                            <p>Call price: <b>$ {}</b></p>
                            <p>Put price: <b>$ {}</b></p>
                        </fieldset>
                    </form>

                        <form class="form-box" method="post" action=".">
                                <fieldset>
                                    <h3>Black-Scholes Euro Option Calculator</h3>
                                    <p>
                                        <label>$ Spot price <b>(S)</b></label>
                                        <input type="number" step="any" min=".0000001" name="S" />
                                         USD
                                    </p>
                                    <p>
                                        <label>$ Strike price <b>(K)</b></label>
                                        <input type="number" step="any" min=".0000001" name="K" />
                                         USD
                                    </p>
                                    <p>
                                        <label>Time to maturity <b>(T)</b></label>
                                        <input type="number" step="any" min=".0000001" name="T" />
                                        Years
                                    </p>
                                    <p>
                                        <label>Risk free rate <b>(r)</b></label>
                                        <input type="number" step="any" min="0.000001" name="r" />
                                         %
                                    </p>
                                    <p>
                                        <label>Volatility <b>(σ)</b></label>
                                        <input type="number" step="any" min="0.000001" name="sigma" />
                                         %
                                    </p>
                                    <p>
                                        <input class="calc-btn" type="submit" value="Calculate &raquo;" />
                                    </p>
                                </fieldset>
                            </form>

                            </div>
                            </div>
                        </main>

                        <!--##################################-->

                        <!-- jQuery, Popper.js, Bootstrap JS -->
                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                    </body>

                    <hr>

                    <footer class="container">
                        <p>black-scholes.org 2019-2020 :: <a target="_blank" href="https://www.linkedin.com/in/adam-elmachkour/">Author & admin</a></p>
                    </footer>

                </html>
            '''.format(round(call, 8),round(put, 8))
        else:
            result = "NaN"
            return '''
            <!doctype html>
                <html>
                    <head>
                        <!-- Required meta tags -->
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <!-- Bootstrap CSS -->
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                        <link rel="stylesheet" href="static/style.css">
                    </head>
                    <body>

                    <!--##################################-->

                    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a class="navbar-brand" href="/">BSM</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                        <div class="navbar-nav">
                          <a class="nav-item nav-link active" href="/">Home</a>
                          <a class="nav-item nav-link" target="_blank" href="https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model">Wiki</a>
                        </div>
                    </div>
                </nav>

                <main role="main">
                <!-- Main jumbotron for a primary marketing message or call to action -->
                <div class="jumbotron">
                    <div class="container">
                        <h1 class="text-light bg-dark">What is the <i>Black-Scholes</i> Model?</h1>
                        <h4>The Black Scholes model, also known as the Black-Scholes-Merton (BSM) model, is a differential equation used to solve for European options prices. The formula, developed by three economists – Fischer Black, Myron Scholes and Robert Merton – awarded them the 1997 Nobel Prize in Economics. It was introduced in their 1973 paper, "<a target="_blank" href="https://www.cs.princeton.edu/courses/archive/fall09/cos323/papers/black_scholes73.pdf">The Pricing of Options and Corporate Liabilities,</a>" published in the Journal of Political Economy.</h4>
                    </div>
                </div>

                <div class="container">

                    <div class="row">

                      <div class="col-md-6">
                        <h2>Call Option</h2>
                        <p>A Call option gives the owner the right, but not the obligation, to buy an asset (the underlying), at a specified price (the strike), at a predetermined date (the expiry or maturity) to a given party.</p>
                      </div>

                      <div class="col-md-6">
                        <h2>Put Option</h2>
                        <p>A Put option gives the owner the right, but not the obligation, to sell an asset (the underlying), at a specified price (the strike), at a predetermined date (the expiry or maturity) to a given party.</p>
                      </div>

                    </div>

                </div>

                <div class="jumbotron bg-white">
                    <div class="container">

                        <form class="form-box">
                            <fieldset>
                                <h3>Results</h3>
                                <p>Output is <b> {result}</b>; invalid input.</p>
                            </fieldset>
                        </form>

                        <form class="form-box" method="post" action=".">
                                <fieldset>
                                    <h3>Black-Scholes Euro Option Calculator</h3>
                                    <p>
                                        <label>$ Spot price <b>(S)</b></label>
                                        <input type="number" step="any" min=".0000001" name="S" />
                                         USD
                                    </p>
                                    <p>
                                        <label>$ Strike price <b>(K)</b></label>
                                        <input type="number" step="any" min=".0000001" name="K" />
                                         USD
                                    </p>
                                    <p>
                                        <label>Time to maturity <b>(T)</b></label>
                                        <input type="number" step="any" min=".0000001" name="T" />
                                        Years
                                    </p>
                                    <p>
                                        <label>Risk free rate <b>(r)</b></label>
                                        <input type="number" step="any" min="0.000001" name="r" />
                                         %
                                    </p>
                                    <p>
                                        <label>Volatility <b>(σ)</b></label>
                                        <input type="number" step="any" min="0.000001" name="sigma" />
                                         %
                                    </p>
                                    <p>
                                        <input class="calc-btn" type="submit" value="Calculate &raquo;" />
                                    </p>
                                </fieldset>
                            </form>

                            </div>
                            </div>
                        </main>

                        <!--##################################-->

                        </div>
                        </div>

                        <!-- jQuery, Popper.js, Bootstrap JS -->
                        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                    </body>

                    <hr>

                    <footer class="container">
                        <p>black-scholes.org 2019-2020 :: <a target="_blank" href="https://www.linkedin.com/in/adam-elmachkour/">Author & admin</a></p>
                    </footer>

                </html>
            '''.format(result=result)

    return '''
    <!doctype html>
        <html>
            <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <!-- Bootstrap CSS -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <link rel="stylesheet" href="static/style.css">
            </head>
            <body>

                    <!--##################################-->

                    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a class="navbar-brand" href="/">BSM</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                        <div class="navbar-nav">
                          <a class="nav-item nav-link active" href="/">Home</a>
                          <a class="nav-item nav-link" target="_blank" href="https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model">Wiki</a>
                        </div>
                    </div>
                </nav>

                <main role="main">
                <!-- Main jumbotron for a primary marketing message or call to action -->
                <div class="jumbotron">
                    <div class="container">
                        <h1 class="text-light bg-dark">What is the <i>Black-Scholes</i> Model?</h1>
                        <h4>The Black Scholes model, also known as the Black-Scholes-Merton (BSM) model, is a differential equation used to solve for European options prices. The formula, developed by three economists – Fischer Black, Myron Scholes and Robert Merton – awarded them the 1997 Nobel Prize in Economics. It was introduced in their 1973 paper, "<a target="_blank" href="https://www.cs.princeton.edu/courses/archive/fall09/cos323/papers/black_scholes73.pdf">The Pricing of Options and Corporate Liabilities,</a>" published in the Journal of Political Economy.</h4>
                    </div>
                </div>

                <div class="container">

                    <div class="row">

                      <div class="col-md-6">
                        <h2>Call Option</h2>
                        <p>A Call option gives the owner the right, but not the obligation, to buy an asset (the underlying), at a specified price (the strike), at a predetermined date (the expiry or maturity) to a given party.</p>
                      </div>

                      <div class="col-md-6">
                        <h2>Put Option</h2>
                        <p>A Put option gives the owner the right, but not the obligation, to sell an asset (the underlying), at a specified price (the strike), at a predetermined date (the expiry or maturity) to a given party.</p>
                      </div>

                    </div>

                </div>

                <div class="jumbotron bg-white">
                    <div class="container">

                        <form class="form-box" method="post" action=".">
                                <fieldset>
                                    <h3>Black-Scholes Euro Option Calculator</h3>
                                    <p>
                                        <label>$ Spot price <b>(S)</b></label>
                                        <input type="number" step="any" min=".0000001" name="S" />
                                         USD
                                    </p>
                                    <p>
                                        <label>$ Strike price <b>(K)</b></label>
                                        <input type="number" step="any" min=".0000001" name="K" />
                                         USD
                                    </p>
                                    <p>
                                        <label>Time to maturity <b>(T)</b></label>
                                        <input type="number" step="any" min=".0000001" name="T" />
                                        Years
                                    </p>
                                    <p>
                                        <label>Risk free rate <b>(r)</b></label>
                                        <input type="number" step="any" min="0.000001" name="r" />
                                         %
                                    </p>
                                    <p>
                                        <label>Volatility <b>(σ)</b></label>
                                        <input type="number" step="any" min="0.000001" name="sigma" />
                                         %
                                    </p>
                                    <p>
                                        <input class="calc-btn" type="submit" value="Calculate &raquo;" />
                                    </p>
                                </fieldset>
                            </form>

                            </div>
                            </div>
                        </main>

                        <!--##################################-->

                <!-- jQuery, Popper.js, Bootstrap JS -->
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            </body>

            <hr>


            <footer class="container">
                <p>black-scholes.org 2019-2020 :: <a target="_blank" href="https://www.linkedin.com/in/adam-elmachkour/">Author & admin</a></p>
            </footer>

        </html>
    '''.format(errors=errors)

################################################################################
################################################################################

@app.route("/sale", methods=["GET", "POST"])

def laura():
    return '''
    <p>Contact me if you are interested in renting or buying this domain.</p>
    '''