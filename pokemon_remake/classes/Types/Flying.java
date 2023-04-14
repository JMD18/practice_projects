package classes.Types;
import java.util.ArrayList;

public class Flying extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Flying() {
        
        super(6, "Flying", weaknesses, resistances);
        weaknesses.add(new Electric());
        weaknesses.add(new Ice());
        weaknesses.add(new Rock());
        resistances.add(new Fighting());
        resistances.add(new Bug());
        resistances.add(new Grass());

    }

}