# Password Generator

This is a simple Python script that generates random passwords. It allows you to customize the length of the password and decide whether to include digits and special characters. This script can be useful for creating secure passwords for various purposes.

## How to Use

1. Make sure you have Python installed on your system.

2. Download the `password_generator.py` script.

3. Open your terminal or command prompt.

4. Navigate to the directory where the `password_generator.py` script is located.

5. Run the script by entering the following command:

   ```shell
   python password_generator.py
   ```

6. Follow the prompts to customize your password:

   - You can specify the length of the password. The default length is 12 characters, but you can enter your desired length.
   
   - You can choose to include digits in the password by typing 'y' for yes or 'n' for no.
   
   - You can also choose to include special characters in the password by typing 'y' for yes or 'n' for no.

7. After you have answered the prompts, the script will generate a random password and display it on the screen.

## Customization

You can easily modify this script to fit your needs. Here are some ways you can customize it:

- **Change the Default Password Length**: You can change the default password length by modifying the `default_length` variable in the `generate_password` function.

- **Change the Character Sets**: You can modify the character sets used for password generation. For example, you can add or remove characters from `string.digits` or `string.punctuation` as needed.

- **Customize the User Prompts**: You can change the user prompts and messages in the `main` function to make them more user-friendly or informative.

