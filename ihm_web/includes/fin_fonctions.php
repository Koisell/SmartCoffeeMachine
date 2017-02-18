<?php

if(isset($connection_BDD) && $connection_BDD) // Déconnexion de MySQL
{
	bdd_close($connection_BDD);
}

?>
