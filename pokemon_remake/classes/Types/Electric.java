package classes.Types;
import java.util.ArrayList;

public class Electric extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Electric() {
        
        super(5, "Electric", weaknesses, resistances);
        weaknesses.add(new Ground());
        weaknesses.add(new Water());
        resistances.add(new Electric());
        resistances.add(new Flying());
        resistances.add(new Steel());

    }

}