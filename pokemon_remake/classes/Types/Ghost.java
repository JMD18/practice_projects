package classes.Types;
import java.util.ArrayList;

public class Ghost extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Ghost() {
        
        super(11, "Ghost", weaknesses, resistances);
        weaknesses.add(new Ghost());
        weaknesses.add(new Dark());
        resistances.add(new Psychic());
        resistances.add(new Normal());
        
    }

}