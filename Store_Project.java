package practice_projects;

import java.util.*;


/*	Practice creating a class to go along with
 * 	YT coding interview found at the link below:
 * 
 * 	https://youtu.be/46dZH7LDbf8
 * 
 */

class Store {

	ArrayList<Integer> values = new ArrayList<Integer>();
    HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();

    public static void main(String[] args) {
        

		Store s = new Store();

		s.insert(s, 3);
		s.insert(s, 4);
		s.insert(s, 4);
		s.insert(s, 5);

		s.remove(s, 7);

		s.getRandom(s);
        
    }



	public void insert(Store s, int value) {
		if(values.contains(value)) return;

		s.values.add(value);
		s.map.put(value,s.values.size() - 1);

		// System.out.println("\nAdded " + value + " to the map.");
		// System.out.println("Values: " + s.values.toString());
		// System.out.println("Map: " + s.map.toString());

	}

	public void remove(Store s, int value) {
		if(!(values.contains(value))) {
			System.out.println("\n" + value + " not found in values.");
			// System.out.println("Values: " + s.values.toString());
			// System.out.println("Map: " + s.map.toString());


			return;
		}

	}

	public void getRandom(Store s) {

	}


}