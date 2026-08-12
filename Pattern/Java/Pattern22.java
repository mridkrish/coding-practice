import java.util.*;

public class Pattern22 {

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);


        System.out.print("Enter the square matrix size: ");
        int n = sc.nextInt();

        for(int i = 0; i < (2 * n - 1); i++){
            
            for(int j = 0; j < (2 * n - 1); j++){

                int minDist = Math.min(Math.min(i, (2 * n - 2) - i), Math.min(j, (2 * n - 2) - j));

                System.out.print(n-minDist + " ");

            }

            System.out.println("");
        }
    }
}