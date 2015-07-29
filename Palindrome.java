class Palindrome {
	public static void main(String[] args) {
		for (int i = 0; i < args.length; i++) {
			System.out.println(args[i]);
			System.out.println(isPalindrome(args[i]));
		}
	}

	private static boolean isPalindrome(String str) {
		String reverseStr = reverse(str);
		return reverseStr.equals(str);
	}

	private static String reverse(String str) {
		String result = "";
		for (int i = str.length() - 1; i >= 0; i--) {
			result += str.charAt(i);
		}
		return result;
	}
}