package classes.Types;
import java.util.ArrayList;

public class Poison extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Poison() {
        
        super(8, "Poison", weaknesses, resistances);
        weaknesses.add(new Ground());
        weaknesses.add(new Psychic());
        resistances.add(new Fighting());
        resistances.add(new Poison());
        resistances.add(new Bug());

    }

}