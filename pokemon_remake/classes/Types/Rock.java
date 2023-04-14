package classes.Types;
import java.util.ArrayList;

public class Rock extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Rock() {
        
        super(13, "Rock", weaknesses, resistances);
        weaknesses.add(new Water());
        weaknesses.add(new Grass());
        weaknesses.add(new Fighting());
        weaknesses.add(new Ground());
        weaknesses.add(new Steel());
        resistances.add(new Normal());
        resistances.add(new Flying());
        resistances.add(new Poison());
        resistances.add(new Fire());
        resistances.add(new Electric());
        
    }

}