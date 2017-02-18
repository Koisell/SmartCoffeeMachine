<?php
/*!	\file
 * 	@brief Fonctions diverses de l'application : manipulation de variables de base
 * 
 * 	@version 	2.1
 *	@author 	Équipe ECAO
 * 	@date		décembre 2012
 */

function decouper($chaine, $debut, $longueur)
{
	return mb_substr($chaine, $debut, $longueur, 'UTF-8');
}

function enMinuscules($chaine)
{
	return mb_strtolower($chaine, 'UTF-8');
}

function enMajuscules($chaine)
{
	return mb_strtoupper($chaine, 'UTF-8');
}

function estVide($chaine)
{
	return (empty($chaine) && $chaine != "0") || $chaine == null || $chaine == "NULL";
}


/**
    * \fn
	* @brief Fonction mettant en forme une courte chaine
    * 
    * Il s'agit de mettre une majuscule sur chaque initiale, excepté pour les mots de liaison
    * 
    * @param[in] $chaine 			la chaine à mettre en forme
    * @return 						la chaine mise en forme
    */
    
function miseEnFormeCourteChaine($chaine)
{
	$chaine = enMinuscules($chaine);
	
	$majuscule = true;
	$chaine_normalisee = "";
	
	// Suppresion des underscores dans la chaine
	$chaine = str_replace('_', '\'', $chaine);
	
	for($i = 0 ; $i < strlen($chaine) ; $i++)
	{
		$lettre = decouper($chaine, $i, 1);
		
		if($lettre == '-' || $lettre == ' ' || $lettre == '\'')
		$majuscule = true;
		
		elseif(!empty($lettre) && $majuscule)
		{
			if((decouper($chaine, $i, 4) != "des " && // S'il ne s'agit pas d'un mot de liaison
				decouper($chaine, $i, 3) != "de " && 
				decouper($chaine, $i, 3) != "en " && 
				decouper($chaine, $i, 3) != "au " && 
				decouper($chaine, $i, 4) != "aux " && 
				decouper($chaine, $i, 2) != "d'" && 
				decouper($chaine, $i, 2) != "l'" && 
				decouper($chaine, $i, 3) != "du " && 
				decouper($chaine, $i, 4) != "rue " && 
				decouper($chaine, $i, 5) != "dans " && 
				decouper($chaine, $i, 4) != "les " && 
				decouper($chaine, $i, 3) != "of " && 
				decouper($chaine, $i, 4) != "for " && 
				decouper($chaine, $i, 4) != "the " && 
				decouper($chaine, $i, 4) != "and " && 
				decouper($chaine, $i, 2) != "a " && 
				decouper($chaine, $i, 3) != "as " && 
				decouper($chaine, $i, 3) != "et ") ||
				$i == 0)
			$lettre = enMajuscules($lettre); // L'initial est mise en majuscule
			
			$majuscule = false;
		}
       
		$chaine_normalisee .= $lettre;
	}
	
	$chaine_normalisee .= " ";
	
	// Sigles généraux
	$chaine_normalisee = str_replace("Bp ", "BP ", $chaine_normalisee);
	$chaine_normalisee = str_replace("Insa ", "INSA ", $chaine_normalisee);
	$chaine_normalisee = str_replace("I.n.s.a ", "I.N.S.A ", $chaine_normalisee);
	$chaine_normalisee = str_replace("S.a.r.l ", "S.A.R.L ", $chaine_normalisee);
	$chaine_normalisee = str_replace("Zi ", "ZI ", $chaine_normalisee);
	$chaine_normalisee = str_replace("Tp ", "TP ", $chaine_normalisee);
	$chaine_normalisee = str_replace("&amp;rsquo;", "'", $chaine_normalisee);
	$chaine_normalisee = str_replace("&rsquo;", "'", $chaine_normalisee);
	
	return rtrim($chaine_normalisee);
}




?>