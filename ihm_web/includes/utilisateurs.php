<?php

function prenomUtilisateur()
{
	if(isset($_SESSION['prenom']))
		return $_SESSION['prenom'];
	
	else
		return null;
}

function nomUtilisateur()
{
	if(isset($_SESSION['nom']))
		return $_SESSION['nom'];
	
	else
		return null;
}

function idUtilisateur()
{
	if(isset($_SESSION['id']))
		return $_SESSION['id'];
	
	else
		return null;
}

function dateInscriptionUtilisateur()
{
	if(isset($_SESSION['date_inscription']))
		return $_SESSION['date_inscription'];
	
	else
		return null;
}

function utilisateurEstIdentifie()
{
	return isset($_SESSION['identification']);
}

function preferenceEnAutomatique()
{
	return isset($_SESSION['proposition_automatique']) && $_SESSION['proposition_automatique'] == '1';
}

function getPreferenceLongueur()
{
	if(isset($_SESSION['souhait_longueur']))
		return $_SESSION['souhait_longueur'];
	
	else
		return null;
}

function getPreferenceIntensite()
{
	if(isset($_SESSION['souhait_intensite']))
		return $_SESSION['souhait_intensite'];
	
	else
		return null;
}

function getPreferenceSucre()
{
	if(isset($_SESSION['souhait_sucre']))
		return $_SESSION['souhait_sucre'];
	
	else
		return null;
}

function setPreferenceLongueur($preference)
{
	$_SESSION['souhait_longueur'] = $preference;
}

function setPreferenceIntensite($preference)
{
	$_SESSION['souhait_intensite'] = $preference;
}

function setPreferenceSucre($preference)
{
	$_SESSION['souhait_sucre'] = $preference;
}

function setPreferenceEnAutomatique($preference)
{
	$_SESSION['proposition_automatique'] = $preference;
}
    
function identifierUtilisateur($login, $mot_de_passe, $forcer_identification = false)
{
	// Récupération des informations du compte de l'utilisateur dans la base
	$requete = bdd_query($db, "SELECT * FROM utilisateurs WHERE email='" . $login . "' LIMIT 1");
	$donnees = bdd_fetch_array($requete);
	
	if($forcer_identification || md5($mot_de_passe) == $donnees['mot_de_passe'])
	{
		// L'utilisateur s'est bien identifié
		$_SESSION['identification'] = true;
		
		// Mise à jour des autres sessions
		$_SESSION['prenom'] = $donnees['prenom'];
		$_SESSION['nom'] = $donnees['nom'];
		$_SESSION['email'] = $donnees['email'];
		$_SESSION['date_inscription'] = $donnees['date_inscription'];
		$_SESSION['date_derniere_visite'] = $donnees['date_derniere_visite'];
		setPreferenceIntensite($donnees['souhait_intensite']);
		setPreferenceLongueur($donnees['souhait_longueur']);
		setPreferenceSucre($donnees['souhait_sucre']);
		$_SESSION['proposition_automatique'] = $donnees['proposition_automatique'];
		$_SESSION['uid'] = $donnees['uid'];
		$_SESSION['id'] = $donnees['id'];
		
		return true;
	}
	
	else
		return false;
}
    
function deconnecterUtilisateur()
{
	session_destroy();
}

?>
