from flask import Blueprint, render_template,request,redirect,url_for,make_response
import string, random
from .DatabaseModels import User
from flask_login import login_user, logout_user, current_user, login_required
from . import Database

# TokenGeneration Function
def TokenGeneration():
    Token = ''.join(random.choices(string.ascii_uppercase +
                                           string.digits + string.ascii_lowercase, k=15))
    Check = User.query.filter_by(AuthToken=Token).first()
    if Check:
        return TokenGeneration()
    else:
        return Token

PageRoute = Blueprint("PageRoute", __name__)


@PageRoute.route("/")
def DefaultPage():
    return render_template("HomePage.html"), 200


@PageRoute.route("/Home")
def HomePage():
    return render_template("HomePage.html"), 200


@PageRoute.route("/Login", methods=["POST", "GET"])
def LoginPage():
    if request.method == "POST":
        FormUsername= request.form.get("Username")
        FormPassowrd= request.form.get("Password")
        AttemptedUser = User.query.filter_by( Username= FormUsername, Password= FormPassowrd ).first()
        if AttemptedUser == None:
            return render_template("LoginPage.html", msg="display: show;")
        login_user(AttemptedUser)
        Token = TokenGeneration()
        AttemptedUser.AuthToken = Token
        Database.session.commit()

        Res = make_response(redirect(url_for('PostRoute.ShowRooms')))
        Res.set_cookie('AuthToken', Token)
        return Res
    return render_template("LoginPage.html",msg="display: none;"), 200


@PageRoute.route("/SignUp")
def SignUpPage():
    return render_template("SignUpPage.html"), 200

@PageRoute.route("/Logout")
@login_required
def LogoutPage():
    current_user.AuthToken = None
    Database.session.commit()
    logout_user()
    res = redirect(url_for('PageRoute.HomePage'))
    res.set_cookie('AuthToken', "", expires=1)
    return res