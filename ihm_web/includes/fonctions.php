<?php 

if(!isset($temoin_inclusion_fonctions))
{
	session_start();
	
	include("bdd.php");
	include("localisation.php");
	include("config_local.php");
	include("utilisateurs.php");
	include("dates.php");
	include("cafe.php");
	include("manipulations_variables.php");
	//include("mbed.php");
	include("mails.php");

	$temoin_inclusion_fonctions = true;
}

?>