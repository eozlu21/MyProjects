package main;

import twitter.Twitter;
import user.RegularUser;
import user.VerifiedUser;

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
		
		// Creating a Twitter object
		Twitter twitter = new Twitter();
		
		// Creating RegularUser object and sending Tweets
		RegularUser user1 = (RegularUser) twitter.addUser("Muhammet", "Regular");
		user1.sendTweet("Weather is so nice today!");
		user1.sendTweet("I wanna hang out with my friends.");
		user1.sendTweet("My paper has been published, I am so happy :D.");
		
		// Creating VerifiedUser object and sending Tweets
		VerifiedUser user2 = (VerifiedUser)twitter.addUser("Dogan", "Verified");
		user2.sendTweet("I have homework deadline for tonight.");
		user2.sendTweet("This weekend is my birthday.");
		user2.sendTweet("I will celebrate my birthday at yacht; who wants to join?");
		
		// Creating RegularUser object and sending Tweets
		RegularUser user3 = (RegularUser)twitter.addUser("Muge", "Regular");
		user3.sendTweet("I will watch my favorite TV show.");
		user3.sendTweet("My car is not working.");
		
		// Creating three VerifiedUser objects and sending Tweets
		VerifiedUser user4 = (VerifiedUser)twitter.addUser("Vahideh", "Verified");
		user4.sendTweet("I miss my family.");
		user4.sendTweet("I will return home after my last exam.");
		
		VerifiedUser user5 = (VerifiedUser)twitter.addUser("Kerem", "Verified");
		user5.sendTweet("I will join Dogan's birthday.");
		
		VerifiedUser user6 = (VerifiedUser)twitter.addUser("Canberk", "Verified");
		user6.sendTweet("I also will join Dogan's birthday party.");
		
		
		// Call displayAllTweets() method to display all Tweets
		twitter.displayAllTweets();
		
		System.out.println("------------------------------------");
		
		// delete tweet with index 1 from user 3
		user3.deleteTweet(1);
		
		// edit tweet with index 0 from user 2
		user2.editTweet(0, "I will go swimming with Burak.");

		// Call displayAllTweets() method to display all Tweets
		twitter.displayAllTweets();
		
		System.out.println("------------------------------------");
		
		// delete tweet with index 1 from user 1
		user1.deleteTweet(1);
		
		// edit tweet with index 0 from user 4
		user4.editTweet(0, "I also wanna join Dogan's birthday.");
		
		// Call displayAllTweets() method to display all Tweets
		twitter.displayAllTweets();
		
		// call calculateRevenue() method
		System.out.println("------------------------------------");
		System.out.println("Revenue for this month: " + twitter.calculateRevenue() + "$");

		user1.followUser(user2);
		user1.followUser(user3);
		user1.followUser(user4);

		user1.displayFollowedUserTweets();

		twitter.displayInteractions();
		
		// attempting to add a user with an invalid type
		System.out.println("------------------------------------");
		twitter.addUser("Hilal", "Special");
	}

}
