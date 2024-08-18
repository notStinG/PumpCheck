<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <img src="{{ url_for('static', filename='dbbg.jpeg') }}">
    <h2>Login</h2>
    <form method="POST">
        <label for="username">Username</label>
        <input type="text" name="username" id="username" required><br><br>
        <label for="password">Password</label>
        <input type="password" name="password" id="password" required><br><br>
        <button type="submit">Login</button>
    </form><br>
    <form action="{{ url_for('register') }}">
        <button type="submit">Don't have an account? Register here</button>
    </form>
</body>
</html>
