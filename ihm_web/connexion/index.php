<?php
include("../includes/fonctions.php");

if(utilisateurEstIdentifie())
{
	$titre = "Déconnexion de l'application";

	include("../includes/haut.php");
	
		deconnecterUtilisateur();
		rediriger(accesHttpRacine());
		echo "<p><br />Vous êtes maintenant déconnecté.<br /><br />Redirection...</p>";
	
	include("../includes/fin.php");
}

else
{
	$titre = "Connexion à l'application";

	include("../includes/haut.php");
		
	if(isset($_POST['login_cafe']) && isset($_POST['mot_de_passe_cafe']))
	{
		if(identifierUtilisateur($_POST['login_cafe'], $_POST['mot_de_passe_cafe']))
		{
			echo "<p><br />Vous êtes maintenant connecté à la plate-forme.<br /><br />Redirection...</p>";
			rediriger(accesHttpRacine() . "utilisateur/index.php");
		}
		
		else
		{
			echo "<p><br /><strong class=\"erreur\">Échec de la connexion, mauvaise identification.</strong>.<br /><br />Redirection...</p>";
			rediriger(accesHttpRacine() . "connexion/index.php");
		}
	}

	else
	{
		?>
			<p class="info">Pour régler vos préférences et accéder aux services en ligne de la machine à café, merci de bien vouloir entrer vos identifiants :</p>
			
			<form action="" method="post">
				<table class="formulaire_connexion">
					<tr>
						<th><label for="login_cafe">Votre adresse mail : </label></th>
						<td><input type="text" name="login_cafe" id="login_cafe" value="" /></td>
					</tr>
					<tr>
						<th><label for="mot_de_passe_cafe">Votre mot de passe : </label></th>
						<td><input type="password" name="mot_de_passe_cafe" id="mot_de_passe_cafe" value="" /></td>
					</tr>
					<tr>
						<th></th>
						<td><input type="submit" value="Se connecter" /></td>
					</tr>	
				</table>
			</form>
		<?php
	}
	
	include("../includes/fin.php");
}

?>