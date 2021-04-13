import random
import string


email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'hotmail.co.uk',
                 'hotmail.fr', 'msn.com', 'yahoo.fr', 'yandex.ru', 'outlook.com', 'yahoo.co.uk',
                 'live.com', 'yahoo.co.in', 'mail.ru', 'live.fr']


# function generate random text combaining different lower cases and digits
# string_length is the length of the string
def generate_random_string(string_length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=string_length))


# N: number of emails you want to generate
def generate_emails(N):
    for _ in range(N):

        # we generate random length
        prefix_length = random.randint(8, 20)

        # call the function to generate random email prefix
        email_prefix = generate_random_string(prefix_length)

        # generate random email suffix from the email_domains list above
        email_suffix = random.choice(email_domains)

        # print the output generated email
        generated_email = f'{email_prefix}@{email_suffix}'

        print(generated_email)

        # store each email in file called fake_emails.txt
        with open('fake_emails.txt', 'a+') as f:
            f.write(generated_email + '\n')


if __name__ == '__main__':
    while True:
        try:
            print("How many email addresses do you want to generate?")
            nb_emails = int(input(">> "))
        except ValueError:
            print("Please Enter a valid Integer number!!\n")
        except Exception as e:
            raise
        else:
            generate_emails(nb_emails)
            break


print('\n[+] DONE [+]\n')
