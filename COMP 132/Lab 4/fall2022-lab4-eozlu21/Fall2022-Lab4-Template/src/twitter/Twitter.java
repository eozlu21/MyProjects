package twitter;

import java.util.ArrayList;

import user.RegularUser;
import user.User;
import user.VerifiedUser;

public class Twitter {

    private ArrayList<User> users = new ArrayList<User>();

    public Twitter() {
    }

    public User addUser(String username, String type) {
        User newUser;
        if (type == "Regular") {
            newUser = new RegularUser(username);
        }
        else if (type == "Verified") {
            newUser = new VerifiedUser(username);
        }

        else {
            System.out.printf("No such user type: %s \n", type);
            newUser = new User(username);
        }
        this.users.add(newUser);
        return newUser;
    }
    public int calculateRevenue(){
        int counter = 0;
        for (User user : users) {
            if (user.getType() == "Verified") {
                counter++;
            }
        }
        return (counter*8);
    }

    public void displayAllTweets(){
        for (User user : users) {
            user.displayTweets();
        }

    }

    public void displayInteractions(){
        int verifiedCount = 0;
        int regularCount = 0;
        for (User user : users){
            if (user.getType() == "Regular"){
                regularCount += user.getTweetCount();
            }
            else if (user.getType() == "Verified"){
                verifiedCount += user.getTweetCount();
            }
        }
        System.out.printf("Total Number of Tweets: %s\n", verifiedCount + regularCount);
        System.out.printf("Number of tweets from verified users: %s\n", verifiedCount);
        System.out.printf("Number of tweets from regular users: %s\n", regularCount);
    }

}
