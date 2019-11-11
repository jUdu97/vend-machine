//create array of snack items with associated prices

//ask user for valid input on what snack they want to check the price on

//confirm if choice is what user wants

//display price, subtract amount given by user until paid

import java.util.*;

/* class for vending machine with various snacking choices */
class vendMach {
	//string array of snack items
	String snackArray[] = 
		{"Oreo Pack", "Cheez-its", "Snickers", 
		"Fudge Rounds", "Twizzlers", "Sour Patch Kids", 
		"Skittles", "M & Ms", "Babe Ruth", 
		"Hubba Bubba", "Snickers", "Slim Jim", 
		"Hot Cheetos", "5 Gum", "Animal Crackers"};
	
	//string array of snack index codes
	String indexArray[] = 
		{"A1", "A2", "A3", 
		"B1", "B2", "B3", 
		"C1", "C2", "C3", 
		"D1", "D2", "D3", 
		"E1", "E2", "E3"};
	
	//double array of snack prices
	double priceArray[] = 
		{2.25, 1.75, 1.25, 
		3.25, 1.25, 2.25, 
		2.75, 1.25, 0.75, 
		1.25, 2.75, 3.25, 
		1.75, 1.25, 2.25};
	
	//method that chooses a snack and returns a corresponding price
	static class choosing extends vendMach {
		
		public String checkSnac() {
			//print out options with snack codes
			System.out.println("Barrington Vending Machine\n");
			System.out.println("-----------------------------------------------------------------------\n");
			
			for (int i = 0; i < 3; i++) {
				System.out.printf("%-20s\t", snackArray[i] + " (" + indexArray[i] + ")");
		    }
			System.out.println("\n");
			for (int j = 3; j < 6; j++) {
		    	System.out.printf("%-20s\t", snackArray[j] + " (" + indexArray[j] + ")");
		    }
			System.out.println("\n");
			for (int k = 6; k < 9; k++) {
		    	System.out.printf("%-18s\t", snackArray[k] + " (" + indexArray[k] + ")");
		    }
			System.out.println("\n");
			for (int m = 9; m < 12; m++) {
		    	System.out.printf("%-18s\t", snackArray[m] + " (" + indexArray[m] + ")");
		    }
			System.out.println("\n");
			for (int p = 12; p < 15; p++) {
		    	System.out.printf("%-18s\t", snackArray[p] + " (" + indexArray[p] + ")");
		    }
			System.out.println("\n-----------------------------------------------------------------------\n");
			System.out.println("ONLY ACCEPTS QUARTERS ($0.25)!");
			System.out.println("\n-----------------------------------------------------------------------\n");
			
			//ask user what snack they want
			Scanner askSnak = new Scanner(System.in);  
		    String getSnak;
		    Boolean chkMsg;
		    
		    //loop condition for checking if snack code is valid
		    do {
		    	System.out.println("What snack do you want?: ");
			    getSnak = askSnak.nextLine();
			    chkMsg = Arrays.asList(indexArray).contains(getSnak);
			    if (chkMsg == true) {
			    	break;
			    }
		    	
		    } while (chkMsg == false);
		    
		    //confirm with user it is the snack they want
		    Scanner confirmSnak = new Scanner(System.in);
		    String verifSnak;
		    
		    Boolean chkMsg2 = Arrays.asList(indexArray).contains(getSnak);
		    String choiceMsg2="";
		    
		    //loop condition for confirmation of snack
		    do {
			    System.out.println("Confirm (Y/N)?: ");
			    verifSnak = confirmSnak.nextLine();
			    
			    if (verifSnak == "Y") {
			    	break;
			    }
		    } while (verifSnak.equals("N"));
		    
		    choiceMsg2 += "Your snack choice: " + getSnak + "was vended."; //print out snack choice
		    
		    //if ... else if choice in snack array
		    if (chkMsg2 == true) {
		    	pricing snkPrice = new pricing();
			    snkPrice.amountChk(getSnak);
			    choiceMsg2 += "\nEnjoy!";
		    } else {
		    	choiceMsg2 += "None";
		    }
		   
		    askSnak.close(); //close askSnak scanner
		    confirmSnak.close(); //close confirmSnak scanner
		    
		    return choiceMsg2; //return snack choice and price;
		    
		}//end checking snack method
	}//end choosing class 
	
	static class pricing extends vendMach {
		public void amountChk (String snChk) {
			//get index of chosen snack code
			int dolIndex = Arrays.asList(indexArray).indexOf(snChk);
			
			//get price of chosen snack price
			double priceAmt = priceArray[dolIndex];
			
			//print out price of chosen snack
			String priceMsg = "Price: $" + priceAmt;
			System.out.println(priceMsg);
			
			//ask user to input quarters 
			Scanner askSnak2 = new Scanner(System.in);
			String amtMsg = "Amount: $"; 
			System.out.println(amtMsg); //print string asking for user amount
			double amtSnak = askSnak2.nextDouble(); //get user input for payment
			double chgAmt = priceAmt - amtSnak; //get change from user input
			System.out.println(String.format("You need: $%.2f", chgAmt));
			
			//loop for user input if not equal to price
			do {
				System.out.println(amtMsg);
				amtSnak = askSnak2.nextDouble();
				double newPrice = chgAmt - amtSnak;
				
				chgAmt = newPrice;
				System.out.println(String.format("You need: $%.2f", chgAmt));
				
				if (chgAmt == 0.0) {
					break;
				}//break statement
			} while (chgAmt !=0); //end while loop
			
		    askSnak2.close();
		    
		}//end of amountChk method
	}//end pricing class 
	
	//start main
	public static void main (String[] args) {
		//create instance of choosing class
		choosing choice1 = new choosing();
		
		//print out chosen snack
		System.out.println(choice1.checkSnac());
		
	}//end main
}

//Sources
//https://www.w3schools.com/java/java_user_input.asp
//https://www.javatpoint.com/substring
//https://www.geeksforgeeks.org/scanner-class-in-java/
//https://javadevnotes.com/java-double-to-string-2-decimal-places-examples
 