package practice_projects;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;



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

		s.insert(3);
		s.insert(4);
		s.insert(4);
		s.insert(1);
		s.remove(3);
		s.getRandom();
		
		Store p = new Store();

		p.insert(5);
		p.insert(9);
		p.insert(9);
		p.insert(2);
		p.remove(9);
		p.getRandom();
        
    }


	// insert value into list of values + insert value into map as key, with index as 'value' 
	// also, no duplicates
	public void insert(int value) {

		if(values.contains(value)) return;

		this.values.add(value);
		this.map.put(value,this.values.size() - 1);

		// printing for testing and examples
		// System.out.println("\nAdded " + value + " to the list and map.");
		this.printValues();
		// System.out.println("Map: " + s.map.toString());

	}


	public void remove(int value) {

		if(!(values.contains(value))) {
			System.out.println("\n" + value + " not found in values.");
			return;
		}

		// init elements to be swapped (swapping to lastIndex and then popping as to make shifting unnecessary)
		int lastIndex = this.values.size()-1;
		int index = this.map.get(value);
		int temp_val = this.values.get(lastIndex);

		// replacing values
		this.values.set(lastIndex, value);
		this.values.set(index, temp_val);
		this.map.replace(temp_val, index);

		// removing values
		this.values.remove(lastIndex);
		this.map.remove(value);

		// sys.outs for testing
		// System.out.println("\n" + "Removed " + value + " from list and map.");
		// System.out.println(index + " " + temp_val);
		this.printValues();
		// System.out.println("Map: " + s.map.toString());		
	}


	// gets random element from Values
	public void getRandom() {
		Random rn = new Random();
		int randomIndex = rn.nextInt(this.values.size());

		System.out.println("Random element : " + this.values.get(randomIndex));
	}


	// c'mon...you know what it does
	public void printValues() {
		System.out.println("Values: " + this.values.toString());
	}	

}
