<?php
include("../includes/fonctions.php");

if(!utilisateurEstIdentifie())
	include("../connexion/index.php");

else
{
	$titre = "Votre compte";
	include("../includes/haut.php");
	
	$requete_consommations = bdd_query($db, "SELECT * FROM consommations WHERE utilisateur=" . idUtilisateur() . " ORDER BY date DESC LIMIT 15");
	?>
		
	<script>
		// Script de gestion de sélection d'une liste d'entités (pages de paramétrage)
		$(document).ready(function()
		{
			// Enregistrement des modifications
			$("select,input[type=radio]").change(enregistrerPreferences);
			
			function selectionnerModeAutoAvecConfirmation()
			{
				selectionnerModeAuto(true);
			}
			
			function selectionnerModePersoAvecConfirmation()
			{
				selectionnerModePerso(true);
			}
			
			function selectionnerModeAuto(autoriser_confirmation)
			{
				var difference = $("#selection_automatique input[type=radio]").attr('checked');
				
				configurerCadreSelectionne($("#selection_automatique"),
											$("#selection_automatique input[type=radio]"),
											$("#selection_automatique select"));
													
				configurerCadreNonSelectionne($("#informations_souhait"),
											$("#informations_souhait input[type=radio]"),
											$("#informations_souhait select"));
											
				$("#selection_automatique img").attr('src', '<?php echo accesHttpRacine(); ?>design/img/automatique.png');
				enregistrerPreferences(autoriser_confirmation && difference != $("#selection_automatique input[type=radio]").attr('checked'));
			}
			
			function selectionnerModePerso(autoriser_confirmation)
			{
				var difference = $("#informations_souhait input[type=radio]").attr('checked');
				
				configurerCadreNonSelectionne($("#selection_automatique"),
												$("#selection_automatique input[type=radio]"),
												$("#selection_automatique select"));
													
				configurerCadreSelectionne($("#informations_souhait"),
												$("#informations_souhait input[type=radio]"),
												$("#informations_souhait select"));
												
				$("#selection_automatique img").attr('src', '<?php echo accesHttpRacine(); ?>design/img/automatique_noirblanc.png');
				enregistrerPreferences(autoriser_confirmation && difference != $("#informations_souhait input[type=radio]").attr('checked'));
			}
			
			function configurerCadreSelectionne(cadre, radio, checkbox)
			{
				// Changement de style
				cadre.removeClass("non_selectionne");
				
				// Désactivation des éléments intérieurs
				checkbox.attr('disabled', false);
				
				// Sélection sur le bouton radio
				radio.attr('checked','checked');
			}
			
			function configurerCadreNonSelectionne(cadre, radio, checkbox)
			{
				// Changement de style
				cadre.addClass("non_selectionne");
				
				// Désactivation des éléments intérieurs
				checkbox.attr('disabled', 'true');
				
				// Sélection sur le bouton radio
				radio.attr('checked', false);
			}
			
			function enregistrerPreferences(afficher_message_confirmation)
			{
				// Enregistrement...
				$(document).load("enregistrer_preferences.php?id=<?php echo idUtilisateur(); ?>" +
																"&date_inscription=<?php echo dateInscriptionUtilisateur(); ?>" + 
																"&mode=" + $('input[type=radio][name=base_selection]:checked').val() + 
																"&intensite=" + $("select[name=intensite] > option:selected").val() + 
																"&longueur=" + $("select[name=longueur] > option:selected").val() + 
																"&sucre=" + 1);
				
				if(afficher_message_confirmation)
				{
					// Pour éviter les problèmes d'affichage, on teste si le message est invisible
					if(!$("#parametres_prochaine_consommation+p.message_confirmation").is(":visible"))
					{
						// Apparition du texte de confirmation de l'enregistrement
						$("#parametres_prochaine_consommation+p.message_confirmation").hide().delay(500).fadeIn(800);
						
						// Puis le texte est effacé au bout de 4 secondes
						$("#parametres_prochaine_consommation+p.message_confirmation").delay(4000).fadeOut(800);
					}
				}
			}
			
			// Par défaut, on sélectionne l'un des deux cadres en fonctions du précédent choix de l'utilisateur
			<?php
			if(mysql_num_rows($requete_consommations) == 0) // Si aucune consommation n'a été enregistrée auparavant
			{
				?>
				selectionnerModePerso(false);
				<?php
			}
			
			else
			{
				if(preferenceEnAutomatique())
					echo "selectionnerModeAuto(false);";
				
				else
					echo "selectionnerModePerso(false);";
				?>
				
				// Lorsque l'utilisateur clic sur la sélection automatique
				$("#selection_automatique").click(selectionnerModeAutoAvecConfirmation);
					
				// Lorsque l'utilisateur clic sur les programmation d'une sélection
				$("#informations_souhait").click(selectionnerModePersoAvecConfirmation);
				<?php
			}
			?>
		});
	</script>

	<p class="intro">Sur cette page vous pouvez suivre vos consommations et paramétrer vos préférences.
	Celles-ci seront automatiquement mises à jour lors de votre prochain passage à la machine à café.
	<br /><br />
	Si vous souhaitez modifier les informations vous concernant, rendez-vous sur 
	<a href="editer_informations.php">la page d'édition de vos informations</a>.</p>

	<h1>Votre sélection habituelle</h1>
	
	<p>
		Votre <em>sélection habituelle</em> est celle qui vous sera automatiquement proposée lors de la préparation de votre prochain café.
		Souhaitez-vous que la machine vous propose le type de café que vous avez l'habitude de prendre ?
	</p>
	
	<div id="parametres_prochaine_consommation">
		<div id="selection_automatique">
			<center>
				<input type="radio" class="decision" name="base_selection" id="auto" value="1" <?php if(mysql_num_rows($requete_consommations) == 0) echo "disabled=\"disabled\""; ?>><br />
				<label for="auto" class="choix_principal">Selon mes habitudes</label>
			</center>
			
			<hr />
			
			<img alt="Sélection automatique" />
		</div>
		
		<div id="informations_souhait">
			<center>
				<input type="radio" class="decision" name="base_selection" id="perso" value="0"><br />
				<label for="perso" class="choix_principal">En programmant une sélection</label>
			</center>
			
			<hr />
			
			<ul>
				<li>Longueur :&nbsp;&nbsp; <?php Longueur::afficherChoix(getPreferenceLongueur()); ?></li>
				<li>Intensité &nbsp;:&nbsp;&nbsp; <?php Intensite::afficherChoix(getPreferenceIntensite()); ?></li>
				<li>Sucre : <?php Sucre::afficherChoix(getPreferenceSucre()); ?></li>
			</ul>
		</div>
	</div>
	
	<p class="message_confirmation">Vos préférences ont été enregistrées</p>
	<p>La sélection automatique qui vous est proposée s'inspire de vos récentes consommations.</p>
	
	
	<h1>Liste de vos récentes consommations</h1>
	
	<?php
	if(mysql_num_rows($requete_consommations) == 0)
		echo "<p>Vous n'avez encore jamais utilisé la machine à café !</p>";
	
	else
	{
		?>
		<table class="liste_consommations">
			<tr class="entete">
				<th>Café consommé le</th>
				<th>Longueur</th>
				<th>Intensité</th>
				<th>Sucre</th>
			</tr>
			
			<?php
			$k = 0;
			
			while($donnees_consommations = bdd_fetch_array($requete_consommations))
			{
				if($k == 1)
				{
					$k = 0;
					$background = " class=\"fond_impair\"";
				}
				
				else
				{	
					$background = "";
					$k ++;
				}
				?>
				<tr<?php echo $background; ?>>
					<td><?php echo dateTextuelle($donnees_consommations['date'], true, false, true); ?></td>
					<td><?php echo ucwords(Longueur::nom($donnees_consommations['longueur'])); ?></td>
					<td><?php echo ucwords(Intensite::nom($donnees_consommations['intensite'])); ?></td>
					<td><?php echo Sucre::equivalentBinaireTextuel($donnees_consommations['sucre']); ?></td>
				</tr>
				<?php
			}
			?>
		
		</table>
		<?php
	}
	
	include("../includes/fin.php");
}
?>