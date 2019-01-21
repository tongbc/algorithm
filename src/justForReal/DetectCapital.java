package justForReal;

public class DetectCapital {
	public  boolean detectCapitalUse(String word) {
		if(word.length()==1) return true;
		if(word.length()==2&&(isUpper(word.charAt(0))||((!isUpper(word.charAt(0)))&&(!isUpper(word.charAt(1)))))){
			return true;
		}
		
		if (!isUpper(word.charAt(0))) {
			for (int i = 1; i < word.length(); i++) {
				if (isUpper(word.charAt(i))) {
					return false;
				}
			}
		} else {
			if (!isUpper(word.charAt(1))) {
				for (int i = 2; i < word.length(); i++) {
					if (isUpper(word.charAt(i))) {
						return false;
					}
				}
			} else {
				for (int i = 2; i < word.length(); i++) {
					if (!isUpper(word.charAt(i))) {
						return false;
					}
				}
			}
		}
		return true;
	}

	public boolean isUpper(char ch) {
		if (ch - 'A' > 31) {
			return false;
		} else {
			return true;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DetectCapital temp = new DetectCapital();
		System.out.println(temp.detectCapitalUse("usa"));

	}

}
