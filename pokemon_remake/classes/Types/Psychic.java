package classes.Types;
import java.util.ArrayList;

public class Psychic extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();
    static ArrayList<Types> immunities = new ArrayList<Types>();

    public Psychic() {
        
        super(16, "Psychic", weaknesses, resistances, immunities);
        weaknesses.add(new Bug());
        weaknesses.add(new Ghost());
        weaknesses.add(new Dark());
        resistances.add(new Fighting());
        resistances.add(new Psychic());
        immunities.add(new Psychic());

    }

}