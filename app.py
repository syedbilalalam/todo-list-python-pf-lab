from flask import Flask, render_template, request, redirect, url_for, session

# Flask initialization code
app = Flask(__name__)
app.secret_key = "P-TODO-APP"

# Route for / as home page
@app.route("/")
def home():
    todo_list = session.get("todo_list") or [] # If the list is not in session the empty list

    # Checking for list filter request
    filter = request.args.get("filter") or "default"
    
    list_to_be_rendered = []
    
    if filter == "completed":
        for todo in todo_list:
            if todo['completed']:
                list_to_be_rendered.append(todo)   

    elif filter == "incomplete":
        for todo in todo_list:
            if not todo['completed']:
                list_to_be_rendered.append(todo)
    
    else:
        for todo in todo_list:
            list_to_be_rendered.append(todo)

    return render_template(
        "index.html",
        todo_list = list_to_be_rendered,
        todo_list_length = len(list_to_be_rendered)
    )

# Route for adding a new todo to the todo list
@app.route("/add/todo", methods=["POST"])
def add_todo():
    todo_list = session.get("todo_list") or [] # fetching todo list from session
    todo_name = request.form["todo"]           # checking the todo name what user given in form

    # Add this new todo to the todo list
    todo_list.append({
        "name": todo_name,
        "completed": False,
        "in_edit_mode": False
    })

    # Saving new list to the session
    session["todo_list"] = todo_list

    return redirect(url_for('home'))

# Route for deleting a todo
@app.route("/delete/todo", methods=["POST"])
def delete_todo():
    todo_list = session.get("todo_list") or [] # fetching todo list from session

    # Fetching index with proper error handling
    index = None
    try:
        index = int(request.form["index"]) # Index of the target element
        
        # deleting todo from the list
        del todo_list[index]

        # Saving new list to the session
        session["todo_list"] = todo_list

    except:
        return redirect(url_for('home'))

    return redirect(url_for('home'))

# Route for starting an edit on todo app
@app.route("/start/edit/todo", methods=["POST"])
def start_edit_todo():
    todo_list = session.get("todo_list") or [] # fetching todo list from session

    # Fetching index with proper error handling
    index = None
    try:
        index = int(request.form["index"]) # Index of the target element
    except:
        return redirect(url_for('home'))

    # Marking that index as in edit mode
    todo_list[index]["in_edit_mode"] = True
    
    # Saving new list to the session
    session["todo_list"] = todo_list

    return redirect(url_for('home'))

# Route for updating the todo name
@app.route("/edit/todo", methods=["POST"])
def edit_todo():
    todo_list = session.get("todo_list") or [] # fetching todo list from session
    new_todo_name = request.form["value"]

    # Fetching index with proper error handling
    index = None
    try:
        index = int(request.form["index"]) # Index of the target element
    except:
        return redirect(url_for('home'))

    todo_list[index]["name"] = new_todo_name
    todo_list[index]["in_edit_mode"] = False
    
    # Saving new list to the session
    session["todo_list"] = todo_list

    return redirect(url_for('home'))

# Route for updating completion status
@app.route("/update/completion", methods=["POST"])
def update_completion():
    todo_list = session.get("todo_list") or [] # fetching todo list from session

    # Fetching index with proper error handling
    index = None
    try:
        index = int(request.form["index"]) # Index of the target element
    except:
        return redirect(url_for('home'))

    # Toggling the completion status from completed to not completed or vice versa
    todo_list[index]["completed"] = not(todo_list[index]["completed"])

    # Saving new list to the session
    session["todo_list"] = todo_list

    return redirect(url_for('home'))


# The following command will start the backend in debug mode
# Debug mode se error dhond ne mea aasani hoti hy
if __name__ == "__main__":
    app.run(debug=True)
