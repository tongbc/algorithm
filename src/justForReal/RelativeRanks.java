package justForReal;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class RelativeRanks {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1,2,3};
		System.out.println(RelativeRanks.findRelativeRanks(nums));
	}
	
	public static String[] findRelativeRanks(int[] nums) {
		String[] result = new String[nums.length];
        int[] tmp = Arrays.copyOf(nums, nums.length);
        Arrays.sort(tmp);
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = tmp.length - 1; i >= 0; i--) {
            // score -> ranking
            map.put(tmp[i], tmp.length - i);
        }


        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) == 1) {
                result[i] = "Gold Medal";
            } else if (map.get(nums[i]) == 2) {
                result[i] = "Silver Medal";
            } else if (map.get(nums[i]) == 3) {
                result[i] = "Bronze Medal1";
            } else {
                result[i] = String.format("%s", map.get(nums[i]));
            }
        }
        return result;
	}
}
