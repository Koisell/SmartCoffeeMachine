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

function enregistrerDistance($dist)
{
	$requete = bdd_query($db, "UPDATE parametres SET distance=" . $dist);
}

function demanderUnCafe($parametre_longueur, $parametre_intensite)
{
	$requete = bdd_query($db, "UPDATE parametres 
							SET demande_cafe=1, 
								demande_cafe_longueur=" . $parametre_longueur . ", 
								demande_cafe_intensite=" . $parametre_intensite);
}

function signalerFinDePreparationDuCafe()
{
	$requete = bdd_query($db, "UPDATE parametres SET demande_cafe=0");
}

function machineLibre()
{
	$requete = bdd_query($db, "SELECT demande_cafe, demande_purge FROM parametres");
	$donnees = bdd_fetch_array($requete);
	
	return $donnees['demande_cafe'] == 0 && $donnees['demande_purge'] == 0;
}

function demanderUnePurge()
{
	$requete = bdd_query($db, "UPDATE parametres SET demande_purge=1");
}

function signalerFinDePurge()
{
	$requete = bdd_query($db, "UPDATE parametres SET demande_purge=0");
}

function signalerPurgeEnCours()
{
	$requete = bdd_query($db, "UPDATE parametres SET demande_purge=2");
}

function signalerPreparationEnCours()
{
	$requete = bdd_query($db, "UPDATE parametres SET demande_cafe=2");
}

?>