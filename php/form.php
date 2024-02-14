<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>form</title>
</head>
<body style="justify-content: center; align-items: center">
    <form method="post" action="form.php">
       <label for="name">Name</label>
       <input type="text" name="name" required> <br>
       <label for="RollNo">RollNo</label>
       <input type="text" name="rollno" required><br>
       <button type="submit">Login</button>
    </form>
    <?php
    if($_POST){
    echo print_r($_POST);
    }
    ?>
</body>
</html>