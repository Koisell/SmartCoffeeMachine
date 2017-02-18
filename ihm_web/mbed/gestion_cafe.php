<?php
include("../includes/fonctions.php");

if(isset($_GET['boisson_prete']))
	signalerFinDePreparationDuCafe();

if(isset($_GET['boisson_en_preparation']))
	signalerPreparationEnCours();

$requete = bdd_query($db, "SELECT demande_cafe, demande_cafe_longueur, demande_cafe_intensite FROM parametres");
$donnees = bdd_fetch_array($requete);
	
echo $donnees['demande_cafe'] . "/" . $donnees['demande_cafe_longueur'] . "/" . $donnees['demande_cafe_intensite'];
?>