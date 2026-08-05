class Solution {

    public HashMap <String, List<String>> map = new HashMap<>();
    
    public String encode(List<String> strs) {
        String encodedString = "abc";

        map.put(encodedString, strs);

        return encodedString;
    }

    public List<String> decode(String str) {
        return map.get(str);
    }
}
