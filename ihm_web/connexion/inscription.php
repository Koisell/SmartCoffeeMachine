<?php
include("../includes/fonctions.php");

if(isset($mise_a_jour_compte))
	$mise_a_jour_compte = true;

else
	$mise_a_jour_compte = false;

if(isset($_POST['envoi']))
{
	if(informationsValides($mise_a_jour_compte))
	{
		include("../includes/haut.php");
		
		if(enregistrerInformations())
		{
			identifierUtilisateur(enMinuscules($_POST['login_cafe']), null, true); // On force l'identification, puisque l'inscription est correcte
			echo "<p><br />Vos informations ont bien été enregistrées.<br /><br />Redirection...</p>";
			rediriger("../utilisateur", 4);
		}
		
		else
		{
			echo "<p><br /><strong class=\"erreur\">Erreur dans l'enregistrement de vos informations.</strong><br /><br />Redirection...</p>";
			rediriger("../connexion/inscription.php", 4);
		}
		
		include("../includes/fin.php");
		die();
	}
	
	if($mise_a_jour_compte)
	{
		$titre = "Mise à jour de vos informations";
		$texte_bouton_validation = "Mettre à jour";
	}

	else
	{	
		$titre = "Inscription à l'application";
		$texte_bouton_validation = "Valider l'inscription";
	}
	
	$valeur_clef = $_POST['clef_cafe'];
	$valeur_nom = $_POST['nom_cafe'];
	$valeur_prenom = $_POST['prenom_cafe'];
	$valeur_login = $_POST['login_cafe'];
}

else
{
	if($mise_a_jour_compte)
	{
		$titre = "Mise à jour de vos informations";
		$texte_bouton_validation = "Mettre à jour";
		
		$valeur_clef = $_SESSION['uid'];
		$valeur_nom = $_SESSION['nom'];
		$valeur_prenom = $_SESSION['prenom'];
		$valeur_login = $_SESSION['email'];
	}

	else
	{	
		$titre = "Inscription à l'application";
		$texte_bouton_validation = "Valider l'inscription";
		
		$valeur_clef = "";
		$valeur_nom = "";
		$valeur_prenom = "";
		$valeur_login = "@insa-rouen.fr";
	}
}

include("../includes/haut.php");

if(!utilisateurEstIdentifie() || $mise_a_jour_compte)
{
?>
	<p class="intro"></p>

	<h1><?php echo $titre; ?></h1>

	<p><?php
	if(isset($_POST['envoi']) && !informationsValides($mise_a_jour_compte))
	{
		echo "<strong class=\"erreur\">Attention : certaines informations entrées présentent des erreurs</strong>";
	}
	?></p>
	
	<p><?php
	if($mise_a_jour_compte)
		echo "Merci de vérifier que les informations suivantes sont valides :";
	
	else
		echo "Saisissez la clef d'inscription que vous a fourni la machine à café pour vous inscrire :";
	?></p>
	
	<form action="" method="post">
		<table class="formulaire_connexion">
			<tr>
				<th><label for="clef_cafe">La clef d'inscription : </label></th>
				<td>
					<input <?php if($mise_a_jour_compte) echo "disabled=\"disabled\""; ?> type="text" name="clef_cafe" id="clef_cafe" value="<?php echo $valeur_clef; ?>" />
					<?php if($mise_a_jour_compte) echo "<input type=\"hidden\" name=\"clef_cafe\" value=\"" . $valeur_clef . "\" />"; ?>
				</td>
			</tr>
			<?php inclureMessageErreurSiExistant('erreur_clef_cafe'); ?>
			<tr style="border-top: 1px solid #ddd;">
				<th><label for="nom_cafe">Votre nom : </label></th>
				<td><input type="text" name="nom_cafe" id="nom_cafe" value="<?php echo $valeur_nom; ?>" /></td>
			</tr>
			<?php inclureMessageErreurSiExistant('erreur_nom_cafe'); ?>
			<tr>
				<th><label for="prenom_cafe">Votre prénom : </label></th>
				<td><input type="text" name="prenom_cafe" id="prenom_cafe" value="<?php echo $valeur_prenom; ?>" /></td>
			</tr>
			<?php inclureMessageErreurSiExistant('erreur_prenom_cafe'); ?>
			<tr>
				<th><label for="login_cafe">Votre adresse mail : </label></th>
				<td><input type="text" name="login_cafe" id="login_cafe" value="<?php echo $valeur_login; ?>" /></td>
			</tr>
			<?php inclureMessageErreurSiExistant('erreur_login_cafe'); ?>
			<tr>
				<th><label for="mot_de_passe_cafe">Votre mot de passe : </label></th>
				<td><input type="password" name="mot_de_passe_cafe" id="mot_de_passe_cafe" value="" /></td>
			</tr>
			<?php inclureMessageErreurSiExistant('erreur_mot_de_passe_cafe'); ?>
			<tr>
				<th><label for="confirmation_mot_de_passe_cafe">Confirmez votre mot de passe : </label></th>
				<td><input type="password" name="confirmation_mot_de_passe_cafe" id="confirmation_mot_de_passe_cafe" value="" /></td>
			</tr>
			<tr>
				<th></th>
				<td><input type="submit" name="envoi" value="<?php echo $texte_bouton_validation; ?>" /></td>
			</tr>	
		</table>
	</form>

<?php
}

else
{
	?>
	
	<p><span class="erreur">Erreur :</span> Vous êtes déjà inscrit sur la plate-forme.</p>
	
	<?php
}

include("../includes/fin.php");




/*		Fonctions associées		*/

function informationsValides($simple_mise_a_jour)
{
	$informations_valides = true;
	
	// Réinitialisations
	$_POST['erreur_clef_cafe'] = null;
	$_POST['erreur_mot_de_passe_cafe'] = null;
	$_POST['erreur_prenom_cafe'] = null;
	$_POST['erreur_nom_cafe'] = null;
	$_POST['erreur_login_cafe'] = null;
	
	if(!$simple_mise_a_jour && !clefExisteEtEstLibre($_POST['clef_cafe']))
	{
		$informations_valides = false;
		$_POST['erreur_clef_cafe'] = "La clef n'est pas valide ou n'a jamais existée";
	}
	
	if($_POST['mot_de_passe_cafe'] != $_POST['confirmation_mot_de_passe_cafe'])
	{
		$informations_valides = false;
		$_POST['erreur_mot_de_passe_cafe'] = "Les deux mots de passe entrés ne correspondent pas";
	}
	
	if($_POST['prenom_cafe'] == "")
	{
		$informations_valides = false;
		$_POST['erreur_prenom_cafe'] = "Merci de bien indiquer votre prénom";
	}
	
	if($_POST['nom_cafe'] == "")
	{
		$informations_valides = false;
		$_POST['erreur_nom_cafe'] = "Merci de bien indiquer votre nom";
	}
	
	if($_POST['mot_de_passe_cafe'] == "")
	{
		$informations_valides = false;
		$_POST['erreur_mot_de_passe_cafe'] = "Merci d'entrer un mot de passe";
	}
	
	if(!preg_match("#^[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$#", $_POST['login_cafe']))
	{
		$informations_valides = false;
		$_POST['erreur_login_cafe'] = "L'adresse email entrée n'est pas valide";
	}
	
	if(emailExisteDeja($_POST['login_cafe'], $simple_mise_a_jour))
	{
		$informations_valides = false;
		$_POST['erreur_login_cafe'] = "L'adresse email référence déja un autre compte";
	}
	
	return $informations_valides;
}

function inclureMessageErreurSiExistant($nom_variable_post)
{
	if(isset($_POST[$nom_variable_post]))
	{
		echo "<tr>
				<th></th>
				<td class=\"erreur\">" . $_POST[$nom_variable_post] . "</td>
			</tr>";
	}
}


function enregistrerInformations()
{
	// Les informations sont mises à jour dans la BDD
	return bdd_query($db, "UPDATE utilisateurs SET 
						prenom='" . filtreSecurite(miseEnFormeCourteChaine($_POST['prenom_cafe'])) . "',
						nom='" . filtreSecurite(miseEnFormeCourteChaine($_POST['nom_cafe'])) . "',
						email='" . filtreSecurite(enMinuscules($_POST['login_cafe'])) . "',
						mot_de_passe='" . filtreSecurite(md5($_POST['mot_de_passe_cafe'])) . "',
						date_inscription='" . time() . "',
						date_derniere_visite='" . time() . "'
					WHERE uid='" . filtreSecurite(enMinuscules($_POST['clef_cafe'])) . "'");
}


function filtreSecurite($chaine)
{
	return htmlentities($chaine, ENT_QUOTES);
}


function emailExisteDeja($email, $simple_mise_a_jour)
{
	if($simple_mise_a_jour) // Si l'utilisateur est actuellement connecté, on ne veut pas confondre avec son adresse mail actuellement enregistrée
		$restriction = " AND id!='" . idUtilisateur() . "' ";
	
	else
		$restriction = "";
		
	$requete = bdd_query($db, "SELECT COUNT(*) AS nb_emails 
								FROM utilisateurs 
								WHERE email='" . enMinuscules($email) . "'" . $restriction);
	$donnees = bdd_fetch_array($requete);
	
	return $donnees['nb_emails'] > 0;
}


function clefExisteEtEstLibre($clef)
{
	// On cherche à savoir si cette clef représente une entrée dans la base et si cette entrée n'a pas déja fait l'objet d'une inscription
	$requete = bdd_query($db, "SELECT COUNT(*) AS nb_clefs 
								FROM utilisateurs 
								WHERE uid='" . enMinuscules($clef) . "' AND prenom=''");
	$donnees = bdd_fetch_array($requete);
	return $donnees['nb_clefs'] == 1;
}

?>
