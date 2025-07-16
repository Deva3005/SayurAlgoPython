'''

Encode the Sentence 
    if the word in Odd'th position move each letter to next nth letter by forward
    if the word in Even'th position move each letter to next nth letter by forward + Reverse the word
    return all

Extra
1) Decode the Sentence ✅
2) Use File Instead of Sentence...✅

abcdefghijklmnoopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

'''
import string

al = string.ascii_lowercase
au = string.ascii_uppercase

def _00_fix_indexOutOfRange(keyToEncode:int,index:int)->int:
    if index+keyToEncode >= len(al):
        index = (index + keyToEncode)-len(al)-2
    if index+keyToEncode < 0:
        index = len(al) + (index-keyToEncode)
    return index+keyToEncode

def _00_reverse_word(word:str)->str:
    return word[::-1]

def _01_encode_word(encodeKey:int,word:str)->str:
    tmp=""
    for i in word:
        
        if i in al:
            jumpIndex = _00_fix_indexOutOfRange(encodeKey, al.find(i))
            tmp+=al[jumpIndex]
        elif i in au:
            jumpIndex = _00_fix_indexOutOfRange(encodeKey, au.find(i))
            tmp+=au[jumpIndex]
        else:
            # To Handle Special Characters
            tmp+=i
    return tmp

def _02_encodingFunction(keyToEncode:int,sentence:str)->str:
    result=[]
    for i,word in enumerate(sentence.split()):
        if(i%2!=0):
            result.append(_01_encode_word(keyToEncode,word))
        else:
            result.append(_01_encode_word(keyToEncode,_00_reverse_word(word)))
    return " ".join(result)

def _03_decode_word(encodeKey:int,word:str)->str:
    tmp=""
    for i in word:
        if i in al:
            tmp+=al[al.find(i)-encodeKey]
        elif i in au:
            tmp+=au[au.find(i)-encodeKey]
        else:
            tmp+=i
    return tmp

def _04_decodingFunction(keyToEncode:int,sentence:str)->str:
    decodeResult=[]
    for i,word in enumerate(decode_sentence.split()):
        if(i%2==0):
            decodeResult.append(_03_decode_word(keyToEncode,word))
        else:
            decodeResult.append(_03_decode_word(keyToEncode,_00_reverse_word(word)))
    return " ".join(decodeResult)

if __name__ == "__main__":
    # Test the encoding and decoding functions
    keyToEncode = 2
    
    sampleFile = open("index.html", "r")
    sentence = sampleFile.read()
    print(sentence)
    
    encoded = _02_encodingFunction(keyToEncode, sentence)
    
    encodeFile=open("advpy_test01_encoded.txt", "w")
    encodeFile.write(encoded)
    encodeFile.close()
    
    print(f"Encoded: {encoded}")
    sampleFile.close()
    
    # decode_sentence="K oc vjg ipkM"
    decode_sentence=encoded
    decoded = _04_decodingFunction(keyToEncode,decode_sentence)
    decodeFile = open("advpy_test01_decoded.txt","w")
    decodeFile.write(decoded)
    decodeFile.close()
    print(f"Decoded: {decoded}")