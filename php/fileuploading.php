<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>files uploading</title>
</head>
<body>
<form action=
le File Upload Using PHP in Tamil
enctype="multipart/form-data" method="post" id="frm">
<h2>Upload Multiple Files Using PHP</h2>
<label for='upload'>Select Files to Upload :< /label>
<input id='file' name="file[]" type="file" multiple="multiple" />
<p><input type="submit" name="submit" value="Submit"></p>
</form>
<?php
if(isset($_POST['submit']))
{
if (count($_FILE['file'] ['name']) >0) 

 for($i=0;$i<count($_FILE['file'] ['name']);$i++)
{

$tmp=$_FILES['file'] ['tmp_name'] [$i];
 if ($tmp !="")
   {
     $name=$_FILES['file'] ['name'] [$i];
      $path="Files/".$FILES ['file'] ['name'] [$i];
      if (move_uploaded_file($tmp, $path) )
        {
          $files[]=$name;
        }
    }
 }
 if (is_array($files) )
{
echo "Uploaded Successufully";
}
}
?>
</body>
</html>