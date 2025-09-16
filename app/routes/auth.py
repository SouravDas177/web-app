from flask import Blueprint,session,url_for,redirect,render_template,request,flash


auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/login",methods=["GET","POST"])

def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if password and username:
            session["user"]=username
            flash("login successfull","success")

        else:
            
            flash('invalid user number or password',"danger")
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("auth.login"))