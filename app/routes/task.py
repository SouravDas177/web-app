from flask import session, Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models import Task

task_bp = Blueprint("task", __name__)

@task_bp.route("/")
def view_task():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    tasks = Task.query.all()
    return render_template("tasks.html", tasks=tasks)


@task_bp.route("/add", methods=["POST"])
def add_task():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    title = request.form.get("title")
    if title:
        new_task = Task(title=title)  # status defaults to Pending
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully", "success")

    return redirect(url_for("task.view_task"))


@task_bp.route("/tasks/<int:task_id>", methods=["POST"])
def toggal_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()
    return redirect(url_for("task.view_task"))


@task_bp.route("/clear", methods=["POST"])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash("All tasks cleared", "info")
    return redirect(url_for("task.view_task"))
