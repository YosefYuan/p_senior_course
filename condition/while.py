
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

