package classes.Types;
import java.util.ArrayList;

public class Steel extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Steel() {
        
        super(9, "Steel", weaknesses, resistances);
        weaknesses.add(new Fire());
        weaknesses.add(new Fighting());
        weaknesses.add(new Ground());
        resistances.add(new Normal());
        resistances.add(new Flying());
        resistances.add(new Poison());
        resistances.add(new Rock());
        resistances.add(new Bug());
        resistances.add(new Steel());

    }

}