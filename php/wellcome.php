<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>wellcome php</title>
</head>
<body>
    <h2>Hello php</h2>
    <?php
       echo "hello<br>\n";
     echo "Date is: " .date('j-m-y,h:i:s');
    ?>
    <h2>join strings</h2>
    <?php
    $name1='jothi';
    $name2='Ram';             # dot operator used for concadination
    $name=$name1.' '.$name2;
    echo "$name1 <br>\n";
    print "$name2 <br>\n";        
    echo"$name is successfuly joined";
    ?> 
    <h2>indexed array</h2>
    <?php 
      $array=['j','r','c'];
      $array[]='m';
      print_r($array);
      echo "\n<br>$array[2]<br>";
    ?>
    <h2>ASSociate Array</h2>
    <?php 
      $ass_arr=[
        'name'=>'Jothi Ram',
        'Age'=>'20',
         'profession'=>'student'             
      ];
     print_r($ass_arr);
     echo"<br>";
     $ass_arr['Id']='003';
     print_r($ass_arr);
     echo '<br>';
     echo $ass_arr['name'].' '."C M";
    ?>
    <h1>operators</h1>
    <h3>arithmatic operator</h3>
    <?php $a=10; $b=2;
     $c=$a+$b.'<br>';
     $c.=$a-$b.'<br>';
     $c.=$a*$b.'<br>';
     $c.=$a/$b.'<br>';
     echo "$c";
     $d=$a%$b.'<br>';
     print $d
    ?>
    <h2>statements</h2>
    <?php 
       $a=20; $b=10; $c=5;
       if($a>$b && $a>$c){
        echo $a.'is greater';
       }
       else if ($b>$a && $b>$c){
        echo "$b is greater";
       }
       else{ echo "$c is greater";
    }
    ?>
    <h2>include files</h2>
    <?php
      include"jr.php";
    ?>
</body>
</html>