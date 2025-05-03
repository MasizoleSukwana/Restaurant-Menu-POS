from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
menu_items = []
id_counter = 1

@app.route("/")
def index():
    return render_template("index.html", menu=menu_items)

@app.route("/create", methods=["GET", "POST"])
def create():
    global id_counter
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = float(request.form["price"])
        menu_items.append({
            "id": id_counter,
            "name": name,
            "description": description,
            "price": price
        })
        id_counter += 1
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit(item_id):
    item = next((i for i in menu_items if i["id"] == item_id), None)
    if request.method == "POST":
        item["name"] = request.form["name"]
        item["description"] = request.form["description"]
        item["price"] = float(request.form["price"])
        return redirect(url_for("index"))
    return render_template("edit.html", item=item)

@app.route("/delete/<int:item_id>")
def delete(item_id):
    global menu_items
    menu_items = [i for i in menu_items if i["id"] != item_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
