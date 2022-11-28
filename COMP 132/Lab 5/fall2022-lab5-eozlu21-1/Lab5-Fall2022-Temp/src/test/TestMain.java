package test;

import java.util.ArrayList;

import starWar.*;

public class TestMain {

/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted at the course website and (3) any study notes handwritten by myself.
I have not used, accessed or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME AND STUDENT ID
SIGNATURE: Ege Erdem Özlü, 80481
********************************************************************************/

	public static void boostHealths(ArrayList<ForceWielder> allCharacters){
		for (ForceWielder character : allCharacters){
			if (character instanceof IHealthBoostable){
				if (character instanceof Master){
					((Master) character).healthBoost();
				}
				else if (character instanceof Jedi){
					((Jedi) character).healthBoost();
				}
			}
		}
	}

	

	public static void main(String[] args) {
		
		// An ArrayList for collecting all the characters
		ArrayList<ForceWielder> allCharacters = new ArrayList<ForceWielder>();
		
		// Creating the objects of the characters
		Jedi jedi1 = new Jedi("Yoda", 30, 100, 40, "green", 0);
		Knight knight1 = new Knight("Obi-Wan Kenobi", 12, 100, 25, "blue", 0, null);
		Padawan padawan1 = new Padawan("Anakin Skywalker", 5, 0, 20, "blue", 0, knight1);
		
		knight1.setPadawan(padawan1);
		
		Sith sith1 = new Sith("Kont Dooku", 20, 150, 20, 0);
		Master master1 = new Master("Darth Sidious", 40, 200, 30, 0, null);
		Apprentice apprentice1 = new Apprentice("Darth Maul", 15, 175, 25, 0, master1);
		
		master1.setApprentice(apprentice1);
		
		System.out.println("-------------------------information--------------------------------");
		
		// Appending all the characters to the ArrayList
		allCharacters.add(jedi1);
		allCharacters.add(knight1);
		allCharacters.add(padawan1);
		allCharacters.add(sith1);
		allCharacters.add(master1);
		allCharacters.add(apprentice1);
		
		// Displaying the information of characters
		for (ForceWielder character : allCharacters) {
			System.out.println(character);
		}
		
		System.out.println("--------------------------------------------------------------------");

		jedi1.revealLightsaber();
		
		System.out.println("--------------------------------------------------------------------");
		jedi1.saberFight(sith1);
		sith1.saberFight(jedi1);
		
		System.out.println("--------------------------------------------------------------------");
		jedi1.heal();

		knight1.revealLightsaber();
		padawan1.revealLightsaber();
		
		master1.shockJedi(padawan1);
		

		knight1.healPadawan();

		padawan1.confuseSith(apprentice1);

		apprentice1.chokeJedi(knight1);
		
		System.out.println("--------------------------------------------------------------------");

		apprentice1.betrayMaster();

		for (ForceWielder character : allCharacters) {
			System.out.println(character);
		}

		boostHealths(allCharacters);

		System.out.println("------------------------Health Boosts to characters--------------------------------------------");
		for (ForceWielder character : allCharacters) {
			System.out.println(character);
		}
	}

}
