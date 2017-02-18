<?php
include("../includes/fonctions.php");

if(isset($_GET['fin_purge']))
	signalerFinDePurge();

if(isset($_GET['purge_en_cours']))
	signalerPurgeEnCours();

$requete = bdd_query($db, "SELECT demande_purge FROM parametres");
$donnees = bdd_fetch_array($requete);
	
echo $donnees['demande_purge'];
?>