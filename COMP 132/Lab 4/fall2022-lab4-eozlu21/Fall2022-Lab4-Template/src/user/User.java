package user;

import java.util.ArrayList;

import twitter.Tweet;

public class User {

    private String username;
    private int id;
    private ArrayList<Tweet> tweets = new ArrayList<Tweet>();
    private static int idTracker;
    protected String type = "None";
    private ArrayList<User> followedUsers = new ArrayList<User>();
    private int tweetCount;

    public User(String username) {
        this.username = username;
        this.id = idTracker;
        idTracker++;
    }

    public ArrayList<User> getFollowedUsers() {
        return this.followedUsers;
    }

    public void setFollowedUsers(ArrayList<User> followedUsers) {
        this.followedUsers = followedUsers;
    }

    public int getTweetCount() {
        return this.tweetCount;
    }

    public void setTweetCount(int tweetCount) {
        this.tweetCount = tweetCount;
    }

    public String getType() {
        return this.type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getUsername() {
        return this.username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public ArrayList<Tweet> getTweets() {
        return this.tweets;
    }

    public void setTweets(ArrayList<Tweet> tweets) {
        this.tweets = tweets;
    }

    public void displayTweets(){
        System.out.println(this.username + ":");
        for (Tweet tweet: this.getTweets()) {
            System.out.printf("Tweet: %s", tweet.toString());
            System.out.println("");
        }
        System.out.println("");
    }

    public void sendTweet(String content) {
        this.tweets.add(new Tweet(content));
        tweetCount++;
    }

    public void followUser(User user){
        this.followedUsers.add(user);
    }

    public void displayFollowedUserTweets(){
        ArrayList<User> verifiedUsers = new ArrayList<User>();
        ArrayList<User> regularUsers = new ArrayList<User>();
        for (User user : this.followedUsers) {
            if (user.getType() == "Regular") {
                regularUsers.add((RegularUser)user);
            }
            else if (user.getType() == "Verified") {
                verifiedUsers.add((VerifiedUser)user);
            }
        } 
        for(User user: verifiedUsers){
            user.displayTweets();
        }
        for (User user : regularUsers){
            user.displayTweets();
        }
    }
}
