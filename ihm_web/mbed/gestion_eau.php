<?php
include("../includes/fonctions.php");

if(isset($_GET['bac_vide']))
	signalerManqueEau();

if(isset($_GET['bac_plein']))
	signalerRechargeEau();
	
if(isset($_GET['dist']))
	enregistrerDistance($_GET['dist']);
?>