package passphrase;

public class PassphraseEncoder {

    public static String encoder(String en){
        String[] strA = en.split("");
        StringBuilder stringBuilder = new StringBuilder();

        for(int i=0;i<strA.length;i++){
            if(strA[i].equals(strA[i].toUpperCase())){
                stringBuilder.append(strA[i].toLowerCase());
            }
            else if(strA[i].equals(strA[i].toLowerCase())){
                stringBuilder.append(strA[i].toUpperCase());
            }
            else{
                stringBuilder.append(strA[i]);
            }
        }
        String encode = stringBuilder.toString();
        return encode;
    }

    public static String decoder(String de){
        String[] strA = de.split("");
        StringBuilder stringBuilder = new StringBuilder();

        for(int i=0;i<strA.length;i++){
            if(strA[i].equals(strA[i].toLowerCase())){
                stringBuilder.append(strA[i].toUpperCase());
            }
            else if(strA[i].equals(strA[i].toUpperCase())){
                stringBuilder.append(strA[i].toLowerCase());
            }
            else{
                stringBuilder.append(strA[i]);
            }
        }
        String decode = stringBuilder.toString();
        return decode;
    }
}
