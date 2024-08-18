from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import datetime


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feed')
def feed():
    conn = get_db_connection()
    posts = conn.execute('''
        SELECT workout_posts.title, workout_posts.favourite, workout_posts.routine, users.display_name 
        FROM workout_posts
        JOIN users ON workout_posts.user_id = users.id
    ''').fetchall()
    conn.close()
    return render_template('feed.html', posts=posts)

@app.route('/kitchen')
def kitchen():
    conn = get_db_connection()
    recipes = conn.execute('''
        SELECT kitchen_posts.recipe_title, kitchen_posts.ingredients, kitchen_posts.recipe, users.display_name 
        FROM kitchen_posts
        JOIN users ON kitchen_posts.user_id = users.id
    ''').fetchall()
    conn.close()
    return render_template('kitchen.html', recipes=recipes)


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('loginpage.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        display_name = request.form['display_name']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password, display_name) VALUES (?, ?, ?)', (username, password, display_name))
        conn.commit()
        conn.close()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/workoutpost', methods=('GET', 'POST'))
def workoutpost():
    if request.method == 'POST':
        title = request.form['workout_title']
        favourite = request.form['favourite']
        routine = request.form['routine']
        user_id = session['user_id'] 
        
        conn = get_db_connection()
        conn.execute('INSERT INTO workout_posts (title, favourite, routine, user_id) VALUES (?, ?, ?, ?)', 
                     (title, favourite, routine, user_id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('feed'))
    return render_template('workoutpost.html')


@app.route('/kitchenpost', methods=('GET', 'POST'))
def kitchenpost():
    if request.method == 'POST':
        recipe_title = request.form['recipetitle']
        ingredients = request.form['ingredientlist']
        recipe = request.form['recipe']
        user_id = session['user_id']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO kitchen_posts (recipe_title, ingredients, recipe, user_id) VALUES (?, ?, ?, ?)', 
                     (recipe_title, ingredients, recipe, user_id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('kitchen'))
    return render_template('kitchenpost.html')



if __name__ == '__main__':
    app.run(debug=True)
