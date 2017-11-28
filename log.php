<?php
 
?>
<!DOCTYPE html>
<html>
<head> 
	<?php

	
	if(isset($_POST['login']))
	{  	
	if($_POST['user'] == 'admin' && $_POST['pass'] == 'acza')
	{
		echo "<h2>hello</h2>";
	}
	else
	{
		echo "<h2>sorry</h2>";
	}
}
	 
?>

            
            <form id="form1" method="POST" action="log.php" accept-charset="UTF-8" role="form" >
            <input type="text" name="user" class="form-control input-sm chat-input" placeholder="username" />
            </br>
            <input type="password"  name="pass" class="form-control input-sm chat-input" placeholder="password" />
            </br>
            <div class="wrapper">
            <span class="group-btn">    
 			<button type="submit"   form="form1" class="form-control" value="Submit" name="login"> Login</button>
 	 
            </span>  
            </div> 
            </form>  
            
