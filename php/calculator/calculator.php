<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scientific Calculator</title>
    <style>
        .calculator {
            width: 300px;
            margin: 50px auto;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <form method="post">
            <input type="text" name="expression" placeholder="Enter expression" autofocus>
            <button type="submit">Calculate</button>
        </form>
        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            if (isset($_POST["expression"])) {
                $expression = $_POST["expression"];
                // Evaluate the expression using eval() function
                $result = eval("return $expression;");
                if ($result !== FALSE) {
                    echo "<h2>Result: $result</h2>";
                } else {
                    echo "<h2>Error: Invalid expression</h2>";
                }
            }
        }
        ?>
    </div>
</body>
</html>
