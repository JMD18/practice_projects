package classes.Types;
import java.util.ArrayList;

public class Fairy extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Fairy() {
        
        super(4, "Fairy", weaknesses, resistances);
        weaknesses.add(new Poison());
        weaknesses.add(new Steel());
        resistances.add(new Fighting());
        resistances.add(new Bug());
        resistances.add(new Dark());

    }

}