import java.util.*;

public class Pattern19 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter number of rows: ");
        int n=sc.nextInt();

        for(int i=0; i<n; i++){

            for(int j = n-i; j > 0; j--){
                System.out.print("*");
            }

            for(int k=0; k<=i*2; k++){
                System.out.print(" ");
            }
            

            for(int j = n-i; j > 0; j--){
                System.out.print("*");
            }

            System.err.println();
        }

        for(int i=n-1; i>=0; i--){

            for(int j = n-i; j > 0; j--){
                System.out.print("*");
            }

            for(int k=0; k<=i*2; k++){
                System.out.print(" ");
            }
            

            for(int j = n-i; j > 0; j--){
                System.out.print("*");
            }

            System.err.println();
        }

        sc.close();
        
    }
    
}
