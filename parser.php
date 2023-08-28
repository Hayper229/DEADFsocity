#!/bin/php
<?php
//echo "hi";
function parse() {
     $ht=file_get_contents("http://www.google.com");
     echo $ht ;
}
parse();
//$pr=shell_exec('ls -a');
//echo "id: ";
//$sys=shell_exec('id ');
//echo $sys;

//echo "OS: ";
//$sys=shell_exec('uname -a');
//echo $sys;

// file_get_contents
// file_get_html
//SYStem shell command :shell _exec
//system
?>
