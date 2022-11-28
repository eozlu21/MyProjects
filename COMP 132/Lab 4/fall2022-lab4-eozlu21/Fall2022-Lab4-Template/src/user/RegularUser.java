package user;

public class RegularUser extends User{

    
    public RegularUser(String content) {
        super(content);
        this.type = "Regular";
    }

    public void deleteTweet(int id) {
        this.getTweets().remove(id);
        this.setTweetCount(this.getTweetCount() - 1);
    }

    @Override
    public void displayTweets() {
        System.out.println("(Regular) " + this.getUsername() + ":");
        for (twitter.Tweet tweet: this.getTweets()) {
            System.out.printf("Tweet: %s", tweet.toString());
            System.out.println("");
        }
        System.out.println("");
    }

    

    
}
