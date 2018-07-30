package justForReal;

public class PerfectNumber {
	public static boolean checkPerfectNumber(int num) {
		int high = (int) Math.sqrt(num);
		int result = 1;
		for (int i = 2; i < high + 1; i++) {
			if(num%i==0){
				result+=(i+num/i);
			}
		}
		return result == num;
	}
	public static void main(String[] args) {
		System.out.println(PerfectNumber.checkPerfectNumber(28));
		System.out.println('A'-'a');
		
	}
}
