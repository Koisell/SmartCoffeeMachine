<?php

function bacEauDeLaMachineEstVide()
{
	$requete = bdd_query($db, "SELECT bac_vide FROM parametres");
	$donnees = bdd_fetch_array($requete);
	
	return $donnees['bac_vide'] == 1;
}

function signalerManqueEau()
{
	$requete = bdd_query($db, "UPDATE parametres SET bac_vide=1");
	informerGerantQueBacEauVide();
}

function signalerRechargeEau()
{
	$requete = bdd_query($db, "UPDATE parametres SET bac_vide=0");
	informerGerantQueBacEauPlein();
}

?>