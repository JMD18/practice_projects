package classes.Types;
import java.util.ArrayList;

public class Fighting extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Fighting() {
        
        super(10, "Fighting", weaknesses, resistances);
        weaknesses.add(new Flying());
        weaknesses.add(new Psychic());
        weaknesses.add(new Fairy());
        resistances.add(new Rock());
        resistances.add(new Bug());
        resistances.add(new Dark());

    }

}