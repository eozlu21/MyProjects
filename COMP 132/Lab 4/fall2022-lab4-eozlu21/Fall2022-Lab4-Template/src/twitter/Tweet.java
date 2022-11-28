package twitter;

public class Tweet {

    private String content;

    public Tweet(String content) {
        this.content = content;
    }

    public String getContent() {
        return this.content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public void edit(String newContent) {
        this.content = newContent;
    }

    public String toString() {
        return this.content;
    }

}
