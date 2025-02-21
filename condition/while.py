
while True:
    try:
        text = input('Please enter your question (or type "q" to exit): ')
        if text.lower() == 'q':  # Allows 'Q' or 'q' for exit
            print('Exiting system...')
            break
        print(f"You entered: {text}")
    except KeyboardInterrupt:
        print("\nUser interrupted the program. Exiting...")
        break  # Exit gracefully on Ctrl+C
    except Exception as err:
        print(f'An error occurred: {err}')

x = [1, 2, 3, 4, 5]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print(y)
print(y)