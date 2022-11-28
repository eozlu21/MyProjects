package simulation;
import java.util.ArrayList;

public class Training {

    private String title;
    private String code;
    private ArrayList<Intern> interns = new ArrayList<Intern>();


    public String getTitle() {
        return this.title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getCode() {
        return this.code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public ArrayList<Intern> getInterns() {
        return this.interns;
    }

    public void setInterns(ArrayList<Intern> interns) {
        this.interns = interns;
    }


    public Training(String title, String code){
        this.title = title;
        this.code = code;
    }

    public void appendIntern(Intern intrn){
        interns.add(intrn);
    }

    public ArrayList<String> getInternList(){
        ArrayList<String> strList = new ArrayList<String>();

        for (Intern iterIntern : this.interns){
            strList.add(iterIntern.getName());
        }
        return strList;
    }



}
