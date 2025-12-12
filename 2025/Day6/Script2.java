import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Script2 {

    private static String[] processLine(String line) {
        ArrayList<String> cellsList = new ArrayList<>();
        char[] characters = line.toCharArray();
        for (char c : characters) {
            if (Character.isWhitespace(c)) {
                cellsList.add("");
            } else {
                cellsList.add(String.valueOf(c));
            }
        }
        return cellsList.toArray(new String[0]);
    }

    private static long multiplication(ArrayList<Integer> numbers) {
        long result = 1;
        for (int n : numbers) {
            result *= n;
        }
        return result;
    }

    private static long sum(ArrayList<Integer> numbers) {
        long result = 0;
        for (int n : numbers) {
            result += n;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] firstLine = processLine(scanner.nextLine());
        String[] secondLine = processLine(scanner.nextLine());
        String[] thirdLine = processLine(scanner.nextLine());
        String[] fourthLine = processLine(scanner.nextLine());
        String[] operations = scanner.nextLine().trim().split("\\s+");
        scanner.close();

        int max = Arrays.stream(new int[] { firstLine.length, secondLine.length, thirdLine.length, fourthLine.length })
                .max().getAsInt();
        String[][] matrix = new String[4][max];
        matrix[0] = firstLine;
        matrix[1] = secondLine;
        matrix[2] = thirdLine;
        matrix[3] = fourthLine;

        int indexOperations = 0;
        long grandTotal = 0;
        ArrayList<Integer> numbers = new ArrayList<>();

        for (int k = 0; k < max; k++) {
            boolean columnaVacia = matrix[0][k].trim().isEmpty() &&
                    matrix[1][k].trim().isEmpty() &&
                    matrix[2][k].trim().isEmpty() &&
                    matrix[3][k].trim().isEmpty();
            if (!columnaVacia) {
                numbers.add(Integer.parseInt((matrix[0][k] + matrix[1][k] + matrix[2][k] + matrix[3][k]).trim()));
            } else {
                grandTotal += (operations[indexOperations].equals("*")) ? multiplication(numbers) : sum(numbers);
                indexOperations++;
                numbers = new ArrayList<>();
            }

        }

        grandTotal += (operations[indexOperations].equals("*")) ? multiplication(numbers) : sum(numbers);

        System.out.println(grandTotal);

    }
}