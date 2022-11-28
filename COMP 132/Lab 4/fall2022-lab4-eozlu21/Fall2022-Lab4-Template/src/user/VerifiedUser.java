package user;

public class VerifiedUser extends User {


    public VerifiedUser(String content) {
        super(content);
        this.type = "Verified";
    }
    
    public void editTweet(int id, String newContent) {
        this.getTweets().get(id).setContent(newContent);
    }

    @Override
    public void displayTweets() {
        System.out.println("(Verified) " + this.getUsername() + ":");
        for (twitter.Tweet tweet: this.getTweets()) {
            System.out.printf("Tweet: %s", tweet.toString());
            System.out.println("");
        }
        System.out.println("");
    }
}
