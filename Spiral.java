class Spiral {
	public static void main(String[] args) {
		int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
		int m = 4;
		int n = 3;
		createSpiral(arr, m, n);
	}

	private static void createSpiral(int[] arr, int m, int n) {
		int startM = startN = 0;
		int pos = 0;
		int[] result = [m * n];
		int side = 0;
		while (m != 0 && n != 0) {
			if (side % 4 == 0) {
				pos = fillRow(arr, result, pos, m, startN, true);
				startN++;
			} else if (side % 4 == 1) {
				pos = fillCol(arr, result, pos, n, m, true);
				m--;
			} else if (side % 4 == 2) {
				pos = fillRow(arr, result, pos, m, n, false);
				n--;
			} else {
				pos = fillCol(arr, result, pos, n, startM, false);
				startM++;
			}
			side++;
		}
	}

	private static int fillRow(int[] arr, int[] result, int pos, int lim, int row, boolean flag) {

		if (flag) {
			for (int i = 0; i < lim; i++) {
				
			}
		} else {

		}

	}

}