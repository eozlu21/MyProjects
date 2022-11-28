package main;

/* import java.util.Random;
import java.util.Scanner;

import numguessr.NumGuessr;
import numguessr.User;
 */
public class Main {

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

	public static void main(String[] args) {

		long a = System.currentTimeMillis();
		int x = 1;
		for (int i = 0; i < 10000; i++){
			x++;
			for (int k = 0; k < 10000; k++){
				x--;
				for (int j = 0; j < 10000; j++){
					x = 1;
				}
			}
		}
		
		long b = System.currentTimeMillis();
		System.out.println(a);
		System.out.println(b);
		System.out.println(b-a);
		System.out.println(x);

		/* // 1. Get 2 names for the users.

		Scanner input = new Scanner(System.in);
		System.out.println("User 1 Name:");
		String user1Name = input.next();
		System.out.println("User 2 Name:");
		String user2Name = input.next();
		
		// 2. Create 2 User objects using those names.
		
		User user1 = new User(user1Name);
		User user2 = new User(user2Name);

		// 3. Create a Numguessr object using 2 User objects.

		NumGuessr game = new NumGuessr(user1, user2);

		// 4. Create a loop for the 3 rounds of Numguessr

		for (int i = 1; i <= 3; i++) {
			
		

		// For each iteration of the loop:
			Boolean user1CorrectEntry = false;
			Boolean user2CorrectEntry = false;
			int user1Number = -1;
			int user2Number = -1;
		// 4.1. Get a number between 1 and 100 (both inclusive) from the first user.
			while (!user1CorrectEntry) {
			System.out.println(user1.toString() + " enter a number between 1 and 100 (both inclusive).");
			user1Number = input.nextInt();
			if (user1Number >= 1 && user1Number <= 100){
				user1CorrectEntry = true;
			}
			else {
				System.out.println("Wrong input is given. Try Again.");
			}
			}
			user1.setGuessedNumber(user1Number);
		// 4.2. Get a number between 1 and 100 (both inclusive) from the second user.
			while (!user2CorrectEntry) {
				System.out.println(user2.toString() + " enter a number between 1 and 100 (both inclusive).");
				user2Number = input.nextInt();
				if (user2Number >= 1 && user2Number <= 100){
					user2CorrectEntry = true;
				}
				else {
					System.out.println("Wrong input is given. Try Again.");
				}
				}
				user2.setGuessedNumber(user2Number);

		// 4.3. Play a round of Numguessr with a computer generated random number.
				game.play(getRandomNumber());
		}
		input.close();
		// 5. At the end, announce the winner.
		game.whoWon();
	}

	// Use this method to get a random number from computer between 1 and 100 (both inclusive).
	public static int getRandomNumber() {
		return new Random().nextInt(100) + 1; */
	}
}
