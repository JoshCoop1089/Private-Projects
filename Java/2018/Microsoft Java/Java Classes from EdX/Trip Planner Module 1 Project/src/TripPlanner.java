import java.util.Scanner;
public class TripPlanner {
    public static void main(String[] args) {
        NameAndPlace();
        MoneyAndLength();
        TimeDifference();
        CountryArea();
    }

    public static void NameAndPlace() {
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to Vacation Planner!");
        System.out.print("What is your name? ");
        String name = input.nextLine();

        System.out.print("Nice to meet you " + name + ", where are you travelling to? ");
        String destination = input.nextLine();

        System.out.println("Great! " + destination + " sounds like a great trip");
        Stars();
        }

    public static void MoneyAndLength() {
        Scanner input = new Scanner(System.in);

        System.out.print("How many days are you going to spend travelling? ");
        int days = input.nextInt();

        System.out.print("How much money, in USD, are you planning to spend on your trip? ");
        int money = input.nextInt();

        System.out.print("What is the three letter currency symbol for your travel destination? ");
        String countryCode = " "+input.next();

        System.out.print("How many"+countryCode+" are there in 1 USD? ");
        double conversion = input.nextDouble();

        int hours = days*24;
        int minutes = hours*60;
        System.out.println("\nIf you are travelling for " +days+ " days that is the same as "
                +hours+" hours or "+minutes+" minutes");

        double perDiem = (double)money / days;
        double moneyPerDay = ((double) ((int) (perDiem*100)))/100.0;
        System.out.println("If you are going to spend $"+money+" USD that means per day you can spend up to $"
                +moneyPerDay+" USD");

        double localMoneys = conversion*money;
        double localMoney = ((double) ((int) (localMoneys*100)))/100.0;
        double localPerDiem = localMoneys / days;
        localPerDiem = ((double) ((int) (localPerDiem*100)))/100.0;
        System.out.println("Your total budget in"+countryCode+" is "+localMoney+countryCode+
                ", which per day is "+localPerDiem+countryCode);
        Stars();
    }

    public static void TimeDifference() {
        Scanner input = new Scanner(System.in);
        System.out.print("What is the time difference, in hours, between your home and your destination? ");
        int timeDifference = input.nextInt();

        int midnightChanged = (24+timeDifference)%24;
        int noonChanged = (12+timeDifference)%24;
        System.out.println("This means that when it is midnight at home it will be "+midnightChanged+":00 in" +
                " your travel destination\nand when it is noon at home it will be "+noonChanged+":00");
        Stars();
    }

    public static void CountryArea() {
        Scanner input = new Scanner(System.in);
        System.out.print("What is the square area of the destination country in km2? ");
        double sqKilo = input.nextDouble();
        double conversion = 0.386102;
        double sqMiles = sqKilo*conversion;
        sqMiles = ((double) ((int) (sqMiles*100)))/100.0;

        System.out.println("In miles2 that is "+sqMiles);
        Stars();
    }

    public static void Stars() {
        System.out.println("**********\n");
    }
}
