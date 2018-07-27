package justForReal;

import java.util.Arrays;

public class test1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	public int findContentChildren(int[] g, int[] s) {
		Arrays.sort(g);
		Arrays.sort(s);
		int i=0;
		for(int j=0;i<g.length&&i<s.length;j++){
			if(g[i]<=s[j]){
				i++;
			}
		}
		return i;
	}

}
