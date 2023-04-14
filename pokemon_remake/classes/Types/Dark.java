package classes.Types;
import java.util.ArrayList;

public class Dark extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Dark() {
        
        super(15, "Dark", weaknesses, resistances);
        weaknesses.add(new Fighting());
        weaknesses.add(new Bug());
        weaknesses.add(new Fairy());
        resistances.add(new Ghost());
        resistances.add(new Dark());
        resistances.add(new Psychic());
        
    }

}