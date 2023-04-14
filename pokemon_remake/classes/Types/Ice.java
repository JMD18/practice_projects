package classes.Types;
import java.util.ArrayList;

public class Ice extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Ice() {
        
        super(7, "Ice", weaknesses, resistances);
        weaknesses.add(new Fire());
        weaknesses.add(new Fighting());
        weaknesses.add(new Rock());
        weaknesses.add(new Steel());
        resistances.add(new Ice());

    }

}