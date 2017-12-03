#hints for the various stages, only use this if all hope is lost:D

def hint(stage):
    try:
        r=hints[stage].next()
        return r
    except:
        return 'no more hints for this stage'


#example: hint(0) gives you the first hint for stage 0(the pcap), another call to hint(0) will give you the next hint for that stage, and so on...
#dont read below this line unless you want spoilers

































































hints = {
    0:['Analyze the pcap to understand how to talk with the server. If you are having difficulties finding the relevant conversation in the capture, look through the various tcp streams for odd-looking traffic.','If you send a message with proper credentials to the server, it will reply with a challenge that you need to decrypt. If the correct solution is sent back to the server you will be given credentials for the next stage(which is accessed in the same manner).', 'It is highly recommended that you make yourself an easy to use shell in order to interact with the server and analyze data.'],	
    1:['In this stage you need to decipher single-byte xor encrypted text.','Think of a way to automate the process of "guessing a key and checking whether the result makes sense". You can assume the original text is written in English.','Seeing non-printable characters in the decrypted text is a good indication that you used a bad key.'],
    2:['This time the key is not a single byte:)','Try to determine the key length first. It might change between sessions!', 'Read about Hamming distance(or edit distance, same same). A useful trait of it is that distance(a,b)==distance(a^X,b^X). Think how this can help you determine the key length. A different possible approach for finding the key length could be to compare two ciphertexts from different sessions, and deduce possible key lengths from some correlation between them.','After finding the key length, the next step is splitting the problem into a few simple single-byte xor cases and solving each of them separately.'],
    3:['The summer months are nice.', 'ROT??'],
    4:['This is a Vigenere cipher!','When there is so much ciphertext availble like in this stage, frequency analysis can yield very good results.'],
    5:['In this stage, what you send in the "morestuff" parameter is encrypted and then returned to you.','what is wrong with block ciphers?','Repetitions!'],
    6:['What happens when your data is 15 bytes long? try thinking about how the first encrypted block looks.','Find one byte of the appended data at a time by bruteforcing one unknown byte in an otherwise known block.'],
    7:['You just need a way to find the point where your data is starting, afterwards it is just like the previous level. The length of the prefix is random.', 'Spamming is nice!'],
    8:['You can use the morestuff parameter in the connection string to generate encrypted blocks of your choosing, just remember to align your data properly with multiples of the block size.','Remember that in ECB mode, each block is individually encrypted *and decrypted*.'],
    9:['What happens to block1 when you flip a bit in block0? and what happens to further blocks?', 'Try sending "almost" the data you REALLY want to send and alter it after encryption. You can do that in a way that will make the server decrypt specific bytes differently.'],
    10:['Last stage, no hints!\r\n\r\nFor real.'],
}

for i in hints:
    hints[i]=iter(hints[i])
