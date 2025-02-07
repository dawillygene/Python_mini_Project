PSEUDOCODE :
START
    DEFINE function encrypt(text, shift)
        INITIALIZE encrypted_text as empty string
        FOR each character in text
            IF character is a letter
                DETERMINE new shifted character
                ADD shifted character to encrypted_text
            ELSE
                ADD character to encrypted_text unchanged
        RETURN encrypted_text

    DEFINE function decrypt(text, shift)
        CALL encrypt function with negative shift value
        RETURN decrypted text

    GET user input for plaintext
    GET user input for shift value
    CALL encrypt function and display encrypted text
    CALL decrypt function and display decrypted text
END


Step 2: Algorithm
1.Define an encrypt function that takes text and shift as input.

2.Loop through each character in the text:
  If it's a letter, shift it by the given amount.
  If it's not a letter, keep it unchanged.
3.Define a decrypt function, which calls encrypt with a negative shift.

4.Take user input for a message and shift value.
5.Encrypt and display the ciphertext.
6.Decrypt and display the original text



User Input:

Enter the text to encrypt: My name is dawilly gene!
Enter shift value: 12