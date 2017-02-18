<?php
include("../includes/fonctions.php");

// Sécurité : les transmissions d'infos ne se font que par des nombres (évite les injections SQL)
if(isset($_GET['id']) && is_numeric($_GET['id']) && 
	isset($_GET['date_inscription']) && is_numeric($_GET['date_inscription']) && 
	isset($_GET['mode']) && is_numeric($_GET['mode']) && 
	isset($_GET['intensite']) && is_numeric($_GET['intensite']) && 
	isset($_GET['longueur']) && is_numeric($_GET['longueur']) && 
	isset($_GET['sucre']) && is_numeric($_GET['sucre']))
{
	$resultat = bdd_query($db, "UPDATE utilisateurs 
								SET proposition_automatique='" . $_GET['mode'] . "',
								souhait_intensite='" . $_GET['intensite'] . "',
								souhait_longueur='" . $_GET['longueur'] . "',
								souhait_sucre='" . $_GET['sucre'] . "'
								WHERE id='" . $_GET['id'] . "' AND date_inscription='" . $_GET['date_inscription'] . "'");
	
	setPreferenceEnAutomatique($_GET['mode']);
	setPreferenceIntensite($_GET['intensite']);
	setPreferenceLongueur($_GET['longueur']);
	setPreferenceSucre($_GET['sucre']);
}

else
	echo "Erreur d'exécution.";
	
include("../includes/fin_fonctions.php");

?>