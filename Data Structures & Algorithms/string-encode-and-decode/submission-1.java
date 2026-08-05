class Solution {

    public String encode(List<String> strs) {
        String encodedString = "";
        for (int i = 0; i < strs.size(); i++) {
            encodedString += strs.get(i).length() + "*" + strs.get(i);
        }
        return encodedString;
    }

    public List<String> decode(String str) {

        ArrayList<String> decoded = new ArrayList<>();

        int i = 0;
        while (i < str.length()) {
            
            int j = i;

            while (str.charAt(j) != '*') {
                j++;
            }

            int length = Integer.parseInt(str.substring(i, j));

            i = j + 1;
            j += length + 1;

            decoded.add(str.substring(i, j));

            i = j;
            
        }

        return decoded;
    }
}
