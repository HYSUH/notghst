from flask import Flask
app = Flask(__name__)

@app.route('/users/<string:username>')
def get_user(username):
    return 'Hello {}'.format(username)


@app.route('/recipe/<int:recipeId>')
def get_receipe(recipeId):
    return 'Hello recepie Id {}'.format(recipeId)


@app.route('/ingredients/<int:ingredientId>')
def get_ingredient(ingredientId):
    return 'Hello Ingredient Id {}'.format(ingredientId)