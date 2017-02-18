<?php

/**
    * \fn
	* @brief Procédure d'envoi de mail basique
    * 
    * @param[in] $destinataire 			l'adresse email du destinataire
    * @param[in] $sujet 				l'objet du mail
    * @param[in] $message 				le contenu du message du mail
    */

function envoyerMail($destinataire, $sujet, $message) // Fonction de base d'envoi de mails
{
	$nom_service = "La cafetière intelligente ASI";
	$adresse_envoi = "asi-12-cafetiere@insa-rouen.fr";
	$adresse_reponse = "simon.rohou@insa-rouen.fr";
	$content_type = "text/plain";
	$charset = "iso-8859-1";
	$content_transfer_encoding = "8bit";
	
	$headers =	'From: "' . $nom_service . '"<' . $adresse_envoi . '>'."\n";
	$headers .=	'Reply-To: ' . $adresse_reponse ."\n";
	$headers .=	'Content-Type: ' . $content_type . '; charset="' . $charset . '"'."\n";
	$headers .=	'Content-Transfer-Encoding: ' . $content_transfer_encoding;
	
	return mail($destinataire, $sujet, $message, $headers);
}

function informerGerantQueBacEauVide()
{
	return envoyerMail("simon.rohou@gmail.com", "Le bac d'eau a besoin d'être rempli", "Test");
}

function informerGerantQueBacEauPlein()
{
	return envoyerMail("simon.rohou@gmail.com", "Le bac d'eau a été rempli", "Test");
}

?> 